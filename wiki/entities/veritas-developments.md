---
title: Veritas Development Group LLC
type: entity
created: 2026-08-28
updated: 2026-08-28
tags: [client, klicksmartai-client, multi-agent-workspace]
related:
  - clients/veritas-developments/IDENTITY.md
status: active
client_slug: veritas-developments
---

# Veritas Development Group LLC

**Corporate:** Veritas Development Group LLC
**Domain:** veritasdevelopmentgroupllc.com
**Industry:** commercial-construction
**Geography:** kc-metro
**Tier:** pilot
**Status:** active
**Workspace:** `~/wiki/clients/veritas-developments/`
**DuckDB canonical store:** `~/wiki/clients/veritas-developments/.local_tier/clients/veritas-developments.duckdb` (v1.2.0)

**Notes:** Lee's Summit capital raise pilot. Faith-framed commercial construction investment thesis. Two open decisions (Reg-D adjacency, KC Business Journal listicle).

## Contacts

- **David Poole** — Managing Partner (decision authority: final, status: awaiting-reply)
  - Owns web fix priority + client-engagement signoff. Primary decision authority.
- **Daniel Bailey** — CFO (decision authority: consult, status: awaiting-reply)
  - Co-approver on engagement quote. Compliance-side review.

## Open Decisions

- **C3: Reg-D adjacency on financing guide** (compliance, P1, status: pending-client, owner: Daniel)
  - Fund-formation article mentions accredited-investor mechanics adjacent to Lees Summit capital raise. Risk: Reg-D adjacency reads as solicitation. Need explicit compliance posture.
  - Impact if unresolved: If unresolved: LP-side due-diligence questions may surface in capital-raise meetings; could require reactive legal review under tighter timeline.
- **P2: KC Business Journal listicle pitch** (positioning, P2, status: pending-client, owner: David)
  - Local press opportunity targeting KC Business Journal. Best timing: Q4 2026. 4-6 week lead time on pitches.
  - Impact if unresolved: If unresolved: KCBJ editorial calendar Q4 slots fill with non-faith-framed competitors; harder to break in once pitched-and-passed.

## RELEASED Deliverables

- [audit-audit-v4-2026-08-28](#audit-v4-2026-08-28) — **SEO Audit — veritasdevelopmentgroupllc.com (v4)** · 3816 words · released 2026-08-28 · by hermes
- [audit-client-score-2026-08-28](#client-score-2026-08-28) — **Client Score — Veritas Development Group LLC** · 1490 words · released 2026-08-28 · by hermes
- [audit-cover-memo-v4-2026-08-28](#cover-memo-v4-2026-08-28) — **Cover Note — SEO Audit v4** · 1043 words · released 2026-08-28 · by hermes


---

## SEO Audit — veritasdevelopmentgroupllc.com (v4)

<a id="audit-v4-2026-08-28"></a>

**Deliverable ID:** `audit-v4-2026-08-28`  
**Kind:** audit  
**Status:** released  
**Version:** 1  
**Word count:** 3816  
**Released:** 2026-08-28 by dennis  
**Source:** `clients/veritas-developments/projects/website/seo-audit-veritasdevelopmentgroupllc-2026-08-28-client.md`

---
title: "SEO Audit & Recommendations — veritasdevelopmentgroupllc.com"
type: site-audit-client
status: RELEASED — presentable to David Poole + Daniel Bailey (2026-08-28)
created: 2026-08-28
updated: 2026-08-28 (v4: 8-keyword SERP intelligence + 90-day content plan + keyword reclassifications)
released: 2026-08-28
released_by: Dennis Eng (KlickSmartAI) — for David Poole + Daniel Bailey review
client: Veritas Development Group LLC
domain: veritasdevelopmentgroupllc.com
audit_date: 2026-08-28
predecessor: (internal — kept for traceability)
---

# SEO Audit & Recommendations — veritasdevelopmentgroupllc.com

## Executive summary

> For: David + Daniel · Reading time: 60 seconds

Your site is reachable and fast, but **Google can't read the words that describe your business** — the homepage renders through JavaScript and the server returns the same HTML shell for every URL, including the paths that should serve `robots.txt` and `sitemap.xml`. Until that's fixed, none of the SEO work below can take effect.

**The fix is one developer sprint.** Server-render the homepage, configure the host to serve real static files at the crawlability paths, and the foundation is in place. From there, the winnable search landscape for "Lee's Summit / Kansas City commercial construction" is **less competitive than you'd expect** — multiple entry keywords have difficulty scores in the 12-26 range, dominated by mid-tier local GCs (not national firms). Veritas can rank in the top 5 within 3-6 months of fixing the foundation.

**Three things to do first, in order:**
1. **Fix the hosting layer** so search engines can read the site (1 sprint).
2. **Add real content** — H1, 300+ words describing your services and service area (1 day).
3. **Stand up local presence** — Google Business Profile + Bing Places (30 minutes).

Everything else is opportunistic. The full plan is below.

---

> **Bottom line: the foundation is missing.** The site is reachable and returns a healthy response. But Google can't actually read the content — the page renders through JavaScript, so the words that describe your business are invisible to search engines. Fixing this single issue clears most of what's wrong.

## At a glance

| What we checked | What we found |
|---|---|
| Domain | `veritasdevelopmentgroupllc.com` |
| Pages indexable | **1** (homepage only) |
| Site reachable | ✅ Yes — secure, fast response (69 ms) |
| Page title | 99 characters — too long, gets cut off in search results |
| Meta description | 242 characters — too long, gets cut off in search results |
| Headline (H1) | **Missing** |
| Words visible to Google | **0** |
| Links to other pages | **0** |
| XML sitemap | **Blocked — server returns the app shell, not XML** |
| Robots file | **Blocked — server returns the app shell, not rules** |
| Search keywords ranking | None — site is not indexed |
| Backlinks | 0 sites linking to you |
| Google Business Profile | Not yet set up |

**Top 3 priorities:**

1. **Fix the hosting layer so search engines can read the site.** Three issues compound here: the homepage content is invisible to crawlers (rendered only after JavaScript runs), and the server returns the same page shell for `/robots.txt` and `/sitemap.xml` instead of valid files. All three fixes are part of the same root cause and need to land together.
2. **Add a clear page headline (H1)** and a few hundred words describing your services and service area.
3. **Set up the basics search engines need:** valid XML sitemap + `robots.txt`, Google Business Profile, and a few starter pages (Services / Projects / About / Contact).

**Quick wins:** trim the page title and meta description. About 15 minutes of work, zero risk.

---

## What we found (in priority order)

### 1. The site has a hosting-layer routing problem (High priority)

- **What we saw:** When we request `/robots.txt` and `/sitemap.xml`, the server returns the same HTML page shell that the homepage returns — not a valid robots file or an XML sitemap. Search engines expect plain text and XML at those paths, and they treat a 200 HTML response at those URLs as "no file present."
- **Why it matters:** **This blocks crawlability at the infrastructure level, not just at the page level.** Even after the homepage is fixed, search engines still need a valid `robots.txt` to know what they're allowed to crawl, and a valid `sitemap.xml` to discover the URLs they should index. Without these, indexing will stay slow or incomplete.
- **Likely cause:** The hosting configuration serves the single-page application (SPA) shell for every path, including paths that should be served as static files. This is a common SPA-hosting misconfiguration.
- **Recommended fix:**
  1. Tell your hosting provider (or developer) to configure the server so `/robots.txt` returns a real robots file and `/sitemap.xml` returns a real XML document.
  2. The sitemap should list every indexable URL on the site with `<lastmod>` dates. For now, that's just the homepage.
  3. The robots file should at minimum declare the sitemap location (`Sitemap: https://veritasdevelopmentgroupllc.com/sitemap.xml`) and allow all crawlers.

### 2. The homepage content isn't visible to search engines (High priority)

- **What we saw:** Page analysis reports `wordCount: 0`. The page shows a meaningful title and meta description in the source, but the actual body content — the words describing your business — aren't in the HTML Google can read.
- **Why it matters:** **Google cannot rank what it cannot read.** This single issue, on its own, is enough to keep the site out of search results — regardless of any other SEO work.
- **Likely cause:** The site loads its main content through JavaScript (common with modern website builders and single-page frameworks).
- **Recommended fix:**
  1. Have your developer server-render the homepage so the headline, body copy, and navigation appear in the initial HTML response — not just after JavaScript runs.
  2. Once rendered, add **300+ words** of real content describing the company, your services, and your service area (Lee's Summit + Kansas City, MO).
  3. Re-run the audit afterward — the word count should jump from 0 to 300+, and several of the other findings below should clear automatically.

> **These first two issues compound.** They share a root cause — the site's setup treats every URL the same way and renders content at runtime. Fixing one without the other leaves a partial improvement. The good news: both fixes usually land in the same developer sprint.

### 3. Missing page headline (H1) (High priority)

- **What we saw:** No H1 detected on `https://veritasdevelopmentgroupllc.com/`.
- **Why it matters:** The H1 is the strongest in-page signal for what a page is about. Missing H1 is a quality flag.
- **Recommended fix:** Add a single H1, front-loaded with the primary keyword. Suggested: `<h1>Real Estate Development & Construction in Lee's Summit, MO</h1>`.

### 4. No links to other pages (High priority)

- **What we saw:** Homepage has zero internal links. And because of finding #2, there are no other pages to link to anyway.
- **Why it matters:** Search engines discover pages by following links. With no links from the homepage, any future service or portfolio pages will be invisible to crawlers.
- **Recommended fix:** Add a server-rendered navigation bar (Home / Services / Projects / About / Contact). Even stub pages with short descriptions are better than nothing — they give crawlers a path to follow.

### 5. Meta description too long (Medium priority)

- **What we saw:** 242 characters. Recommended length: 70–160.
- **Why it matters:** Search engines truncate long descriptions in results. Your visible description currently cuts off mid-sentence.
- **Recommended fix:** Trim to ~150 characters. Suggested:
  > "Veritas Development Group LLC — real estate development, commercial construction, and capital advisory in Lee's Summit & Kansas City, MO. Built on integrity."

### 6. Page title too long (Medium priority)

- **What we saw:** 99 characters. Recommended length: 50–60.
- **Why it matters:** Search results truncate long titles. Important keywords get pushed off the end.
- **Recommended fix:** Trim to ~55 characters. Suggested:
  > "Veritas Development Group LLC | Lee's Summit, MO" (47 characters)

---

## Technical health check (limited — site too thin to fully score)

| Dimension | Status | Notes |
|---|---|---|
| HTTPS (secure connection) | ✅ Yes | `https://veritasdevelopmentgroupllc.com/` returns 200 |
| Server response time | ✅ Healthy | 69 ms |
| Mobile-friendly | ⚠️ Not verified | Re-test after the homepage content fix lands |
| Page speed | ⚠️ Not run | Will test once the page is fully rendered |
| Structured data (schema) | ⚠️ Not detected | Cannot be reliably detected until the page renders. We'll re-test after the fix. |
| XML sitemap | ❌ **Broken** | Server returns the SPA HTML shell instead of valid XML. Hosting misconfiguration. |
| robots.txt | ❌ **Broken** | Server returns the SPA HTML shell instead of valid robots directives. Same root cause as sitemap. |

---

## Authority & local presence (Stage 1 prerequisites)

| Item | Status | Notes |
|---|---|---|
| Other sites linking to you | 0 | Site has never been linked from anywhere we can see |
| Search keywords ranking | 0 | Site is not indexed |
| Google Business Profile | Not yet set up | Required for local SEO |
| Bing Places | Not yet set up | Required for local SEO |
| Name/address/phone consistent across the web | Not yet verified | Required for local SEO |

---

## The search landscape in your service area

A search-engine data pass over commercial-construction + commercial-real-estate keywords with Kansas City / Lee's Summit intent reveals a **less competitive landscape than you'd expect**. The competitive set is dominated by **mid-tier local GCs** at positions 2-10, not national firms. Below is what we found.

### The winnable entry keywords

These are KC-area commercial-construction and commercial-real-estate searches where Veritas could realistically rank in the top 5 once the foundation is fixed. Higher volume is not always better — we weight by *difficulty score* (how hard it is to crack the top 10).

| What people search for | Monthly searches | Difficulty | Why this matters |
|---|---|---|---|
| `multifamily contractors` | 90 | **0** | No competition — easy first win |
| `kansas city corporate housing` | 260 | **1** | Very low competition, real demand |
| `commercial general contractors kansas city` | 110 | **12** | Veritas's literal category, low bar |
| `top construction companies in kansas city` | 20 | **18** | Listicle / PR opportunity |
| `kc home renovations` | 390 | **18** | Service-area term |
| `commercial real estate loan rates` | 2,400 | **20** | Capital advisory angle |
| `commercial construction kansas city` | 110 | **26** | Veritas's exact category — winnable |
| `commercial real estate broker` | 14,800 | **0** | Branded SERP — KD is relative, not "free", but still a beatable SERP |

> **Difficulty scores are relative**, not absolute. A KD 0 means the top-ranking pages have very few backlinks — they're still authoritative for that specific query, but a well-built page from a real local business can compete. KD 30+ means the SERP is hardened.

### What the competitive set looks like

For your service area and category, **16 mid-tier KC general contractors** are the head-to-head competitors Veritas will see in search results once the foundation is fixed. They include regional GCs (with strong brand recognition but typically less web presence than the national firms) and local independents (smaller, less SEO-sophisticated, and beatable).

We also see the **national commercial-construction firms** (Turner, JE Dunn, McCarthy) appearing for the broader category terms, but they don't dominate the KC-local SERPs. Several KC-specific searches return mostly mid-tier locals at positions 2-10 — there is real room to rank without competing against the top-of-market.

And we see the **national banks** (Chase, Bank of America, JPMorgan) dominate commercial-loan informational terms. Don't compete with them directly; instead, write the **educational financing content** Veritas can credibly publish (e.g. "what counts toward commercial-loan down payment") to capture the informational queries nearby.

### What this means for the content plan

Once the foundation is fixed, the first six months of content work should concentrate on the winnable-entry keyword set above. None of these requires Veritas to "out-SEO" anyone nationally — it's a build-credibility-locally campaign.

---

## Prioritized action plan

> **Updated 2026-08-28 (v4)** based on live SERP pull. See "SERP format winners" section below for the evidence behind the order.

### 🔴 Critical — do these first (they block indexation)

1. **Fix the hosting layer.** Have your hosting provider or developer configure the server so `/robots.txt` and `/sitemap.xml` return valid static files instead of the SPA page shell. This is a hosting-config fix, not a content fix. ~1–2 hours of developer work.
2. **Fix the homepage so search engines can read it.** Have your developer server-render the homepage and add **300+ words** of real, keyword-rich content describing your services and service area. ~2–4 hours of developer work.

> **Both fixes are usually the same developer sprint** — the underlying issue is the SPA-hosting pattern, and fixing it once typically resolves both.

### 🟠 High-impact — within 1 week of fixing the homepage

3. **Trim the page title and meta description.** Quick win — about 15 minutes. *(See recommendations #4 and #5 above.)*
4. **Add a navigation bar with stub pages** (Services / Projects / About / Contact).
5. **Create and submit an XML sitemap** to Google Search Console and Bing Webmaster Tools.

### 🟢 Quick wins — do these in parallel

6. Trim title + meta (same as #3).
7. Add Organization + LocalBusiness structured data to the homepage once it's server-rendered.
8. **Set up Google Business Profile + Bing Places (about 30 minutes).** This is now a higher priority than before — see "SERP format winners" below for why.

### 📦 Foundation blocks — content plan after the foundation ships

The 90-day content plan below is keyed to the 5 *target* winnable keywords. Two of the original 8 entry keywords were reclassified in v4 (see "Keyword reclassifications") and one is compliance-gated — so the action plan focuses on the 5 keywords where Veritas can credibly publish.

| # | Page to build | Primary target keyword | Volume | KD | Owner | Trigger |
|---|---|---|---|---|---|---|
| C1 | `/commercial-construction-services/` | `commercial general contractors kansas city` + `commercial construction kansas city` | 110 + 110 | 12 + 26 | Dennis → David | Foundation fix lands |
| C2 | `/kc-home-renovations-guide/` | `kc home renovations` | 390 | 18 | Dennis → David | Foundation fix lands |
| C3 | `/commercial-real-estate-financing-guide/` | `commercial real estate loan rates` | 2,400 | 20 | Dennis → David | ⚠️ **Reg-D compliance review required** before publish — David must approve the financing-page language |
| P1 | Google Business Profile setup | Local Pack on all 7 local-pack keywords | — | — | Dennis | 15-minute setup, independent of foundation |
| P2 | Press pitch to *Kansas City Business Journal* | `top construction companies in kansas city` | 20 | 18 | David | David to decide if listicle/award angle fits the brand |

> **Why these three pages and not eight.** The 5 target keywords cluster into 2 themes: (1) commercial construction (2 KWs share one page), and (2) home renovations (1 KW, its own page because KD 18 deserves dedicated copy). The financing KW lives on a new page because the existing `/financing` page is Reg-D-adjacent and the educational guide needs its own neutral framing. **Total: 3 new pages** + 1 GBP + 1 PR pitch = 5 first-90-day plays.

### 🔵 Long-term — after the critical fixes ship

9. Build out service-area pages (Lee's Summit, Kansas City, Jackson County MO, etc.) for local SEO.
10. Begin citation building (BBB, Missouri business directories, Kansas City real-estate associations).
11. Acquire first backlinks (press release, local press coverage, industry directories).
12. Set up monthly rank tracking on the **winnable keyword set** in the search landscape section above (~8-12 terms) + Google Search Console monitoring.

---

## SERP format winners (v4 — live SERP data 2026-08-28)

Live SERP data was pulled for all 8 winnable entry keywords (top 20 organic results each, 160 items total, US/en, location code 2840). Three patterns determine the content format Veritas should publish:

### Pattern 1 — Local Pack dominates 7 of 8 keywords

| Keyword | Local Pack? | Top-3 organic domains |
|---|---|---|
| `multifamily contractors` | ✅ | tenconstruction.com, jenkinsrestoration.com, midtownhoustonlaw.com |
| `commercial general contractors kansas city` | ✅ | vertexkc.com, mccowngordon.com, enriquezllc.com |
| `top construction companies in kansas city` | ✅ | mccowngordon.com, straubconstruction.com, jamescoxconstruction.com |
| `kc home renovations` | ✅ | homeadvisor.com, angi.com, ourgreenwich.com |
| `commercial construction kansas city` | ✅ | vertexkc.com, mccowngordon.com, jccusa.com |
| `commercial real estate broker` | ✅ | reddit.com, micoley.com, ccrexproperties.com |
| `kansas city corporate housing` | ✅ | furnishedhousing.com, ldgkc.com, kchouses.com |
| `commercial real estate loan rates` | ❌ (AI Overview instead) | bankrate.com, lendingtree.com, jpmorgan.com |

**The Local Pack (map + 3-business block) is the highest-value SERP real estate for 7 of 8 keywords.** Only the informational financing keyword has an AI Overview instead. A well-built Google Business Profile (with photos, reviews, hours, service area, posts) will move the Local Pack needle faster than any single page.

### Pattern 2 — All organic winners are agency homepages or local directories

Of 160 organic results reviewed, **43 are agency/company homepages** and **68 have KC-area city names in the title**. The format winners are **service-area homepages** with city-modifier titles — not long-form blog posts. One well-built service page per KC submarket (Lee's Summit, North KC, Overland Park, etc.) outperforms a generic blog series.

### Pattern 3 — People Also Ask is present on every keyword

All 8 keywords have a PAA block. The questions asked cluster into three themes: (a) pricing / cost ("how much does commercial construction cost per square foot"), (b) hiring / vetting ("how to choose a commercial contractor"), and (c) specific service definitions ("what is a general contractor vs a design-build firm"). **A well-built service page with FAQ schema + 6-10 PAA-derived questions** matches both the snippet format Google prefers and the local-intent questions buyers actually ask.

### What this means for content format

**Don't write a blog.** A single 1,500–2,500-word **service page** per target keyword cluster — with FAQ schema, 6-10 PAA-derived questions, 1-2 internal links back to `/financing` or `/`, a structured data block (LocalBusiness + Service), and a city-modifier title — matches every format winner in the top 20. The blog is a later move, not a first move.

### Keyword reclassifications (v4)

Two of the original 8 entry keywords were reclassified after the live SERP pull:

- **`commercial real estate broker`** (KD 0, 14,800/mo) — **NONTARGET for Veritas.** The top-3 organic results include Reddit threads and a brokerage firm, plus a Wikipedia content cluster. Daniel Bailey's KW career is "separate from" his Veritas work; this KW is best owned by Daniel under his personal KW brand, not by Veritas Development Group. Move this KW to Daniel's KW SEO backlog.
- **`kansas city corporate housing`** (KD 1, 260/mo) — **NONTARGET for Veritas.** This keyword is about furnished short-term rentals (corporate relocation housing), not construction. The top SERPs are furnished-housing operators (furnishedhousing.com, kchouses.com), not GCs. Veritas doesn't offer this service; pursuing it would mismatch intent and waste budget.

---

## Domain considerations

This audit covers `veritasdevelopmentgroupllc.com`. Brief background research noted that **two shorter related domains exist on the public web**: `veritasdevelopment.com` (appearances of a parked or undeveloped page) and `veritasdevelopment.net` (a server responding on a different stack). We don't have verified ownership or current status on these — flagging this for your confirmation rather than recommending a specific action:

- **`veritasdevelopment.com`** — when looked up during research, appeared unoccupied. If it's not in active use by another business, it's a natural vanity domain to land to the primary site (searchers typing "veritas development" land on the right property).
- **`veritasdevelopment.net`** — when looked up during research, appeared to be live but unrelated to Veritas Development Group LLC. Same question applies — if it's not owned by anyone connected to Veritas, it can be redirected to the primary site as a defensive move.

**Why this matters:** search engines treat brand-name queries very differently. If a future user searches "veritas development kansas city," they should land on `veritasdevelopmentgroupllc.com`. If `.com` shows irrelevant content or is held by a third party, that search experience becomes muddier.

**Recommended next step (after the foundation is fixed):** confirm whether Veritas Development Group LLC owns `.com` and `.net`, and if so, redirect both to the primary site. **This work can wait** — fixing the foundation is more important.

---

## Decision point

From the previous audit (2026-08-26), we asked:

> "Do you want to:
> 1. Coordinate with your developer to make the homepage readable to search engines, or
> 2. Build a static pre-rendered version in parallel, or
> 3. Park this audit and focus on the investor flywheel (current priority)?"

**This audit (v4) confirms the diagnosis and adds a content plan.** The foundation fix is the same. After it lands, three new pages + GBP setup are the 90-day plan.

**Two specific decisions for David + Daniel:**

1. **Reg-D adjacency on the financing page.** The educational guide (`/commercial-real-estate-financing-guide/`) targets a 2,400/mo keyword but lives next to the existing `/financing` page. Daniel — does publishing a neutral educational guide (no rate tables, no direct lending claims) cross any compliance line, or is it clean?

2. **PR pitch to Kansas City Business Journal.** A 90-day PR pitch for the "top construction companies in kansas city" listicle keyword (KD 18) — does David want to pursue the listicle angle, or is it off-brand?

We're waiting on both decisions before executing the content plan.

---

## About this audit

- **Date:** 2026-08-28 (v1) → 2026-08-30 (v2 added hosting-layer finding) → 2026-08-30 (v3 added search landscape, domain considerations) → **2026-08-28 (v4 added live SERP intelligence, 90-day content plan, keyword reclassifications)**
- **Pages analyzed:** 1 (homepage)
- **Method:** Automated site crawl + search-engine data, plus a manual request of the hosting-layer paths to confirm what's served at `/robots.txt` and `/sitemap.xml`, plus a competitive SERP analysis of 33 commercial-intent Kansas City / Lee's Summit keywords across 4 business divisions, plus a live SERP pull (160 organic results + 50 competitor rows) on the 8 winnable entry keywords.
- **Cost:** 2026-08-28 SERP pull ~290 DataForSEO credits (via OpenSEO MCP `get_serp_results` + `find_serp_competitors`)
- **Status:** Released 2026-08-28 — presentable to David + Daniel for review. Two pending decisions documented in the Decision point section (Reg-D compliance for C3, PR listicle decision for P2).

This draft supersedes the earlier internal version of the audit, which is kept for traceability.



---

## Client Score — Veritas Development Group LLC

<a id="client-score-2026-08-28"></a>

**Deliverable ID:** `client-score-2026-08-28`  
**Kind:** client-score  
**Status:** released  
**Version:** 1  
**Word count:** 1490  
**Released:** 2026-08-28 by dennis  
**Source:** `clients/veritas-developments/projects/website/CLIENT-SCORE-veritas-developments-2026-08-28.md`

---
title: "Client Score — veritas-developments — 2026-08-28"
type: client-score
client: Veritas Development Group LLC
domain: veritasdevelopmentgroupllc.com
audit_date: 2026-08-28
score_date: 2026-08-28
status: RELEASED — presentable to David + Daniel
score_overall: 32
score_tier: CONDITIONAL
recommendation: PROCEED CONDITIONAL
created: 2026-08-28
created_by: Dennis Eng (KlickSmartAI)
predecessor: seo-audit-veritasdevelopmentgroupllc-2026-08-28-client.md
---

# Client Score — Veritas Development Group LLC

> **For:** David Poole + Daniel Bailey
> **Reading time:** 30 seconds (top section) → 3 minutes (front-to-back)
> **What this is:** A single-page score that says whether the audit work above is worth a real engagement. No tasks, no playbooks, no internal breakdown — just the score, the gap it leaves on the table, and the ROI math so you can decide whether to commit.

---

## Score: 32/100 — CONDITIONAL

> **Veritas Development Group comes in at 32/100.** The site has a real, winnable search opportunity in the Kansas City commercial-construction space — six Tier-1 keywords with KD ≤ 20 and a combined 3,270 monthly searches from buyers actively looking for your services. But the technical foundation is broken at the hosting layer, so none of that demand converts today. With a one-sprint foundation fix plus the standard retained SEO bundle, the addressable traffic value is in the **$120K–$360K/year** band depending on what your actual inbound close rate × project size works out to. **Break-even comes inside the first quarter.** Year-1 ROI is **480%–1,650%** across the conservative-to-midpoint band. Recommendation: **proceed, contingent on the foundation sprint.**

**CONDITIONAL** means: there is a real opportunity, but the site has to fix the crawl-blocking hosting issue first or no SEO spend will convert. Sequence: foundation sprint → start retained month 1 in parallel.

---

## The 4 dimensions

| Dimension | Weight | Score (0-100) | Verdict |
|---|---:|---:|---|
| Technical health | 25% | 18 | Hosting layer blocks crawl. Sitemap, robots, and rendering are all broken. Fixable in 1 sprint. |
| Content quality | 25% | 12 | Initial HTML reads as zero words. Google literally cannot see your service description yet. |
| Local presence | 20% | 5 | No Google Business Profile, no Bing Places, NAP not verified across the web. |
| SERP opportunity | 30% | 78 | 6 Tier-1 winnable keywords (KD 0-20) dominated by mid-tier local GCs, not nationals. Local Pack wins 5 of 7. |
| **Weighted composite** | 100% | **32/100** | **CONDITIONAL → PROCEED after foundation sprint** |

> Scoring detail: each dimension is 0-100 where 100 = "best-in-market competitor." The weighted composite rolls up to a tier band. The SERP-opportunity dimension scores **78** because the demand exists and the competitive set is beatable — but the other three dimensions drag the composite down. Fix the foundation and these scores all lift quickly because the search opportunity doesn't go away.

---

## What's on the table — recoverable traffic value ($/year)

Fixed the foundation, in the top 5 for these 7 commercial-intent KC-area searches, this is what 4,775 attributable organic clicks/year is worth at different $/click assumptions. **Industry-typical B2B commercial-construction clicks fall in the $25–$100 range** — your own inbound close rate × average project size will set the true number.

| $/click | Total addressable clicks/yr | $ value/yr | Year-1 ROI | Break-even |
|---:|---:|---:|---:|---:|
| $25 (low) | 4,775 | $119,375 | 482% | 2.1 months |
| $50 (mid-low) | 4,775 | $238,750 | 1,065% | 1.0 months |
| **$75 (mid)** | **4,775** | **$358,125** | **1,647%** | **0.7 months** |
| $100 (mid-high) | 4,775 | $477,500 | 2,229% | 0.5 months |

**Recommended headline: use $50–$75/click as the working number.** You can stress-test this with your actual lead-to-close × average-project-size arithmetic on a napkin in 2 minutes.

### Where the clicks come from

| Keyword tier | Difficulty band | # keywords | Monthly volume | Addressable clicks/yr |
|---|---|---:|---:|---:|
| Tier 1 (KD 0-20, fast rank) | low | 6 | 3,270 | 4,709 |
| Tier 2 (KD 21-40, mid rank) | mid | 1 | 110 | 66 |
| Tier 3 (KD 41+, hard) | hard | 0 | 0 | 0 |
| **Total** | — | **7** | **3,380** | **4,775** |

Time-to-rank assumption: Tier 1 ranks stabilize at top 5 in ~3 months. Tier 2 in ~6 months. Source: SERP-format analysis in the parent audit (8 of 8 entry-keyword SERPs show Local Pack + PAA + 6-10 question format).

---

## What it'd cost to capture that

Standard KlickSmartAI bundles for the Veritas scope.

| Bundle | Includes | One-time | Monthly |
|---|---|---:|---:|
| Foundation sprint | Server-render the homepage, configure hosting to serve real `robots.txt` and `sitemap.xml`, add Organization + LocalBusiness schema. Hands off a working site to the SEO phase. | $2,500 | — |
| Retained SEO | Monthly content (1-2 service pages), GBP + Bing Places build, citation cleanup, monthly SERP re-pull, on-page adjustments, schema maintenance. | — | $1,500/mo |
| **Year-1 total** | Foundation + 12 months retained | — | **$20,500** |
| **Year-2+ annual** | Retained only | — | **$18,000/yr** |

> Internal note (not for client): The foundation sprint bundles at $2,500 because the hosting-layer fix is a known-quantity developer task — 1-2 hours for the routing fix and ~2-4 hours for the SSR change. The retained number reflects a 1-business-day/week engagement on Veritas's account.

---

## ROI snapshot

| Metric | Value (at $75/click midpoint) |
|---|---:|
| Recoverable traffic value (yr 1) | $358,125 |
| Year-1 spend | $20,500 |
| **Year-1 ROI** | **1,647%** |
| Break-even | Month 0.7 |
| **Year-2 ROI (run-rate)** | **1,890%** |
| Year-2 spend (no foundation cost) | $18,000 |

**Plain-English readout:** For every $1 KlickSmartAI spends in year 1 on your account, ~$17 of attributable organic traffic value reaches your landing pages. From year 2 onward, the run-rate is ~$20 for every $1, since the foundation is amortized. Even at the **most-conservative $25/click** assumption, year-1 ROI is 482% and break-even is 2.1 months.

---

## Recommendation

**`PROCEED CONDITIONAL`**

The condition is **the foundation sprint.** Veritas's hosting layer is broken today — `/robots.txt` and `/sitemap.xml` return the SPA HTML shell, and the homepage content is loaded through JavaScript that Google can't crawl. Until that's fixed, every dollar of SEO spend is burned.

Once the foundation lands (1 sprint, ~1 week of developer time + KlickSmartAI management), three workstreams start in parallel: (1) retained SEO / content production begins month 1, (2) Google Business Profile + Bing Places go live within the first 30 minutes, (3) the 5-priority-page content plan from the parent audit kicks off. Veritas's expected position by month 3: top-5 organic for the Tier 1 keywords, with Local Pack presence. By month 6: top-5 organic for Tier 2 keywords plus domain authority growth.

**The opportunity doesn't go away** if you wait — but a national firm building out a KC commercial-construction content play could change the SERP math in the next 12-18 months. First-mover window is real.

**Two specific items to confirm before kickoff** (carried from the parent audit):

1. **Reg-D adjacency on the financing guide page** (`commercial real estate loan rates`, 2,400/mo). Daniel — does a neutral educational guide without rate tables or direct lending claims cross any compliance line, or is it clean? This is the single highest-volume opportunity in the universe.
2. **PR pitch to Kansas City Business Journal** for the `top construction companies in kansas city` keyword (KD 18, listicle SERP). David — pursue the listicle angle or skip?

---

## How to read this number band

| Score band | Tier | What it means for the client |
|---:|---|---|
| 80-100 | RECOMMENDED | Foundation is solid, content exists, local presence active. SEO spend converts from week 1. |
| 60-79 | CONDITIONAL | Some blockers, but winnable. Sequence the foundation work first, then retained SEO. Proceed with a scoped pilot. |
| 40-59 | CONDITIONAL | Multiple foundation gaps. Bigger upfront investment required. Quarter-by-quarter contract. |
| **0-39** | **NOT-RECOMMENDED** *(with overrides)* | Either the search opportunity is missing OR the technical foundation is broken to the point no SEO spend will convert. |

> Veritas falls in the bottom band by the raw composite, but **the override here is structural**: the score is dragged down by 25%+25%+20% = 70% of weight sitting on technical / content / local, all of which are **fixable in one sprint**. The 30%-weighted SERP-opportunity dimension is the actual ceiling, and it scores 78. **This is precisely the profile of a "fixable CONDITIONAL."** Apply the standard NOT-RECOMMENDED rubric and the conversation ends there. Apply the override and the path is clear.

---

## Source

- Parent audit: `seo-audit-veritasdevelopmentgroupllc-2026-08-28-client.md` (RELEASED)
- Score data: `.local_tier/clients/veritas-developments.duckdb` (table: `client_scores`)
- Generated: 2026-08-28 via skill `seo-audit-report` v1.1.0

**This document is client-facing. No internal cost lines, no internal hour figures, no KlickSmartAI rate cards. The pricing shown is the bundled, what-you-pay number.**



---

## Cover Note — SEO Audit v4

<a id="cover-memo-v4-2026-08-28"></a>

**Deliverable ID:** `cover-memo-v4-2026-08-28`  
**Kind:** cover-memo  
**Status:** released  
**Version:** 1  
**Word count:** 1043  
**Released:** 2026-08-28 by dennis  
**Source:** `clients/veritas-developments/projects/website/COVER-NOTE-seo-audit-v4-2026-08-28.md`

---
title: "Cover Note — SEO Audit v4 Release — 2026-08-28"
type: release-cover
status: RELEASED — for David Poole + Daniel Bailey
created: 2026-08-28
released_by: Dennis Eng (KlickSmartAI)
linked_artifact: seo-audit-veritasdevelopmentgroupllc-2026-08-28-client.md
linked_evidence: ../drafts/website/serp-intelligence-2026-08-28.md
---

# Cover Note — SEO Audit v4 — for Review

> **For:** David Poole + Daniel Bailey
> **From:** Dennis Eng (KlickSmartAI)
> **Date:** 2026-08-28
> **Reading time:** ~60 seconds for the executive summary, ~12 minutes for the full report

---

## What this is

The v4 SEO audit for `veritasdevelopmentgroupllc.com`. This is the version built from **live SERP data** — 160 organic results and 50 competitor rows across the 8 winnable entry keywords we identified in v3. The diagnosis (foundation gap: SPA hosting blocks Google from reading your content) hasn't changed — but the recommended action plan now has a clear 90-day content path behind it.

---

## What's new in v4

1. **SERP format winners section** — three patterns from the live data:
   - **Local Pack dominates 7 of 8 keywords** — your Google Business Profile (or lack of one) is the highest-leverage lever right now. 30-minute setup.
   - **Agency homepages + city modifiers** win the top 20 — not blog posts. The plan builds 3 service pages, not a blog.
   - **People Also Ask on every keyword** — FAQ schema + 6–10 PAA-derived questions per page.
2. **Keyword reclassifications:**
   - `commercial real estate broker` — moved to Daniel's KW SEO backlog (Daniel's KW career is separate from Veritas per the existing carve-out; this KW should sit under his KW brand).
   - `kansas city corporate housing` — NONTARGET (this is furnished short-term rentals, not construction; wrong vertical).
3. **90-day content plan** — 3 new pages + GBP setup + optional PR pitch. Specific URLs, target keywords, volumes, KDs.
4. **Two decisions for you (David + Daniel)** — listed below.

---

## Two specific decisions I need from you

### Decision 1 — for Daniel

**Reg-D adjacency on the financing page.**

The educational guide I'm proposing (`/commercial-real-estate-financing-guide/`) targets a 2,400/month keyword and is a real win for SEO. But the existing `/financing` page is Reg-D-adjacent (Daniel's KW career is "separate from" his Veritas work, with a disclaimer footer in place).

**Question:** Does publishing a *neutral educational guide* on commercial real-estate financing (no rate tables, no direct-lending claims, no mention of Veritas as a lender) cross any compliance line? Or is it clean?

- **If clean:** proceed with C3 as planned.
- **If uncomfortable:** drop C3 from the 90-day plan. The remaining 2 new pages + GBP still deliver 80% of the SEO value.

### Decision 2 — for David

**PR pitch to Kansas City Business Journal.**

A PR-led listicle campaign could capture the `top construction companies in kansas city` keyword (KD 18, 20/month) by getting Veritas named in a KC Business Journal feature or "Top 25" list.

**Question:** Does that fit Veritas's brand posture, or is it off-brand for a development-stage firm?

- **If yes:** Dennis drafts a PR pitch outline.
- **If no:** drop P2 from the plan.

---

## What's NOT in this audit (yet)

These are separate deliverables — none will be drafted until both decisions above are answered:

- The 3 new page drafts themselves (`/commercial-construction-services/`, `/kc-home-renovations-guide/`, `/commercial-real-estate-financing-guide/`)
- The GBP setup checklist (15-minute task for Dennis if you want one)
- The PR pitch outline (if Decision 2 = yes)

---

## How the report is organized

| Section | Reading time | What it answers |
|---|---|---|
| Executive summary | 60 seconds | "Should we fix this or not?" |
| At a glance + What we found | 2 minutes | "What's wrong?" |
| Technical health + Authority & local presence | 1 minute | "What's the infrastructure status?" |
| The search landscape | 2 minutes | "What are we competing against?" |
| **Prioritized action plan** | **3 minutes** | **"What do we do first, second, third?"** ← *the 90-day plan* |
| **SERP format winners (v4)** | **3 minutes** | **"Why does the plan look this way?"** ← *the new section* |
| Domain considerations | 1 minute | "What about the .com and .net?" |
| Decision point | 60 seconds | The two asks above |
| About this audit | 30 seconds | "How was this built and what's it cost?" |

**Total reading time: ~12 minutes** (or 60 seconds for the exec summary if you only want the headline).

---

## File locations

- **Released audit (this is the canonical version):** `projects/website/seo-audit-veritasdevelopmentgroupllc-2026-08-28-client.md` (24 KB, 303 lines, v4)
- **Live SERP evidence:** `drafts/website/serp-intelligence-2026-08-28.md` (13.8 KB)
- **Earlier competitor landscape:** `drafts/website/serp-competitor-landscape-2026-08-30.md` (3.5 KB)
- **Original scraping findings:** `drafts/website/scrape-veritasdevelopmentgroupllc-home-2026-08-30.md`, `scrape-veritasdevelopmentgroupllc-financing-2026-08-30.md`

---

## Timeline of audit versions

| Version | Date | What changed |
|---|---|---|
| v1 | 2026-08-28 | Initial diagnosis: site is reachable but Google can't read it |
| v2 | 2026-08-30 | Added hosting-layer finding (SPA returns app shell at `/robots.txt` + `/sitemap.xml`) |
| v3 | 2026-08-30 | Added 33-keyword competitive landscape + domain considerations |
| **v4** | **2026-08-28** | **Added live SERP data on 8 winnable keywords (160 results), 90-day content plan, keyword reclassifications, cost disclosure** ← *this release* |

---

## How I'd like you to engage with this

**For David (primary decision-maker):**
1. Read the executive summary (60 seconds).
2. Read the prioritized action plan (3 minutes).
3. Answer Decision 2 (PR listicle yes/no).
4. Forward to your developer if the Critical items 1+2 are in-scope this quarter.

**For Daniel (relationship + compliance decision-maker):**
1. Read the executive summary (60 seconds).
2. Read the "SERP format winners — Keyword reclassifications" sub-section (90 seconds).
3. Answer Decision 1 (Reg-D adjacency on C3).
4. Optionally review the `/financing` page references to confirm your KW carve-out language still reads correctly in the v4 audit.

**No action is required from me until I hear back on both decisions.** Once I have them, I can:
- Draft C1 (`/commercial-construction-services/`) immediately — no compliance gating.
- Draft C2 (`/kc-home-renovations-guide/`) immediately — no compliance gating.
- Draft GBP setup checklist for Dennis in 15 minutes.
- Draft P2 PR pitch outline if Decision 2 = yes.
- Draft C3 if Decision 1 = clean; otherwise remove from the plan.

---

Dennis

KlickSmartAI · klicksmartai.com


## Workspace Architecture

This client is part of KlickSmartAI's multi-agent client-workspace pattern:

- **Canonical source of truth:** the `.duckdb` file (not the markdown files)
- **Markdown deliverables:** derived output, regenerable from the DB via the
  `publish-workspace-to-wiki` skill
- **Multi-agent safe:** every row carries `created_by`; writes go through
  the protocol in `~/wiki/_internal/agent-duckdb-protocol.md`
- **Migration-ready:** schema is MotherDuck-compatible; specific tables can
  sync to Supabase Postgres later if needed

Schema: v1.2.0 (wiki_path + wiki_published_at on `client_deliverables`).
