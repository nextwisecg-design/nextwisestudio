import { MARKETS, getDict } from "./content/index.mjs";

const esc = (s) => String(s ?? "").replace(/[&<>"']/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]));
const host = (u) => { try { return new URL(u).hostname.replace(/^www\./, ""); } catch { return "source"; } };
const cap = (s) => (s ? s[0].toUpperCase() + s.slice(1) : s);

export const L = {
  en: {
    top: "Free audit for", talk: "Talk it through, 20 min", prepared: "Prepared for", on: "on",
    short: "The short version", tally: ["Works", "Worth a look", "Gaps"],
    status: { ok: "Works", warn: "Worth a look", bad: "Gap", unknown: "Not seen" },
    fixesT: "Three fixes you can make this week, free",
    fixesS: "No software, no budget, no need to talk to us. Tick them off as you go; this page remembers.",
    done: "All three done. That's the free part working.",
    kitBand: "We also wrote the copy for you.", kitOpen: "Open your free kit", pdf: "Download the audit as PDF",
    chT: "How customers reach you", chS: "Every line links to where we saw it.",
    hrT: "After hours and weekends", hrS: "What a customer reads depends on where they look.",
    rvT: "What your customers say about speed",
    calcT: "What one unanswered evening is worth to you", calcS: "We won't guess your numbers. Put in yours; nothing leaves this page.",
    calcX: ["× 52 weeks × share you'd win ×"], rate: "Share of them you'd win, %", ex: "for example", year: "A year of those evenings",
    replies: "replies instantly", build: "If you want it built", timeline: "Timeline", invest: "Investment",
    investTail: "Part of the fee can be tied to a number we agree on.", book: "Book 20 minutes with Darius",
    fine: "Or just use the three fixes. They're yours either way.",
    howT: "How we made this",
    howP: (d) => `Researched with NEXTWISE's own AI agents, the same kind we build for clients, then checked line by line and sent by Darius Arvinte, our founder. Only public information, as of ${d}.`,
    read: "What we read", notDone: "What we didn't do", founder: "Founder, NEXTWISE",
    wrong: "Spotted something wrong? Reply to the email and we'll correct it.",
    draft: "Draft. Not approved yet; don't send this link.",
    kit: {
      label: "Free kit", for: "for", intro: "Ready-to-use copy, written for your business. Edit it, use it, share it inside your team. No strings.",
      back: "Back to the audit", pdf: "Download as PDF", copy: "Copy", copied: "Copied",
      s1: "After-hours replies", s1s: "Send these automatically when nobody can answer. Swap in your real response times.",
      s2: "“What happens next” lines", s2s: "Put these under your forms and booking buttons.",
      s3: "Voicemail greeting", s3s: "Thirty seconds. Record it once per office or brand.",
      s4: "Replies to your reviews", s4s: "Including the one that hurts. Answer within a day.",
      s5: "Listings checklist", s5s: "Make every place a customer finds you say the same thing.",
      where: "Where", fix: "What to check", done: "Done",
      license: (c) => `Free to use and adapt inside ${c}. Prepared by NEXTWISE from public information.`,
    },
  },
  ro: {
    top: "Audit gratuit pentru", talk: "Discutăm 20 de minute", prepared: "Pregătit pentru", on: "pe",
    short: "Pe scurt", tally: ["Merge", "De verificat", "Lipsă"],
    status: { ok: "Merge", warn: "De verificat", bad: "Lipsă", unknown: "Nevăzut" },
    fixesT: "Trei lucruri pe care le rezolvați gratuit, săptămâna asta",
    fixesS: "Fără software, fără buget, fără să vorbiți cu noi. Bifați-le pe măsură ce le faceți; pagina ține minte.",
    done: "Toate trei gata. Asta e partea gratuită, funcționând.",
    kitBand: "V-am scris și textele.", kitOpen: "Deschideți kitul gratuit", pdf: "Descărcați auditul ca PDF",
    chT: "Cum ajung clienții la dumneavoastră", chS: "Fiecare rând are link la locul unde l-am văzut.",
    hrT: "Seara și în weekend", hrS: "Ce citește un client depinde de unde se uită.",
    rvT: "Ce spun clienții despre timpul de răspuns",
    calcT: "Cât valorează o seară fără răspuns", calcS: "Nu vă ghicim cifrele. Introduceți-le pe ale dumneavoastră; nimic nu pleacă de pe pagină.",
    calcX: ["× 52 de săptămâni × cât ați câștiga ×"], rate: "Cât din ele ați câștiga, %", ex: "de exemplu", year: "Un an de astfel de seri",
    replies: "răspunde imediat", build: "Dacă vreți să-l construim", timeline: "Termen", invest: "Investiție",
    investTail: "O parte din onorariu poate fi legată de o cifră stabilită împreună.", book: "Programați 20 de minute",
    fine: "Sau folosiți doar cele trei soluții. Sunt ale dumneavoastră oricum.",
    howT: "Cum am făcut auditul",
    howP: (d) => `Documentat cu agenții AI ai NEXTWISE, de felul celor pe care îi construim pentru clienți, apoi verificat rând cu rând și trimis de echipa NEXTWISE. Doar informații publice, la data de ${d}.`,
    read: "Ce am citit", notDone: "Ce nu am făcut", founder: "Fondator, NEXTWISE",
    wrong: "Ați găsit o greșeală? Răspundeți la mesaj și o corectăm.",
    draft: "Ciornă. Încă neaprobată; nu trimiteți acest link.",
    kit: {
      label: "Kit gratuit", for: "pentru", intro: "Texte gata de folosit, scrise pentru firma dumneavoastră. Modificați-le, folosiți-le, dați-le echipei. Fără obligații.",
      back: "Înapoi la audit", pdf: "Descărcați ca PDF", copy: "Copiază", copied: "Copiat",
      s1: "Răspunsuri în afara programului", s1s: "Trimise automat când nu poate răspunde nimeni. Puneți timpii reali de răspuns.",
      s2: "Rânduri „ce urmează”", s2s: "De pus sub formulare și butoanele de rezervare.",
      s3: "Mesaj de robot telefonic", s3s: "Treizeci de secunde. Înregistrat o dată pentru fiecare locație.",
      s4: "Răspunsuri la recenzii", s4s: "Inclusiv la cea care doare. Răspundeți în aceeași zi.",
      s5: "Listă de verificare a profilurilor", s5s: "Ca peste tot unde vă găsește un client să scrie același lucru.",
      where: "Unde", fix: "Ce verificați", done: "Gata",
      license: (c) => `Liber de folosit și adaptat în ${c}. Pregătit de NEXTWISE din informații publice.`,
    },
  },
};

function rows(items, t) {
  return items
    .map(
      (r) => `<li class="row row--${esc(r.status)}">
        <div class="row-name">${esc(r.name)}</div>
        <div class="row-detail">${esc(r.detail)}${r.url ? ` <a class="src" href="${esc(r.url)}" target="_blank" rel="noopener">${esc(host(r.url))}</a>` : ""}</div>
        <div class="row-status"><span class="pill pill--${esc(r.status)}">${esc(t.status[r.status] || r.status)}</span></div>
      </li>`
    )
    .join("");
}

function shell({ lang, title, desc, V, body, draft, t }) {
  return `<!doctype html>
<html lang="${lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex, nofollow">
<title>${esc(title)} | NEXTWISE</title>
<meta name="description" content="${esc(desc)}">
<meta property="og:title" content="${esc(title)}">
<meta property="og:description" content="${esc(desc)}">
<meta property="og:image" content="https://nextwise.studio/og.png">
<meta name="theme-color" content="#0E0E1B">
<link rel="icon" href="/favicon.ico">
<link rel="stylesheet" href="/fonts/fonts.css">
<link rel="stylesheet" href="/assets/audit.css?v=${V}">
</head>
<body>
${draft ? `<p class="draft">${esc(t.draft)}</p>` : ""}
${body}
</body>
</html>`;
}

function bookUrl(a) {
  const M = MARKETS[a.market] || MARKETS.global;
  const cal = new URL(M.cal);
  cal.searchParams.set("notes", `Audit: ${a.company}`);
  return cal.toString();
}

export function renderAudit(a, V, { draft = false } = {}) {
  const lang = a.lang === "ro" ? "ro" : "en";
  const t = L[lang];
  const d = getDict(a.market, lang);
  const starter = d.pricing.tiers[0];
  const cal = bookUrl(a);
  const counts = [...a.channels, ...a.hours].reduce((m, r) => ((m[r.status] = (m[r.status] || 0) + 1), m), {});
  const hasKit = Boolean(a.kit);

  const body = `<header class="top">
  <div class="w top-in">
    <a class="mark" href="/" aria-label="NEXTWISE">NEXTWISE</a>
    <span class="top-for">${esc(t.top)} ${esc(a.company)}</span>
    <a class="btn btn--primary btn--sm" href="${esc(cal)}" target="_blank" rel="noopener">${esc(t.talk)}</a>
  </div>
</header>

<main id="main">
  <section class="cover">
    <div class="w cover-in">
      <div>
        <p class="cover-for">${esc(t.prepared)} <strong>${esc(a.company)}</strong> ${esc(t.on)} ${esc(a.date)}</p>
        <h1${String(a.headline).split(/\s+/).length > 12 || /\S{18,}/.test(a.headline) ? ' class="long"' : ""}>${esc(a.headline)}</h1>
        <p class="cover-intro">${esc(a.intro)}</p>
        ${a.scope ? `<p class="cover-scope">${esc(a.scope)}${a.scopeUrl ? ` <a href="${esc(a.scopeUrl)}" target="_blank" rel="noopener">${lang === "ro" ? "Sursa" : "Source"}</a>` : ""}</p>` : ""}
      </div>
      <aside class="short" aria-labelledby="short-t">
        <h2 id="short-t">${esc(t.short)}</h2>
        <ul>${a.summary.map((s) => `<li>${esc(s)}</li>`).join("")}</ul>
        <dl class="tally">
          <div><dt>${esc(t.tally[0])}</dt><dd>${counts.ok || 0}</dd></div>
          <div><dt>${esc(t.tally[1])}</dt><dd>${counts.warn || 0}</dd></div>
          <div><dt>${esc(t.tally[2])}</dt><dd>${counts.bad || 0}</dd></div>
        </dl>
      </aside>
    </div>
  </section>

  <section class="sec fixes-sec" aria-labelledby="fix-t">
    <div class="w">
      <div class="head">
        <h2 id="fix-t">${esc(t.fixesT)}</h2>
        <p>${esc(t.fixesS)}</p>
      </div>
      <ol class="fixes">
        ${a.fixes
          .map(
            (f, i) => `<li class="fix">
          <label>
            <input type="checkbox" data-fix="${i}">
            <span class="fix-box" aria-hidden="true"></span>
            <span class="fix-n" aria-hidden="true">${i + 1}</span>
            <span class="fix-text"><strong>${esc(f.title)}</strong> ${esc(f.body)}</span>
          </label>
        </li>`
          )
          .join("")}
      </ol>
      <p class="fix-done" id="fix-done" hidden>${esc(t.done)}</p>
      <div class="gift">
        <p>${hasKit ? esc(t.kitBand) : ""}</p>
        <div class="gift-btns">
          ${hasKit ? `<a class="btn btn--primary" href="kit/">${esc(t.kitOpen)}</a>` : ""}
          <button class="btn btn--ghost" type="button" data-print>${esc(t.pdf)}</button>
        </div>
      </div>
    </div>
  </section>

  <section class="sec" aria-labelledby="ch-t">
    <div class="w">
      <div class="head"><h2 id="ch-t">${esc(t.chT)}</h2><p>${esc(t.chS)}</p></div>
      <ul class="rows">${rows(a.channels, t)}</ul>
    </div>
  </section>

  <section class="sec sec--tint" aria-labelledby="hr-t">
    <div class="w">
      <div class="head"><h2 id="hr-t">${esc(t.hrT)}</h2><p>${esc(t.hrS)}</p></div>
      <ul class="rows">${rows(a.hours, t)}</ul>
    </div>
  </section>

  <section class="sec" aria-labelledby="rv-t">
    <div class="w">
      <div class="head"><h2 id="rv-t">${esc(t.rvT)}</h2><p>${esc(a.reviewsNote)}</p></div>
      <div class="quotes">
        ${a.quotes
          .map(
            (q) => `<figure class="quote quote--${esc(q.tone)}">
          <blockquote>“${esc(q.q)}”</blockquote>
          <figcaption><a href="${esc(q.url)}" target="_blank" rel="noopener">${esc(q.who)}</a></figcaption>
        </figure>`
          )
          .join("")}
      </div>
    </div>
  </section>

  <section class="sec sec--tint no-print" aria-labelledby="calc-t">
    <div class="w calc-in">
      <div>
        <h2 id="calc-t">${esc(t.calcT)}</h2>
        <p class="lead">${esc(t.calcS)}</p>
        <p class="formula">${esc(a.calc.leads)} ${esc(t.calcX[0])} ${esc(a.calc.job)}</p>
      </div>
      <form class="calc" id="calc" novalidate data-unit="${esc(a.calc.unit)}" data-locale="${lang === "ro" ? "ro-RO" : "en-US"}">
        <label>${esc(cap(a.calc.leads))}<input inputmode="numeric" name="leads" placeholder="${esc(t.ex)} 10"></label>
        <label>${esc(t.rate)}<input inputmode="numeric" name="rate" placeholder="${esc(t.ex)} 20"></label>
        <label>${esc(cap(a.calc.job))}, ${esc(a.calc.unit)}<input inputmode="numeric" name="value" placeholder="${esc(t.ex)} 450"></label>
        <output id="calc-out" class="calc-out" aria-live="polite"><span>${esc(t.year)}</span><b>—</b></output>
      </form>
    </div>
  </section>

  <section class="sec" aria-labelledby="cv-t">
    <div class="w convo-in">
      <div class="phone" aria-label="${esc(a.convo.title)}">
        <div class="phone-top"><b>${esc(a.convo.channel)}</b><span>${esc(t.replies)}</span></div>
        <div class="phone-body">
          ${a.convo.turns.map(([w, x]) => `<p class="msg msg--${w === "c" ? "c" : "a"}">${esc(x)}</p>`).join("")}
        </div>
      </div>
      <div>
        <h2 id="cv-t">${esc(a.convo.title)}</h2>
        <p class="note">${esc(a.convo.note)}</p>
        <div class="build">
          <p class="build-k">${esc(t.build)}</p>
          <h3>${esc(a.build.name)}</h3>
          <p>${esc(a.build.what)}</p>
          <dl>
            <div><dt>${esc(t.timeline)}</dt><dd>${esc(a.build.timeline)}</dd></div>
            <div><dt>${esc(t.invest)}</dt><dd>${esc(starter.price)}. ${esc(starter.terms)}. ${esc(t.investTail)}</dd></div>
          </dl>
          <a class="btn btn--primary no-print" href="${esc(cal)}" target="_blank" rel="noopener">${esc(t.book)}</a>
          <p class="build-fine">${esc(t.fine)}</p>
        </div>
      </div>
    </div>
  </section>

  <section class="sec sec--line" aria-labelledby="m-t">
    <div class="w method">
      <div>
        <h2 id="m-t">${esc(t.howT)}</h2>
        <p>${esc(t.howP(a.date))}</p>
        <p class="sign">${esc(a.signer || "Darius Arvinte")}<span>${esc(a.signerRole || t.founder)} · <a href="mailto:${esc(a.signerEmail || "darius@nextwise.studio")}">${esc(a.signerEmail || "darius@nextwise.studio")}</a></span></p>
      </div>
      <div class="method-cols">
        <div><h3>${esc(t.read)}</h3><ul>${a.method.read.map((x) => `<li>${esc(x)}</li>`).join("")}</ul></div>
        <div><h3>${esc(t.notDone)}</h3><ul>${a.method.notDone.map((x) => `<li>${esc(x)}</li>`).join("")}</ul></div>
      </div>
    </div>
  </section>
</main>

<footer class="foot">
  <div class="w foot-in">
    <span>NEXTWISE SRL, CUI 52675540${lang === "ro" ? ", București" : ", Bucharest, Romania"}</span>
    <a href="/">nextwise.studio</a>
    <span>${esc(t.wrong)}</span>
  </div>
</footer>

<script>
(() => {
  const key = "nw-audit-${esc(a.slug)}";
  const boxes = [...document.querySelectorAll("[data-fix]")];
  const done = document.getElementById("fix-done");
  let saved = [];
  try { saved = JSON.parse(localStorage.getItem(key) || "[]"); } catch {}
  const sync = () => { done.hidden = !boxes.every((b) => b.checked); };
  boxes.forEach((b, i) => {
    b.checked = !!saved[i];
    b.addEventListener("change", () => {
      try { localStorage.setItem(key, JSON.stringify(boxes.map((x) => x.checked))); } catch {}
      sync();
    });
  });
  sync();
  document.querySelectorAll("[data-print]").forEach((b) => b.addEventListener("click", () => window.print()));
  const f = document.getElementById("calc");
  const out = document.querySelector("#calc-out b");
  const num = (v) => parseFloat(String(v).replace(/[^0-9.]/g, ""));
  f.addEventListener("input", () => {
    const l = num(f.leads.value), r = num(f.rate.value), v = num(f.value.value);
    if ([l, r, v].some((x) => !isFinite(x) || x <= 0)) { out.textContent = "—"; return; }
    const n = Math.round(l * 52 * (r / 100) * v).toLocaleString(f.dataset.locale);
    out.textContent = f.dataset.unit === "€" || f.dataset.unit === "lei" || f.dataset.unit === "AED" ? n + " " + f.dataset.unit : f.dataset.unit + n;
  });
})();
</script>`;
  return shell({ lang, title: `${t.top} ${a.company}`, desc: a.headline, V, body, draft, t });
}

export function renderKit(a, V, { draft = false } = {}) {
  const lang = a.lang === "ro" ? "ro" : "en";
  const t = L[lang];
  const k = a.kit;
  const T = t.kit;
  const card = (label, text, id) => `<div class="kcard"><div class="kcard-h"><b>${esc(label)}</b><button type="button" class="kcopy no-print" data-copy="${id}">${esc(T.copy)}</button></div><p id="${id}">${esc(text)}</p></div>`;
  let n = 0;
  const body = `<header class="top no-print">
  <div class="w top-in">
    <a class="mark" href="/" aria-label="NEXTWISE">NEXTWISE</a>
    <a class="top-back" href="../">${esc(T.back)}</a>
    <button class="btn btn--primary btn--sm" type="button" data-print>${esc(T.pdf)}</button>
  </div>
</header>
<main class="kit">
  <section class="sheet kit-cover">
    <p class="kit-label">${esc(T.label)}</p>
    <h1>${esc(k.title)}</h1>
    <p class="kit-for">${esc(T.for)} <strong>${esc(a.company)}</strong> · ${esc(a.date)}</p>
    <p class="kit-intro">${esc(T.intro)}</p>
    <ol class="kit-toc">
      <li>${esc(T.s1)}</li><li>${esc(T.s2)}</li><li>${esc(T.s3)}</li><li>${esc(T.s4)}</li><li>${esc(T.s5)}</li>
    </ol>
    <p class="kit-mark">NEXTWISE</p>
  </section>

  <section class="sheet">
    <h2><span>1</span>${esc(T.s1)}</h2><p class="ks">${esc(T.s1s)}</p>
    <div class="kgrid">${k.autoReplies.map((r) => card(`${r.channel} · ${r.when}`, r.text, `k${n++}`)).join("")}</div>
  </section>

  <section class="sheet">
    <h2><span>2</span>${esc(T.s2)}</h2><p class="ks">${esc(T.s2s)}</p>
    <div class="kgrid">${k.formLines.map((r) => card(r.where, r.text, `k${n++}`)).join("")}</div>
    <h2 class="mt"><span>3</span>${esc(T.s3)}</h2><p class="ks">${esc(T.s3s)}</p>
    ${card(k.voicemail.label, k.voicemail.text, `k${n++}`)}
  </section>

  <section class="sheet">
    <h2><span>4</span>${esc(T.s4)}</h2><p class="ks">${esc(T.s4s)}</p>
    <div class="kgrid">${k.reviewReplies.map((r) => card(r.to, r.text, `k${n++}`)).join("")}</div>
  </section>

  <section class="sheet">
    <h2><span>5</span>${esc(T.s5)}</h2><p class="ks">${esc(T.s5s)}</p>
    <table class="ktable">
      <thead><tr><th>${esc(T.where)}</th><th>${esc(T.fix)}</th><th>${esc(T.done)}</th></tr></thead>
      <tbody>${k.checklist.map((c) => `<tr><td>${c.url ? `<a href="${esc(c.url)}" target="_blank" rel="noopener">${esc(c.where)}</a>` : esc(c.where)}</td><td>${esc(c.item)}</td><td><span class="kbox"></span></td></tr>`).join("")}</tbody>
    </table>
    <p class="kit-license">${esc(T.license(a.company))}</p>
  </section>
</main>
<script>
document.querySelectorAll("[data-print]").forEach((b) => b.addEventListener("click", () => window.print()));
document.querySelectorAll("[data-copy]").forEach((b) => b.addEventListener("click", async () => {
  const txt = document.getElementById(b.dataset.copy).textContent;
  try { await navigator.clipboard.writeText(txt); b.textContent = ${JSON.stringify(T.copied)}; setTimeout(() => (b.textContent = ${JSON.stringify(T.copy)}), 1500); } catch {}
}));
</script>`;
  return shell({ lang, title: `${k.title} · ${a.company}`, desc: T.intro, V, body, draft, t });
}

// Basic checks so a malformed audit never renders half a page.
export function validateAudit(a) {
  const need = ["slug", "company", "market", "date", "headline", "intro", "summary", "channels", "hours", "quotes", "fixes", "calc", "convo", "build", "method"];
  const missing = need.filter((k) => a?.[k] == null);
  if (missing.length) return `missing: ${missing.join(", ")}`;
  if (!/^[a-z0-9-]+$/.test(a.slug)) return "bad slug";
  if (a.fixes.length !== 3) return "needs exactly 3 fixes";
  if (a.kit) {
    const kn = ["title", "autoReplies", "formLines", "voicemail", "reviewReplies", "checklist"].filter((k) => a.kit[k] == null);
    if (kn.length) return `kit missing: ${kn.join(", ")}`;
  }
  return "";
}
