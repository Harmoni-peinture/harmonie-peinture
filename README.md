# Harmonie Peinture

Site internet, identité visuelle et supports de communication d'**Harmonie Peinture**, entreprise de peinture, plâtrerie, isolation RGE, carrelage et sols à Malleval (42520), depuis 1999.

- Téléphones : 06 69 19 05 77 (Laurent Koy) · 06 12 21 27 58 (Nicolas Bonnet)
- E-mail : harmonie.malleval@gmail.com
- Adresse : 69 chemin de Rochecourbe, 42520 Malleval
- Domaine : harmoniepeinture42.com (à brancher)

## Contenu du dépôt

| Dossier | Contenu |
| --- | --- |
| `site/` | Le site en ligne : 21 pages HTML, CSS, images, `sitemap.xml`, `robots.txt`, `llms.txt` |
| `outils/` | Le générateur des pages (`build.py`, `data.py`, `index.src.html`) et les sources des visuels réseaux sociaux |
| `brand/` | Charte graphique, cartes de visite, 50 posts, stories, couvertures à la une, photo de profil |

## Mise en ligne (GitHub Pages, gratuit)

Chaque modification enregistrée sur `main` met le site en ligne automatiquement en 1 à 2 minutes (`.github/workflows/pages.yml` publie le dossier `site/`).
Adresse provisoire : https://harmoni-peinture.github.io/harmonie-peinture/

Brancher le nom de domaine harmoniepeinture42.com :
1. Créer le fichier `site/CNAME` contenant `www.harmoniepeinture42.com`.
2. Dans la zone DNS du domaine (Wix, OVH…), ajouter un enregistrement CNAME `www` → `harmoni-peinture.github.io`, et pour le domaine nu les 4 enregistrements A de GitHub Pages : 185.199.108.153, 185.199.109.153, 185.199.110.153, 185.199.111.153.
3. Dans GitHub : Settings → Pages → Custom domain `www.harmoniepeinture42.com`, puis cocher « Enforce HTTPS ».

## Modifier le site

- Texte d'une page ville ou métier : modifier `outils/data.py`, puis lancer `python3 outils/build.py`.
- Page d'accueil : modifier `outils/index.src.html`, puis relancer `build.py`.
- Mentions légales : modifier directement `site/mentions-legales.html`.
- Formulaire : renseigner la clé Web3Forms dans `outils/index.src.html` (objet `FORM_CONFIG`), puis relancer `build.py`.

Règles de marque et faits à respecter : voir `CLAUDE.md`.
