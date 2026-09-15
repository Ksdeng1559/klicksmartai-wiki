# Business Loan Marketplace — Proposal for Review

**Prepared for:** Claude Code + ChatGPT (strategic review)
**Prepared by:** Hermes (KlickSmartAI chief-of-staff AI)
**Date:** 2026-09-14
**Author:** Dennis Eng (Mortgages by Dennis Eng, BC mortgage broker)
**Status:** Review draft — feedback welcome before build

---

## Executive Summary (TL;DR)

**The opportunity:** Build a business loan comparison site at `mortgagesbydenniseng.ca/business-loans/` that captures Canadian business-owner + commercial mortgage + self-employed borrower search demand through SEO.

**The thesis:** A mortgage-broker perspective is structurally impossible for credit brokers like Swoop to replicate. We can advise on HELOC, equity takeout, refinance-for-business, and CMHC commercial options — products that credit brokers can't include in their content because their commission model excludes them.

**The anchors:** Three broker-friendly private lenders + one government anchor:
- **BDC** (Business Development Bank of Canada) — trust + comparison anchor
- **Glasslake Funding** — owner-occupied commercial mortgage ($200K-$5M, all Canada) — Dennis onboarded ✅
- **Triple Queens** — bridge / construction / factoring ($2M+, BC/AB/ON/QC) — confirmed broker-friendly ✅
- **Kingsmen Capital** — SMB asset-based LOC + term loans ($25K-$10M, all Canada) — Dennis confirmed all-pay-commission ✅

**The size:** 88 pages across 9 tiers targeting ~41,580 vol/mo addressable search demand. Year-1 investment: $7K-13K. Realistic month-12 lead volume: 84-139/mo.

**The differentiator:** Every commercial-lending page has a "Mortgage Lens" section — HELOC, refinance, equity takeout alternatives the borrower should consider first. This is the structural moat vs Swoop.

**The ask:** Review the strategy, lender mix, page count, and tier prioritization. Flag risks, gaps, or tactical adjustments before we start building.

---

## 1. Context

Dennis is rebuilding mortgagesbydenniseng.ca on WordPress. The new site will host a `/business-loans/` subdirectory as the first major vertical expansion of his brokerage practice (Mortgages by Dennis Eng, BC-licensed mortgage broker).

**Why now:**
- Canadian small business lending demand is growing (BDC's 2026 outlook, tariff-driven working capital needs, post-CEBA consolidation)
- Swoop Funding dominates the head terms (`business loan`, `business loans canada`, etc.) with 757 indexable URLs but has structural gaps in commercial mortgage / mortgage-lens content
- WordPress + Rank Math Pro is the standard stack; we don't need to invent tooling

**Why a subdirectory, not a new domain:**
- Inherits the root domain's authority transfer
- Single SEO footprint, single brand
- Cross-link between mortgage content and business-lending content

**Constraints (Dennis-confirmed):**
- No-cost / low-cost strategy with aspirational-but-real budget
- WordPress rebuild (current site returns 404, currently on Wix)
- 4-layer pipeline rule: DataForSEO → Supabase → DuckDB → HTML on every research run (per KlickSmartAI standard)

**Dennis's commercial commission correction (verbatim, 2026-09-14):**
> "The min commercial mortgage broker commission is min $5000 to 1.5% to 2%, depending on mortgage transaction size."

This means a single commercial mortgage funded deal = $5K-$40K+ in broker commission, which is what makes the comparison site worth building.

---

## 2. Lender Anchor Mix

This is the most important strategic question for review. We have **4 anchors** covering different deal sizes and products:

| Lender | Sweet spot | Geography | Range | Differentiator | Status |
|---|---|---|---|---|---|
| **BDC** | Government-backed, established | All Canada | Up to $350K (SBL) / $5M+ (CRE) | Cheapest rate, longest amortization (25 yr), 36 mo IO | Trust anchor + comparison |
| **Glasslake Funding** | Owner-occupied commercial mortgage | All Canada (BC contact) | $200K-$5M | Bayview Asset Management subsidiary (institutional); "move beyond box-ticking" underwriting | ✅ Dennis onboarded |
| **Triple Queens** | Bridge, construction, factoring, mezzanine | BC/AB/ON/QC | $2M+ | Private lender, 5-10 day close, $5M+ bridge | ✅ Confirmed broker-friendly |
| **Kingsmen Capital** | SMB asset-based LOC, term loans | All Canada (Toronto HQ) | $25K-$10M (SMB) / $2-30M (Corp) | B-lender, 1-2 yr in business, no min credit, government-backed, bilingual EN/FR | ✅ Dennis confirmed all-pay-commission |

**Coverage matrix:**

| Deal size | Primary anchor | Secondary | Use case |
|---|---|---|---|
| $25K-$100K (startup/micro) | Kingsmen | Multi-lender | Term loans, micro ABL |
| $100K-$2M (established SMB) | Kingsmen | Glasslake | ABL, owner-occupied property |
| $200K-$5M (commercial mortgage) | Glasslake | Kingsmen | Owner-occupied, emergency |
| $2M-$5M (bridge/construction) | Triple Queens | — | Fast capital, draw schedules |
| $2M-$30M (upper mid-market) | Kingsmen Corp | — | Acquisitions, debt advisory |
| $5M+ (institutional) | Multi-lender | — | Trez, Romspen, etc. |

**Why this mix works:**
- We cover $25K to $30M end-to-end (no deal-size gap)
- Every tier has a real Canadian lender willing to pay broker commission
- Three private + one government = the "honest comparison" the comparison site promises
- Each lender serves a different product surface (no overlap = no conflict of interest)

**Questions for Claude Code + ChatGPT:**
- Is the 4-anchor mix right? Should we add a 5th (e.g., Trez Capital for institutional bridge) before launch?
- Are we missing a critical lender category (e.g., credit unions, online lenders)?
- Should we deprioritize any anchor based on conversion economics?
- Is the BDC anchor used correctly (comparison + trust signal, not direct referral)?

---

## 3. Keyword Universe & Competitive Reality

### Keyword universe (addressable search demand)

| Tier | Pages | Volume | Notes |
|---|---:|---:|---|
| T0 — Cornerstone + foundation | 13 | 8,300/mo | Education + lead capture |
| T1 — Head terms | 9 | 15,890/mo | High-volume, high-competition |
| T2 — Product pillars | 5 | 6,250/mo | LOC, unsecured, short term, etc. |
| T3 — Government programs | 5 | 3,110/mo | BDC + CSBFP — Swoop can't touch |
| T4 — Best X / Vertical industry | 24 | 4,400-4,500/mo | Includes 17 verticals (7 new from Kingsmen industry surface) |
| T5 — Tariff trigger | 2 | ~10/mo (event-driven, 1,134% spike) | News trigger |
| T6 — Vector 6 (commercial mortgage + LOC + factoring) | 22 | 3,770/mo | Highest revenue per page |
| T7 — Lead magnets | 4 | direct traffic | Top of funnel |
| T8 — Utility | 4 | n/a | About, disclosure, lender directory |
| **Total** | **88** | **~41,580/mo** | |

**Highest-CPC terms now in scope:**
1. accounts receivable financing — 90 vol/mo @ **$103.12 CPC** (highest in dataset)
2. invoice factoring canada — 140 vol/mo @ $74.28
3. small business line of credit — 260 vol/mo @ $71.09
4. ar financing / receivables financing — 90 vol/mo @ $58.89
5. factoring company canada — 110 vol/mo @ $48.63

### Competitive audit (Swoop Funding)

Swoop is the dominant credit broker. Verified sitemap data:
- **757 indexable URLs**: 252 product pages, 25 knowledge-hub glossaries, 30 sectors, 30 case studies, 220+ other
- Uses Rank Math on WordPress
- 110K+ newsletter subs
- 3+ years of authority
- **Structural gap:** zero HELOC, equity-takeout, refinance-for-business, or commercial mortgage content (commission model excludes these)

**Swoop owns:** 4 head terms — `business loan`, `business loans canada`, `small business loan`, `small business loan canada`

**Swoop-vulnerable:** 28 SERPs totaling 9,780 vol/mo across 5 attack vectors (educational/how-to, "Best X" comparisons, government programs BDC/CSBFP, province-modified pages, vertical industries, mortgage-lens content)

### Competitive audit (LendCity Mortgages)

LendCity is a separate competitor for the **commercial mortgage renewal SERP**:
- Ranks #1 for "commercial mortgage renewal Canada" with 3,200-word article
- 4.8/5 Google rating, 136 reviews
- "Top 1% mortgage agent in Canada"
- Mortgage Architects license #12728
- Uses Rank Math

**LendCity owns:** Commercial mortgage investor-focused content. **Their gap:** owner-occupied commercial mortgage (where Glasslake anchors), emergency content (lender won't renew / declined), and property-type verticals (gas stations, restaurants, auto dealerships, mixed-use).

**Questions for Claude Code + ChatGPT:**
- Is the page count (88) right for a 12-month build? Too many? Too few?
- Should we deprioritize any tier based on volume / competition reality?
- Are we under-investing in commercial mortgage content (highest revenue per page)?
- Should we add a "competitor gap" tier that targets LendCity-specific SERPs?

---

## 4. Sitemap Architecture

Full sitemap on disk: `~/wiki/clients/business-loans-canada/sitemap.md` (88 URLs, 22KB)

### Build sequence (12 months)

| Month | Pages | Tier | Volume target |
|---|---|---|---|
| 1-2 | 22 | T0 (13) + T1 (9) | 5,000 sessions/mo |
| 3 | 7 | T6 Vector 6B-1 (1) + T2 (5) + T6 bridge (1) | 8K-12K sessions/mo |
| 4 | 5 | T3 (5) | 12K-16K sessions/mo |
| 5-6 | 14 | T4 Best X (7) + T4 vertical existing (4) + T6 emergency (2) + T5 tariff (1) | 15K-22K sessions/mo |
| 7 | 6 | T4 vertical Kingsmen (3) + T6 Vector 6B-3 (2) + T6 Vector 6A (1) | 18K-28K sessions/mo |
| 8-9 | 14 | T4 vertical Kingsmen remaining (4) + T6 Vector 6B-4 (3) + T6 Kingsmen special (3) + lead magnets (4) | 22K-32K sessions/mo |
| 10-12 | 5 | T6 Triple Queens adjacents (3) + T8 marketplace (2) | 28K-45K sessions/mo |

### 7 new Kingsmen-anchored verticals (added 2026-09-14)

1. `/business-loans-canada/retail-business-loans/` — general store $70K BC 4-day example
2. `/business-loans-canada/salon-business-loans/` — salon tile
3. `/business-loans-canada/auto-repair-shop-loans/` — auto repair tile
4. `/business-loans-canada/delivery-business-loans/` — delivery services tile
5. `/business-loans-canada/medical-practice-loans/` — physiotherapy clinic 3-day example
6. `/business-loans-canada/liquor-store-business-loans/` — liquor store tile
7. `/business-loans-canada/coffee-shop-business-loans/` — coffee shop tile

**Questions for Claude Code + ChatGPT:**
- Should we re-order any tiers? (e.g., build T3 BDC comparison content first because it's lowest competition?)
- Is the month-3 launch of the Glasslake commercial mortgage pillar the right early bet?
- Should we ship the 22 foundation pages as a single push or in 2-3 milestones?

---

## 5. Differentiator: Mortgage Lens

Every commercial-lending page in the site has a **"Mortgage Lens" callout** with this message:

> **Stop. Before you borrow on the business, consider these alternatives:**
> - **HELOC** — borrow against your home equity at 5-7% rates (lower than most business LOCs)
> - **Refinance property** — pull equity out of your commercial property for cash
> - **CMHC MLI Select** — insured multi-residential financing at lower rates
> - **Self-employed mortgage** — stated-income options for business owners

**Why this matters:**

Swoop is a credit broker. Their commission model only includes unsecured / term-loan products. They cannot — by their structural model — recommend a HELOC or refinance because they can't earn commission on those products. The Mortgage Lens callout is a real, durable differentiator that:
1. Saves borrowers money (lower rates)
2. Builds trust (we're not just trying to sell them a business LOC)
3. Drives higher-value leads to Dennis (mortgage commissions are higher than referral fees)
4. Is structurally defensible (Swoop can't replicate it without breaking their commission model)

**Questions for Claude Code + ChatGPT:**
- Should the Mortgage Lens be a section on every page, or only on T2/T6 product pages?
- Should we make the Mortgage Lens content deeper (e.g., dedicated /self-employed-mortgage/ pages) than the current 1-page Vector 6A treatment?
- Is there a better framing for this differentiator?

---

## 6. Lead Economics

### Per-deal revenue

| Lead type | Conversion | Per-deal value |
|---|---|---|
| Standard business-loan lead (Swoop-style) | 3-5% | $50-150 referral fee |
| Self-employed Vector 6A lead | 5-8% | $500-1,000 commission |
| **Commercial mortgage Vector 6B lead (Glasslake)** | 2-5% | **min $5K OR 1.5-2% (per Dennis) = $7,500-$30,000+** |
| Kingsmen term loan lead | 5-10% | TBD (commission rate TBC with Kingsmen) |
| Triple Queens bridge / factoring lead | 5-10% | TBD (commission rate TBC with Triple Queens) |

### Month-12 lead volume projection

Realistic: **84-139 leads/mo** across all categories
- ~60% from Swoop-vulnerable SERPs (28 SERPs, 9,780 vol/mo)
- ~30% from new long-tail terms (T3 government, T4 vertical, T6 anchor)
- ~10% from branded search (Dennis, Glasslake, Triple Queens, Kingsmen)

### Revenue projection (month 12)

- Standard business-loan leads: 50-80/mo × 4% × $100 = **$200-320/mo**
- Self-employed Vector 6A leads: 8-12/mo × 6% × $750 = **$360-540/mo**
- **Commercial mortgage Vector 6B leads: 8-15/mo × 3% × $15K avg = $3,600-6,750/mo**
- **Kingsmen leads: 8-15/mo × 7% × $3K avg = $1,680-3,150/mo**
- Triple Queens leads: 3-5/mo × 7% × $5K avg = $1,050-1,750/mo
- **Total realistic month-12 revenue: $7K-12.5K/mo**

If Vector 6B converts higher (Glasslake is high-intent, $5K minimum commission): **$20K-65K/mo** total realistic upside.

### Year-1 ROI

- Investment: $7K-13K (Rank Math Pro $60, content writing $3-6K, lead form tool $0-500, optional design $2-5K)
- Year-1 cumulative revenue: $40K-150K (assuming launch at month 4)
- **Year-1 ROI: 3-20x**

**Questions for Claude Code + ChatGPT:**
- Are the conversion percentages realistic? (Standard 3-5%, vector 5-8%, commercial 2-5%?)
- Should we model Glasslake's $5K minimum as the floor for the commercial mortgage cluster?
- Is the Kingsmen commission structure correctly assumed at ~$3K avg (we need to confirm with their broker agreement)?

---

## 7. Risks & Open Questions

### Risks

1. **Glasslake lender relationship risk** — Dennis is onboarded but rate sheet + commission agreement still pending. If Glasslake's broker agreement terms are worse than expected, the entire Vector 6B economics change.
2. **Triple Queens + Kingsmen commission verification** — neither commission rate is confirmed in writing. Both are inferred from "all pay commissions" + broker program marketing copy.
3. **BDC comparison risk** — BDC is included as trust anchor, but BDC doesn't pay broker commission. We must be careful to disclose this clearly to avoid implying BDC referral.
4. **SEO competition from Swoop** — 757 indexable URLs + 3 years authority. We need to compete on long-tail and depth, not head terms.
5. **LendCity commercial mortgage competition** — 3,200+ word articles, 136 reviews, Top 1% agent. We need to differentiate on owner-occupied + emergency content.
6. **WordPress rebuild risk** — current site is on Wix and returns 404. If the WordPress rebuild is delayed, the launch is delayed.
7. **Québec / bilingual coverage** — Kingsmen serves QC. We have not decided if Dennis serves QC. If yes, we need French pages.

### Open questions (need answers before build)

1. **FSRA license # + jurisdiction** — confirm Dennis's license number + jurisdiction (BC? ON?) to display in footer
2. **BDC partner signal** — verify if Dennis has formal BDC referral agreement or just uses BDC as comparison anchor
3. **Brokerage branding** — Mortgage Architects or Verico (or both?) — confirm
4. **Email for lender routing** — separate inboxes per lender or all to Dennis with auto-distribute?
5. **Bilingual coverage** — does Dennis serve Québec? If yes, French pages needed
6. **Phone number** — confirm
7. **Lead form CRM** — HubSpot? Mailchimp? Custom form-to-email?
8. **Content writing** — Dennis writes? Outsourced? AI-assisted?
9. **First 3 pillars priority** — should we start with /business-line-of-credit/ (2,680 vol/mo, T2) or /commercial-mortgage-broker-canada/ (Glasslake anchor, highest revenue)?
10. **Launch timing** — soft launch (5 pages) or full foundation launch (22 pages)?

---

## 8. What We're Asking You to Review

### High-leverage questions

1. **Lender mix** — is the 4-anchor mix (BDC + Glasslake + Triple Queens + Kingsmen) the right one? Any critical gap?
2. **Page count & prioritization** — 88 pages across 9 tiers in 12 months — too aggressive? Too conservative?
3. **Vector 6B (commercial mortgage) prioritization** — should we shift the build order to publish this cluster earlier given the $5K+ commission per deal?
4. **Mortgage Lens differentiator** — is this the right framing? Should it be more prominent?
5. **Lead economics** — are the conversion percentages + per-deal values realistic? Is the month-12 lead volume projection (84-139/mo) conservative or optimistic?
6. **T3 (BDC / CSBFP) government cluster** — is this the right comparison-site moat? Should it be larger?
7. **Tariff T5 cluster** — worth a dedicated pillar (currently 2 pages, event-driven) or should we sunset it given 10 vol/mo base rate?
8. **Build sequence** — does the 12-month build sequence make sense? Any tier re-ordering?
9. **Risks** — what are we missing? What could go wrong that we haven't surfaced?

### Lower-priority but worth noting

- Is "BDC partner" the right trust signal wording (vs "BDC comparison" or "BDC reference")?
- Should we add a /blog/ from day one, or wait until month 4-6?
- Should we add a /resources/ section for downloadable PDFs (qualification checklist, government grants guide)?
- Should the public-facing lender directory (/lenders/) be alphabetical or tiered by deal size?
- What's the right tone for the BDC vs Private Lender comparison page (since BDC doesn't pay commission)?

---

## 9. Source Files

If you want to deep-dive on any section:

| Topic | File | Size |
|---|---|---|
| Sitemap (88 URLs, full tier breakdown) | `~/wiki/clients/business-loans-canada/sitemap.md` | 22KB |
| Wireframe (homepage + T2/T3/T5/T6/T8 page-by-page) | `~/wiki/clients/business-loans-canada/wireframe.md` | 52KB |
| Executive summary (TL;DR + ROI table) | `~/wiki/clients/business-loans-canada/strategy/executive-summary.md` | 12KB |
| Organic search strategy (5-phase 12-month playbook) | `~/wiki/clients/business-loans-canada/strategy/organic-search-strategy.md` | 32KB |
| Swoop competitive analysis (757 URLs, 6 attack vectors) | `~/wiki/clients/business-loans-canada/strategy/swoop-competitive-analysis.md` | 27KB |
| Page content proposals (4 priority pages outlined) | `~/wiki/clients/business-loans-canada/strategy/page-content-proposals.md` | 22KB |
| Client workspace header (lender anchor block) | `~/wiki/clients/business-loans-canada/README.md` | 8KB |

### Lender-specific research

| Lender | File | Size |
|---|---|---|
| Glasslake Funding | `../../research/commercial-mortgage-renewal/glasslake_partner_analysis.md` | 12KB |
| Triple Queens | `../../research/triplequeens-bridge/triplequeens_partner_analysis.md` | 12KB |
| Triple Queens indexed URLs | `../../research/triplequeens-bridge/triplequeens_industries.md` | 6KB |
| Kingsmen Capital partner | `../../research/kingsmen-capital/kingsmen_partner_analysis.md` | 10KB |
| Kingsmen Capital industries | `../../research/kingsmen-capital/kingsmen_industries.md` | 8KB |

### Keyword research

| Cluster | File | Size |
|---|---|---|
| Tariff loan batch (124 terms) | `../../research/tariff-loan-batch/` | 25KB |
| Mortgage lens Vector 6A (28 terms) | `../../research/mortgage-lens-vector6/` | 12KB |
| Commercial mortgage renewal Vector 6B (15 terms) | `../../research/commercial-mortgage-renewal/` | 22KB |
| Operating LOC + factoring (highest CPC cluster) | `../../research/operating-loc-factoring/` | TBD |

### Research spend to date

~$0.56 across 11 DataForSEO API calls + 5 live SERP searches + 9 page extracts.

---

## 10. Closing

This proposal is the cumulative output of a full research sprint (2026-09-13 → 2026-09-14):
- 124 commercial-intent keywords identified and consolidated
- Swoop Funding sitemap audited (757 indexable URLs)
- LendCity SERP audit (commercial mortgage cluster)
- 3 private lender anchors profiled (Glasslake + Triple Queens + Kingsmen)
- BDC product surface scraped (5 products)
- 88-page sitemap across 9 tiers built
- Page-by-page wireframe (cornerstone + T2/T3/T5/T6/T8 templates)
- Lead economics modeled with Dennis's commission correction ($5K min or 1.5-2%)

The strategy has been pressure-tested against:
- Swoop's 757-URL footprint (we know what we can and can't beat)
- LendCity's commercial mortgage authority (we know the gaps)
- Real Canadian keyword data (DataForSEO verified)
- Real lender product surfaces (BDC + 3 privates)
- Dennis's actual broker economics ($5K+ per commercial mortgage)

**Feedback priorities** (in order):
1. Lender mix validation
2. Build sequence validation
3. Lead economics sanity check
4. Risk gaps
5. Open questions blocking launch

Reply to Dennis directly with feedback. He reads low-context, terminal-style replies. Short, lowercase, no markdown.

Thanks for the review.
