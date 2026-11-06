export default {
  slug: "usa-hometown-experts",
  company: "USA Hometown Experts",
  market: "us",
  date: "November 4, 2026",
  headline: "Two of your brands give two different answers to the same 2 a.m. question.",
  intro:
    "We read Metro Plumbing, Heating & Air and Dixie Electric, Plumbing & Air the way a homeowner would at night: website, listings, reviews. Everything below links to where we saw it. Three fixes cost nothing and you can make them this week.",
  scope:
    "USA Hometown Experts runs eight local brands. We couldn't read the parent company's website, so this covers two of them: Metro (Chattanooga, TN) and Dixie (Montgomery, AL and nearby markets).",
  scopeUrl: "https://www.businesswire.com/news/home/20261015432894/en/GHK-Capital-Partners-LP-Completes-Acquisition-of-USA-Hometown-Experts-Inc.",
  summary: [
    "Metro's website promises 24/7 emergency service. Its HomeAdvisor profile says it offers no emergency service.",
    "Dixie's website lists office hours ending at 5 or 6 p.m. A listing citing its Google profile says “Open 24 hours.”",
    "Reviews praise your speed, with one recent “I never heard back.”",
  ],
  channels: [
    { name: "Phone, Metro", status: "warn", detail: "Two numbers on the contact page: (423) 855-0967 and (423) 250-9376.", url: "https://metropha.com/contact/" },
    { name: "Online booking, Metro", status: "ok", detail: "“Schedule Your Service” form, plus “Book Online” and “Instant Quote.”", url: "https://metropha.com/" },
    { name: "Phone, Dixie", status: "ok", detail: "One company number: (334) 262-2946.", url: "https://calldixie.com/contact/" },
    { name: "Online booking, Dixie", status: "ok", detail: "Date and time picker. “Our office will reach out to you shortly to confirm.”", url: "https://calldixie.com/contact/" },
    { name: "Portals", status: "ok", detail: "Metro on HomeAdvisor, Dixie on BBB: customers meet you off your own sites too.", url: "https://www.homeadvisor.com/rated.MetroSewerDrainInc.78196536.html" },
    { name: "Live chat or text", status: "unknown", detail: "Not seen on either site. A widget that loads separately may not have shown up for us." },
  ],
  hours: [
    { name: "Metro, website", status: "ok", detail: "“We offer 24/7 emergency plumbing service across Greater Chattanooga.”", url: "https://metropha.com/" },
    { name: "Metro, HomeAdvisor", status: "bad", detail: "“No, Metro Plumbing, Heating & Air does not offer emergency services.” Same profile lists 24/7 hours.", url: "https://www.homeadvisor.com/rated.MetroSewerDrainInc.78196536.html" },
    { name: "Dixie, website", status: "warn", detail: "7 a.m.–5 p.m. CT (Montgomery, Auburn-Opelika), 8 a.m.–6 p.m. ET (Columbus, LaGrange). Emergency repairs mentioned, no 24/7 wording.", url: "https://calldixie.com/contact/" },
    { name: "Dixie, Google data", status: "bad", detail: "A directory citing the Google profile shows “Open 24 hours” every day.", url: "https://serviceagent.ai/directory/alabama/montgomery/hvac/dixie-electric-plumbing-air/" },
  ],
  reviewsNote: "Most of what we read is positive on speed, with an occasional miss.",
  quotes: [
    { q: "Response time and availability are excellent.", who: "Laura M. on Dixie, BBB, April 2025", url: "https://prod.bbb.org/us/al/montgomery/profile/electrician/dixie-electric-plumbing-air-0463-75000791/customer-reviews", tone: "pos" },
    { q: "willingness to stop by my house late in the afternoon to accommodate my hours", who: "Pat W. on Metro, Customer Lobby, May 2025", url: "https://www.customerlobby.com/reviews/46589/metro-plumbing-heating-air", tone: "pos" },
    { q: "I never heard back", who: "Precious S. on Dixie, Yelp review on MapQuest, November 2025", url: "https://startpage.mapquest.com/us/alabama/dixie-electric-plumbing-air-371235107", tone: "neg" },
  ],
  fixes: [
    { title: "Correct Metro's HomeAdvisor profile.", body: "Its emergency answer contradicts the website. Whichever is current, a homeowner should read the same answer in both places." },
    { title: "Line up Dixie's hours.", body: "Compare the Google Business Profile with the website, and say plainly what happens after 5 p.m. and on weekends, including how to reach someone for an urgent job." },
    { title: "Show one phone number on Metro's contact page.", body: "If the second number is for call tracking, the customer only needs one. While you're there, click through “Book Online” to confirm it opens the scheduler." },
  ],
  calc: { unit: "$", job: "average ticket", leads: "after-hours calls or forms a week, across the brands" },
  convo: {
    title: "What a 9 p.m. call could sound like",
    note: "Illustrative only, using Metro's advertised emergency service. A real version follows your rules for dispatch, safety and pricing.",
    channel: "Metro Plumbing, Heating & Air",
    turns: [
      ["c", "Hi, our furnace quit and the house is getting cold. Is anyone there this late?"],
      ["a", "Yes, I can help. Do you smell gas, or is anyone at risk from the cold right now?"],
      ["c", "No gas smell. We do have a toddler, though."],
      ["a", "Thanks for telling me. What's the address, and is this the best number for the technician?"],
      ["c", "We're in Hixson, and this number works."],
      ["a", "I've sent this to the on-call technician and flagged the toddler. You'll get a text once they confirm a time."],
      ["c", "What if I start smelling gas while we wait?"],
      ["a", "Leave the house and call 911 and your gas utility from outside. I've added this to your notes for the technician."],
    ],
  },
  build: {
    name: "One after-hours desk for all eight brands",
    what: "An agent on phone, text and web forms that answers in each brand's name, triages emergencies with your safety script, and hands the on-call tech a complete job, not a voicemail.",
    timeline: "First brand live in about two weeks, the rest brand by brand.",
  },
  kit: {
    title: "After-hours Response Kit",
    autoReplies: [
      { channel: "Text, Metro", when: "missed call after hours", text: "Hi, this is Metro Plumbing, Heating & Air. Sorry we missed your call. If you smell gas, leave the house and call 911 and your gas utility from outside. For an urgent repair, reply URGENT with your address and our on-call technician will call you back within [time]. Anything else, reply with a few words and we'll call you [tomorrow from 8 a.m.]." },
      { channel: "Text, Dixie", when: "missed call after hours", text: "Hi, this is Dixie Electric, Plumbing & Air. Our office is closed right now and opens at [7 a.m. CT]. If this is an emergency repair, reply URGENT with your address and [what happens next]. If you smell gas or see sparks, get everyone outside and call 911 first." },
      { channel: "Email, both brands", when: "form submitted after hours", text: "Thanks, we've got your request for [service] at [address]. Our office is closed right now, so here's exactly what happens next: [a team member calls you by 9 a.m. tomorrow / the on-call tech calls within the hour if you marked it urgent]. If anything changes, just reply to this email." },
    ],
    formLines: [
      { where: "Under Metro's “Schedule Your Service” button", text: "We confirm every request by [phone/text] within [time] during business hours. After hours? Call [one number] for emergencies; everything else is confirmed first thing next morning." },
      { where: "Under Dixie's booking picker", text: "Picked a time? We'll call or text to confirm by [time]. Booking after 5 p.m. or on a weekend means we'll confirm the next business morning." },
    ],
    voicemail: { label: "Metro, after hours, 30 seconds", text: "You've reached Metro Plumbing, Heating & Air. Our office is closed, but we offer 24/7 emergency service across Greater Chattanooga. If you smell gas, hang up, leave the house and call 911. For an urgent repair, leave your name, address and what's going on, and our on-call technician will call you back within [time]. For anything else, we'll call you back [tomorrow morning]. Thank you." },
    reviewReplies: [
      { to: "Reply to “I never heard back” (Dixie, MapQuest/Yelp)", text: "We're sorry. Not hearing back is exactly what we never want for a customer, and it shouldn't have happened. We'd like to make it right: please call [name] directly at (334) 262-2946, or reply here with the best time, and we'll follow through personally. We've also [what you changed, e.g. added a confirmation text to every request] so this doesn't happen again." },
      { to: "Reply to a review praising speed (Laura M., BBB)", text: "Thank you, Laura. Getting to you quickly matters to us as much as the work itself, and we'll pass your words on to the team. We're here whenever you need us." },
      { to: "Reply to a late-visit thank-you (Pat W., Customer Lobby)", text: "Thanks, Pat. Working around your schedule is part of the job, and we're glad it helped. See you next time, and we hope not too soon." },
    ],
    checklist: [
      { where: "Metro, HomeAdvisor profile", url: "https://www.homeadvisor.com/rated.MetroSewerDrainInc.78196536.html", item: "Emergency service answer matches the website's 24/7 promise." },
      { where: "Metro, contact page", url: "https://metropha.com/contact/", item: "One phone number shown; the second one removed or labelled." },
      { where: "Metro, “Book Online”", url: "https://metropha.com/", item: "Click through and confirm it opens the scheduler." },
      { where: "Dixie, Google Business Profile", item: "Hours match the website (7–5 CT, 8–6 ET) or the site says 24/7." },
      { where: "Dixie, contact page", url: "https://calldixie.com/contact/", item: "One sentence on what to do after 5 p.m. and on weekends." },
      { where: "Dixie, BBB profile", url: "https://prod.bbb.org/us/al/montgomery/profile/electrician/dixie-electric-plumbing-air-0463-75000791/customer-reviews", item: "Hours and phone match the website." },
      { where: "Both brands, review sites", item: "Every negative review answered within a day, using the reply above as a start." },
    ],
  },
  method: {
    read: ["Metro and Dixie websites (home and contact pages)", "HomeAdvisor and BBB profiles", "Public reviews on BBB, Customer Lobby and MapQuest", "A directory listing citing Google Business Profile data"],
    notDone: ["We didn't call or submit any form, so we can't say how after-hours contacts are handled in practice.", "We didn't review the other six brands."],
  },
};
