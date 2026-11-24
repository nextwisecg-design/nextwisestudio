// Market variants. Each market overrides parts of the base copy, per language.
// Prices for US (USD) and UAE (AED) are rounded conversions of the EUR ranges:
// Darius confirms them before launch.

export const CAL_DARIUS = "https://cal.com/nextwise/30mindiagnosis";
// Until Cristi and Alex have their own Cal.com links, Romania books with the same link.
export const CAL_RO = "https://cal.com/nextwise/30mindiagnosis";
export const EMAIL = "darius@nextwise.studio";

export const MARKETS = {
  global: { code: "global", flag: "🌍", name: { en: "Global", ro: "Global" }, defaultLang: "en", currency: "EUR", cal: CAL_DARIUS, owner: "Darius" },
  us: { code: "us", flag: "🇺🇸", name: { en: "United States", ro: "Statele Unite" }, defaultLang: "en", currency: "USD", cal: CAL_DARIUS, owner: "Darius" },
  uae: { code: "uae", flag: "🇦🇪", name: { en: "UAE and the Gulf", ro: "Emirate și Golf" }, defaultLang: "en", currency: "AED", cal: CAL_DARIUS, owner: "Darius" },
  ro: { code: "ro", flag: "🇷🇴", name: { en: "Romania", ro: "România" }, defaultLang: "ro", currency: "EUR", cal: CAL_RO, owner: "Cristi & Alex" },
};
export const MARKET_ORDER = ["global", "us", "uae", "ro"];

// Example businesses for the live diagnosis, per market.
export const EXAMPLES = {
  global: {
    en: ["Logistics company, 120 trucks, three depots, dispatch by phone", "B2B distributor with 4,000 products, quotes sent by email", "Private equity fund with seven portfolio companies"],
    ro: ["Firmă de logistică, 120 de camioane, trei depozite, dispecerat la telefon", "Distribuitor B2B cu 4.000 de produse, oferte trimise pe email", "Fond de private equity cu șapte firme în portofoliu"],
  },
  us: {
    en: ["Insurance agency, three offices, 25 producers", "Home services company with 40 technicians in Texas", "PE fund with nine portfolio companies"],
    ro: ["Agenție de asigurări, trei birouri, 25 de agenți", "Firmă de servicii la domiciliu cu 40 de tehnicieni în Texas", "Fond PE cu nouă firme în portofoliu"],
  },
  uae: {
    en: ["Real-estate brokerage in Dubai, 60 agents, leads from portals", "Restaurant group with seven venues in Abu Dhabi", "Family business holding with five operating companies"],
    ro: ["Agenție imobiliară în Dubai, 60 de agenți, lead-uri din portaluri", "Grup de restaurante cu șapte locații în Abu Dhabi", "Holding de familie cu cinci firme operaționale"],
  },
  ro: {
    en: ["Group of three hotels in Brașov, bookings by phone and email", "Building-materials distributor, 4,000 products, quotes by email", "Car dealer with service centres in two cities"],
    ro: ["Grup de trei hoteluri în Brașov, rezervări la telefon și pe email", "Distribuitor de materiale de construcții, 4.000 de produse, oferte pe email", "Dealer auto cu service în două orașe"],
  },
};

const tiersEN = (p, t, names) => ({ tiers: [0, 1, 2].map((i) => ({ price: p[i], terms: t[i] })) });

export const OVERRIDES = {
  global: { en: {}, ro: {} },

  us: {
    en: {
      hero: {
        title: "Production AI for US operators. Live in days, priced on outcomes.",
        sub: "We design, build and run AI systems inside mid-market companies and PE portfolios: revenue engines, operations intelligence and custom agents. Live in days, measured every week, with part of our fee tied to the result.",
      },
      pricing: tiersEN(
        ["$15–50k", "$55–130k", "$220–550k+"],
        ["One-time setup, retainer from $3.5k / month", "Setup, $9–11k / month and a 10% success fee", "Custom scope, fractional CAIO, portfolio-wide"]
      ),
    },
    ro: {
      hero: {
        title: "AI în producție pentru firmele din SUA. Live în zile, plătit pe rezultat.",
        sub: "Proiectăm, construim și rulăm sisteme AI în firme mijlocii și portofolii PE: motoare de vânzări, inteligență operațională și agenți la comandă. Live în zile, măsurate săptămânal, cu o parte din onorariu legată de rezultat.",
      },
      pricing: tiersEN(
        ["15–50k $", "55–130k $", "220–550k+ $"],
        ["Implementare unică, abonament de la 3,5k $ / lună", "Implementare, 9–11k $ / lună și 10% taxă de succes", "Scop personalizat, CAIO fracționat, la nivel de portofoliu"]
      ),
    },
  },

  uae: {
    en: {
      hero: {
        title: "AI systems for the Gulf's fastest-moving companies.",
        sub: "WhatsApp-first agents that speak Arabic and English, revenue engines and operations intelligence, built into your business in days. We're in Dubai from 2 to 15 December 2026.",
      },
      market: {
        title: "Built for how business is done in the Gulf.",
        body: "Your customers are on WhatsApp, they switch between Arabic and English mid-sentence, and they expect an answer now. We build systems for that, not adapted from somewhere else.",
        points: [
          "WhatsApp-first: agents live where your customers already talk",
          "Arabic and English in the same conversation",
          "Prices in AED, contracts in English",
          "Leads from property portals and ads answered in minutes",
          "One system across all your branches and brands",
          "Meet us in person in Dubai, 2–15 December 2026",
        ],
        cta: "Book a meeting in Dubai",
      },
      pricing: tiersEN(
        ["AED 60–180k", "AED 200–480k", "AED 800k–2M+"],
        ["One-time setup, retainer from AED 12k / month", "Setup, AED 32–40k / month and a 10% success fee", "Custom scope, fractional CAIO, group-wide"]
      ),
    },
    ro: {
      hero: {
        title: "Sisteme AI pentru cele mai rapide firme din Golf.",
        sub: "Agenți pe WhatsApp care vorbesc arabă și engleză, motoare de vânzări și inteligență operațională, puse în firma ta în câteva zile. Suntem în Dubai între 2 și 15 decembrie 2026.",
      },
      market: {
        title: "Construit pentru felul în care se face business în Golf.",
        body: "Clienții tăi sunt pe WhatsApp, trec din arabă în engleză în aceeași frază și așteaptă răspuns acum. Construim sisteme pentru asta, nu adaptate din altă parte.",
        points: [
          "WhatsApp întâi: agenții sunt acolo unde vorbesc deja clienții",
          "Arabă și engleză în aceeași conversație",
          "Prețuri în AED, contracte în engleză",
          "Lead-urile din portaluri și reclame primesc răspuns în minute",
          "Un singur sistem pentru toate filialele și brandurile",
          "Ne vedem față în față în Dubai, 2–15 decembrie 2026",
        ],
        cta: "Programează o întâlnire în Dubai",
      },
      pricing: tiersEN(
        ["60–180k AED", "200–480k AED", "800k–2M+ AED"],
        ["Implementare unică, abonament de la 12k AED / lună", "Implementare, 32–40k AED / lună și 10% taxă de succes", "Scop personalizat, CAIO fracționat, la nivel de grup"]
      ),
    },
  },

  ro: {
    en: {
      hero: {
        title: "AI systems that make Romanian companies money.",
        sub: "We build and run AI systems inside your company in days, not months: sales, operations and decisions. Our team speaks Romanian, comes to your office and invoices from Romania.",
      },
      market: {
        title: "For companies in Romania",
        body: "You talk to people who know the market: Cristi and Alex handle Romania directly, and the systems are built for Romanian customers, Romanian invoices and Romanian law.",
        points: [
          "Contract and invoice from a Romanian company, NEXTWISE SRL",
          "Meetings at your office or online",
          "Systems that speak Romanian to your customers",
          "GDPR from day one, data in the EU",
          "Systems from €7k, scaled to the size of your company",
          "A proposal the same day as the diagnosis call",
        ],
        cta: "Book a call with Cristi or Alex",
      },
      pricing: tiersEN(
        ["€7–15k", "€15–25k", "€25k+"],
        ["One-time setup, optional monthly support", "Setup, monthly support and an optional success fee", "Custom scope, several systems, phased"]
      ),
    },
    ro: {
      hero: {
        title: "Sisteme AI care aduc bani firmelor din România.",
        sub: "Construim și rulăm sisteme AI în firma ta în zile, nu în luni: vânzări, operațiuni și decizii. Echipa vorbește română, vine la sediu și facturează din România.",
      },
      market: {
        title: "Pentru firmele din România",
        body: "Vorbești cu oameni care cunosc piața: Cristi și Alex se ocupă direct de România, iar sistemele sunt făcute pentru clienți români, facturi românești și legislația de aici.",
        points: [
          "Contract și factură de la o firmă românească, NEXTWISE SRL",
          "Întâlniri la sediul tău sau online",
          "Sisteme care vorbesc românește cu clienții tăi",
          "GDPR din prima zi, date în UE",
          "Sisteme de la 7k €, pe măsura firmei tale",
          "Propunere în aceeași zi cu discuția de diagnoză",
        ],
        cta: "Programează o discuție cu Cristi sau Alex",
      },
      pricing: tiersEN(
        ["7–15k €", "15–25k €", "25k+ €"],
        ["Implementare unică, suport lunar opțional", "Implementare, suport lunar și taxă de succes opțională", "Scop personalizat, mai multe sisteme, pe etape"]
      ),
    },
  },
};

// Deep merge where arrays of objects merge by index (used for pricing tiers).
export function merge(base, over) {
  if (Array.isArray(base) && Array.isArray(over)) {
    return base.map((b, i) => (over[i] === undefined ? b : merge(b, over[i])));
  }
  if (base && typeof base === "object" && over && typeof over === "object") {
    const out = { ...base };
    for (const k of Object.keys(over)) out[k] = k in base ? merge(base[k], over[k]) : over[k];
    return out;
  }
  return over === undefined ? base : over;
}
