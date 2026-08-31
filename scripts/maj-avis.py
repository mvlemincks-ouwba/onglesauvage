#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Met à jour la section « avis » du site depuis la fiche Booksy d'Ongle Sauvage.

Le script lit la page publique Booksy, en extrait la note, le nombre d'avis et
les avis les plus récents, puis réécrit directement le HTML du site :

  - le bloc de cartes entre les repères <!-- avis:start --> et <!-- avis:end -->
  - les compteurs balisés <span data-avis-rating> et <span data-avis-count>
  - "ratingValue" et "reviewCount" dans les données structurées JSON-LD

Le site reste donc entièrement statique : aucun JavaScript n'est nécessaire
côté visiteur pour afficher les avis.

Usage :
    python3 scripts/maj-avis.py            # met à jour les fichiers trouvés
    python3 scripts/maj-avis.py --check    # n'écrit rien, affiche ce qui changerait

Le script échoue (code de sortie 1) sans rien écrire si l'extraction donne un
résultat manifestement cassé : le site conserve alors sa dernière version valide.
"""

import argparse
import html
import json
import os
import re
import sys
import urllib.error
import urllib.request

URL = os.environ.get("BOOKSY_URL", "https://booksy.com/fr-fr/"
                     "62614_ongle-sauvage_onglerie_80506_castillon-de-castets")

# Pages du site à mettre à jour (celles qui existent sont traitées).
CIBLES = ("index.html", "v2.html")

# Garde-fous : en dessous de ce nombre d'avis extraits, on considère que la
# structure de la page Booksy a changé et on préfère ne rien écrire.
MIN_AVIS = 3
MAX_CARTES = 12          # nombre de cartes affichées dans le carrousel
LONGUEUR_EXTRAIT = 175   # au-delà, le texte est coupé en fin de phrase

# Libellés de prestation : réécriture pour l'affichage sur le site.
# Une valeur vide masque le libellé (ex. « dépose », qui n'est pas ce que
# l'avis met en avant et prêterait à confusion sous une carte élogieuse).
LIBELLES = (
    (re.compile(r"^Dépose\b", re.I), ""),
    (re.compile(r"^Semi permanent\b", re.I), "Semi-permanent"),
)

UA = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
      "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")


class ExtractionCassee(RuntimeError):
    """La page Booksy ne ressemble plus à ce que le script sait lire."""


class PageNonBalisee(RuntimeError):
    """La page HTML ne contient pas les repères de mise à jour."""


# --------------------------------------------------------------------------- #
# Récupération et extraction
# --------------------------------------------------------------------------- #

def telecharge(url=URL):
    requete = urllib.request.Request(url, headers={
        "User-Agent": UA,
        "Accept-Language": "fr-FR,fr;q=0.9",
    })
    with urllib.request.urlopen(requete, timeout=45) as reponse:
        brut = reponse.read()
    return brut.decode("utf-8", errors="replace")


def note_et_total(page):
    """Note moyenne et nombre total d'avis, lus dans le JSON-LD de Booksy."""
    bloc = re.search(
        r'<script[^>]*application/ld\+json[^>]*>(\{"@context".*?"@type":"NailSalon".*?)</script>',
        page, re.S)
    if not bloc:
        raise ExtractionCassee("bloc JSON-LD NailSalon introuvable")
    try:
        donnees = json.loads(bloc.group(1))
    except json.JSONDecodeError as erreur:
        raise ExtractionCassee("JSON-LD illisible : %s" % erreur)

    agregat = donnees.get("aggregateRating") or {}
    note = agregat.get("ratingValue")
    total = agregat.get("reviewCount")
    if note is None or total is None:
        raise ExtractionCassee("aggregateRating incomplet")
    return float(note), int(total)


def nettoie(texte):
    """Décode les entités, réduit les espaces, supprime les retours à la ligne."""
    texte = html.unescape(texte)
    texte = texte.replace(" ", " ")
    texte = re.sub(r"\s+", " ", texte)
    return texte.strip()


def libelle_prestation(brut):
    """Normalise le libellé Booksy, ou renvoie une chaîne vide s'il faut le masquer."""
    for motif, remplacement in LIBELLES:
        if motif.search(brut):
            if not remplacement:
                return ""
            return motif.sub(remplacement, brut, count=1)
    return brut


# Booksy sert dans le corps de la carte une version raccourcie de l'avis,
# terminée par « ... », et n'affiche le texte intégral qu'après un clic. Ce
# texte complet est toutefois présent ailleurs dans la page (données
# structurées et données de rendu) : on va l'y rechercher.
FIN_TRONQUEE = re.compile(r"\s*(?:\.\.\.|…)\s*$")


def texte_complet(tronque, page):
    """Retrouve la version intégrale d'un avis tronqué par Booksy.

    Renvoie le texte le plus long trouvé dans la page, ou le texte tronqué
    d'origine (nettoyé de ses points de suspension) si la recherche échoue.
    """
    prefixe = FIN_TRONQUEE.sub("", tronque)
    mots = [re.escape(mot) for mot in prefixe.split() if mot]
    if len(mots) < 4:
        return prefixe
    # Les espaces peuvent apparaître comme retours à la ligne échappés (\n)
    # selon l'endroit de la page où le texte est stocké.
    motif = re.compile(r"(?:\s|\\n|\\r|\\t)+".join(mots))

    meilleur = prefixe
    for trouve in motif.finditer(page):
        segment = lit_chaine(page, trouve.start())
        if segment and len(segment) > len(meilleur):
            meilleur = segment
    return meilleur


def lit_chaine(page, depart):
    """Lit une chaîne à partir de `depart` jusqu'au guillemet non échappé suivant."""
    i = depart
    limite = min(len(page), depart + 4000)
    while i < limite:
        if page[i] in "<>":
            # On est tombé dans le balisage HTML : ce n'est pas la copie
            # intégrale de l'avis, on abandonne ce candidat.
            return None
        if page[i] == '"' and page[i - 1] != "\\":
            brut = page[depart:i]
            try:
                texte = nettoie(json.loads('"%s"' % brut))
            except (json.JSONDecodeError, ValueError):
                return None
            return None if FIN_TRONQUEE.search(texte) else texte
        i += 1
    return None


def extraits_avis(page):
    """Liste d'avis : prénom, prestation, texte. Ordre = du plus récent au plus ancien."""
    blocs = page.split('data-testid="review-item"')[1:]
    avis = []
    for bloc in blocs:
        auteur = re.search(r'data-testid="review-author"[^>]*>([^<]+)<', bloc)
        corps = re.search(r'data-testid="review-body"[^>]*><span>(.*?)</span>', bloc, re.S)
        if not auteur or not corps:
            continue
        texte = nettoie(re.sub(r"<[^>]+>", " ", corps.group(1)))
        if not texte:
            continue
        if FIN_TRONQUEE.search(texte):
            texte = texte_complet(texte, page)
        prestations = [nettoie(p) for p in
                       re.findall(r'data-testid="review-service"[^>]*>([^<]*?)<', bloc)]
        prestations = [p for p in prestations if p]
        avis.append({
            "nom": nettoie(auteur.group(1)),
            "prestation": libelle_prestation(prestations[0]) if prestations else "",
            "texte": texte[0].upper() + texte[1:],
        })
    if len(avis) < MIN_AVIS:
        raise ExtractionCassee("%d avis extraits, minimum attendu %d" % (len(avis), MIN_AVIS))
    return avis


# --------------------------------------------------------------------------- #
# Mise en forme
# --------------------------------------------------------------------------- #

def extrait(texte, limite=LONGUEUR_EXTRAIT):
    """Raccourcit un avis trop long en s'arrêtant sur une fin de phrase."""
    if len(texte) <= limite:
        return texte
    fenetre = texte[:limite + 1]
    coupe = max(fenetre.rfind(". "), fenetre.rfind("! "), fenetre.rfind("? "))
    if coupe >= limite * 0.5:
        return texte[:coupe + 1].strip()
    coupe = fenetre.rfind(" ")
    return texte[:coupe].rstrip(" ,;:") + "…"


def carte(avis):
    nom = html.escape(avis["nom"], quote=False)
    texte = html.escape(extrait(avis["texte"]), quote=False)
    presta = html.escape(avis["prestation"], quote=False)
    ligne_presta = ('\n          <div class="review-service">%s</div>' % presta) if presta else ""
    return ("""        <article class="review">
          <div class="quote">&ldquo;</div>
          <p>%s</p>
          <div class="review-name">%s</div>%s
        </article>""" % (texte, nom, ligne_presta))


def bloc_cartes(avis):
    cartes = "\n".join(carte(a) for a in avis[:MAX_CARTES])
    return ('      <div class="reviews-rail" id="reviewsRail" tabindex="0" role="group"'
            ' aria-label="Avis clientes, défilement horizontal">\n'
            + cartes + "\n      </div>")


def note_fr(note):
    """5.0 -> « 5,0 »."""
    return ("%.1f" % note).replace(".", ",")


# --------------------------------------------------------------------------- #
# Réécriture du HTML
# --------------------------------------------------------------------------- #

def applique(source, avis, note, total):
    resultat = source

    debut = resultat.find("<!-- avis:start")
    fin = resultat.find("<!-- avis:end -->")
    if debut == -1 or fin == -1 or fin < debut:
        raise PageNonBalisee("repères <!-- avis:start --> / <!-- avis:end --> absents")
    ouverture = resultat.find("-->", debut) + len("-->")
    resultat = resultat[:ouverture] + "\n" + bloc_cartes(avis) + "\n      " + resultat[fin:]

    resultat = re.sub(r"(<span data-avis-count>)[^<]*(</span>)",
                      lambda m: m.group(1) + str(total) + m.group(2), resultat)
    resultat = re.sub(r"(<span data-avis-rating>)[^<]*(</span>)",
                      lambda m: m.group(1) + note_fr(note) + m.group(2), resultat)

    resultat = re.sub(r'("ratingValue":\s*")[^"]*(")',
                      lambda m: m.group(1) + ("%.1f" % note) + m.group(2), resultat)
    resultat = re.sub(r'("reviewCount":\s*")[^"]*(")',
                      lambda m: m.group(1) + str(total) + m.group(2), resultat)

    return resultat


def main():
    analyseur = argparse.ArgumentParser(description=__doc__,
                                        formatter_class=argparse.RawDescriptionHelpFormatter)
    analyseur.add_argument("--check", action="store_true",
                           help="n'écrit rien, indique seulement ce qui changerait")
    analyseur.add_argument("--fichier", action="append", dest="fichiers",
                           help="page à mettre à jour (par défaut : index.html et v2.html)")
    options = analyseur.parse_args()

    try:
        page = telecharge()
    except (urllib.error.URLError, urllib.error.HTTPError, OSError) as erreur:
        print("Échec du téléchargement de la fiche Booksy : %s" % erreur, file=sys.stderr)
        return 1

    try:
        note, total = note_et_total(page)
        avis = extraits_avis(page)
    except ExtractionCassee as erreur:
        print("Extraction impossible : %s" % erreur, file=sys.stderr)
        print("La page Booksy a probablement changé de structure. "
              "Le site n'a pas été modifié.", file=sys.stderr)
        return 1

    print("Booksy : note %s sur %d avis, %d avis récupérés"
          % (note_fr(note), total, len(avis)))

    cibles = options.fichiers or [f for f in CIBLES if os.path.exists(f)]
    if not cibles:
        print("Aucune page à mettre à jour (index.html / v2.html introuvables)", file=sys.stderr)
        return 1

    modifies = []
    balisees = 0
    for chemin in cibles:
        if not os.path.exists(chemin):
            print("  %s : introuvable, ignoré" % chemin)
            continue
        with open(chemin, encoding="utf-8") as fichier:
            source = fichier.read()
        try:
            nouveau = applique(source, avis, note, total)
        except PageNonBalisee:
            print("  %s : pas de repères d'avis, ignoré" % chemin)
            continue
        balisees += 1
        if nouveau == source:
            print("  %s : déjà à jour" % chemin)
            continue
        if options.check:
            print("  %s : serait mis à jour" % chemin)
        else:
            with open(chemin, "w", encoding="utf-8") as fichier:
                fichier.write(nouveau)
            print("  %s : mis à jour" % chemin)
        modifies.append(chemin)

    if balisees == 0:
        print("Aucune page balisée : ajoutez les repères <!-- avis:start --> et "
              "<!-- avis:end --> autour du carrousel.", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
