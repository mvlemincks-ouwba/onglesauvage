# Ongle Sauvage

Site vitrine one-page pour **Ongle Sauvage**, onglerie et nail art à Castets et Castillon (Sud-Gironde).

En ligne : https://mvlemincks-ouwba.github.io/onglesauvage/

## Contenu

- `index.html` — la page complète (HTML + CSS, aucune dépendance à installer)
- `v2.html` — refonte en cours : palette sauge / eucalyptus / beige, typographies Cormorant Garamond + Parisienne
- `assets/` — logo et photos des réalisations
- `scripts/maj-avis.py` — synchronisation des avis Booksy
- `.github/workflows/avis-booksy.yml` — exécution quotidienne de cette synchronisation

Les réservations pointent vers la fiche Booksy du salon, les photos viennent de la fiche Booksy et du compte Instagram [@ongle_sauvage](https://www.instagram.com/ongle_sauvage/).

## Modifier le site

Éditez `index.html` et poussez sur `main` : GitHub Pages redéploie automatiquement.

Pour prévisualiser en local :

```bash
python3 -m http.server 8000
```

puis ouvrez http://localhost:8000.

## Design

Maquette source : projet Claude Design « Ongle Sauvage » (design system ouwba). Typographies Anton et Inter Tight, palette rose / nude / encre.

## Avis Booksy : mise à jour automatique

Les avis affichés sur le site sont synchronisés chaque jour depuis la fiche
Booksy par le workflow `.github/workflows/avis-booksy.yml` (06:12 UTC, ou à la
demande depuis l'onglet Actions).

Le script `scripts/maj-avis.py` lit la page publique Booksy et réécrit
directement le HTML : les cartes entre les repères `<!-- avis:start -->` et
`<!-- avis:end -->`, les compteurs `<span data-avis-count>` /
`<span data-avis-rating>`, et `reviewCount` / `ratingValue` dans les données
structurées JSON-LD. Le site reste donc entièrement statique — aucun
JavaScript n'est nécessaire au visiteur pour voir les avis, et le
référencement reste correct.

```bash
python3 scripts/maj-avis.py --check   # montre ce qui changerait, sans écrire
python3 scripts/maj-avis.py           # applique la mise à jour
```

Points à connaître :

- **Ne pas modifier à la main** le bloc entre les deux repères : il est écrasé
  à chaque exécution.
- Le carrousel affiche les **10 avis les plus récents** (ceux servis sur la
  première page Booksy) ; la note et le nombre total portent bien sur
  l'ensemble des avis.
- Si Booksy change la structure de ses pages, le script **échoue sans rien
  écrire** : le site conserve ses derniers avis valides et GitHub envoie un
  mail d'échec du workflow.
- GitHub **suspend les workflows planifiés** après 60 jours sans activité sur
  le dépôt. Un commit, ou un lancement manuel depuis l'onglet Actions, les
  réactive.
