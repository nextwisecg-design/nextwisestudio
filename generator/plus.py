"""Piese comune pentru versiunile 3 și 4: reutilizează pagina din v2 (conținut, carduri, fișe) și adaugă
animații în plus. Fiecare versiune vine cu introul ei și cu motorul ei de fundal (FX).
Contractul FX: definește `kick()` și `enter()` și pune clasa `entered` pe <body>."""
import v2

MARK_FX = "// ───────────────────────── particulele"
MARK_UI = "// ───────────────────────── scroll: progres"

CSS_PLUS = r'''
/* ── în plus față de v2 */
.sheet{clip-path:circle(0px at var(--ox,50%) var(--oy,50%));transition:clip-path .32s var(--ease)}
.sheet.open{clip-path:circle(150vmax at var(--ox,50%) var(--oy,50%));transition:clip-path .85s cubic-bezier(.77,0,.175,1)}
.sheet .sh-back{opacity:1;transition:none}.sheet .sh-panel{opacity:1;transform:none;transition:none}
.btn,.enter,.pb-open{transition:transform .14s var(--ease),filter .2s,background .2s,translate .3s var(--ease)}
.cell.rv.in{transform:perspective(900px) rotateX(var(--rx,0deg)) rotateY(var(--ry,0deg))}
.cell.rv.in.tilt{transition:border-color .25s,transform .12s linear}
.marq div{animation-name:slide2;transform:skewX(var(--sk,0deg))}
@keyframes slide2{to{translate:-50% 0}}
@media (min-width:1001px){.mock{transform:perspective(1100px) rotateY(var(--my,-9deg)) rotateX(4deg)}}
.hw{display:inline-block;overflow:hidden;vertical-align:bottom;padding:0 .05em .14em 0;margin:0 -.05em -.14em 0}
.hw>span{display:inline-block;transform:translateY(112%)}
.rv.in .hw>span{transform:none;transition:transform .95s var(--ease);transition-delay:calc(.08s + var(--i)*60ms)}
.shock{position:fixed;left:var(--sx,50%);top:var(--sy,60%);width:40px;height:40px;margin:-20px;border-radius:50%;border:2px solid #fff;box-shadow:0 0 30px 6px rgba(142,123,255,.8),inset 0 0 30px 6px rgba(61,214,245,.6);pointer-events:none;z-index:70;opacity:0}
.entered .shock{animation:shock 1.1s cubic-bezier(.2,.7,.2,1) forwards}
@keyframes shock{0%{opacity:1;transform:scale(.4)}100%{opacity:0;transform:scale(70)}}
@media (prefers-reduced-motion:reduce){.sheet,.sheet.open{clip-path:none;transition:none}.hw>span{transform:none!important}.shock{display:none}.marq div{transform:none}}
'''

JS_PLUS = r'''
// ───────────────────────── în plus: fișa se deschide din punctul apăsat
$$('[data-open]').forEach(b=>b.addEventListener('click',e=>{const s=document.getElementById('sheet-'+b.dataset.open);if(!s)return;const r=b.getBoundingClientRect();s.style.setProperty('--ox',(e.clientX||r.left+r.width/2)+'px');s.style.setProperty('--oy',(e.clientY||r.top+r.height/2)+'px')},true));
// titlurile urcă pe cuvinte
$$('.s-head .h2').forEach(h=>{h.innerHTML=h.textContent.trim().split(/\s+/).map((w,i)=>'<span class="hw"><span style="--i:'+i+'">'+w+'</span></span>').join(' ')});
const FINE=matchMedia('(hover:hover) and (pointer:fine)').matches;
if(FINE&&!RM){
 $$('.btn,.enter,.pb-open').forEach(b=>{b.addEventListener('pointermove',e=>{const r=b.getBoundingClientRect();b.style.translate=((e.clientX-r.left-r.width/2)*.2).toFixed(1)+'px '+((e.clientY-r.top-r.height/2)*.3).toFixed(1)+'px'});b.addEventListener('pointerleave',()=>{b.style.translate='0px 0px'})});
 $$('.cell').forEach(cd=>{cd.addEventListener('pointermove',e=>{const r=cd.getBoundingClientRect();cd.classList.add('tilt');cd.style.setProperty('--ry',((e.clientX-r.left)/r.width-.5)*10+'deg');cd.style.setProperty('--rx',(.5-(e.clientY-r.top)/r.height)*8+'deg')});cd.addEventListener('pointerleave',()=>{cd.classList.remove('tilt');cd.style.setProperty('--ry','0deg');cd.style.setProperty('--rx','0deg')})})}
// la scroll: textul din hero se retrage, banda se înclină după viteză, macheta se rotește
const heroT=$('.hero .txt'),mq=$('.marq div'),mock=$('.mock'),prodS=$('#site-uri');let ly=scrollY,sk=0;
function plus(){const y=scrollY,v=y-ly;ly=y;
 if(heroT){const p=Math.min(1,y/(innerHeight*.9));heroT.style.transform='translateY('+(p*-80).toFixed(1)+'px)';heroT.style.opacity=(1-p*1.15).toFixed(3)}
 sk+=(Math.max(-10,Math.min(10,v*.28))-sk)*.18;if(mq)mq.style.setProperty('--sk',sk.toFixed(2)+'deg');
 if(mock&&prodS){const r=prodS.getBoundingClientRect(),q=Math.max(0,Math.min(1,(innerHeight-r.top)/(innerHeight+r.height)));mock.style.setProperty('--my',(-24+q*36).toFixed(1)+'deg')}
 requestAnimationFrame(plus)}
if(!RM)requestAnimationFrame(plus);
'''


def assemble(fx, extra=""):
    """JS-ul paginii: începutul și partea de interfață din v2, cu alt FX la mijloc și cu extra la final."""
    J = v2.JS
    head, ui = J[:J.index(MARK_FX)], J[J.index(MARK_UI):]
    assert "window.__nw=" in ui
    ui = ui.replace("window.__nw=", JS_PLUS + extra + "\nwindow.__nw=")
    return head + fx + "\n" + ui


def build(name, title, intro, css_extra, fx, extra_js="", head=None, **kw):
    html = v2.page(title, v2.FULL_CSS + CSS_PLUS + css_extra, intro, assemble(fx, extra_js), head, **kw)
    (v2.ROOT / f"{name}.html").write_text(html, encoding="utf-8")
    print(f"{name}.html", len(html) // 1024, "KB")
