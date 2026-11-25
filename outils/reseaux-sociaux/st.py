import sys,json,re
sys.path.insert(0,'/home/claude/brand/posts2');sys.path.insert(0,'/home/claude/brand/posts')
from posts import FONTS
LOGOC='''<svg viewBox="0 0 120 120" class="{c}"><path d="M84 26V94" stroke="{w}" stroke-width="12" stroke-linecap="round" fill="none"/><path d="M84 26V50" stroke="#C2531B" stroke-width="12" stroke-linecap="round" fill="none"/><circle cx="36" cy="27" r="7.5" fill="{f}"/><path d="M36 44V94" stroke="{f}" stroke-width="12" stroke-linecap="round" fill="none"/><path d="M36 62L69 42" stroke="{f}" stroke-width="6" stroke-linecap="round" fill="none"/><circle cx="69" cy="42" r="8.5" fill="{f}"/><circle cx="69" cy="42" r="2.6" fill="{h}"/><path d="M48 82H63L61 96H50Z" fill="{f}"/></svg>'''
def lg(c,dark=True): return LOGOC.format(c=c,w='rgba(244,241,230,.35)' if dark else '#E6E0D0',f='#F4F1E6' if dark else '#1F4D3A',h='#1b2a23' if dark else '#F4F1E6')
G='<svg width="40" height="40" viewBox="0 0 48 48"><path fill="#4285F4" d="M45 24.5c0-1.6-.1-3.1-.4-4.5H24v8.5h11.8c-.5 2.7-2 5-4.4 6.6v5.5h7.1c4.2-3.8 6.5-9.5 6.5-16.1z"/><path fill="#34A853" d="M24 46c5.9 0 10.9-2 14.5-5.4l-7.1-5.5c-2 1.3-4.5 2.1-7.4 2.1-5.7 0-10.5-3.8-12.2-9H4.5v5.7C8.1 41.1 15.5 46 24 46z"/><path fill="#FBBC05" d="M11.8 28.2c-.4-1.3-.7-2.7-.7-4.2s.3-2.9.7-4.2v-5.7H4.5C3 17.1 2 20.4 2 24s1 6.9 2.5 9.9l7.3-5.7z"/><path fill="#EA4335" d="M24 10.8c3.2 0 6.1 1.1 8.4 3.3l6.3-6.3C34.9 4.2 29.9 2 24 2 15.5 2 8.1 6.9 4.5 14.1l7.3 5.7c1.7-5.2 6.5-9 12.2-9z"/></svg>'
GRAIN='<svg style="position:absolute;inset:0;opacity:.12;mix-blend-mode:overlay;z-index:9" width="1080" height="1920"><filter id="n"><feTurbulence type="fractalNoise" baseFrequency=".85" numOctaves="3"/></filter><rect width="100%" height="100%" filter="url(#n)"/></svg>'
CSS='''html,body{margin:0}*{box-sizing:border-box}
.s{width:1080px;height:1920px;position:relative;overflow:hidden;font-family:Inter,sans-serif}
h1{margin:0;font-family:Urbanist;font-weight:700;letter-spacing:-.045em;line-height:.95}
.top{position:absolute;left:80px;right:80px;top:250px;display:flex;justify-content:space-between;align-items:center;z-index:4}
.k{font:600 24px Inter;letter-spacing:.24em;text-transform:uppercase}
.lgo{width:96px;height:96px}
/* avis */
.rv{background:#F4F1E6;color:#111412}
.rv .grid{position:absolute;left:80px;right:80px;top:200px;bottom:300px;background-image:linear-gradient(rgba(31,77,58,.08) 1.5px,transparent 1.5px),linear-gradient(90deg,rgba(31,77,58,.08) 1.5px,transparent 1.5px);background-size:115px 115px}
.rv .k{color:#1F4D3A}
.rv .body{position:absolute;left:80px;right:80px;top:470px;bottom:560px;display:flex;flex-direction:column;justify-content:center;z-index:3}
.rv .st{color:#F4B400;font-size:64px;letter-spacing:10px}
.rv blockquote{margin:44px 0 0;font:700 var(--fs,74px)/1.08 Urbanist;letter-spacing:-.035em}
.rv .by{margin-top:54px;display:flex;align-items:center;gap:22px}
.rv .av{width:84px;height:84px;border-radius:50%;background:#1F4D3A;color:#F4F1E6;display:grid;place-items:center;font:700 38px Urbanist}
.rv .by b{display:block;font:700 36px Urbanist;letter-spacing:-.02em}.rv .by span{font:500 24px Inter;color:#6B7770}
.rv .bot{position:absolute;left:80px;right:80px;bottom:360px;z-index:3;display:flex;align-items:center;gap:20px;padding-top:34px;border-top:2px solid rgba(31,77,58,.2);font:600 28px Inter;color:#1F4D3A}
.rv .bot b{font:800 44px Urbanist;color:#111412;letter-spacing:-.03em}
.rv .num{margin-left:auto;font:600 24px Inter;letter-spacing:.2em;color:#6B7770}
/* sommaire avis */
.sum{background:#1F4D3A;color:#F4F1E6;background-image:repeating-linear-gradient(90deg,rgba(255,255,255,.035) 0 120px,transparent 120px 240px)}
.sum .k{color:#CFE8EE}
.sum .big{position:absolute;left:80px;right:80px;top:560px;z-index:3}
.sum .big b{display:block;font:800 380px/0.8 Urbanist;letter-spacing:-.07em}
.sum .big .st{font-size:70px;letter-spacing:12px;margin-top:40px;background:linear-gradient(90deg,#F4B400 92%,rgba(244,241,230,.3) 92%);-webkit-background-clip:text;background-clip:text;color:transparent;display:inline-block}
.sum .big p{font:400 40px/1.35 Inter;color:rgba(244,241,230,.82);margin:44px 0 0;max-width:820px}
.sum .g{position:absolute;left:80px;bottom:380px;display:flex;align-items:center;gap:18px;font:600 30px Inter;z-index:3;background:rgba(244,241,230,.1);border:1px solid rgba(244,241,230,.25);padding:22px 30px;border-radius:999px}
/* services */
.sv{background:#0f1a15;color:#F4F1E6}
.sv .bg{position:absolute;inset:0;background-size:cover;background-position:center}
.sv .bg::after{content:"";position:absolute;inset:0;background:linear-gradient(180deg,rgba(9,18,14,.6) 0,rgba(9,18,14,.1) 22%,rgba(9,18,14,.15) 40%,rgba(9,18,14,.9) 66%,#0b1611 100%)}
.sv .k{color:#CFE8EE}
.sv .txt{position:absolute;left:80px;right:80px;bottom:380px;z-index:3}
.sv .n{font:600 26px Inter;letter-spacing:.24em;color:#F2B48F;text-transform:uppercase}
.sv h1{font-size:118px;margin-top:22px}
.sv ul{list-style:none;padding:0;margin:44px 0 0;display:grid;gap:20px}
.sv li{display:flex;gap:20px;align-items:baseline;font:500 36px Inter;color:rgba(244,241,230,.9)}
.sv li::before{content:"";width:14px;height:14px;border-radius:50%;background:#C2531B;flex:none;transform:translateY(-4px)}
.sv .pill{display:inline-flex;margin-top:54px;background:#F4F1E6;color:#1F4D3A;border-radius:999px;padding:24px 36px;font:600 30px Inter}
.ix{background:#1F4D3A;color:#F4F1E6;background-image:repeating-linear-gradient(90deg,rgba(255,255,255,.035) 0 120px,transparent 120px 240px)}
.ix .k{color:#CFE8EE}
.ix .t{position:absolute;left:80px;right:80px;top:470px;z-index:3}
.ix h1{font-size:150px}
.ix ol{list-style:none;padding:0;margin:70px 0 0;counter-reset:a}
.ix li{counter-increment:a;display:flex;gap:30px;align-items:baseline;padding:22px 0;border-top:1.5px solid rgba(244,241,230,.2);font:600 44px Urbanist;letter-spacing:-.02em}
.ix li::before{content:"0" counter(a);font:600 24px Inter;letter-spacing:.2em;color:#F2B48F;width:60px}
'''
def page(cls,body): return f'<div class="s {cls}">{body}{GRAIN}</div>'
REV=[('Annie Q.','Local Guide Google','Super entreprise nous recherchons depuis près de 2 ans pour effectuer nos travaux. Et nous avons fait appel à Harmonie peinture et en 1 semaine fait. Le travail très bien et personnel exceptionnel au service de son client.'),
('Sébastien P.','Avis Google','Société hyper compétente, avec une superbe équipe, je recommande fortement !'),
('Annick R.','Avis Google','Je tiens à remercier toute l’équipe d’Harmonie Peinture pour son efficacité, son sérieux et son résultat professionnel ! Bravo, je conseille.'),
('Christine K.','Avis Google','Merci pour les soins apportés à nos travaux. Excellent travail.')]
def review(i,n,meta,txt,tot):
    L=len(txt); fs=84 if L<90 else 72 if L<150 else 62
    return page('rv',f'<div class="grid"></div><div class="top"><span class="k">Avis clients</span>{lg("lgo",False)}</div><div class="body"><div class="st">★★★★★</div><blockquote style="--fs:{fs}px">« {txt} »</blockquote><div class="by"><span class="av">{n[0]}</span><div><b>{n}</b><span>{meta}</span></div></div></div><div class="bot">{G}<b>4,6</b>/5 sur Google<span class="num">{i:02d} / {tot:02d}</span></div>')
def summary():
    return page('sum',f'<div class="top"><span class="k">Avis clients</span>{lg("lgo")}</div><div class="big"><b>4,6</b><div class="st">★★★★★</div><p>Note moyenne sur Google. Ce que nos clients disent de nous, sans retouche.</p></div><div class="g">{G}Avis vérifiés Google</div>')
SV=[('Peinture intérieure','ph/p20.jpg',['Murs et plafonds','Boiseries et portes','Préparation des supports']),
('Façades & extérieurs','ph/p39.jpg',['Façades et pignons','Volets et avant-toits','Ferronneries']),
('Plaques de plâtre','ph/r-placo.jpg',['Cloisons et doublages','Aménagement de combles','Qualification Qualibat RGE']),
('Faux plafonds','ph/r-plafond.jpg',['Plafonds suspendus','Éclairage encastré','Plafonds tendus']),
('Isolation RGE','ph/p66.jpg',['Murs et rampants','Combles perdus, planchers bas','Aides possibles (MaPrimeRénov’)']),
('Carrelage','ph/p43.jpg',['Sols et murs','Salles de bains, crédences','Remplacement de carreaux']),
('Revêtements de sol','ph/m-chambre-3.jpg',['Parquet et stratifié','Vinyle et lino','Réparation de lames']),
('Réparations','ph/p67.jpg',['Fissures et trous','Plaques abîmées','Carreaux cassés'])]
def service(i,t,img,items):
    lis=''.join(f'<li>{x}</li>' for x in items)
    return page('sv',f'<div class="bg" style="background-image:url({img})"></div><div class="top"><span class="k">Nos services</span>{lg("lgo")}</div><div class="txt"><div class="n">{i:02d} / {len(SV):02d}</div><h1>{t}</h1><ul>{lis}</ul><span class="pill">Devis gratuit · 06 69 19 05 77</span></div>')
def index():
    lis=''.join(f'<li>{t}</li>' for t,_,_ in SV)
    return page('ix',f'<div class="top"><span class="k">Harmonie Peinture</span>{lg("lgo")}</div><div class="t"><h1>Nos<br>services.</h1><ol>{lis}</ol></div>')
OUT=[('avis-00-note',summary())]+[(f'avis-{i+1:02d}',review(i+1,*r,len(REV))) for i,r in enumerate(REV)]+[('services-00-sommaire',index())]+[(f'services-{i+1:02d}',service(i+1,*s)) for i,s in enumerate(SV)]
for slug,b in OUT:
    for a in [' ?',' :',' !']: b=b.replace(a,' '+a[1:])
    open(slug+'.html','w').write(f'<!DOCTYPE html><html><head><meta charset="utf-8">{FONTS}<style>{CSS}</style></head><body>{b}</body></html>')
json.dump([s for s,_ in OUT],open('list.json','w'));print(len(OUT))
