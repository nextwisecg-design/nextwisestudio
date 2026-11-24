"""Conținut comun pentru cele trei previzualizări nextwise.studio (24.11.2026).
Sursa: HQ (src/probono.ts, skin.css), brief-ul Casa Alesia (docs/BRIEF.md, PROGRESS.md), discuția cu Darius.
"""
import base64, pathlib

ROOT = pathlib.Path(__file__).parent
NM = ROOT / "node_modules"

FONT_FILES = {
    "Geist": [("@fontsource-variable/geist/files/geist-latin-wght-normal.woff2", "100 900", "normal", "L"),
              ("@fontsource-variable/geist/files/geist-latin-ext-wght-normal.woff2", "100 900", "normal", "X")],
    "Geist Mono": [("@fontsource-variable/geist-mono/files/geist-mono-latin-wght-normal.woff2", "100 900", "normal", "L"),
                   ("@fontsource-variable/geist-mono/files/geist-mono-latin-ext-wght-normal.woff2", "100 900", "normal", "X")],
    "Instrument Serif": [("@fontsource/instrument-serif/files/instrument-serif-latin-400-normal.woff2", "400", "normal", "L"),
                         ("@fontsource/instrument-serif/files/instrument-serif-latin-ext-400-normal.woff2", "400", "normal", "X"),
                         ("@fontsource/instrument-serif/files/instrument-serif-latin-400-italic.woff2", "400", "italic", "L"),
                         ("@fontsource/instrument-serif/files/instrument-serif-latin-ext-400-italic.woff2", "400", "italic", "X")],
}
RANGES = {
    "L": "U+0000-00FF,U+0131,U+0152-0153,U+02BB-02BC,U+02C6,U+02DA,U+02DC,U+0304,U+0308,U+0329,U+2000-206F,U+20AC,U+2122,U+2191,U+2193,U+2212,U+2215,U+FEFF,U+FFFD",
    "X": "U+0100-02BA,U+02BD-02C5,U+02C7-02CC,U+02CE-02D7,U+02DD-02FF,U+0304,U+0308,U+0329,U+1D00-1DBF,U+1E00-1E9F,U+1EF2-1EFF,U+2020,U+20A0-20AB,U+20AD-20C0,U+2113,U+2C60-2C7F,U+A720-A7FF",
}


def fonts_css(*families):
    out = []
    for fam in families:
        for path, weight, style, rng in FONT_FILES[fam]:
            b64 = base64.b64encode((NM / path).read_bytes()).decode()
            out.append(
                f"@font-face{{font-family:'{fam}';font-style:{style};font-weight:{weight};font-display:swap;"
                f"src:url(data:font/woff2;base64,{b64}) format('woff2');unicode-range:{RANGES[rng]}}}")
    return "\n".join(out)


# Paleta din HQ (skin.css, tema întunecată „Orbită”)
PALETTE = dict(ink="#090A11", side="#0E0F17", surface="#12131B", raised="#1A1B25", line="#24252F",
               line2="#353748", text="#EDEEF5", text2="#CFD1DE", muted="#9C9FB2", faint="#818497",
               violet="#8E7BFF", violet2="#6E5AE8", link="#B9AEFF", green="#4ADE80", amber="#F5B454")

CONTACT = dict(emails=["darius@nextwise.studio", "denis@nextwise.studio"], phone="0756 079 049", phone_href="+40756079049")

MODULES = [
    ("Recepție și cereri", "Răspuns pe WhatsApp, site și telefon, cu programări făcute direct din conversație."),
    ("Follow-up și ofertare", "Nicio ofertă trimisă și uitată. Fiecare client primește un răspuns."),
    ("Documente", "Oferte, contracte și fișe, generate din șabloanele firmei tale."),
    ("Marketing", "Postări, video scurt și recenzii, publicate doar cu aprobarea ta."),
    ("Operațiuni interne", "Sarcini, termene și evidențe, ținute la zi fără tabele paralele."),
    ("Tablou de conducere", "Cifrele firmei într-un singur ecran și un raport scurt pe telefon."),
]

SITE_PRODUCT = dict(
    title="Site de prezentare pentru firma ta",
    lead="Pentru firme mici care nu au site sau au unul care nu le mai reprezintă. Vezi macheta făcută pentru firma ta înainte să plătești ceva.",
    price="de la 200 €", monthly="mentenanță de la 30 € pe lună",
    points=["O pagină clară, cu serviciile și datele de contact", "Arată bine pe telefon", "Găzduire și mentenanță incluse în abonament",
            "Personalizare printr-un formular de câteva minute"],
)

STEPS = [
    ("Discuție", "Înțelegem cum lucrează firma azi și unde se pierde timp."),
    ("Plan", "Alegem împreună ce se construiește întâi și cum arată reușita."),
    ("Pilot", "Pornim pe o parte din firmă, pe cazuri reale."),
    ("Pornire", "Extindem, instruim echipa și rămânem pentru mentenanță."),
]

PRINCIPLES = [
    "Agentul propune, omul aprobă. Nimic nu pleacă din firmă fără un „da”.",
    "Agenți mici, cu o singură sarcină fiecare.",
    "Datele firmei rămân ale firmei, cu acces pe roluri.",
    "Nu promitem cifre pe care nu le putem dovedi.",
]

# status: "gata" = construit și testat în cod; "urmeaza" = planificat. Sursa: PROGRESS.md din proiect, 24.11.2026.
CASA = dict(
    slug="casa-alesia", name="Casa Alesia", kind="Sistem de operare cu agenți AI",
    who="Complex turistic și de evenimente, județul Cluj", since="din iunie 2026",
    status="În construcție", status_key="wip",
    summary="Restaurant, evenimente, cazare și catering, cu aceeași bucătărie. Construim un sistem pe roluri în care agenții AI propun, iar oamenii aprobă.",
    modules=[
        ("Calendar comun", "Camere, săli, evenimente și catering într-un singur calendar, sincronizat cu Google Calendar.", "gata"),
        ("Comenzi de la mese", "Aplicație web pe telefonul ospătarului. Comanda ajunge la bar, la bucătărie și în casa de marcat existentă.", "urmeaza"),
        ("Ecranele barului și bucătăriei", "Comenzile apar în timp real pe televizorul din bucătărie și pe telefon.", "gata"),
        ("Configurator de eveniment", "Pagină publică în română, engleză și germană: pachete, extra-uri, sala văzută în 3D și avans plătit online.", "gata"),
        ("Bucătărie", "Necesarul pe eveniment calculat din rețetar, ore, personal, mise en place și pierderi.", "gata"),
        ("Sarcini", "Pe persoană, cu timpul lucrat contorizat. Un agent se oferă să preia sarcinile pe care le poate face singur.", "gata"),
        ("Furnizori", "Compară ofertele, propune comanda și o trimite doar după „da”, în plafoane fixe.", "gata"),
        ("Cifrele zilei", "Vânzări, mese ocupate, stoc și marjă pe farfurie, citite din casa de marcat.", "urmeaza"),
        ("WhatsApp", "Confirmări, numărul final de invitați, remindere și cereri de recenzie.", "urmeaza"),
        ("Agenți AI", "Companionul direcției cu propuneri zilnice, agenți pentru management, agentul de ocupare, companionul bucătăriei și asistentul de pe pagina de evenimente.", "urmeaza"),
    ],
    facts=[
        ("Rulează la client", "Pe un server aflat în complex, nu în cloud."),
        ("Merge și fără internet", "Ecranele, comenzile și calendarul funcționează mai departe."),
        ("Două limbi pentru personal", "Interfața e în română și engleză."),
        ("Totul rămâne la client", "Codul, datele și conturile sunt pe numele lor."),
    ],
    stack=["Next.js", "PostgreSQL", "Agenți AI", "Tailscale"],
)

PROJECTS = [
    CASA,
    dict(slug="grupul-schiorilor", name="Grupul Schiorilor", kind="Platformă de membri",
         who="Comunitate de schiori din România", since="din noiembrie 2026",
         status="Live", status_key="live", url="https://grupulschiorilor.ro", domain="grupulschiorilor.ro",
         summary="Site și platformă de membri cu abonamente. Plățile, facturile și treburile de zi cu zi merg singure.",
         delivered=["Platformă de membri cu abonamente plătite cu cardul", "Facturi emise automat după fiecare plată",
                    "Notificări trimise membrilor", "Rutină automată care rulează în fiecare dimineață",
                    "Domeniu propriu, găzduire și suport IT"],
         stack=["Stripe", "Oblio", "Netlify", "Funcții serverless"]),
    dict(slug="cosmina-petrescu", name="Cosmina Petrescu", kind="Site de prezentare",
         who="Salon de manichiură și pedichiură", since="din noiembrie 2026",
         status="Live", status_key="live", url="https://cosminapetrescu.netlify.app", domain="cosminapetrescu.netlify.app",
         summary="Site de prezentare pe o singură pagină, gata de arătat clientelor. Exact tipul de site pe care îl facem pentru firme mici.",
         delivered=["Site pe o pagină, cu serviciile salonului", "Arată bine pe telefon", "Găzduire inclusă"],
         stack=["HTML", "Netlify"]),
]

NAV = [("sisteme", "Sisteme AI"), ("site-uri", "Site-uri"), ("portofoliu", "Portofoliu"), ("cum-lucram", "Cum lucrăm"), ("contact", "Contact")]


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def done_count():
    return sum(1 for m in CASA["modules"] if m[2] == "gata"), len(CASA["modules"])
