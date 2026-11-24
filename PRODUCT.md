# Product

<!-- impeccable:product-schema 1 -->

## Platform

web

## Users

Deux publics d'égale importance, confirmés par Marc :

- **Les voisines.** Habitantes de Castets et Castillon et du Sud-Gironde qui cherchent une onglerie près de chez elles. Elles arbitrent sur la proximité, les horaires et la confiance.
- **Les amatrices de nail art.** Elles choisissent la créatrice pour son travail et acceptent de faire de la route.

Elles arrivent d'Instagram, de Booksy, de Google ou du bouche-à-oreille, le plus souvent sur un téléphone, et sont en train de décider si elles prennent rendez-vous.

La clientèle n'est pas exclusivement féminine ni adulte : il existe un forfait homme et un forfait étudiant (sur justificatif), et le salon accueille les enfants.

## Product Purpose

Site vitrine one-page d'Ongle Sauvage, onglerie et nail art d'Emelyne à Castets et Castillon.

Son objectif premier, confirmé par Marc : **remplir l'agenda**. Tout le reste de la page sert cette conversion. Le succès se mesure en rendez-vous pris sur Booksy, pas en visites ni en temps passé sur la page.

## Positioning

Le nail art dessiné à la main, ongle par ongle, construit avec la cliente : une couleur, une inspiration, une occasion, puis le motif réalisé pinceau en main. Emelyne est prothésiste ongulaire et nail artiste certifiée — nail art, hygiène, dépose complète, stickers faits main, maladies et pathologies de l'ongle.

Une onglerie voisine peut proposer du gel et du gel X. Ce qu'elle ne peut pas reprendre sans mentir : la création sur mesure dessinée à la main et cet ensemble de certifications, dont la partie pathologies de l'ongle.

## Operating Context

- **Sur rendez-vous uniquement**, via la fiche Booksy, consultable 24 h/24 : `https://booksy.com/fr-fr/62614_ongle-sauvage_onglerie_80506_castillon-de-castets`. Les créneaux réellement libres n'existent que là.
- **Emelyne travaille seule.** Pas d'équipe, pas de choix de praticienne, pas de planning à plusieurs.
- Salon au 31 Rue du Port, 33210 Castets et Castillon. Lundi – vendredi 09:00 – 19:00, fermé samedi et dimanche. Téléphone 07 81 85 57 70.
- Paiement : espèces, carte bancaire, virement. Sur place : places de parking, Wi-Fi, adapté aux enfants.
- Cartes cadeaux disponibles depuis la page Booksy.
- Instagram [@ongle_sauvage](https://www.instagram.com/ongle_sauvage/) est le canal vivant : nouvelles créations, projets en cours et disponibilités de dernière minute y passent en premier. Une page Facebook existe aussi.
- Le site est statique, servi par GitHub Pages sur onglesauvage.com. On le modifie en éditant `index.html` et en poussant sur `main`.

## Capabilities and Constraints

**Les six prestations** présentées sur la page : gel · pose américaine (gel X) · semi-permanent, mains et pieds · soin de l'ongle · forfaits (classique, étudiant sur justificatif, homme) · réparation d'un ongle cassé ou décollé, en gel comme en gel X.

**Contraintes durables, confirmées par Marc — elles doivent rester vraies dans toute évolution :**

- **Booksy est le seul canal de réservation.** Aucun formulaire, aucune prise de rendez-vous maison : chaque appel à l'action pointe vers la fiche Booksy.
- **Aucun tarif ni durée affiché sur le site.** Ils vivent sur Booksy et nulle part ailleurs. La page le dit explicitement.
- **Le bloc avis est synchronisé, pas rédigé.** `scripts/maj-avis.py` réécrit chaque jour (GitHub Actions, 06:12 UTC) les cartes entre `<!-- avis:start -->` et `<!-- avis:end -->`, les compteurs `data-avis-count` / `data-avis-rating`, et `reviewCount` / `ratingValue` du JSON-LD. Toute édition manuelle de cette zone est écrasée. Le carrousel affiche au plus 12 cartes (`MAX_CARTES`), prises parmi les avis que sert la première page Booksy — 9 aujourd'hui ; la note et le total affichés portent, eux, sur l'ensemble des avis. En dessous de 3 avis extraits (`MIN_AVIS`), le script considère que Booksy a changé de structure et n'écrit rien : le site garde ses derniers avis valides. Contrainte liée : la page ne doit porter qu'une seule occurrence de `"ratingValue"` et de `"reviewCount"`, car le script les réécrit par substitution globale avec la note agrégée — des objets `Review` individuels porteurs de leur propre note seraient écrasés dès le lendemain.
- **Salon solo.** Rien dans le site ne doit laisser croire à une équipe.

**Contraintes techniques :**

- HTML + CSS statiques dans un seul fichier, aucune dépendance, aucune étape de build. Le contenu reste lisible sans JavaScript : les carrousels sont un enrichissement, pas une condition d'accès.
- `CNAME` ne doit jamais être supprimé, sinon GitHub réinitialise le domaine personnalisé.
- `v1.html` est la première version du site, conservée pour mémoire en `noindex`. Elle n'est pas maintenue et ne doit pas réapparaître dans le sitemap.
- Données structurées JSON-LD de type `NailSalon` dans la page : adresse, horaires, téléphone, moyens de paiement, note agrégée. Elles doivent rester cohérentes avec le contenu visible.

**Vocabulaire métier**, en français, tel qu'Emelyne l'emploie : prothésiste ongulaire, nail artiste, pose, remplissage, dépose, gel X ou pose américaine, semi-permanent, forfait, réparation.

**Non décidé à ce jour**, donc à ne pas supposer : pas de boutique en ligne, pas de paiement sur le site, pas de version anglaise, pas de blog, pas de deuxième adresse.

## Brand Commitments

- Le nom est **Ongle Sauvage**. La promesse portée par la page : « le nail art qui vous ressemble ».
- **La voix est celle d'Emelyne, à la première personne**, et elle vouvoie la cliente. Chaleureuse, directe, avec ses émojis. Ce n'est pas du texte marketing : c'est elle qui parle. Toute réécriture de ces passages se fait avec elle, pas à sa place.
- Assets fournis : `assets/logo.jpg`, `assets/emelyne.jpg`, et une bibliothèque de photos de réalisations (`assets/nailart-*.jpg`, `assets/pedicure-*.jpg`, `assets/galerie-*.jpg`) issues de la fiche Booksy et du compte Instagram — 28 fichiers au total, dont 21 réalisations utilisées dans la page : 16 dans la galerie, les autres en ouverture et en habillage de sections.
- Aucune marque de produit n'est citée nulle part sur le site. Ne pas en introduire sans accord.

## Evidence on Hand

- **Avis réels** : 5,0 sur 18 avis Booksy au moment de l'écriture, avec prénom et prestation, repris automatiquement depuis la fiche. Le chiffre bouge, le script le met à jour.
- **Photos réelles** : les ongles montrés sont ceux de son travail. Pas de banque d'images.
- **Certifications** déclarées par Emelyne : nail art, hygiène, dépose complète, stickers faits main, maladies et pathologies de l'ongle. Aucun organisme certificateur ni justificatif n'est disponible dans le dépôt — ne pas nommer d'école ni de label.
- **Comptes sociaux** actifs : Instagram et Facebook, liés depuis la page.

**À ne jamais inventer, faute de preuve :** tarifs et durées, nombre de clientes, années d'expérience, récompenses, presse, avant/après, équipe, seconde adresse, partenariats ou marques de produits.

## Product Principles

1. **Tout mène à Booksy.** Une page, une action. Ce qui n'aide pas à prendre rendez-vous n'a pas à grandir.
2. **Le prix se découvre sur Booksy, jamais ici.** Le site ne promet pas un montant qu'il ne contrôle pas.
3. **Montrer le travail, pas une idée du travail.** Les photos sont les siennes ; une illustration générique coûterait la crédibilité qui fait réserver.
4. **C'est Emelyne qui parle.** Le ton du site est le ton du salon : si la cliente ne retrouve pas la même personne en poussant la porte, la page a menti.
5. **Un fichier qui s'édite et se pousse.** Pas de build, pas de dépendance : Emelyne et Marc doivent pouvoir corriger une ligne et la voir en ligne.
