"""Versiunea de producție pentru nextwise.studio: pornește de la v5.html și scoate
  out/index.html (română) și out/en/index.html (engleză), cu titlu și meta reale, comutator de limbă,
  intro sărit la schimbarea limbii, favicon, robots și sitemap.
Rulare: python3 v5.py && python3 prod.py"""
import base64, hashlib, json, pathlib, re, shutil, sys
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
        f'<meta property="og:description" content="{DESC["ro"]}">\n<meta property="og:url" content="%%CANON%%">\n'
        f'<meta property="og:image" content="{SITE}/%%OGIMG%%">\n<meta property="og:image:width" content="1200">\n<meta property="og:image:height" content="630">\n'
        f'<meta property="og:locale" content="%%OGLOCALE%%">\n<meta name="twitter:card" content="summary_large_image">\n<meta name="twitter:image" content="{SITE}/%%OGIMG%%">')
h = rep(h, f"<title>{old_title}</title>", head)
# comutatorul de limbă în meniu și în subsol
h = rep(h, '<a class="btn" href="#contact">Scrie-ne</a></nav>', '<a class="lang" href="%%OTHER%%" hreflang="%%OTHERLANG%%" lang="%%OTHERLANG%%">%%OTHERLABEL%%</a><a class="btn" href="#contact">Scrie-ne</a></nav>')
h = rep(h, '<a href="https://anpc.ro/" target="_blank" rel="noopener">ANPC</a></nav>', '<a href="https://anpc.ro/" target="_blank" rel="noopener">ANPC</a><a href="%%OTHER%%" hreflang="%%OTHERLANG%%" lang="%%OTHERLANG%%">%%OTHERNAME%%</a></nav>')
h = rep(h, "</style>\n<noscript>", ".links a.lang{display:inline-flex!important;align-items:center;justify-content:center;min-width:44px;height:38px;padding:0 12px;border:1px solid var(--line2);border-radius:999px;font-size:14px;font-weight:600;color:var(--text)}\n"
        "body.skip #intro{display:none}body.skip .site,body.skip .site *{transition-duration:0s!important;transition-delay:0s!important}\n</style>\n<noscript>")
# introul apare o singură dată pe sesiune: la schimbarea limbii intri direct în site
h = rep(h, "\nwindow.__nw=", "\ntry{if(sessionStorage.getItem('nw_in')){B.classList.add('skip');enter();setTimeout(()=>B.classList.remove('skip'),400)}}catch(e){}\n"
        "$('#enter').addEventListener('click',()=>{try{sessionStorage.setItem('nw_in','1')}catch(e){}});\nwindow.__nw=")

LANG = {"ro": dict(CANON=f"{SITE}/", OTHER="/en/", OTHERLANG="en", OTHERLABEL="EN", OTHERNAME="English", OGIMG="og-ro.jpg", OGLOCALE="ro_RO"),
        "en": dict(CANON=f"{SITE}/en/", OTHER="/", OTHERLANG="ro", OTHERLABEL="RO", OTHERNAME="Română", OGIMG="og-en.jpg", OGLOCALE="en_GB")}


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
# portofoliul de site-uri (25.11.2026)
D.update({
    "Vezi site-uri făcute de noi": "See websites we made",
    "Site-uri făcute de noi.": "Websites we made.",
    "Doar site-uri, live, pe care le poți deschide. Sistemele cu agenți AI sunt mai jos, la": "Only websites, live, that you can open. The systems with AI agents are further down, under",
    "Sisteme construite și pentru cine.": "Systems we built and who for.",
    "Deschide fișa tehnică de pe fiecare proiect ca să vezi ce e sub capotă. Site-urile de prezentare sunt mai sus, la":
        "Open the technical sheet on each project to see what is under the hood. The presentation websites are further up, under",
    "Site de cabinet": "Practice website",
    "Cabinet de psihologie pentru copii și adulți, București": "Psychology practice for children and adults, Bucharest",
    "Site pentru un cabinet de psihologie, construit în jurul unui test de un minut care îi arată părintelui de unde să înceapă.":
        "A website for a psychology practice, built around a one-minute test that shows parents where to start.",
    "Test de orientare de un minut, după care cabinetul te sună": "One-minute guidance test, after which the practice calls you",
    "O pagină pentru fiecare serviciu": "One page for each service",
    "Blog cu resurse pentru părinți și pagină de recenzii": "Blog with resources for parents and a reviews page",
    "Pagini legale și ANPC": "Legal pages and consumer-protection notices",
    "Un părinte îngrijorat nu știe ce serviciu îi trebuie copilului. Site-ul îl duce întâi printr-un test scurt, iar apoi cabinetul ia legătura cu el.":
        "A worried parent does not know which service their child needs. The website first takes them through a short test, and then the practice gets in touch.",
    "Test de orientare": "Guidance test",
    "Câteva întrebări, un minut, apoi cabinetul ia legătura cu părintele.": "A few questions, one minute, then the practice contacts the parent.",
    "Servicii pe pagini separate": "Services on separate pages",
    "Evaluare, terapie, logopedie, consiliere și grupuri, fiecare cu pagina ei.": "Assessment, therapy, speech therapy, counselling and groups, each with its own page.",
    "Încredere": "Trust",
    "Povestea psihologului, recenziile părinților și un blog cu resurse.": "The psychologist's story, parents' reviews and a blog with resources.",
    "Cadru": "Framework",
    "Vercel, HTTPS": "Vercel, HTTPS",
    "servicii, test, blog, recenzii, contact": "services, test, blog, reviews, contact",
    "confidențialitate, termeni, cookie-uri, ANPC": "privacy, terms, cookies, consumer protection",
    "Părinte": "Parent", "Test": "Test", "Cabinetul": "The practice",
    "Platformă de cursuri": "Course platform",
    "Cursuri de acupunctură și medicină tradițională chineză și japoneză": "Courses in acupuncture and traditional Chinese and Japanese medicine",
    "Platformă pentru cursuri fizice de acupunctură, cu un chestionar de un minut care recomandă cursul potrivit și rezervare online.":
        "A platform for in-person acupuncture courses, with a one-minute quiz that recommends the right course, and online booking.",
    "Chestionar care recomandă cursul potrivit": "Quiz that recommends the right course",
    "O pagină pentru fiecare curs, plus un pachet": "One page for each course, plus a bundle",
    "Programare la curs și cont de cursant": "Course booking and a student account",
    "Pagini legale, de livrare și de anulare": "Legal, delivery and cancellation pages",
    "Un terapeut care vrea să învețe acupunctură nu știe cu care din cele șase cursuri să înceapă. Site-ul îi recomandă unul într-un minut, apoi îl lasă să rezerve.":
        "A therapist who wants to learn acupuncture does not know which of the six courses to start with. The website recommends one in a minute, then lets them book.",
    "Chestionar": "Quiz",
    "Câteva întrebări și o recomandare de curs, în loc de o listă din care alegi pe ghicite.": "A few questions and a course recommendation, instead of a list you pick from by guessing.",
    "Cursuri": "Courses",
    "Șase cursuri, fiecare cu pagina lui, plus un pachet.": "Six courses, each with its own page, plus a bundle.",
    "Rezervare": "Booking",
    "Programare la curs și cont pentru cursant.": "Course booking and an account for the student.",
    "Cursant": "Student",
    "cont, programare, politici de livrare și de anulare": "account, booking, delivery and cancellation policies",
    "Cookie-uri": "Cookies",
    "banner cu alegere: doar strict necesare sau toate": "banner with a choice: strictly necessary only, or all",
    "Cont": "Account",
    "Pagini": "Pages", "Legal": "Legal",
    "Schema sistemului Marius Macovei": "System diagram for Marius Macovei",
    "Schema sistemului Flaviu Mihăiță": "System diagram for Flaviu Mihăiță",
    "Deschide mariusmacovei.ro": "Open mariusmacovei.ro",
    "Deschide psihflavium.ro": "Open psihflavium.ro",
})
# texte adăugate după check-ul din 24.11.2026
D.update({
    "dimineața": "morning", "la prânz": "midday", "seara": "evening",
    "Site-ul ține minte, doar pe durata vizitei și doar în browserul tău, că ai trecut de animația de început. Nu este un cookie și nu ajunge la noi.":
        "The website remembers, only for the duration of your visit and only in your browser, that you have passed the opening animation. It is not a cookie and it does not reach us.",
    "funcții serverless": "serverless functions",
    "cont de membru, cu confirmare pe email": "member account, with email confirmation",
    "Serviciile noastre se adresează firmelor și altor profesioniști.": "Our services are meant for companies and other professionals.",
    "Abonamentul de mentenanță are o durată minimă de 6 până la 12 luni. Durata exactă este scrisă în ofertă, înainte să plătești.":
        "The maintenance subscription has a minimum term of 6 to 12 months. The exact term is written in the quote, before you pay.",
    "Dacă ne ceri să începem lucrul înainte să treacă cele 14 zile și apoi te retragi, plătești partea de serviciu făcută până atunci, în condițiile legii.":
        "If you ask us to start work before the 14 days have passed and then withdraw, you pay for the part of the service provided up to that point, as the law provides.",
    "Dacă versiunea în engleză diferă de cea în română, se aplică versiunea în română.": "If the English version differs from the Romanian one, the Romanian version applies.",
    "Când te contactăm noi:": "When we contact you:",
    "datele de contact ale firmei, luate din surse publice (profilul firmei pe Google, site-ul firmei, registre publice): denumirea, telefonul, emailul și numele persoanei de contact, dacă este public.":
        "the company's contact details, taken from public sources (the company's Google profile, its website, public registers): name, phone number, email address and the name of the contact person, if public.",
    "Nu ești obligat să ne dai date. Fără datele de contact nu îți putem răspunde.": "You are not obliged to give us data. Without contact details we cannot reply to you.",
    "ca să prezentăm serviciile noastre firmelor care ar putea avea nevoie de ele: interes legitim (lit. f); te poți opune oricând, iar noi ștergem datele;":
        "to present our services to companies that may need them: legitimate interest (point (f)); you can object at any time and we delete the data;",
    "Folosim furnizori care prelucrează date în numele nostru: găzduirea site-ului (Netlify), email, WhatsApp (când ne scrii acolo), servicii de inteligență artificială care ne ajută să sortăm și să redactăm mesaje, procesatorul de plăți și programul de facturare. Datele ajung la autorități doar când legea ne obligă.":
        "We use providers that process data on our behalf: website hosting (Netlify), email, WhatsApp (when you write to us there), artificial intelligence services that help us sort and draft messages, the payment processor and the invoicing software. Data reaches the authorities only when the law requires it.",
    "Mesajele care nu duc la un contract le păstrăm cel mult 12 luni. Datele firmelor pe care le contactăm noi le păstrăm cel mult 12 luni de la ultimul contact sau până ne ceri să le ștergem. Datele din contracte și facturi le păstrăm pe durata cerută de legislația financiar-contabilă.":
        "Messages that do not lead to a contract are kept for 12 months at most. Data about companies we contact ourselves is kept for 12 months at most from the last contact, or until you ask us to delete it. Data from contracts and invoices is kept for the period required by financial and accounting law.",
})
SAME = {"EN", "RO", "English", "Română", "website", "NEXTWISE", "agent", "%%OTHERLABEL%%", "%%OTHERNAME%%", "%%CANON%%", "#090A11", "%%OGLOCALE%%", "summary_large_image", "1200", "630", SITE + "/%%OGIMG%%"}
SAME |= {"Flaviu Mihăiță", "Marius Macovei", "mariusmacovei.ro", "psihflavium.ro", "Vercel", "Next.js, Vercel"}

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
allowed = ("Bacău", "Română", "Flaviu Mihăiță")
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
for f in ("favicon.svg", "favicon.ico", "apple-touch-icon.png", "og-ro.jpg", "og-en.jpg"):
    if (ROOT / "static" / f).exists():
        shutil.copy(ROOT / "static" / f, OUT / f)
    else:
        print("LIPSEȘTE static/" + f + " (rulează node og.mjs, apoi din nou python3 prod.py)")

# pagina 404: adresele care nu există primesc un 404 adevărat, nu prima pagină
(OUT / "404.html").write_text("""<!DOCTYPE html>
<html lang="ro"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Pagina nu există | NEXTWISE</title><meta name="robots" content="noindex">
<link rel="icon" href="/favicon.svg" type="image/svg+xml"><meta name="theme-color" content="#090A11">
<style>
*{box-sizing:border-box;margin:0}body{min-height:100vh;display:grid;place-items:center;padding:24px;background:#090A11;color:#ECEBF5;font:17px/1.5 system-ui,-apple-system,"Segoe UI",Roboto,sans-serif}
main{max-width:520px}.n{font-size:13px;letter-spacing:.32em;font-weight:700;color:#ECEBF5;text-decoration:none}
h1{font-size:clamp(34px,7vw,56px);line-height:1.04;letter-spacing:-.04em;font-weight:600;margin:28px 0 14px}
p{color:#B9B8C9}.b{display:flex;gap:10px;flex-wrap:wrap;margin-top:28px}
.b a{display:inline-flex;align-items:center;height:48px;padding:0 20px;border-radius:999px;font-weight:600;text-decoration:none;color:#fff;background:linear-gradient(90deg,#8E7BFF,#3DD6F5)}
.b a+a{background:none;border:1px solid #2A2B3A;color:#ECEBF5}a:focus-visible{outline:2px solid #3DD6F5;outline-offset:3px}
</style></head><body><main>
<a class="n" href="/">NEXTWISE</a>
<h1>Pagina asta nu există.</h1>
<p>Adresa e greșită sau pagina a fost mutată. <span lang="en">This page does not exist.</span></p>
<p class="b"><a href="/">Mergi la prima pagină</a><a href="/en/" lang="en" hreflang="en">Go to the home page</a></p>
</main></body></html>
""", encoding="utf-8")


# headerele de securitate. Scriptul fiecărei pagini e permis prin amprenta lui (sha256), deci orice alt script e blocat.
def script_hashes(doc):
    return ["'sha256-" + base64.b64encode(hashlib.sha256(s.encode("utf-8")).digest()).decode() + "'" for s in re.findall(r"<script>(.*?)</script>", doc, flags=re.S)]


hashes = sorted(set(script_hashes(ro) + script_hashes(en)))
assert 1 <= len(hashes) <= 4, hashes
CSP = ("default-src 'none'; script-src " + " ".join(hashes) + "; style-src 'unsafe-inline'; img-src 'self' data:; font-src data:; "
       "connect-src 'none'; manifest-src 'self'; base-uri 'none'; form-action 'none'; frame-ancestors 'none'")
(OUT / "_headers").write_text("/*\n  Content-Security-Policy: " + CSP + "\n  X-Frame-Options: DENY\n  X-Content-Type-Options: nosniff\n"
                              "  Referrer-Policy: strict-origin-when-cross-origin\n  Permissions-Policy: camera=(), microphone=(), geolocation=()\n", encoding="utf-8")
print("out/index.html", len(ro) // 1024, "KB · out/en/index.html", len(en) // 1024, "KB ·", sorted(p.name for p in OUT.rglob("*") if p.is_file()))
