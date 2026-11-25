"""NEXTWISE · versiunea 2 (24.11.2026): intro cu particule care formează numele, buton „Intră în site”,
rețea de particule care își schimbă forma la scroll, carduri de portofoliu în stilul paginii Pro bono din HQ,
care se deschid cu fișa tehnică."""
from common import *
from v2data import PORTFOLIO, MODULE_HUES

MV = [
    '<span class="mv chat"><i></i><i></i><i></i></span>',
    '<span class="mv ping"><i></i><b></b><i></i></span>',
    '<span class="mv doc"><i></i><i></i><i></i><i></i></span>',
    '<span class="mv eq"><i></i><i></i><i></i><i></i><i></i><i></i></span>',
    '<span class="mv chk"><i></i><i></i><i></i></span>',
    '<span class="mv spark"><svg viewBox="0 0 120 44" preserveAspectRatio="none"><path pathLength="1" d="M2,36 L22,30 L40,33 L58,18 L76,22 L96,8 L118,12"/></svg></span>',
]
CHECK = '<svg viewBox="0 0 16 16" aria-hidden="true"><path d="M3 8.5l3.2 3.2L13 5"/></svg>'
ARROW = '<svg viewBox="0 0 16 16" aria-hidden="true"><path d="M5 11L11 5M6 5h5v5"/></svg>'


SHOW_DATES = True


def diagram(p):
    d, hue = p["diagram"], p["hue"]
    ins, outs = d["ins"], d["outs"]
    Hh = 330 if outs else 215
    cx, cy = 150, 150
    o = [f'<svg class="dia" viewBox="0 0 360 {Hh}" role="img" aria-label="Schema sistemului {esc(p["name"])}">']
    paths = []

    def xs(n, a=44, b=316):
        return [180] if n == 1 else [a + (b - a) * i / (n - 1) for i in range(n)]

    for i, (lab, x) in enumerate(zip(ins, xs(len(ins), 50, 310))):
        pth = f"M{x:.0f},52 C{x:.0f},100 {cx},90 {cx},{cy - 23}"
        paths.append((pth, False))
        anchor = "middle" if len(ins) == 1 or 0 < i < len(ins) - 1 else ("start" if i == 0 else "end")
        tx = x if anchor == "middle" else (x - 8 if anchor == "start" else x + 8)
        ty = 30 if (i % 2 == 0 or len(ins) < 3) else 14
        o.append(f'<circle class="n" cx="{x:.0f}" cy="46" r="6"/><text class="l" x="{tx:.0f}" y="{ty}" text-anchor="{anchor}">{esc(lab)}</text>')
    paths.append((f"M{cx + 75},{cy} L250,{cy}", True))
    for i, (lab, x) in enumerate(zip(outs, xs(len(outs), 30, 330))):
        pth = f"M{cx},{cy + 23} C{cx},{cy + 80} {x:.0f},{cy + 60} {x:.0f},264"
        paths.append((pth, False))
        anchor = "middle" if 0 < i < len(outs) - 1 else ("start" if i == 0 else "end")
        tx = x if anchor == "middle" else (x - 8 if anchor == "start" else x + 8)
        ty = 292 if i % 2 == 0 else 312
        o.append(f'<circle class="n" cx="{x:.0f}" cy="270" r="6"/><text class="l" x="{tx:.0f}" y="{ty}" text-anchor="{anchor}">{esc(lab)}</text>')
    for k, (pth, both) in enumerate(paths):
        o.append(f'<path class="e" d="{pth}"/>')
        o.append(f'<circle class="pu" r="2.6"><animateMotion dur="{2.2 + (k % 3) * .5:.1f}s" begin="{k * .35:.2f}s" repeatCount="indefinite" path="{pth}"'
                 + (' keyPoints="0;1;0" keyTimes="0;0.5;1" calcMode="linear"' if both else "") + "/></circle>")
    o.append(f'<rect class="core" x="{cx - 75}" y="{cy - 23}" width="150" height="46" rx="12"/><text class="lc" x="{cx}" y="{cy + 5}" text-anchor="middle">{esc(d["core"])}</text>')
    o.append(f'<rect class="st" x="250" y="{cy - 23}" width="104" height="46" rx="12"/><text class="ls" x="302" y="{cy + 4}" text-anchor="middle">{esc(d["store"])}</text>')
    o.append("</svg>")
    return "".join(o)


def card(p):
    items = "".join(f"<li>{CHECK}<span>{esc(x)}</span></li>" for x in p["delivered"])
    stack = "".join(f"<li>{esc(s)}</li>" for s in p["stack"])
    link = (f'<a class="pb-link" href="{p["url"]}" target="_blank" rel="noopener">{esc(p["domain"])}{ARROW}</a>' if p["live"]
            else '<span class="pb-link off">Sistem intern, fără adresă publică</span>')
    return f'''
<article class="pb-card rv" style="--pb-h:{p["hue"]}" data-slug="{p["slug"]}">
  <div class="pb-cover">
    <span class="pb-bar" aria-hidden="true"><i></i><i></i><i></i><em>{esc(p["bar"])}</em></span>
    <span class="pb-art" aria-hidden="true"><small class="pb-x">NEXTWISE <i>×</i></small><b>{esc(p["name"])}</b><small>{esc(p["kind"])}</small></span>
    <span class="pb-live {"on" if (p["live"] or p.get("green")) else "in"}"><i></i>{esc(p["badge"])}</span>
  </div>
  <div class="pb-body">
    <div class="pb-top"><span class="pb-kind">{esc(p["kind"])}</span>{('<span class="pb-since">din ' + esc(p["since"]) + "</span>") if SHOW_DATES else ""}</div>
    <h3>{esc(p["name"])}</h3>
    <p class="pb-who">{esc(p["who"])}</p>
    <p class="pb-sum">{esc(p["summary"])}</p>
    <h4>Ce am livrat</h4>
    <ul class="pb-list">{items}</ul>
    <ul class="pb-stack" aria-label="Tehnologii">{stack}</ul>
    <div class="pb-foot">
      <button class="pb-open" type="button" data-open="{p["slug"]}">Deschide fișa tehnică</button>
      {link}
    </div>
  </div>
</article>'''


def sheet(p):
    did = "".join(f'<li style="--i:{i}"><b>{esc(a)}</b><span>{esc(b)}</span></li>' for i, (a, b) in enumerate(p["did"]))
    spec = "".join(f'<div style="--i:{i}"><dt>{esc(a)}</dt><dd>{esc(b)}</dd></div>' for i, (a, b) in enumerate(p["spec"]))
    link = (f'<a class="btn" href="{p["url"]}" target="_blank" rel="noopener">Deschide {esc(p["domain"])}</a>' if p["live"] else "")
    return f'''
<div class="sheet" id="sheet-{p["slug"]}" style="--pb-h:{p["hue"]}" hidden>
  <div class="sh-back" data-close></div>
  <div class="sh-panel" role="dialog" aria-modal="true" aria-labelledby="sh-t-{p["slug"]}" tabindex="-1">
    <header class="sh-head">
      <div><p class="sh-kind">{esc(p["kind"])}</p><h3 id="sh-t-{p["slug"]}">{esc(p["name"])}</h3><p class="sh-who">{esc(p["who"])}{(", din " + esc(p["since"])) if SHOW_DATES else ""}</p></div>
      <button class="sh-x" type="button" data-close aria-label="Închide fișa">Închide</button>
    </header>
    <div class="sh-body">
      <div class="sh-col">
        <p class="sh-intro">{esc(p["intro"])}</p>
        <h4>Ce am făcut</h4>
        <ul class="sh-did">{did}</ul>
        {link}
      </div>
      <div class="sh-col tech">
        <h4>Cum circulă datele</h4>
        {diagram(p)}
        <h4>Fișa tehnică</h4>
        <dl class="sh-spec">{spec}</dl>{p.get("tech_extra", "")}
      </div>
    </div>
  </div>
</div>'''


mods = "".join(f'<li class="cell rv" style="--h:{MODULE_HUES[i]}">{MV[i]}<h3>{esc(n)}</h3><p>{esc(d)}</p></li>' for i, (n, d) in enumerate(MODULES))
marq = "".join(f'<span style="--h:{MODULE_HUES[i]}">{esc(n)}</span>' for i, (n, _) in enumerate(MODULES))
steps = "".join(f'<li style="--h:{[258, 205, 32, 330][i]}"><i class="nd"></i><h3>{esc(a)}</h3><p>{esc(b)}</p></li>' for i, (a, b) in enumerate(STEPS))
princ = "".join(f"<li>{esc(x)}</li>" for x in PRINCIPLES)
nav = "".join(f'<a href="#{k}">{esc(v)}</a>' for k, v in NAV[:-1])
sp = SITE_PRODUCT
pts = "".join(f"<li>{CHECK}<span>{esc(x)}</span></li>" for x in sp["points"])
h1 = "".join(f'<span class="w"><span style="--i:{i}">{w}</span></span> ' for i, w in enumerate("Sisteme AI care lucrează în firma ta.".split()))
mails = "".join(f'<a href="mailto:{m}">{m}</a>' for m in CONTACT["emails"])

CSS = r'''
%%FONTS%%
@property --ang{syntax:'<angle>';initial-value:0deg;inherits:false}
:root{--ink:#090A11;--side:#0E0F17;--surface:#12131B;--raised:#1A1B25;--card:#13141C;--line:#24252F;--line2:#353748;--text:#EDEEF5;--text2:#CFD1DE;--muted:#9C9FB2;--faint:#818497;
--violet:#8E7BFF;--blue:#5B8CFF;--cyan:#3DD6F5;--mint:#7CF0C5;--amber:#FFB547;--pink:#FF5FA8;--green:#4ADE80;--link:#B9AEFF;
--spec:linear-gradient(90deg,#8E7BFF,#5B8CFF,#3DD6F5,#7CF0C5,#FFB547,#FF5FA8);
--ease:cubic-bezier(.23,1,.32,1);--pad:clamp(18px,4vw,56px)}
*{box-sizing:border-box;margin:0;padding:0}
html{scroll-behavior:smooth;background:var(--ink)}
body{font-family:'Geist',system-ui,sans-serif;background:var(--ink);color:var(--text);font-size:17px;line-height:1.55;-webkit-font-smoothing:antialiased;overflow-x:hidden}
body:not(.entered){overflow:hidden;height:100svh}
body.locked{overflow:hidden}
a{color:inherit;text-decoration:none}button{font:inherit;color:inherit;cursor:pointer;border:0;background:none}
:focus-visible{outline:2px solid var(--cyan);outline-offset:3px;border-radius:6px}
h1,h2,h3,h4{text-wrap:balance}
.sr{position:absolute;width:1px;height:1px;overflow:hidden;clip-path:inset(50%)}
.wrap{max-width:1280px;margin:0 auto;padding:0 var(--pad)}
#fx{position:fixed;inset:0;width:100%;height:100%;z-index:0;pointer-events:none}
.site{position:relative;z-index:1;opacity:0;pointer-events:none;transition:opacity .9s var(--ease) .25s}
.entered .site{opacity:1;pointer-events:auto}
/* intro */
#intro{position:fixed;inset:0;z-index:50;display:grid;place-items:center;transition:opacity .7s var(--ease),visibility 0s .7s}
#intro .stack{position:absolute;top:57%;left:0;right:0;display:grid;justify-items:center;gap:26px;padding:0 20px;text-align:center}
#intro p{font-family:'Geist Mono',monospace;font-size:14px;color:var(--text2);letter-spacing:.04em;opacity:0;animation:fade 1s var(--ease) 1.1s forwards}
.enter{position:relative;padding:17px 34px;border-radius:999px;font-weight:600;font-size:17px;color:#fff;background:#0D0E16;opacity:0;transform:scale(.95);animation:pop .7s var(--ease) 1.7s forwards;transition:transform .16s var(--ease)}
.enter::before{content:"";position:absolute;inset:-2px;border-radius:999px;z-index:-1;background:conic-gradient(from var(--ang),#8E7BFF,#3DD6F5,#7CF0C5,#FFB547,#FF5FA8,#8E7BFF);animation:spin 3.2s linear infinite}
.enter::after{content:"";position:absolute;inset:-14px;border-radius:999px;z-index:-2;background:conic-gradient(from var(--ang),#8E7BFF,#3DD6F5,#7CF0C5,#FFB547,#FF5FA8,#8E7BFF);filter:blur(22px);opacity:.55;animation:spin 3.2s linear infinite}
.enter:active{transform:scale(.97)}
@media (hover:hover) and (pointer:fine){.enter:hover{transform:scale(1.04)}}
.entered #intro{opacity:0;visibility:hidden;pointer-events:none}
@keyframes spin{to{--ang:360deg}}@keyframes fade{to{opacity:1}}@keyframes pop{to{opacity:1;transform:none}}
/* progress + nav */
.prog{position:fixed;top:0;left:0;right:0;height:3px;background:var(--spec);transform-origin:left;transform:scaleX(0);z-index:30}
.nav{position:fixed;top:16px;left:0;right:0;z-index:20}
.nav .in{display:flex;align-items:center;justify-content:space-between;height:58px;padding:0 8px 0 22px;border:1px solid var(--line);border-radius:999px;background:rgba(12,13,20,.88)}
.brand{font-weight:800;letter-spacing:.22em;font-size:14.5px}
.links{display:flex;gap:26px;align-items:center;font-size:15px;color:var(--text2)}
.btn{display:inline-flex;align-items:center;gap:8px;background:linear-gradient(120deg,#6E5AE8,#8E7BFF 45%,#3DD6F5);color:#fff;font-weight:600;padding:12px 22px;border-radius:999px;font-size:15.5px;transition:transform .14s var(--ease),filter .2s}
.btn:active{transform:scale(.97)}
.btn.soft{background:rgba(255,255,255,.06);border:1px solid var(--line2)}
@media (hover:hover) and (pointer:fine){.links a:not(.btn):hover{color:#fff}.btn:hover{filter:brightness(1.14)}}
/* hero */
.hero{min-height:100svh;display:flex;align-items:center;padding:120px 0 60px}
.hero .wrap{width:100%}.hero .txt{max-width:640px}
.hero h1{font-size:clamp(44px,6.8vw,104px);line-height:.97;letter-spacing:-.048em;font-weight:600}
.w{display:inline-block;overflow:hidden;vertical-align:bottom;padding:0 .05em .12em 0;margin:0 -.05em -.12em 0}
.w>span{display:inline-block;transform:translateY(112%)}
.entered .w>span{transform:none;transition:transform 1s var(--ease);transition-delay:calc(.45s + var(--i)*70ms)}
.hero .sub{margin-top:26px;font-size:clamp(18px,1.5vw,21px);color:var(--text2);max-width:40ch;line-height:1.45}
.hero .cta{margin-top:32px;display:flex;gap:12px;flex-wrap:wrap}
.hero .sub,.hero .cta{opacity:0;transform:translateY(14px)}
.entered .hero .sub,.entered .hero .cta{opacity:1;transform:none;transition:opacity .9s var(--ease) 1.05s,transform .9s var(--ease) 1.05s}
.entered .hero .cta{transition-delay:1.2s}
/* marquee */
.marq{overflow:hidden;border-block:1px solid var(--line);background:rgba(9,10,17,.7);padding:22px 0}
.marq div{display:flex;gap:56px;width:max-content;animation:slide 38s linear infinite}
.marq span{font-size:clamp(22px,2.6vw,36px);font-weight:600;letter-spacing:-.03em;color:hsl(var(--h) 90% 70%);white-space:nowrap;display:flex;align-items:center;gap:56px}
.marq span::after{content:"";width:10px;height:10px;border-radius:50%;background:currentColor}
@keyframes slide{to{transform:translateX(-50%)}}
/* sections */
section{padding:clamp(72px,9vw,130px) 0;position:relative}
.s-head{display:grid;grid-template-columns:minmax(0,7fr) minmax(0,5fr);gap:32px;align-items:end;margin-bottom:40px}
.h2{font-size:clamp(34px,4.6vw,64px);line-height:1.02;letter-spacing:-.04em;font-weight:600}
.s-head p{color:var(--text2);font-size:18px;max-width:40ch;justify-self:end}
/* modules */
.bento{list-style:none;display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:14px}
.cell{--c:hsl(var(--h) 88% 66%);border:1px solid var(--line);border-radius:22px;background:linear-gradient(160deg,hsl(var(--h) 80% 60%/.14),transparent 52%),rgba(19,20,28,.92);padding:26px;min-height:250px;display:flex;flex-direction:column;transition:border-color .25s,transform .3s var(--ease)}
.cell h3{font-size:24px;font-weight:600;letter-spacing:-.02em;margin-top:auto;padding-top:26px}
.cell p{color:var(--muted);margin-top:6px}
@media (hover:hover) and (pointer:fine){.cell:hover{border-color:hsl(var(--h) 80% 60%/.6);transform:translateY(-4px)}}
.mv{display:flex;height:64px;align-items:flex-end;gap:7px;color:var(--c)}
.mv i,.mv b{display:block;background:currentColor;border-radius:6px}
.chat{flex-direction:column;align-items:flex-start;justify-content:flex-end;gap:6px}
.chat i{height:14px;border-radius:8px 8px 8px 2px;transform-origin:left;animation:bub 3.6s var(--ease) infinite}
.chat i:nth-child(1){width:64px}.chat i:nth-child(2){width:96px;margin-left:34px;border-radius:8px 8px 2px 8px;opacity:.5;animation-delay:.5s}.chat i:nth-child(3){width:48px;animation-delay:1s}
@keyframes bub{0%,8%{transform:scale(0);opacity:0}16%,84%{transform:none;opacity:1}100%{transform:none;opacity:0}}
.chat i:nth-child(2){animation-name:bub2}@keyframes bub2{0%,8%{transform:scale(0);opacity:0}16%,84%{transform:none;opacity:.5}100%{opacity:0}}
.ping{align-items:center;gap:0;width:150px;position:relative;border-bottom:0}
.ping::before{content:"";position:absolute;left:8px;right:8px;top:50%;height:2px;background:currentColor;opacity:.3}
.ping i{width:16px;height:16px;border-radius:50%;background:var(--ink);border:2px solid currentColor;position:relative;z-index:1}.ping i:last-child{margin-left:auto}
.ping b{position:absolute;left:3px;top:50%;width:10px;height:10px;margin-top:-5px;border-radius:50%;background:#fff;z-index:2;animation:go 2.4s cubic-bezier(.77,0,.175,1) infinite alternate}
@keyframes go{to{transform:translateX(134px)}}
.doc{flex-direction:column;align-items:flex-start;justify-content:flex-end;gap:8px}
.doc i{height:6px;border-radius:3px;transform-origin:left;animation:wr 3.2s var(--ease) infinite}
.doc i:nth-child(1){width:120px}.doc i:nth-child(2){width:150px;animation-delay:.25s;opacity:.7}.doc i:nth-child(3){width:96px;animation-delay:.5s;opacity:.7}.doc i:nth-child(4){width:132px;animation-delay:.75s;opacity:.45}
@keyframes wr{0%{transform:scaleX(0)}30%,90%{transform:none}100%{transform:scaleX(0)}}
.eq i{width:12px;height:100%;border-radius:4px;transform-origin:bottom;animation:eq 1.3s ease-in-out infinite alternate}
.eq i:nth-child(1){animation-delay:-.2s}.eq i:nth-child(2){animation-delay:-.9s;opacity:.8}.eq i:nth-child(3){animation-delay:-.5s}.eq i:nth-child(4){animation-delay:-1.1s;opacity:.7}.eq i:nth-child(5){animation-delay:-.3s}.eq i:nth-child(6){animation-delay:-.7s;opacity:.6}
@keyframes eq{from{transform:scaleY(.18)}to{transform:scaleY(1)}}
.chk{flex-direction:column;align-items:flex-start;justify-content:flex-end;gap:8px}
.chk i{width:130px;height:12px;border-radius:4px;background:linear-gradient(90deg,currentColor 12px,transparent 12px 20px,color-mix(in srgb,currentColor 30%,transparent) 20px);animation:tick 3.6s steps(1) infinite;opacity:.35}
.chk i:nth-child(2){animation-delay:.6s;width:150px}.chk i:nth-child(3){animation-delay:1.2s;width:110px}
@keyframes tick{0%{opacity:.35}25%,92%{opacity:1}}
.spark svg{width:160px;height:64px;overflow:visible}.spark path{fill:none;stroke:currentColor;stroke-width:3;stroke-linecap:round;stroke-linejoin:round;vector-effect:non-scaling-stroke;stroke-dasharray:1;animation:dr 3.4s var(--ease) infinite}
@keyframes dr{0%{stroke-dashoffset:1}45%,88%{stroke-dashoffset:0}100%{stroke-dashoffset:-1}}
/* product */
.prod{position:relative;border-radius:30px;padding:2px;background:conic-gradient(from var(--ang),#8E7BFF,#3DD6F5,#7CF0C5,#FFB547,#FF5FA8,#8E7BFF);animation:spin 9s linear infinite}
.prod .inn{border-radius:28px;background:#0C0D15;display:grid;grid-template-columns:minmax(0,6fr) minmax(0,6fr);overflow:hidden}
.prod .l{padding:clamp(26px,4vw,56px)}
.prod .lead{color:var(--text2);font-size:18px;margin-top:16px;max-width:44ch}
.price{margin-top:28px;display:flex;align-items:baseline;gap:16px;flex-wrap:wrap}
.price b{font-size:clamp(44px,5.2vw,76px);font-weight:600;letter-spacing:-.045em;line-height:1;white-space:nowrap;background:var(--spec);-webkit-background-clip:text;background-clip:text;color:transparent}
.price span{color:var(--muted)}
.pts{list-style:none;margin-top:24px;display:grid;gap:10px}
.pts li,.pb-list li{display:grid;grid-template-columns:18px minmax(0,1fr);gap:8px;align-items:start}
.pts svg,.pb-list svg{width:16px;height:16px;margin-top:5px;fill:none;stroke:var(--green);stroke-width:2.2;stroke-linecap:round;stroke-linejoin:round}
.prod .l .btn{margin-top:28px}
.prod .r{position:relative;padding:clamp(26px,4vw,56px);display:grid;place-items:center;background:radial-gradient(420px 320px at 80% 10%,rgba(61,214,245,.16),transparent 70%),radial-gradient(420px 320px at 10% 100%,rgba(255,95,168,.14),transparent 70%)}
.mock{width:100%;max-width:440px;border:1px solid var(--line2);border-radius:16px;background:var(--surface);overflow:hidden;transform:perspective(1100px) rotateY(-9deg) rotateX(4deg)}
.mock .bar{height:34px;border-bottom:1px solid var(--line);display:flex;gap:6px;align-items:center;padding:0 14px}.mock .bar i{width:8px;height:8px;border-radius:50%;background:var(--line2)}
.mock .pg{padding:22px;display:grid;gap:12px}
.mock .b{border-radius:8px;transform-origin:left;animation:bld 7s var(--ease) infinite}
.b1{height:26px;width:70%;background:#fff}.b2{height:10px;background:var(--raised);animation-delay:.35s!important}.b3{height:10px;width:55%;background:var(--raised);animation-delay:.6s!important}
.b4{height:32px;width:120px;border-radius:999px!important;background:linear-gradient(120deg,#8E7BFF,#3DD6F5);animation-delay:.95s!important}
.b5{height:110px;background:linear-gradient(135deg,rgba(255,95,168,.5),rgba(255,181,71,.45));animation-delay:1.4s!important}
.g3{display:grid;grid-template-columns:repeat(3,1fr);gap:10px}.g3 .b{height:50px;background:var(--raised)}.g3 .b:nth-child(1){animation-delay:1.9s}.g3 .b:nth-child(2){animation-delay:2.1s}.g3 .b:nth-child(3){animation-delay:2.3s}
@keyframes bld{0%{transform:scaleX(0);opacity:0}9%,90%{transform:none;opacity:1}100%{transform:none;opacity:0}}
.mock-cap{margin-top:16px;font-size:13.5px;color:var(--faint);text-align:center}
/* portfolio: carduri în stilul paginii Pro bono din HQ */
.pb-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(min(100%,350px),1fr));gap:22px;perspective:1400px}
.pb-card{--pb-c:hsl(var(--pb-h) 72% 58%);display:flex;flex-direction:column;min-width:0;border:1px solid var(--line);border-radius:18px;background:var(--card);overflow:hidden;transform:rotateX(var(--rx,0deg)) rotateY(var(--ry,0deg));transition:border-color .2s,transform .35s var(--ease),box-shadow .35s}
.pb-cover{display:block;position:relative;aspect-ratio:16/9;overflow:hidden;color:#fff;background:radial-gradient(120% 90% at 85% 10%,color-mix(in srgb,var(--pb-c) 72%,transparent),transparent 60%),radial-gradient(90% 80% at 0% 100%,color-mix(in srgb,var(--violet) 55%,transparent),transparent 65%),#12101f}
.pb-cover::after{content:"";position:absolute;inset:26px 0 0;background:linear-gradient(105deg,transparent 40%,rgba(255,255,255,.16) 50%,transparent 60%);transform:translateX(-100%)}
.pb-bar{position:absolute;inset:0 0 auto;height:28px;display:flex;align-items:center;gap:5px;padding:0 12px;background:rgba(255,255,255,.08);border-bottom:1px solid rgba(255,255,255,.08)}
.pb-bar i{width:7px;height:7px;border-radius:50%;background:rgba(255,255,255,.28)}
.pb-bar em{margin-left:8px;font-style:normal;font-size:12px;color:rgba(255,255,255,.78);white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.pb-art{position:absolute;inset:28px 0 0;display:grid;align-content:center;justify-items:start;padding:0 24px;gap:6px}
.pb-art b{font-size:clamp(26px,2.6vw,34px);font-weight:700;letter-spacing:-.025em;line-height:1.08}
.pb-art small{font-size:13.5px;color:rgba(255,255,255,.8)}
.pb-art .pb-x{font-size:13px;font-weight:700;letter-spacing:.22em;color:#fff}
.pb-art .pb-x i{font-style:normal;font-weight:400;letter-spacing:0;margin-left:4px;color:color-mix(in srgb,var(--pb-c) 70%,#fff)}
.pb-live{position:absolute;right:14px;bottom:14px;display:inline-flex;align-items:center;gap:8px;font-size:13px;font-weight:600;padding:6px 12px;border-radius:999px;background:rgba(9,10,17,.72);border:1px solid rgba(255,255,255,.16)}
.pb-live i{width:8px;height:8px;border-radius:50%;background:var(--green)}
.pb-live.on i{animation:blink 1.8s ease-in-out infinite}.pb-live.in i{background:var(--amber)}
@keyframes blink{50%{box-shadow:0 0 0 6px rgba(74,222,128,0)}0%{box-shadow:0 0 0 0 rgba(74,222,128,.55)}}
.pb-body{display:flex;flex-direction:column;gap:9px;padding:20px 22px 22px;flex:1}
.pb-top{display:flex;justify-content:space-between;align-items:center;gap:8px;font-size:13px}
.pb-kind{padding:3px 10px;border-radius:999px;background:color-mix(in srgb,var(--pb-c) 16%,transparent);color:color-mix(in srgb,var(--pb-c) 75%,var(--text));font-weight:550}
.pb-since{color:var(--faint)}
.pb-body h3{font-size:23px;letter-spacing:-.02em;margin-top:4px}
.pb-who{font-size:14.5px;color:var(--muted)}
.pb-sum{margin-top:2px;font-size:16px;line-height:1.5}
.pb-body h4{margin-top:8px;font-size:13.5px;color:var(--faint);font-weight:600}
.pb-list{list-style:none;display:grid;gap:6px;font-size:15px}
.pb-stack{list-style:none;margin-top:8px;display:flex;flex-wrap:wrap;gap:6px}
.pb-stack li{font-size:12.5px;padding:3px 9px;border-radius:6px;border:1px solid var(--line);color:var(--muted)}
.pb-foot{margin-top:auto;padding-top:16px;display:grid;gap:12px}
.pb-open{width:100%;padding:13px 16px;border-radius:12px;font-weight:600;font-size:15.5px;color:#fff;background:color-mix(in srgb,var(--pb-c) 22%,var(--raised));border:1px solid color-mix(in srgb,var(--pb-c) 50%,var(--line));transition:background .2s,transform .14s var(--ease)}
.pb-open:active{transform:scale(.98)}
.pb-link{display:inline-flex;align-items:center;gap:5px;font-size:14.5px;color:var(--link);font-weight:550;overflow-wrap:anywhere}
.pb-link svg{width:15px;height:15px;fill:none;stroke:currentColor;stroke-width:1.8;stroke-linecap:round;stroke-linejoin:round}
.pb-link.off{color:var(--faint);font-weight:400}
@media (hover:hover) and (pointer:fine){.pb-card:hover{border-color:color-mix(in srgb,var(--pb-c) 55%,var(--line));box-shadow:0 24px 60px -30px hsl(var(--pb-h) 80% 50%/.55)}.pb-card:hover .pb-cover::after{transform:translateX(100%);transition:transform .9s var(--ease)}.pb-open:hover{background:color-mix(in srgb,var(--pb-c) 34%,var(--raised))}.pb-link:not(.off):hover{text-decoration:underline}}
/* fișa tehnică */
.sheet{position:fixed;inset:0;z-index:60;display:grid;place-items:center;padding:clamp(0px,2.4vw,32px)}
.sheet[hidden]{display:none}
.sh-back{position:absolute;inset:0;background:rgba(5,6,10,.92);opacity:0;transition:opacity .3s var(--ease)}
.sh-panel{--pb-c:hsl(var(--pb-h) 72% 58%);position:relative;width:min(1120px,100%);max-height:100%;overflow:auto;overscroll-behavior:contain;border:1px solid color-mix(in srgb,var(--pb-c) 45%,var(--line));border-radius:24px;background:#0C0D15;opacity:0;transform:translateY(26px) scale(.97);transition:opacity .35s var(--ease),transform .45s var(--ease)}
.sheet.open .sh-back{opacity:1}.sheet.open .sh-panel{opacity:1;transform:none}
.sh-head{position:sticky;top:0;z-index:2;display:flex;justify-content:space-between;align-items:flex-start;gap:16px;padding:clamp(20px,3vw,34px);border-bottom:1px solid var(--line);background:radial-gradient(520px 260px at 100% 0%,color-mix(in srgb,var(--pb-c) 34%,transparent),transparent 70%),#0C0D15}
.sh-kind{font-family:'Geist Mono',monospace;font-size:13px;color:color-mix(in srgb,var(--pb-c) 70%,#fff)}
.sh-head h3{font-size:clamp(32px,4.4vw,60px);font-weight:600;letter-spacing:-.045em;line-height:1;margin-top:6px}
.sh-who{color:var(--muted);margin-top:8px;font-size:15.5px}
.sh-x{flex:none;padding:10px 18px;border-radius:999px;border:1px solid var(--line2);background:rgba(255,255,255,.05);font-weight:600;font-size:15px}
.sh-body{display:grid;grid-template-columns:minmax(0,5fr) minmax(0,6fr)}
.sh-col{padding:clamp(20px,3vw,34px)}
.sh-col.tech{border-left:1px solid var(--line);background:#090A11}
.sh-intro{font-size:18.5px;line-height:1.5}
.sh-col h4{font-size:14px;color:var(--faint);font-weight:600;margin:28px 0 12px}.sh-col.tech h4:first-child{margin-top:0}
.sh-did{list-style:none}
.sh-did li{display:grid;gap:2px;padding:13px 0;border-top:1px solid var(--line)}
.sh-did b{font-weight:600;font-size:16.5px}.sh-did span{color:var(--muted);font-size:15.5px}
.sh-col .btn{margin-top:22px}
.dia{display:block;width:100%;max-width:440px;height:auto;margin:0 auto}
.dia .e{fill:none;stroke:color-mix(in srgb,var(--pb-c) 55%,transparent);stroke-width:1.3}
.dia .n{fill:#090A11;stroke:var(--pb-c);stroke-width:1.6}
.dia .l{font-family:'Geist Mono',monospace;font-size:11px;fill:var(--text2)}
.dia .core{fill:color-mix(in srgb,var(--pb-c) 26%,#12131B);stroke:var(--pb-c);stroke-width:1.4}
.dia .st{fill:#12131B;stroke:var(--line2);stroke-width:1.2}
.dia .lc{font-size:14px;font-weight:600;fill:#fff}.dia .ls{font-family:'Geist Mono',monospace;font-size:11px;fill:var(--text)}
.dia .pu{fill:#fff}
.sh-spec{font-family:'Geist Mono',monospace;font-size:13.5px;line-height:1.5;border:1px solid var(--line);border-radius:14px;overflow:hidden}
.sh-spec div{display:grid;grid-template-columns:128px minmax(0,1fr);gap:14px;padding:11px 16px;border-top:1px solid var(--line)}
.sh-spec div:first-child{border-top:0}
.sh-spec dt{color:color-mix(in srgb,var(--pb-c) 72%,#fff)}.sh-spec dd{color:var(--text2)}
.sh-spec div,.sh-did li{opacity:0;transform:translateY(8px)}
.sheet.open .sh-spec div,.sheet.open .sh-did li{opacity:1;transform:none;transition:opacity .5s var(--ease),transform .5s var(--ease);transition-delay:calc(.18s + var(--i)*45ms)}
/* process */
.stepw{position:relative;margin-top:20px}.steps{list-style:none;display:grid;grid-template-columns:repeat(4,1fr);position:relative}
.stepw::before{content:"";position:absolute;left:0;right:0;top:9px;height:2px;background:var(--line2)}
.stepw .bar{position:absolute;left:0;right:0;top:9px;height:2px;background:var(--spec);transform-origin:left;transform:scaleX(0)}
.steps li{padding-right:26px;position:relative}
.nd{display:block;width:20px;height:20px;border-radius:50%;background:var(--ink);border:2px solid var(--line2);position:relative;z-index:1;transition:border-color .4s,background .4s,box-shadow .4s}
.steps li.on .nd{border-color:hsl(var(--h) 88% 66%);background:hsl(var(--h) 88% 66%);box-shadow:0 0 0 7px hsl(var(--h) 88% 66%/.18)}
.steps h3{font-size:28px;font-weight:600;letter-spacing:-.025em;margin-top:26px}.steps p{color:var(--muted);margin-top:6px;max-width:26ch}
.princ{list-style:none;margin-top:72px;display:grid;grid-template-columns:1fr 1fr;gap:0 clamp(24px,4vw,64px)}
.princ li{padding:22px 0;border-top:1px solid var(--line);font-size:20px;color:var(--text2)}
/* contact */
.cta-box{position:relative;border-radius:34px;padding:2px;background:conic-gradient(from var(--ang),#8E7BFF,#3DD6F5,#7CF0C5,#FFB547,#FF5FA8,#8E7BFF);animation:spin 9s linear infinite}
.cta-box .inn{border-radius:32px;background:rgba(10,11,18,.9);padding:clamp(30px,6vw,88px)}
.cta-box h2{font-size:clamp(40px,6.4vw,100px);font-weight:600;letter-spacing:-.05em;line-height:.98;max-width:12ch;background:var(--spec);-webkit-background-clip:text;background-clip:text;color:transparent;padding-bottom:.08em}
.ways{margin-top:44px;display:flex;gap:clamp(22px,5vw,80px);flex-wrap:wrap}
.ways p{color:var(--muted);font-size:14.5px;margin-bottom:4px}
.ways a{display:block;font-size:clamp(19px,2vw,26px);font-weight:500;letter-spacing:-.01em}
@media (hover:hover) and (pointer:fine){.ways a:hover{color:var(--cyan)}}
footer{padding:28px 0 44px;color:var(--faint);font-size:14px;position:relative;z-index:1}
footer .wrap{display:flex;justify-content:space-between;gap:16px;flex-wrap:wrap}
.rv{opacity:0;transform:translateY(26px)}
.rv.in{opacity:1;transform:none;transition:opacity .9s var(--ease),transform .9s var(--ease);transition-delay:calc(var(--d,0)*90ms)}
.pb-card.rv{transform:translateY(40px) rotateX(10deg)}.pb-card.rv.in{transform:rotateX(var(--rx,0deg)) rotateY(var(--ry,0deg))}
.pb-card.rv.in.tilt{transition:border-color .2s,box-shadow .35s,transform .12s linear}
@media (max-width:1000px){.s-head,.prod .inn,.sh-body{grid-template-columns:1fr}.s-head p{justify-self:start}.bento{grid-template-columns:1fr 1fr}.steps{grid-template-columns:1fr 1fr;row-gap:40px}.stepw::before,.stepw .bar{display:none}.links a:not(.btn){display:none}.sh-col.tech{border-left:0;border-top:1px solid var(--line)}.mock{transform:none}.hero{align-items:flex-end;padding-bottom:64px}}
@media (max-width:640px){body{font-size:16px}.bento,.princ{grid-template-columns:1fr}.cell{min-height:210px}.steps{grid-template-columns:1fr}.sheet{padding:0}.sh-panel{border-radius:0;height:100%;border:0}.sh-spec div{grid-template-columns:1fr;gap:2px}.prod{border-radius:22px}.prod .inn{border-radius:20px}.cta-box{border-radius:24px}.cta-box .inn{border-radius:22px}.marq div{gap:36px}.marq span{gap:36px}}
@media (prefers-reduced-motion:reduce){html{scroll-behavior:auto}*,*::before,*::after{animation:none!important}.rv,.w>span,.hero .sub,.hero .cta,.sh-spec div,.sh-did li,.pb-card.rv{opacity:1!important;transform:none!important;transition:none!important}#intro p,.enter{opacity:1;transform:none}.sh-panel,.sh-back{transition:none}.mv i,.mv b,.mock .b{transform:none;opacity:1}.spark path{stroke-dashoffset:0}}
'''

JS = r'''
(()=>{
const RM=matchMedia('(prefers-reduced-motion:reduce)').matches,B=document.body;
const $=(s,r=document)=>r.querySelector(s),$$=(s,r=document)=>[...r.querySelectorAll(s)];
// ───────────────────────── particulele
const cv=$('#fx'),c=cv.getContext('2d');
const COL=['#8E7BFF','#5B8CFF','#3DD6F5','#7CF0C5','#FFB547','#FF5FA8'];
let W=0,H=0,D=1,N=0,t=0,last=0,shape='logo',al=1,mx=0,my=0,entered=false,vis=true,ready=false;
let X,Y,VX,VY,SZ,FZ,S={},edges=[],bk=[],pulses=[],seed=7;
const rnd=()=>{seed=(seed*16807)%2147483647;return seed/2147483647};
function size(){D=Math.min(devicePixelRatio||1,1.5);W=innerWidth;H=innerHeight;cv.width=W*D;cv.height=H*D;c.setTransform(D,0,0,D,0,0)}
function build(){
 seed=7;N=W<760?640:1500;X=new Float32Array(N);Y=new Float32Array(N);VX=new Float32Array(N);VY=new Float32Array(N);SZ=new Float32Array(N);FZ=new Float32Array(N).fill(1);
 const mk=()=>new Float32Array(N*3);S={sphere:mk(),rings:mk(),wave:mk(),scat:mk(),helix:mk(),logo:mk()};bk=COL.map(()=>[]);
 const cols=Math.ceil(Math.sqrt(N*2.4)),rows=Math.ceil(N/cols);
 for(let i=0;i<N;i++){const j=i*3;
  X[i]=W/2+(rnd()-.5)*40;Y[i]=H*.42+(rnd()-.5)*40;VX[i]=(rnd()-.5)*30;VY[i]=(rnd()-.5)*30;SZ[i]=.8+rnd()*1.25+(rnd()<.06?1.4:0);bk[Math.min(5,Math.floor(i/N*6))].push(i);
  const yy=1-2*(i+.5)/N,r=Math.sqrt(1-yy*yy),th=i*2.399963,rad=.8+rnd()*.2;S.sphere[j]=r*Math.cos(th)*rad;S.sphere[j+1]=yy*rad;S.sphere[j+2]=r*Math.sin(th)*rad;
  if(i%12===0){const a=rnd()*6.28,b=Math.acos(2*rnd()-1),q=.13*Math.cbrt(rnd());S.rings[j]=q*Math.sin(b)*Math.cos(a);S.rings[j+1]=q*Math.cos(b);S.rings[j+2]=q*Math.sin(b)*Math.sin(a)}
  else{const k=i%3,R=[.5,.8,1.12][k]+(rnd()-.5)*.03,a=rnd()*6.28,tx=[.5,-.4,.16][k],tz=[.35,-.55,.12][k];let x=Math.cos(a)*R,y=0,z=Math.sin(a)*R;
   let y1=y*Math.cos(tx)-z*Math.sin(tx),z1=y*Math.sin(tx)+z*Math.cos(tx);let x2=x*Math.cos(tz)-y1*Math.sin(tz),y2=x*Math.sin(tz)+y1*Math.cos(tz);S.rings[j]=x2;S.rings[j+1]=y2;S.rings[j+2]=z1}
  S.wave[j]=((i%cols)/(cols-1)-.5)*4.2;S.wave[j+1]=0;S.wave[j+2]=(Math.floor(i/cols)/(rows-1)-.5)*2.6;
  S.scat[j]=(rnd()-.5)*4.6;S.scat[j+1]=(rnd()-.5)*2.8;S.scat[j+2]=(rnd()-.5)*2.4;
  const u=i/N,ang=u*Math.PI*9+(i%2?Math.PI:0),hr=.44+(i%7===0?-(rnd()*.44):0);S.helix[j]=(u-.5)*4.4;S.helix[j+1]=Math.sin(ang)*hr;S.helix[j+2]=Math.cos(ang)*hr;
  S.logo[j]=(rnd()-.5)*2;S.logo[j+1]=(rnd()-.5)*.5;S.logo[j+2]=0}
 // muchii între vecinii de pe sferă
 const E=W<760?150:300,step=Math.floor(N/E),ns=[];for(let k=0;k<E;k++)ns.push(k*step);edges=[];
 ns.forEach(a=>{let b1=-1,b2=-1,d1=9,d2=9;ns.forEach(b=>{if(a===b)return;const dx=S.sphere[a*3]-S.sphere[b*3],dy=S.sphere[a*3+1]-S.sphere[b*3+1],dz=S.sphere[a*3+2]-S.sphere[b*3+2],d=dx*dx+dy*dy+dz*dz;if(d<d1){d2=d1;b2=b1;d1=d;b1=b}else if(d<d2){d2=d;b2=b}});if(b1>a)edges.push([a,b1]);if(b2>a)edges.push([a,b2])});
 logo()}
function logo(){const o=document.createElement('canvas'),w=1400,h=260;o.width=w;o.height=h;const g=o.getContext('2d');g.fillStyle='#fff';g.textBaseline='middle';const fs=168;g.font=`800 ${fs}px Geist, sans-serif`;
 const txt='NEXTWISE',sp=fs*.17,ws=[...txt].map(ch=>g.measureText(ch).width),tot=ws.reduce((a,b)=>a+b,0)+sp*(txt.length-1);let x=(w-tot)/2;[...txt].forEach((ch,i)=>{g.fillText(ch,x,h/2+6);x+=ws[i]+sp});
 const d=g.getImageData(0,0,w,h).data,pts=[];for(let y=0;y<h;y+=3)for(let x2=0;x2<w;x2+=3)if(d[(y*w+x2)*4+3]>128)pts.push([x2,y]);if(!pts.length)return;
 for(let i=pts.length-1;i>0;i--){const j=Math.floor(rnd()*(i+1));[pts[i],pts[j]]=[pts[j],pts[i]]}
 const pick=[];for(let i=0;i<N;i++)pick.push(pts[i%pts.length]);pick.sort((a,b)=>a[0]-b[0]);const half=tot/2;
 for(let i=0;i<N;i++){S.logo[i*3]=(pick[i][0]-w/2)/half;S.logo[i*3+1]=(pick[i][1]-h/2-6)/half;S.logo[i*3+2]=(rnd()-.5)*.05}}
function cfg(s){const m=W<760,u=Math.min(W,H);switch(s){
 case'logo':return{a:'logo',cx:W/2,cy:H*.42,s:Math.min(W*.44,540),al:1,spin:0,tilt:0};
 case'sphere':return m?{a:'sphere',cx:W*.5,cy:H*.3,s:u*.36,al:.62,spin:.22,tilt:.22}:{a:'sphere',cx:W*.74,cy:H*.5,s:u*.37,al:1,spin:.22,tilt:.22};
 case'rings':return{a:'rings',cx:W*.5,cy:H*.5,s:u*(m?.62:.52),al:m?.3:.42,spin:.16,tilt:.35};
 case'wave':return{a:'wave',cx:W*.5,cy:H*.62,s:Math.max(W*.34,300),al:m?.4:.55,spin:0,tilt:.42};
 case'scat':return{a:'scat',cx:W*.5,cy:H*.5,s:u*.5,al:.3,spin:.035,tilt:0};
 case'helix':return{a:'helix',cx:W*.5,cy:H*.74,s:m?W*.34:W*.2,al:m?.3:.42,spin:0,tilt:0,roll:.5};
 default:return m?{a:'sphere',cx:W*.5,cy:H*1.0,s:u*.7,al:.6,spin:.1,tilt:.25}:{a:'sphere',cx:W*.5,cy:H*1.08,s:u*.86,al:.7,spin:.1,tilt:.25}}}
const secs=$$('[data-shape]');
function pick(){if(!entered)return'logo';let s=secs[0].dataset.shape;const y=scrollY+H*.55;for(const e of secs)if(e.offsetTop<=y)s=e.dataset.shape;return s}
function frame(ts){if(!vis)return;const dt=Math.min(48,ts-last||16);last=ts;if(!RM)t+=dt*.001;shape=pick();const g=cfg(shape),A=S[g.a];al+=(g.al-al)*(RM?1:.05);
 const ay=(g.spin?t*g.spin:(g.a==='logo'?Math.sin(t*.7)*.14:0))+mx*.3,ax=g.tilt+(g.roll?t*g.roll:0)+my*.16,cy_=Math.cos(ay),sy_=Math.sin(ay),cx_=Math.cos(ax),sx_=Math.sin(ax),K=g.a==='logo'?.05:.035,DM=.84,wave=g.a==='wave';
 for(let i=0;i<N;i++){const j=i*3;let x=A[j],y=A[j+1],z=A[j+2];if(wave)y=Math.sin(x*2.1+t*1.2)*.14+Math.cos(z*3.1+t*.9)*.1;
  const x1=x*cy_+z*sy_,z1=-x*sy_+z*cy_,y2=y*cx_-z1*sx_,z2=y*sx_+z1*cx_,f=2.7/(2.7+z2),tx=g.cx+x1*g.s*f,ty=g.cy+y2*g.s*f;FZ[i]=f;
  if(RM){X[i]=tx;Y[i]=ty}else{VX[i]=(VX[i]+(tx-X[i])*K)*DM;VY[i]=(VY[i]+(ty-Y[i])*K)*DM;X[i]+=VX[i];Y[i]+=VY[i]}}
 c.globalCompositeOperation='source-over';c.clearRect(0,0,W,H);c.globalCompositeOperation='lighter';
 const thr=W<760?64:92,th2=thr*thr,near=[],isLogo=g.a==='logo';c.beginPath();if(!isLogo)for(const[a,b]of edges){const dx=X[a]-X[b],dy=Y[a]-Y[b];if(dx*dx+dy*dy<th2){c.moveTo(X[a],Y[a]);c.lineTo(X[b],Y[b]);near.push(a,b)}}
 c.globalAlpha=Math.min(1,al)*.5;c.strokeStyle='#6F62D8';c.lineWidth=1;c.stroke();
 c.globalAlpha=Math.min(1,al);for(let b=0;b<6;b++){c.fillStyle=COL[b];c.beginPath();for(const i of bk[b]){const r=isLogo?Math.min(1.5,SZ[i]):SZ[i]*FZ[i];c.moveTo(X[i]+r,Y[i]);c.arc(X[i],Y[i],r,0,6.2832)}c.fill()}
 if(!RM&&near.length&&pulses.length<(W<760?5:12)&&Math.random()<.2){const k=(Math.random()*near.length/2|0)*2;pulses.push({a:near[k],b:near[k+1],p:0})}
 c.fillStyle='#fff';for(let k=pulses.length-1;k>=0;k--){const p=pulses[k];p.p+=dt/560;if(p.p>=1){pulses.splice(k,1);continue}const x=X[p.a]+(X[p.b]-X[p.a])*p.p,y=Y[p.a]+(Y[p.b]-Y[p.a])*p.p;c.globalAlpha=Math.min(1,al*1.4);c.beginPath();c.arc(x,y,2.2,0,6.2832);c.fill();c.globalAlpha=al*.25;c.beginPath();c.arc(x,y,7,0,6.2832);c.fill()}
 c.globalAlpha=1;if(!RM)requestAnimationFrame(frame)}
const kick=()=>{if(RM)requestAnimationFrame(frame)};
size();build();
(document.fonts&&document.fonts.load?document.fonts.load("800 168px Geist","NEXTWISE"):Promise.resolve()).then(()=>{logo();ready=true;kick()}).catch(()=>{ready=true});
requestAnimationFrame(frame);
let rz;addEventListener('resize',()=>{clearTimeout(rz);rz=setTimeout(()=>{const ow=W;size();if(Math.abs(ow-W)>40)build();kick()},150)});
addEventListener('pointermove',e=>{mx=e.clientX/W-.5;my=e.clientY/H-.5},{passive:true});
document.addEventListener('visibilitychange',()=>{vis=!document.hidden;if(vis){last=0;requestAnimationFrame(frame)}});
// ───────────────────────── intrarea
const enterBtn=$('#enter');
function enter(){if(entered)return;entered=true;B.classList.add('entered');if(!RM)for(let i=0;i<N;i++){const dx=X[i]-W/2,dy=Y[i]-H*.42,d=Math.hypot(dx,dy)||1,p=26+Math.random()*46;VX[i]+=dx/d*p;VY[i]+=dy/d*p}kick();setTimeout(()=>{const h=$('.hero h1');h&&h.setAttribute('tabindex','-1')},50)}
enterBtn.addEventListener('click',enter);setTimeout(()=>{try{enterBtn.focus({preventScroll:true})}catch(e){}},1900);
// ───────────────────────── scroll: progres, pași, apariții
const prog=$('.prog'),steps=$('.stepw'),bar=$('.stepw .bar'),lis=$$('.steps li');
function onScroll(){const max=document.documentElement.scrollHeight-innerHeight;prog.style.transform=`scaleX(${max>0?Math.min(1,scrollY/max):0})`;
 if(steps){const r=steps.getBoundingClientRect(),p=Math.max(0,Math.min(1,(innerHeight*.78-r.top)/(innerHeight*.5)));bar.style.transform=`scaleX(${p})`;lis.forEach((li,i)=>li.classList.toggle('on',p>=i/lis.length+.04))}kick()}
addEventListener('scroll',onScroll,{passive:true});onScroll();
const io=new IntersectionObserver(es=>es.forEach(e=>{if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target)}}),{threshold:.12});
$$('.rv').forEach(e=>io.observe(e));
$$('.bento .cell,.pb-grid .pb-card').forEach((e,i)=>e.style.setProperty('--d',i%3));
// ───────────────────────── carduri: înclinare la cursor
if(matchMedia('(hover:hover) and (pointer:fine)').matches&&!RM)$$('.pb-card').forEach(cd=>{
 cd.addEventListener('pointermove',e=>{const r=cd.getBoundingClientRect();cd.classList.add('tilt');cd.style.setProperty('--ry',((e.clientX-r.left)/r.width-.5)*7+'deg');cd.style.setProperty('--rx',(.5-(e.clientY-r.top)/r.height)*5+'deg')});
 cd.addEventListener('pointerleave',()=>{cd.classList.remove('tilt');cd.style.setProperty('--ry','0deg');cd.style.setProperty('--rx','0deg')})});
// ───────────────────────── fișa tehnică
let cur=null,opener=null;
function openSheet(slug,btn){const s=document.getElementById('sheet-'+slug);if(!s)return;opener=btn;cur=s;s.hidden=false;B.classList.add('locked');s.querySelector('.sh-panel').scrollTop=0;requestAnimationFrame(()=>requestAnimationFrame(()=>{s.classList.add('open');s.querySelector('.sh-x').focus({preventScroll:true})}))}
function closeSheet(){if(!cur)return;const s=cur;cur=null;s.classList.remove('open');B.classList.remove('locked');setTimeout(()=>{s.hidden=true},RM?0:340);opener&&opener.focus({preventScroll:true})}
$$('[data-open]').forEach(b=>b.addEventListener('click',()=>openSheet(b.dataset.open,b)));
$$('[data-close]').forEach(b=>b.addEventListener('click',closeSheet));
addEventListener('keydown',e=>{if(!cur)return;if(e.key==='Escape'){closeSheet();return}if(e.key==='Tab'){const f=$$('a[href],button',cur).filter(x=>x.offsetParent!==null);if(!f.length)return;const a=f[0],z=f[f.length-1];if(e.shiftKey&&document.activeElement===a){e.preventDefault();z.focus()}else if(!e.shiftKey&&document.activeElement===z){e.preventDefault();a.focus()}}});
window.__nw={enter,openSheet,closeSheet};
})();
'''

INTRO = '<div id="intro"><span class="sr">NEXTWISE</span><div class="stack"><p>AI Systems Studio</p><button id="enter" class="enter" type="button">Intră în site</button></div></div>'


def make_h1(text):
    return "".join(f'<span class="w"><span style="--i:{i}">{w}</span></span> ' for i, w in enumerate(text.split()))


def default_prod():
    return f'''<div class="prod rv"><div class="inn">
    <div class="l"><h2 class="h2">{esc(sp["title"])}.</h2><p class="lead">{esc(sp["lead"])}</p>
      <p class="price"><b>{esc(sp["price"])}</b><span>{esc(sp["monthly"])}</span></p>
      <ul class="pts">{pts}</ul><a class="btn" href="#contact">Cere macheta</a></div>
    <div class="r"><div><div class="mock" aria-hidden="true"><div class="bar"><i></i><i></i><i></i></div><div class="pg"><div class="b b1"></div><div class="b b2"></div><div class="b b3"></div><div class="b b4"></div><div class="b b5"></div><div class="g3"><div class="b"></div><div class="b"></div><div class="b"></div></div></div></div><p class="mock-cap">Schiță de principiu. Macheta reală se face cu datele firmei tale.</p></div></div>
  </div></div>'''


def page(title, css, intro, js, head=None, prod=None, ways=None, footer=None, extra=""):
    h1 = make_h1(head or "Sisteme AI care lucrează în firma ta.")
    prod = prod or default_prod()
    ways = ways or f'<div class="ways"><div><p>Email</p>{mails}</div><div><p>Telefon</p><a href="tel:{CONTACT["phone_href"]}">{CONTACT["phone"]}</a></div></div>'
    footer = footer or '<footer><div class="wrap"><span>NEXTWISE, AI Systems Studio</span><span>România, 2026</span></div></footer>'
    return f'''<!DOCTYPE html>
<html lang="ro"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<meta name="description" content="NEXTWISE construiește sisteme AI și site-uri pentru firme din România.">
<style>{css}</style>
<noscript><style>#intro{{display:none!important}}.site{{opacity:1;pointer-events:auto}}body:not(.entered){{overflow:auto;height:auto}}.rv,.w>span,.hero .sub,.hero .cta{{opacity:1;transform:none}}</style></noscript>
</head>
<body>
<canvas id="fx" aria-hidden="true"></canvas>
{intro}
<div class="site">
<div class="prog" aria-hidden="true"></div>
<header class="nav"><div class="wrap"><div class="in"><a class="brand" href="#top">NEXTWISE</a><nav class="links" aria-label="Meniu">{nav}<a class="btn" href="#contact">Scrie-ne</a></nav></div></div></header>
<main id="top">
<div class="hero" data-shape="sphere"><div class="wrap"><div class="txt">
  <h1>{h1}</h1>
  <p class="sub">Construim agenți AI și automatizări, le legăm de programele pe care le folosești deja și rămânem lângă tine după pornire.</p>
  <p class="cta"><a class="btn" href="#portofoliu">Vezi ce am construit</a><a class="btn soft" href="#sisteme">Ce construim</a></p>
</div></div></div>
<div class="marq" aria-hidden="true"><div>{marq}{marq}</div></div>

<section id="sisteme" data-shape="rings"><div class="wrap">
  <div class="s-head rv"><h2 class="h2">Șase module care lucrează împreună.</h2><p>Alegem ce are nevoie firma ta și le legăm de programele pe care le folosești deja.</p></div>
  <ul class="bento">{mods}</ul>
</div></section>

<section id="site-uri" data-shape="wave"><div class="wrap">
  {prod}
</div></section>

<section id="portofoliu" data-shape="scat"><div class="wrap">
  <div class="s-head rv"><h2 class="h2">Sisteme construite și pentru cine.</h2><p>Deschide fișa tehnică de pe fiecare proiect ca să vezi ce e sub capotă. Site-urile de prezentare sunt mai sus, la <a href="#site-uri-facute">Site-uri</a>.</p></div>
  <div class="pb-grid">{"".join(card(p) for p in PORTFOLIO)}</div>
</div></section>

<section id="cum-lucram" data-shape="helix"><div class="wrap">
  <div class="s-head rv"><h2 class="h2">Patru pași până la un sistem pornit.</h2><p>Pornim mic, pe cazuri reale, și extindem doar ce se dovedește util.</p></div>
  <div class="stepw rv"><span class="bar" aria-hidden="true"></span><ol class="steps">{steps}</ol></div>
  <ul class="princ rv">{princ}</ul>
</div></section>

<section id="contact" data-shape="end"><div class="wrap">
  <div class="cta-box rv"><div class="inn"><h2>Spune-ne unde pierzi cel mai mult timp.</h2>
    {ways}
  </div></div>
</div></section>
</main>
{footer}
</div>
{"".join(sheet(p) for p in PORTFOLIO)}
{extra}
<script>{js}</script>
</body></html>'''

FULL_CSS = CSS.replace("%%FONTS%%", fonts_css("Geist", "Geist Mono"))

if __name__ == "__main__":
    HTML = page("NEXTWISE · Site nou · versiunea 2", FULL_CSS, INTRO, JS)
    (ROOT / "v2.html").write_text(HTML, encoding="utf-8")
    print("v2.html", len(HTML) // 1024, "KB")
