(() => {
  const NW = window.__NW;
  const $ = (s, el = document) => el.querySelector(s);
  const $$ = (s, el = document) => [...el.querySelectorAll(s)];
  const params = new URLSearchParams(location.search);
  const state = { lang: NW.lang, ui: NW.ui, diag: NW.diag, askError: NW.askError };

  const esc = (s) => String(s).replace(/[&<>"']/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]));
  const get = (o, p) => p.split(".").reduce((x, k) => (x == null ? x : x[k]), o);

  // Header: border on scroll, mobile menu
  const bar = $("#bar");
  const onScroll = () => bar.classList.toggle("is-scrolled", scrollY > 8);
  addEventListener("scroll", onScroll, { passive: true });
  onScroll();
  const menuBtn = $("#menu-btn");
  const nav = $("#nav");
  menuBtn?.addEventListener("click", () => {
    const open = nav.classList.toggle("is-open");
    menuBtn.setAttribute("aria-expanded", String(open));
  });
  $$("#nav a").forEach((a) => a.addEventListener("click", () => { nav.classList.remove("is-open"); menuBtn.setAttribute("aria-expanded", "false"); }));

  // Pickers: close on outside click and Escape
  const picks = $$(".pick");
  document.addEventListener("click", (e) => picks.forEach((p) => { if (!p.contains(e.target)) p.open = false; }));
  document.addEventListener("keydown", (e) => {
    if (e.key !== "Escape") return;
    picks.forEach((p) => { if (p.open) { p.open = false; $("summary", p).focus(); } });
  });

  // Choosing a market remembers it, so the home page stops redirecting by IP.
  $$("[data-market]").forEach((a) =>
    a.addEventListener("click", (e) => {
      document.cookie = `nw_market=${a.dataset.market}; path=/; max-age=31536000; samesite=lax`;
      const runtimeLang = params.get("lang");
      if (runtimeLang && !NW.prerendered.includes(runtimeLang)) {
        e.preventDefault();
        const url = new URL(a.href, location.origin);
        url.pathname = `/${a.dataset.market}/`;
        if (a.dataset.market === "ro") url.pathname = "/ro/en/";
        url.searchParams.set("lang", runtimeLang);
        location.href = url.toString();
      }
    })
  );

  // Systems: accessible tabs with arrow keys
  const tabs = $$(".sys-tab");
  const select = (i, focus) => {
    tabs.forEach((t, j) => {
      const on = i === j;
      t.setAttribute("aria-selected", String(on));
      t.tabIndex = on ? 0 : -1;
      $("#panel-" + j).hidden = !on;
    });
    if (focus) tabs[i].focus();
  };
  tabs.forEach((t, i) => {
    t.addEventListener("click", () => select(i));
    t.addEventListener("keydown", (e) => {
      const rtl = document.documentElement.dir === "rtl";
      const next = { ArrowDown: 1, ArrowRight: rtl ? -1 : 1, ArrowUp: -1, ArrowLeft: rtl ? 1 : -1 }[e.key];
      if (next) { e.preventDefault(); select((i + next + tabs.length) % tabs.length, true); }
      if (e.key === "Home") { e.preventDefault(); select(0, true); }
      if (e.key === "End") { e.preventDefault(); select(tabs.length - 1, true); }
    });
  });

  // Small Markdown renderer for streamed AI answers (headings, bullets, bold).
  function md(src, level = "h4") {
    const lines = esc(src).split("\n");
    let html = "", list = false;
    const inline = (s) => s.replace(/\*\*(.+?)\*\*/g, "<strong>$1</strong>");
    for (const raw of lines) {
      const l = raw.trim();
      if (/^[-*•] /.test(l)) { if (!list) { html += "<ul>"; list = true; } html += `<li>${inline(l.slice(2))}</li>`; continue; }
      if (list) { html += "</ul>"; list = false; }
      if (!l) continue;
      if (l.startsWith("### ")) html += `<h5>${inline(l.slice(4))}</h5>`;
      else if (l.startsWith("## ")) html += `<${level}>${inline(l.slice(3))}</${level}>`;
      else if (l.startsWith("# ")) html += `<${level}>${inline(l.slice(2))}</${level}>`;
      else html += `<p>${inline(l)}</p>`;
    }
    if (list) html += "</ul>";
    return html;
  }

  async function stream(url, body, onText) {
    const res = await fetch(url, { method: "POST", headers: { "content-type": "application/json" }, body: JSON.stringify(body) });
    if (!res.ok || !res.body) throw new Error("http " + res.status);
    const reader = res.body.getReader();
    const dec = new TextDecoder();
    let all = "";
    for (;;) {
      const { value, done } = await reader.read();
      if (done) break;
      all += dec.decode(value, { stream: true });
      onText(all);
    }
    if (!all.trim()) throw new Error("empty");
    return all;
  }

  // Live diagnosis
  const form = $("#diag-form");
  const input = $("#diag-input");
  const out = $("#diag-out");
  const outText = $("#diag-text");
  const outQ = $("#diag-q");
  const actions = $("#diag-actions");
  const btn = $("#diag-btn");
  $$(".chip").forEach((c) => c.addEventListener("click", () => { input.value = c.dataset.example; input.focus(); }));

  form?.addEventListener("submit", async (e) => {
    e.preventDefault();
    const text = input.value.trim();
    if (text.length < 15) {
      input.setAttribute("aria-invalid", "true");
      input.placeholder = state.diag.tooShort;
      input.value = text;
      input.focus();
      return;
    }
    input.removeAttribute("aria-invalid");
    btn.disabled = true;
    form.hidden = true;
    out.hidden = false;
    actions.hidden = true;
    outQ.textContent = text;
    outText.innerHTML = `<p class="thinking"><b></b>${esc(state.diag.running)}</p>`;
    try {
      const answer = await stream("/api/diagnose", { text, market: NW.market, lang: state.lang }, (t) => {
        outText.innerHTML = md(t);
        outText.lastElementChild?.classList.add("caret");
      });
      outText.innerHTML = md(answer);
      const book = $("#diag-book");
      const url = new URL(NW.cal);
      url.searchParams.set("notes", `Website diagnosis: ${text}`.slice(0, 480));
      book.href = url.toString();
      actions.hidden = false;
    } catch {
      outText.innerHTML = `<p class="diag-err">${esc(state.diag.error)}</p>`;
      actions.hidden = false;
    } finally {
      btn.disabled = false;
    }
  });
  $("#diag-again")?.addEventListener("click", () => {
    out.hidden = true;
    form.hidden = false;
    input.value = "";
    input.focus();
  });

  // Ask NEXTWISE AI
  const askForm = $("#ask-form");
  const askInput = $("#ask-input");
  const askLog = $("#ask-log");
  const askBtn = $("#ask-btn");
  askForm?.addEventListener("submit", async (e) => {
    e.preventDefault();
    const q = askInput.value.trim();
    if (q.length < 3) { askInput.focus(); return; }
    askInput.value = "";
    askBtn.disabled = true;
    const item = document.createElement("div");
    item.innerHTML = `<p class="ask-q">${esc(q)}</p><div class="ask-a"><p class="thinking"><b></b></p></div>`;
    askLog.prepend(item);
    const a = $(".ask-a", item);
    try {
      const answer = await stream("/api/ask", { q, market: NW.market, lang: state.lang }, (t) => { a.innerHTML = md(t, "p"); });
      a.innerHTML = md(answer, "p");
    } catch {
      a.innerHTML = `<p class="diag-err">${esc(state.askError)}</p>`;
    } finally {
      askBtn.disabled = false;
    }
  });

  // Live translation for languages we don't prerender
  const toast = $("#toast");
  function showToast(html, spin) {
    toast.innerHTML = (spin ? '<span class="dot" aria-hidden="true"></span>' : "") + html;
    toast.hidden = false;
  }

  const originals = new Map();
  function apply(section, dict) {
    $$(`[data-i^="${section}."]`).forEach((el) => {
      if (!originals.has(el)) originals.set(el, el.textContent);
      const v = get({ [section]: dict }, el.dataset.i);
      if (typeof v === "string") el.textContent = v;
    });
    $$(`[data-i-ph^="${section}."]`).forEach((el) => {
      if (!originals.has(el)) originals.set(el, { ph: el.placeholder });
      const v = get({ [section]: dict }, el.dataset.iPh);
      if (typeof v === "string") el.placeholder = v;
    });
    if (section === "meta" && dict.title) document.title = dict.title;
    if (section === "ui") state.ui = { ...state.ui, ...dict };
    if (section === "diag") state.diag = { ...state.diag, ...dict };
    if (section === "faq" && dict.askError) state.askError = dict.askError;
  }

  async function translate(lang) {
    const L = NW.langs[lang];
    if (!L) return;
    state.lang = lang;
    document.documentElement.lang = lang;
    if (L.rtl) document.documentElement.dir = "rtl";
    $("#lang-cur").textContent = lang.toUpperCase();
    $$("#pick-lang a").forEach((a) => a.toggleAttribute("aria-current", a.dataset.lang === lang));
    showToast(esc(NW.ui.translating) + "…", true);
    const sections = ["meta", "nav", "hero", "stats", "diag", "work", "systems", "how", "why", "market", "pricing", "faq", "contact", "footer", "ui"].filter(
      (s) => document.querySelector(`[data-i^="${s}."], [data-i-ph^="${s}."]`) || ["ui", "diag", "meta"].includes(s)
    );
    let ok = 0;
    await Promise.all(
      sections.map(async (s) => {
        const key = `nw:${lang}:${NW.market}:${s}`;
        try {
          let dict = JSON.parse(sessionStorage.getItem(key) || "null");
          if (!dict) {
            const r = await fetch(`/api/translate?m=${NW.market}&l=${lang}&s=${s}`);
            if (!r.ok) throw new Error();
            dict = await r.json();
            try { sessionStorage.setItem(key, JSON.stringify(dict)); } catch {}
          }
          apply(s, dict);
          ok++;
        } catch {}
      })
    );
    if (ok === sections.length) {
      showToast(`${esc(state.ui.translated)} <button type="button" id="orig">${esc(state.ui.showOriginal)}</button>`);
    } else {
      // Undo a partial translation so the page is never half in one language.
      originals.forEach((v, el) => { if (typeof v === "string") el.textContent = v; else el.placeholder = v.ph; });
      document.documentElement.lang = NW.lang;
      document.documentElement.dir = "ltr";
      $("#lang-cur").textContent = NW.lang.toUpperCase();
      state.lang = NW.lang;
      state.ui = NW.ui; state.diag = NW.diag; state.askError = NW.askError;
      showToast(`${esc(state.ui.translateError)} <button type="button" id="orig">${esc(state.ui.close)}</button>`);
    }
    $("#orig")?.addEventListener("click", () => {
      if (ok === sections.length) { const u = new URL(location.href); u.searchParams.delete("lang"); location.href = u.toString(); }
      else toast.hidden = true;
    });
  }

  const want = params.get("lang");
  if (want && !NW.prerendered.includes(want) && NW.langs[want]) translate(want);
})();
