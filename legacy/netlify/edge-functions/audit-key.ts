import type { Config } from "@netlify/edge-functions";

// Preview links look like /audit/<slug>/?k=<key>. The query string doesn't reach the audit
// function in production, so the key moves into the path: /audit/<slug>/p/<key>/ (and .../kit/).
export default async (req: Request) => {
  const url = new URL(req.url);
  const k = url.searchParams.get("k") || "";
  const m = url.pathname.match(/^\/audit\/([a-z0-9-]{3,80})\/(kit\/?)?$/);
  if (!m || !/^[a-z0-9]{12,64}$/.test(k)) return;
  const to = new URL(`/audit/${m[1]}/p/${k}/${m[2] ? "kit/" : ""}`, url);
  return new Response(null, { status: 302, headers: { location: to.pathname, "cache-control": "private, no-store", "x-robots-tag": "noindex, nofollow" } });
};

export const config: Config = { path: "/audit/*", onError: "bypass" };
