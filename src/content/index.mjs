import en from "./en.mjs";
import ro from "./ro.mjs";
import { OVERRIDES, merge } from "./markets.mjs";

export * from "./markets.mjs";

// Languages written by hand and prerendered as static pages.
export const PRERENDERED = ["en", "ro"];

// Every language offered. The ones not prerendered are translated live by AI
// from the English page and cached.
export const LANGS = {
  en: { label: "English", flag: "🇬🇧" },
  ro: { label: "Română", flag: "🇷🇴" },
  ar: { label: "العربية", flag: "🇦🇪", rtl: true },
  de: { label: "Deutsch", flag: "🇩🇪" },
  es: { label: "Español", flag: "🇪🇸" },
  pt: { label: "Português", flag: "🇵🇹" },
  fr: { label: "Français", flag: "🇫🇷" },
  it: { label: "Italiano", flag: "🇮🇹" },
  pl: { label: "Polski", flag: "🇵🇱" },
  nl: { label: "Nederlands", flag: "🇳🇱" },
  cs: { label: "Čeština", flag: "🇨🇿" },
  sk: { label: "Slovenčina", flag: "🇸🇰" },
  hu: { label: "Magyar", flag: "🇭🇺" },
  hr: { label: "Hrvatski", flag: "🇭🇷" },
  bg: { label: "Български", flag: "🇧🇬" },
  sr: { label: "Srpski", flag: "🇷🇸" },
  sl: { label: "Slovenščina", flag: "🇸🇮" },
  lt: { label: "Lietuvių", flag: "🇱🇹" },
  lv: { label: "Latviešu", flag: "🇱🇻" },
  et: { label: "Eesti", flag: "🇪🇪" },
  fi: { label: "Suomi", flag: "🇫🇮" },
  sv: { label: "Svenska", flag: "🇸🇪" },
  da: { label: "Dansk", flag: "🇩🇰" },
  no: { label: "Norsk", flag: "🇳🇴" },
  el: { label: "Ελληνικά", flag: "🇬🇷" },
  uk: { label: "Українська", flag: "🇺🇦" },
};

const BASE = { en, ro };

export function getDict(market, lang) {
  const l = BASE[lang] ? lang : "en";
  return merge(BASE[l], OVERRIDES[market]?.[l] || {});
}

// Top-level sections, translated one request at a time.
export const SECTIONS = ["meta", "nav", "hero", "stats", "diag", "work", "systems", "how", "why", "market", "pricing", "faq", "contact", "footer", "ui"];

// Bump when the English copy changes so cached translations refresh.
export const CONTENT_VERSION = "2026-11-04a";
