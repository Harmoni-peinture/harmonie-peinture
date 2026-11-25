from faces2 import *
def stack(face,k,left,top,rot,edgeA,edgeB,n=26,z=1):
    w,h=85*k,55*k
    ext=",".join(f"{-i}px {i}px 0 {edgeA if (i//2)%2==0 else edgeB}" for i in range(1,n+1))
    sh=f"{-n-14}px {n+22}px 26px rgba(0,0,0,.55),{-n-60}px {n+90}px 110px rgba(0,0,0,.45)"
    inner=f'<div style="transform:scale({k/3.7795});transform-origin:0 0;margin:{-3*k}px 0 0 {-3*k}px">{face}</div>'
    return f'''<div style="position:absolute;left:{left}px;top:{top}px;width:{w}px;height:{h}px;transform:rotate({rot}deg);z-index:{z}">
<div style="position:absolute;inset:0;box-shadow:{ext},{sh}"></div>
<div style="position:absolute;inset:0;overflow:hidden">{inner}<div style="position:absolute;inset:0;background:linear-gradient(125deg,rgba(255,255,255,.16),rgba(255,255,255,0) 40%,rgba(0,0,0,.08))"></div></div></div>'''
def ball(left,top,size):
    return f'''<div style="position:absolute;z-index:3;left:{left-size*0.42}px;top:{top+size*0.52}px;width:{size*1.1}px;height:{size*0.62}px;border-radius:50%;background:rgba(0,0,0,.62);filter:blur({size*0.08}px);transform:rotate(-38deg)"></div><div style="position:absolute;z-index:3;left:{left+size*0.05}px;top:{top+size*0.62}px;width:{size*0.75}px;height:{size*0.4}px;border-radius:50%;background:rgba(0,0,0,.7);filter:blur({size*0.04}px)"></div>
<img src="ball.png" style="position:absolute;z-index:4;left:{left}px;top:{top}px;width:{size}px;height:auto;filter:brightness(1.02) saturate(.9)">'''
def page(W,H,bg,body):
    return f'''<!DOCTYPE html><html><head><meta charset="utf-8">{FONTS}<style>{CSS}html,body{{margin:0}}</style></head><body>
<div style="width:{W}px;height:{H}px;position:relative;overflow:hidden;background:url({bg}) center/cover">{body}
<div style="position:absolute;inset:0;background:radial-gradient(90% 80% at 40% 35%,rgba(255,240,210,.08),rgba(0,0,0,0) 60%,rgba(0,0,0,.25))"></div></div></body></html>'''
GA,GB='#163a2b','#1d4636'; CA,CB='#d8d2c1','#e6e1d1'
K=9.2
land=page(2400,1800,'turf-land.jpg',
  stack(FRONT,K,560,250,-9,GA,GB,28,2)+stack(BACK,K,1120,860,7,CA,CB,24,1)+ball(1830,250,330))
open('m-land.html','w').write(land)
K2=8.4
port=page(1440,1800,'turf-port.jpg',
  stack(BACK,K2,420,960,9,CA,CB,22,1)+stack(FRONT,K2,250,330,-11,GA,GB,28,2)+ball(1040,1400,280))
open('m-port.html','w').write(port)
