(()=>{const $=s=>document.querySelector(s),$$=s=>[...document.querySelectorAll(s)];
const hd=$('#hd'),mbar=$('#mbar');let lastY=0;
const on=()=>{const y=scrollY;hd.classList.toggle('sc',y>8);hd.classList.toggle('hide',y>lastY&&y>400);lastY=y;if(mbar)mbar.classList.toggle('on',y>innerHeight*.6&&(innerHeight+y)<document.body.scrollHeight-600)};
addEventListener('scroll',on,{passive:true});on();
const io=new IntersectionObserver(es=>{for(const e of es){if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target)}}},{threshold:.12,rootMargin:'0px 0px -40px 0px'});
$$('.rv').forEach(el=>io.observe(el));
$$('.yr').forEach(e=>e.textContent=new Date().getFullYear());})();
