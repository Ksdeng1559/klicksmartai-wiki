# Accord Financial — Style Capture for Mortgages by Dennis Eng

**Source:** accordfinancial.com — scraped 2026-10-03
**Pages sampled:** home, services, solutions, apply-now, about-us, accordexpress-covid-19-loans, investor-relations, financial-reports, plus the FR (French) home mirror
**Raw scrapes:** `style-source/` (17 HTML + MD files, both EN and FR)

---

## 1. Brand voice in one paragraph

Accord is **measured, capital-markets credible, and quietly confident.** Voice sits in the institutional-middle register: not banking-formal (no "Dear Valued Client" filler), not startup-casual (no "Hey founders!"). Sentences are short and complete. Adjectives are earned: "fast and flexible" is their tagline-pair (used 4-6 times per page). Brand names itself in third person by default ("Accord offers...", "Accord understands...") but slips into "We deliver..." / "Our services..." for directness when describing offerings. The Canadian-anchor voice is strong — they say "Canadian" or "Canada" deliberately, not "North American."

**Voice signature phrases (in priority order, lift these for our pages):**
- "fast and flexible" — the brand duet (use together, never alone)
- "leveraging your assets" — used for any asset-based product (LOC, factoring, ABL)
- "every business is unique" — empathy framing before listing offerings
- "the next stage of growth" — neutral-positive way to talk about expansion
- "optimize your cash flow" / "spearhead a restructuring" — verb-led action statements

**Voice anti-patterns (do NOT borrow):**
- No exclamation marks in body copy
- No emoji
- No second-person ("you can", "we'll help you") in headings — that's for CTAs only
- No question-form headings
- No testimonials with full-name attribution — Accord doesn't carry them

---

## 2. Page architecture (the 6-section rhythm)

The home page runs a **6-section pattern** in this exact order:

1. **Hero** — single H2 statement + supporting paragraph + 1 CTA. No top-half. No pre-header rotator/slider.
2. **What We Do** — 4 financing-product cards (icon + title + 1-sentence summary + Learn more link)
3. **How We Help** — situation cards (Growth / Acquisitions / Restructuring / Receivables / Unexpected Events) with link to dedicated page
5. **Who We Serve** — industry cards (Manufacturing, Retail, Wholesale, Import/Export, Apparel, Food&B, Construction, Services) + "View our Expertise" CTA
6. **Latest News** — 3 latest posts in card grid + "View All" link to news archive
7. **How Can We Help You?** — gravity form with conditional logic + secondary CTA stack ("Apply / Get Ready to Apply / Accord Services / FAQ / Contact us")
8. **Footer trust band** — Quick Links / Investor Relations / Resources three-column, with SEDAR + TSX quote + PDF decks

**Key structural choices to mirror:**
- **H1 on home is "Home"** (hidden/decorative; the visible hero uses H2). SEO cost is real but they accept it for the visual cleanness. **We should NOT copy this** — keep our H1 as the visible hero statement.
- **No carousel on home.** Static hero. We should keep ours static too — carousels tank conversion.
- **Section H2s are always 3-4 words, question-or-statement form:** "What We Do", "How We Help", "Who We Serve", "Latest News", "How Can We Help You?"
- **Each section is short** — 3-5 cards max. Accord trusts the user to click for detail.

---

## 3. Typography & layout signals

**Builder:** WordPress + Divi theme (Elegant Themes) — confirmed by `et_pb_button`, `et_pb_section`, `gfield`, `gform` class signatures (724 "d-" prefix class instances on home alone). Migration target is also WordPress, so Divi's CSS block naming transfers 1:1.

**Visual signature:**
- **Palette:** Deep institutional navy primary (#004F71 / #015072 / #005a87 / #006ba1) + soft teal accent (#6FCDDF / #31cdcf / #34e2e4) + small green CTA confirmation (#67a671). White space dominant. No warm accent, no orange, no gradients — they're a "trust blue" shop.
- **Type pairing:** Divi's default — Open Sans / Raleway stack. Body weights 400-600, headings 600-700.
- **Image style:** Real-photo editorial (people, buildings, industries) — no illustrations, no flat-design icons in hero, no stock-people-in-suits clichés.
- **Spacing:** Generous. Hero has full-viewport height feel. Section vertical padding ~80-120px desktop.

**For our rebuild (WordPress — same stack):**
- Adopt the **navy + teal + green** palette directly. It signals "capital markets" without saying "bank." Glasslake uses warm cream; Kingsmen uses corporate blue; Bizcap uses purple — so we own **navy + teal** for "Dennis can carry it" reliability.
- Match the **3-4 word H2** pattern across every page. This is the easiest voice signal to copy and the one that costs the most SEO if missed.
- Copy the **Learn more / Apply Now / Get Started / Get in Touch / View All / Read more** CTA vocabulary exactly. These convert short.

---

## 4. Headline & title formulas (lifted from real pages)

| Page | Title pattern | Real example |
|------|---------------|--------------|
| Home | `Topic in Geo \| Brand` | Business Financing in Canada \| Accord Financial |
| Services | `Verb + Object 2 + Preposition + Object 3` | Leverage Your Assets to Fuel the Next Stage of Growth |
| About | `Emotional abstract noun` | Embracing the Future from a Position of Strength |
| Apply | `Action verb + noun` | Apply Now / Smart and Flexible Business Funding |
| Accordexpress | `Product noun + with + Brand` | Small Business Loans with AccordExpress |
| Investor | `Plain corporate` | Investor Relations / Financial Reports |

**Meta description pattern:** `[Brand] helps [audience] access [benefit list].`

> "Accord Financial helps Canadian companies access flexible financing for cash flow, growth, acquisitions, restructuring, receivables, inventory and equipment."

→ For us: "Mortgages by Dennis Eng helps Canadian small-business owners compare business loans, lines of credit, factoring, bridge financing and commercial mortgages across BDC, Glasslake, Kingsmen and other approved lenders."

**Hero H2 pattern:** `Verb-ing + Object + for + Audience`

> "Simplifying Access to Capital for Canadian Entrepreneurs"

→ For us: "Comparing Business Loans for Canadian Small-Business Owners" / "Matching Capital to Canadian SMBs"

---

## 5. CTA vocabulary (lift verbatim)

```
Apply Now / APPLY NOW         → primary action (form / landing)
Learn more                    → secondary action (drill-in)
Get Started                   → entry-point CTA from low-intent pages
Get in Touch                  → personal-contact fallback
View All                      → news archive / category page
Read more                     → blog post card
Get Ready to Apply            → pre-qualification resource (PDF)
```

**Apply-page CTA stack (mirror this exactly on our `/apply/` page):**

| Button label | Target | Purpose |
|--------------|--------|---------|
| Apply | TFA Forms external URL | Start application for funding today |
| Get Ready to Apply | PDF download | Learn what you need to prepare before applying |
| Accord Services | Internal /services/ | Discover our financing solutions and see how we can help |
| FAQ | PDF download | Quick answers to help you through the financing process |
| Contact us | Internal /contact/ | Low-friction fallback |

**CTA micro-copy pattern:**
- 2-3 word button label
- 8-12 word sub-line ("Start your application for funding today.")
- 1-2 sentence body paragraph between CTA blocks
- White-on-navy or navy-on-cream — never inverted

---

## 6. Trust signals (the institutional-banker stack)

Accord builds trust without a single testimonial. Instead they carry:

1. **Public-company rigour** — TSX:ACD ticker in footer + linked stock quote to TMX. We don't have a ticker, but we can mirror by carrying: **Dare2Dream Verico BC license number in footer + Mortgage Architects affiliation**. (Already in our compliance disclosure — promote it.)
2. **Investor-relations desk** — Financial Reports / Articles and By-Laws / Investor Presentation / Corporate Governance. We don't have this; skip.
3. **Regulatory filings** — direct SEDAR link. We can't, skip.
4. **PDF asset library** — Investor decks, articles of incorporation. We can mirror with: **PDF rate sheets** (Glasslake, Kingsmen, AFN, Bizcap) under `/lender-info/` once we have sign-off.
5. **"40 years of experience" / "Founded 19XX"** — we don't carry this; skip.
6. **"Trusted by" logo bar** — they don't have one. Don't add ours either; the lenders themselves are the trust signal in a comparison marketplace.

**Our version of the trust stack should be:**
1. BC license + Verico / Dare2Dream in footer
2. Compliance disclosure: "Dennis is a licensed mortgage broker; may refer to one or more lenders" (already drafted in wireframe)
3. Lender-rate PDF downloads under `/lender-info/` (when available)
4. Honest "we are paid commission by some lenders" disclosure on every product page
5. **No fabricated reviews, no Trustpilot screenshots** — that's the wrong play for a regulated broker

---

## 7. Section copy patterns (the H2 → H3 → paragraph rhythm)

Every Accord product page uses the same structural template:

```
H1: (page-specific verb-led statement)
P:  (intro paragraph, 2-3 sentences, audience empathy)

H2: Our Solutions  /  Our Services  /  How it Works
H3: Card 1 title (product name)
P:  1-2 sentence elevator pitch ending in "Learn more" link

H3: Card 2 title
P:  1-2 sentence elevator pitch ending in "Learn more" link

... (4-6 cards)

H2: How Can We Help You?  (form CTA section)
H2: Need industry-specific advice?  (cross-link section)
```

**The 1-sentence elevator pitch formula:**
```
[Product] is [designed for / ideal for / a viable alternative for] [use case],
[Accord's / the lender's] [benefit sentence].
```

Examples pulled verbatim:
- "**Factoring** is ideal for [businesses with slow receivables]. Boost your working capital and unlock the value of your accounts receivable by factoring with Accord. We offer flexible financing solutions from $100,000 to $20 million, improving your company's cash flow."
- "**Retail Inventory Financing**. Many lenders shy away from financing retailers, but Accord understands that your business is unique, and we want to help you grow and prosper with fast and flexible financing solutions."
- "**Small Business Loans**. Accord Small Business Finance helps small businesses, whose financial needs cannot be readily met through their primary bank or credit union with traditional loans, by providing various solutions, such as equipment financing, to boost liquidity."

**For our pages, swap Accord → Glasslake / Kingsmen / AFN / Bizcap, and use this exact 1-sentence elevator formula:**

> "**Invoice factoring.** Turn unpaid invoices into working capital. Kingsmen Capital purchases your receivables and pays you up to 90% within 24-48 hours, with the remainder (minus a 1-3% fee) collected when your client pays. Best for B2B businesses with $25K-$10M annual revenue."

---

## 8. Form pattern (Gravity Forms with conditional logic)

The "How Can We Help You?" form has **conditional Country/Province dropdowns** — choose Canada → shows province list; choose United States → state list; choose Other → free text.

**For our build:** Mirror this on `/apply/` with a multi-step form:
1. **Contact Info** (name, email, phone)
3. **Business Info** (name, time in business, monthly revenue, province)
5. **Financing Need** (amount, purpose dropdown, urgency dropdown, deal summary textarea)
6. **Consent** (broker disclosure, privacy policy checkbox required)

Keep the form **3 columns max on desktop, full-width stacked on mobile**. Accord's form is dense (single column). For our longer form, break into steps.

---

## 9. SEO signals from raw HTML

- **Per-page H1 count:** 1 (sometimes hidden on home)
- **H2 per page:** 4-6 (section rhythm)
- **H3 per page:** 4-8 (cards within sections)
- **Title pattern:** Topic | Brand (48-60 chars)
- **Meta description:** Brand + audience + benefit list (155-160 chars)
- **Image alt text:** absent (we should add alt text on every product image — Accord's gap)
- **Schema:** likely LocalBusiness + FinancialProduct; check for review/testimonial markup (none found on scraped pages)
- **Internal cross-link density:** very high (every card links to a dedicated service page)

---

## 10. Anti-AI-slop quick checklist

When writing Mortgages by Dennis Eng pages in Accord style, avoid:

- ❌ Generic LLM phrases: "in today's fast-paced world", "look no further", "comprehensive solution", "robust platform", "leverage our solutions"
- ❌ Em-dash stuffing ("— your trusted partner — your growth engine —")
- ❌ 3-bullet stacked feature lists ("Fast. Flexible. Affordable.")
- ❌ Vague urgency ("don't wait until it's too late")
- ❌ "Whether you're a startup or enterprise" (we serve SMB; say SMB)
- ❌ Starting 3+ sentences in a row with the same word
- ❌ Headings ending in colons
- ❌ Bullet walls longer than 5 items without sub-headings
- ❌ Made-up statistics ("trusted by 10,000+ Canadian businesses")
- ❌ Testimonials without written client consent
- ❌ "Conclusion" or "Summary" sections

**Use instead:**
- ✅ Sentence-case headings ("Compare business loan options" not "Business Loans Options: Your Complete Guide")
- ✅ Verb-led H1s and H2s ("Leverage..." / "Match capital to...")
- ✅ Specific number ranges ($200K-$5M not "$250K+")
- ✅ Lender names named plainly (Glasslake, not "a leading Canadian lender")
- ✅ Canadian spelling plain ("Get your business financing..." not "Obtain your...")
- ✅ One CTA per section, never three stacked CTAs

---

## 11. Files written

- `accord-style-capture.md` (this file) — writing guide
- `style-source/` — 17 raw scrapes for cross-reference

**Reference docs to cross-link from this capture:**
- `verticals/business-loans-canada/wireframe.md` — our page wireframe (must be rewritten in this voice before launch)
- `verticals/business-loans-canada/strategy/page-content-proposals.md` — full content outlines (must adopt this voice)
- `verticals/business-loans-canada/executive-summary-with-citations.md` — client-facing summary (should use this meta-description pattern)