import type { Config, Context } from "@netlify/edge-functions";

// Sends visitors of the home page to their market's version.
// A market chosen in the site's picker (cookie) always wins over the IP.
// Search engines and link previews are never redirected: they get /global content at "/".
const BOTS = /bot|crawler|spider|crawling|slurp|bingpreview|facebookexternalhit|linkedinbot|whatsapp|telegram|twitterbot|embedly|preview|lighthouse/i;
const MARKETS = ["global", "us", "uae", "ro"];
const GULF = ["AE", "SA", "QA", "KW", "BH", "OM"];

export default async (req: Request, context: Context) => {
  const ua = req.headers.get("user-agent") || "";
  if (BOTS.test(ua)) return;

  const chosen = context.cookies.get("nw_market");
  let market = chosen && MARKETS.includes(chosen) ? chosen : "";
  if (!market) {
    const cc = context.geo?.country?.code || "";
    market = cc === "US" ? "us" : GULF.includes(cc) ? "uae" : cc === "RO" || cc === "MD" ? "ro" : "global";
  }
  const to = new URL(`/${market}/`, req.url);
  to.search = new URL(req.url).search;
  return new Response(null, {
    status: 302,
    headers: { location: to.toString(), "cache-control": "private, no-store", vary: "cookie" },
  });
};

export const config: Config = { path: "/", onError: "bypass" };
