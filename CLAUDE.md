# Contexte pour les assistants IA (Claude, ChatGPT, Codex…)

Tu travailles pour **Harmonie Peinture** (Malleval, 42), artisan peintre-plaquiste depuis 1999, 5 artisans salariés, certifié Qualibat RGE, chef d'entreprise : Laurent Koy. Associé fondateur : Nicolas Bonnet. Gestion & administration : Sophie Koy.

## Règles de marque (charte v1.0, `brand/charte/`)
- Couleurs : Golf Green #1F4D3A (marque), Sunset #C2531B (UNIQUEMENT boutons et appels à l'action), Caddie #F4F1E6 (fond), Retro Sky #CFE8EE (encadrés, badges), Graphite #111412 (texte).
- Polices : Urbanist (titres, 700), Inter (textes).
- Style : épuré, aéré, coins arrondis, boutons pilule. Esprit « club de golf » purement visuel (écusson, rayures de tonte, drapeau) : ne jamais écrire le mot golf.
- Ton : vouvoiement, phrases courtes, concret, pas de superlatifs (« les meilleurs »…).
- Photos : uniquement des chantiers réels d'Harmonie Peinture.
- Signature : « Le travail bien fait, du sol au plafond. » et « Chaque mur, un sans-faute. »

## Faits à respecter (ne rien inventer)
- Téléphones : 06 69 19 05 77 (Laurent Koy, chef d'entreprise, numéro principal) et 06 12 21 27 58 (Nicolas Bonnet, associé fondateur) · harmonie.malleval@gmail.com · 69 chemin de Rochecourbe, 42520 Malleval.
- Horaires : lundi au vendredi, 8 h – 17 h.
- SASU, RCS Saint-Étienne 887 942 720, SIRET 887 942 720 00020, TVA FR10887942720.
- Note Google 4,6. Zone : environ 35 km autour de Malleval.
- Ne jamais inventer d'avis, de prix ni de délais.

## Structure technique
- `site/` est généré : ne pas modifier les pages villes/métiers à la main, passer par `outils/data.py` puis `python3 outils/build.py`.
- Chaque page porte des données structurées schema.org (HousePainter, Service, FAQPage, BreadcrumbList) : les garder cohérentes avec les faits ci-dessus.
- Après tout ajout de page, mettre à jour `sitemap.xml` (fait automatiquement par `build.py`).
