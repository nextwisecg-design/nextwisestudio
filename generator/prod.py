"""Versiunea de producție pentru nextwise.studio: pornește de la v5.html și scoate
  out/index.html (română) și out/en/index.html (engleză), cu titlu și meta reale, comutator de limbă,
  intro sărit la schimbarea limbii, favicon, robots și sitemap.
Rulare: python3 v5.py && python3 prod.py"""
import json, pathlib, re, shutil, sys
import i18n, v2

ROOT = pathlib.Path(__file__).parent
OUT = ROOT / "out"
SITE = "https://nextwise.studio"
TITLE = {"ro": "NEXTWISE | Sisteme AI și site-uri pentru firme", "en": "NEXTWISE | AI systems and websites for businesses"}
DESC = {"ro": "NEXTWISE construiește sisteme AI și site-uri pentru firme din România.", "en": "NEXTWISE builds AI systems and websites for businesses in Romania."}
H1_EN = "AI systems that work inside your company."
CAP_EN = "8 departments, one system. Drag the planet to rotate it."
DEP_EN = [["Reception", "Answers enquiries and makes bookings, after hours too."], ["Sales", "Every quote gets a follow-up. None is left forgotten."],
          ["Marketing", "Posts and reviews, published only with your approval."], ["Operations", "Tasks and deadlines kept up to date, without parallel spreadsheets."],
          ["Finance", "Invoices issued automatically after every payment."], ["Purchasing", "Compares supplier offers and proposes the order."],
          ["Admin", "Quotes, contracts and forms, from the company's templates."], ["Management", "The company's numbers on one screen."]]
TOOLS_EN = ["WhatsApp", "Email", "Calendar", "Invoicing", "Website", "Phone"]

h = (ROOT / "v5.html").read_text(encoding="utf-8")


def rep(s, a, b, n=1):
    assert s.count(a) == n, (s.count(a), a[:80])
    return s.replace(a, b)


# ── 1. baza de producție (română)
old_title = re.search(r"<title>(.*?)</title>", h).group(1)
head = (f'<title>{TITLE["ro"]}</title>\n<link rel="canonical" href="%%CANON%%">\n'
        f'<link rel="alternate" hreflang="ro" href="{SITE}/">\n<link rel="alternate" hreflang="en" href="{SITE}/en/">\n<link rel="alternate" hreflang="x-default" href="{SITE}/">\n'
        '<link rel="icon" href="/favicon.svg" type="image/svg+xml">\n<link rel="icon" href="/favicon.ico" sizes="any">\n<link rel="apple-touch-icon" href="/apple-touch-icon.png">\n<meta name="theme-color" content="#090A11">\n'
        f'<meta property="og:type" content="website">\n<meta property="og:site_name" content="NEXTWISE">\n<meta property="og:title" content="{TITLE["ro"]}">\n'
        f'<meta property="og:description" content="{DESC["ro"]}">\n<meta property="og:url" content="%%CANON%%">')
h = rep(h, f"<title>{old_title}</title>", head)
# comutatorul de limbă în meniu și în subsol
h = rep(h, '<a class="btn" href="#contact">Scrie-ne</a></nav>', '<a class="lang" href="%%OTHER%%" hreflang="%%OTHERLANG%%" lang="%%OTHERLANG%%">%%OTHERLABEL%%</a><a class="btn" href="#contact">Scrie-ne</a></nav>')
h = rep(h, '<a href="https://anpc.ro/" target="_blank" rel="noopener">ANPC</a></nav>', '<a href="https://anpc.ro/" target="_blank" rel="noopener">ANPC</a><a href="%%OTHER%%" hreflang="%%OTHERLANG%%" lang="%%OTHERLANG%%">%%OTHERNAME%%</a></nav>')
h = rep(h, "</style>\n<noscript>", ".links a.lang{display:inline-flex!important;align-items:center;justify-content:center;min-width:44px;height:38px;padding:0 12px;border:1px solid var(--line2);border-radius:999px;font-size:14px;font-weight:600;color:var(--text)}\n"
        "body.skip #intro{display:none}body.skip .site,body.skip .site *{transition-duration:0s!important;transition-delay:0s!important}\n</style>\n<noscript>")
# introul apare o singură dată pe sesiune: la schimbarea limbii intri direct în site
h = rep(h, "\nwindow.__nw=", "\ntry{if(sessionStorage.getItem('nw_in')){B.classList.add('skip');enter();setTimeout(()=>B.classList.remove('skip'),400)}}catch(e){}\n"
        "$('#enter').addEventListener('click',()=>{try{sessionStorage.setItem('nw_in','1')}catch(e){}});\nwindow.__nw=")

LANG = {"ro": dict(CANON=f"{SITE}/", OTHER="/en/", OTHERLANG="en", OTHERLABEL="EN", OTHERNAME="English"),
        "en": dict(CANON=f"{SITE}/en/", OTHER="/", OTHERLANG="ro", OTHERLABEL="RO", OTHERNAME="Română")}


def fill(s, lang):
    for k, v in LANG[lang].items():
        s = s.replace(f"%%{k}%%", v)
    assert "%%" not in s
    return s


ro = fill(h, "ro")

# ── 2. engleza
ro_s = (ROOT / "ro_strings.txt").read_text(encoding="utf-8").split("\n")
en_s = (ROOT / "en_strings.txt").read_text(encoding="utf-8").rstrip("\n").split("\n")
assert len(ro_s) == len(en_s), (len(ro_s), len(en_s))
D = dict(zip(ro_s, en_s))
# adresa de contact a firmei s-a schimbat pe denis@ (24.11): aceleași fraze, altă adresă
for k in list(D):
    if "darius@nextwise.studio" in k and k != "darius@nextwise.studio":
        D[k.replace("darius@nextwise.studio", "denis@nextwise.studio")] = D[k].replace("darius@nextwise.studio", "denis@nextwise.studio")
D.update({"Datele firmei": "Company details", "Identificare": "Identification", "Contact": "Contact",
          "Denumire: NEXTWISE AI STUDIO S.R.L.": "Name: NEXTWISE AI STUDIO S.R.L."})
D[TITLE["ro"]] = TITLE["en"]
D[DESC["ro"]] = DESC["en"]
D["Intră în site"] = "Enter the site"
SAME = {"EN", "RO", "English", "Română", "website", "NEXTWISE", "agent", "%%OTHERLABEL%%", "%%OTHERNAME%%", "%%CANON%%", "#090A11"}

e = h
a, b = e.index("<h1>"), e.index("</h1>") + 5
e = e[:a] + "<h1>" + v2.make_h1(H1_EN) + "</h1>" + e[b:]
# cuvintele din h1 nu se traduc nod cu nod
for w in H1_EN.split():
    SAME.add(w)
e, missing = i18n.translate(e, D, SAME)
if missing:
    print("NETRADUSE:", len(missing))
    for m in missing[:40]:
        print("  ", m[:140])
    sys.exit(1)
e = rep(e, '<html lang="ro">', '<html lang="en">')
m = re.search(r"const DEP=(\[\[.*?\]\]),TOOLS=(\[.*?\]);", e)
e = e.replace(m.group(0), "const DEP=" + json.dumps(DEP_EN, ensure_ascii=False) + ",TOOLS=" + json.dumps(TOOLS_EN, ensure_ascii=False) + ";")
cap = re.search(r'content:"(\d+ departamente[^"]*)"', e)
e = e.replace(cap.group(1), CAP_EN)
en = fill(e, "en")

# ── 3. verificare: nu mai rămâne română în pagina engleză (în afara numelor proprii și a adresei)
parts, ns = i18n.nodes(en)
left = sorted({t.strip() for _, t in ns if re.search(r"[ăâîșțĂÂÎȘȚ]", t)})
allowed = ("Bacău", "Română")
left = [t for t in left if not any(x in t for x in allowed)]
if left:
    print("ROMÂNĂ RĂMASĂ:", left[:20]); sys.exit(1)

# ── 4. fișierele
if OUT.exists():
    shutil.rmtree(OUT)
(OUT / "en").mkdir(parents=True)
(OUT / "index.html").write_text(ro, encoding="utf-8")
(OUT / "en" / "index.html").write_text(en, encoding="utf-8")
(OUT / "robots.txt").write_text(f"User-agent: *\nAllow: /\nSitemap: {SITE}/sitemap.xml\n")
(OUT / "sitemap.xml").write_text(f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">\n'
                                 f'<url><loc>{SITE}/</loc><xhtml:link rel="alternate" hreflang="ro" href="{SITE}/"/><xhtml:link rel="alternate" hreflang="en" href="{SITE}/en/"/></url>\n'
                                 f'<url><loc>{SITE}/en/</loc><xhtml:link rel="alternate" hreflang="ro" href="{SITE}/"/><xhtml:link rel="alternate" hreflang="en" href="{SITE}/en/"/></url>\n</urlset>\n')
for f in ("favicon.svg", "favicon.ico", "apple-touch-icon.png"):
    shutil.copy(ROOT / "static" / f, OUT / f)
print("out/index.html", len(ro) // 1024, "KB · out/en/index.html", len(en) // 1024, "KB ·", sorted(p.name for p in OUT.rglob("*") if p.is_file()))
