import sys,json
sys.path.insert(0,'/home/claude/brand/posts')
from posts import FONTS, CSS as BASE, logo, wrap, top, foot, typo, number, quote, tips, ba, photo
LOGOC='''<svg viewBox="0 0 120 120" class="{c}"><path d="M84 26V94" stroke="{w}" stroke-width="12" stroke-linecap="round" fill="none"/><path d="M84 26V50" stroke="#C2531B" stroke-width="12" stroke-linecap="round" fill="none"/><circle cx="36" cy="27" r="7.5" fill="{f}"/><path d="M36 44V94" stroke="{f}" stroke-width="12" stroke-linecap="round" fill="none"/><path d="M36 62L69 42" stroke="{f}" stroke-width="6" stroke-linecap="round" fill="none"/><circle cx="69" cy="42" r="8.5" fill="{f}"/><circle cx="69" cy="42" r="2.6" fill="{h}"/><path d="M48 82H63L61 96H50Z" fill="{f}"/></svg>'''
def lg(c,w='rgba(244,241,230,.35)',f='#F4F1E6',h='#1b2a23'): return LOGOC.format(c=c,w=w,f=f,h=h)
CSS=BASE+'''
.hk{background:#0f1a15;color:#F4F1E6}
.hk .bg{position:absolute;inset:0;background-size:cover;background-position:center}
.hk .bg::after{content:"";position:absolute;inset:0;background:linear-gradient(180deg,rgba(9,18,14,.55) 0,rgba(9,18,14,.08) 22%,rgba(9,18,14,.1) 45%,rgba(9,18,14,.86) 78%,rgba(9,18,14,.96) 100%)}
.hk .bar{position:absolute;left:72px;right:72px;top:68px;display:flex;justify-content:space-between;align-items:center;z-index:3}
.hk .brand{display:flex;align-items:center;gap:14px;font:700 30px Urbanist;letter-spacing:-.02em}
.hk .brand .i{width:54px;height:54px}
.hk .pill{font:600 20px Inter;letter-spacing:.2em;text-transform:uppercase;padding:14px 22px;border-radius:999px;background:rgba(244,241,230,.14);backdrop-filter:blur(10px);border:1px solid rgba(244,241,230,.25)}
.hk .txt{position:absolute;left:72px;right:72px;bottom:150px;z-index:3}
.hk h1{font-size:var(--fs,100px);line-height:.95;letter-spacing:-.05em}
.hk h1 em{font-style:normal;color:#CFE8EE}
.hk p{font:400 32px/1.4 Inter;color:rgba(244,241,230,.84);margin:30px 0 0;max-width:860px}
.hk .bt{position:absolute;left:72px;right:72px;bottom:64px;z-index:3;display:flex;justify-content:space-between;font:600 21px Inter;letter-spacing:.18em;text-transform:uppercase;color:rgba(244,241,230,.62);border-top:1px solid rgba(244,241,230,.22);padding-top:26px}
.hk .bt b{color:#F2B48F;font-weight:600}
.lgp{background:#0f1a15}
.lgp .bg{position:absolute;inset:0;background-size:cover;background-position:center;filter:saturate(.8)}
.lgp .bg::after{content:"";position:absolute;inset:0;background:rgba(10,24,18,.52)}
.lgp .lk{position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center;z-index:3;color:#F4F1E6}
.lgp .lk .i{width:190px;height:190px}
.lgp .lk b{font:700 150px/1 Urbanist;letter-spacing:-.05em;margin-top:18px}
.lgp .lk small{font:600 26px Inter;letter-spacing:.7em;text-transform:uppercase;margin-top:20px;color:#CFE8EE;padding-left:.7em}
.lgp .bt{position:absolute;left:0;right:0;bottom:70px;text-align:center;font:600 22px Inter;letter-spacing:.24em;text-transform:uppercase;color:rgba(244,241,230,.75);z-index:3}
.mo{display:grid;grid-template-columns:repeat(3,1fr);grid-template-rows:repeat(3,1fr);gap:0;width:1080px;height:1350px}
.mo div{background-size:cover;background-position:center;position:relative}
.mo .g{background:#1F4D3A;display:flex;flex-direction:column;align-items:center;justify-content:center;color:#F4F1E6;text-align:center;padding:20px}
.mo .g .i{width:96px;height:96px}
.mo .g b{font:700 50px/1 Urbanist;letter-spacing:-.04em;margin-top:12px}
.mo .g small{font:600 13px Inter;letter-spacing:.5em;text-transform:uppercase;color:#CFE8EE;margin-top:10px}
.mo .t{background:#F4F1E6;display:flex;align-items:flex-end;padding:30px;color:#1F4D3A;font:700 44px/1 Urbanist;letter-spacing:-.04em}
.pal{background:#F4F1E6}
.pal .sw{position:absolute;left:72px;right:72px;top:470px;bottom:150px;display:grid;grid-template-columns:repeat(4,1fr);gap:14px}
.pal .sw div{border-radius:26px;position:relative;padding:26px;display:flex;flex-direction:column;justify-content:flex-end;font:700 30px/1.1 Urbanist;letter-spacing:-.02em}
.pal .sw small{display:block;font:500 18px Inter;letter-spacing:.12em;margin-top:8px;opacity:.75}
.pal .th{top:190px}
.mk{background:#0f1a15}
.mk .bg{position:absolute;inset:0;background-size:cover;background-position:center}
.mk .stamp{position:absolute;z-index:2;mix-blend-mode:multiply;opacity:.92;display:flex;align-items:center;gap:22px;color:#1F4D3A}
.mk .stamp .i{width:150px;height:150px}
.mk .stamp b{font:700 120px/1 Urbanist;letter-spacing:-.05em}
'''
import re
def fs(h):
    L=max(len(re.sub('<[^>]+>','',x)) for x in h.split('<br>'))
    return 100 if L<=18 else 90 if L<=22 else 80 if L<=26 else 72
def hook(img,pill,h,p='',pos='center',cta='Devis gratuit'):
    return f'''<div class="p hk"><div class="bg" style="background-image:url({img});background-position:{pos}"></div>
<div class="bar"><span class="brand">{lg("i")}Harmonie</span><span class="pill">{pill}</span></div>
<div class="txt"><h1 style="--fs:{fs(h)}px">{h}</h1>{f"<p>{p}</p>" if p else ""}</div>
<div class="bt"><span>harmonie-peinture.com</span><span><b>{cta}</b> · 06 69 19 05 77</span></div></div>'''
def lgpost(img,bt='Peinture · Plâtrerie · Isolation · Sols',pos='center'):
    return f'''<div class="p lgp"><div class="bg" style="background-image:url({img});background-position:{pos}"></div>
<div class="lk">{lg("i")}<b>Harmonie</b><small>Peinture</small></div><div class="bt">{bt}</div></div>'''
def mosaic(imgs,center='logo',txt=''):
    cells=[]
    for i,im in enumerate(imgs):
        if i==4:
            cells.append(f'<div class="g">{lg("i")}<b>Harmonie</b><small>Peinture</small></div>' if center=='logo' else f'<div class="g"><b style="font-size:56px">{txt}</b></div>')
        elif im.startswith('T:'): cells.append(f'<div class="t">{im[2:]}</div>')
        else: cells.append(f'<div style="background-image:url({im})"></div>')
    return '<div class="p">'+'<div class="mo">'+''.join(cells)+'</div></div>'
def palette(k,h,cols):
    sw=''.join(f'<div style="background:{c};color:{t}">{n}<small>{code}</small></div>' for n,code,c,t in cols)
    return wrap('c',f'{top(k,False)}<div class="th"><h1 style="font-size:92px">{h}</h1></div><div class="sw">{sw}</div>{foot(False)}').replace('<div class="th">','<div class="th" style="position:absolute;left:80px;right:80px;top:190px">',1)
def mock(img,left,top_,rot,size=1,pos='center'):
    return f'''<div class="p mk"><div class="bg" style="background-image:url({img});background-position:{pos}"></div>
<div class="stamp" style="left:{left}px;top:{top_}px;transform:rotate({rot}deg) scale({size})">{lg("i","#7FA493","#1F4D3A","#ffffff")}<b>Harmonie</b></div></div>'''
from posts import GRAIN
def palette(k,h,cols):
    sw=''.join(f'<div style="background:{c};color:{t}">{n}<small>{code}</small></div>' for n,code,c,t in cols)
    return f'<div class="p c pal">{top(k,False)}<div style="position:absolute;left:80px;right:80px;top:200px;z-index:3"><h1 style="font-size:92px">{h}</h1></div><div class="sw">{sw}</div>{foot(False)}{GRAIN}</div>'
P='ph/'
POSTS=[
 ("01-coup-de-propre", hook(P+'p68.jpg','Peinture intérieure','Besoin d’un coup de propre<br>sur vos murs ?<br><em>Passez par nous.</em>','Préparation, deux couches, chantier rendu propre. Devis gratuit après visite.')),
 ("02-logo-rouleau", lgpost(P+'p20.jpg')),
 ("03-deux-couches", hook(P+'p22.jpg','Notre méthode','Un mur.<br>Deux couches.<br><em>Zéro trace.</em>','La différence entre un mur repeint et un mur bien repeint.','center 30%')),
 ("04-cuisine", photo(P+'m-cuisine.jpg','Chantier','Une cuisine repeinte,<br>du sol au plafond.','Murs, plafond et boiseries par nos équipes, autour de Malleval.')),
 ("05-depuis-1999", typo('Notre histoire','Peintres, plaquistes,<br><em>artisans. Depuis 1999.</em>','Une entreprise locale, une équipe salariée, une exigence qui ne change pas.')),
 ("06-preparation", hook(P+'p41.jpg','Plâtrerie','Avant la peinture,<br><em>il y a la préparation.</em>','Rebouchage, enduit, ponçage : 80 % d’un beau résultat se joue ici.','center 20%')),
 ("07-avis-annie", quote('En 1 semaine fait. Le travail très bien et personnel exceptionnel au service de son client.','Annie Q.')),
 ("08-carreau-fendu", hook(P+'p43.jpg','Carrelage','Un carreau fendu ?<br><em>On le remplace.</em><br>Pas toute la pièce.','Remplacement de carreaux sans casser les voisins.','center 35%')),
 ("09-mosaique-metiers", mosaic([P+'p20.jpg',P+'p49.jpg',P+'p61.jpg',P+'m-sdb.jpg','',P+'p23.jpg',P+'p67.jpg',P+'m-chambre.jpg',P+'p71.jpg'])),
 ("10-conseil-repeindre", tips('Conseil de peintre','3 signes qu’un mur<br>doit être repeint.',[('Il farine','Passez la main : si elle blanchit, la peinture ne protège plus le support.'),('Il fissure','Les microfissures laissent entrer l’humidité : à reboucher avant de peindre.'),('Il se tache','Une peinture lessivable bien posée se nettoie ; sinon, il est temps.')])),
 ("11-couleur", hook(P+'p37.jpg','Couleurs','Envie de couleur ?<br><em>On ose avec vous.</em>','Mur d’accent, pièce entière ou simple touche : on vous conseille la bonne teinte.')),
 ("12-palette", palette('Tendances','Les teintes<br>du moment.',[('Vert sapin','Mur d’accent','#1F4D3A','#F4F1E6'),('Blanc cassé','Pièces de vie','#EFEBE0','#111412'),('Terracotta','Touche chaude','#C2531B','#fff'),('Bleu brume','Chambres','#CFE8EE','#111412')])),
 ("13-combles", hook(P+'p66.jpg','Aménagement','Vos combles peuvent<br><em>devenir une pièce.</em>','Isolation RGE, plaques de plâtre, peinture : une seule équipe.')),
 ("14-avant-apres", ba(P+'r-avant.jpg',P+'r-apres.jpg','Même pièce.<br>Autre vie.')),
 ("15-logo-pots", lgpost(P+'p64.jpg','Depuis 1999 · Malleval')),
 ("16-plafonds-hauts", hook(P+'p36.jpg','Plafonds & cages d’escalier','Plafonds hauts ?<br><em>On a les échelles.</em>','Cages d’escalier, mezzanines, grandes hauteurs : en toute sécurité.','center 25%')),
 ("17-chiffre-50", number('En chiffres','+50','chantiers chaque année.','Maisons, appartements, bureaux et commerces, de Chavanay à Annonay.')),
 ("18-finitions", hook(P+'p55.jpg','Le détail','Les finitions,<br><em>c’est là que tout se joue.</em>','Angles nets, raccords invisibles, plinthes propres.')),
 ("19-avis-sebastien", quote('Société hyper compétente, avec une superbe équipe, je recommande fortement !','Sébastien P.')),
 ("20-salle-de-bains", hook(P+'p45.jpg','Salle de bains','Une salle de bains<br><em>qui vous ressemble.</em>','Faïence, peinture adaptée aux pièces humides, finitions soignées.')),
 ("21-devis-gratuit", typo('Notre engagement','Devis gratuit.<br><em>Visite sur place.</em>','Laurent vient voir votre projet et vous remet un devis détaillé, poste par poste.')),
 ("22-proteger-preparer", hook(P+'p27.jpg','Notre méthode','On protège.<br>On prépare.<br><em>On peint.</em>','Sols bâchés, meubles protégés, chantier rendu propre chaque soir.')),
 ("23-conseil-finitions", tips('Conseil de peintre','Mat, velours<br>ou satiné ?',[('Mat','Cache les défauts, rendu doux. Idéal plafonds, chambres, salons.'),('Velours','Le bon compromis : légèrement lavable, reflet discret. Pièces de vie.'),('Satiné','Lessivable et résistant. Cuisines, salles de bains, boiseries.')],'c')),
 ("24-boiseries", hook(P+'p69.jpg','Boiseries','Fenêtres, portes,<br>boiseries :<br><em>on fait aussi.</em>','Ponçage, sous-couche adaptée, laque soignée.','center 30%')),
 ("25-sdb-chantier", photo(P+'m-sdb.jpg','Chantier','Faïence, peinture,<br>finitions nettes.','Dans une pièce humide, tout se joue sur la préparation et le choix des produits.')),
 ("26-logo-pinceau", lgpost(P+'p57.jpg','Le travail bien fait, du sol au plafond')),
 ("27-carrelage", hook(P+'p51.jpg','Carrelage','Carrelage posé<br><em>au millimètre.</em>','Support préparé, pose de niveau, joints réguliers.')),
 ("28-un-interlocuteur", number('Notre façon de travailler','1','seul interlocuteur.','Laurent Koy vous suit du devis à la réception. Pas de commercial, pas d’intermédiaire.','c')),
 ("29-pot-de-peinture", hook(P+'p60.jpg','Le métier','Un pot de peinture<br><em>ne fait pas un peintre.</em>','La préparation, le geste et les bons produits, si.')),
 ("30-avis-annick", quote('Je tiens à remercier toute l’équipe pour son efficacité, son sérieux et son résultat professionnel ! Bravo, je conseille.','Annick R.')),
 ("31-rge-aides", typo('Certifiée Qualibat RGE','Isoler,<br><em>avec des aides.</em>','Nos travaux d’isolation peuvent ouvrir droit à MaPrimeRénov’, aux primes énergie et à l’éco-PTZ, sous conditions.','s')),
 ("32-professionnels", hook(P+'p74.jpg','Professionnels','Bureaux, commerces,<br>locaux :<br><em>on intervient aussi.</em>','Un chantier organisé pour ne pas arrêter votre activité.')),
 ("33-mosaique-gestes", mosaic([P+'p53.jpg',P+'p25.jpg',P+'p42.jpg',P+'p21.jpg','',P+'p58.jpg',P+'p50.jpg',P+'p19.jpg',P+'p35.jpg'],'txt','Le geste<br>juste.')),
 ("34-25-ans", hook(P+'p17.jpg','Savoir-faire','25 ans de métier.<br><em>La même exigence.</em>','Depuis 1999, chaque chantier est suivi comme le premier.')),
 ("35-conseil-combles", tips('Conseil isolation','Le toit,<br>premier fuyard.',[('Jusqu’à 30 %','de la chaleur d’une maison mal isolée s’échappe par la toiture (source : ADEME).'),('Combles perdus','Souvent le chantier d’isolation le plus rentable.'),('Entreprise RGE','Condition pour prétendre aux aides : c’est notre cas.')])),
 ("36-bons-produits", hook(P+'p62.jpg','Nos produits','On choisit les bons produits.<br><em>Pour que ça dure.</em>','Peintures professionnelles adaptées à chaque pièce et chaque support.')),
 ("37-chambre", photo(P+'m-chambre.jpg','Chantier','Des murs calmes,<br>une pièce qui respire.','Murs repris, peinture mate, sol posé.')),
 ("38-avant-de-vendre", hook(P+'p20.jpg','Vente ou location','Vous vendez ?<br><em>Repeignez d’abord.</em>','Des murs frais donnent envie de visiter. Et de signer.','center 40%')),
 ("39-sans-sous-traitance", typo('Notre équipe','5 artisans.<br><em>0 sous-traitant.</em>','Peintres et plaquistes, tous salariés de l’entreprise. La même équipe du premier au dernier jour.')),
 ("40-fissures", hook(P+'p67.jpg','Réparation','Fissures, trous,<br>bosses :<br><em>on rebouche tout.</em>','Avant de peindre, un support parfaitement lisse.')),
 ("41-avis-christine", quote('Merci pour les soins apportés à nos travaux. Excellent travail.','Christine K.')),
 ("42-facades", hook(P+'p39.jpg','Extérieur','Façades :<br><em>on prend de la hauteur.</em>','Diagnostic du support, nettoyage, peinture adaptée aux intempéries.')),
 ("43-zones", typo('Où nous intervenons','On arrive<br><em>près de chez vous.</em>','','g','<div class="chips"><span>Malleval</span><span>Chavanay</span><span>Pélussin</span><span>Condrieu</span><span>Vienne</span><span>Roussillon</span><span>Serrières</span><span>Annonay</span><span>Rayon 35 km</span></div>')),
 ("44-une-couleur-par-piece", hook(P+'p71.jpg','Conseil couleur','Une couleur par pièce ?<br><em>On vous conseille.</em>','Lumière, usage, mobilier : on choisit ensemble.')),
 ("45-logo-chantier", lgpost(P+'p73.jpg','Rénovation · Malleval · Loire')),
 ("46-faience", hook(P+'p48.jpg','Salle de bains','Faïence et peinture<br><em>de salle de bains.</em>','Des matériaux faits pour l’humidité, posés pour durer.')),
 ("47-sejour", photo(P+'m-sejour.jpg','Chantier','La lumière,<br>ça se travaille.','Murs clairs, plafond net, menuiseries reprises.')),
 ("48-volets", hook(P+'p35.jpg','Extérieur','Volets et boiseries<br>extérieures :<br><em>c’est la saison.</em>','Une lasure ou une peinture bien posée protège le bois pour des années.','center 30%')),
 ("49-signature", typo('Harmonie Peinture','Chaque mur,<br><em>un sans-faute.</em>','Peinture, plâtrerie, isolation RGE, carrelage et sols autour de Malleval.')),
 ("50-devis", typo('Devis gratuit','Un projet ?<br><em>Parlons-en.</em>','Laurent vous rappelle, vient voir votre projet et vous remet un devis détaillé, gratuit et sans engagement.','g','<div class="cta">06 69 19 05 77</div>')),
]
if __name__=='__main__':
    import os
    for slug,body in POSTS:
        for a in [' ?',' :',' !',' ;']:
            body=body.replace(a,'\u00a0'+a[1:])
        open(f'{slug}.html','w').write(f'<!DOCTYPE html><html><head><meta charset="utf-8">{FONTS}<style>{CSS}</style></head><body>{body}</body></html>')
    json.dump([s for s,_ in POSTS],open('list.json','w'))
    print(len(POSTS))
