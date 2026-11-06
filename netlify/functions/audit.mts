import type { Config } from "@netlify/functions";
import { renderAudit, renderKit, validateAudit } from "../../src/audit-template.mjs";
import { V } from "../lib/version.mjs";

// Audits written by the research agents live in the Notion database "Audituri publice".
// The audit itself is a JSON code block inside the row's page (same schema as src/audits/*.mjs).
// A page goes public only when Status = "Aprobat". Before that, the link with ?k=<Cheie preview>
// shows it to the team with a "Draft" banner.
// Static audits in dist/audit/ win over this function (preferStatic).
const AUDITS_DB = Netlify.env.get("NOTION_AUDITS_DB") || "eac5c8c4bc5841fb9f5a8fff583e64c6";
const NOTION = "https://api.notion.com/v1";

const headers = () => ({
  authorization: `Bearer ${Netlify.env.get("NOTION_TOKEN")}`,
  "notion-version": "2022-06-28",
  "content-type": "application/json",
});

const text = (rt: any[] = []) => rt.map((t) => t.plain_text ?? "").join("");

async function findRow(slug: string) {
  const r = await fetch(`${NOTION}/databases/${AUDITS_DB}/query`, {
    method: "POST",
    headers: headers(),
    body: JSON.stringify({ filter: { property: "Slug", rich_text: { equals: slug } }, page_size: 1 }),
  });
  if (!r.ok) throw new Error(`notion query ${r.status}`);
  return (await r.json()).results?.[0];
}

async function readJson(pageId: string) {
  let cursor: string | undefined;
  do {
    const r = await fetch(`${NOTION}/blocks/${pageId}/children?page_size=100${cursor ? `&start_cursor=${cursor}` : ""}`, { headers: headers() });
    if (!r.ok) throw new Error(`notion blocks ${r.status}`);
    const j = await r.json();
    for (const b of j.results) {
      if (b.type !== "code") continue;
      const raw = text(b.code.rich_text).trim();
      if (!raw.startsWith("{")) continue;
      try { return JSON.parse(raw); } catch { /* not the audit block */ }
    }
    cursor = j.has_more ? j.next_cursor : undefined;
  } while (cursor);
  return null;
}

const page = (status: number, html: string, cache: string) =>
  new Response(html, {
    status,
    headers: {
      "content-type": "text/html; charset=utf-8",
      "x-robots-tag": "noindex, nofollow",
      "cache-control": "no-cache",
      "netlify-cdn-cache-control": cache,
      "netlify-vary": "query=k",
    },
  });

const notFound = () =>
  page(404, `<!doctype html><meta charset="utf-8"><meta name="robots" content="noindex"><title>Not found | NEXTWISE</title><link rel="stylesheet" href="/assets/audit.css?v=${V}"><main class="sec"><div class="w"><h1>This audit isn't available.</h1><p>It may not be published yet. <a href="/">nextwise.studio</a></p></div></main>`, "public, s-maxage=60");

export default async (req: Request, context: any) => {
  const url = new URL(req.url);
  if (!url.pathname.endsWith("/")) return Response.redirect(new URL(url.pathname + "/" + url.search, url), 301);
  const slug = String(context.params.slug || "");
  const kit = url.pathname.endsWith("/kit/");
  if (!/^[a-z0-9-]{3,80}$/.test(slug) || !AUDITS_DB || !Netlify.env.get("NOTION_TOKEN")) return notFound();

  try {
    const row = await findRow(slug);
    if (!row) return notFound();
    const props = row.properties || {};
    const status = props.Status?.select?.name || props.Status?.status?.name || "";
    const key = text(props["Cheie preview"]?.rich_text);
    const approved = status === "Aprobat";
    const preview = !approved && key.length >= 12 && url.searchParams.get("k") === key;
    if (!approved && !preview) return notFound();

    const a = await readJson(row.id);
    if (!a || a.slug !== slug || validateAudit(a)) return notFound();
    if (kit && !a.kit) return notFound();

    let html = kit ? renderKit(a, V, { draft: preview }) : renderAudit(a, V, { draft: preview });
    if (preview) {
      const q = `?k=${encodeURIComponent(key)}`;
      html = html.replace('href="kit/"', `href="kit/${q}"`).replace('href="../"', `href="../${q}"`);
    }
    // Approved pages are cached at the edge for 5 minutes, so edits in Notion show up quickly.
    return page(200, html, preview ? "no-store" : "public, s-maxage=300, stale-while-revalidate=86400");
  } catch (e) {
    console.error("audit", slug, e);
    return page(503, "<!doctype html><meta charset=utf-8><title>NEXTWISE</title><p>Temporarily unavailable. Please try again in a minute.</p>", "no-store");
  }
};

export const config: Config = {
  path: ["/audit/:slug", "/audit/:slug/", "/audit/:slug/kit", "/audit/:slug/kit/"],
  preferStatic: true,
};
