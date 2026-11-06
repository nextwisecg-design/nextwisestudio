export default {
  slug: "king-risk-partners",
  company: "King Risk Partners",
  market: "us",
  date: "November 4, 2026",
  headline: "64 offices, fast people, and no opening hours anywhere on the site.",
  intro:
    "We read King Risk Partners the way a client would: website, forms, public listings and reviews. Speed is a real strength in what we found. Three gaps around it cost nothing to close, and you can close them this week.",
  summary: [
    "Reviews keep coming back to one thing: you return calls quickly.",
    "The site lists 64 offices in 16 states, but no hours, after-hours or claims information on the pages we read.",
    "Quote and certificate forms don't say who receives the request or when they'll respond.",
  ],
  channels: [
    { name: "Phone", status: "ok", detail: "Two central numbers, (844) KING-INS and (888) 377-0420, plus a local number for each of 64 offices in 16 states (our count).", url: "https://www.king-insurance.com/contact-us/" },
    { name: "Quote requests", status: "warn", detail: "“Fill out my online form” opens a form hosted by a third party. No word on when you'll respond.", url: "https://jumpem.wufoo.com/forms/zdmyven0ju96mq" },
    { name: "Certificates", status: "ok", detail: "A dedicated certificate request page.", url: "https://www.king-insurance.com/request-for-certificate/" },
    { name: "Existing clients", status: "ok", detail: "Client login and Pay A Bill. We didn't open either.", url: "https://insurlink.vertafore.com/end-insured/3048841-1" },
    { name: "Chat, text, claims", status: "unknown", detail: "No chat, texting, or claims page or number on the pages we read. A widget that loads separately may not have shown up for us." },
  ],
  hours: [
    { name: "Your website", status: "bad", detail: "No hours, weekend, after-hours or claims-line wording on the homepage, contact page, or the Avon and Tampa office pages.", url: "https://www.king-insurance.com/avon/" },
    { name: "Gainesville, public listing", status: "ok", detail: "Birdeye: Monday to Friday, 8 a.m.–5 p.m., closed weekends.", url: "https://reviews.birdeye.com/king-insurance-partners-173504338159070" },
    { name: "Forms", status: "bad", detail: "No statement of when someone will get back to a person who requests a quote.", url: "https://www.king-insurance.com/" },
  ],
  reviewsNote: "Birdeye shows 4.1 from 94 Google reviews for Gainesville. Speed is a strength in everything we read; we saw no recurring pattern of slow-response complaints.",
  quotes: [
    { q: "They are easy to reach and return calls quickly.", who: "Janet H., your testimonial page", url: "https://king-insurance.com/rave-reviews", tone: "pos" },
    { q: "She solved my problem more quickly than I ever thought possible.", who: "Google review on Birdeye, Gainesville, about three months ago", url: "https://reviews.birdeye.com/king-insurance-partners-173504338159070", tone: "pos" },
    { q: "personable, responsive, quick to resolve any issues", who: "Google review on Birdeye, Gainesville, about five months ago", url: "https://reviews.birdeye.com/king-insurance-partners-173504338159070", tone: "pos" },
  ],
  fixes: [
    { title: "Publish hours for every office.", body: "On the contact page list and on each office page, matched to Google. It matters more as newly acquired offices join with their own schedules." },
    { title: "Add a “what happens next” line next to the forms.", body: "On the quote and certificate pages, say who receives the request and when they'll respond, using whatever is true today." },
    { title: "Add one short claims page.", body: "How to report a claim, links to carrier claim lines, and what to do when the office is closed." },
  ],
  calc: { unit: "$", job: "average first-year commission per new account", leads: "quote or certificate requests a week that arrive after hours" },
  convo: {
    title: "What a Friday-evening certificate request could look like",
    note: "Illustrative only. Names are placeholders. A real version follows your routing and licensing rules, and never confirms or changes coverage.",
    channel: "King Risk Partners",
    turns: [
      ["c", "I need a certificate of insurance for a general contractor by Monday morning. Is your office closed?"],
      ["a", "The office is closed for the evening, but I can start this now. What are your business name and the contractor's name?"],
      ["c", "Sample Roofing, and it's for Sample Builders."],
      ["a", "Thanks. Did they ask for additional insured wording?"],
      ["c", "Yes. Can you confirm my policy allows that?"],
      ["a", "I can't confirm or change coverage, but a licensed team member can. I've sent them your request with the Monday deadline."],
      ["c", "How will I know it went through?"],
      ["a", "You'll get an email now with a copy of the request, and your office will follow up when it opens."],
    ],
  },
  build: {
    name: "Your speed, kept after 5 p.m. and across every new office",
    what: "Every form, call and certificate request gets an instant, accurate answer and lands with the right office, complete. Licensed staff handle coverage; the agent makes sure nothing waits until Monday unseen.",
    timeline: "First offices live in about two weeks; each acquired office plugs in as it joins.",
  },
  kit: {
    title: "Client Response Kit",
    autoReplies: [
      { channel: "Email", when: "online quote form, any time", text: "Thanks for contacting King Risk Partners. Your quote request has reached our [office] team. A licensed agent will [call / email] you by [time]. If you have a deadline (a renewal, a contract, a closing), reply with the date and we'll work to it." },
      { channel: "Email", when: "certificate request", text: "Got it, your certificate request for [holder] is in. Certificates are usually issued within [time] during business hours. If you need it by a specific date, reply with the deadline. We'll email a copy as soon as it's issued." },
      { channel: "Text", when: "missed call after hours", text: "Hi, this is King Risk Partners. Our office is closed right now and opens at [time]. To report a claim tonight, call the claim number on your policy or carrier app. For anything else, reply here and we'll get back to you [first thing tomorrow]." },
    ],
    formLines: [
      { where: "Next to “Fill out my online form”", text: "Your request goes straight to a licensed agent at [office], who will contact you within [time]." },
      { where: "On the certificate request page", text: "Requests received before [time] are usually issued the same business day. Need it sooner? Call [number]." },
    ],
    voicemail: { label: "Any office, after hours, 30 seconds", text: "You've reached King Risk Partners, [office]. We're closed right now; our hours are [hours]. To report a claim, please call the number on your policy or carrier app. Otherwise leave your name, number and what you need, and we'll call you back [the next business morning]. We return calls quickly. Thank you." },
    reviewReplies: [
      { to: "Reply to “solved my problem more quickly than I ever thought possible” (Gainesville, Google)", text: "Thank you! Solving things fast is exactly what we want to be known for. We'll pass this on to [agent name]." },
      { to: "Reply to “personable, responsive, quick to resolve” (Gainesville, Google)", text: "Thank you for taking the time to write this. Responsiveness is something we work at every day, and it's great to hear it shows." },
      { to: "Template for a future negative review", text: "We're sorry this wasn't the experience you expected; it's not the standard we hold ourselves to. Please call [name] at [number] so we can look at your account personally and put it right." },
    ],
    checklist: [
      { where: "Contact page office list", url: "https://www.king-insurance.com/contact-us/", item: "Hours added for all 64 offices." },
      { where: "Office pages (e.g. Avon)", url: "https://www.king-insurance.com/avon/", item: "Hours and an after-hours line on each office page." },
      { where: "Quote form", url: "https://jumpem.wufoo.com/forms/zdmyven0ju96mq", item: "Confirmation message says who receives it and when they'll respond." },
      { where: "Certificate page", url: "https://www.king-insurance.com/request-for-certificate/", item: "Turnaround time stated." },
      { where: "Gainesville, Birdeye", url: "https://reviews.birdeye.com/king-insurance-partners-173504338159070", item: "Hours match Google and the website." },
      { where: "New site page", item: "One short claims page with carrier claim links and closed-office instructions." },
      { where: "Newly acquired offices", item: "Google profile hours and phone match the King site within a week of joining." },
    ],
  },
  method: {
    read: ["king-insurance.com homepage, contact page, Avon and Tampa office pages", "Quote form and certificate request page", "Birdeye profile for Gainesville", "Your testimonial page and public Google reviews"],
    notDone: ["We didn't call or submit any form, so we can't say how after-hours contacts are handled in practice.", "We sampled 2 of the 64 office pages; others may show hours."],
  },
};
