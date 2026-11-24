import { MARKETS, MARKET_ORDER, LANGS, PRERENDERED, EXAMPLES, EMAIL } from "./content/index.mjs";

const esc = (s) =>
  String(s ?? "").replace(/[&<>"']/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]));

const get = (obj, path) => path.split(".").reduce((o, k) => (o == null ? o : o[k]), obj);

export const SITE = "https://nextwise.studio";

// URL of a market page in a prerendered language.
export function pageUrl(market, lang) {
  const m = MARKETS[market];
  return lang === m.defaultLang ? `/${market}/` : `/${market}/${lang}/`;
}

export function render({ market, lang, d, isRoot = false }) {
  const M = MARKETS[market];
  // Text helper: element tagged with its copy key so live translation can swap it.
  const T = (tag, key, attrs = "") => `<${tag} data-i="${key}"${attrs ? " " + attrs : ""}>${esc(get(d, key))}</${tag}>`;
  const t = (key) => esc(get(d, key));

  const self = pageUrl(market, lang);
  const canonical = SITE + self;
  const noindex = market !== "ro" && lang !== M.defaultLang; // e.g. /us/ro/ is for showing, not for search
  const examples = EXAMPLES[market][lang] || EXAMPLES[market].en;
  const hasMarketSection = Boolean(d.market);
  const cal = M.cal;

  const hreflang = [
    ["x-default", "/global/"],
    ["en", "/global/"],
    ["en-US", "/us/"],
    ["en-AE", "/uae/"],
    ["ro", "/ro/"],
    ["en-RO", "/ro/en/"],
  ]
    .map(([h, u]) => `<link rel="alternate" hreflang="${h}" href="${SITE}${u}">`)
    .join("\n    ");

  const marketMenu = MARKET_ORDER.map((code) => {
    const mm = MARKETS[code];
    const href = pageUrl(code, PRERENDERED.includes(lang) ? lang : mm.defaultLang);
    const cur = code === market ? ' aria-current="page"' : "";
    return `<li><a href="${href}" data-market="${code}"${cur}><span class="flag" aria-hidden="true">${mm.flag}</span>${esc(mm.name[lang] || mm.name.en)}</a></li>`;
  }).join("");

  const langMenu = Object.entries(LANGS)
    .map(([code, L]) => {
      const href = PRERENDERED.includes(code) ? pageUrl(market, code) : `${pageUrl(market, "en")}?lang=${code}`;
      const cur = code === lang ? ' aria-current="true"' : "";
      return `<li><a href="${href}" hreflang="${code}" lang="${code}" data-lang="${code}"${cur}>${esc(L.label)}</a></li>`;
    })
    .join("");

  const stats = [1, 2, 3]
    .map((n) => `<div class="stat"><dt data-i="stats.s${n}l">${t(`stats.s${n}l`)}</dt><dd data-i="stats.s${n}v">${t(`stats.s${n}v`)}</dd></div>`)
    .join("");

  const chips = examples
    .map((e, i) => `<button type="button" class="chip" data-example="${esc(e)}">${esc(e)}</button>`)
    .join("");

  const work = d.work.items
    .map((it, i) => {
      const live = i === 0;
      const facts = it.facts.map((f, j) => `<li data-i="work.items.${i}.facts.${j}">${esc(f)}</li>`).join("");
      return `<article class="case ${live ? "case--lead" : ""}">
          <header class="case-head">
            <h3 class="case-name">${esc(it.name)}</h3>
            <span class="status ${live ? "status--live" : "status--build"}" data-i="work.${live ? "live" : "building"}">${t(`work.${live ? "live" : "building"}`)}</span>
          </header>
          <p class="case-sector" data-i="work.items.${i}.sector">${esc(it.sector)}</p>
          <p class="case-title" data-i="work.items.${i}.title">${esc(it.title)}</p>
          <p class="case-body" data-i="work.items.${i}.body">${esc(it.body)}</p>
          ${it.quote ? `<blockquote class="case-quote" data-i="work.items.${i}.quote">${esc(it.quote)}</blockquote>` : ""}
          <ul class="case-facts">${facts}</ul>
        </article>`;
    })
    .join("");

  const sysTabs = d.systems.items
    .map(
      (s, i) =>
        `<button type="button" role="tab" id="tab-${i}" aria-controls="panel-${i}" aria-selected="${i === 0}" tabindex="${i === 0 ? 0 : -1}" class="sys-tab"><span class="sys-n">${i + 1}</span><span data-i="systems.items.${i}.name">${esc(s.name)}</span></button>`
    )
    .join("");

  const sysPanels = d.systems.items
    .map((s, i) => {
      const flow = s.flow
        .map((f, j) => `<li class="node" style="--i:${j}"><span data-i="systems.items.${i}.flow.${j}">${esc(f)}</span></li>`)
        .join("");
      return `<div role="tabpanel" id="panel-${i}" aria-labelledby="tab-${i}" class="sys-panel" ${i === 0 ? "" : "hidden"}>
          <h3 class="sys-name" data-i="systems.items.${i}.name">${esc(s.name)}</h3>
          <p class="sys-desc" data-i="systems.items.${i}.desc">${esc(s.desc)}</p>
          <p class="flow-label" data-i="systems.flowLabel">${t("systems.flowLabel")}</p>
          <ol class="flow" style="--n:${s.flow.length}">${flow}</ol>
        </div>`;
    })
    .join("");

  const steps = d.how.steps
    .map(
      (s, i) => `<li class="step">
          <span class="step-n" aria-hidden="true">${i + 1}</span>
          <p class="step-when" data-i="how.steps.${i}.when">${esc(s.when)}</p>
          <h3 class="step-title" data-i="how.steps.${i}.title">${esc(s.title)}</h3>
          <p class="step-body" data-i="how.steps.${i}.body">${esc(s.body)}</p>
        </li>`
    )
    .join("");

  const why = d.why.items
    .map(
      (w, i) => `<div class="why-item"><h3 data-i="why.items.${i}.title">${esc(w.title)}</h3><p data-i="why.items.${i}.body">${esc(w.body)}</p></div>`
    )
    .join("");

  const marketPoints = hasMarketSection
    ? d.market.points.map((p, i) => `<li data-i="market.points.${i}">${esc(p)}</li>`).join("")
    : "";

  const tiers = d.pricing.tiers
    .map((tr, i) => {
      const pop = i === 1;
      const feats = tr.features.map((f, j) => `<li data-i="pricing.tiers.${i}.features.${j}">${esc(f)}</li>`).join("");
      return `<article class="tier ${pop ? "tier--pop" : ""}">
          ${pop ? `<p class="tier-pop" data-i="pricing.popular">${t("pricing.popular")}</p>` : ""}
          <h3 class="tier-name" data-i="pricing.tiers.${i}.name">${esc(tr.name)}</h3>
          <p class="tier-sub" data-i="pricing.tiers.${i}.sub">${esc(tr.sub)}</p>
          <p class="tier-price" data-i="pricing.tiers.${i}.price">${esc(tr.price)}</p>
          <p class="tier-terms" data-i="pricing.tiers.${i}.terms">${esc(tr.terms)}</p>
          <ul class="tier-feats">${feats}</ul>
          <a class="btn ${pop ? "btn--primary" : "btn--ghost"}" href="${cal}" target="_blank" rel="noopener" data-i="pricing.tiers.${i}.cta">${esc(tr.cta)}</a>
        </article>`;
    })
    .join("");

  const faqs = d.faq.items
    .map(
      (f, i) => `<details class="qa"${i === 0 ? " open" : ""}><summary data-i="faq.items.${i}.q">${esc(f.q)}</summary><p data-i="faq.items.${i}.a">${esc(f.a)}</p></details>`
    )
    .join("");

  const footMarkets = MARKET_ORDER.map((code) => {
    const mm = MARKETS[code];
    return `<li><a href="${pageUrl(code, mm.defaultLang)}" data-market="${code}">${esc(mm.name[lang] || mm.name.en)}</a></li>`;
  }).join("");

  const footLangs = Object.entries(LANGS)
    .map(([code, L]) => {
      const href = PRERENDERED.includes(code) ? pageUrl(market, code) : `${pageUrl(market, "en")}?lang=${code}`;
      return `<li><a href="${href}" lang="${code}" title="${esc(L.label)}">${code.toUpperCase()}</a></li>`;
    })
    .join("");

  const boot = {
    market,
    lang,
    defaultLang: M.defaultLang,
    cal,
    email: EMAIL,
    prerendered: PRERENDERED,
    langs: Object.fromEntries(Object.entries(LANGS).map(([k, v]) => [k, { rtl: !!v.rtl }])),
    ui: d.ui,
    diag: { running: d.diag.running, error: d.diag.error, tooShort: d.diag.tooShort },
    askError: d.faq.askError,
  };

  return `<!doctype html>
<html lang="${lang}" dir="ltr" data-market="${market}">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title data-i="meta.title">${t("meta.title")}</title>
    <meta name="description" content="${t("meta.description")}">
    ${noindex ? '<meta name="robots" content="noindex, follow">' : ""}
    <link rel="canonical" href="${isRoot ? SITE + "/global/" : canonical}">
    ${hreflang}
    <meta property="og:type" content="website">
    <meta property="og:title" content="${t("hero.title")}">
    <meta property="og:description" content="${t("meta.description")}">
    <meta property="og:url" content="${canonical}">
    <meta property="og:image" content="${SITE}/og.png">
    <meta name="twitter:card" content="summary_large_image">
    <meta name="theme-color" content="#0E0E1B">
    <link rel="icon" href="/favicon.ico">
    <link rel="preload" href="/fonts/commissioner-latin-flar-normal.woff2" as="font" type="font/woff2" crossorigin>
    <link rel="stylesheet" href="/fonts/fonts.css">
    <link rel="stylesheet" href="/assets/site.css?v=__V__">
    <script type="application/ld+json">${JSON.stringify({
      "@context": "https://schema.org",
      "@type": "Organization",
      name: "NEXTWISE",
      legalName: "NEXTWISE SRL",
      url: SITE,
      email: EMAIL,
      address: { "@type": "PostalAddress", addressLocality: "Bucharest", addressCountry: "RO" },
      description: get(d, "meta.description"),
    })}</script>
  </head>
  <body>
    <a class="skip" href="#main" data-i="nav.skip">${t("nav.skip")}</a>

    <header class="bar" id="bar">
      <div class="wrap bar-in">
        <a class="mark" href="${self}" aria-label="NEXTWISE">NEXTWISE</a>
        <nav class="nav" id="nav" aria-label="Main">
          <a href="#systems" data-i="nav.systems">${t("nav.systems")}</a>
          <a href="#work" data-i="nav.work">${t("nav.work")}</a>
          <a href="#pricing" data-i="nav.pricing">${t("nav.pricing")}</a>
          <a href="#faq" data-i="nav.faq">${t("nav.faq")}</a>
        </nav>
        <div class="bar-tools">
          <details class="pick" id="pick-market">
            <summary aria-label="${t("nav.market")}"><span class="flag" aria-hidden="true">${M.flag}</span><span class="pick-cur">${esc(M.name[lang] || M.name.en)}</span></summary>
            <div class="pick-pop"><p class="pick-label" data-i="nav.market">${t("nav.market")}</p><ul>${marketMenu}</ul></div>
          </details>
          <details class="pick" id="pick-lang">
            <summary aria-label="${t("nav.language")}"><span class="pick-cur" id="lang-cur">${lang.toUpperCase()}</span></summary>
            <div class="pick-pop pick-pop--langs"><p class="pick-label" data-i="nav.language">${t("nav.language")}</p><ul>${langMenu}</ul></div>
          </details>
          <a class="btn btn--primary btn--sm bar-cta" href="${cal}" target="_blank" rel="noopener" data-i="nav.book">${t("nav.book")}</a>
          <button class="menu-btn" type="button" aria-expanded="false" aria-controls="nav" id="menu-btn"><span class="sr" data-i="nav.menu">${t("nav.menu")}</span><span class="burger" aria-hidden="true"></span></button>
        </div>
      </div>
    </header>

    <main id="main">
      <section class="hero" id="top">
        <div class="wrap hero-in">
          <div class="hero-copy">
            <h1 class="hero-title" data-i="hero.title">${t("hero.title")}</h1>
            <p class="hero-sub" data-i="hero.sub">${t("hero.sub")}</p>
            <div class="hero-ctas">
              <a class="btn btn--primary" href="${cal}" target="_blank" rel="noopener" data-i="hero.cta">${t("hero.cta")}</a>
              <a class="btn btn--ghost" href="#diagnose" data-i="hero.cta2">${t("hero.cta2")}</a>
            </div>
            <dl class="stats">${stats}</dl>
          </div>

          <div class="console" id="diagnose" aria-labelledby="diag-title">
            <div class="console-bar" aria-hidden="true"><i></i><i></i><i></i><span>nextwise / diagnose</span></div>
            <div class="console-body">
              <h2 class="console-title" id="diag-title" data-i="diag.title">${t("diag.title")}</h2>
              <p class="console-sub" data-i="diag.sub">${t("diag.sub")}</p>
              <form class="diag-form" id="diag-form" novalidate>
                <label class="sr" for="diag-input" data-i="diag.label">${t("diag.label")}</label>
                <textarea id="diag-input" name="text" rows="3" maxlength="800" placeholder="${t("diag.placeholder")}" data-i-ph="diag.placeholder"></textarea>
                <p class="chips-label" data-i="diag.examples">${t("diag.examples")}</p>
                <div class="chips">${chips}</div>
                <button class="btn btn--primary btn--block" type="submit" id="diag-btn" data-i="diag.button">${t("diag.button")}</button>
                <p class="console-note" data-i="diag.note">${t("diag.note")}</p>
              </form>
              <div class="diag-out" id="diag-out" aria-live="polite" hidden>
                <p class="diag-q" id="diag-q"></p>
                <div class="diag-text" id="diag-text"></div>
                <div class="diag-actions" id="diag-actions" hidden>
                  <a class="btn btn--amber" id="diag-book" href="${cal}" target="_blank" rel="noopener" data-i="diag.cta">${t("diag.cta")}</a>
                  <button class="btn btn--quiet" type="button" id="diag-again" data-i="diag.again">${t("diag.again")}</button>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>

      <section class="sec" id="work" aria-labelledby="work-title">
        <div class="wrap">
          <div class="sec-head">
            <h2 id="work-title" data-i="work.title">${t("work.title")}</h2>
            <p data-i="work.sub">${t("work.sub")}</p>
          </div>
          <div class="cases">${work}
            <aside class="case case--more">
              <p class="case-title" data-i="work.moreTitle">${t("work.moreTitle")}</p>
              <p class="case-body" data-i="work.moreBody">${t("work.moreBody")}</p>
            </aside>
          </div>
        </div>
      </section>

      <section class="sec sec--tint" id="systems" aria-labelledby="sys-title">
        <div class="wrap">
          <div class="sec-head">
            <h2 id="sys-title" data-i="systems.title">${t("systems.title")}</h2>
            <p data-i="systems.sub">${t("systems.sub")}</p>
          </div>
          <div class="sys">
            <div class="sys-tabs" role="tablist" aria-labelledby="sys-title">${sysTabs}</div>
            <div class="sys-panels">${sysPanels}</div>
          </div>
        </div>
      </section>

      <section class="sec" id="how" aria-labelledby="how-title">
        <div class="wrap">
          <div class="sec-head"><h2 id="how-title" data-i="how.title">${t("how.title")}</h2></div>
          <ol class="steps">${steps}</ol>
        </div>
      </section>

      <section class="sec sec--line" aria-labelledby="why-title">
        <div class="wrap why">
          <h2 id="why-title" data-i="why.title">${t("why.title")}</h2>
          <div class="why-list">${why}</div>
        </div>
      </section>

      ${
        hasMarketSection
          ? `<section class="sec mkt" id="for-you" aria-labelledby="mkt-title">
        <div class="wrap mkt-in">
          <div>
            <h2 id="mkt-title" data-i="market.title">${t("market.title")}</h2>
            <p data-i="market.body">${t("market.body")}</p>
            <a class="btn btn--primary" href="${cal}" target="_blank" rel="noopener" data-i="market.cta">${t("market.cta")}</a>
          </div>
          <ul class="mkt-points">${marketPoints}</ul>
        </div>
      </section>`
          : ""
      }

      <section class="sec" id="pricing" aria-labelledby="price-title">
        <div class="wrap">
          <div class="sec-head">
            <h2 id="price-title" data-i="pricing.title">${t("pricing.title")}</h2>
            <p data-i="pricing.sub">${t("pricing.sub")}</p>
          </div>
          <div class="tiers">${tiers}</div>
          <p class="fine" data-i="pricing.note">${t("pricing.note")}</p>
        </div>
      </section>

      <section class="sec sec--tint" id="faq" aria-labelledby="faq-title">
        <div class="wrap faq">
          <div>
            <h2 id="faq-title" data-i="faq.title">${t("faq.title")}</h2>
            <div class="qas">${faqs}</div>
          </div>
          <aside class="ask" aria-labelledby="ask-title">
            <h3 id="ask-title" data-i="faq.askTitle">${t("faq.askTitle")}</h3>
            <p class="ask-sub" data-i="faq.askSub">${t("faq.askSub")}</p>
            <form id="ask-form" class="ask-form" novalidate>
              <label class="sr" for="ask-input" data-i="faq.askLabel">${t("faq.askLabel")}</label>
              <input id="ask-input" name="q" maxlength="400" autocomplete="off" placeholder="${t("faq.askPlaceholder")}" data-i-ph="faq.askPlaceholder">
              <button class="btn btn--primary" type="submit" id="ask-btn" data-i="faq.askButton">${t("faq.askButton")}</button>
            </form>
            <div class="ask-log" id="ask-log" aria-live="polite"></div>
          </aside>
        </div>
      </section>

      <section class="cta-band" id="contact" aria-labelledby="cta-title">
        <div class="wrap cta-in">
          <h2 id="cta-title" data-i="contact.title">${t("contact.title")}</h2>
          <p data-i="contact.sub">${t("contact.sub")}</p>
          <a class="btn btn--amber btn--lg" href="${cal}" target="_blank" rel="noopener" data-i="contact.cta">${t("contact.cta")}</a>
          <p class="cta-note"><span data-i="contact.note">${t("contact.note")}</span> <span data-i="contact.email">${t("contact.email")}</span> <a href="mailto:${EMAIL}">${EMAIL}</a></p>
        </div>
      </section>
    </main>

    <footer class="foot">
      <div class="wrap foot-in">
        <div class="foot-brand">
          <p class="mark mark--light">NEXTWISE</p>
          <p data-i="footer.tagline">${t("footer.tagline")}</p>
        </div>
        <nav aria-labelledby="fm"><p class="foot-h" id="fm" data-i="footer.markets">${t("footer.markets")}</p><ul>${footMarkets}</ul></nav>
        <nav aria-labelledby="fl"><p class="foot-h" id="fl" data-i="footer.languages">${t("footer.languages")}</p><ul class="foot-langs">${footLangs}</ul></nav>
      </div>
      <div class="wrap foot-legal">
        <p data-i="footer.rights">${t("footer.rights")}</p>
        <p data-i="footer.company">${t("footer.company")}</p>
        <p><a href="mailto:${EMAIL}">${EMAIL}</a></p>
      </div>
    </footer>

    <div class="toast" id="toast" role="status" hidden></div>
    <script>window.__NW=${JSON.stringify(boot)}</script>
    <script src="/assets/app.js?v=__V__" defer></script>
  </body>
</html>`;
}
