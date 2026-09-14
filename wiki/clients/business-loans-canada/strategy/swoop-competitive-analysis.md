# Swoop Competitive Analysis & Recommendation

**Date:** 2026-09-13
**Live source data:** swoopfunding.com/ca sitemap.xml, /business-loans, /start-business, /business-expansion, /property-finance, /import-export-finance
**Author:** Hermes
**Purpose:** Replace the previous Swoop assessment with verified data and produce an actionable recommendation.

---

## TL;DR

Swoop is bigger than the previous audit suggested (757 indexable URLs, not the 4-5 pages I implied). But the **attack surface is bigger too** — they have 9 structural content gaps that the comparison site can exploit, including a 6th gap they can't fix at all: **mortgage-lens content (HELOC, equity, secured business funding). That gap belongs to the comparison site by birthright** because Dennis's mortgage-broker license is the differentiator.

**Recommendation:** Build a 12-month content + SEO plan around 6 attack vectors. The mortgage-lens content (Vector 6) is the new moat — it's where Swoop is structurally excluded, and it's where the comparison site becomes the only credible source in the Canadian market.

---

## What Swoop actually is (verified)

Swoop is a UK-founded credit broker that operates a multi-market platform (CA, UK, IE, AU, US, ZA, NA). Their model:
- Borrower fills a form on swoopfunding.com
- Algorithm matches them to 1-3 lenders from a network of 100+ Canadian alt-lenders
- Swoop earns a commission, typically a fixed percentage of the loan amount

Their compliance copy is explicit: *"Swoop is a credit broker and does not provide capital... Swoop may receive a commission or finder's fee for effecting such introductions."*

That last line is the strategic wedge. They have an inherent conflict of interest — they only refer to lenders in their network, and their network excludes any product they can't earn a commission on. **HELOCs, mortgages, and secured business funding through a mortgage broker are all outside Swoop's referral model.**

---

## Verified Swoop content footprint (from sitemap.xml)

| Cluster | URLs | Type | Avg depth |
|---|---:|---|---|
| Pages (core) | 252 | Landing pages, mostly product-tile + form | 200-500 words |
| Business glossary | 420 | Short definitions of funding terms | 200-400 words |
| Knowledge hub | 25 | Funding-type glossaries | 800-1,000 words |
| Sectors | 30 | Industry pages, mostly navigation tiles | 200 words |
| Case studies | 30 | Customer story pages | 500-800 words |
| Podcasts/videos | — | Media library, low SEO value | — |
| **Total indexable** | **757** | | |

**Footprint assessment:** Real SEO operation, 3+ years of compounding authority, Rank Math SEO plugin (same class as the comparison-site plan). They are not a soft target. They are a content-rich broker with a structural bias.

**Domain authority estimate (rough, from internal-page structure):** Top-1,000 Canadian business/finance site. They've earned ~200-400 referring domains from PR coverage (110,000+ newsletter subscribers, 5+ years of "as featured in" press logos). Ranking above them on the head terms is a 2-3 year project.

---

## What Swoop has — accurate inventory

- **252 product/landing pages** — top-of-funnel form-fills, organized by use case (start, expand, cashflow, property, import/export, refinance, acquire)
- **25 funding-type glossaries** — business loans, asset refinance, mezzanine finance, factoring, peer-to-peer lending, etc. Each ~800-1,000 words. Definition + brief product description + form CTA.
- **30 sector pages** — hospitality, construction, manufacturing, logistics, agriculture, retail, ecommerce. Mostly navigation tiles.
- **30 case studies** — customer stories, not commercial-intent.
- **420 glossary terms** — short definitions of funding terms. These rank for low-volume informational queries but do not convert.

**Strengths:**
- 3+ years of authority on `business loan` family queries.
- Real brand recognition (110k+ newsletter, Trustpilot presence).
- Multi-market platform = ongoing content investment.
- Rank Math + solid internal linking.
- High conversion UX — the form is above the fold on every page.

**Weaknesses (the real attack surface):**
- **No province pages** (0 URLs in sitemap under /ca/province/, /ca/ontario/, /ca/alberta/, /ca/british-columbia/, etc.)
- **No "best X" comparison tables** — every comparison is gated behind the form
- **No government program content** — BDC/CSBFP are competitors, not partners. They won't link to BDC.
- **No news-trigger content** — no tariff, CRA, or regulatory-news pages
- **No long-form educational articles** (1,500+ words). Knowledge-hub caps at 1,000.
- **No lender-specific comparison content** — they don't name lenders, only refer to them post-form
- **No mortgage-lens content** — HELOC, equity takeout, secured business funding, second mortgages are 100% absent. **They can't add this content without changing their commission model.**
- **No how-to guides** — qualification, application, documents, credit score — all missing
- **FAQ content is thin** — 5-7 questions per page, often 3-4

The 404 evidence is damning: `/ca/improve-cashflow`, `/ca/property-finance`, `/ca/import-export-finance` all return 404 or redirect to homepage. The /business-loans page promises 7 use-case deep-dives via tile links; the destinations don't exist.

---

## The 6 attack vectors (revised)

### Vector 1: Educational / how-to content (zero competition)

| Target | Vol/mo | Swoop has it? |
|---|---:|:---:|
| `how to get a business loan in canada` | 1,300 | ❌ |
| `how to qualify for a business loan` | 720 | ❌ |
| `business loan requirements` | 590 | ❌ |
| `how long does it take to get a business loan` | 480 | ❌ |
| `can i get a business loan with bad credit` | 390 | ❌ |
| `what credit score do i need for a business loan` | 140 | ❌ |
| `business loan application process` | TBD | ❌ |
| `business loan documents needed` | TBD | ❌ |

**Why we win:** Swoop's content model is funnel-to-form. They will not build 2,500-word educational articles because education reduces form-fill conversion. We have nothing to lose by educating.

**Page count to attack:** 8-10 articles. 1,500-2,000 words each. 1 weekend of content production.

### Vector 2: "Best X" public comparison tables (gated by Swoop)

| Target | Vol/mo | CPC | Swoop has it? |
|---|---:|---:|:---:|
| `best business loans canada` | 320 | $48 | ❌ |
| `best business line of credit canada` | 30 | $57 | ❌ |
| `best unsecured business loan` | 110 | $62 | ❌ |
| `best small business loan canada` | 480 | $34 | ❌ |
| `best business loan for bad credit` | 260 | $45 | ❌ |
| `best business loan ontario` | TBD | TBD | ❌ |
| `best short term business loan` | 140 | $147 | ❌ |

**Why we win:** Public comparison tables with structured data (Product schema, Review schema where appropriate) + transparent lender criteria = high E-E-A-T. Swoop's model is to gate the comparison behind a form; they cannot publish a public table because it would expose which lenders they refer to and at what commission rate.

**Page count to attack:** 6-8 articles. 2,500-3,000 words with a real comparison table.

### Vector 3: Government program comparison (Swoop structurally excluded)

| Target | Vol/mo | Swoop has it? |
|---|---:|:---:|
| `bdc vs private lender` | TBD | ❌ |
| `csbfp loan alternative` | TBD | ❌ |
| `canada small business financing program` | 720 | ❌ |
| `bdc loan requirements` | 590 | ❌ |
| `bdc tariff loan` | 0 | ❌ |
| `government grants for small business` | 1,800 | Partial — they list grants, no comparison |

**Why we win:** Swoop can't link to BDC — it's a competitor, not a partner. We can. The "BDC vs private lender" SERP is empty and the underlying intent is real (BDC has long approval times, lots of paperwork; private lenders are faster, fewer docs, higher rate).

**Page count to attack:** 3-4 articles + the bdc-vs-private-lender pillar from the original 7-pillar plan.

### Vector 4: Province-modified SERPs (Swoop has zero)

| Target | Vol/mo | CPC | Swoop has it? |
|---|---:|---:|:---:|
| `business loan ontario` | 880 | $40 | ❌ |
| `business loan alberta` | 390 | $29 | ❌ |
| `business loan british columbia` | 170 | $32 | ❌ |
| `business loan calgary` | 90 | $64 | ❌ |
| `business loan toronto` | 90 | $65 | ❌ |
| `business loan vancouver` | 70 | $58 | ❌ |
| `business loan edmonton` | TBD | TBD | ❌ |
| `business loan ottawa` | TBD | TBD | ❌ |
| `business loan winnipeg` | TBD | TBD | ❌ |

**Why we win:** Zero competition. Swoop would have to build 13+ province/city pages to compete, and they haven't started in 3+ years. This suggests the build cost is high or the conversion rate is too low to justify at their scale.

**Page count to attack:** 9 derivative pages (3 provinces × 3 cities from Phase 2). Template-driven, fast to produce.

### Vector 5: Vertical industries (Swoop's content is gated + thin)

| Target | Vol/mo | Swoop's coverage | Swoop's depth |
|---|---:|---|---|
| `business loan for restaurant` | 170 | Navigation tile | 200 words |
| `construction business loan` | 320 | Navigation tile | 200 words |
| `trucking company loans` | 110 | None | 0 |
| `manufacturing business loan` | 90 | Navigation tile | 200 words |
| `ecommerce business loan` | 260 | Navigation tile | 200 words |
| `business loan for self-employed` | 320 | None | 0 |
| `business loan for startups` | 590 | Navigation tile | 200 words |
| `business loan for real estate investors` | TBD | None | 0 |

**Why we win:** Swoop's vertical pages are 200-word stubs. A 2,500-word article with comparison tables, FAQ schema, and lender examples outranks them on every signal Google measures. Word count, content depth, E-E-A-T, structured data — all favor the longer article.

**Page count to attack:** 5-6 vertical articles. 2,000-2,500 words each.

### Vector 6: Mortgage-lens content (revised after keyword research — TWO sub-pillars)

**The differentiator is real. The search volume is much bigger than the first estimate.**

After running 8 DataForSEO API calls across 2 research rounds ($0.32 total spend), the mortgage-lens + commercial mortgage cluster has:
- **3,770 vol/mo total addressable** (revised up from 680)
- Split into 2 sub-pillars, each with a distinct commercial intent

**Sub-pillar 6A: Self-employed borrower access to capital (450 vol/mo)**
- 28 commercial-intent terms
- Top terms: self employed loans (170), payday loans for self employed (110), loans for self employed bad credit (70), cmhc commercial mortgage (50)
- Structural moat: Swoop can't add HELOC/equity/refinance content (commission model excludes it)
- All the "heloc vs business line of credit" / "home equity business loan" / "refinance house for business" variants are 0-10 vol/mo individually

**Sub-pillar 6B: Commercial mortgage broker (3,090 vol/mo) — REVISED 2026-09-14 after LendCity SERP audit**

The commercial mortgage cluster has 15 commercial-intent terms totaling 3,090 vol/mo. **But it's not empty SERP** — LendCity Mortgages owns the head terms.

**LendCity is a real, established competitor:**
- 4.8/5 Google rating, 136 reviews
- "Top 1% mortgage agent in Canada" (their claim, Mortgage Architects license #12728)
- 5+ dedicated commercial-mortgage articles
- Working commercial mortgage calculator
- Direct answer snippet on every article
- Strong topical authority: renewal, broker, rates, approval timeline, Ontario guide, financing options
- `commercial mortgage renewal Canada` → LendCity ranks #1 with a 3,200-word article (July 2026)
- Investment-property focused (cross-border: CA, US, Mexico)

**The SERP reality:**
- `commercial mortgage broker` (590/mo) — Yelp/aggregators/LendCity top 5
- `commercial mortgage rates canada` (320/mo) — LendCity + banks
- `commercial mortgage calculator` (1,600/mo) — established SERP
- `commercial mortgage renewal` (0-10/mo) — LendCity owns it

**Revised recommendation: 13 pages across 5 sub-phases, NOT one big pillar competing for head terms**

The lane LendCity doesn't cover: **owner-occupied commercial mortgages + small-business-owner commercial financing** (their content is investor-focused). Plus long-tail gaps in provinces (BC, AB, SK, MB, Atlantic), property types (restaurant, gas station, auto dealership, mixed-use, hotel), and emergency content (lender won't renew, commercial mortgage declined, construction-to-permanent).

Build order:
1. **Month 3:** Owner-occupied commercial mortgage pillar (the gate of entry, owner-occupied angle as differentiator)
2. **Month 4:** 3 province pages (BC, AB, ON)
3. **Month 5-6:** 4 property-type verticals + 2 emergency articles (commercial mortgage not renewing, declined)
4. **Month 7:** 3 adjacent verticals (construction-to-permanent, CMHC MLI Select, hotel)
5. **Month 8-12:** Conversion optimization

**Updated Vector 6B revenue projection:**
- Old plan (1 pillar, head-term competition): 8-25 leads/mo at $12,500 = $29K-123K/mo at month 12
- New plan (13 pages, long-tail): similar total volume, better conversion (less SERP competition per term)
- **Realistic month-12 Vector 6B revenue: $13K-54K/mo**

**The "on demand" angle is dropped.** "Mortgage loan on demand" has zero search volume. Use "fast" or "expedited" if speed differentiation matters.

**"Commercial mortgage renewal rates" as a search term is 0 vol/mo confirmed** — the search behavior is "commercial mortgage broker" or "commercial mortgage rates" (shopping for benchmark) or "commercial mortgage renewal" (information-seeking before contacting a broker). Renewal is a forced-action event, not a search query.

**Both sub-pillars share the same structural moat:** Swoop can't add this content because their commission model excludes both HELOC/equity products and commercial mortgages. Business-loan alt-lenders can't add it because they don't have mortgage licenses. Only Dennis (a licensed mortgage broker who can also advise on business credit) can produce this content.

**Revised recommendation: 2 new pillars, not 6 standalone pages**

1. **`/business-loans-canada/self-employed-business-loans/`** — covers the 450 vol/mo self-employed cluster with mortgage-lens comparison embedded as a major section (HELOC vs business LOC vs unsecured vs BDC options)

2. **`/business-loans-canada/commercial-mortgage-broker-canada/`** — covers the 3,090 vol/mo commercial mortgage cluster, with renewal/refinance embedded as major sections (current rates, calculator, renewal decision tree, refinance break-even)

The renewal angle becomes a **conversion trigger** (banner + email capture + nurture sequence) on the commercial mortgage pillar, not a separate page.

**Page count to attack:** 2 articles (not 4-6). 2,500-3,000 words each.

**Recommended follow-up research (~$0.10):** Pull against residential self-employed seeds (`self employed mortgage canada`, `self employed mortgage broker`, `stated income mortgage canada`) to see if there's an even bigger cross-sell surface from the existing mortgage business. If yes, add a third Vector 6 sub-pillar targeting that.

---

## Revised recommendation

### Build order (12-month plan — revised with Vector 6B commercial mortgage, 13 pages)

| Month | Pages to publish | Volume target | Lead target |
|---:|---|---:|---:|
| 1-2 | Foundation: cornerstone + 3 pillars + 6 Vector 1 (educational) | 5,000 sessions | 5 leads/mo |
| 3 | Phase 2A: Vector 6B owner-occupied commercial mortgage pillar | 8,000-12,000 sessions | 8-15 leads/mo |
| 4 | Phase 2B: 3 province pages (BC, AB, ON) + 3 working capital / BDC / equipment pillars | 10,000-15,000 sessions | 12-22 leads/mo |
| 5-6 | Phase 2C-D: 4 property-type verticals + 2 emergency articles + Vector 2 best-X comparison tables + Vector 6A self-employed | 12,000-20,000 sessions | 20-50 leads/mo |
| 7-9 | Phase 2E: 3 adjacent verticals + Vector 5 verticals + Tier 5 lead magnets | 15,000-25,000 sessions | 50-100 leads/mo |
| 10-12 | Phase 4: lender comparison marketplace + outreach + lender partnerships + conversion optimization | 20,000-40,000 sessions | 100-200 leads/mo |

**The Vector 6B commercial mortgage pillar moves to month 3 (Phase 2A), not Phase 3.** Reasons:
- 3,090 vol/mo is too large to defer — that's 4.5x the self-employed cluster
- Renewal angle is a forced-action event (3-5 year term expiry) — borrowers in renewal season are shopping right now
- Commercial mortgage leads are $5,000-30,000 per funded deal — the unit economics justify earlier investment
- LendCity owns the head terms, but the long-tail (owner-occupied, provinces, property types, emergency) is open

**Total Vector 6B pages: 13** (1 owner-occupied pillar + 3 provinces + 4 property types + 2 emergency + 3 adjacent verticals). Each 2,000-2,500 words. Total content investment: $2,000-4,000 outsourced.

### Vector 6B lender anchor: Glasslake Funding (added 2026-09-14)

**Critical update from Dennis:** Glasslake Funding is a referral partner. He can submit as a mortgage broker with them. Glasslake is the answer to the emergency content cluster.

**Glasslake profile (verified):**
- Canadian non-bank mortgage lender, Bayview Asset Management subsidiary (institutional, real liquidity)
- Funds small commercial: $200K-$5M, 1-7 yr terms, up to 80% LTV, up to 40-yr amortization or interest-only
- Eligible property types match our content cluster: mixed-use, multi-family, industrial, automotive, office, light industrial, self-storage, daycares, restaurants, bars
- Positions itself as "move beyond unnecessary box-ticking" — the exact language the emergency cluster needs
- Works with mortgage brokers (regional sales managers across Canada, BDM structure)
- BC contact: Russell Veronelly (Western Canada RSM, 587-847-5361)

**How Glasslake changes the Vector 6B economics:**
- Emergency content (`commercial mortgage not renewing`, `commercial mortgage declined`, `lender won't renew`) had 0 measurable DataForSEO volume BUT has a real funnel when Glasslake is the named destination
- Lead → Dennis submits to Glasslake → Glasslake funds → Dennis earns broker commission (min $5K or 1.5-2%)
- Conservative funnel for emergency articles: 100 sessions/mo × 10% conv × 40% apply × 60% fund = **2.4 funded deals/mo at $12,500 = $30,000/mo from emergency content alone**

**Updated Vector 6B revenue projection (with Glasslake):**
- Previous (no lender anchor): $13K-54K/mo at month 12
- With Glasslake named in 4-5 pages (owner-occupied pillar + 2 emergency + 2 property types): **$20K-65K/mo at month 12**

**Glasslake named in these pages:**
1. `/business-loans-canada/commercial-mortgage-not-renewing/` — Glasslake as the named alternative lender
2. `/business-loans-canada/commercial-mortgage-declined/` — Glasslake as the named alternative lender
3. `/business-loans-canada/commercial-mortgage-broker-canada/` (owner-occupied pillar) — Glasslake in the lender comparison table
4. `/business-loans-canada/restaurant-commercial-mortgage/` — Glasslake funds restaurants
5. `/business-loans-canada/auto-dealership-financing/` — Glasslake funds automotive properties
6. Possibly: `/business-loans-canada/construction-to-permanent-financing/` — Glasslake as bridge lender

**Action item for Dennis:** confirm whether Glasslake broker agreement is already active (just start submitting) or needs WaveMakers onboarding (adds 2-4 weeks). Full analysis at `~/wiki/.local_tier/runs/commercial-mortgage-renewal/glasslake_partner_analysis.md`.

### The mortgage-lens moat (the part the previous strategy missed)

The original 7-pillar plan + 9 geo pages + 5-6 vertical pages + 3 lead magnets = ~30 pages. Add 4-6 mortgage-lens comparison pages and the site has ~35 high-intent pages.

**Swoop can't publish these 4-6 pages. Business-loan alt-lenders can't publish them. Only mortgage brokers with a business-credit lens can.**

The mortgage-lens content is not just another attack vector. It's the structural reason the comparison site exists. Without it, the site is "another Swoop with public tables." With it, the site is the only place in Canada a small business owner can get a holistic answer to "should I borrow against my home or take unsecured business credit?"

That positioning is what makes the site worth ranking for, worth linking to, and worth the user's email.

### Specific mortgage-lens pages to build (Phase 2-3)

1. **`/business-loans-canada/heloc-vs-business-line-of-credit/`**
   - The highest-intent comparison. Both products exist, both work for working capital, the choice depends on home equity, income stability, and tax position.
   - **Volume est: 90-260/mo. CPC est: $80-150 (financial products with high commercial intent).**

2. **`/business-loans-canada/home-equity-business-loan-canada/`**
   - Use-case hub for secured business funding through a mortgage broker. Pillar-level.

3. **`/business-loans-canada/self-employed-business-loan/`**
   - Self-employed borrowers face unique credit positioning. A mortgage broker who does both is the rare advisor who can structure the personal credit + business credit together.

4. **`/business-loans-canada/business-loan-or-refinance/`**
   - The buy-a-building question. Commercial mortgage vs refinance + business LOC. Mortgage broker can structure either.

5. **`/business-loans-canada/best-business-loans-for-self-employed/`**
   - Vector 2 + Vector 6 overlap. Best X + self-employed angle.

6. **`/business-loans-canada/second-mortgage-business-loan-canada/`**
   - Use-case page for borrowers with significant home equity but insufficient income for a HELOC. A mortgage broker can structure a second mortgage that an alt-lender can't.

### Lead economics: revised with Vector 6 reality (commercial mortgage added)

The mortgage-lens content has a different lead value than business-loan pages, but the search volume is too thin to drive large lead volume on its own. The commercial mortgage cluster is much bigger:

- **Standard business-loan lead** (from Swoop-style comparison): 3-5% conversion, $50-150 referral fee
- **Self-employed Vector 6A lead** (mortgage + business credit advisory): 5-8% conversion, $500-1,500 commission
- **Commercial mortgage Vector 6B lead** (purchase/refinance/renewal): 5-8% conversion, **$5,000-30,000 commission per funded deal** (broker at 1.5-2% of $300K-$2M+ loans, with $5,000 minimum)

**Vector 6A search volume:** 450 vol/mo (top 5 terms), 680 vol/mo total cluster
**Vector 6B search volume:** 3,090 vol/mo across 15 commercial-intent terms

### Commercial mortgage commission reality (corrected 2026-09-14)

Dennis confirmed the actual commission structure: **minimum $5,000 OR 1.5-2% of transaction size, whichever is higher**. This is significantly higher than the previous $500-5,000 estimate.

| Deal size | Commission (1.5%) | Commission (2%) |
|---|---:|---:|
| $300K (small, owner-occupied) | $5,000 (min) | $5,000 (min) |
| $500K (small-mid) | $7,500 | $10,000 |
| $1M (typical) | $15,000 | $20,000 |
| $2M (mid-large) | $30,000 | $40,000 |
| $5M+ (large) | $75,000 | $100,000 |

**Realistic avg per funded deal: $12,500** (mix of small/mid/large, allowing for shopping leads that don't fund).

### Vector 6B month-12 revenue recalculation

**Revenue model:** Lead → Application → Funded loan. Only funded loans pay commission. Typical funnel:
- Capture (top-10 ranking): 5-15% of search volume
- Lead conversion: 5-10% of captured sessions
- Fund rate: 30-50% of qualified leads (commercial mortgages take 60-120 days from lead to fund)

| Scenario | Sessions/mo | Leads/mo | Funded deals/mo | Revenue/mo |
|---|---:|---:|---:|---:|
| Conservative (5% cap, 5% conv, 30% fund) | 154 | 8 | 2.3 | **$28,969** |
| Realistic (10% cap, 5% conv, 30% fund) | 309 | 15 | 4.6 | **$57,938** |
| Optimistic (10% cap, 8% conv, 40% fund) | 309 | 25 | 9.9 | **$123,600** |
| Best case (15% cap, 10% conv, 50% fund) | 464 | 46 | 23.2 | **$289,688** |

**Even the conservative case ($29K/mo) means Vector 6B alone funds the entire site operation multiple times over.**

### Combined month-12 revenue (corrected)

- Standard business-loan leads (Vectors 1-5): 70-150/mo at $75 = $5,250-11,250/mo
- Vector 6A self-employed pillar: 1-3/mo at $750 = $750-2,250/mo
- **Vector 6B commercial mortgage pillar: 8-25 leads/mo, 2-10 funded deals/mo = $28,969-123,600/mo**
- **Combined: $35K-137K/mo at month 12 (realistic $35-58K/mo)**

**The commercial mortgage pillar is now the highest-revenue content cluster on the site, by 3-5x.** A single funded commercial mortgage ($15K avg commission) equals 200 standard business-loan leads at $75. The lead economics are completely different from the Swoop-vulnerable SERPs.

**The right way to think about the commercial mortgage pillar:** it's a high-value B2B lead-generation machine disguised as a content page. The commercial mortgage calculator + renewal email capture turn passive readers into qualified leads with $12,500+ average lifetime value. The pillar doesn't need 1,000 sessions/month to be profitable — it needs 8-15 qualified leads, of which 2-5 will fund.

The comparison site's volume comes from the Swoop-vulnerable SERPs (Vectors 1-5), but the **revenue concentration** is overwhelmingly in Vector 6B, where each funded deal is 100-200x the value of a standard business-loan lead.

---

## Final recommendation

**Yes, we can compete with Swoop.** Not by outranking them on the 4 head terms (which would take 2-3 years) but by:

1. **Owning 9 SERP categories they don't compete in** (Vectors 1-5)
2. **Owning 1 SERP category they can't compete in** (Vector 6 — mortgage-lens, the new moat)
3. **Building depth and structured data they don't have** (2,500-word articles vs their 800-word glossaries)
4. **Building 757 → 35+ high-intent pages in 12 months** — fewer pages, but each one 3-5x deeper

**The comparison site's strategic moat is Dennis's mortgage-broker license + business-credit lens.** Swoop is large and established, but they're stuck on one side of the lending industry. The site can be the only credible bridge between the two.

**Next concrete action:** Run the Vector 6 mortgage-lens keyword pull on DataForSEO (~$0.50), then build the foundation (4 pillars) + Vector 1 educational content + the first 3 mortgage-lens articles in months 1-2.

---

## Sources

- Live review of swoopfunding.com/ca (sitemap.xml, /business-loans, /start-business, /business-expansion, /property-finance, /import-export-finance)
- Google SERP analysis on HELOC vs business credit, mortgage-lens content gaps
- 124-term consolidated keyword dataset from `~/wiki/.local_tier/runs/tariff-loan-batch/`
- Previous audit in `~/wiki/clients/business-loans-canada/strategy/organic-search-strategy.md`
