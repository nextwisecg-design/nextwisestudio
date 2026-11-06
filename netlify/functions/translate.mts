import Anthropic from "@anthropic-ai/sdk";
import { getStore } from "@netlify/blobs";
import type { Config } from "@netlify/functions";
import { getDict, SECTIONS, CONTENT_VERSION, PRERENDERED } from "../../src/content/index.mjs";
import { MODEL_FAST, langName, validMarket, aiReady, jsonError } from "../lib/knowledge.mts";
import { LANGS } from "../../src/content/index.mjs";

// Same keys and nesting as the English source, strings only.
function sameShape(a: any, b: any): boolean {
  if (typeof a === "string") return typeof b === "string";
  if (Array.isArray(a)) return Array.isArray(b) && a.length === b.length && a.every((x, i) => sameShape(x, b[i]));
  if (a && typeof a === "object") return b && typeof b === "object" && Object.keys(a).every((k) => sameShape(a[k], b[k]));
  return true;
}

const CACHED = {
  "content-type": "application/json; charset=utf-8",
  "cache-control": "public, max-age=3600",
  "netlify-cdn-cache-control": "public, s-maxage=31536000, durable",
};

// Translates one section of a market page into a language we don't prerender,
// once, then serves it from Blobs and the CDN.
export default async (req: Request) => {
  const url = new URL(req.url);
  const market = validMarket(url.searchParams.get("m"));
  const lang = url.searchParams.get("l") || "";
  const section = url.searchParams.get("s") || "";
  if (!(lang in LANGS) || PRERENDERED.includes(lang)) return jsonError(400, "bad_lang");
  if (!SECTIONS.includes(section)) return jsonError(400, "bad_section");

  const source = (getDict(market, "en") as any)[section];
  if (!source) return Response.json({}, { headers: CACHED });

  const store = getStore("i18n");
  const key = `${CONTENT_VERSION}/${market}/${lang}/${section}`;
  const hit = await store.get(key, { type: "json" }).catch(() => null);
  if (hit) return Response.json(hit, { headers: CACHED });

  if (!aiReady()) return jsonError(503, "ai_unavailable");
  const client = new Anthropic();
  const msg = await client.messages.create({
    model: MODEL_FAST,
    max_tokens: 4000,
    system: `You translate website copy for NEXTWISE, an AI systems studio, from English into ${langName(lang)}.
Return ONLY a JSON object with exactly the same keys, nesting and array lengths as the input; translate every string value.
Keep unchanged: brand and product names (NEXTWISE, NewsForce, Casa Alesia, Intensa, Claude, Gemini, GPT, Grok, Slack, WhatsApp, Cal.com), the abbreviations EBITDA, CAIO, PE, AI, ERP, CRM, all numbers, currency amounts and symbols, dates and email addresses.
Write natural, concise business copy for company owners, the way a native copywriter would, not word-for-word. Keep each string about as long as the original. Use the formal "you" where the language has one.`,
    messages: [{ role: "user", content: JSON.stringify(source) }],
  });
  const text = msg.content.map((b: any) => (b.type === "text" ? b.text : "")).join("");
  let out: any;
  try {
    out = JSON.parse(text.slice(text.indexOf("{"), text.lastIndexOf("}") + 1));
  } catch {
    return jsonError(502, "bad_translation");
  }
  if (!sameShape(source, out)) return jsonError(502, "shape_mismatch");
  await store.setJSON(key, out).catch(() => {});
  return Response.json(out, { headers: CACHED });
};

export const config: Config = {
  path: "/api/translate",
  method: "GET",
  rateLimit: { windowLimit: 90, windowSize: 60, aggregateBy: ["ip", "domain"] },
};
