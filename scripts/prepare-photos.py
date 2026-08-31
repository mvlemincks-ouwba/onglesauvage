#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Prépare des photos de téléphone pour le site : redimensionne, compresse, nettoie.

Une photo d'iPhone pèse 2 à 4 Mo : publiée telle quelle, elle rend la page très
lente sur mobile. Ce script la ramène à une taille raisonnable et supprime au
passage toutes les métadonnées (dont la position GPS, souvent présente sur les
photos prises au téléphone).

Ce qu'il fait pour chaque image :
  - applique la rotation indiquée par l'EXIF, puis l'oublie (une photo prise en
    portrait reste droite même si le navigateur ignore la métadonnée) ;
  - réduit le grand côté à --max-cote pixels maximum (jamais d'agrandissement) ;
  - réenregistre en JPEG progressif optimisé, sans aucune métadonnée.

Usage :
    python3 scripts/prepare-photos.py source.jpeg=assets/nom-final.jpg [...]
    python3 scripts/prepare-photos.py --max-cote 1600 --qualite 80 src=dest
    python3 scripts/prepare-photos.py --crop 0.08,0.16,0.74,0.74 src=dest

L'option --crop recadre avant le redimensionnement, en fractions de l'image
d'origine (x,y,largeur,hauteur, entre 0 et 1). Elle sert à zoomer sur le
sujet quand la photo laisse trop de vide autour — utile pour les vignettes.

Exemple :
    python3 scripts/prepare-photos.py \\
        ~/Downloads/IMG_0176.jpeg=assets/nailart-alice.jpg
"""

import argparse
import os
import sys

try:
    from PIL import Image, ImageOps
except ImportError:
    print("Pillow est nécessaire : python3 -m pip install Pillow", file=sys.stderr)
    sys.exit(1)

MAX_COTE = 1400
QUALITE = 78


def gps_present(image):
    """Indique si l'image transporte des coordonnées GPS."""
    try:
        exif = image.getexif()
    except Exception:
        return False
    # 0x8825 = pointeur vers le bloc GPS
    return 0x8825 in exif


def boite_de_recadrage(taille, crop):
    """Convertit un recadrage exprimé en fractions en pixels."""
    x, y, largeur, hauteur = crop
    L, H = taille
    gauche = max(0, min(L - 1, int(round(x * L))))
    haut = max(0, min(H - 1, int(round(y * H))))
    droite = max(gauche + 1, min(L, int(round((x + largeur) * L))))
    bas = max(haut + 1, min(H, int(round((y + hauteur) * H))))
    return (gauche, haut, droite, bas)


def prepare(source, destination, max_cote=MAX_COTE, qualite=QUALITE, crop=None):
    poids_avant = os.path.getsize(source)
    with Image.open(source) as image:
        gps = gps_present(image)
        # Applique l'orientation EXIF et repart d'une image sans métadonnée.
        image = ImageOps.exif_transpose(image)
        if image.mode not in ("RGB", "L"):
            image = image.convert("RGB")

        avant = image.size
        if crop:
            image = image.crop(boite_de_recadrage(image.size, crop))
        if max(image.size) > max_cote:
            ratio = max_cote / float(max(image.size))
            cible = (max(1, round(image.width * ratio)),
                     max(1, round(image.height * ratio)))
            image = image.resize(cible, Image.LANCZOS)

        propre = Image.new(image.mode, image.size)
        propre.putdata(list(image.getdata()))

        dossier = os.path.dirname(destination)
        if dossier:
            os.makedirs(dossier, exist_ok=True)
        propre.save(destination, "JPEG", quality=qualite,
                    optimize=True, progressive=True)

    poids_apres = os.path.getsize(destination)
    return {
        "avant": avant,
        "apres": image.size,
        "poids_avant": poids_avant,
        "poids_apres": poids_apres,
        "gps": gps,
    }


def ko(octets):
    return "%.0f Ko" % (octets / 1024.0)


def main():
    analyseur = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    analyseur.add_argument("paires", nargs="+", metavar="SOURCE=DESTINATION",
                           help="chemin de la photo d'origine et nom du fichier à produire")
    analyseur.add_argument("--max-cote", type=int, default=MAX_COTE,
                           help="taille maximale du grand côté, en pixels (défaut : %d)" % MAX_COTE)
    analyseur.add_argument("--qualite", type=int, default=QUALITE,
                           help="qualité JPEG de 1 à 95 (défaut : %d)" % QUALITE)
    analyseur.add_argument("--crop", metavar="X,Y,L,H",
                           help="recadrage en fractions de l'image d'origine, "
                                "par exemple 0.08,0.16,0.74,0.74")
    options = analyseur.parse_args()

    crop = None
    if options.crop:
        try:
            crop = tuple(float(v) for v in options.crop.split(","))
        except ValueError:
            crop = None
        if not crop or len(crop) != 4 or not all(0 <= v <= 1 for v in crop):
            print("--crop attend quatre fractions entre 0 et 1 : X,Y,L,H", file=sys.stderr)
            return 1

    total_avant = total_apres = 0
    avec_gps = []
    for paire in options.paires:
        if "=" not in paire:
            print("Format attendu : source=destination (reçu : %s)" % paire, file=sys.stderr)
            return 1
        source, destination = paire.split("=", 1)
        source = os.path.expanduser(source)
        if not os.path.exists(source):
            print("Introuvable : %s" % source, file=sys.stderr)
            return 1
        infos = prepare(source, destination, options.max_cote, options.qualite, crop)
        total_avant += infos["poids_avant"]
        total_apres += infos["poids_apres"]
        if infos["gps"]:
            avec_gps.append(destination)
        print("  %-34s %dx%d → %dx%d   %8s → %8s" % (
            os.path.basename(destination),
            infos["avant"][0], infos["avant"][1],
            infos["apres"][0], infos["apres"][1],
            ko(infos["poids_avant"]), ko(infos["poids_apres"])))

    print("\nTotal : %s → %s (%.0f %% de moins)" % (
        ko(total_avant), ko(total_apres),
        100 * (1 - total_apres / float(total_avant)) if total_avant else 0))
    if avec_gps:
        print("Coordonnées GPS supprimées sur : %s" % ", ".join(
            os.path.basename(chemin) for chemin in avec_gps))
    return 0


if __name__ == "__main__":
    sys.exit(main())
