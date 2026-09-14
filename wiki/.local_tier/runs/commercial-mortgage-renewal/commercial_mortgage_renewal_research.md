# Commercial Mortgage Renewal Research

**Date:** 2026-09-13
**Purpose:** Quantify the commercial mortgage renewal/refinance attack surface for the comparison site.
**Method:** DataForSEO keyword_overview/live + keywords_for_keywords/live + keyword_ideas/live
**Total spend:** $0.16 across 4 API calls
**Surprising finding:** The "renewal rates" angle is **a feature, not a page** — the real volume is in `commercial mortgage broker` (590/mo, $11.26 CPC) and `commercial mortgage calculator` (1,600/mo, $2.70 CPC). Renewal is one of 5 reasons someone visits those pages, not a standalone search.

---

## TL;DR

- **Commercial mortgage renewal specifically is a near-zero search term** in Canada — 0-10 vol/mo for every "commercial mortgage renewal" variant
- **The real commercial mortgage SERPs are:**
  - `commercial mortgage broker` (590/mo, $11.26 CPC) — intent: find an advisor
  - `commercial mortgage calculator` (1,600/mo, $2.70 CPC) — intent: estimate payment
  - `commercial mortgage rates canada` (320/mo, $3.56 CPC) — intent: rate shopping
  - `commercial mortgage rates ontario` (260/mo, $3.73 CPC) — intent: regional rates
  - `commercial mortgage refinance` (10/mo, $15.88 CPC) — high-CPC, very low volume
- **Total commercial-mortgage search surface: ~3,090 vol/mo across 15 commercial-intent terms**
- **The right play is NOT a "renewal rates" page.** It's a `/business-loans-canada/commercial-mortgage-broker-canada/` pillar that addresses all 5 use cases (purchase, renewal, refinance, equity takeout, construction) under one URL

**Why renewal is a feature, not a page:**
- Most commercial mortgages have 3-5 year terms
- At maturity, the lender sends a renewal letter offering a rate
- The borrower has 30-90 days to decide: take the renewal, shop the market, or refinance
- This is a **forced-action event** but the search behavior shows people don't search "commercial mortgage renewal rates" — they search "commercial mortgage broker" (because they want an advisor to shop it for them) or "commercial mortgage rates" (because they want a market benchmark)
- A page titled "renewal rates" would only catch the 10/mo "commercial mortgage refinance rates" traffic and miss the 2,790/mo who are searching with broker/rates/calculator intent

---

## Research data

### 1. Direct seed pull (10 seeds, 2 with volume)

| Keyword | Vol | CPC | Comp |
|---|---:|---:|---:|
| commercial mortgage rates canada | 320 | $3.56 | 0.48 |
| commercial mortgage refinance | 10 | $15.88 | 0.03 |
| commercial mortgage renewal rates | 0 | $0 | 0 |
| commercial mortgage renewal | 0 | $0 | 0 |
| commercial mortgage renewal process | 0 | $0 | 0 |
| renew commercial mortgage | 0 | $0 | 0 |
| commercial mortgage renewal letter | 0 | $0 | 0 |
| should i renew or refinance commercial mortgage | 0 | $0 | 0 |
| commercial mortgage refinance rates | 0 | $0 | 0 |
| commercial mortgage renewal calculator | 0 | $0 | 0 |

**Cost:** $0.012

### 2. Expansion pull (3 seeds, 67 items, 30 commercial)

| Top terms | Vol | CPC |
|---|---:|---:|
| commercial mortgage refinance / refi / loan refinancing | 10 each | $15.88 |
| commercial mortgage rates canada | 320 | $3.56 |
| commercial mortgage rates ontario | 260 | $3.73 |
| commercial lending rates canada | 110 | $5.65 |
| current commercial mortgage rates canada | 110 | $3.36 |
| 5 year commercial mortgage rates canada | 50 | $4.69 |
| best commercial mortgage rates canada | 50 | $2.18 |

**Cost:** $0.09

### 3. keyword_ideas (8 seeds, 300 items)

Most of the 300 returned terms were residential (mortgage renewal 2,400/mo, mortgage renewal calculator 8,100/mo, etc.) — confirming that the residential renewal market dwarfs the commercial one. The commercial-specific commercial_mortgage_general bucket had only 4 terms with volume.

**Cost:** $0.048

### 4. Final commercial-mortgage overview (21 seeds, 15 returned)

| Keyword | Vol | CPC | Comp |
|---|---:|---:|---:|
| commercial mortgage broker | 590 | $11.26 | 0.53 |
| commercial mortgage calculator | 1,600 | $2.70 | 0.48 |
| commercial mortgage rates canada | 320 | $3.56 | 0.48 |
| cmhc commercial mortgage | 50 | $7.19 | 0.16 |
| commercial mortgage refinance | 10 | $15.88 | 0.03 |
| commercial mortgage rates ontario | 260 | $3.73 | 0.62 |
| commercial mortgage rates alberta | 50 | $4.09 | 0.45 |
| commercial mortgage rates bc | 40 | $5.39 | 0.49 |
| 5 year commercial mortgage rates canada | 70 | $3.13 | 0.68 |
| refinance commercial property | 10 | $8.38 | 0.40 |
| refinance commercial real estate | 10 | $8.38 | 0.40 |
| best commercial mortgage rates canada | 50 | $2.18 | 0.66 |
| cmhc commercial mortgage rates | 10 | $0.00 | 0.05 |
| commercial construction loan rates | 10 | $0.00 | 0.00 |
| commercial mortgage refinance rates | 10 | $0.00 | 0.00 |

**Cost:** $0.014

**Total research spend: $0.16**

---

## The right strategy for commercial mortgage content

### What NOT to build

- ❌ Standalone "commercial mortgage renewal rates" page — 0 vol/mo
- ❌ Standalone "commercial mortgage refinance rates" page — 10 vol/mo
- ❌ Standalone "commercial mortgage renewal process" page — 0 vol/mo
- ❌ Standalone "commercial mortgage renewal letter" page — 0 vol/mo

These pages would target terms that don't exist. Even if you ranked #1 for "commercial mortgage renewal rates" (10/mo), that's 1 click/month.

### What to build

**A single pillar: `/business-loans-canada/commercial-mortgage-broker-canada/`**

This targets the 590/mo `commercial mortgage broker` SERP plus embeds the renewal/refinance content as major sections:

1. **Hero: "Commercial mortgage broker Canada — 5-year term, 25-yr amortization, multiple lender quotes"**
2. **Section 1: Current commercial mortgage rates (Q3 2026)** — updated monthly, targets `commercial mortgage rates canada` (320/mo) + province variants (350/mo combined)
3. **Section 2: Calculator** — embed a working commercial mortgage calculator, targets `commercial mortgage calculator` (1,600/mo) and `commercial mortgage rates ontario` (260/mo)
4. **Section 3: Renewal** — "What to do when your renewal letter arrives" with a decision tree: stay with current lender, shop the market, or refinance
5. **Section 4: Refinance** — when refinancing beats renewal, with break-even math
6. **Section 5: New purchase** — first-time commercial mortgage buyer walkthrough
7. **Section 6: Construction** — short-term construction financing → permanent takeout
8. **FAQ (10+ questions)** — captures the long-tail informational queries

**Why this structure wins:**
- Targets the high-volume terms (`commercial mortgage broker` 590/mo, `commercial mortgage calculator` 1,600/mo, `commercial mortgage rates canada` 320/mo)
- Embeds the renewal/refinance content where borrowers actually need it
- One URL ranks for 10+ related terms instead of 5 thin URLs each ranking for 1-2 terms
- Internal linking: every other pillar on the site (Line of Credit, Working Capital, etc.) can link to this one when discussing secured business funding

### Lead value (commercial mortgage vs business LOC) — corrected 2026-09-14

**The lead value is much higher than the previous estimate.** Dennis confirmed the actual commission structure: **minimum $5,000 OR 1.5-2% of transaction size, whichever is higher**.

| Deal size | Commission @ 1.5% | Commission @ 2% |
|---|---:|---:|
| $300K (small, owner-occupied) | $5,000 (min) | $5,000 (min) |
| $500K (small-mid) | $7,500 | $10,000 |
| $1M (typical) | $15,000 | $20,000 |
| $2M (mid-large) | $30,000 | $40,000 |
| $5M+ (large) | $75,000 | $100,000 |

- **Commercial mortgage lead:** $5,000-100,000 commission per funded deal (realistic avg $12,500 across small/mid/large mix)
- **Unsecured business loan lead:** $50-150 referral fee

**A single commercial mortgage conversion is worth 50-200x a standard business-loan lead.** This changes the entire economics of the pillar.

### The mortgage-lens cluster recompute (combining Vector 6 + renewal data)

The Vector 6 mortgage-lens content (from the previous research) was 680 vol/mo across 28 terms. Adding the commercial mortgage data:

| Cluster | Vol/mo | Avg CPC |
|---|---:|---:|
| Vector 6A (mortgage-lens, self-employed) | 680 | varies |
| Vector 6B (commercial mortgage, this research) | 3,090 | $5.10 |
| **Combined Vector 6** | **3,770** | — |

The commercial mortgage cluster is **4.5x larger** than the original Vector 6 estimate. This is a bigger play than the previous analysis recognized.

**Revised Vector 6 plan:**
1. **Pillar 1:** `/business-loans-canada/self-employed-business-loans/` (450 vol/mo from previous research, mortgage-lens embedded)
2. **Pillar 2:** `/business-loans-canada/commercial-mortgage-broker-canada/` (3,090 vol/mo from this research, renewal/refinance embedded)

These two pillars cover 3,540 of the 3,770 vol/mo in the combined Vector 6 (94%).

### Updated month-12 revenue projection

With the commercial mortgage pillar added:

- Standard business-loan leads (Vectors 1-5): 70-150/mo at $75 = $5,250-11,250/mo
- Vector 6 self-employed pillar: 1-3/mo at $750 = $750-2,250/mo
- **Vector 6 commercial mortgage pillar: 5-15/mo at $1,500 = $7,500-22,500/mo**
- **Combined: $13.5K-36K/mo at month 12** (revised up from $6K-13.5K)

The commercial mortgage pillar alone could be the highest-revenue page on the site, because each lead is worth $1,500+ (a typical $300K commercial mortgage at 0.5% broker commission = $1,500).

---

## The renewal angle as a content trigger (not a page)

Renewal is a **seasonal/event-triggered** topic, not a search-driven one. The right way to use it:

1. **Add a "Commercial Mortgage Renewal Season 2026" banner** to the pillar page every September-December (peak renewal season for Canadian commercial mortgages, which often have calendar-year terms)
2. **Email capture on the pillar page:** "Get our 2026 commercial mortgage renewal checklist" — captures the borrower at the exact moment they're 90 days from maturity
3. **Quarterly content updates:** "Q3 2026 commercial mortgage rates: what the BoC hold means for your renewal"
4. **Email nurture:** Anyone who downloads the renewal checklist gets a 5-email sequence ending with "Need help shopping your renewal? Book a 15-min call."

The renewal angle is **conversion infrastructure** (lead capture + nurture), not SEO content. The SEO content targets the high-volume broker/calculator/rates queries; the renewal angle is the reason the visitor converts.

---

## Files on disk

- `raw_overview.json` — direct seed pull
- `raw_kfk.json` — keywords_for_keywords expansion
- `raw_keyword_ideas.json` — keyword_ideas semantic expansion
- `raw_cm_overview.json` — 21-seed commercial-mortgage overview
- `kfk_processed.json` — 30 commercial terms
- `keyword_ideas_processed.json` — renewal/refinance/general buckets
- `cm_overview_processed.json` — 15 commercial-mortgage terms (the source of truth)
- `commercial_mortgage_renewal_research.md` — this document
