import json, html
E=html.escape
FONTS='''<link rel="stylesheet" href="node_modules/@fontsource/urbanist/600.css"><link rel="stylesheet" href="node_modules/@fontsource/urbanist/700.css"><link rel="stylesheet" href="node_modules/@fontsource/urbanist/800.css"><link rel="stylesheet" href="node_modules/@fontsource/inter/400.css"><link rel="stylesheet" href="node_modules/@fontsource/inter/500.css"><link rel="stylesheet" href="node_modules/@fontsource/inter/600.css">'''
LOGO='''<svg viewBox="0 0 120 120" class="{c}"><path d="M84 26V94" stroke="{w}" stroke-width="12" stroke-linecap="round" fill="none"/><path d="M84 26V50" stroke="#C2531B" stroke-width="12" stroke-linecap="round" fill="none"/><circle cx="36" cy="27" r="7.5" fill="{f}"/><path d="M36 44V94" stroke="{f}" stroke-width="12" stroke-linecap="round" fill="none"/><path d="M36 62L69 42" stroke="{f}" stroke-width="6" stroke-linecap="round" fill="none"/><circle cx="69" cy="42" r="8.5" fill="{f}"/><circle cx="69" cy="42" r="2.6" fill="{h}"/><path d="M48 82H63L61 96H50Z" fill="{f}"/></svg>'''
def logo(dark=True,c='lg'): return LOGO.format(c=c,w='#3C705A' if dark else '#E6E0D0',f='#F4F1E6' if dark else '#1F4D3A',h='#1F4D3A' if dark else '#F4F1E6')
GRAIN='''<svg class="grain" width="1080" height="1350"><filter id="n"><feTurbulence type="fractalNoise" baseFrequency=".85" numOctaves="3" stitchTiles="stitch"/></filter><rect width="100%" height="100%" filter="url(#n)"/></svg>'''
CSS='''html,body{margin:0}*{box-sizing:border-box}
.p{width:1080px;height:1350px;position:relative;overflow:hidden;font-family:Inter,sans-serif}
.grain{position:absolute;inset:0;opacity:.13;mix-blend-mode:overlay;pointer-events:none;z-index:9}
.g{background:#1F4D3A;color:#F4F1E6}.c{background:#F4F1E6;color:#111412}.s{background:#CFE8EE;color:#111412}
.grid{position:absolute;left:72px;right:72px;top:72px;bottom:72px;background-image:linear-gradient(rgba(244,241,230,.13) 1.5px,transparent 1.5px),linear-gradient(90deg,rgba(244,241,230,.13) 1.5px,transparent 1.5px);background-size:93.3px 93.3px;border-right:1.5px solid rgba(244,241,230,.13);border-bottom:1.5px solid rgba(244,241,230,.13)}
.c .grid{background-image:linear-gradient(rgba(31,77,58,.1) 1.5px,transparent 1.5px),linear-gradient(90deg,rgba(31,77,58,.1) 1.5px,transparent 1.5px);border-color:rgba(31,77,58,.1)}
.k{font:600 22px Inter;letter-spacing:.24em;text-transform:uppercase}
.g .k{color:#CFE8EE}.c .k,.s .k{color:#1F4D3A}
.top{position:absolute;left:80px;right:80px;top:80px;display:flex;justify-content:space-between;align-items:center;z-index:3}
.lg{width:84px;height:84px}
.foot{position:absolute;left:80px;right:80px;bottom:72px;display:flex;justify-content:space-between;align-items:flex-end;z-index:3;font:600 22px Inter;letter-spacing:.2em;text-transform:uppercase}
.g .foot{color:rgba(244,241,230,.7)}.c .foot,.s .foot{color:#3A4440}
h1{margin:0;font-family:Urbanist,sans-serif;font-weight:700;letter-spacing:-.045em;line-height:.92}
.big{position:absolute;left:80px;right:80px;bottom:170px;z-index:3}
.big h1{font-size:128px}
.big h1 em{font-style:normal;color:#CFE8EE}
.c .big h1 em,.s .big h1 em{color:#1F4D3A}
.big p{font:400 34px/1.45 Inter;margin:36px 0 0;max-width:820px;opacity:.85}
/* photo */
.ph{position:absolute;left:0;right:0;top:0;height:900px;background-size:cover;background-position:center}
.ph::after{content:"";position:absolute;inset:0;background:linear-gradient(180deg,rgba(0,0,0,.25),transparent 30%)}
.ph .tag{position:absolute;left:56px;top:56px;background:rgba(244,241,230,.92);color:#1F4D3A;border-radius:999px;padding:16px 26px;font:600 22px Inter;letter-spacing:.16em;text-transform:uppercase;z-index:2}
.pb{position:absolute;left:0;right:0;bottom:0;height:450px;padding:64px 80px;background:#1F4D3A;color:#F4F1E6;background-image:repeating-linear-gradient(90deg,rgba(255,255,255,.035) 0 90px,transparent 90px 180px)}
.pb h1{font-size:76px;line-height:.98}
.pb p{font:400 28px/1.45 Inter;margin:22px 0 0;color:rgba(244,241,230,.8);max-width:820px}
.pb .lg{position:absolute;right:72px;top:64px;width:72px;height:72px}
/* number */
.num{position:absolute;left:68px;top:250px;font:800 470px/0.8 Urbanist;letter-spacing:-.07em;z-index:3}
/* quote */
.q{position:absolute;left:80px;right:80px;top:0;bottom:0;z-index:3;display:flex;flex-direction:column;justify-content:center}
.q .st{color:#F4B400;font-size:54px;letter-spacing:8px}
.q blockquote{margin:44px 0 0;font:700 76px/1.06 Urbanist;letter-spacing:-.035em;position:relative}

.q .by{margin-top:56px;font:500 30px Inter;color:#3A4440}.q .by b{color:#111412;font-weight:600}
/* tips */
.tips{position:absolute;left:80px;right:80px;top:470px;z-index:3;display:grid;gap:0}
.tips div{display:grid;grid-template-columns:110px 1fr;gap:20px;padding:30px 0;border-top:2px solid rgba(31,77,58,.25);align-items:baseline}
.tips b{font:700 60px Urbanist;color:#1F4D3A;letter-spacing:-.03em}
.tips h3{margin:0;font:700 40px/1.1 Urbanist;letter-spacing:-.02em}
.tips p{margin:10px 0 0;font:400 26px/1.45 Inter;color:#3A4440}
.th{position:absolute;left:80px;right:80px;top:200px;z-index:3}.th h1{font-size:92px}
/* before after */
.ba{position:absolute;left:0;right:0;top:0;height:1350px;display:grid;grid-template-rows:1fr 1fr}
.ba div{background-size:cover;background-position:center;position:relative}
.ba span{position:absolute;left:56px;top:56px;background:rgba(17,20,18,.6);color:#fff;border-radius:999px;padding:14px 26px;font:600 24px Inter;letter-spacing:.18em;text-transform:uppercase}
.ba .ap span{background:#F4F1E6;color:#1F4D3A}
.bal{position:absolute;left:0;right:0;top:672px;height:6px;background:#F4F1E6;z-index:2}
.bat{position:absolute;right:56px;bottom:56px;z-index:3;background:#1F4D3A;color:#F4F1E6;border-radius:28px;padding:34px 40px;max-width:600px}
.bat h1{font-size:56px}
/* zones */
.chips{display:flex;flex-wrap:wrap;gap:14px;margin-top:44px}
.chips span{border:2px solid rgba(244,241,230,.35);border-radius:999px;padding:14px 26px;font:500 28px Inter}
.cta{display:inline-flex;align-items:center;gap:16px;margin-top:48px;background:#C2531B;color:#fff;border-radius:999px;padding:30px 50px;font:600 34px Inter}
.ball{position:absolute;width:190px;height:190px;border-radius:50%;background:radial-gradient(circle at 34% 28%,#fff,#f1f0ec 35%,#d6d5cf 70%,#b3b2ab);box-shadow:-20px 30px 40px rgba(0,0,0,.35);z-index:4}
.flag{position:absolute;z-index:4}
'''
def wrap(cls,body,grain=True): return f'<div class="p {cls}">{body}{GRAIN if grain else ""}</div>'
def top(k,dark=True): return f'<div class="top"><span class="k">{k}</span>{logo(dark)}</div>'
def foot(dark=True,l='Harmonie Peinture',r='Malleval · 42'): return f'<div class="foot"><span>{l}</span><span>{r}</span></div>'
def photo(img,tag,h,p,pos='center'):
    return wrap('g',f'<div class="ph" style="background-image:url({img});background-position:{pos}"><span class="tag">{tag}</span></div><div class="pb">{logo(True)}<h1>{h}</h1><p>{p}</p></div>',grain=False)
def typo(k,h,p,cls='g',extra=''):
    dark=cls=='g'
    return wrap(cls,f'<div class="grid"></div>{top(k,dark)}<div class="big"><h1>{h}</h1>{f"<p>{p}</p>" if p else ""}{extra}</div>{foot(dark)}')
def number(k,n,h,p,cls='g'):
    dark=cls=='g'
    return wrap(cls,f'<div class="grid"></div>{top(k,dark)}<div class="num">{n}</div><div class="big"><h1 style="font-size:92px">{h}</h1><p>{p}</p></div>{foot(dark)}')
def quote(txt,name,city=''):
    return wrap('c',f'{top("Avis Google",False)}<div class="q"><div class="st">★★★★★</div><blockquote>« {txt} »</blockquote><div class="by"><b>{name}</b> · avis Google</div></div>{foot(False,"Note moyenne 4,6 sur Google","Harmonie Peinture")}')
def tips(k,h,items,cls='s'):
    rows=''.join(f'<div><b>0{i+1}</b><span><h3>{a}</h3><p>{b}</p></span></div>' for i,(a,b) in enumerate(items))
    return wrap(cls,f'{top(k,False)}<div class="th"><h1>{h}</h1></div><div class="tips">{rows}</div>{foot(False)}')
def ba(av,ap,h):
    return wrap('g',f'<div class="ba"><div style="background-image:url({av})"><span>Avant</span></div><div class="ap" style="background-image:url({ap})"><span>Après</span></div></div><div class="bal"></div><div class="bat"><h1>{h}</h1></div>',grain=False)
FLAG='<svg class="flag" style="right:120px;top:300px" width="150" height="260" viewBox="0 0 150 260"><path d="M20 250V20" stroke="#F4F1E6" stroke-width="6" stroke-linecap="round"/><path d="M20 20l100 34-100 34z" fill="#C2531B"/><ellipse cx="20" cy="252" rx="36" ry="9" fill="rgba(0,0,0,.25)"/></svg>'
POSTS=[
 ("01-lancement", photo("img/m-cuisine.jpg","Nouveau site","Le travail bien fait,<br>du sol au plafond.","Peinture, plâtrerie, isolation RGE et sols, autour de Malleval. Découvrez nos chantiers sur harmonie-peinture.fr")),
 ("02-depuis-1999", typo("Notre histoire","Depuis<br><em>1999.</em>","Plus de 25 ans à peindre, plâtrer et isoler les maisons du Pilat rhodanien et de la vallée du Rhône.")),
 ("03-avant-apres", ba("img/r-avant.jpg","img/r-apres.jpg","Même pièce.<br>Autre vie.")),
 ("04-avis-annie", quote("En 1 semaine fait. Le travail très bien et personnel exceptionnel au service de son client.","Annie Q.")),
 ("05-chiffre-50", number("En chiffres","+50","chantiers chaque année.","Maisons, appartements, bureaux et commerces, de Chavanay à Annonay.")),
 ("06-conseil-repeindre", tips("Conseil de peintre","3 signes qu'un mur<br>doit être repeint.",[("Il farine","Passez la main : si elle blanchit, la peinture ne protège plus le support."),("Il fissure","Les microfissures laissent entrer l'humidité : à reboucher avant de peindre."),("Il se tache","Une peinture lessivable bien posée se nettoie ; sinon, il est temps.")])),
 ("07-salle-de-bains", photo("img/m-sdb.jpg","Salle de bains","Faïence, peinture,<br>finitions nettes.","Dans une pièce humide, tout se joue sur la préparation et le choix des produits.")),
 ("08-rge-aides", typo("Certifiée Qualibat RGE","Isoler,<br><em>avec des aides.</em>","Nos travaux d'isolation peuvent ouvrir droit à MaPrimeRénov', aux primes énergie et à l'éco-PTZ, sous conditions.",'s')),
 ("09-avis-sebastien", quote("Société hyper compétente, avec une superbe équipe, je recommande fortement !","Sébastien P.")),
 ("10-sans-sous-traitance", typo("Notre équipe","5 artisans.<br><em>0 sous-traitant.</em>","Peintres et plaquistes, tous salariés de l'entreprise. La même équipe du premier au dernier jour.")),
 ("11-chambre", photo("img/m-chambre.jpg","Chambre","Des murs calmes,<br>une pièce qui respire.","Murs repris, peinture mate, sol posé. Le genre de chantier qu'on aime rendre.")),
 ("12-conseil-finitions", tips("Conseil de peintre","Mat, velours<br>ou satiné ?",[("Mat","Cache les défauts, rendu doux. Idéal plafonds, chambres, salons."),("Velours","Le bon compromis : légèrement lavable, reflet discret. Pièces de vie."),("Satiné","Lessivable et résistant. Cuisines, salles de bains, boiseries.")],'c')),
 ("13-zones", typo("Où nous intervenons","On arrive<br><em>près de chez vous.</em>","",'g','<div class="chips"><span>Malleval</span><span>Chavanay</span><span>Pélussin</span><span>Condrieu</span><span>Vienne</span><span>Roussillon</span><span>Serrières</span><span>Annonay</span><span>Rayon 35 km</span></div>')),
 ("14-avis-annick", quote("Je tiens à remercier toute l'équipe pour son efficacité, son sérieux et son résultat professionnel ! Bravo, je conseille.","Annick R.")),
 ("15-platrerie", photo("img/r-placo.jpg","En chantier","Avant la peinture,<br>il y a la plâtrerie.","Plaques, bandes, joints : la partie qu'on ne voit plus, mais qui fait tout.")),
 ("16-un-interlocuteur", number("Notre façon de travailler","1","seul interlocuteur.","Laurent Koy vous suit du devis à la réception. Pas de commercial, pas d'intermédiaire.",'c')),
 ("17-conseil-combles", tips("Conseil isolation","Le toit,<br>premier fuyard.",[("Jusqu'à 30 %","de la chaleur d'une maison mal isolée s'échappe par la toiture (source : ADEME)."),("Combles perdus","Souvent le chantier d'isolation le plus rentable, réalisé en peu de temps."),("Entreprise RGE","Condition pour prétendre aux aides : c'est notre cas.")])),
 ("18-sejour", photo("img/m-sejour.jpg","Séjour","La lumière,<br>ça se travaille.","Murs clairs, plafond net, menuiseries reprises : la pièce paraît plus grande.")),
 ("19-avis-christine", quote("Merci pour les soins apportés à nos travaux. Excellent travail.","Christine K.")),
 ("20-devis", typo("Devis gratuit","Un projet ?<br><em>Parlons-en.</em>","Laurent vous rappelle, vient voir votre projet et vous remet un devis détaillé, gratuit et sans engagement.",'g','<div class="cta">06 69 19 05 77</div>')),
]
for slug,body in POSTS:
    open(f'{slug}.html','w').write(f'<!DOCTYPE html><html><head><meta charset="utf-8">{FONTS}<style>{CSS}</style></head><body>{body}</body></html>')
json.dump([s for s,_ in POSTS],open('list.json','w'))
