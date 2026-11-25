# -*- coding: utf-8 -*-
import json, math, html, os, re, datetime
from data import *

ROOT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "site")
TODAY = datetime.date.today().isoformat()
E = html.escape

LOGO = '<svg width="34" height="34" viewBox="0 0 120 120" aria-hidden="true"><path d="M84 26V94" stroke="#E6E0D0" stroke-width="12" stroke-linecap="round" fill="none"/><path d="M84 26V50" stroke="#C2531B" stroke-width="12" stroke-linecap="round" fill="none"/><circle cx="36" cy="27" r="7.5" fill="#1F4D3A"/><path d="M36 44V94" stroke="#1F4D3A" stroke-width="12" stroke-linecap="round" fill="none"/><path d="M36 62L69 42" stroke="#1F4D3A" stroke-width="6" stroke-linecap="round" fill="none"/><circle cx="69" cy="42" r="8.5" fill="#1F4D3A"/><circle cx="69" cy="42" r="2.6" fill="#F4F1E6"/><path d="M48 82H63L61 96H50Z" fill="#1F4D3A"/></svg>'
GLOGO = '<svg width="14" height="14" viewBox="0 0 48 48" aria-hidden="true"><path fill="#4285F4" d="M45 24.5c0-1.6-.1-3.1-.4-4.5H24v8.5h11.8c-.5 2.7-2 5-4.4 6.6v5.5h7.1c4.2-3.8 6.5-9.5 6.5-16.1z"/><path fill="#34A853" d="M24 46c5.9 0 10.9-2 14.5-5.4l-7.1-5.5c-2 1.3-4.5 2.1-7.4 2.1-5.7 0-10.5-3.8-12.2-9H4.5v5.7C8.1 41.1 15.5 46 24 46z"/><path fill="#FBBC05" d="M11.8 28.2c-.4-1.3-.7-2.7-.7-4.2s.3-2.9.7-4.2v-5.7H4.5C3 17.1 2 20.4 2 24s1 6.9 2.5 9.9l7.3-5.7z"/><path fill="#EA4335" d="M24 10.8c3.2 0 6.1 1.1 8.4 3.3l6.3-6.3C34.9 4.2 29.9 2 24 2 15.5 2 8.1 6.9 4.5 14.1l7.3 5.7c1.7-5.2 6.5-9 12.2-9z"/></svg>'


PICTO = {
 "rouleau": '<rect x="3" y="3" width="14" height="6" rx="2"/><path d="M17 6h3v5h-8v3"/><rect x="10.5" y="14" width="3" height="7" rx="1"/>',
 "plaque": '<rect x="5" y="3" width="14" height="18" rx="1.5"/><path d="M5 8h14M9 8v13"/>',
 "isolation": '<path d="M3 11l9-7 9 7"/><path d="M5 10v10h14V10"/><path d="M8 15c1.5-1 2.5 1 4 0s2.5 1 4 0"/>',
 "carrelage": '<rect x="3" y="3" width="18" height="18" rx="2"/><path d="M12 3v18M3 12h18"/>',
 "niveau": '<rect x="2" y="9" width="20" height="6" rx="3"/><circle cx="12" cy="12" r="1.4"/><path d="M8.5 9v6M15.5 9v6"/>',
 "seau": '<path d="M5 9h14l-1.6 11H6.6z"/><path d="M8 9a4 4 0 0 1 8 0"/>',
}
SVC_PICTO = {"peintre-batiment": "rouleau", "plaquiste-plaques-de-platre": "plaque", "isolation-rge": "isolation", "carrelage-revetement-sol": "carrelage"}
def picto(name, size=22, stroke="#fff"):
    return f'<svg width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="{stroke}" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{PICTO[name]}</svg>'

def crest(bg="#F4F1E6", fg="#1F4D3A", wall="#E6E0D0", accent="#C2531B", hole="#F4F1E6", label="Harmonie Peinture, Malleval, depuis 1999"):
    return f'''<svg class="crest" viewBox="0 0 200 200" role="img" aria-label="{label}"><defs><path id="crp{fg[1:]}" d="M100 100m-74 0a74 74 0 1 1 148 0a74 74 0 1 1 -148 0"/></defs>
<circle cx="100" cy="100" r="98" fill="{bg}"/><circle cx="100" cy="100" r="58" fill="none" stroke="{fg}" stroke-width="1.6"/>
<g class="ring"><text font-family="Urbanist,Inter,sans-serif" font-weight="700" font-size="13.5" fill="{fg}"><textPath href="#crp{fg[1:]}" textLength="456" lengthAdjust="spacing">HARMONIE PEINTURE · MALLEVAL · DEPUIS 1999 · </textPath></text></g>
<g transform="translate(64 64) scale(.6)"><path d="M84 26V94" stroke="{wall}" stroke-width="12" stroke-linecap="round" fill="none"/><path d="M84 26V50" stroke="{accent}" stroke-width="12" stroke-linecap="round" fill="none"/><circle cx="36" cy="27" r="7.5" fill="{fg}"/><path d="M36 44V94" stroke="{fg}" stroke-width="12" stroke-linecap="round" fill="none"/><path d="M36 62L69 42" stroke="{fg}" stroke-width="6" stroke-linecap="round" fill="none"/><circle cx="69" cy="42" r="8.5" fill="{fg}"/><circle cx="69" cy="42" r="2.6" fill="{hole}"/><path d="M48 82H63L61 96H50Z" fill="{fg}"/></g></svg>'''

def city_url(c): return f"peintre-{c['slug']}.html"
def svc_url(s): return f"{s['slug']}.html"
def dist_txt(c): return "nos locaux" if c["dist"] == 0 else f"≈ {c['dist']} km"

BUSINESS_ID = SITE + "/#entreprise"
def business_ld():
    return {
      "@type": ["HousePainter", "HomeAndConstructionBusiness"], "@id": BUSINESS_ID,
      "name": "Harmonie Peinture", "legalName": "Harmonie Peinture SASU",
      "url": SITE + "/", "telephone": TEL_INT, "contactPoint": [{"@type": "ContactPoint", "telephone": TEL_INT, "contactType": "customer service", "name": "Laurent Koy", "areaServed": "FR", "availableLanguage": "French"}, {"@type": "ContactPoint", "telephone": TEL2_INT, "contactType": "customer service", "name": "Nicolas Bonnet", "areaServed": "FR", "availableLanguage": "French"}], "image": SITE + "/img/r-cuisine.jpg", "logo": SITE + "/img/logo.png",
      "description": "Entreprise de peinture, plâtrerie, isolation RGE, carrelage et revêtements de sol basée à Malleval (Loire), depuis 1999. Cinq artisans salariés, certifiée Qualibat RGE.",
      "foundingDate": "1999", "numberOfEmployees": {"@type": "QuantitativeValue", "value": 5},
      "vatID": "FR10887942720", "taxID": "88794272000020", "naics": "238320", "isicV4": "4334",
      "address": {"@type": "PostalAddress", "streetAddress": ADDR["street"], "postalCode": ADDR["cp"], "addressLocality": ADDR["city"], "addressRegion": ADDR["region"], "addressCountry": "FR"},
      "geo": {"@type": "GeoCoordinates", "latitude": GEO[0], "longitude": GEO[1]},
      "openingHoursSpecification": [{"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday","Tuesday","Wednesday","Thursday","Friday"], "opens": "08:00", "closes": "17:00"}],
      "areaServed": [{"@type": "City", "name": c["name"], "address": {"@type": "PostalAddress", "postalCode": c["cp"], "addressCountry": "FR"}} for c in CITIES]
                    + [{"@type": "GeoCircle", "geoMidpoint": {"@type": "GeoCoordinates", "latitude": GEO[0], "longitude": GEO[1]}, "geoRadius": "30000"}],
      "hasCredential": [{"@type": "EducationalOccupationalCredential", "credentialCategory": "Qualification professionnelle", "name": "Qualibat RGE", "recognizedBy": {"@type": "Organization", "name": "Qualibat", "url": "https://www.qualibat.com"}}],
      "employee": {"@type": "Person", "name": "Laurent Koy", "jobTitle": "Chef d'entreprise"},
      "knowsAbout": ["Peinture intérieure", "Peinture extérieure", "Plaques de plâtre", "Faux plafonds", "Isolation thermique", "Carrelage", "Revêtements de sol"],
      "makesOffer": [{"@type": "Offer", "itemOffered": {"@type": "Service", "name": s["name"], "url": f"{SITE}/{svc_url(s)}"}} for s in SERVICES],
      "priceRange": "Sur devis", "currenciesAccepted": "EUR",
    }

def faq_ld(faq): return {"@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faq]}
def crumbs_ld(items): return {"@type": "BreadcrumbList", "itemListElement": [{"@type": "ListItem", "position": i+1, "name": n, "item": f"{SITE}/{u}"} for i, (n, u) in enumerate(items)]}
def ld(*objs): return '<script type="application/ld+json">' + json.dumps({"@context": "https://schema.org", "@graph": list(objs)}, ensure_ascii=False, separators=(",", ":")) + '</script>'

def head(title, desc, path, img="img/r-cuisine.jpg", extra=""):
    return f'''<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{E(title)}</title>
<meta name="description" content="{E(desc)}">
<link rel="canonical" href="{SITE}/{path}">
<meta name="robots" content="index,follow,max-image-preview:large">
<meta name="geo.region" content="FR-42"><meta name="geo.placename" content="Malleval"><meta name="geo.position" content="{GEO[0]};{GEO[1]}"><meta name="ICBM" content="{GEO[0]}, {GEO[1]}">
<meta property="og:type" content="website"><meta property="og:locale" content="fr_FR"><meta property="og:site_name" content="Harmonie Peinture">
<meta property="og:title" content="{E(title)}"><meta property="og:description" content="{E(desc)}"><meta property="og:url" content="{SITE}/{path}"><meta property="og:image" content="{SITE}/{img}">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#F4F1E6">
<link rel="icon" href="/favicon.ico" sizes="48x48"><link rel="icon" href="/favicon.svg" type="image/svg+xml"><link rel="icon" href="/favicon-96x96.png" sizes="96x96" type="image/png"><link rel="apple-touch-icon" href="/apple-touch-icon.png"><link rel="manifest" href="/site.webmanifest"><meta name="theme-color" content="#1F4D3A">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=Urbanist:wght@500;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/site.css">
{extra}
</head>'''

def header(home=False):
    p = "" if home else "index.html"
    return f'''<header id="hd">
<div class="nav">
<a class="brand" href="{p or '#accueil'}" aria-label="Harmonie Peinture, accueil">{LOGO}<span class="wm"><b>Harmonie</b><small>Peinture</small></span></a>
<nav class="links" aria-label="Navigation principale"><a href="{p}#services">Métiers</a><a href="{p}#qui-sommes-nous">L'entreprise</a><a href="{p}#zones">Zones</a><a href="{p}#realisations">Réalisations</a><a href="{p}#faq">FAQ</a></nav>
<a class="btn btn-o" href="{p}#contact">Devis</a>
</div>
</header>'''

def footer():
    svc = "".join(f'<li><a href="{svc_url(s)}">{E(s["name"])}</a></li>' for s in SERVICES)
    cities = sorted(CITIES, key=lambda c: c["dist"])
    c1 = "".join(f'<li><a href="{city_url(c)}">Peintre à {E(c["name"])}</a></li>' for c in cities[:8])
    c2 = "".join(f'<li><a href="{city_url(c)}">Peintre à {E(c["name"])}</a></li>' for c in cities[8:])
    return f'''<footer>
<div class="wrap">
<div class="fsig"><p>Chaque mur,<br><span>un sans-faute.</span></p><div style="--s:120px">{crest(bg="#1F4D3A", fg="#F4F1E6", wall="#3C705A", hole="#1F4D3A")}</div></div>
<div class="fgrid">
<div><a class="brand" href="index.html" aria-label="Harmonie Peinture, accueil">{LOGO}<span class="wm"><b>Harmonie</b><small>Peinture</small></span></a>
<p style="margin-top:18px">{ADDR["street"]}<br>{ADDR["cp"]} {ADDR["city"]} (Loire)<br>Lun – ven, 8 h – 17 h</p>
<p style="margin-top:10px"><a class="tel" href="tel:{TEL_INT}">{TEL}</a><br><span style="font-size:13px">Laurent Koy</span></p><p style="margin-top:8px"><a class="tel" href="tel:{TEL2_INT}">{TEL2}</a><br><span style="font-size:13px">Nicolas Bonnet</span></p></div>
<div><h4>Nos métiers</h4><ul>{svc}<li><a href="zones-intervention.html">Zones d'intervention</a></li></ul></div>
<div><h4>Près de chez vous</h4><ul>{c1}</ul></div>
<div><h4>&nbsp;</h4><ul>{c2}</ul></div>
</div>
<div class="ft">
<span>© <span class="yr">2026</span> Harmonie Peinture · SASU · RCS Saint-Étienne 887 942 720 · Qualibat RGE</span>
<nav aria-label="Liens légaux"><a href="mentions-legales.html#mentions">Mentions légales</a><a href="mentions-legales.html#cgu">CGU</a><a href="mentions-legales.html#confidentialite">Confidentialité</a></nav>
</div>
</div>
</footer>'''

def faq_html(faq, open_first=True):
    out = []
    for i, (q, a) in enumerate(faq):
        out.append(f'<details{" open" if (i == 0 and open_first) else ""}><summary>{E(q)}</summary><p>{E(a)}</p></details>')
    return '<div class="faq">' + "".join(out) + '</div>'

def stars(): return '<div class="stars" aria-label="5 étoiles sur 5">★★★★★</div>'

def cta(city=None):
    q = f"?commune={city['name']}" if city else ""
    where = f" à {E(city['name'])}" if city else ""
    return f'''<section class="band" style="padding-top:0"><div class="wrap"><div class="cta rv">
<div><h2>Un projet{where} ?<br>Parlons-en.</h2><p>Laurent Koy vous rappelle, vient voir votre projet et vous remet un devis détaillé. Gratuit et sans engagement.</p></div>
<div class="acts"><a class="btn btn-w" href="index.html{q}#contact">Demander un devis</a><a class="btn btn-gh" href="tel:{TEL_INT}">Appeler le {TEL}</a></div>
</div></div></section>'''

def page_end(js=True):
    return f'''<div class="mbar" id="mbar"><a class="btn btn-o" href="index.html#contact">Demander un devis</a></div>
<script src="assets/site.js" defer></script>
</body>
</html>'''

# ---------- carte ----------
def map_svg(link_prefix="", highlight=None, w=600, h=560):
    lon0, lat0 = 4.715, 5.0
    cx, cy = GEO[1], GEO[0]
    k = 1400  # px par degré de latitude
    kx = k * math.cos(math.radians(45.38))
    def P(lat, lon): return (w/2 + (lon - cx) * kx + 10, h/2 - (lat - 45.355) * k)
    rhone = [(45.60,4.77),(45.56,4.83),(45.525,4.872),(45.50,4.83),(45.48,4.80),(45.462,4.772),(45.44,4.773),(45.415,4.755),(45.39,4.752),(45.36,4.757),(45.33,4.763),(45.30,4.775),(45.26,4.795),(45.22,4.81),(45.17,4.825),(45.12,4.83)]
    pts = " ".join(f"{P(a,b)[0]:.1f},{P(a,b)[1]:.1f}" for a, b in rhone)
    mx, my = P(*GEO)
    r35 = 26 * k / 110.57
    r15 = 15 * k / 110.57
    s = [f'<svg viewBox="0 0 {w} {h}" role="img" aria-label="Carte schématique de nos zones d\'intervention autour de Malleval">',
         '<defs><radialGradient id="zg"><stop offset="0" stop-color="#1F4D3A" stop-opacity=".16"/><stop offset="1" stop-color="#1F4D3A" stop-opacity=".03"/></radialGradient><clipPath id="zc"><rect width="%d" height="%d" rx="24"/></clipPath></defs>' % (w, h),
         f'<g clip-path="url(#zc)"><rect width="{w}" height="{h}" fill="#F7F5EE"/>',
         f'<circle cx="{mx:.1f}" cy="{my:.1f}" r="{r35:.1f}" fill="url(#zg)" stroke="#1F4D3A" stroke-opacity=".25" stroke-dasharray="4 6"/>',
         f'<circle cx="{mx:.1f}" cy="{my:.1f}" r="{r15:.1f}" fill="none" stroke="#1F4D3A" stroke-opacity=".18" stroke-dasharray="2 5"/>',
         f'<polyline points="{pts}" fill="none" stroke="#9CCBD6" stroke-width="9" stroke-linecap="round" stroke-linejoin="round" opacity=".75"/>',
         f'<text x="{P(45.405,4.765)[0]+14:.0f}" y="{P(45.405,4.765)[1]:.0f}" font-family="Inter" font-size="11" fill="#5E9BAA" font-style="italic">Rhône</text></g>']
    for c in CITIES:
        if c["slug"] == "malleval": continue
        x, y = P(c["lat"], c["lon"])
        hl = highlight == c["slug"]
        LAB = {"chavanay":("start",9,4),"condrieu":("end",-9,2),"les-roches-de-condrieu":("start",9,4),"saint-clair-du-rhone":("start",9,9),"saint-pierre-de-boeuf":("middle",0,19),"pelussin":("end",-9,4)}
        anchor, dx, dy = LAB.get(c["slug"], ("end" if c["lon"] < 4.74 else "start", -9 if c["lon"] < 4.74 else 9, 4))
        tx = x + dx
        s.append(f'<a href="{link_prefix}{city_url(c)}"><circle class="d" cx="{x:.1f}" cy="{y:.1f}" r="{6 if hl else 4.5}" fill="#1F4D3A"/><text x="{tx:.1f}" y="{y+dy:.1f}" text-anchor="{anchor}" font-family="Inter" font-size="{13 if hl else 12}" font-weight="{700 if hl else 500}" fill="{"#1F4D3A" if hl else "#3A4440"}">{E(c["name"])}</text></a>')
    s.append(f'<a href="{link_prefix}{city_url(CITY["malleval"])}"><ellipse cx="{mx:.1f}" cy="{my:.1f}" rx="13" ry="5" fill="#1F4D3A" opacity=".16"/><ellipse cx="{mx:.1f}" cy="{my:.1f}" rx="3.2" ry="1.6" fill="#111412"/><path d="M{mx:.1f} {my:.1f}V{my-30:.1f}" stroke="#111412" stroke-width="2" stroke-linecap="round"/><path d="M{mx:.1f} {my-30:.1f}l15 5.5l-15 5.5z" fill="#C2531B"/><text x="{mx-10:.1f}" y="{my-14:.1f}" text-anchor="end" font-family="Urbanist" font-size="15" font-weight="800" fill="#111412">Malleval</text></a>')
    s.append('</svg>')
    return "".join(s)

def chips(cs, prefix=""):
    return '<div class="chips">' + "".join(f'<a href="{prefix}{city_url(c)}">{E(c["name"])}<small>{c["dn"]}</small></a>' for c in cs) + '</div>'

# ---------- pages ville ----------
def build_city(c):
    path = city_url(c)
    near = [CITY[n] for n in c["near"]]
    title = f"Peintre et plaquiste à {c['name']} ({c['dn']}) | Harmonie Peinture"
    desc = f"Peinture, plaques de plâtre, isolation RGE, carrelage et sols à {c['name']} ({c['cp']}). Artisans salariés basés à Malleval depuis 1999, {('à ' + str(c['dist']) + ' km environ') if c['dist'] else 'sur place'}. Devis gratuit."
    loc = "Malleval, notre commune" if c["dist"] == 0 else f"à environ {c['dist']} km de notre atelier de Malleval"
    faq = [
      (f"Intervenez-vous à {c['name']} ?", f"Oui. {c['name']} ({c['cp']}, {c['dep']}) fait partie de notre secteur d'intervention : notre atelier est {'dans la commune' if c['dist']==0 else 'à environ ' + str(c['dist']) + ' km, à Malleval'}. Nous y réalisons peinture, plâtrerie, isolation, carrelage et sols."),
      (f"Comment obtenir un devis à {c['name']} ?", f"Appelez le {TEL} ou remplissez le formulaire : Laurent Koy vous rappelle, vient voir votre projet à {c['name']} et vous remet un devis détaillé, gratuit et sans engagement."),
      (f"Les habitants de {c['name']} peuvent-ils bénéficier des aides pour l'isolation ?", "Oui, sous conditions. Nos travaux d'isolation sont certifiés Qualibat RGE : ils peuvent ouvrir droit à MaPrimeRénov', aux primes énergie (CEE) et à l'éco-prêt à taux zéro, selon vos revenus et votre logement."),
      ("Qui réalise les travaux ?", "Nos cinq artisans salariés, peintres et plaquistes. Nous ne sous-traitons pas : la même équipe intervient du début à la fin du chantier."),
    ]
    rv = REVIEWS[hash(c["slug"]) % len(REVIEWS)] if False else REVIEWS[CITIES.index(c) % len(REVIEWS)]
    pool = [("img/m-cuisine.jpg","Cuisine : murs et plafond"),("img/m-sdb.jpg","Salle de bains, faïence murale"),("img/m-chambre.jpg","Chambre repeinte, sol stratifié"),("img/m-sejour.jpg","Séjour repeint"),("img/m-chambre-3.jpg","Chambre, peinture et sol"),("img/r-plafond.jpg","Faux plafond avec spots")]
    photos = [p for p in pool if p[0] != c["img"]][:3]
    crumbs = [("Accueil","index.html"),("Zones d'intervention","zones-intervention.html"),(f"Peintre à {c['name']}", path)]
    svc_ld = {"@type": "Service", "name": f"Peinture, plâtrerie et isolation à {c['name']}", "serviceType": "Peinture et finitions du bâtiment",
              "provider": {"@id": BUSINESS_ID}, "areaServed": {"@type": "City", "name": c["name"], "address": {"@type": "PostalAddress", "postalCode": c["cp"], "addressRegion": c["dep"], "addressCountry": "FR"}},
              "url": f"{SITE}/{path}"}
    out = head(title, desc, path, c["img"], ld(business_ld(), svc_ld, faq_ld(faq), crumbs_ld(crumbs)))
    svcards = "".join(f'<a class="svc" href="{svc_url(s)}" style="background-image:url({s["img"]})"><span class="pic">{picto(SVC_PICTO[s["slug"]])}</span><div><h3>{E(s["short"])}</h3><p>{E(s["card"])}</p><span class="go">Découvrir ›</span></div></a>' for s in SERVICES)
    out += f'''
<body>
{header()}
<main>
<section class="phero"><div class="pcard" style="background-image:url({c["img"]})"><div class="in">
<nav class="crumbs" aria-label="Fil d'Ariane"><a href="index.html">Accueil</a>›<a href="zones-intervention.html">Zones d'intervention</a>›<span>{E(c["name"])}</span></nav>
<span class="kick">{E(c["name"])} · {E(c["dep"])} ({c["dn"]})</span>
<h1>Peintre et plaquiste<br>à <em>{E(c["name"])}.</em></h1>
<p class="lede">{E(c["lede"])}</p>
<div class="ctas"><a class="btn btn-o" href="index.html?commune={E(c["name"])}#contact">Demander un devis</a><a class="lnk" href="tel:{TEL_INT}"><span>{TEL}</span> ›</a></div>
</div></div></section>
<section style="padding:12px 12px 0"><div class="facts">
<div><b>{dist_txt(c)}</b><span>{"Malleval, notre atelier" if c["dist"]==0 else "depuis notre atelier de Malleval"}</span></div>
<div><b>1999</b><span>année de création</span></div>
<div><b>5</b><span>artisans salariés, sans sous-traitance</span></div>
<div><b>RGE</b><span>certifiée Qualibat</span></div>
</div></section>

<section class="band"><div class="wrap two">
<div class="rv"><span class="eyebrow">À {E(c["name"])}</span><h2>Des artisans<br>du coin.</h2></div>
<div class="prose rv">{"".join(f"<p>{E(p)}</p>" for p in c["p"])}
<h3>Nos travaux fréquents à {E(c["name"])}</h3>
<ul class="tick">{"".join(f"<li>{E(j)}</li>" for j in c["jobs"])}</ul></div>
</div></section>

<section class="band" style="padding-top:0"><div class="wrap">
<div class="sh rv"><div><span class="eyebrow">Nos métiers</span><h2>Tout ce qu'on fait,<br>à {E(c["name"])}.</h2></div><p class="lede">Quatre métiers, une seule équipe. Chaque page détaille nos méthodes.</p></div>
<div class="svcs four rv">{svcards}</div>
</div></section>

<section class="band" style="padding-top:0"><div class="wrap">
<div class="sh rv"><div><span class="eyebrow">Réalisations</span><h2>Nos chantiers,<br>en vrai.</h2></div><p class="lede">Quelques travaux réalisés par nos équipes dans le secteur.</p></div>
<div class="ph3 rv">{"".join(f'<img src="{src}" alt="{E(alt)}" loading="lazy" width="1400" height="1050">' for src, alt in photos)}</div>
<blockquote class="quote rv" style="margin:12px 0 0">{stars()}<p style="margin-top:12px">« {E(rv[1])} »</p><footer>{E(rv[0])} · avis Google</footer></blockquote>
</div></section>

<section class="band" style="padding-top:0"><div class="wrap faqw">
<div class="rv"><span class="eyebrow">Questions fréquentes</span><h2>Vos questions,<br>à {E(c["name"])}.</h2></div>
<div class="rv">{faq_html(faq)}</div>
</div></section>

<section class="band" style="padding-top:0"><div class="wrap zones">
<div class="rv"><span class="eyebrow">Autour de {E(c["name"])}</span><h2>Nous intervenons aussi à…</h2>
{chips(near)}
<p style="margin-top:24px"><a class="lnk" style="padding:0" href="zones-intervention.html"><span>Toutes nos zones d'intervention</span> ›</a></p></div>
<div class="map rv">{map_svg(highlight=c["slug"])}<span class="note">Schéma indicatif · rayon d'environ 35 km</span></div>
</div></section>
{cta(c)}
</main>
{footer()}
{page_end()}'''
    return path, out

# ---------- pages service ----------
def build_service(s):
    path = svc_url(s)
    crumbs = [("Accueil","index.html"),(s["name"], path)]
    svc_ld = {"@type": "Service", "name": s["name"], "description": s["desc"], "provider": {"@id": BUSINESS_ID},
              "areaServed": [{"@type": "City", "name": c["name"]} for c in CITIES], "url": f"{SITE}/{path}"}
    out = head(s["title"], s["desc"], path, s["img"], ld(business_ld(), svc_ld, faq_ld(s["faq"]), crumbs_ld(crumbs)))
    others = "".join(f'<a class="svc" href="{svc_url(o)}" style="background-image:url({o["img"]})"><span class="pic">{picto(SVC_PICTO[o["slug"]])}</span><div><h3>{E(o["short"])}</h3><p>{E(o["card"])}</p><span class="go">Découvrir ›</span></div></a>' for o in SERVICES if o is not s)
    cs = sorted(CITIES, key=lambda c: c["dist"])
    out += f'''
<body>
{header()}
<main>
<section class="phero"><div class="pcard" style="background-image:url({s["img"]})"><div class="in">
<nav class="crumbs" aria-label="Fil d'Ariane"><a href="index.html">Accueil</a>›<span>{E(s["name"])}</span></nav>
<span class="kick">{E(s["kick"])}</span>
<h1>{s["h1"]}</h1>
<p class="lede">{E(s["lede"])}</p>
<div class="ctas"><a class="btn btn-o" href="index.html?travaux={E(s["short"])}#contact">Demander un devis</a><a class="lnk" href="#faq"><span>Questions fréquentes</span> ›</a></div>
</div></div></section>

<section class="band"><div class="wrap two">
<div class="rv"><span class="eyebrow">Notre approche</span><h2>Bien préparé,<br>bien fini.</h2></div>
<div class="prose rv">{"".join(f"<p>{E(p)}</p>" for p in s["intro"])}
<h3>Ce que nous réalisons</h3><ul class="tick">{"".join(f"<li>{E(i)}</li>" for i in s["items"])}</ul></div>
</div></section>

<section class="band" style="padding-top:0"><div class="wrap">
<div class="sh rv"><div><span class="eyebrow">Réalisations</span><h2>Sur nos chantiers.</h2></div><p class="lede">Des travaux réalisés par nos propres équipes.</p></div>
<div class="ph3 rv">{"".join(f'<img src="{src}" alt="{E(alt)}" loading="lazy" width="1400" height="1050">' for src, alt in s["photos"])}</div>
</div></section>

<section class="band" style="padding-top:0" id="faq"><div class="wrap faqw">
<div class="rv"><span class="eyebrow">Questions fréquentes</span><h2>{E(s["short"])} :<br>vos questions.</h2></div>
<div class="rv">{faq_html(s["faq"])}</div>
</div></section>

<section class="band" style="padding-top:0"><div class="wrap">
<div class="rv"><span class="eyebrow">Où nous intervenons</span><h2>{E(s["short"])}, près de chez vous.</h2></div>
<div class="chips rv">{"".join(f'<a href="{city_url(c)}">{E(c["name"])}<small>{c["dn"]}</small></a>' for c in cs)}</div>
</div></section>

<section class="band" style="padding-top:0"><div class="wrap">
<div class="rv"><span class="eyebrow">Nos autres métiers</span><h2>Une seule équipe pour tout le chantier.</h2></div>
<div class="svcs rv">{others}</div>
</div></section>
{cta()}
</main>
{footer()}
{page_end()}'''
    return path, out

# ---------- hub zones ----------
def build_hub():
    path = "zones-intervention.html"
    title = "Zones d'intervention autour de Malleval | Harmonie Peinture"
    desc = "Harmonie Peinture intervient dans un rayon d'environ 35 km autour de Malleval : Chavanay, Pélussin, Condrieu, Vienne, Roussillon, Serrières, Annonay, Bourg-Argental, Saint-Vallier…"
    crumbs = [("Accueil","index.html"),("Zones d'intervention", path)]
    groups = {}
    for c in sorted(CITIES, key=lambda c: c["dist"]): groups.setdefault(f'{c["dep"]} ({c["dn"]})', []).append(c)
    gh = "".join(f'<div class="rv" style="margin-top:40px"><h3>{E(g)}</h3>{chips(cs)}</div>' for g, cs in groups.items())
    out = head(title, desc, path, "img/r-apres.jpg", ld(business_ld(), crumbs_ld(crumbs)))
    out += f'''
<body>
{header()}
<main>
<section class="phero"><div class="pcard" style="background-image:url(img/r-apres.jpg);min-height:min(70svh,680px)"><div class="in">
<nav class="crumbs" aria-label="Fil d'Ariane"><a href="index.html">Accueil</a>›<span>Zones d'intervention</span></nav>
<span class="kick">Pilat rhodanien · vallée du Rhône</span>
<h1>Où nous<br><em>intervenons.</em></h1>
<p class="lede">Depuis notre atelier de Malleval, nos équipes interviennent dans un rayon d'environ 35 km, sur cinq départements.</p>
</div></div></section>
<section class="band"><div class="wrap zones">
<div><div class="rv"><span class="eyebrow">Nos communes</span><h2>Choisissez votre commune.</h2><p class="lede" style="margin-top:18px">Chaque page présente nos travaux dans la commune et ses environs.</p></div>{gh}
<div class="rv" style="margin-top:40px"><h3>Et aussi</h3><div class="chips">{"".join(f"<span>{E(t)}</span>" for t in OTHER_TOWNS)}</div>
<p style="margin-top:20px;color:var(--mute);font-size:15px">Votre commune n'apparaît pas ? Appelez-nous au <a href="tel:{TEL_INT}">{TEL}</a> : nous vous dirons si nous pouvons intervenir.</p></div></div>
<div class="map rv" style="position:sticky;top:96px">{map_svg()}<span class="note">Schéma indicatif · rayon d'environ 35 km</span></div>
</div></section>
{cta()}
</main>
{footer()}
{page_end()}'''
    return path, out

# ---------- index ----------
def build_index():
    src = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "index.src.html"), encoding="utf-8").read()
    cs = sorted(CITIES, key=lambda c: c["dist"])
    zones = f'''<section class="band" id="zones" style="padding-top:0">
<div class="wrap zones">
<div class="rv"><span class="eyebrow">Zones d'intervention</span><h2>Près de chez vous.</h2>
<p class="lede" style="margin-top:18px">Depuis Malleval, nous intervenons dans un rayon d'environ 35 km : Pilat rhodanien, vallée du Rhône, nord de l'Ardèche et de la Drôme.</p>
{chips(cs)}
<p style="margin-top:24px"><a class="lnk" style="padding:0" href="zones-intervention.html"><span>Toutes nos zones</span> ›</a></p></div>
<div class="map rv">{map_svg()}<span class="note">Schéma indicatif · rayon d'environ 35 km</span></div>
</div>
</section>'''
    faq = f'''<section class="band" id="faq" style="padding-top:0">
<div class="wrap faqw">
<div class="rv"><span class="eyebrow">Questions fréquentes</span><h2>Avant de<br>vous lancer.</h2><p class="lede" style="margin-top:18px">Une autre question ? Appelez-nous au <a href="tel:{TEL_INT}" style="font-weight:600;text-decoration:none">{TEL}</a>.</p></div>
<div class="rv">{faq_html(FAQ_HOME)}</div>
</div>
</section>'''
    title = "Peintre et plaquiste RGE à Malleval (42) | Harmonie Peinture"
    desc = "Peintres et plaquistes à Malleval depuis 1999 : peinture, plaques de plâtre, isolation RGE, carrelage et sols, de Chavanay à Vienne et Annonay. Devis gratuit."
    hd = head(title, desc, "", "img/r-cuisine.jpg", ld(business_ld(), {"@type": "WebSite", "@id": SITE + "/#site", "url": SITE + "/", "name": "Harmonie Peinture", "inLanguage": "fr-FR", "publisher": {"@id": BUSINESS_ID}}, faq_ld(FAQ_HOME)))
    hd = hd.replace(f'<link rel="canonical" href="{SITE}/">', f'<link rel="canonical" href="{SITE}/">')
    out = src.replace("{{HEAD}}", hd).replace("{{HEADER}}", header(home=True)).replace("{{ZONES}}", zones).replace("{{FAQ}}", faq).replace("{{FOOTER}}", footer()).replace("{{CREST}}", crest()).replace("{{COMMUNES}}", "".join(f'<option value="{E(c["name"])}">' for c in cs) + "".join(f'<option value="{E(t)}">' for t in OTHER_TOWNS))
    return "index.html", out

def build_extras():
    urls = ["", "zones-intervention.html"] + [svc_url(s) for s in SERVICES] + [city_url(c) for c in CITIES] + ["mentions-legales.html"]
    sm = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "".join(f"  <url><loc>{SITE}/{u}</loc><lastmod>{TODAY}</lastmod></url>\n" for u in urls) + "</urlset>\n"
    robots = f"""User-agent: *
Allow: /

# Moteurs IA : accès autorisé (visibilité dans ChatGPT, Perplexity, Claude, Gemini…)
User-agent: GPTBot
Allow: /
User-agent: OAI-SearchBot
Allow: /
User-agent: ChatGPT-User
Allow: /
User-agent: PerplexityBot
Allow: /
User-agent: ClaudeBot
Allow: /
User-agent: Claude-SearchBot
Allow: /
User-agent: Google-Extended
Allow: /

Sitemap: {SITE}/sitemap.xml
"""
    llms = f"""# Harmonie Peinture

> Entreprise artisanale de peinture, plâtrerie (plaques de plâtre), isolation RGE, carrelage et revêtements de sol, basée à Malleval (Loire, 42520), en activité depuis 1999. Cinq artisans salariés, sans sous-traitance. Certifiée Qualibat RGE. Intervient dans un rayon d'environ 35 km autour de Malleval (Loire, Rhône, Isère, Ardèche, nord de la Drôme).

## Fiche entreprise
- Raison sociale : Harmonie Peinture (SASU, capital 22 000 €)
- Adresse : {ADDR['street']}, {ADDR['cp']} {ADDR['city']}, France
- Téléphone : {TEL} (Laurent Koy, chef d'entreprise) · {TEL2} (Nicolas Bonnet, associé fondateur)
- Horaires : lundi au vendredi, 8 h – 17 h ; fermé le week-end
- Chef d'entreprise : Laurent Koy
- Création de l'activité : 1999
- Effectif : 5 artisans salariés (peintres et plaquistes)
- SIREN : 887 942 720 · RCS Saint-Étienne · NAF 43.34Z
- Certification : Qualibat RGE (plaques de plâtre ; isolation des murs, rampants et plafonds ; combles perdus ; planchers bas)
- Avis clients : note moyenne de 4,6/5 sur Google
- Devis : gratuit, après visite, sans engagement

## Métiers
""" + "".join(f"- [{s['name']}]({SITE}/{svc_url(s)}) : {s['desc']}\n" for s in SERVICES) + """
## Zones d'intervention
""" + "".join(f"- [Peintre à {c['name']} ({c['cp']}, {c['dep']})]({SITE}/{city_url(c)}) : {('siège de l’entreprise' if c['dist']==0 else 'environ ' + str(c['dist']) + ' km de Malleval')}\n" for c in sorted(CITIES, key=lambda c: c['dist'])) + "- Autres communes proches : " + ", ".join(OTHER_TOWNS) + "\n" + """
## Questions fréquentes
""" + "".join(f"- {q} {a}\n" for q, a in FAQ_HOME)
    for name, content in [("sitemap.xml", sm), ("robots.txt", robots), ("llms.txt", llms)]:
        open(os.path.join(ROOT, name), "w", encoding="utf-8").write(content)

if __name__ == "__main__":
    pages = [build_index(), build_hub()] + [build_service(s) for s in SERVICES] + [build_city(c) for c in CITIES]
    for p, h in pages:
        open(os.path.join(ROOT, p), "w", encoding="utf-8").write(h)
    build_extras()
    print(len(pages), "pages")
