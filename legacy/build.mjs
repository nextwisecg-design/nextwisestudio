import { existsSync } from "node:fs";
// Static build: one HTML page per market and prerendered language.
import { mkdir, writeFile, readFile, copyFile, readdir, rm } from "node:fs/promises";
import { join, dirname } from "node:path";
import { createHash } from "node:crypto";
import { MARKETS, MARKET_ORDER, PRERENDERED, getDict } from "./src/content/index.mjs";
import { render, pageUrl, SITE } from "./src/template.mjs";
import { renderAudit, renderKit, validateAudit } from "./src/audit-template.mjs";

const OUT = "dist";
await rm(OUT, { recursive: true, force: true });
await mkdir(join(OUT, "assets"), { recursive: true });
await mkdir(join(OUT, "fonts"), { recursive: true });

// Assets, versioned by content hash
const css = await readFile("src/site.css", "utf8");
const js = await readFile("src/client/app.js", "utf8");
const auditCss = await readFile("src/audit.css", "utf8");
const V = createHash("sha1").update(css + js + auditCss).digest("hex").slice(0, 10);
await writeFile(join(OUT, "assets/site.css"), css);
await writeFile(join(OUT, "assets/app.js"), js);
await writeFile(join(OUT, "assets/audit.css"), auditCss);

// Self-hosted fonts (no third-party font requests, GDPR-friendly)
const fontSets = [
  ["node_modules/@fontsource-variable/commissioner", ["flar.css"]],
  ["node_modules/@fontsource/ibm-plex-mono", ["400.css", "500.css"]],
  ["node_modules/@fontsource/ibm-plex-sans-arabic", ["400.css", "600.css"]],
];
let fontCss = "";
for (const [dir, files] of fontSets) {
  for (const f of files) {
    const src = await readFile(join(dir, f), "utf8");
    // keep only scripts we use
    const blocks = src.split("/*").filter((b) => b.trim());
    for (const b of blocks) {
      if (/vietnamese/.test(b)) continue;
      fontCss += "/*" + b.replace(/url\(\.\/files\/([^)]+)\)/g, "url(/fonts/$1)");
    }
  }
  for (const file of await readdir(join(dir, "files"))) {
    if (!file.endsWith(".woff2")) continue;
    if (/vietnamese/.test(file)) continue;
    if (dir.includes("commissioner") && !file.includes("-flar-")) continue;
    if (dir.includes("plex-mono") && !/-(400|500)-normal/.test(file)) continue;
    if (dir.includes("arabic") && !/-(400|600)-normal/.test(file)) continue;
    await copyFile(join(dir, "files", file), join(OUT, "fonts", file));
  }
}
// woff fallbacks are not shipped; drop their url() entries
fontCss = fontCss.replace(/,\s*url\(\/fonts\/[^)]+\.woff\) format\('woff'\)/g, "");
await writeFile(join(OUT, "fonts/fonts.css"), fontCss);

// Pages
const urls = [];
for (const market of MARKET_ORDER) {
  for (const lang of PRERENDERED) {
    const d = getDict(market, lang);
    const html = render({ market, lang, d }).replaceAll("__V__", V);
    const path = pageUrl(market, lang);
    await mkdir(join(OUT, path), { recursive: true });
    await writeFile(join(OUT, path, "index.html"), html);
    const indexable = market === "ro" || lang === MARKETS[market].defaultLang;
    if (indexable) urls.push(path);
  }
}
// "/" serves the global page to search engines and to anyone the edge function skips
await writeFile(join(OUT, "index.html"), render({ market: "global", lang: "en", d: getDict("global", "en"), isRoot: true }).replaceAll("__V__", V));

// Free audits: one private page per prospect, never indexed
let audits = 0;
for (const f of (await readdir("src/audits")).filter((x) => x.endsWith(".mjs"))) {
  const a = (await import("./src/audits/" + f)).default;
  await mkdir(join(OUT, "audit", a.slug), { recursive: true });
  const bad = validateAudit(a);
  if (bad) throw new Error(`Audit ${f}: ${bad}`);
  await writeFile(join(OUT, "audit", a.slug, "index.html"), renderAudit(a, V));
  if (a.kit) {
    await mkdir(join(OUT, "audit", a.slug, "kit"), { recursive: true });
    await writeFile(join(OUT, "audit", a.slug, "kit", "index.html"), renderKit(a, V));
  }
  // Pre-rendered PDFs (made with `npm run pdfs`), served next to the page
  for (const kind of ["audit", "kit"]) {
    const pdf = join("src/audits/pdf", `${a.slug}-${kind}.pdf`);
    if (existsSync(pdf)) await copyFile(pdf, join(OUT, "audit", a.slug, `${kind}.pdf`));
  }
  audits++;
}
// The live audit function needs the same asset version as the static pages
await writeFile("netlify/lib/version.mjs", `export const V = ${JSON.stringify(V)};\n`);

// 404
const nf = render({ market: "global", lang: "en", d: getDict("global", "en") }).replaceAll("__V__", V);
await writeFile(join(OUT, "404.html"), nf.replace("<head>", '<head>\n    <meta name="robots" content="noindex">'));

// Public files
for (const f of await readdir("public")) await copyFile(join("public", f), join(OUT, f));
await writeFile(
  join(OUT, "sitemap.xml"),
  `<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n${urls
    .map((u) => `  <url><loc>${SITE}${u}</loc></url>`)
    .join("\n")}\n</urlset>\n`
);
await writeFile(join(OUT, "robots.txt"), `User-agent: *\nAllow: /\nDisallow: /api/\nDisallow: /audit/\n\nSitemap: ${SITE}/sitemap.xml\n`);

console.log(`Built ${urls.length + 4} pages and ${audits} audits, assets v${V}`);
