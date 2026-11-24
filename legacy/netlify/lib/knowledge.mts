import { getDict, MARKETS, LANGS, EMAIL } from "../../src/content/index.mjs";

export const MODEL_SMART = "claude-sonnet-5-5";
export const MODEL_FAST = "claude-haiku-5-5";

export function langName(code: string): string {
  const names: Record<string, string> = {
    en: "English", ro: "Romanian", ar: "Arabic (Gulf business register, Modern Standard Arabic)", de: "German", es: "Spanish",
    pt: "Portuguese", fr: "French", it: "Italian", pl: "Polish", nl: "Dutch", cs: "Czech", sk: "Slovak", hu: "Hungarian",
    hr: "Croatian", bg: "Bulgarian", sr: "Serbian (Latin script)", sl: "Slovenian", lt: "Lithuanian", lv: "Latvian",
    et: "Estonian", fi: "Finnish", sv: "Swedish", da: "Danish", no: "Norwegian (Bokmål)", el: "Greek", uk: "Ukrainian",
  };
  return names[code] || "English";
}

export function validMarket(m: unknown): string {
  return typeof m === "string" && m in MARKETS ? m : "global";
}
export function validLang(l: unknown): string {
  return typeof l === "string" && l in LANGS ? l : "en";
}

// Everything the AI may say about NEXTWISE, built from the website copy.
export function knowledge(market: string): string {
  const d: any = getDict(market, "en");
  const M: any = (MARKETS as any)[market];
  const lines: string[] = [];
  lines.push(`NEXTWISE is an AI systems studio (NEXTWISE SRL, Romania, based in Bucharest). Contact: ${EMAIL}. Booking link: ${M.cal}.`);
  lines.push(`Visitor's market: ${M.name.en}. Prices for this market are in ${M.currency}.`);
  lines.push(`Positioning: ${d.hero.title} ${d.hero.sub}`);
  lines.push("\nSYSTEMS WE BUILD:");
  d.systems.items.forEach((s: any) => lines.push(`- ${s.name}: ${s.desc} Flow: ${s.flow.join(" → ")}.`));
  lines.push("\nPROCESS:");
  d.how.steps.forEach((s: any) => lines.push(`- ${s.when}, ${s.title}: ${s.body}`));
  lines.push("\nPRINCIPLES:");
  d.why.items.forEach((w: any) => lines.push(`- ${w.title} ${w.body}`));
  lines.push(`\nPRICING (${M.currency}): ${d.pricing.sub}`);
  d.pricing.tiers.forEach((t: any) => lines.push(`- ${t.name} (${t.sub}): ${t.price}. ${t.terms}. Includes: ${t.features.join("; ")}.`));
  lines.push(d.pricing.note);
  lines.push("\nCLIENT WORK (public, with permission):");
  d.work.items.forEach((w: any, i: number) => lines.push(`- ${w.name}, ${w.sector} (${i === 0 ? "live" : "in build"}): ${w.title}. ${w.body} Facts: ${w.facts.join("; ")}.`));
  if (d.market) {
    lines.push(`\nFOR THIS MARKET: ${d.market.title} ${d.market.body}`);
    d.market.points.forEach((p: string) => lines.push(`- ${p}`));
  }
  lines.push("\nFAQ:");
  d.faq.items.forEach((f: any) => lines.push(`Q: ${f.q}\nA: ${f.a}`));
  return lines.join("\n");
}

export function aiReady(): boolean {
  return Boolean(process.env.ANTHROPIC_API_KEY || process.env.NETLIFY_AI_GATEWAY_KEY);
}

// Stream text deltas from an Anthropic message stream to the browser.
export function textStream(
  run: () => AsyncIterable<any>,
  onDone?: (full: string) => Promise<void>
): Response {
  const enc = new TextEncoder();
  const body = new ReadableStream({
    async start(controller) {
      let full = "";
      try {
        for await (const ev of run()) {
          if (ev.type === "content_block_delta" && ev.delta?.type === "text_delta") {
            full += ev.delta.text;
            controller.enqueue(enc.encode(ev.delta.text));
          }
        }
        if (onDone) await onDone(full).catch(() => {});
      } catch (err) {
        console.error("stream error", err);
        if (!full) controller.error(err);
      }
      try { controller.close(); } catch {}
    },
  });
  return new Response(body, {
    headers: { "content-type": "text/plain; charset=utf-8", "cache-control": "no-store", "x-content-type-options": "nosniff" },
  });
}

export function jsonError(status: number, error: string): Response {
  return Response.json({ error }, { status, headers: { "cache-control": "no-store" } });
}
