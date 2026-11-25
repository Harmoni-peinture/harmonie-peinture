IC={
'services':'<rect x="3" y="3" width="8" height="8" rx="2"/><rect x="13" y="3" width="8" height="8" rx="2"/><rect x="3" y="13" width="8" height="8" rx="2"/><rect x="13" y="13" width="8" height="8" rx="2"/>',
'realisations':'<rect x="3" y="3" width="14" height="6" rx="2"/><path d="M17 6h3v5h-8v3"/><rect x="10.5" y="14" width="3" height="7" rx="1"/>',
'avis':'<path d="M12 3.5l2.6 5.3 5.8.8-4.2 4.1 1 5.8L12 16.8l-5.2 2.7 1-5.8-4.2-4.1 5.8-.8z"/>',
'avant-apres':'<rect x="3" y="4" width="18" height="16" rx="2"/><path d="M12 2v20"/><path d="M7 9l-2 3 2 3M17 9l2 3-2 3"/>',
'devis':'<path d="M6 3h9l4 4v14H6z"/><path d="M15 3v4h4M9 12h7M9 16h5"/>',
'equipe':'<circle cx="9" cy="8" r="3"/><circle cx="17" cy="9" r="2.4"/><path d="M3.5 20c.5-3.6 2.8-5.5 5.5-5.5s5 1.9 5.5 5.5M15 14.6c2.6.1 4.5 1.8 5 5.4"/>',
'conseils':'<path d="M9 18h6M10 21h4"/><path d="M12 3a6 6 0 0 0-3.5 10.9c.6.5 1 1.2 1 2.1h5c0-.9.4-1.6 1-2.1A6 6 0 0 0 12 3z"/>',
'zones':'<path d="M12 21s-7-6.2-7-11.5A7 7 0 0 1 19 9.5C19 14.8 12 21 12 21z"/><circle cx="12" cy="9.5" r="2.5"/>',
'isolation':'<path d="M3 11l9-7 9 7"/><path d="M5 10v10h14V10"/><path d="M8 15c1.5-1 2.5 1 4 0s2.5 1 4 0"/>',
'couleurs':'<rect x="3" y="4" width="5" height="16" rx="1.5"/><rect x="9.5" y="4" width="5" height="16" rx="1.5"/><rect x="16" y="4" width="5" height="16" rx="1.5"/>',
'contact':'<path d="M5 4h3l1.5 4-2 1.2a10 10 0 0 0 5.3 5.3l1.2-2 4 1.5v3a2 2 0 0 1-2 2A15 15 0 0 1 3 6a2 2 0 0 1 2-2"/>',
}
NAMES={'realisations':'Réalisations','avis':'Avis clients','avant-apres':'Avant / Après','devis':'Devis','equipe':'L’équipe','conseils':'Conseils','zones':'Zones','isolation':'Isolation RGE','couleurs':'Couleurs','contact':'Contact'}
CSS='''html,body{margin:0}.s{width:1080px;height:1920px;position:relative;overflow:hidden;background:#1F4D3A;
background-image:repeating-linear-gradient(90deg,rgba(255,255,255,.035) 0 120px,transparent 120px 240px),radial-gradient(70% 45% at 50% 50%,rgba(255,255,255,.07),rgba(0,0,0,.18))}
.c{position:absolute;left:50%;top:50%;width:860px;height:860px;transform:translate(-50%,-50%);border-radius:50%;border:3px solid rgba(244,241,230,.28);display:grid;place-items:center}
.c::before{content:"";position:absolute;inset:60px;border-radius:50%;background:rgba(244,241,230,.06)}
.c svg{width:400px;height:400px;position:relative}
.dot{position:absolute;left:50%;top:calc(50% + 250px);width:26px;height:26px;border-radius:50%;background:#C2531B;transform:translateX(-50%)}'''
import json
names=[]
for k,p in IC.items():
    accent = 'stroke="#F4F1E6"'
    svg=f'<svg viewBox="0 0 24 24" fill="none" stroke="#F4F1E6" stroke-width="1.35" stroke-linecap="round" stroke-linejoin="round">{p}</svg>'
    open(f'{k}.html','w').write(f'<!DOCTYPE html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body><div class="s"><div class="c">{svg}</div><div class="dot"></div></div></body></html>')
    names.append(k)
json.dump(names,open('list.json','w'))
