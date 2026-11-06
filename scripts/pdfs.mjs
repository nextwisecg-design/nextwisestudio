// Renders audit + kit PDFs for every static audit. Needs Playwright and Chrome locally:
//   npm run build && npx serve dist -l 8765 (or python3 -m http.server 8765 -d dist) && npm run pdfs && npm run build
import { readdir, mkdir } from "node:fs/promises";
const { chromium } = await import(process.env.PLAYWRIGHT || "playwright");
const base = process.env.BASE || "http://localhost:8765";
await mkdir("src/audits/pdf", { recursive: true });
const b = await chromium.launch(process.env.CHROME ? { executablePath: process.env.CHROME } : {});
const p = await b.newPage();
for (const f of (await readdir("src/audits")).filter((x) => x.endsWith(".mjs"))) {
  const a = (await import("../src/audits/" + f)).default;
  for (const [path, kind] of [[`/audit/${a.slug}/`, "audit"], [`/audit/${a.slug}/kit/`, "kit"]]) {
    if (kind === "kit" && !a.kit) continue;
    await p.goto(base + path, { waitUntil: "networkidle" });
    await p.pdf({ path: `src/audits/pdf/${a.slug}-${kind}.pdf`, format: "A4", printBackground: true, preferCSSPageSize: true });
    console.log("pdf", a.slug, kind);
  }
}
await b.close();
