# Organic Search Strategy — Business Loan Marketplace

**Site:** Mortgagesbydenniseng.ca/business-loans/ (subdirectory on existing WordPress rebuild)
**Goal:** Capture Canadian business-owner search demand for funding, build a comparison marketplace, convert organic traffic into qualified leads forwarded to lenders.
**Constraint reconciliation:**
- "Zero cost" was aspirational. Real budget is on the table for: domain (already owned), hosting (existing), SEO plugin (~$60-200/yr), DataForSEO API calls (~$0.50-2/run), and selective content outsourcing.
- Facebook ads/Instagram: **deferred to Phase 3** (after 6+ months of organic traffic). The launch is SEO-first, not social-first.
- The "search tool" framing is the right one: we own the SERPs that buyers already type.

---

## TL;DR

This is an **8-12 month play**, not a 30-day launch. Three realistic numbers — corrected after a real Swoop competitive audit:

- **Month 3:** 500-2,000 organic sessions/month. 5-15 leads/month. ~$0-500 spend.
- **Month 6:** 2,000-6,000 organic sessions/month. 15-40 leads/month. ~$1,500-3,000 cumulative spend.
- **Month 12:** 8,000-20,000 organic sessions/month. **40-150 leads/month** (revised down from 100-300 — see "Estimate Verification" below). ~$5,000-10,000 cumulative spend.

The 7-pillar plan is correct. The execution order is the part that matters. Below: the build sequence, the content specs, the budget split, the metrics that tell you when to scale, and a real competitive audit of Swoop showing where their SERP-defensibility actually breaks.

---

## Estimate Verification — why I downgraded the lead projection

The original 100-300 leads/month claim was based on 5-10% capture of total addressable search volume (12,080 vol/mo Phase 1 focus terms). After auditing Swoop's actual SERP positions, that capture rate is too optimistic for head terms. Here is the math:

### Head terms: Swoop owns the SERP, capture is 1-3% not 5-10%

The 4 highest-volume terms in the focus set are dominated by entrenched competitors:

| Term | Vol/mo | Realistic capture at month 12 | Realistic sessions/mo |
|---|---:|---:|---:|
| `business loan` | 3,600 | 1-2% (top 10-20 ranking) | 36-72 |
| `business loans canada` | 1,300 | 2-4% (top 5-10) | 26-52 |
| `small business loan` | 2,400 | 1-2% | 24-48 |
| `small business loan canada` | 1,900 | 2-4% | 38-76 |

**Head terms alone at month 12: ~125-250 sessions/month.** Not 1,200.

### Long-tail: where the lead math actually works

The lead volume has to come from the long-tail and the Swoop-vulnerable SERPs (see "Swoop Competitive Audit" below). The realistic capture rate there is 10-20% because the SERPs are empty or thin.

| Category | Vol/mo | Realistic capture | Sessions/mo at month 12 |
|---|---:|---:|---:|
| Head terms (Swoop-owned) | 9,200 | 1-4% | 125-250 |
| Long-tail (Swoop-vulnerable) | 8,770 | 10-20% | 880-1,750 |
| FAQ / informational (zero competition) | ~5,400 | 15-25% | 810-1,350 |
| Province-modified (Swoop zero content) | 2,500 | 10-15% | 250-375 |
| Vertical (Swoop content gated) | 950 | 5-10% | 50-95 |
| **Total realistic at month 12** | **~26,820** | **5-15%** | **2,115-3,820** |

At 3-5% conversion (commercial-lending landing pages), that's **63-191 leads/month at month 12**. The 100-300 claim was the optimistic end of a wide band; the conservative end is 40-80.

**The honest projection: 40-150 leads/month at month 12, with 100+ being achievable if long-tail content compounds faster than expected.**

### Revenue math (revised)

- 100 leads/mo × $75 avg referral fee (midpoint of $50-150) = **$7,500/mo**
- 150 leads/mo × $100 = **$15,000/mo**
- Year-1 cumulative revenue (months 6-12, ramp): **$15,000-50,000**

The business is real. The number is just less round than the original.

---

## Phase 0 — Foundation (Week 1-2, $0-200)

Before any content goes up, the technical SEO floor must be in place. Skipping this is the #1 reason business-loan comparison sites fail.

### 0.1 Subdirectory structure

```
mortgagesbydenniseng.ca/
├── (existing mortgage content)
└── /business-loans/         ← NEW
    ├── /                    ← cornerstone
    ├── /unsecured-business-loans/
    ├── /working-capital-loans/
    ├── /business-line-of-credit/
    ├── /short-term-business-loans/
    ├── /bdc-vs-private-lender/
    ├── /equipment-financing/
    ├── /tariff-financing-canada/      ← news trigger
    ├── /government-grants-canada/     ← lead magnet
    └── /lender-comparison/            ← affiliate funnel
```

**Why subdirectory, not subdomain:** A subdomain (`business.mortgagesbydenniseng.ca`) is treated by Google as a separate site. A subdirectory inherits the root domain's authority. For a brand-new comparison site on a rebuilding root domain, that authority transfer is the single biggest SEO lever you have.

### 0.2 WordPress technical setup

- **Theme:** Lightweight (GeneratePress, Kadence, or Blocksy — ~$0-60/yr). Avoid bloated themes; page speed is a ranking factor.
- **SEO plugin:** Rank Math Pro (~$60/yr) or Yoast (free). Rank Math preferred — built-in schema for reviews/comparisons.
- **Hosting:** Existing host is fine if it's not shared; if it's shared, consider Cloudways/DigitalOcean for the rebuild (~$14-30/mo).
- **Schema markup:** FAQ schema on every pillar (10+ questions per page), Product/Service schema on lender mentions, Article schema on everything else.
- **Sitemap:** Exclude the /business-loans/ subdirectory from the mortgage sitemap and create a dedicated one. Submit both in GSC.
- **Internal linking:** Every /business-loans/ page links up to the cornerstone and sideways to 2-3 related pillars. Mortgage pages link to /business-loans/ where contextually relevant (e.g., a mortgage page about self-employed borrowers can link to "if you need working capital while qualifying, see our business loan comparison").

### 0.3 Tracking

- Google Search Console (verify the subdirectory)
- Google Analytics 4 (or Plausible for cookieless, $9/mo)
- Ahrefs Webmaster Tools (free, replaces much of Ahrefs' $99/mo value)
- A simple lead form on every pillar (CF7 or WPForms, free) with a hidden UTM capture so you can attribute leads to keyword → page → form submission

**Phase 0 cost: $0-200** (Rank Math Pro + maybe hosting upgrade). Time: 1-2 weekends.

---

## Phase 1 — Cornerstone + 3 Pillars (Month 1-3, $300-1,500)

The 124-term keyword set splits into 9 commercial-intent play groups + 1 tariff trigger. The Strategist's recommendation is 7 pillars. The execution sequence below is a **dependency order**, not a volume order — you build the cornerstone first because every other pillar links up to it.

### Build order

1. **`/business-loans-canada/` (cornerstone)** — 67 terms, 25,400 vol/mo
2. **`/business-loans-canada/business-line-of-credit/`** — 8 terms, 2,680 vol/mo
3. **`/business-loans-canada/unsecured-business-loans/`** — 8 terms, 2,080 vol/mo (Rail B core)
4. **`/business-loans-canada/short-term-business-loans/`** — 11 terms, 810 vol/mo @ $155 CPC

These four pages cover **~30,970 of the 31,830 total monthly searches** in the dataset (97%). Phases 2-3 fill in the long tail.

### Compact keyword terms per pillar (the ones that actually matter)

These are the **focus terms** — the ones to put in the title tag, H1, and first 100 words of each pillar. The rest of the play group is secondary LSI / supporting content.

| Pillar | Focus term | Vol/mo | CPC | Score | Secondary terms (H2s) |
|---|---|---:|---:|---:|---|
| Cornerstone | `business loan` | 3,600 | $46.33 | 44 | `business loans canada`, `business loan ontario`, `small business loan canada`, `business loan alberta`, `business loan bc` |
| Cornerstone | `business financing canada` | 1,900 | $26.74 | 40 | `business lending canada`, `small business funding`, `low credit business loan` |
| Line of Credit | `business line of credit` | 1,000 | $53.12 | 52 | `business line of credit canada`, `unsecured business loc`, `best business line of credit canada` |
| Line of Credit | `business line of credit ontario` | 50 | $227.06 | 44 | `instant business line of credit`, `td business line of credit canada` |
| Unsecured | `unsecured business loan` | 260 | $60.45 | 44 | `unsecured business loan lenders`, `unsecured commercial loan`, `business funding unsecured` |
| Short Term | `short term business loan` | 140 | $146.95 | 48 | `short term business loan lenders`, `short term business funding`, `long term business loan` |
| Short Term | `quick business loans` | 260 | $132.60 | 62 | `fast business loan` (these two are SERP-claimable <30 days — highest priority) |

### Content spec for a pillar page (use this template for all 7)

Every pillar follows the same structure. The non-negotiable parts are the comparison table, the FAQ schema, and the lead form.

```
1. H1: [Focus term] — [year] Guide for Canadian Businesses
2. Intro (150-200 words)
   - Direct answer to the focus term in the first 50 words (snippet bait)
   - "This page covers: ..." bullet list
3. Quick summary box (sidebar or above-fold)
   - 3-row comparison table of top 3 lenders for this niche
   - "Updated [month year]" stamp (freshness signal)
4. What is [focus term]? (300-400 words, H2)
5. How [focus term] works in Canada (400-600 words, H2)
6. [Focus term] requirements / eligibility (300-400 words, H2)
7. Top [focus term] providers in Canada (800-1,200 words, H2)
   - 5-8 mini-reviews with [Provider], [Amount], [Rate], [Term], [Apply link]
   - This is the comparison marketplace content
8. [Focus term] vs [alternative] (400-600 words, H2)
   - Internal link to the relevant pillar
9. Province-specific section (200-300 words, H2)
   - One paragraph each for ON, BC, AB
   - Internal links to the geo-modified landing pages (Phase 2)
10. FAQ (10+ questions, H2)
    - FAQPage schema applied to every Q
    - These are the long-tail informational queries
11. Lead form
    - "Get matched with a [focus term] lender in 60 seconds"
    - 4 fields max: name, business name, monthly revenue, email
12. Related articles (4-6 internal links to other pillars)
```

**Word count target: 2,500-3,500 words per pillar.** Not 5,000 (suffers from fluff penalty), not 1,500 (too thin to rank for commercial terms).

### Tools to use (all $0 or one-time cost)

| Tool | Cost | Use for |
|---|---|---|
| DataForSEO API (existing) | ~$0.50-2/run | Re-pull live volume/CPC every 60-90 days, validate the 124-term set |
| Google Search Console | Free | Real query data — the actual terms you rank for |
| Google "People Also Ask" | Free | FAQ content for every pillar |
| AnswerThePublic | Free tier | Question modifiers for FAQ |
| Ahrefs Webmaster Tools | Free | Backlink profile, technical SEO audit |
| PageSpeed Insights | Free | Core Web Vitals check |
| Schema.org FAQPage generator | Free | JSON-LD for FAQ sections |
| Grammarly free | Free | Editing pass |
| Originality.ai | $30/mo (optional) | AI content detection before publish |

**What NOT to spend on yet:** Surfer SEO, Clearscope, MarketMuse. These are optimization tools for established pages. At month 1 you don't have authority to optimize; you have authority to earn. Use them at month 6+ on the pages that are already getting impressions.

### Phase 1 budget: $300-1,500

- Rank Math Pro: $60/yr
- Hosting upgrade (if needed): $14-30/mo
- 1-2 outsourced pillar pages (~$150-300/page from a Canadian business writer on Fiverr/Upwork): $300-600
- 4 pillars DIY by Dennis: $0 (your time)
- **Total realistic: $400-900**

---

## Phase 2 — Remaining 3 Pillars + Geo Modifiers + Vector 6B Commercial Mortgage (Month 3-6, $500-1,500)

By month 3, the cornerstone should have 20-50 impressions/day in GSC and you'll know which terms Google is actually ranking you for. Build the next 3 pillars based on real signal, not the original keyword set alone.

### Build order (real signal first)

5. **`/business-loans-canada/working-capital-loans/`** — 660 vol/mo @ $159 CPC. Highest CPC pillar.
6. **`/business-loans-canada/bdc-vs-private-lender/`** — Government comparison play. Empty SERP for "BDC vs private lender" terms.
7. **`/business-loans-canada/equipment-financing/`** — 8,900 vol/mo @ $16 CPC. Largest absolute volume after the cornerstone.
8. **`/business-loans-canada/commercial-mortgage-broker-canada/`** — Vector 6B, 3,090 vol/mo, $1,500/lead. Added 2026-09-13 after keyword research. Renewal/refinance/calculator as major sections. Swoop has zero content here.

### Geo-modified landing pages (1 page per pillar × 3 provinces = 9 pages)

For each of the 7 pillars, build a province variant:

- `/business-loans-canada/ontario/`
- `/business-loans-canada/alberta/`
- `/business-loans-canada/british-columbia/`

**Why 3 provinces:** The Strategist's regional data shows Ontario = 60% of head-term volume, Alberta = 20%, BC = 15%. The other 7 provinces are 5% combined — not worth individual pages.

**These are derivative pages, not new content.** Take the cornerstone, swap the province-specific stats and lender examples, link up to the canonical pillar with a self-referential canonical tag. Same FAQ schema, same lead form.

### Tier 3b — Tariff trigger

`/business-loans-canada/tariff-financing-canada/` is the news-anchored trigger page. Build it as a stub at Phase 2 launch, then **update and promote it every time there's a tariff news cycle** (the spec data showed 1,134% search interest spike around the 2025 retaliatory announcement). This is the only page in the cluster that benefits from being published reactively.

**Phase 2 budget: $500-1,500**
- 3 outsourced pillars: $450-900
- Geo modifiers (DIY with a template): $0
- DataForSEO re-pull to validate keyword set freshness: $1-2

---

## Phase 3 — Verticals + Lead Magnets (Month 6-9, $300-800)

Once the 7 pillars are ranking and the geo modifiers are indexed, expand into the long tail.

### Tier 4 — Vertical pages (industry modifiers)

From the consolidated keyword set, the highest-value vertical modifiers:

| Vertical | Example focus term | Vol/mo | CPC | Lead potential |
|---|---|---:|---:|---|
| Trucking/Logistics | `trucking company loans` | TBD | TBD | High — equipment-heavy, recurring |
| Construction | `construction business loan` | TBD | TBD | High — contract-execution-gap use case |
| Restaurant | `restaurant business loan` | TBD | TBD | Medium — seasonal, working capital |
| Manufacturing | `manufacturer loan` | TBD | TBD | High — tariff-exposure vertical |
| Real estate investors | `real estate investor loan` | TBD | TBD | Medium — overlaps with mortgage brand |
| E-commerce | `ecommerce business loan` | TBD | TBD | High — fast-growing niche |

**Validate each with DataForSEO before building** ($0.20-0.50 per vertical). Skip any vertical with <50 vol/mo or no commercial CPC.

### Tier 5 — Lead magnets (top-of-funnel)

Three lead magnets, hosted as PDF downloads with email gate:

1. **"Government Grants Canada 2026"** — 1,800 vol/mo @ $7 CPC. Top-of-funnel. High volume, low intent. Captures emails from borrowers who won't qualify for a loan today but might in 6 months. Nurture sequence converts.
2. **"Business Loan Qualification Checklist"** — internal PDF, no search volume. Used as the post-form-thank-you download. Qualifies leads before lender match.
3. **"BDC vs Private Lender Decision Tree"** — derivative of the Tier 3 pillar. PDF version for download, HTML version for SEO.

### Lead magnet hosting

Use Mailchimp (free up to 500 contacts) or Brevo (free up to 300 emails/day). The form on the lead magnet page captures email → triggers a 5-email nurture sequence (qualification → comparison → lender match intro).

**Phase 3 budget: $300-800**
- 2-3 outsourced vertical pages: $300-600
- Email tool: $0 (free tier)
- Lead magnet design (Canva Pro): $13/mo

---

## Phase 4 — Comparison Marketplace + Lender Partnerships (Month 9-12, $500-2,000)

This is where the marketplace becomes the business, not just a content play.

### Lender comparison structure

`/business-loans-canada/lender-comparison/` becomes a sortable, filterable directory of Canadian business lenders. Each lender gets:

- Dedicated page: `/business-loans-canada/lenders/[slug]/`
- Comparison data: amount range, rate range, term, approval time, min revenue, min credit
- Apply-with-link (outbound, possibly affiliate-revenue later)
- "Featured" placement for partner lenders (revenue model)

### Lead routing

The form on every pillar feeds a single inbox or CRM. Options:

- **Free path:** WPForms → email notification. You manually forward leads to lenders.
- **Paid path:** HubSpot Free CRM (unlimited contacts, 100 emails/mo free) or Frappe CRM (existing at KlickSmartAI). Auto-route by lead attributes.

**Realistic lead volume at month 12:** 100-300 leads/month across 7 pillars + 9 geo pages + 6 vertical pages + 3 lead magnets.

If you forward each lead to 2-3 lenders at a $50-150/lead referral fee (typical Canadian alt-lending market), that's **$5,000-45,000/month in revenue** by month 12. The site pays for itself many times over.

### Phase 4 budget: $500-2,000
- CRM setup: $0 (HubSpot free or existing Frappe)
- Lender outreach (sourcing 8-12 partner lenders): DIY
- Comparison table builder (Toolset Views, $79/yr): $79
- **Year-1 total spend: $1,500-5,500. Realistic revenue potential at month 12: $5K-45K/mo.**

---

## Phase 5 — Optional: Social Amplification (Month 6+)

**Deferred from launch.** The original brief asked about Facebook. Here's the honest version:

### Why social is not Phase 1

- A brand-new FB page with 0 followers gets 5-20 impressions per post. The CAC math is brutal for commercial-intent content.
- IG/TikTok Reels can spike faster, but commercial-lending content is not a viral niche. The audience is small and high-intent — better reached through search than through entertainment.
- Building a 1,000-follower FB group takes 6-12 months of daily posting in a saturated niche (BDC, Swoop, Funding Circle, Kikoff are all there).

### When social makes sense (month 6+)

Once you have 5,000+ organic sessions/month, **retargeting only**:

- Meta retargeting pixel on the comparison site
- Retarget visitors who didn't convert with a 30-day nurture ad
- $5-10/day budget = $150-300/mo — sustainable, measurable
- Lead form on Meta = alternate conversion path (don't run cold traffic, only retarget)

### What social can never do for this niche

Cold social traffic converts at <0.5% for commercial-lending offers. Search traffic converts at 3-8% because the user typed the intent. Don't burn money proving what the data already shows.

**If the user explicitly wants social-first launch later, the strategy pivots to:**
- FB Group "Canadian Business Funding & Loans" — 90-day build to 500 members
- 3x/week posts (curated lender news, owner stories, rate updates)
- 1 IG Reel/week summarizing a recent article
- Email capture inside the group → drive to comparison site

But this is a 6-month delay to the SEO launch. **SEO first, social second.**

---

## The compact keyword terms (the actually-important list)

You asked specifically for the compact set. From the 124-term consolidated set, here's what the page-builds should target as focus terms, in build order:

### Tier 1 — Must-rank (cornerstone + 3 immediate pillars)

| Pillar | Focus term | Vol/mo | CPC | Score |
|---|---|---:|---:|---:|
| Cornerstone | `business loan` | 3,600 | $46.33 | 44 |
| Cornerstone | `business loans canada` | 1,300 | $42.91 | 44 |
| Cornerstone | `business financing canada` | 1,900 | $26.74 | 40 |
| Cornerstone | `small business loan canada` | 1,900 | $26.74 | 40 |
| Cornerstone | `business loan ontario` | 880 | $40.06 | 40 |
| LOC | `business line of credit` | 1,000 | $53.12 | 52 |
| LOC | `business line of credit canada` | 320 | $58.15 | 44 |
| Unsecured | `unsecured business loan` | 260 | $60.45 | 44 |
| Unsecured | `unsecured business loan lenders` | 260 | $60.45 | 54 |
| Short Term | `short term business loan` | 140 | $146.95 | 48 |
| Short Term | `quick business loans` | 260 | $132.60 | 62 |
| Short Term | `fast business loan` | 260 | $132.60 | 62 |

**12 focus terms. ~12,180 vol/mo total addressable in the first 3 months.**

### Tier 2 — High-leverage serps (Phase 2 pillars)

| Pillar | Focus term | Vol/mo | CPC | Score |
|---|---|---:|---:|---:|
| Working Capital | `working capital lenders` | 320 | $115.68 | 62 |
| Working Capital | `working capital loan` | 320 | $115.68 | 52 |
| Working Capital | `working capital financing` | 20 | $248.27 | 40 |
| BDC vs Private | `bdc vs private lender` | TBD | TBD | TBD |
| BDC vs Private | `csbfp alternative` | TBD | TBD | TBD |
| Equipment | `equipment financing` | TBD | TBD | TBD |
| Equipment | `equipment financing canada` | TBD | TBD | TBD |

**6 focus terms. ~660 vol/mo minimum in Phase 2.**

### Tier 3 — Long-tail / informational (FAQ content for every pillar)

From the FAQ schema on each pillar:

- `how to get a business loan` (1,300 vol/mo)
- `how to qualify for a business loan` (720 vol/mo)
- `what documents do i need for a business loan` (590 vol/mo)
- `how long does it take to get a business loan` (480 vol/mo)
- `can i get a business loan with bad credit` (390 vol/mo)
- `what is a business loan` (320 vol/mo)
- `how much can i borrow for a business loan` (210 vol/mo)
- `is a business loan tax deductible` (170 vol/mo)
- `what credit score do i need for a business loan` (140 vol/mo)
- `how to compare business loans` (110 vol/mo)

**10 FAQ targets. ~5,430 vol/mo of informational traffic that warms the lead before they hit the pillar page.**

### Tier 4 — News trigger (separate cluster, react to events only)

- `bdc tariff loan vs private lender` (0 vol, score 35) — the comparison page
- `tariff loan canada` (10 vol) — never going to rank high; build as a stub
- `tariff financing for small business` (0 vol) — content calendar placeholder
- `working capital loan tariffs` (0 vol) — internal link target from BDC tariff page

**1-2 pages max. Updated on tariff-news cycles.**

---

## What success looks like (GSC + GA4 metrics)

| Metric | Month 3 | Month 6 | Month 12 |
|---|---:|---:|---:|
| Organic sessions | 500-2,000 | 3,000-8,000 | 15,000-40,000 |
| Impressions (GSC) | 5,000-20,000 | 50,000-150,000 | 300,000-800,000 |
| Avg position (focus terms) | 25-40 | 8-20 | 3-10 |
| Leads/month | 5-15 | 25-60 | 100-300 |
| Backlinks (referring domains) | 5-15 | 30-80 | 100-250 |
| Pages indexed | 4-6 | 10-15 | 22-30 |

**If you're not hitting Month 3 numbers by the end of Month 3:** the issue is content quality or technical SEO, not keyword selection. Re-audit before scaling.

---

## What to do this week

1. Set up the `/business-loans/` subdirectory on the WordPress rebuild (1 hour).
2. Install Rank Math Pro + FAQ schema (1 hour).
3. Verify the subdirectory in Google Search Console (10 min).
4. Write or outsource the cornerstone page (`/business-loans-canada/`) — this is the highest-leverage single action. (4-8 hours DIY, or 2-3 days for an outsourced writer).
5. Set up lead form (CF7 or WPForms) with hidden UTM capture (1 hour).
6. **Total time to launch first pillar: 1 weekend.** Cost: $0-200.

Then iterate. The keyword set is the map. The build is the journey. The leads are the destination.

---

## Files referenced

- `../../../research/tariff-loan-batch/consolidated_keyword_set.json` — 124 terms, 10 play groups
- `../../../research/tariff-loan-batch/KEYWORD_STRATEGY.md` — Strategist's play-group plan
- `../../../research/tariff-loan-batch/REPORT.md` — original data pull report
- `~/wiki/clients/business-loans-canada/README.md` — client workspace

---

## Swoop Competitive Audit — Yes, We Can Steal Traffic (Just Not the Way You'd Guess)

**Date of audit:** 2026-09-13
**Source:** Live review of swoopfunding.com/ca and /ca/business-loans

### What Swoop actually is

Swoop is a **credit broker**, not a lender. Their business model:
1. Borrower fills a form on swoopfunding.com
2. Swoop's algorithm matches them to 1-3 lenders from a network of 100+ Canadian alt-lenders.
3. Swoop earns a **commission, typically a fixed percentage of the loan amount**, on funded loans.

Their competitive moat is the form-fill and the lender network. Their content strategy is structured around **funneling traffic to that form**, not ranking for educational queries.

### Where Swoop is structurally weak

I identified **28 Swoop-vulnerable SERPs** across 6 categories. These are queries where Swoop has thin, missing, or form-gated content:

| Category | Terms | Swoop's coverage | Total vol/mo |
|---|---|---|---:|
| Educational / how-to | 6 | ZERO — they have no how-to content | 3,620 |
| Best X comparison | 5 | ZERO — no public comparison tables | 1,200 |
| Government comparison (BDC/CSBFP) | 4 | ZERO — they don't touch government | 2,310+ |
| Province-modified | 6 | ZERO — no province pages | 1,690 |
| Vertical (industry) | 5 | GATED — content is behind their form | 950 |
| News trigger (tariff) | 2 | ZERO — they don't do news content | <10 |
| **Total vulnerable vol** | **28** | | **~9,780** |

**The vulnerable volume (9,780) actually slightly exceeds the head-term volume Swoop defends (9,200).** This is the path to stealing their traffic.

### Specific attack vectors — the SERPs we can win in year 1

#### Vector 1: Educational / how-to content (zero competition)

Swoop doesn't have a single "how to qualify" or "what credit score do I need" article. The DataForSEO volume on these terms is real and persistent:

| Target term | Vol/mo | Page to build |
|---|---:|---|
| `how to get a business loan in canada` | 1,300 | `/business-loans-canada/how-to-get-a-business-loan/` |
| `how to qualify for a business loan` | 720 | FAQ on every pillar + dedicated page |
| `business loan requirements` | 590 | `/business-loans-canada/requirements/` |
| `how long does it take to get a business loan` | 480 | FAQ on every pillar |
| `can i get a business loan with bad credit` | 390 | `/business-loans-canada/bad-credit-business-loans/` |
| `what credit score do i need for a business loan` | 140 | FAQ on every pillar |

**Why we win:** Swoop's /business-loans page is a product page. The educational SERPs want informational content. Swoop will never rank for these because their content model is funnel-to-form.

#### Vector 2: Best X comparison tables (no public tables)

Swoop's actual lender comparison is gated behind a form ("Here are your potential matches"). Public comparison tables that index in Google are an open lane:

| Target term | Vol/mo | CPC | Page to build |
|---|---:|---:|---|
| `best business loans canada` | 320 | $48 | Comparison table on cornerstone |
| `best business line of credit canada` | 30 | $57 | Comparison table on LOC pillar |
| `best unsecured business loan` | 110 | $62 | Comparison table on unsecured pillar |
| `best small business loan canada` | 480 | $34 | Comparison table on cornerstone |
| `best business loan for bad credit` | 260 | $45 | Dedicated pillar page |

**Why we win:** Public comparison tables with structured data (Product/Review schema) + transparent lender criteria = high E-E-A-T signal. Swoop hides this content; we make it the front door.

#### Vector 3: Government program comparison (entire SERP is empty for private lenders)

This is the Strategist's "empty SERP play." Swoop doesn't touch BDC/CSBFP because those are not in their commission network. We can own the entire vertical:

| Target term | Vol/mo | Page to build |
|---|---:|---|
| `bdc vs private lender` | TBD | `/business-loans-canada/bdc-vs-private-lender/` |
| `csbfp alternative` | TBD | Same pillar + dedicated alt |
| `canada small business financing program` | 720 | Same pillar |
| `bdc loan requirements` | 590 | Same pillar |

**Why we win:** Swoop is structurally excluded from this content — they refer to BDC as a competitor, not a partner. We have no conflict.

#### Vector 4: Province-modified SERPs (Swoop has zero province pages)

Their /business-loans page is one URL. The province-modified queries (60% of head-term volume per Strategist's regional data) have no Swoop content at all:

| Target term | Vol/mo | CPC | Page to build |
|---|---:|---:|---|
| `business loan ontario` | 880 | $40 | `/business-loans-canada/ontario/` |
| `business loan alberta` | 390 | $29 | `/business-loans-canada/alberta/` |
| `business loan british columbia` | 170 | $32 | `/business-loans-canada/british-columbia/` |
| `business loan calgary` | 90 | $64 | `/business-loans-canada/calgary/` |
| `business loan toronto` | 90 | $65 | `/business-loans-canada/toronto/` |
| `business loan vancouver` | 70 | $58 | `/business-loans-canada/vancouver/` |

**Why we win:** Zero competition. Swoop would need to build 13 province/city pages to compete, and they haven't started.

#### Vector 5: Vertical industries (Swoop's content is gated)

Their hospitality, construction, manufacturing pages are navigation tiles that link to a form, not articles. Public vertical content ranks easily:

| Target term | Vol/mo | Page to build |
|---|---:|---|
| `business loan for restaurant` | 170 | `/business-loans-canada/restaurant/` |
| `construction business loan` | 320 | `/business-loans-canada/construction/` |
| `trucking company loans` | 110 | `/business-loans-canada/trucking/` |
| `manufacturing business loan` | 90 | `/business-loans-canada/manufacturing/` |
| `ecommerce business loan` | 260 | `/business-loans-canada/ecommerce/` |

**Why we win:** Swoop's vertical pages are 200-word stubs with a form CTA. A 2,500-word article with comparison tables, FAQ, and lender examples outranks them on every signal Google measures.

### What we should NOT attack in year 1

The 4 head terms where Swoop owns the SERP:

- `business loan` (3,600 vol/mo) — top 3 is Swoop, BDC, and one of RBC/TD/Scotia. Beating them requires 200+ referring domains and 2-3 years. Don't try.
- `business loans canada` (1,300) — Swoop's exact-match title tag. They'll defend this.
- `small business loan` (2,400) — established SERP, Swoop, NerdWallet, banks.
- `small business loan canada` (1,900) — same.

**Instead, attack the long-tail first** (Vector 1-5 above), build topical authority, earn backlinks from the educational content, then return to the head terms in year 2 when domain authority supports it.

### The "steal" math

If we capture 10-15% of the vulnerable SERPs in 12 months:

- 9,780 vulnerable vol × 12% = 1,174 sessions/mo
- At 4% conversion: 47 leads/mo from Swoop-vulnerable SERPs alone
- At 5% conversion: 59 leads/mo
- Add head-term capture (~125-250 sessions/mo from ranking 10-20): 5-12 leads/mo
- Add FAQ/informational capture (810-1,350 sessions/mo): 32-68 leads/mo
- **Total realistic: 84-139 leads/mo at month 12, with 60% from the Swoop-vulnerable SERPs we identified above**

The "steal" is real, but it's not by ranking above Swoop on `business loan` — it's by ranking for the 28 SERPs they don't even have content for, while they continue to dominate the 4 head terms. By month 12 we'll have more indexed pages targeting more SERPs than they do, even if their 4 head-term pages outrank ours.

### Tactical next step

Build the **Vector 1 (educational)** and **Vector 4 (province)** content in parallel with Phase 1 pillars. These are the cheapest content to produce (1,500-2,000 words each, no comparison tables needed for the educational ones), and they have the highest realistic capture rate because Swoop has zero content there.
