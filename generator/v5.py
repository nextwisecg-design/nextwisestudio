"""NEXTWISE · versiunea 5 (combo cerut de Darius, 24.11.2026): introul „Reactor” din v4, puțin schimbat și
mai sobru la culoare, plus planeta de particule din v2 în hero: se rotește încet, are modulele scrise pe ea,
rute între ele, un inel de text și se poate roti cu mouse-ul. Paleta: violet, albastru, turcoaz (fără curcubeu).
Cardurile de portofoliu își păstrează culoarea din HQ."""
import math
import v2
import v4
from plus import build, MARK_FX, MARK_UI
import v5legal as L

HUES = [258, 246, 232, 218, 204, 192]
NAMES = ["Recepție", "Follow-up", "Documente", "Marketing", "Operațiuni", "Tablou"]


def arcs():
    out = []
    for i, h in enumerate(HUES):
        a0, a1 = math.radians(-90 + i * 60 + 6), math.radians(-90 + i * 60 + 54)
        out.append(f'<path class="a" pathLength="1" style="--i:{i};--h:{h}" d="M{168 * math.cos(a0):.1f},{168 * math.sin(a0):.1f} A168,168 0 0 1 {168 * math.cos(a1):.1f},{168 * math.sin(a1):.1f}"/>')
    return "".join(out)


boot = "".join(f'<li style="--i:{i};--h:{h}">{n}<b>pornit</b></li>' for i, (n, h) in enumerate(zip(NAMES, HUES)))

INTRO = f'''<div id="intro" class="i4 i5">
  <div class="rx">
    <svg viewBox="-200 -200 400 400" aria-hidden="true">
      <circle class="tk" r="191"/>{arcs()}<circle class="dz" r="140"/><circle class="th" r="114"/>
      <g class="sat s1"><circle cx="140" r="5"/></g><g class="sat s2"><circle cx="-114" r="3.5"/></g>
    </svg>
    <button id="enter" class="rcore" type="button" aria-label="Intră în site"><span>Intră în site</span></button>
  </div>
  <ul class="boot" aria-hidden="true">{boot}</ul>
</div><div class="gtip" aria-hidden="true"><b></b><span></span></div>'''

CSS = v4.CSS + r'''
/* ── versiunea 5: mai puțină culoare */
:root{--spec:linear-gradient(90deg,#8E7BFF,#5B8CFF,#3DD6F5)}
.prod,.cta-box{background:conic-gradient(from var(--ang),#8E7BFF,#3DD6F5,#6E5AE8,#5B8CFF,#8E7BFF)}
.marq span{color:var(--text)}
.marq span:nth-child(even){color:transparent;-webkit-text-stroke:1px rgba(185,174,255,.75)}
.marq span::after{background:var(--violet)}
.bento .cell:nth-child(1),.bento .cell:nth-child(4){--h:258!important}.bento .cell:nth-child(2),.bento .cell:nth-child(5){--h:226!important}.bento .cell:nth-child(3),.bento .cell:nth-child(6){--h:196!important}
.steps li:nth-child(1){--h:258!important}.steps li:nth-child(2){--h:236!important}.steps li:nth-child(3){--h:214!important}.steps li:nth-child(4){--h:192!important}
.b5{background:linear-gradient(135deg,rgba(142,123,255,.55),rgba(61,214,245,.4))}
.prod .r{background:radial-gradient(420px 320px at 80% 10%,rgba(61,214,245,.14),transparent 70%),radial-gradient(420px 320px at 10% 100%,rgba(142,123,255,.16),transparent 70%)}
.cta-box h2{background:none;color:var(--text);-webkit-background-clip:border-box;background-clip:border-box}
.price b{background:none;color:var(--text)}
/* introul, puțin schimbat */
.i5 .rx::before{content:"";position:absolute;inset:13%;border-radius:50%;background:conic-gradient(from 0deg,rgba(142,123,255,.34),transparent 24%);-webkit-mask:radial-gradient(circle closest-side,transparent 65%,#000 66%);mask:radial-gradient(circle closest-side,transparent 65%,#000 66%);animation:rot 3.6s linear infinite}
.i5 .a{stroke:hsl(var(--h) 92% 68%)}
.i5 .rcore span{font-variant-numeric:tabular-nums}
.hero{position:relative}
@media (hover:hover) and (pointer:fine) and (min-width:1001px){.hero::after{content:"%%CAP%%";position:absolute;right:var(--pad);bottom:30px;font-family:'Geist Mono',monospace;font-size:13px;color:var(--faint);opacity:0;transition:opacity 1s 2s}.entered .hero::after{opacity:1}}
.marq{display:none}
.i4 .sat{animation-duration:17s}.i4 .s2{animation-duration:26s}.i4 .dz{animation-duration:50s}
.i5 .rx::before{animation-duration:9s}
.i4 .a{animation-duration:.9s;animation-delay:calc(.6s + var(--i)*.45s)}
.boot li{animation-delay:calc(.6s + var(--i)*.45s)}
.rcore{animation-delay:3.4s}.rcore::before{animation-duration:3.8s;animation-delay:4.2s}
.entered .i4 .rx{transition:transform 1.6s cubic-bezier(.6,0,.9,.25),opacity .6s linear 1s}
.entered #intro.i4{transition:visibility 0s 1.65s}
.chat i{animation-duration:6.4s}.ping b{animation-duration:4.8s}.doc i{animation-duration:5.8s}.eq i{animation-duration:3s}.chk i{animation-duration:6.4s}.spark path{animation-duration:6.4s}
.mock .b{animation-duration:13s}
.prod,.cta-box{animation-duration:24s}
.pb-live.on i{animation-duration:3.4s}
.gtip{position:fixed;left:0;top:0;z-index:6;width:250px;padding:12px 14px;border-radius:12px;background:#12131B;border:1px solid var(--line2);pointer-events:none;opacity:0;transition:opacity .18s var(--ease);display:grid;gap:3px}
.gtip.on{opacity:1}.gtip.l{margin-left:-250px}
.gtip b{font-size:15px;font-weight:600}.gtip span{font-size:14px;line-height:1.4;color:var(--text2)}
@media (prefers-reduced-motion:reduce){.i5 .rx::before{display:none}}
'''

# ── FX: motorul de particule din v2, cu planeta îmbogățită
J = v2.JS
FX = J[J.index(MARK_FX):J.index(MARK_UI)]


def rep(a, b):
    global FX
    assert FX.count(a) == 1, (FX.count(a), a[:70])
    FX = FX.replace(a, b)


DEP = [('Recepție', 'Răspunde la cereri și face programări, și după program.'), ('Vânzări', 'Fiecare ofertă primește follow-up. Niciuna nu rămâne uitată.'), ('Marketing', 'Postări și recenzii, publicate doar cu aprobarea ta.'), ('Operațiuni', 'Sarcini și termene ținute la zi, fără tabele paralele.'), ('Financiar', 'Facturi emise automat după fiecare plată.'), ('Achiziții', 'Compară ofertele furnizorilor și propune comanda.'), ('Administrativ', 'Oferte, contracte și fișe, din șabloanele firmei.'), ('Direcție', 'Cifrele firmei într-un singur ecran.')]
TOOLS = ['WhatsApp', 'Email', 'Calendar', 'Facturare', 'Site', 'Telefon']
import json as _json
GLOBE = r'''
let rotX=0,rv=0,ga=0,gpx=-9e3,gpy=-9e3,hov=-1,smx=0,smy=0;
const DEP=%%DEP%%,TOOLS=%%TOOLS%%;
const sph=(la,lo)=>[Math.cos(la)*Math.cos(lo),Math.sin(la),Math.cos(la)*Math.sin(lo)];
const GD=[.5,-.15,.3,-.5,.12,-.35,.55,-.05].map((la,i)=>sph(la,i*.7854+.2)),GT=[-.62,.68,-.3,.75,-.7,.35].map((la,i)=>sph(la,i*1.0472+.6));
const nearD=v=>{let b=0,d=9;GD.forEach((q,i)=>{const e=Math.hypot(v[0]-q[0],v[1]-q[1],v[2]-q[2]);if(e<d){d=e;b=i}});return b},GTN=GT.map(nearD);
const SAT=[{r:1.36,tx:.5,tz:.3,sp:.085,ph:0},{r:1.52,tx:-.4,tz:-.5,sp:-.06,ph:2},{r:1.44,tx:.15,tz:.9,sp:.07,ph:4}];
const tip=$('.gtip'),fineP=matchMedia('(hover:hover) and (pointer:fine)').matches;
addEventListener('pointermove',e=>{gpx=e.clientX;gpy=e.clientY},{passive:true});
let limL=0;function lim(){let r=0;$$('.hero .w').forEach(e=>{r=Math.max(r,e.getBoundingClientRect().right)});limL=r+14}
lim();addEventListener('resize',()=>setTimeout(lim,200));document.fonts&&document.fonts.ready&&document.fonts.ready.then(lim);
function bootRect(){const e=$('.i4 .rx');if(!e)return[W/2,H/2,200];const b=e.getBoundingClientRect();return[b.left+b.width/2,b.top+b.height/2,b.width/2]}
function globe(g,cy_,sy_,cx_,sx_){const m=W<760;
 const P3=(x,y,z)=>{const x1=x*cy_+z*sy_,z1=-x*sy_+z*cy_,y2=y*cx_-z1*sx_,z2=y*sx_+z1*cx_,f=2.7/(2.7+z2);return[g.cx+x1*g.s*f,g.cy+y2*g.s*f,z2,f]};
 const fr=z=>Math.max(0,Math.min(1,(.2-z)/.55));
 const arc=(a,b,u,h)=>{const x=a[0]+(b[0]-a[0])*u,y=a[1]+(b[1]-a[1])*u,z=a[2]+(b[2]-a[2])*u,L=Math.hypot(x,y,z)||1,k=(1+h*Math.sin(Math.PI*u))/L;return P3(x*k,y*k,z*k)};
 const route=(a,b,h,col,w,i,sp)=>{let pv=null;c.strokeStyle=col;c.lineWidth=w;for(let s=0;s<=22;s++){const p=arc(a,b,s/22,h);if(pv){c.globalAlpha=ga*(.06+.46*fr((p[2]+pv[2])/2));c.beginPath();c.moveTo(pv[0],pv[1]);c.lineTo(p[0],p[1]);c.stroke()}pv=p}
  if(!RM){const p=arc(a,b,(t*sp+i*.37)%1,h);c.globalAlpha=ga*(.1+.9*fr(p[2]));c.fillStyle='#fff';c.beginPath();c.arc(p[0],p[1],2.4*p[3],0,6.2832);c.fill()}};
 c.globalCompositeOperation='source-over';c.lineCap='round';c.textBaseline='alphabetic';
 // rute între departamente și spre programele firmei
 for(let i=0;i<GD.length;i++)route(GD[i],GD[(i+1)%GD.length],.24,'#8E7BFF',1.1,i,.055);
 if(!m)GT.forEach((v,i)=>route(v,GD[GTN[i]],.12,'#3DD6F5',.9,i,.07));
 // agenții, ca sateliți
 SAT.forEach(s=>{const ct=Math.cos(s.tx),st=Math.sin(s.tx),cz=Math.cos(s.tz),sz=Math.sin(s.tz),pos=a=>{const x=Math.cos(a)*s.r,z=Math.sin(a)*s.r,y1=-z*st,z1=z*ct;return[x*cz-y1*sz,x*sz+y1*cz,z1]};
  c.setLineDash([2,7]);c.strokeStyle='#B9AEFF';c.lineWidth=1;c.globalAlpha=ga*.22;c.beginPath();for(let i=0;i<=60;i++){const v=pos(i/60*6.2832),p=P3(v[0],v[1],v[2]);i?c.lineTo(p[0],p[1]):c.moveTo(p[0],p[1])}c.stroke();c.setLineDash([]);
  const v=pos(t*s.sp+s.ph),p=P3(v[0],v[1],v[2]),f=fr(p[2]),d=GD[nearD([v[0]/s.r,v[1]/s.r,v[2]/s.r])],q=P3(d[0],d[1],d[2]);
  c.globalAlpha=ga*(.12+.5*f)*fr(q[2]);c.strokeStyle='#3DD6F5';c.beginPath();c.moveTo(p[0],p[1]);c.lineTo(q[0],q[1]);c.stroke();
  c.globalAlpha=ga*(.3+.7*f);c.fillStyle='#fff';c.beginPath();c.arc(p[0],p[1],3.2*p[3],0,6.2832);c.fill();c.strokeStyle='#3DD6F5';c.beginPath();c.arc(p[0],p[1],7*p[3],0,6.2832);c.stroke();
  if(!m){c.font="12px 'Geist Mono',monospace";c.textAlign='left';c.fillStyle='#CFD1DE';c.globalAlpha=ga*(.2+.7*f);c.fillText('agent',p[0]+12,p[1]+4)}});
 // programele firmei, ca puncte mici
 if(!m)GT.forEach((v,i)=>{const p=P3(v[0],v[1],v[2]),f=fr(p[2]);if(f<.05)return;const r=p[0]>=g.cx;c.globalAlpha=ga*f*.9;c.fillStyle='#3DD6F5';c.beginPath();c.arc(p[0],p[1],2.6,0,6.2832);c.fill();c.font="12px 'Geist Mono',monospace";c.textAlign=r?'left':'right';c.fillStyle='#9C9FB2';c.fillText(TOOLS[i],p[0]+(r?9:-9),p[1]+4)});
 // departamentele
 let best=-1,bd=34*34,bx=0,by=0;
 GD.forEach((v,i)=>{const p=P3(v[0],v[1],v[2]),f=fr(p[2]);if(f<(m?.6:.02))return;const dx=p[0]-g.cx,dy=p[1]-g.cy,L=Math.hypot(dx,dy)||1,ux=dx/L,uy=dy/L,len=m?16:34,ex=p[0]+ux*len,ey=p[1]+uy*len,sd=ux>=0?1:-1,on=hov===i;
  c.font=(on?'700 ':'600 ')+(m?11.5:15)+"px 'Geist',sans-serif";const tw=c.measureText(DEP[i][0]).width,lx=ex+sd*((m?24:42)+tw),flip=(sd<0&&lx<(m?4:limL))||(sd>0&&lx>W-8);
  if(f>.5&&fineP&&ga>.7){const d2=Math.min((p[0]-gpx)**2+(p[1]-gpy)**2,flip?(p[0]-gpx)**2+(p[1]-20-gpy)**2:(ex+sd*52-gpx)**2+(ey-gpy)**2);if(d2<bd){bd=d2;best=i;bx=p[0];by=p[1]}}
  c.globalAlpha=ga*f;if(!flip){c.strokeStyle='rgba(237,238,245,.75)';c.lineWidth=1;c.beginPath();c.moveTo(p[0],p[1]);c.lineTo(ex,ey);c.lineTo(ex+sd*(m?10:18),ey);c.stroke()}
  if(on){c.fillStyle='rgba(142,123,255,.3)';c.beginPath();c.arc(p[0],p[1],15,0,6.2832);c.fill()}
  c.fillStyle='#fff';c.beginPath();c.arc(p[0],p[1],on?4.6:3.4,0,6.2832);c.fill();c.strokeStyle='#8E7BFF';c.lineWidth=on?1.6:1;c.beginPath();c.arc(p[0],p[1],on?15:8+1.5*Math.sin(t*.7+i),0,6.2832);c.stroke();
  c.fillStyle=on?'#fff':'#EDEEF5';if(flip){c.textAlign='center';c.fillText(DEP[i][0],Math.max(tw/2+6,Math.min(W-tw/2-6,p[0])),p[1]-18)}else{c.textAlign=sd>0?'left':'right';c.fillText(DEP[i][0],ex+sd*(m?14:24),ey+5)}});
 if(tip){if(best!==hov){hov=best;if(hov>=0){tip.firstChild.textContent=DEP[hov][0];tip.lastChild.textContent=DEP[hov][1]}tip.classList.toggle('on',hov>=0)}
  if(hov>=0){const left=bx>=g.cx;tip.classList.toggle('l',left);tip.style.transform='translate('+Math.round(bx+(left?-24:24))+'px,'+Math.round(by+22)+'px)';if(!RM)rotX-=g.spin/60}}
 c.globalAlpha=1}
'''.replace("%%DEP%%", _json.dumps([list(d) for d in DEP], ensure_ascii=False)).replace("%%TOOLS%%", _json.dumps(TOOLS, ensure_ascii=False))
ZZ = ''''''

rep("const COL=['#8E7BFF','#5B8CFF','#3DD6F5','#7CF0C5','#FFB547','#FF5FA8'];",
    "const COL=['#B9AEFF','#8E7BFF','#7C8CFF','#5B8CFF','#4FB4FF','#3DD6F5'];" + GLOBE)
rep("function pick(){if(!entered)return'logo';", "function pick(){if(!entered)return'boot';")
rep("switch(s){\n case'logo':", "switch(s){\n case'boot':{const r=bootRect();return{a:'rings',cx:r[0],cy:r[1],s:Math.max(u*.5,r[2]*2.6),al:.6,spin:.045,tilt:.2}}\n case'logo':")
rep("case'sphere':return m?{a:'sphere',cx:W*.5,cy:H*.3,s:u*.36,al:.62,spin:.22,tilt:.22}:{a:'sphere',cx:W*.74,cy:H*.5,s:u*.37,al:1,spin:.22,tilt:.22};",
    "case'sphere':return m?{a:'sphere',cx:W*.5,cy:H*.29,s:u*.3,al:.7,spin:.028,tilt:.22}:{a:'sphere',cx:W*.74,cy:H*.5,s:u*.28,al:1,spin:.028,tilt:.22};")
rep("+mx*.3,ax=g.tilt+", "+smx*.09+rotX,ax=g.tilt+")
rep("+my*.16,cy_=", "+smy*.05,cy_=")
rep("function frame(ts){if(!vis)return;", "function frame(ts){if(!vis)return;smx+=(mx-smx)*.03;smy+=(my-smy)*.03;")
rep("p.p+=dt/560;", "p.p+=dt/1900;")
rep("al:m?.3:.42,spin:.16,tilt:.35}", "al:m?.3:.42,spin:.045,tilt:.35}")
rep("al:.3,spin:.035,tilt:0}", "al:.3,spin:.014,tilt:0}")
rep("spin:0,tilt:0,roll:.5}", "spin:0,tilt:0,roll:.11}")
rep("al:.6,spin:.1,tilt:.25}", "al:.6,spin:.03,tilt:.25}")
rep("al:.7,spin:.1,tilt:.25}", "al:.7,spin:.03,tilt:.25}")
rep("Math.sin(x*2.1+t*1.2)*.14+Math.cos(z*3.1+t*.9)*.1", "Math.sin(x*2.1+t*.32)*.14+Math.cos(z*3.1+t*.25)*.1")
rep("K=g.a==='logo'?.05:.035,", "K=g.a==='logo'?.05:.018,")
rep("pulses.length<(W<760?5:12)&&Math.random()<.2", "pulses.length<(W<760?3:6)&&Math.random()<.04")
rep("c.globalAlpha=1;if(!RM)requestAnimationFrame(frame)}",
    "c.globalAlpha=1;rotX+=rv;rv*=.9;ga+=((shape==='sphere'?1:0)-ga)*(RM?1:.05);if(ga>.02)globe(g,cy_,sy_,cx_,sx_);c.globalAlpha=1;if(!RM)requestAnimationFrame(frame)}")
rep("const dx=X[i]-W/2,dy=Y[i]-H*.42,d=Math.hypot(dx,dy)||1,p=26+Math.random()*46;",
    "const dx=X[i]-W/2,dy=Y[i]-H*.46,d=Math.hypot(dx,dy)||1,p=18+Math.random()*34;")
rep("setTimeout(()=>{try{enterBtn.focus({preventScroll:true})}catch(e){}},1900);", "setTimeout(()=>{try{enterBtn.focus({preventScroll:true})}catch(e){}},3600);")

EXTRA = v4.EXTRA.replace("if(!s||RM)return;", "if(!s||RM||s.classList.contains('legal'))return;").replace('setTimeout(st,34)', 'setTimeout(st,60)').replace('n+=3;', 'n+=2;').replace('setTimeout(ty,14)', 'setTimeout(ty,24)') + r'''
// numărătoarea din nucleu: câte module au pornit
const cnt=$('.rcore span');if(cnt&&!RM){const fin=cnt.textContent;cnt.textContent='0/6';for(let i=1;i<=6;i++)setTimeout(()=>{if(!B.classList.contains('entered'))cnt.textContent=i+'/6'},600+(i-1)*450+520);setTimeout(()=>{cnt.textContent=fin},3700)}
// planeta se rotește cu mouse-ul
const heroEl=$('.hero');let drag=false,lx=0;
if(heroEl&&!RM){heroEl.addEventListener('pointerdown',e=>{if(e.pointerType==='touch'||e.target.closest('a,button'))return;drag=true;lx=e.clientX;heroEl.style.cursor='grabbing'});
 addEventListener('pointermove',e=>{if(!drag)return;rv=(e.clientX-lx)*.0026;lx=e.clientX},{passive:true});
 addEventListener('pointerup',()=>{drag=false;heroEl.style.cursor=''});}
'''

CSS = CSS.replace("%%CAP%%", f"{len(DEP)} departamente, un singur sistem. Trage de planetă ca să o rotești.")
MOCK = '<div><div class="mock" aria-hidden="true"><div class="bar"><i></i><i></i><i></i></div><div class="pg"><div class="b b1"></div><div class="b b2"></div><div class="b b3"></div><div class="b b4"></div><div class="b b5"></div><div class="g3"><div class="b"></div><div class="b"></div><div class="b"></div></div></div></div><p class="mock-cap">Schiță de principiu. Macheta reală se face cu datele firmei tale.</p></div>'
v2.SHOW_DATES = False
v2.PORTFOLIO = L.PORTFOLIO5
CSS = CSS + L.CSS
build("v5", "NEXTWISE · Site nou · versiunea 5 · Reactor + planetă", INTRO, CSS, FX, EXTRA,
      prod=L.prod(v2.CHECK, MOCK), ways=L.WAYS, footer=L.FOOTER, extra=L.legal_sheets())
