---
name: Ongle Sauvage
description: Onglerie et nail art en Sud-Gironde — une serre végétale où chaque photo est cadrée en arche.
colors:
  vert-sous-bois: "#2e4d34"
  sauge-poudree: "#a3b18a"
  sauge-brumeuse: "#8fa68d"
  eucalyptus-clair: "#b9cdb0"
  ecume-de-serre: "#e4f1e0"
  creme-de-lin: "#f6f2e8"
  sable: "#efe7d9"
  argile: "#c8b8a4"
  encre-vegetale: "#33402f"
  blanc: "#ffffff"
typography:
  display:
    fontFamily: "Cormorant Garamond, Georgia, serif"
    fontSize: "clamp(40px, 7.4vw, 96px)"
    fontWeight: 500
    lineHeight: 1.02
    letterSpacing: "0.03em"
  headline:
    fontFamily: "Cormorant Garamond, Georgia, serif"
    fontSize: "clamp(32px, 5vw, 64px)"
    fontWeight: 500
    lineHeight: 1.02
    letterSpacing: "0.05em"
  script:
    fontFamily: "Parisienne, cursive"
    fontSize: "clamp(23px, 3.4vw, 42px)"
    fontWeight: 400
    lineHeight: 1.1
    letterSpacing: "0em"
  title:
    fontFamily: "Cormorant Garamond, Georgia, serif"
    fontSize: "22px"
    fontWeight: 500
    lineHeight: 1.1
    letterSpacing: "0.09em"
  body:
    fontFamily: "Jost, system-ui, sans-serif"
    fontSize: "clamp(15px, 1.45vw, 18px)"
    fontWeight: 300
    lineHeight: 1.75
  label:
    fontFamily: "Jost, system-ui, sans-serif"
    fontSize: "12px"
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: "0.24em"
rounded:
  pill: "999px"
  arch: "999px 999px 28px 28px"
  arch-compact: "999px 999px 18px 18px"
  card: "220px 220px 24px 24px"
  review: "160px 160px 24px 24px"
  hours: "240px 240px 26px 26px"
spacing:
  gutter: "24px"
  rail-gap: "16px"
  block: "clamp(58px, 7vw, 110px)"
components:
  button-primary:
    backgroundColor: "{colors.sauge-poudree}"
    textColor: "{colors.blanc}"
    rounded: "{rounded.pill}"
    padding: "15px 30px"
    typography: "{typography.label}"
  button-primary-hover:
    backgroundColor: "{colors.vert-sous-bois}"
    textColor: "{colors.blanc}"
  button-forest:
    backgroundColor: "{colors.vert-sous-bois}"
    textColor: "{colors.creme-de-lin}"
    rounded: "{rounded.pill}"
    padding: "15px 30px"
  button-forest-hover:
    backgroundColor: "{colors.sauge-poudree}"
    textColor: "{colors.blanc}"
  button-pale:
    backgroundColor: "{colors.ecume-de-serre}"
    textColor: "{colors.vert-sous-bois}"
    rounded: "{rounded.pill}"
    padding: "15px 30px"
  button-ghost:
    textColor: "{colors.encre-vegetale}"
    rounded: "{rounded.pill}"
    padding: "14px 28px"
  chip:
    backgroundColor: "{colors.blanc}"
    textColor: "{colors.encre-vegetale}"
    rounded: "{rounded.pill}"
    padding: "9px 18px"
  card-service:
    backgroundColor: "{colors.creme-de-lin}"
    textColor: "{colors.encre-vegetale}"
    rounded: "{rounded.card}"
    padding: "50px 30px 32px"
  card-review:
    backgroundColor: "{colors.creme-de-lin}"
    textColor: "{colors.encre-vegetale}"
    rounded: "{rounded.review}"
    padding: "44px 30px 30px"
  card-hours:
    backgroundColor: "{colors.sauge-poudree}"
    textColor: "{colors.blanc}"
    rounded: "{rounded.hours}"
  arch-label:
    textColor: "{colors.creme-de-lin}"
    rounded: "{rounded.pill}"
    padding: "7px 16px"
  rail-button:
    textColor: "{colors.vert-sous-bois}"
    rounded: "{rounded.pill}"
    width: "44px"
    height: "44px"
---

# Design System: Ongle Sauvage

## Overview

**Creative North Star: « La Serre »**

Une serre a trois choses : une palette de feuillage, une lumière filtrée, et des arches. Ce système emprunte les trois. Les neuf teintes vont du sous-bois à la crème de lin sans jamais sortir du végétal, les fonds restent clairs et mats, et l'arche coiffe chaque photographie de réalisation. Cette arche n'est pas un ornement emprunté : c'est exactement la silhouette d'un ongle en amande. La forme du produit et la forme de la page sont la même, ce qui est la raison pour laquelle le motif peut se répéter dix fois sans lasser.

L'atmosphère est calme, botanique, aérée. Les sections respirent jusqu'à 110px de souffle vertical, les paragraphes ne dépassent pas 46 caractères par ligne, et la page ne bouge pratiquement pas : le seul mouvement est le défilement des rails, la seule ombre tient sous un bouton flottant. Rien ne presse la visiteuse, alors même que la page a un objectif de conversion unique.

Les composants sont raffinés et retenus : des pilules, des bordures d'un pixel, des capitales très espacées, des transitions de 180 ms. Ils s'effacent devant les photographies, qui sont la vraie matière du site. La version précédente, en rose et nude (`v1.html`, conservée en `noindex`), a été remplacée par ce monde : elle sert d'anti-référence.

**Key Characteristics:**

- Neuf teintes végétales, du sous-bois à la crème de lin, aucune couleur hors palette
- L'arche en haut de chaque image, écho de la silhouette de l'ongle
- Des bandes de fond qui changent à chaque section, et pas une seule ombre sur le contenu
- Cormorant Garamond en capitales espacées pour les titres, Parisienne en amorce manuscrite
- Jost en graisse 300 pour le texte courant, en 500 capitales pour les repères

## Colors

Une palette entièrement végétale : deux verts porteurs, trois verts d'ambiance, une terre, et trois neutres chauds. Aucune couleur d'alerte, aucun accent froid.

### Primary

- **Vert Sous-Bois** (#2e4d34) : la couleur porteuse, de loin la plus employée. Tous les titres de section, le nom de la marque, les fonds des deux sections sombres (nail art et pied de page), et le texte des liens.
- **Sauge Poudrée** (#a3b18a) : l'accent actif. Le bouton principal, l'étiquette du héros, le fond de la carte des horaires, le bouton de retour en haut, les numéros de prestation, le guillemet des avis et le `+` de la FAQ.

### Secondary

- **Eucalyptus Clair** (#b9cdb0) : le fond de la section avis, la forme décorative derrière le portrait, l'amorce manuscrite quand elle se pose sur un fond sombre, et la couleur de sélection du texte.
- **Sauge Brumeuse** (#8fa68d) : le registre discret. L'amorce manuscrite sur fond clair, les sur-titres, les intitulés de champ, et le contour de focus clavier.
- **Écume de Serre** (#e4f1e0) : le fond de la section prestations et celui du bouton pâle posé sur les sections sombres.

### Tertiary

- **Argile** (#c8b8a4) : la seule terre de la palette, et le seul usage unique assumé — la petite forme chaude en bas à droite du portrait d'Emelyne. Elle existe pour qu'un point de la page ne soit pas vert.

### Neutral

- **Crème de Lin** (#f6f2e8) : le fond de page, le fond des cartes, et la couleur du texte sur les sections sombres.
- **Sable** (#efe7d9) : le fond des sections à propos et Instagram, et le fond d'attente d'une image en arche avant son chargement.
- **Encre Végétale** (#33402f) : le texte courant. Un vert si sombre qu'il se lit comme du noir, mais qui ne l'est pas.
- **Blanc** (#ffffff) : le texte posé sur Sauge Poudrée et le fond des puces. Jamais un fond de section.

### Named Rules

**La règle de la bande.** Deux sections voisines ne portent jamais le même fond. La page descend en bandes — crème, sable, sous-bois, crème, écume, crème, eucalyptus, crème, sable, sous-bois — et c'est ce rythme qui remplace les séparateurs.

**La règle du vert unique.** Aucune couleur hors du végétal n'entre dans la palette. Un besoin de contraste se résout en changeant de valeur dans la famille, pas en important un accent étranger.

## Typography

**Display Font:** Cormorant Garamond (avec Georgia, serif)
**Body Font:** Jost (avec system-ui, sans-serif)
**Script Font:** Parisienne (avec cursive)

**Character:** Un serif de livre pour l'autorité, une grotesque géométrique pour l'information, une anglaise pour la main. Le contraste entre les capitales très espacées du Cormorant et la légèreté du Jost en graisse 300 est ce qui donne au site son air de carte de salon plutôt que de site de services.

### Hierarchy

- **Display** (500, clamp 40→96px, interligne 1.02, capitales, +0.03em) : le nom du salon dans le héros, et lui seul.
- **Headline** (500, clamp 32→64px, capitales, +0.05em) : les titres de section. Ils arrivent tous précédés d'une amorce manuscrite.
- **Script** (Parisienne 400, clamp 23→42px, interligne 1.1) : l'amorce posée juste au-dessus d'un titre, en chevauchement négatif (`margin-bottom:-.18em`) pour que les deux se touchent.
- **Title** (500, 22px, capitales, +0.09em) : les titres de carte de prestation, les questions de la FAQ (21px) et le nom de la marque dans l'en-tête (21px, +0.16em).
- **Body** (Jost 300, clamp 15→18px, interligne 1.75) : les paragraphes. Jamais au-delà de 46 caractères par ligne dans les blocs centrés, 44 dans les sections sombres.
- **Label** (Jost 400–500, 11–12px, capitales, +0.14em à +0.30em) : les sur-titres, les intitulés, les indices de défilement, le pied de page. C'est l'espacement, pas la taille, qui signale le registre.

### Named Rules

**La règle des trois voix.** Cormorant pour les titres, Parisienne pour l'amorce, Jost pour tout le reste. Une quatrième police n'entre pas, et aucune des trois ne prend le rôle d'une autre.

**La règle de l'amorce.** Parisienne ne sert qu'à l'amorce au-dessus d'un titre. Jamais un paragraphe, jamais un bouton, jamais une étiquette.

**La règle de l'espacement avant la taille.** Pour hiérarchiser deux textes courts, on écarte les lettres plutôt que d'agrandir le corps. Le pied de page et l'en-tête tiennent entièrement sur cette règle.

## Layout

Une seule colonne centrée, large de 1180px au maximum (`--shell`), avec 24px de gouttière qui tombent à 16px sous 560px. La page est une suite de bandes pleine largeur dont le contenu, lui, reste dans la coquille.

Le souffle vertical est une variable unique, `--block` : `clamp(58px, 7vw, 110px)` en haut et en bas de chaque section. C'est la seule mesure d'espacement qui structure la page ; tout le reste est local.

Les grilles à deux colonnes sont volontairement déséquilibrées — `1.05fr / 0.95fr` pour la section à propos, `0.85fr / 1.15fr` pour les horaires — et basculent toutes en une colonne à 820px. La galerie de réalisations et le carrousel d'avis ne sont pas des grilles mais des rails horizontaux à accrochage (`scroll-snap-type: x mandatory`), dont les cartes sont dimensionnées en `clamp` pour qu'un morceau de la suivante reste visible et invite au défilement.

Quatre points de rupture, chacun pour une raison précise : **820px** bascule les grilles en colonne unique, **760px** retire les méta-informations de l'en-tête, **600px** réduit l'arche des vignettes de galerie, **560px** compacte l'en-tête et les gouttières.

### Named Rules

**La règle de la coquille.** Un fond traverse toute la largeur, un contenu jamais. Toute section ajoutée reprend `--shell` et `--block` avant d'inventer son propre espacement.

## Elevation & Depth

Le système est plat, et la profondeur vient de la couleur. Il n'y a **aucune ombre sur le contenu** : ni sur les cartes, ni sur les photos, ni sur l'en-tête collant, qui se contente d'un flou d'arrière-plan et d'un filet d'un pixel. Ce qui donne du relief à la page, c'est l'alternance des bandes de fond et, ponctuellement, les formes décoratives posées derrière le portrait.

Une seule ombre existe dans toute la feuille de style, sous le bouton de retour en haut — le seul élément qui flotte réellement au-dessus du contenu.

### Shadow Vocabulary

- **Flottant** (`box-shadow: 0 6px 20px rgba(46,77,52,.22)`) : réservé à un contrôle fixe superposé au contenu. L'ombre est teintée en vert, jamais en noir.

### Named Rules

**La règle du plat par défaut.** Une ombre n'est permise que sous un élément qui flotte au-dessus du contenu. Un élément dans le flux ne porte pas d'ombre : il change de fond.

**La règle de l'ombre verte.** Si une ombre doit exister, elle est teintée dans la palette (`rgba(46,77,52,…)`), jamais en noir neutre.

## Shapes

Une seule idée de forme, déclinée : l'arche. Un demi-cercle en haut, deux coins vifs en bas. Elle vient de la silhouette d'un ongle en amande, et c'est pour cette raison qu'elle revient partout sans jamais paraître décorative.

L'arche se décline par taille de surface, le bas se durcissant à mesure que l'objet grandit : les photographies prennent `999px 999px 28px 28px` (`--arch`), réduit à `999px 999px 18px 18px` pour les vignettes de galerie sous 600px ; les cartes de prestation `220px 220px 24px 24px` ; les cartes d'avis `160px 160px 24px 24px` ; la carte des horaires `240px 240px 26px 26px`. Les formes décoratives derrière le portrait reprennent la même grammaire, dont une retournée (`20px 20px 999px 999px`) pour éviter la symétrie.

Tout ce qui est petit et cliquable est une pilule complète (999px) : boutons, puces, étiquettes, flèches de rail, vignette du logo, bouton de retour en haut.

Les bordures sont toujours d'un pixel et toujours translucides, pour qu'elles prennent la teinte du fond sur lequel elles reposent. Un seul trait est tireté, sur les cartes de prestation, et c'est ce qui les distingue des cartes d'avis au premier coup d'œil.

### Named Rules

**La règle de l'arche.** Toute image de réalisation est cadrée en arche, sans exception. Une photo à coins droits ne ressemble plus à un ongle.

**La règle de la pilule.** Ce qui se clique est une pilule complète. Un rayon intermédiaire sur un bouton n'existe pas dans ce système.

## Components

### Buttons

- **Shape:** pilule complète (999px), texte en capitales Jost 500 à +0.14em, 14px.
- **Primary (`btn-sage`):** fond Sauge Poudrée, texte blanc, 15px 30px de remplissage. Le bouton de réservation, partout.
- **Forest (`btn-forest`):** fond Vert Sous-Bois, texte Crème de Lin. Pour les appels secondaires sur fond clair.
- **Pale (`btn-pale`):** fond Écume de Serre, texte Vert Sous-Bois. Uniquement sur les sections sombres, où les deux premiers disparaîtraient.
- **Ghost (`btn-ghost`):** sans fond, filet `rgba(51,64,47,.22)`, 14px 28px. Le second choix d'une paire.
- **Hover / Focus:** l'échange de fond entre Sauge Poudrée et Vert Sous-Bois, en 180 ms sur `background`, `color` et `border-color`. Le fantôme, lui, fonce son filet et prend un voile blanc. Le focus clavier est un contour Sauge Brumeuse de 2px décalé de 3px, hérité de `:focus-visible` au niveau du document.

### Chips

- **Style:** fond blanc, texte Encre Végétale, filet `rgba(51,64,47,.08)`, pilule, 9px 18px, 13px.
- **State:** purement descriptives, jamais interactives. Sur fond sombre, la variante `chip-dark` passe en blanc translucide à 10 % avec un filet à 20 %.

### Cards / Containers

- **Corner Style:** arche, dont le rayon haut croît avec la taille de la carte (voir Shapes).
- **Background:** Crème de Lin pour les cartes de prestation et d'avis, Sauge Poudrée pour la carte des horaires.
- **Shadow Strategy:** aucune. Voir Elevation & Depth.
- **Border:** tiretée `rgba(143,166,141,.55)` sur les prestations, aucune sur les avis.
- **Internal Padding:** généreux et asymétrique, plus épais en haut pour dégager la courbe de l'arche — 50px 30px 32px pour les prestations, 44px 30px 30px pour les avis.
- **Behavior:** les cartes d'un même rail prennent la hauteur de la plus longue ; leur contenu est centré verticalement pour que les courtes ne laissent pas de vide.

### Navigation

- **Style:** barre collante en Crème de Lin à 90 % avec flou d'arrière-plan de 14px et un filet d'un pixel en bas. Trois zones : méta à gauche, marque au centre, appel à l'action à droite.
- **Typography:** marque en Cormorant capitales 21px à +0.16em ; méta en Jost 300 capitales 12px.
- **Responsive:** la méta disparaît à 760px, puis la barre se compacte à 560px — marque à 16px, bouton à 10px, interdiction de retour à la ligne.
- **Il n'y a pas de menu.** Aucun lien d'ancre dans l'en-tête, aucun hamburger : une seule action y est possible, réserver.

### Rails (signature)

Le composant qui porte le site. Un conteneur en `flex` à défilement horizontal, accrochage obligatoire, barre de défilement masquée sur tous les moteurs, et un pied qui associe un indice textuel (« 16 réalisations · faites défiler ») à deux flèches rondes de 44px. Les flèches sont transparentes avec un filet, passent en Crème de Lin au survol, et tombent à 30 % d'opacité quand le rail est au bout. Sous `prefers-reduced-motion`, le défilement programmé repasse en `auto`.

### Arch Photo (signature)

Une photographie cadrée en arche, fond Sable en attente de chargement, avec une étiquette en pilule posée en bas au centre : `rgba(46,77,52,.86)`, flou d'arrière-plan de 3px, texte Crème de Lin en capitales 11px à +0.16em, tronqué par ellipse plutôt que replié.

## Do's and Don'ts

### Do:

- **Do** cadrer toute photo de réalisation en arche (`--arch`), et poser son étiquette en pilule translucide au centre bas.
- **Do** faire précéder chaque titre de section d'une amorce Parisienne en chevauchement négatif.
- **Do** changer de fond à chaque section, en suivant la bande déjà en place.
- **Do** reprendre `--shell` et `--block` pour toute section ajoutée, avant d'inventer un espacement local.
- **Do** teinter une ombre dans la palette si elle est inévitable, et la réserver à un élément flottant.
- **Do** hiérarchiser deux textes courts par l'espacement des lettres plutôt que par le corps.
- **Do** laisser les rails fonctionner au doigt et au défilement natif : les flèches sont un supplément, pas la seule porte d'entrée.

### Don't:

- **Don't** mettre une ombre sous une carte, une photo ou l'en-tête. La profondeur passe par la couleur.
- **Don't** introduire une couleur hors palette végétale, ni réveiller `--moss` (#4a5d23) et `--mint` (#c8dcc2), qui sont déclarées mais inutilisées.
- **Don't** utiliser Parisienne ailleurs que dans une amorce de titre.
- **Don't** ajouter une quatrième famille de caractères.
- **Don't** donner un rayon intermédiaire à un bouton : c'est une pilule complète ou rien.
- **Don't** poser un bouton Sauge Poudrée ou Vert Sous-Bois sur une section sombre — c'est le rôle du bouton pâle.
- **Don't** ajouter un menu de navigation : l'en-tête ne porte qu'une action.
- **Don't** reprendre quoi que ce soit du rose et nude de `v1.html`, qui est l'anti-référence de ce système.
