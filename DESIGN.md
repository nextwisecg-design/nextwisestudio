# NEXTWISE — design system

Direction: the brand's purple and amber, kept, but with a stricter job for each. Light, cool paper for reading; one deep-night surface for everything "live" (the AI console, the lead case study, the Ask panel, the closing band). Not based on UXKIN references (not connected); built from the existing site and the brand pitch deck.

## Color
| Token | Value | Role |
|---|---|---|
| paper | #F6F5FA | page background |
| paper-2 | #ECEAF4 | tinted bands, quiet chips |
| card | #FFFFFF | raised surfaces on paper |
| ink | #16152E | text |
| muted | #5D5B73 | secondary text (6.3:1 on paper) |
| line | #DCD9E8 | borders, rules |
| night | #0E0E1B | live surfaces: console, lead case, Ask, contact, footer |
| purple | #763ADF | primary: buttons, links, focus, selected states |
| purple-soft | #EFE8FD | background of the market section |
| amber | #F59F0A | money and outcomes only: on night, or as a button fill |
| amber-ink | #9A5900 | money figures on paper (5.2:1) |

Rule: purple = act, amber = money/result. Nothing else is colored.

## Typography
- Commissioner (variable, self-hosted, with the Flair axis) for everything. Headlines 700–750 with `FLAR 100`, tight tracking (−0.02 to −0.035em). Body 17px / 1.6.
- IBM Plex Mono only inside the AI console and for timeline labels: it marks "this is the machine talking".
- IBM Plex Sans Arabic loads only for Arabic.
- Scale: 13 · 15 · 17 · 19 · 24 · 30 · 46 · 80 (hero, fluid).

## Spacing and shape
- 4px base: 4 · 8 · 12 · 16 · 24 · 32 · 48 · 64 · 96 · 128. Sections: 128px desktop, 96px phone. Content width 1200px.
- Radius: 6 (buttons, inputs), 12 (cards), 20 (console, panels). One shadow, used only on raised popovers, the Growth tier and the market list.

## Components
- Buttons: primary (purple), ghost (outline), amber (money actions on night), quiet (text on night). 48px tall; focus ring 3px purple.
- Pickers: market and language, `<details>` popovers, close on Escape and outside click.
- Systems: tablist with arrow keys; flow diagram with one travelling amber dot (off with reduced motion).
- Status pills: Live (green), In build (amber).

## Motion
One page-load moment (headline, then the console). The flow dot in Systems. Nothing fades in on scroll.
