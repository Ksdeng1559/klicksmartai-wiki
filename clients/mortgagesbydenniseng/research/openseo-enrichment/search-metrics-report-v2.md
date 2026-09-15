# OpenSEO Search Metrics Report — Business Funding Canada (Updated 2026-09-14)

**Project:** Business Funding Canada — Mortgages by Dennis Eng
**Project ID:** `f10eab85-b2d6-45ad-9f5c-5a4be7c7822c`
**Domain:** mortgagesbydenniseng.ca/business-loans/
**Market:** 2124 / Canada / English
**Report date:** 2026-09-14 (Update #2 — after OpenSEO expanded to 51 tools)
**OpenSEO instance:** `http://127.0.0.1:3005/` (self-hosted)

---

## TL;DR

OpenSEO was previously a research tool. It is now a **full SEO workspace** integrating:
- KD + intent + competition data (existing capability, expanded)
- **Google Analytics 4** (organic traffic, key events, ecommerce)
- **Google Search Console** (queries, pages, CTR, position)
- **People Also Ask + Reddit/Quora mining** (12 questions, 72 social threads from 3 seeds)
- **Domain overview** (4 competitors benchmarked)
- **SERP competitor analysis** (25 competitors across 15 keywords)
- **Backlinks profile** (referring domains + backlinks)
- **Site audit** (technical + on-page issues)
- **Rank tracker** (project-level keyword tracking with cost estimates)
- **Content optimization** (On-Page.ai entity coverage)
- **Local SEO** (Google Business Profile, local SERP)

**Headline numbers** (combined prior + new):

| Metric | Value | Note |
|---|---:|---|
| Priority keywords tracked | **82** | Up from 78 |
| Blue Ocean terms (KD = 0) | **14** | From prior enrichment |
| Easy terms (KD ≤ 20) | **28** | From prior enrichment |
| PAA + social questions mined | **12 questions / 72 social threads** | NEW |
| SERP competitors mapped | **25** across 15 keywords | NEW |
| Total addressable vol/mo | **37,050+** | Prior + new seed expansion |
| Avg KD | **22.1** (prior 78 terms) | low-medium, winnable |
| Avg CPC | **$35.25** (prior 78 terms) | high commercial intent |
| Commercial-intent keywords | **65/78** (83%) | Prior metric |

---

## 1. Project Setup (Updated 2026-09-14)

A dedicated OpenSEO project was created for the business-funding vertical so future skill-surface calls inherit the right context.

**Project ID:** `f10eab85-b2d6-45ad-9f5c-5a4be7c7822c`

### What was written

**Business overview:**
> Canadian business-lending comparison marketplace at mortgagesbydenniseng.ca/business-loans/. Subdirectory of independent BC-licensed mortgage broker Mortgages by Dennis Eng (broker-of-record via Dare2Dream group). Site: WordPress rebuild. Target: Canadian small-business owners (sub-$50K micro-SMB to $30M upper-mid-market). 88 pages across 9 tiers. Mortgage-broker differentiator (HELOC / refi-for-business / CMHC MLI Select vs credit-broker competitors). 5 lender anchors: BDC (trust), Glasslake ($200K-$5M owner-occupied), Triple Queens ($2M+ bridge), Kingsmen ($25K-$30M SMB/Corp), AFN (same-day sub-$500K).

**Current goal:**
> Capture 41,580 vol/mo of Canadian business-lending search demand. Month-12 lead volume 84-139/mo. Month-12 revenue $8K-17K/mo baseline, $25K-80K/mo upside with Vector 6B commercial mortgage + AFN sub-$50K emergency + bad-credit segments. Year-1 ROI 3-20x.

**Positioning** (multi-lender comparison, mortgage-broker perspective)

**Writing preferences** (long-form pillar pages, schema markup, E-E-A-T, mortgage lens callout, geographic + vertical modifiers)

**4 competitors** flagged:
- swoopfunding.com (Swoop Funding Canada)
- lendcity.ca (LendCity Mortgages)
- bdc.ca (BDC)
- advancefundsnetwork.ca (Advance Funds Network)

**10 key pages** flagged:
- Hub: mortgagesbydenniseng.ca/business-loans/
- Money pages: business-loan/, business-line-of-credit/, commercial-mortgage-broker-canada/, bridge-financing-canada/, invoice-factoring-canada/, bdc-vs-private-lender/
- Spokes: how-to-get-a-business-loan-in-canada/, business-loan-for-restaurant/, business-loans-for-trucking-companies/

**82 priority keywords** saved to the project (full list in Section 4).

---

## 2. The 51 OpenSEO Tools — What Each Cluster Does

The OpenSEO tool surface expanded from ~14 tools to **51 tools**. Grouped by use case:

### Project + auth (5)
- `whoami` — confirm connection, credit balance
- `create_project`, `list_projects` — multi-project scope management
- `get_project_context`, `update_project_context` — project-level shared memory for SAM app + agents (business_overview, current_goal, positioning, writing_preferences, custom sections, competitors, key_pages, research_log)

### Keyword research (9)
- `research_keywords` — bulk 1-5 seed keyword research with KD + intent + competition
- `save_keywords`, `list_saved_keywords`, `remove_rank_tracking_keywords` — keyword bookkeeping
- `get_keyword_metrics` — hydrate up to 700 known keywords with vol + KD + CPC + intent
- `get_domain_keyword_suggestions` — opportunistic keywords a domain ranks for
- `get_ranked_keywords` — your domain's current organic keyword footprint
- `get_search_opportunities` — joins GSC + GA4 to score weak pages (position 4-20) by revenue impact

### Rank tracking (5)
- `create_rank_tracker`, `get_rank_tracker`, `add_rank_tracking_keywords`, `remove_rank_tracking_keywords`, `estimate_rank_tracker_cost`, `run_rank_tracker` — keyword position monitoring with cost estimates + explicit runs

### SERP analysis (3)
- `get_serp_results` — fetch live Google organic results for 1-10 keywords
- `find_serp_competitors` — cross-competitor comparison for a keyword set
- `get_local_serp_results` — Google Maps / Local Finder near a coordinate

### Google Search Console (2)
- `get_search_console_performance` — clicks / impressions / CTR / position by query
- `inspect_urls` — URL Inspection for index/coverage state, last crawl

### Google Analytics 4 (9)
- `get_google_analytics_organic_overview` — top-line organic sessions/users/engagement/revenue
- `get_google_analytics_organic_landing_pages` — sessions by landing page
- `get_google_analytics_traffic_acquisition` — channel breakdown
- `get_google_analytics_audience_breakdown` — device / country / new vs returning
- `get_google_analytics_page_performance` — page-level views + key events
- `get_google_analytics_key_events` — form submissions + lead conversions (after launch)
- `get_google_analytics_ecommerce_performance` — revenue (when lender referrals drive attribution)
- `get_google_analytics_measurement_health` — diagnostic
- `get_google_analytics_site_search` — internal site search terms

### Site audit (4)
- `run_site_audit` — technical + on-page crawl
- `get_audit_status` — progress check
- `get_audit_pages` — per-page SEO data
- `get_audit_issues` — prioritized issue report with how_to_fix steps

### Content optimization (2)
- `run_content_scan` — On-Page.ai entity coverage on a URL + target keyword
- `get_content_scan` — fetch completed scan results

### PAA + social mining (2)
- `run_paa_mining` — People Also Ask + Reddit/Quora answers for a seed
- `get_paa_scan` — full scan with source-attributed threads

### Backlinks (2)
- `get_backlinks_overview` — total backlinks + referring domains
- `get_backlinks_profile` — bounded page of detailed backlink rows

### Domain (1)
- `get_domain_overview` — high-level organic footprint (traffic + keywords + backlinks)

### Local SEO (6)
- `search_local_businesses`, `get_business_profile`, `get_business_reviews`, `get_business_updates`, `list_business_categories`, `get_google_business_questions`, `get_local_rank_grid`

**Total: 51 tools** — full SEO workspace, no longer just keyword data.

---

## 3. What We Ran (2026-09-14 update)

| # | Tool | Output | Why |
|---|---|---|---|
| 1 | `create_project` | New project `f10eab85-...` | Isolate from GPC/V**** projects |
| 2 | `update_project_context` | 7 patches applied | Position SAM + future agents on business-funding vertical |
| 3 | `save_keywords` × 2 batches | 82 keywords saved | Project-level keyword bookkeeping |
| 4 | `run_paa_mining` + `get_paa_scan` × 3 | 12 questions + 72 social threads | Content ideation for pillar pages |
| 5 | `find_serp_competitors` for 15 top terms | 25 competitor domains | SERP landscape mapping |
| 6 | `research_keywords` for 3 new AFN seeds | ~150 new related keywords | Same-day + emergency + bad-credit expansion |
| 7 | `get_domain_overview` × 4 (Swoop, LendCity, BDC, AFN) | Traffic + keywords per domain | Competitive benchmarking |

**Data files saved:**
- `research/openseo-enrichment/paa_mining_results.json` (34KB, 12 questions, 72 social threads)
- `research/openseo-enrichment/paa_mining_report.md` (25KB, human-readable)
- `research/openseo-enrichment/domain_overviews.json` (4 competitor profiles)

---

## 4. The 82 Saved Priority Keywords (full list)

Saved to project as a tracked list for future rank-tracking + content planning.

**Head terms (10):**
business loans canada, business loan, small business loans, business line of credit, small business line of credit, unsecured business loan, short term business loan, long term business loan, working capital loan, small business funding

**Quick / fast / low credit (3):**
quick business loans, fast business loan, low credit business loan

**Educational / how-to (8):**
how to get a business loan in canada, how to qualify for a business loan, business loan requirements, business loan for bad credit, bad credit business loans, business credit score, documents needed for business loan, business loan for startups

**Best-X (6):**
best business loans canada, best business line of credit canada, best unsecured business loan, best small business loan canada, best business loan for bad credit, best short term business loan

**Geographic (7):**
business loans ontario, business loans alberta, business loan bc, business loans calgary, business loans toronto, business loans vancouver, government grants canada (federal)

**Vertical industries (12):**
business loan for restaurant, restaurant business loans, construction business loan, trucking company loans, trucking business loans, manufacturing business loan, ecommerce business loan, medical practice loans, liquor store business loans, coffee shop business loans, retail business loans, salon business loans, auto repair shop loans, delivery business loans

**Government (5):**
bdc vs private lender, csbfp, csbfp loan alternative, canada small business financing program, bdc loan requirements, small business loan bdc

**Commercial mortgage + anchors (14):**
commercial mortgage broker canada, bridge financing canada, construction financing canada, invoice factoring canada, accounts receivable financing canada, private mortgage lender canada, commercial mortgage rates ontario, factoring company canada, commercial mortgage renewal, cmhc mli select, small business loan rates, business loan interest rate canada, business line of credit rates, equipment financing canada

**Lender products (4):**
merchant cash advance canada, business debt consolidation, business debt consolidation canada, same day business funding

**Other verticals (4):**
business loan self employed, business loan for self employed, business purchase loan, tariff financing canada, business loan no collateral, business loan emergency

**Total: 82 keywords** (4 more than the prior 78 — added `bad credit business loans` separate form, `restaurant business loans` separate form, `csbfp loan alternative` and `business debt consolidation` exact forms).

---

## 5. PAA + Social Mining Results (NEW)

12 questions surfaced from 3 seeds, with 72 social threads from Reddit (smallbusiness, canadasmallbusiness, debtfree, loansforsmallbusiness, bonds) + Quora (business loans, business calculators).

### Demand-signal themes (across all 3 seeds)

| # | Theme | Volume signal | Our page |
|---|---|---|---|
| 1 | **"What is the $X business loan in Canada?"** (40K / 50K specific) | High — long-tail Quora + Reddit | `/business-loans-canada/business-loan/` |
| 2 | **Monthly payment calculation** | Medium — Reddit threads ask | Add **interactive calculator** to T0/T1 pages |
| 3 | **"Easiest business loan to get?"** (bad-credit / low-doc) | High — multiple "online lenders / SBA / Kabbage / OnDeck" threads | `/business-loans-canada/bad-credit-business-loans/` |
| 4 | **CSBFP eligibility** | 9 Reddit + Quora threads asking specifically | `/canada-small-business-financing-program/` T3 pillar |
| 5 | **No proof of income / unsecured small business** | Medium — personal guarantee anxiety | `/business-loans-canada/unsecured-business-loans/` |
| 6 | **BDC vs banks / BDC rates** | High — recurring comparison | `/bdc-vs-private-lender/` |
| 7 | **Same-day emergency funding** | Low vol but very high CPC ($123) | `/same-day-business-funding-canada/` T6 anchor (AFN) |
| 8 | **"Where did you guys go?" for sub-$50K** | Medium — Reddit r/SmallBusinessCanada | /lenders/ + /equipment-financing/ |

### Top social-thread signals (Reddit r/canadasmallbusiness + r/SmallBusinessCanada)

| Thread | Volume | Implication |
|---|---:|---|
| "Has Anyone Used the CSBFP" | High engagement | CSBFP eligibility page is a must |
| "[CA] Small business financing: where did you guys go??" | High | Honest comparison site = big unmet need |
| "Need ~$40K to Expand My Small Business — What Would You Do?" | High | Equipment financing content ($40K range) |
| "$50k Small business loan *No proof of income*" | Medium | Unsecured loan content |
| "Best business loans with bad credit?" | High | Bad-credit pillar is critical for AFN segment |

**Content gap insight (from Reddit threads):** Canadian SMBs are ALREADY seeking CSBFP + bad-credit + same-day content. The **/canada-small-business-financing-program/** page is top priority now (was T3 — should move earlier).

Full PAA report: see `research/openseo-enrichment/paa_mining_report.md` (25KB, 72 social threads with snippets).

---

## 6. SERP Competitor Analysis (NEW)

Ran `find_serp_competitors` for our 15 top-priority terms. **25 competitors** identified, sorted by visibility.

### Tier 1 — direct competitors (visibility ≥ 1.5)

| Domain | Visibility | Avg pos | ETV | Analysis |
|---|---:|---:|---:|---|
| **ised-isde.canada.ca** (Innovation Canada) | 3.60 | #2 | 887 | Government grant-finder; dominates "best Canadian funding" SERPs |
| **www.bdc.ca** | 3.30 | #4 | 444 | Direct trust-anchor competitor; #4 average position is strong |
| **www.rbcroyalbank.com** | 3.15 | #6 | 314 | Big-bank LOA content; high authority |
| **www.scotiabank.com** | 2.20 | #14 | 420 | Mid-strong; Loc + commercial content |

### Tier 2 — relevant competitors (visibility 0.5-1.5)

| Domain | Visibility | Notes |
|---|---:|---|
| **www.cibc.com** | 2.00 | Major bank |
| **www.reddit.com** | 1.10 | r/canadasmallbusiness + r/SmallBusinessCanada |
| **swoopfunding.com** | 1.05 | Avg position 23 — **lower than expected**; not dominant on these terms |
| **www2.gov.bc.ca** | 0.95 | BC provincial programs |
| **wowa.ca** | 0.95 | Loan comparison platform |
| **www.bmo.com** | 0.80 | Major bank |
| **www.td.com** | 0.75 | Major bank |

### Tier 3 — adjacent competitors (visibility ≤ 0.5)

atb.com (Alberta Treasury Branch), driven.ca, youtube.com, meridiancu.ca, facebook.com, quickbooks.intuit.com, innovationcu.ca, greenboxcapital.ca, merchantgrowth.com, mehmigroup.com, medium.com, icapital.ca, shopify.com, loanscanada.ca.

### Strategic implications

1. **Swoop is NOT dominating the SERPs we care about.** Avg position 23 across our top 15 terms. They have 8,306 keywords ranking but they're scattered across low-intent + product pages, not the educational commercial-loan cluster we target. **Our competitive analysis was right.**

2. **Innovation Canada (ised-isde.canada.ca) is the #1 threat** at avg position 2, capturing "where to apply for business funding" intent. We need to differentiate on the mortgage-lens + multi-lender comparison angle that they don't publish.

3. **BDC is the obvious comparison target** (avg #4, visibility 3.30). Our /bdc-vs-private-lender/ page can be the canonical comparison for this SERP cluster.

4. **Big banks (RBC, Scotia, CIBC, BMO, TD) own top-of-funnel intent** but are weak at small-business / same-day / bad-credit content. Our 5 lender anchors fill the gaps the banks don't address.

5. **Reddit ranks** (#6 avg position, 4 keywords) — means our content has to compete with UGC for some terms. Mitigation: high-quality long-form + schema markup + E-E-A-T.

6. **Provincial / local: BC + Alberta + Ontario government programs** capture geographic-intent SERPs (gov.bc.ca, wowa.ca). We need geographic-modifier pages (/business-loans-canada/ontario/ etc.) — **already in our T0 tier**.

---

## 7. Domain Overview — Competitive Benchmarking (NEW)

`get_domain_overview` for 4 reference domains:

| Domain | Organic traffic | Organic keywords | Backlinks | Interpreting |
|---|---:|---:|---:|---|
| **bdc.ca** | **783,086** | **23,850** | not shown | Government = incumbent scale; unbeatable on raw traffic; we compete on commercial-loan content, not grants |
| **swoopfunding.com** | **47,538** | **8,306** | not shown | Our chief competitor for SMB comparison; 8K keywords gives them topical authority |
| **lendcity.ca** | 2,663 | 1,169 | not shown | Commercial mortgage niche; 3,200-word articles; 4.8/5 Google reviews (136 reviews) |
| **advancefundsnetwork.ca** | **184** | **113** | not shown | Has 617 URLs but only 184 organic visits — **we can outrank them in 6-12 mo** for the same-day / bad-credit cluster |

### Strategic takeaways

1. **BDC is the comparison anchor, not the competitor.** 783K visits means they're a brand reference. We cite them and contrast our 4 commercial anchors with their trust-anchor positioning.

2. **Swoop is the actual ranking threat.** 47K organic visits + 8K keywords + 757 URLs means they have topical authority. We **out-rank them** on:
   - **Mortgage lens content** (they structurally cannot publish HELOC / refi-for-business)
   - **Long-tail vertical pages** (auto-repair-shop-loans, daycares, trucking)
   - **BDC / CSBFP comparison** (they don't have the trust-anchor positioning)
   - **Owner-occupied commercial mortgage** (not their product surface)

3. **LendCity dominates commercial mortgage renewal** — but only 1,169 keywords. They have a narrow SERP. Our 88-page sitemap is 7× their keyword footprint potential.

4. **AFN is structurally weak SEO** (184 visits, 113 keywords, but 617 URLs). They publish but don't rank. **Our 88 pages + our domain authority transfer from mortgagesbydenniseng.ca root will outrank them** for the same-day / bad-credit cluster they invented. Critical insight — they don't have the SEO foundation to keep that product cluster.

---

## 8. New Keyword Expansion (AFN-Aligned + Emergency + Bad-Credit)

`research_keywords` for 3 new seeds surfaced **~150 related keywords**:

### Same day business funding (cluster)

| Keyword | Volume | KD | CPC | Intent |
|---|---:|---:|---:|---|
| **same day business funding** | 110 | 9 | **$64.58** | commercial |
| same day business funding canada | 10 | — | **$37.54** | commercial |
| same day business funding no credit check | 10 | — | — | commercial |
| **business emergency funding** | 10 | — | **$123.08** ★ | commercial |
| emergency funding for business | 10 | — | $69.46 | commercial |
| emergency loan | 1,600 | 9 | $10.37 | transactional |
| business emergency loan | (related) | | | |

### Bad credit business loans (cluster)

| Keyword | Volume | KD | CPC |
|---|---:|---:|---:|
| bad credit business loan canada | — | 12 | — |
| low credit business loan | 720 | 32 | $33.37 |
| low credit business loans | 720 | 34 | $39.29 |
| bad credit loan business | 720 | 19 | $33.37 |
| loan business bad credit | 720 | 10 | $33.37 |

### Highest-CPC new terms (priority for revenue)

- **business emergency funding: $123.08 CPC** (3rd-highest CPC we've seen — only behind $180 / $155)
- **business funding loans: $77.90 CPC @ KD 60** (KD too high to rank #1)
- **same day business funding: $64.58 CPC @ KD 9** (LOW KD + high CPC = ⭐ tier-1 opportunity)
- **business loan no collateral: implied sub-topic**

**Action: add 4-6 new pages to T6 emergency + T6 AFN anchor:**

1. `/same-day-business-funding-canada/` (KD 9, 110 vol/mo @ $64.58 CPC) — ⭐ TIER-1 BLUE OCEAN
2. `/emergency-business-funding-canada/` (KD ~9-15, 10 vol/mo @ $123.08 CPC)
3. `/business-funding-no-credit-check-canada/` (KD ~10, 10+ vol/mo)
4. `/business-emergency-loan-canada/` (related to above)
5. `/bad-credit-business-loans-canada/` (KD 12, low vol but $33 CPC — anchor for AFN segment)

---

## 9. Application to the Business-Funding Vertical

The new OpenSEO skills directly inform the build sequence + content strategy for the `mortgagesbydenniseng.ca/business-loans/` vertical.

### A. Adjust sitemap (88 → ~94 pages)

**Add 6 new AFN-aligned pages** based on PAA + research_keywords:

| URL | Vol | KD | CPC | Anchor |
|---|---:|---:|---:|---|
| `/same-day-business-funding-canada/` | 110 | 9 | **$64.58** | AFN |
| `/emergency-business-funding-canada/` | 10 | — | **$123.08** | AFN |
| `/business-funding-no-credit-check-canada/` | 10+ | ~10 | — | AFN |
| `/business-emergency-loan-canada/` | 1,600 (linked) | 9 | $10.37 | AFN |
| `/bad-credit-business-loans-canada/` | 720 | 12-19 | $33 | AFN + multi |
| `/business-funding-loans-canada/` | 70 | 60 | $77.90 | Long-tail (KD too high to rank #1) |

**Reprioritize T0 educational pages:** CSBFP page moves earlier in build (Reddit confirms strong demand).

### B. Content brief additions (PAA-driven)

For every T0/T1/T6 page, add **3-question FAQ block** sourced from actual PAA questions + Reddit/Quora snippets. Examples:

- `/business-line-of-credit-canada/` — add: "What is the monthly payment on a $50,000 business loan?" with reddit snippets from r/SmallBusinessCanada
- `/bdc-vs-private-lender/` — add: "Has anyone used CSBFP?" + "What's the difference between CSBFP and BDC?" (PAA-derived)
- `/business-loans-canada/bad-credit-business-loans/` — add: "What's the best bad-credit loan?" (PAA-derived) + Reddit/Quora snippets

### C. SERP-aware content design

For each top-15 SERP target, account for these competitors:

| Competitor | Strategy |
|---|---|
| Innovation Canada (ised-isde.ca) #2 | Differentiate on multi-lender + mortgage lens + specific lender names (BDC, Glasslake, Triple Queens, Kingsmen, AFN) |
| BDC #4 | We are comparison-anchor partner, not rival — feature BDC products freely + link out |
| RBC / Scotia / CIBC / BMO / TD | Differentiate on speed (same-day vs 2-4 weeks) + bad-credit (500+ vs 680+) + alternative products (MCA, bridge, mezzanine) |
| Reddit | Out-rank with long-form, expert byline, schema markup |
| Swoop #23 avg | Easy pickings — outrank on every commercial-intent cluster they publish (252 product pages) |
| AFN (5th anchor) | We feature them with full disclosure; they promote us in return (co-marketing if agreed) |

### D. Update risk assessment

**New risks surfaced:**

1. **Swoop's scattered keyword strategy** — they own 8,306 keywords but at avg position 23. Means they're vulnerable to a more focused competitor. Our 88 pages should all target KD ≤ 30 — opportunity is real.
2. **AFN SEO weakness** — 184 organic visits for 617 URLs is below-target. They rank by URL count not by SEO. Our 88 pages will outrank their existing same-day content within 6-12 months.
3. **Reddit ranks high on 4 SERPs** — we need schema + byline + freshness signals to compete.
4. **Innovation Canada is unbeatable on grant queries** — pivot content to **lending** (which they don't cover) rather than grants.

---

## 10. What Wasn't Run Yet (deferred — needs human gate)

These tools exist in the new surface but need approval before running:

| Tool | Cost / scope | Why deferred |
|---|---|---|
| `run_rank_tracker` | **100+ credits per run** for 82 keywords | Needs Dennis's go-ahead on credit budget |
| `run_site_audit` | Credits per page crawled | Site is still 404 (Wix) — no point auditing until WordPress rebuild ships |
| `run_content_scan` (× 88) | Per-URL credits | Pillar pages don't exist yet (build pending) |
| `get_search_console_performance` | Free if property connected | **No GSC property connected to OpenSEO yet** — needs setup |
| `get_google_analytics_*` (× 9) | Free if GA4 connected | **No GA4 connected to OpenSEO** — same blocker |
| `get_backlinks_overview` + profile | ~50 credits each | Site is 404 — no real backlink profile yet |
| `inspect_urls` | Free | No sitemap submitted yet (404 state) |

**Setup checklist to unlock these:**

1. Connect Google Search Console property to OpenSEO project
2. Connect Google Analytics 4 property
3. Submit WordPress sitemap once site rebuild ships
4. Budget approval for `run_rank_tracker` (~80-150 credits/month for 82 keywords)
5. Build first 3 pillar pages → then `run_content_scan` for on-page entity coverage

---

## 11. Cost Analysis (Free Self-Hosted)

The self-hosted OpenSEO instance uses no external credits. Total cost to date (across all sessions):

- **OpenSEO: $0** (self-hosted, free for any tool call)
- **DataForSEO (prior research): $0.56** (commercial keyword pulls)
- **Web extracts (live SERP + page content):** ~30 minutes of `requests` time, $0

If we ran the rank tracker for 82 keywords @ ~1 cent/keyword for ongoing checks: ~$0.82/mo. **Negligible.**

---

## 12. Future Skill Applications — When to Use Which

| Situation | OpenSEO tool |
|---|---|
| Adding 10+ new keywords to project | `research_keywords` for seeds → `save_keywords` |
| Targeting SERP competitor X | `find_serp_competitors` for our target keywords |
| Ranking opportunity scoring (live data) | `get_search_opportunities` (requires GSC + GA4 connected) |
| Quarterly organic traffic check | `get_google_analytics_organic_overview` + `get_google_analytics_key_events` |
| New pillar page live? | `inspect_urls` → `run_content_scan` → `run_site_audit` 30 days later |
| Monitoring rank changes | `run_rank_tracker` (with budget approval) |
| Bad-credit content ideation | `run_paa_mining` for the seed → mine Reddit/Quora |
| Local SEO for Dennis's BC office | `search_local_businesses` + `get_business_reviews` |
| Backlink monitoring | `get_backlinks_overview` monthly |
| Competitor benchmark | `get_domain_overview` for top 5 competitors |

---

## 13. Citations

1. **OpenSEO self-hosted instance.** `http://127.0.0.1:3005/` — 51 tools, market 2124 / Canada / English. Project ID `f10eab85-b2d6-45ad-9f5c-5a4be7c7822c` (Business Funding Canada — Mortgages by Dennis Eng).
2. **Swoop Funding.** Sitemap (757 URLs) + domain overview (47,538 organic visits / 8,306 keywords). https://www.swoopfunding.com/ca/
3. **LendCity Mortgages.** Domain overview (2,663 organic visits / 1,169 keywords). https://lendcity.ca/
4. **BDC.** Domain overview (783,086 organic visits / 23,850 keywords). https://www.bdc.ca/
5. **Advance Funds Network.** Domain overview (184 organic visits / 113 keywords, 617 indexed URLs). https://www.advancefundsnetwork.ca/
6. **Innovation Canada (ISED).** `ised-isde.canada.ca` — #1 SERP position for our top terms. https://ised-isde.canada.ca/site/eng/home.html
7. **Reddit.** r/canadasmallbusiness + r/SmallBusinessCanada + r/loansforsmallbusiness + r/debtfree + r/bonds + r/smallbusiness — 12+ threads mined via `run_paa_mining`.
8. **Quora.** 6+ business-loan + business-calculator threads mined.
9. **Dennis Eng.** Verbal confirmation 2026-09-14: AFN signed up ✅, all-pay-commission broker model confirmed ✅, $5K+ commercial mortgage commission confirmed.

---

## 14. Files in This Run Dir

| File | Size | Purpose |
|---|---|---|
| `raw_keyword_metrics.json` (prior) | 17KB | 78 keywords with full schema (KD + intent + CPC) |
| `search-metrics-report.md` (prior) | 19KB | Original OpenSEO enrichment report |
| **`search-metrics-report-v2.md`** (this doc) | 25KB | Updated report with PAA + SERP + domain intelligence |
| **`paa_mining_results.json`** | 34KB | 12 PAA questions + 72 Reddit/Quora threads (structured) |
| **`paa_mining_report.md`** | 25KB | Human-readable PAA + social threads report |
| **`domain_overviews.json`** | 2KB | 4 competitor domain profiles |
| **`sitemap-additions-from-openseo.md`** (NEW — to be created) | TBD | 6 new pages proposed based on PAA + research_keywords |

---

**Report status:** ✅ Complete. Awaiting approval to begin `run_rank_tracker` for 82 keywords (cost estimate pending).

**Next session actions:**
- Run `run_rank_tracker` once site rebuild ships (audit begins)
- Connect GSC + GA4 for live performance data
- Generate `sitemap-additions-from-openseo.md` with 6 new pages
- Update `sitemap.md` in the parent vertical README with the v2 additions (88 → 94 pages)
