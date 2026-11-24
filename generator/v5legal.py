"""Partea legală și de contact pentru versiunea 5 (24.11.2026).
Surse pentru ce cere legea: Legea 365/2002 art. 5 și Legea 31/1990 art. 74 (datele firmei), GDPR art. 13,
Legea 506/2004 art. 4 (cookie-uri), Ordinul ANPC 449/2022 modificat în 2026 (pictograma SAL; SOL nu mai e cerut
din 20.07.2025), OUG 34/2014 (consumatori). Rezumat luat din articole din 2026, neverificat pe textele oficiale.
Datele firmei: din cererea ONRC din 09.11.2026 (de verificat pe certificat). Capitalul social lipsește.
Textele sunt CIORNE: trebuie citite de un avocat înainte de publicare. Ce nu știm e marcat cu [paranteze]."""
from common import esc

CO = dict(
    name="NEXTWISE AI STUDIO S.R.L.",
    seat="str. Radu Negru nr. 4, sc. A, ap. 8, Bacău, jud. Bacău",
    reg="J04/662/2023", cui="48024527", capital="200 lei",
    email="denis@nextwise.studio", phone="0756 079 049", phone_href="+40756079049",
)
SAL_URL = "https://reclamatiisal.anpc.ro/"
SOL_URL = "https://ec.europa.eu/consumers/odr"
import anpc_b64 as _A
M = lambda t: f"<mark>[{t}]</mark>"  # noqa: E731  loc de completat, vizibil
CAPITAL = CO["capital"] or M("capital social de completat")

GETS = ["O pagină clară, cu serviciile și datele de contact", "Făcută pornind de la datele publice ale firmei tale",
        "Arată bine pe telefon", "Personalizare printr-un formular de câteva minute",
        "Găzduire și mentenanță incluse în abonament", "Plată cu cardul sau cu factură"]
HOW = [("Vorbim", "Ne suni sau ne scrii. Nu plătești nimic."),
       ("Vezi macheta", "Îți trimitem site-ul făcut pentru firma ta."),
       ("Plătești doar dacă îți place", "Cu cardul sau cu factură."),
       ("Completezi formularul și publicăm", "Pui textele și pozele tale în câteva minute.")]


def prod(check, mock_html):
    gets = "".join(f"<li>{check}<span>{esc(x)}</span></li>" for x in GETS)
    how = "".join(f"<li><div><b>{esc(a)}</b><span>{esc(b)}</span></div></li>" for a, b in HOW)
    return f'''<div class="prod rv"><div class="inn">
    <div class="l"><h2 class="h2">Site de prezentare pentru firma ta.</h2>
      <p class="lead">Pentru firme mici care nu au site sau au unul care nu le mai reprezintă. Vezi macheta făcută pentru firma ta înainte să plătești ceva.</p>
      <p class="price"><b>de la 200 €</b><span>mentenanță de la 30 € pe lună</span></p>
      <p class="vat">Prețurile includ TVA.</p>
      <p class="cta2"><a class="btn" href="#contact">Cere macheta</a><button class="btn soft" type="button" data-open="cosmina-petrescu">Vezi un site făcut de noi</button></p></div>
    <div class="r">{mock_html}</div>
    <div class="pdet"><div><h3>Ce primești</h3><ul class="pts">{gets}</ul></div><div><h3>Cum merge</h3><ol class="how">{how}</ol></div></div>
  </div></div>'''


WAYS = '''<div class="ways2">
      <div class="pers"><p class="nm">Darius</p><a href="mailto:darius@nextwise.studio">darius@nextwise.studio</a><a href="https://wa.me/40726551387" target="_blank" rel="noopener"><small>WhatsApp</small>0726 551 387</a></div>
      <div class="pers"><p class="nm">Denis</p><a href="mailto:denis@nextwise.studio">denis@nextwise.studio</a><a href="tel:+40756079049"><small>Telefon</small>0756 079 049</a></div>
    </div>'''

FOOTER = f'''<footer class="lg"><div class="wrap">
  <div class="f-top">
    <div class="f-co"><b>{CO["name"]}</b><span>Nr. Reg. Com.: {CO["reg"]}</span><span>CUI: {CO["cui"]}</span><span>Email: {CO["email"]}</span><span>Telefon: {CO["phone"]}</span></div>
    <nav class="f-links" aria-label="Informații legale"><button type="button" data-open="firma">Datele firmei</button><button type="button" data-open="termeni">Termeni și condiții</button><button type="button" data-open="confidentialitate">Politica de confidențialitate</button><button type="button" data-open="cookies">Politica de cookie-uri</button><a href="https://anpc.ro/" target="_blank" rel="noopener">ANPC</a></nav>
    <div class="anpc"><a href="{SAL_URL}" target="_blank" rel="noopener"><img src="data:image/png;base64,{_A.SAL}" width="250" height="62" alt="ANPC, Soluționarea alternativă a litigiilor"></a></div>
  </div>
  <div class="f-bot"><span>© 2026 {CO["name"]}</span><span>NEXTWISE, AI Systems Studio</span></div>
</div></footer>'''

DRAFT = "Ultima actualizare: 24.11.2026"
ID = f'{CO["name"]}, cu sediul social în {CO["seat"]}, înregistrată la Registrul Comerțului sub nr. {CO["reg"]}, CUI {CO["cui"]}, capital social {CAPITAL}'

LEGAL = [
    ("termeni", "Termeni și condiții", [
        ("1. Cine suntem", [f"Site-ul nextwise.studio este administrat de {ID}. Ne poți scrie la {CO['email']} sau ne poți suna la {CO['phone']}."]),
        ("2. Ce este acest site", ["Site-ul prezintă serviciile NEXTWISE: sisteme cu agenți AI, automatizări și site-uri de prezentare.",
                                   "Serviciile noastre se adresează firmelor și altor profesioniști.",
                                   "Informațiile de pe site sunt de prezentare. Nu sunt o ofertă fermă. Un serviciu se contractează doar pe baza unei oferte și a unui contract scris sau a unei comenzi confirmate de noi."]),
        ("3. Serviciile", ["<b>Sisteme AI și automatizări:</b> se stabilesc după o discuție, pe bază de ofertă și contract. Termenele, prețul și ce se livrează sunt cele din contract.",
                           "<b>Site de prezentare:</b> îți arătăm o machetă făcută pentru firma ta, fără nicio obligație. Dacă o vrei, plătești, completezi un formular cu textele și pozele tale, iar noi publicăm site-ul. Găzduirea și mentenanța se plătesc lunar.",
                           "Abonamentul de mentenanță are o durată minimă de 6 până la 12 luni. Durata exactă este scrisă în ofertă, înainte să plătești."]),
        ("4. Prețuri și plată", ["Prețurile de pe site sunt în euro, includ TVA și sunt prețuri de pornire.",
                                 "Plata se face cu cardul, printr-un procesator de plăți, sau prin transfer bancar, pe baza facturii.",
                                 "Prețul final este cel din ofertă sau din pagina de plată, afișat înainte să plătești."]),
        ("5. Dacă ești consumator", ["Dacă ești persoană fizică și cumperi în afara activității tale profesionale, ai drepturile din OUG nr. 34/2014, inclusiv dreptul de a te retrage din contract în 14 zile, fără să dai un motiv, în condițiile și cu excepțiile din lege.",
                                     f"Cererea de retragere o trimiți la {CO['email']}, iar noi îți confirmăm primirea pe email.",
                                     "Dacă ne ceri să începem lucrul înainte să treacă cele 14 zile și apoi te retragi, plătești partea de serviciu făcută până atunci, în condițiile legii."]),
        ("6. Drepturi de autor", ["Textele, grafica, animațiile și codul site-ului aparțin NEXTWISE sau sunt folosite cu acordul titularilor. Nu le poți copia sau refolosi fără acordul nostru scris.",
                                  "Numele și siglele clienților din portofoliu aparțin acestora și apar cu acordul lor."]),
        ("7. Răspundere", ["Ne străduim ca informațiile de pe site să fie corecte și la zi. Pot apărea erori, pe care le corectăm când le aflăm.",
                           "Nu răspundem pentru conținutul site-urilor externe către care trimitem."]),
        ("8. Reclamații și litigii", [f"Dacă ai o nemulțumire, scrie-ne la {CO['email']}. Îți răspundem în cel mult 30 de zile.",
                                      f'Consumatorii se pot adresa Autorității Naționale pentru Protecția Consumatorilor (<a href="https://anpc.ro/" target="_blank" rel="noopener">anpc.ro</a>) și pot folosi soluționarea alternativă a litigiilor (<a href="{SAL_URL}" target="_blank" rel="noopener">reclamatiisal.anpc.ro</a>).',
                                      "Acestor termeni li se aplică legea română. Litigiile care nu se rezolvă pe cale amiabilă se judecă de instanțele competente din România."]),
        ("9. Modificări", ["Putem actualiza acești termeni. Versiunea în vigoare este cea publicată pe site, cu data ultimei modificări.",
                           "Dacă versiunea în engleză diferă de cea în română, se aplică versiunea în română."]),
    ]),
    ("confidentialitate", "Politica de confidențialitate", [
        ("1. Cine răspunde de datele tale", [f"Operatorul datelor este {ID}. Pentru orice întrebare despre datele tale, scrie-ne la {CO['email']}."]),
        ("2. Ce date prelucrăm", ["<b>Când ne contactezi</b> (email, telefon, WhatsApp): numele, numărul de telefon, adresa de email, firma și ce ne scrii.",
                                  "<b>Când te contactăm noi:</b> datele de contact ale firmei, luate din surse publice (profilul firmei pe Google, site-ul firmei, registre publice): denumirea, telefonul, emailul și numele persoanei de contact, dacă este public.",
                                  "<b>Când devii client:</b> datele de facturare și datele persoanei de contact.",
                                  "<b>Date tehnice:</b> furnizorul de găzduire păstrează jurnale tehnice (adresa IP, tipul de browser, data accesării), necesare pentru funcționarea și securitatea site-ului.",
                                  "Site-ul nu are formulare și nu îți cere să îți faci cont.",
                                  "Nu ești obligat să ne dai date. Fără datele de contact nu îți putem răspunde."]),
        ("3. De ce le prelucrăm și în ce temei", ["<ul><li>ca să îți răspundem și să îți facem o ofertă: demersuri la cererea ta, înainte de un contract (art. 6 alin. 1 lit. b din GDPR);</li><li>ca să încheiem și să derulăm contractul: executarea contractului (lit. b);</li><li>ca să prezentăm serviciile noastre firmelor care ar putea avea nevoie de ele: interes legitim (lit. f); te poți opune oricând, iar noi ștergem datele;</li><li>facturare și contabilitate: obligație legală (lit. c);</li><li>securitatea site-ului: interes legitim (lit. f).</li></ul>",
                                                   "Nu îți trimitem mesaje comerciale fără acordul tău."]),
        ("4. Cui le transmitem", ["Folosim furnizori care prelucrează date în numele nostru: găzduirea site-ului (Netlify), email, WhatsApp (când ne scrii acolo), servicii de inteligență artificială care ne ajută să sortăm și să redactăm mesaje, procesatorul de plăți și programul de facturare. Datele ajung la autorități doar când legea ne obligă.",
                                  "Unii furnizori sunt în afara Spațiului Economic European. În aceste cazuri transferul se face cu garanțiile cerute de GDPR (decizie de adecvare sau clauze contractuale standard)."]),
        ("5. Cât timp le păstrăm", ["Mesajele care nu duc la un contract le păstrăm cel mult 12 luni. Datele firmelor pe care le contactăm noi le păstrăm cel mult 12 luni de la ultimul contact sau până ne ceri să le ștergem. Datele din contracte și facturi le păstrăm pe durata cerută de legislația financiar-contabilă."]),
        ("6. Drepturile tale", ["Ai dreptul de acces, de rectificare, de ștergere, de restricționare, de portabilitate și de opoziție, iar acolo unde prelucrarea se bazează pe acord, îl poți retrage oricând.",
                                f"Ne scrii la {CO['email']} și îți răspundem în cel mult o lună.",
                                'Dacă ești nemulțumit, poți face plângere la Autoritatea Națională de Supraveghere a Prelucrării Datelor cu Caracter Personal (<a href="https://www.dataprotection.ro/" target="_blank" rel="noopener">dataprotection.ro</a>).']),
        ("7. Decizii automate", ["Nu luăm decizii cu efecte juridice asupra ta doar prin mijloace automate și nu facem profilare."]),
        ("8. Modificări", ["Dacă schimbăm această politică, publicăm versiunea nouă pe site, cu data ultimei modificări.",
                         "Dacă versiunea în engleză diferă de cea în română, se aplică versiunea în română."]),
    ]),
    ("firma", "Datele firmei", [
        ("Identificare", [f"Denumire: {CO['name']}", f"Sediu social: {CO['seat']}", f"Nr. Reg. Com.: {CO['reg']}", f"CUI: {CO['cui']}", f"Capital social: {CAPITAL}"]),
        ("Contact", [f"Email: {CO['email']}", f"Telefon: {CO['phone']}"]),
    ]),
    ("cookies", "Politica de cookie-uri", [
        ("Ce folosim", ["Site-ul nu folosește cookie-uri de analiză sau de publicitate și nu încarcă instrumente de urmărire de la terți.",
                        "Fonturile și animațiile sunt încărcate de pe site, nu de la terți.",
                        "Site-ul ține minte, doar pe durata vizitei și doar în browserul tău, că ai trecut de animația de început. Nu este un cookie și nu ajunge la noi."]),
        ("Dacă se schimbă ceva", ["Dacă vom adăuga statistici de trafic, hărți, video sau alte servicii care pun cookie-uri, îți vom cere acordul înainte, printr-un banner în care refuzul e la fel de ușor ca acceptul, și vom lista aici fiecare cookie."]),
        ("Linkuri externe", ["Când apeși pe un link către alt serviciu (de exemplu WhatsApp sau pagina de plată), se aplică politica acelui serviciu."]),
    ]),
]


def legal_sheets():
    out = []
    for slug, title, secs in LEGAL:
        body = "".join(f"<h4>{esc(h)}</h4>" + "".join(x if x.startswith("<ul>") else f"<p>{x}</p>" for x in ps) for h, ps in secs)
        out.append(f'''
<div class="sheet legal" id="sheet-{slug}" style="--pb-h:258" hidden>
  <div class="sh-back" data-close></div>
  <div class="sh-panel" role="dialog" aria-modal="true" aria-labelledby="sh-t-{slug}" tabindex="-1">
    <header class="sh-head"><div><p class="sh-kind">Informații legale</p><h3 id="sh-t-{slug}">{esc(title)}</h3></div><button class="sh-x" type="button" data-close aria-label="Închide">Închide</button></header>
    <div class="lg-body"><p class="draft">{esc(DRAFT)}</p>{body}</div>
  </div>
</div>''')
    return "".join(out)


CSS = r'''
/* ── v5: site-uri cu detalii, contact pe persoane, subsol legal, pagini legale */
mark{background:rgba(255,181,71,.16);color:var(--amber);padding:0 5px;border-radius:4px}
.vat{margin-top:10px;font-size:14.5px;color:var(--muted)}
.cta2{margin-top:26px;display:flex;gap:10px;flex-wrap:wrap}.prod .l .cta2 .btn{margin-top:0}
.pdet{grid-column:1/-1;display:grid;grid-template-columns:1fr 1fr;gap:clamp(24px,4vw,56px);padding:clamp(26px,4vw,56px);border-top:1px solid var(--line)}
.pdet h3{font-size:14px;color:var(--faint);font-weight:600;margin-bottom:14px}.pdet .pts{margin-top:0}
.how{list-style:none;counter-reset:h;display:grid;gap:14px}
.how li{counter-increment:h;display:grid;grid-template-columns:30px minmax(0,1fr);gap:14px;align-items:start}
.how li::before{content:counter(h);width:30px;height:30px;border-radius:50%;border:1px solid var(--violet);color:var(--link);display:grid;place-items:center;font:500 13.5px 'Geist Mono',monospace}
.how b{display:block;font-weight:600}.how span{color:var(--muted);font-size:15.5px}
.ways2{margin-top:44px;display:grid;grid-template-columns:repeat(2,minmax(0,auto));justify-content:start;gap:clamp(28px,7vw,110px)}
.pers{display:grid;gap:8px;align-content:start}.pers .nm{font-size:15px;color:var(--muted)}
.pers a{font-size:clamp(18px,1.9vw,25px);font-weight:500;letter-spacing:-.01em;overflow-wrap:anywhere}
.pers a small{display:block;font-size:13px;font-weight:400;color:var(--faint);letter-spacing:0;margin-top:4px}
@media (hover:hover) and (pointer:fine){.pers a:hover{color:var(--cyan)}}
footer.lg{padding:46px 0 40px;border-top:1px solid var(--line);background:rgba(9,10,17,.88);color:var(--muted);font-size:14.5px}
footer.lg .wrap{display:block}
.f-top{display:grid;grid-template-columns:minmax(0,1.5fr) minmax(0,1fr) auto;gap:36px;align-items:start}
.f-co{display:grid;gap:4px}.f-co b{color:var(--text);font-size:16px;font-weight:600;margin-bottom:4px}
.f-links{display:grid;gap:10px;justify-items:start}
.f-links button,.f-links a{color:var(--text2);font-size:15px;text-align:left;text-decoration:underline;text-decoration-color:var(--line2);text-underline-offset:4px}
.anpc{display:grid;gap:10px}.anpc a{display:block;line-height:0}.anpc img{width:250px;max-width:100%;height:auto;display:block}
.f-bot{margin-top:30px;padding-top:18px;border-top:1px solid var(--line);display:flex;justify-content:space-between;gap:12px;flex-wrap:wrap;color:var(--faint);font-size:13.5px}
.sheet.legal .sh-panel{width:min(820px,100%)}
.lg-body{padding:clamp(20px,3vw,34px);font-size:16px;line-height:1.6;color:var(--text2)}
.lg-body h4{color:var(--text);font-size:18px;font-weight:600;margin:28px 0 8px}
.lg-body p{margin-top:8px}.lg-body ul{margin:8px 0 0 20px}.lg-body li{margin-top:5px}
.lg-body a{color:var(--link);text-decoration:underline}.lg-body b{color:var(--text);font-weight:600}
.draft{color:var(--faint);font-size:14px;font-family:'Geist Mono',monospace}
@media (max-width:1000px){.f-top{grid-template-columns:1fr 1fr}.pdet{grid-template-columns:1fr}}
/* ── telefon: mai compact */
@media (max-width:640px){
 section{padding:56px 0}.s-head{margin-bottom:26px;gap:14px}
 .hero{padding-bottom:44px}
 .bento{gap:10px}
 .cell{min-height:0;display:grid;grid-template-columns:62px minmax(0,1fr);column-gap:16px;padding:18px 18px 18px 16px;align-items:start}
 .cell .mv{grid-row:1/3;width:150px;height:64px;margin:2px -88px -36px 0;transform:scale(.41);transform-origin:left top}
 .cell h3{grid-column:2;margin-top:0;padding-top:0;font-size:19px}.cell p{grid-column:2;font-size:15px;margin-top:3px}
 .prod .l,.prod .r,.pdet{padding:24px 20px}.prod .r{padding-top:6px}
 .mock{max-width:280px;margin:0 auto}.cta2 .btn{flex:1 1 100%;justify-content:center}
 .steps{row-gap:0}.steps li{display:grid;grid-template-columns:20px minmax(0,1fr);column-gap:16px;padding:0 0 26px}
 .steps li .nd{grid-row:1/3;margin-top:5px}
 .steps li:not(:last-child)::before{content:"";position:absolute;left:9px;top:28px;bottom:2px;width:2px;background:var(--line2)}
 .steps h3{grid-column:2;margin-top:0;font-size:22px}.steps p{grid-column:2;max-width:none}
 .princ{margin-top:36px}.princ li{font-size:17.5px;padding:16px 0}
 .ways2{grid-template-columns:1fr;gap:28px;margin-top:30px}
 .f-top{grid-template-columns:1fr;gap:26px}
 .pb-body{padding:18px}
}
'''


# ── al patrulea proiect: tabloul nostru intern (date din codul HQ, 24.11.2026: package.json, README, netlify/functions,
# netlify/database/migrations, src/agents.ts). Fără link: e sistem intern. Fără nume de variabile, adrese sau chei.
from v2data import PORTFOLIO as _P

# fără ore exacte și fără detalii de conturi: sunt informații din interior (check 24.11.2026)
DAY = [("dimineața", "SDR România", "aduce lead-urile noi pentru vânzări"),
       ("", "Social Media Manager", "scrie postările de mâine, de aprobat"),
       ("", "Executive Assistant", "sortează emailurile și pregătește răspunsuri"),
       ("", "VP Sales", "verifică lead-urile înainte de apeluri"),
       ("la prânz", "Operations Associate", "face task-urile aprobate"),
       ("seara", "Software Engineer", "publică reparațiile aprobate"),
       ("", "Chief of Staff", "scrie raportul de seară")]
_day = "".join(f'<li style="--i:{i}"><i class="t">{a}</i><b>{esc(b)}</b><span>{esc(c)}</span></li>' for i, (a, b, c) in enumerate(DAY))

HQ = dict(
    slug="nextwise-hq", hue=258, name="NEXTWISE HQ", kind="Tablou de conducere cu agenți AI",
    who="Sistemul nostru intern", since="noiembrie 2026",
    badge="Live, intern", live=False, green=True, bar="sistem intern, fără adresă publică",
    summary="Locul din care conducem firma: lead-uri, task-uri, încasări, postări și rapoarte. Agenții AI lucrează după program, iar oamenii aprobă.",
    delivered=["Lead-uri, task-uri și încasări într-un singur loc", "Agenți AI programați, organizați pe echipe",
               "Postări aprobate de om și publicate automat", "Mod de apeluri pentru vânzări, cu un lead pe ecran",
               "Raport de dimineață pe email și rapoarte PDF"],
    stack=["React", "Neon Postgres", "Netlify", "Notion", "Agenți Claude"],
    intro="Am construit pentru noi ce construim și pentru clienți: un singur ecran din care se vede tot ce mișcă în firmă. Agenții scriu, oamenii aprobă, iar tabloul arată în fiecare dimineață ce e de făcut. Este sistem intern, de aceea nu are adresă publică.",
    did=[("Tabloul principal", "Ținta lunii, încasările și stadiul fiecărui lead, dintr-o privire."),
         ("Lead-uri și apeluri", "Fișa fiecărui lead, ritmul de contact și un mod de apeluri cu un singur lead pe ecran."),
         ("Task-uri și aprobări", "Fiecare om își vede sarcinile. Ce propun agenții așteaptă un „da”."),
         ("Echipa de agenți", "Organigramă pe patru echipe, program, jurnal și stare la zi pentru fiecare agent."),
         ("Lecții", "Feedbackul oamenilor se adună într-un loc pe care agenții îl citesc la fiecare rulare."),
         ("Social", "Postări cu text și imagine, aprobate de om, apoi publicate automat."),
         ("Rapoarte", "Raport de dimineață pe email și rapoarte PDF de seară."),
         ("Roluri", "Conducerea vede tot. Vânzările văd doar lead-urile și sarcinile lor.")],
    spec=[("Găzduire", "Netlify, domeniu propriu, HTTPS"),
          ("Aplicație", "React 18, Vite, TypeScript; 44 de componente de ecran"),
          ("Server", "9 funcții serverless, din care 3 programate și 3 în fundal"),
          ("Bază de date", "Neon Postgres, 14 tabele, 12 migrări aplicate automat după fiecare publicare"),
          ("Sursă", "Notion, sincronizat din oră în oră; un rând se rescrie doar dacă s-a schimbat"),
          ("Scriere", "butoanele scriu întâi în Notion, apoi în baza site-ului"),
          ("Agenți", "15 agenți Claude activi, pe 4 echipe, fiecare cu program și jurnal"),
          ("Imagini", "postările se desenează pe server, cu Satori și Resvg"),
          ("Rapoarte", "PDF generat cu pdf-lib, trimis pe email dimineața"),
          ("Publicare", "Buffer API, doar după aprobarea unui om"),
          ("Secrete", "doar în variabile de mediu, niciodată în cod")],
    diagram=dict(ins=["Agenți Claude", "Echipa"], core="HQ: React + funcții", store="Neon Postgres",
                 outs=["Notion", "Buffer", "Email", "PDF"]),
    tech_extra=f'<h4>O zi obișnuită în HQ</h4><ol class="day">{_day}</ol>',
)
PORTFOLIO5 = [_P[0], HQ, _P[1], _P[2]]

CSS += r"""
@media (min-width:701px){.pb-grid{grid-template-columns:repeat(2,minmax(0,1fr))}}
.day{list-style:none;font-family:'Geist Mono',monospace;font-size:13.5px;border:1px solid var(--line);border-radius:14px;overflow:hidden}
.day li{display:grid;grid-template-columns:78px minmax(0,1fr);gap:2px 14px;padding:11px 16px;border-top:1px solid var(--line);position:relative}
.day li:first-child{border-top:0}
.day li::before{content:"";position:absolute;inset:0;background:color-mix(in srgb,var(--pb-c) 18%,transparent);opacity:0;animation:dayrun 21s linear infinite;animation-delay:calc(var(--i)*3s)}
.day .t{grid-row:1/3;font-style:normal;color:color-mix(in srgb,var(--pb-c) 72%,#fff);position:relative}
.day b{font-family:'Geist',sans-serif;font-size:15px;font-weight:600;color:var(--text);position:relative}
.day span{color:var(--text2);position:relative}
@keyframes dayrun{0%,13%{opacity:1}15%,100%{opacity:0}}
@media (prefers-reduced-motion:reduce){.day li::before{animation:none}}
"""
