"""NEXTWISE · versiunea 4 „Reactor”: introul pornește cele șase module pe un inel, butonul e nucleul;
la intrare zbori prin inele. Fundal: grilă în perspectivă care avansează la scroll, cu impulsuri colorate,
și sistemul de orbite cu modulele în hero."""
import math
from plus import build
from v2data import MODULE_HUES

NAMES = ["Recepție", "Follow-up", "Documente", "Marketing", "Operațiuni", "Tablou"]


def arcs():
    out = []
    for i, h in enumerate(MODULE_HUES):
        a0 = math.radians(-90 + i * 60 + 6)
        a1 = math.radians(-90 + i * 60 + 54)
        x0, y0, x1, y1 = 168 * math.cos(a0), 168 * math.sin(a0), 168 * math.cos(a1), 168 * math.sin(a1)
        out.append(f'<path class="a" pathLength="1" style="--i:{i};--h:{h}" d="M{x0:.1f},{y0:.1f} A168,168 0 0 1 {x1:.1f},{y1:.1f}"/>')
    return "".join(out)


boot = "".join(f'<li style="--i:{i};--h:{h}">{n}<b>pornit</b></li>' for i, (n, h) in enumerate(zip(NAMES, MODULE_HUES)))

INTRO = f'''<div id="intro" class="i4">
  <div class="rx">
    <svg viewBox="-200 -200 400 400" aria-hidden="true">
      <circle class="tk" r="191"/>{arcs()}<circle class="dz" r="140"/><circle class="th" r="114"/>
      <g class="sat s1"><circle cx="140" r="5"/></g><g class="sat s2"><circle cx="-114" r="3.5"/></g>
    </svg>
    <button id="enter" class="rcore" type="button"><span>Intră în site</span></button>
  </div>
  <ul class="boot" aria-hidden="true">{boot}</ul>
</div>'''

CSS = r'''
/* ── intro 4 */
#intro.i4{display:flex;flex-direction:column;align-items:center;justify-content:center;gap:clamp(22px,4.5vh,40px);padding:20px}
.i4 .rx{position:relative;width:min(66vw,54vh,440px);aspect-ratio:1/1;display:grid;place-items:center}
.i4 svg{position:absolute;inset:0;width:100%;height:100%;overflow:visible}
.i4 circle,.i4 path{fill:none}
.i4 .tk{stroke:rgba(237,238,245,.45);stroke-width:7;stroke-dasharray:1.2 10.8;transform-origin:center;animation:rot 60s linear infinite}
.i4 .a{stroke:hsl(var(--h) 90% 66%);stroke-width:7;stroke-linecap:round;stroke-dasharray:1;stroke-dashoffset:1;filter:drop-shadow(0 0 8px hsl(var(--h) 90% 60%/.9));animation:draw .55s cubic-bezier(.23,1,.32,1) forwards;animation-delay:calc(.5s + var(--i)*.3s)}
.i4 .dz{stroke:rgba(142,123,255,.7);stroke-width:1.5;stroke-dasharray:46 16;animation:rot 22s linear infinite reverse}
.i4 .th{stroke:rgba(61,214,245,.45);stroke-width:1}
.i4 .sat{animation:rot 6s linear infinite}.i4 .s2{animation:rot 9s linear infinite reverse}
.i4 .sat circle{fill:#fff;filter:drop-shadow(0 0 8px #fff)}
@keyframes rot{to{transform:rotate(360deg)}}@keyframes draw{to{stroke-dashoffset:0}}
.rcore{position:relative;width:46%;aspect-ratio:1/1;border-radius:50%;display:grid;place-items:center;color:#fff;font-weight:600;font-size:clamp(14px,1.9vh,18px);line-height:1.15;padding:10px;background:radial-gradient(circle at 34% 28%,#B9AEFF,#7C68F2 46%,#3A2CA6);box-shadow:0 0 70px 6px rgba(142,123,255,.55),inset 0 0 30px rgba(255,255,255,.18);opacity:.32;transform:scale(.88);animation:arm .8s cubic-bezier(.23,1,.32,1) 2.45s forwards;transition:translate .3s var(--ease)}
.rcore::before{content:"";position:absolute;inset:-10px;border-radius:50%;border:1.5px solid rgba(185,174,255,.8);opacity:0;animation:ringp 2s ease-out 3.1s infinite}
@keyframes arm{to{opacity:1;transform:none}}@keyframes ringp{0%{opacity:.9;transform:scale(1)}100%{opacity:0;transform:scale(1.55)}}
.rcore:active{scale:.96}
.boot{list-style:none;display:grid;grid-template-columns:repeat(3,auto);gap:8px 26px;font-family:'Geist Mono',monospace;font-size:13.5px;color:var(--text2)}
.boot li{opacity:0;animation:fade .5s var(--ease) forwards;animation-delay:calc(.5s + var(--i)*.3s);display:flex;gap:8px;align-items:baseline}
.boot b{font-weight:500;color:hsl(var(--h) 90% 70%)}
.entered #intro.i4{opacity:1;transition:visibility 0s 1.15s}
.entered .i4 .rx{transform:scale(12);opacity:0;transition:transform 1.1s cubic-bezier(.6,0,.9,.25),opacity .45s linear .65s}
.entered .i4 .boot{opacity:0;transition:opacity .25s}
@media (max-width:640px){.boot{grid-template-columns:repeat(2,auto);font-size:13px}}
@media (prefers-reduced-motion:reduce){.i4 .a{stroke-dashoffset:0}.rcore,.boot li{opacity:1;transform:none}.entered .i4 .rx{transition:none}}
.hero .sub{text-shadow:0 0 22px #090A11,0 0 8px #090A11}
'''

FX = r'''
// ───────────────────────── FX 4: grilă în perspectivă + orbite
const cv=$('#fx'),c=cv.getContext('2d');
const COL=['#8E7BFF','#5B8CFF','#3DD6F5','#7CF0C5','#FFB547','#FF5FA8'],MOD=['Recepție','Follow-up','Documente','Marketing','Operațiuni','Tablou'],MH=[258,205,32,330,150,190];
let W=0,H=0,D=1,entered=false,vis=true,t=0,last=0,mode='intro',al=.5,off=0,lsy=scrollY,mx=0,my=0,pul=[],stars=[],oa=0,warp=0,hyf=.5,spk=[];
const AL={intro:.6,sphere:1,rings:.5,wave:.62,scat:.36,helix:.5,end:1};
const RG=[{r:.42,tilt:.56,rot:-.62,sp:.42,n:[0,3]},{r:.68,tilt:.5,rot:.5,sp:-.3,n:[1,4]},{r:.95,tilt:.44,rot:-.14,sp:.21,n:[2,5]}];
function size(){D=Math.min(devicePixelRatio||1,1.5);W=innerWidth;H=innerHeight;cv.width=W*D;cv.height=H*D;c.setTransform(D,0,0,D,0,0);stars=[];let s=5;const r=()=>{s=(s*16807)%2147483647;return s/2147483647};for(let i=0;i<(W<760?60:130);i++)stars.push({x:r()*W,y:r()*.5,r:.5+r()*1.2,p:r()*6.28,b:(r()*6)|0})}
const secs=$$('[data-shape]');
function pick(){if(!entered)return'intro';let s=secs[0].dataset.shape;const y=scrollY+H*.55;for(const e of secs)if(e.offsetTop<=y)s=e.dataset.shape;return s}
function orbit(cx,cy,R,a){const T=t*1000;const pos=(g,an)=>{const x=Math.cos(an)*g.r*R,y=Math.sin(an)*g.r*R*g.tilt,cr=Math.cos(g.rot+mx*.2),sr=Math.sin(g.rot+mx*.2);return{x:cx+x*cr-y*sr,y:cy+x*sr+y*cr,z:Math.sin(an)}};
 const ell=(g,f,to,al2)=>{c.beginPath();for(let i=0;i<=40;i++){const p=pos(g,f+(to-f)*i/40);i?c.lineTo(p.x,p.y):c.moveTo(p.x,p.y)}c.strokeStyle='rgba(142,123,255,'+al2*a+')';c.lineWidth=1.2;c.stroke()};
 RG.forEach(g=>ell(g,Math.PI,2*Math.PI,.2));const nodes=[];RG.forEach((g,ri)=>g.n.forEach((li,k)=>nodes.push({...pos(g,T*.001*g.sp+k*Math.PI+ri*1.1),li})));
 const dn=n=>{const f=n.z>0,col='hsl('+MH[n.li]+' 90% 66%)';c.globalAlpha=a*(f?1:.45);c.beginPath();c.arc(n.x,n.y,f?7:5,0,6.283);c.fillStyle=col;c.fill();c.beginPath();c.arc(n.x,n.y,f?15:11,0,6.283);c.strokeStyle=col;c.lineWidth=1;c.globalAlpha=a*(f?.5:.2);c.stroke();
  c.globalAlpha=a*(f?.95:.4);c.font=(W<760?'11px':'13.5px')+" 'Geist Mono',monospace";c.fillStyle='#EDEEF5';c.textAlign='center';const tw=c.measureText(MOD[n.li]).width/2+4;c.fillText(MOD[n.li],Math.max(tw,Math.min(W-tw,n.x)),n.y<cy?n.y-22:n.y+30);c.globalAlpha=1};
 nodes.filter(n=>n.z<=0).forEach(dn);
 const core=R*.17,g1=c.createRadialGradient(cx,cy,0,cx,cy,core*4);g1.addColorStop(0,'rgba(142,123,255,'+.5*a+')');g1.addColorStop(.5,'rgba(61,214,245,'+.1*a+')');g1.addColorStop(1,'rgba(142,123,255,0)');c.fillStyle=g1;c.beginPath();c.arc(cx,cy,core*4,0,6.283);c.fill();
 c.globalAlpha=a;const g2=c.createLinearGradient(cx-core,cy-core,cx+core,cy+core);g2.addColorStop(0,'#6E5AE8');g2.addColorStop(1,'#3DD6F5');c.fillStyle=g2;c.beginPath();c.arc(cx,cy,core*(1+Math.sin(T*.0018)*.04),0,6.283);c.fill();
 c.fillStyle='#fff';c.font='600 '+(W<760?'12px':'15px')+" 'Geist',sans-serif";c.textAlign='center';c.fillText('Firma ta',cx,cy+5);c.globalAlpha=1;
 if(!RM&&spk.length<5&&Math.random()<.04)spk.push({li:(Math.random()*6)|0,p:0,inb:Math.random()<.6});
 for(let k=spk.length-1;k>=0;k--){const s=spk[k],n=nodes.find(q=>q.li===s.li);s.p+=.016;if(s.p>=1){spk.splice(k,1);continue}const u=s.inb?s.p:1-s.p,x=n.x+(cx-n.x)*u,y=n.y+(cy-n.y)*u;c.globalAlpha=a*.35*Math.sin(s.p*Math.PI);c.strokeStyle='hsl('+MH[s.li]+' 90% 66%)';c.beginPath();c.moveTo(n.x,n.y);c.lineTo(cx,cy);c.stroke();c.globalAlpha=a;c.fillStyle='#fff';c.beginPath();c.arc(x,y,2.8,0,6.283);c.fill();c.globalAlpha=1}
 RG.forEach(g=>ell(g,0,Math.PI,.42));nodes.filter(n=>n.z>0).forEach(dn)}
function frame(ts){if(!vis)return;const dt=Math.min(48,ts-last||16);last=ts;if(!RM)t+=dt*.001;mode=pick();const sy=scrollY,dv=sy-lsy;lsy=sy;warp*=.94;if(!RM)off+=dt*.00038*(1+warp)+dv*.0024;
 al+=((AL[mode]||.5)-al)*(RM?1:.05);hyf+=((mode==='end'?.36:mode==='intro'?.56:mode==='sphere'?.2:.5)-hyf)*(RM?1:.04);oa+=((mode==='sphere'?1:0)-oa)*(RM?1:.06);
 const hy=H*hyf+my*10,vpx=W/2+mx*60,F=(H-hy)*.5,sp=W/18,m=W<760;
 c.globalCompositeOperation='source-over';c.globalAlpha=1;c.clearRect(0,0,W,H);
 for(const s of stars){c.globalAlpha=al*(.35+.45*Math.sin(t*1.3+s.p));c.fillStyle=COL[s.b];c.beginPath();c.arc(s.x,s.y*hy*1.9,s.r,0,6.283);c.fill()}
 c.globalAlpha=1;let g=c.createLinearGradient(0,hy-H*.26,0,hy);g.addColorStop(0,'rgba(142,123,255,0)');g.addColorStop(1,'rgba(142,123,255,'+.2*al+')');c.fillStyle=g;c.fillRect(0,hy-H*.26,W,H*.26);
 // liniile care fug spre orizont
 c.beginPath();for(let j=-60;j<=60;j++){c.moveTo(vpx+j*sp/14,hy+F/14);c.lineTo(vpx+j*sp/.5,H)}c.strokeStyle='rgba(124,108,240,'+.46*al+')';c.lineWidth=1;c.stroke();
 // liniile care vin spre tine
 const fr=((off%1)+1)%1;for(let k=0;k<28;k++){const z=.5+(k+1-fr)*.5,y=hy+F/z,a=Math.min(1,(y-hy)/(H-hy)*2.4);c.globalAlpha=al*a*.62;c.strokeStyle='#7C6CF0';c.beginPath();c.moveTo(0,y);c.lineTo(W,y);c.stroke()}
 c.globalAlpha=1;g=c.createLinearGradient(0,hy,0,hy+(H-hy)*.34);g.addColorStop(0,'rgba(9,10,17,1)');g.addColorStop(1,'rgba(9,10,17,0)');c.fillStyle=g;c.fillRect(0,hy,W,(H-hy)*.34);
 // impulsuri
 c.globalCompositeOperation='lighter';if(!RM&&pul.length<(m?10:26)&&Math.random()<.45)pul.push({j:Math.round((Math.random()-.5)*(m?10:22)),z:9+Math.random()*4,s:.9+Math.random()*1.6,b:(Math.random()*6)|0});
 for(let k=pul.length-1;k>=0;k--){const p=pul[k];p.z-=p.s*dt*.0016*(1+warp*2+Math.abs(dv)*.06);if(p.z<.5){pul.splice(k,1);continue}const z2=Math.min(14,p.z*1.28),x1=vpx+p.j*sp/p.z,y1=hy+F/p.z,x2=vpx+p.j*sp/z2,y2=hy+F/z2,a=Math.min(1,(y1-hy)/(H-hy)*3);
  c.globalAlpha=al*a;c.strokeStyle=COL[p.b];c.lineWidth=1+2.2*a;c.lineCap='round';c.beginPath();c.moveTo(x2,y2);c.lineTo(x1,y1);c.stroke();c.fillStyle='#fff';c.beginPath();c.arc(x1,y1,1+1.6*a,0,6.283);c.fill()}
 // orizontul în spectru
 c.globalAlpha=al;g=c.createLinearGradient(0,0,W,0);COL.forEach((cl,i)=>g.addColorStop(i/5,cl));c.fillStyle=g;c.fillRect(0,hy-1,W,2);c.globalAlpha=al*.25;c.fillRect(0,hy-4,W,8);
 c.globalCompositeOperation='source-over';c.globalAlpha=1;
 if(oa>.02){const u=Math.min(W,H);m?orbit(W*.5,H*.27,u*.36,oa*.8):orbit(W*.76,H*.46,u*.34,oa)}
 if(!RM)requestAnimationFrame(frame)}
const kick=()=>{if(RM)requestAnimationFrame(frame)};
size();requestAnimationFrame(frame);
let rz;addEventListener('resize',()=>{clearTimeout(rz);rz=setTimeout(()=>{size();kick()},150)});
addEventListener('pointermove',e=>{mx=e.clientX/W-.5;my=e.clientY/H-.5},{passive:true});
document.addEventListener('visibilitychange',()=>{vis=!document.hidden;if(vis&&!RM){last=0;requestAnimationFrame(frame)}});
document.fonts&&document.fonts.ready&&document.fonts.ready.then(kick);
const enterBtn=$('#enter');
function enter(){if(entered)return;entered=true;warp=26;B.classList.add('entered');kick()}
enterBtn.addEventListener('click',enter);setTimeout(()=>{try{enterBtn.focus({preventScroll:true})}catch(e){}},2600);
'''

EXTRA = r'''
// titlurile de pe coperți se „decodează”, fișa tehnică se scrie rând cu rând
const CH='abcdefghijklmnopqrstuvwxyz0123456789';
function scr(el){if(RM||el._s)return;el._s=1;const fin=el.dataset.f||(el.dataset.f=el.textContent),L=fin.length;let f=0;const tot=24;(function st(){let o='';for(let i=0;i<L;i++){const ch=fin[i];o+=(ch===' '||i<f/tot*L)?ch:CH[(Math.random()*CH.length)|0]}el.textContent=o;if(f++<tot)setTimeout(st,34);else{el.textContent=fin;el._s=0}})()}
const io4=new IntersectionObserver(es=>es.forEach(e=>{if(e.isIntersecting){scr(e.target);io4.unobserve(e.target)}}),{threshold:.7});$$('.pb-art b').forEach(e=>io4.observe(e));
$$('[data-open]').forEach(b=>b.addEventListener('click',()=>{const s=document.getElementById('sheet-'+b.dataset.open);if(!s||RM)return;setTimeout(()=>scr(s.querySelector('.sh-head h3')),220);
 $$('.sh-spec dd',s).forEach((d,i)=>{const full=d.dataset.f||(d.dataset.f=d.textContent);if(d._t)return;d._t=1;if(d.offsetHeight)d.style.minHeight=d.offsetHeight+'px';d.textContent='';let n=0;setTimeout(function ty(){n+=3;d.textContent=full.slice(0,n);if(n<full.length)setTimeout(ty,14);else d._t=0},460+i*120)})}));
'''

build("v4", "NEXTWISE · Site nou · versiunea 4 · Reactor", INTRO, CSS, FX, EXTRA, head="Agenți AI care țin firma în mișcare.")
