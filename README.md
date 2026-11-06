# nextwise.studio — v2

Static site with four market variants, live AI features and IP-based routing, on Netlify.

## What's where
| Path | What |
|---|---|
| `src/content/en.mjs`, `ro.mjs` | All copy, English master + Romanian |
| `src/content/markets.mjs` | Market variants (hero, prices, market section, booking link, examples) |
| `src/template.mjs`, `src/site.css`, `src/client/app.js` | Page, styles, browser code |
| `netlify/functions/diagnose.mts` | `/api/diagnose` — live business diagnosis (streams) |
| `netlify/functions/ask.mts` | `/api/ask` — answers questions next to the FAQ |
| `netlify/functions/translate.mts` | `/api/translate` — live AI translation into 24 more languages, cached forever in Blobs |
| `netlify/edge-functions/market.ts` | `/` → `/us/`, `/uae/`, `/ro/` or `/global/` by IP; the market picker's cookie wins; bots are not redirected |
| `src/audits/<slug>.mjs` | One free audit per prospect → `nextwise.studio/audit/<slug>/` (never indexed) |
| `src/audit-template.mjs`, `src/audit.css` | The audit one-pager design |
| `DESIGN.md` | Design tokens and rules |

Pages: `/global/`, `/us/`, `/uae/`, `/ro/` (Romanian), plus `/global/ro/`, `/us/ro/`, `/uae/ro/`, `/ro/en/`. Any other language: `?lang=de`, `?lang=ar`, …

## AI
The functions use the Anthropic SDK with no key in code. On Netlify they use the AI Gateway automatically; if the gateway isn't available on the plan, set `ANTHROPIC_API_KEY` (scope: Functions) in Netlify → Project configuration → Environment variables, then redeploy.
Every diagnosis is saved in the Blobs store `diagnoses` (text, answer, market, country) so sales can prepare the call.

## Deploy
Test link first (does not touch nextwise.studio):
```
npm install
npx -y netlify-cli@latest deploy --build --site db8e5f45-9814-47e0-ac8e-a29f1161ef70 --alias v2
```
→ `https://v2--nextwisestudio.netlify.app`

Live, after approval: same command with `--prod` instead of `--alias v2`.

## Before going live
- Confirm USD/AED ranges in `markets.mjs` and the Romanian tiers (€7–15k / €15–25k / €25k+).
- Confirm the NewsForce quote is theirs.
- Replace `CAL_RO` with Cristi's / Alex's Cal.com link when it exists.

## Free audits
1. Copy an existing file in `src/audits/`, rename it to the prospect's slug, fill in the fields from the audit in Notion.
2. Every finding needs a source URL; status is `ok`, `warn`, `bad` or `unknown`. No invented numbers: the calculator asks the prospect for theirs.
3. Deploy (same command as above). The link to send: `https://nextwise.studio/audit/<slug>/`.
