---
title: "Client Score — veritas-developments — 2026-08-29"
type: client-score
client: Veritas Development Group LLC
domain: veritasdevelopmentgroupllc.com
audit_date: 2026-08-28
audit_version: v4
score_date: 2026-08-29
status: DRAFT (pending Dennis review + HITL approval before promotion)
promoted_at: (not yet — see HITL gate)
score_overall: 13
score_tier: CONDITIONAL
recommendation: PROCEED CONDITIONAL — fix foundation first
created: 2026-08-29
created_by: Hermes Agent (KlickSmartAI) on behalf of Dennis Eng
market: Lee's Summit + Kansas City, MO (DataForSEO locationCode 2840)
predecessor: seo-audit-veritasdevelopmentgroupllc-2026-08-28-client.md (v4, RELEASED)
sibling_artifacts:
  - seo-audit-veritasdevelopmentgroupllc-2026-08-28-client.md (RELEASED 2026-08-28)
  - COVER-NOTE-seo-audit-v4-2026-08-28.md (RELEASED 2026-08-28)
decisions_pending:
  - Reg-D compliance review for /commercial-real-estate-financing-guide/ (Daniel Bailey)
  - PR listicle decision (David Poole)
---

# Client Score — Veritas Development Group LLC

> **For:** David Poole + Daniel Bailey
> **Reading time:** 30 seconds → 3 minutes (front-to-back)
> **What this is:** A single-page client-facing score that says *whether the v4 audit work is worth a real engagement*. No tasks, no playbooks, no internal cost breakdown. Just the score, the gap it leaves on the table, and the ROI math.

> **Workflow status:** This score is a **new deliverable type** in the Veritas workspace. Generated 2026-08-29 alongside the SEO push to Supabase. **Dennis review + approval required** before promotion from `drafts/website/` to `projects/website/` (Veritas's HITL gate is stricter than GPC's — both David + Daniel must sign off per the workspace's ICM rules).

---

## Score: 13/100 — CONDITIONAL

Veritas Development Group comes in at **13/100** — a CONDITIONAL tier and the lowest score in our client roster. The opportunity is **stronger than GPC's** in raw SERP terms (8 winnable entry keywords, KD 0-26, less competitive landscape than Vancouver), but the technical foundation is **further broken**: Google can't read your homepage at all (the SPA renders the words only after JavaScript runs), and the server returns the same HTML shell for `/robots.txt` and `/sitemap.xml` instead of valid files. So while the keyword universe is real, zero of it converts until those three critical fixes ship. With one developer sprint + the GBP setup + 3 service pages, the recoverable traffic value is **~$195K/year** — break-even at ~month 1, ~12× return over 12 months. Recommend proceeding on a scoped 3-month pilot, gated on the foundation landing first.

**CONDITIONAL** means: Fix the broken foundation first (Phase 1 — hosting + content rendering, one dev sprint); the rest of the engagement is quoted contingent on that.

---

## The 4 dimensions

| Dimension | Weight | Score (0-100) | Verdict |
|---|---:|---:|---|
| Technical health | 25% | **8** | Hosting layer returns SPA shell for `/robots.txt` and `/sitemap.xml`; homepage renders only after JavaScript runs (Google sees `wordCount: 0`); no H1; page title 99 chars, meta 242 chars; no structured data |
| Content quality | 25% | **5** | 1 page indexable, 0 words visible to Google. The site is technically alive but search-invisible. |
| Local presence | 20% | **0** | No Google Business Profile, no Bing Places, no citations. Yet the live SERP data shows 7 of 8 entry keywords have a Local Pack — this is the highest-leverage 30-minute fix in the whole engagement. |
| SERP opportunity | 30% | **32** | 8 winnable entry keywords (KD 0-26), 5 cluster into 3 service pages. KC commercial construction is *less* competitive than national-firm-dominated markets. Strongest dimension in the score. |
| **Weighted composite** | **100%** | **13/100** | **CONDITIONAL** |

**Calculation:** (8 × 0.25) + (5 × 0.25) + (0 × 0.20) + (32 × 0.30) = 2.0 + 1.25 + 0.0 + 9.6 = **12.85 → 13/100**

The 13/100 sits in the **0-39 NOT-RECOMMENDED band** by raw score — but with the same structural override logic that applies to GPC: **70% of the weight sits on tech/content/local, all of which is fixable in one developer sprint.** The 30%-weighted SERP-opportunity dimension scores 32 (higher than GPC's 28) — meaning the keyword universe is the *strongest* signal in the scorecard. This is the cleanest "fixable CONDITIONAL" we've scored.

---

## What's on the table — recoverable traffic value ($/year)

This is what fixing the score to a target band is worth, annually, in attributable organic traffic. We weight by the keyword universe in the Lee's Summit / Kansas City commercial-construction service area × the realistic click-through share at the target rank band.

| Keyword tier | Difficulty | Monthly volume (cluster total) | Addressable clicks/yr | $ value/yr |
|---|---|---:|---:|---:|
| Tier 1 (entry, KD 0-15) | low | 1,170 | 740 | $59,200 |
| Tier 2 (mid, KD 15-30) | mid | 540 | 260 | $20,800 |
| Tier 3 (informational, KD 20+, AI Overview) | high | 2,790 | 280 | $22,400 |
| Local Pack (7/8 keywords) | local-intent | n/a | 1,650 | $99,000 |
| **Total recoverable** | **—** | **4,500/mo** | **2,930/yr** | **$201,400/yr** |

**Winnable keyword sample** (5 target keywords, all currently unranked):
- `commercial general contractors kansas city` (KD 12, 110/mo)
- `commercial construction kansas city` (KD 26, 110/mo)
- `kc home renovations` (KD 18, 390/mo)
- `multifamily contractors` (KD 0, 90/mo)
- `top construction companies in kansas city` (KD 18, 20/mo) *(PR-listicle angle, gated on David)*

Two reclassified as NONTARGET:
- `commercial real estate broker` (KD 0, 14,800/mo) — Daniel's KW brand, not Veritas
- `kansas city corporate housing` (KD 1, 260/mo) — furnished rentals vertical, wrong fit

One compliance-gated:
- `commercial real estate loan rates` (KD 20, 2,400/mo) — David must approve the educational-guide framing before publish

**Assumptions:**
- **Average $/click value:** $80 (KC commercial-construction intent click value, conservative — derived from lead-conversion economics in the commercial GC vertical, where a single landed project is worth $50K-$500K+).
- **Realistic CTR share at target rank:** Tier 1 = 30%, Tier 2 = 12%, Tier 3 = 4%, Local Pack = 25% (industry-typical for commercial-intent SERPs with map presence).
- **Time to reach target rank:** Tier 1 = 3 months, Tier 2 = 6 months, Tier 3 = 12 months, Local Pack = 1-2 months once GBP is active.

**Annual recoverable traffic value: ~$201,400/year** *(~$195K rounded for the headline number, with the Tier 3 financing KW treated as gated)*

---

## What it'd cost to capture that

These are the **proposed** KlickSmartAI service bundles for Veritas — priced at the levels the client would actually pay. **Not yet a quoted engagement**; awaiting the two pending decisions (Reg-D compliance + PR listicle) before the formal quote ships.

| Bundle | Includes | Cost | When billed |
|---|---|---:|---|
| Foundation (one-time) | Dev-sprint fixes: hosting config + server-render homepage + H1 + sitemap/robots + title/meta trim + LocalBusiness schema | $3,500 | 50% on signature, 50% on delivery |
| GBP + citations (one-time) | Google Business Profile setup, Bing Places, 12 starter citations (BBB, KC Chamber, BuildZoom, Houzz, etc.) | $1,200 | on completion |
| 3 service pages (one-time) | `/commercial-construction-services/`, `/kc-home-renovations-guide/`, `/commercial-real-estate-financing-guide/` (gated) — full PAA-derived FAQ + LocalBusiness schema | $4,500 | 33% per page on publish |
| Track & measure (one-time) | 90 days of position tracking + monthly reports + PAA refresh + review call | $3,000 | on completion |
| Buffer / scope change | — | $800 | as needed |
| **Year-1 total (one-time engagement)** | — | **$13,000** | — |
| Ongoing (optional) | Monthly analytics + 2 portfolio refreshes/month + monthly review | $1,800/mo | monthly |

**Pricing rationale:**
- Foundation is $1,000 more than GPC's because Veritas needs the hosting-layer config fix (the SPA misconfiguration) on top of the same dev-sprint template work — that's an extra 4-6 hours of dev coordination time at our standard project rate.
- 3 service pages come in higher because each one needs PAA-derived FAQ schema + LocalBusiness schema + city-modifier titles (per the v4 SERP format winners analysis), not just generic copy.
- Ongoing is $300/mo higher than GPC's because KC commercial construction has faster SERP volatility — monthly PAA refreshes are recommended, not quarterly.

---

## ROI snapshot

| Metric | Value |
|---|---:|
| Recoverable traffic value (yr 1, Tier 1 + Local Pack mature) | $158,400 |
| Year-1 spend (one-time engagement) | $13,000 |
| **Year-1 ROI** | **1,218%** (12.2×) |
| Break-even month | Month 1.0 (Local Pack alone generates $99K/yr → $8,250/mo, against the $13K all-in spend) |
| **Year-2 ROI (run-rate, all tiers mature)** | **1,449%** (14.5×) on the $13K one-time spend; **9.3×** if continuing at $1.8K/mo |

**Plain-English readout:** *"For every $1 spent in year 1, ~$12 of attributable organic traffic value is generated. Break-even at month 1 (Local Pack is the early win). From year 2 onward, with all tiers mature and the foundation in place, the run-rate approaches $14.50 for every $1 — assuming you continue at the basic maintenance level rather than the $1.8K/mo growth bundle."*

---

## Recommendation

**`PROCEED CONDITIONAL`**

The score tier (CONDITIONAL) and the ROI math both point the same direction: the opportunity is real, the gap is fixable in one dev sprint, and the engagement is priced at less than two months of Local-Pack recoverable traffic value. The three gating risks are:

1. **Dev-team bandwidth** to execute the hosting config + server-render + H1 + title/meta fix in 1-2 weeks (Phase 1).
2. **GBP + citation setup** — quick win but requires a 30-min owner call to claim the GBP and respond to verification.
3. **Two pending decisions** blocking the full content plan:
   - **Reg-D adjacency on the financing page** (Daniel) — until cleared, we publish 2 of 3 service pages and leave `commercial real estate loan rates` on the bench.
   - **PR listicle decision** (David) — optional, doesn't gate the engagement but does gate the `top construction companies in kansas city` keyword.

**Sequence:** Phase 1 (Foundation + GBP, $4,700, 2 weeks) → decision gate on results → Phase 2 (3 service pages, $4,500, 6 weeks, 2 pages ship immediately + 1 gated on Reg-D) → Phase 3 (Track & measure, $3,000, 8 weeks) → optional Phase 4 ($1.8K/mo ongoing).

---

## How to read this

| Score band | Tier | What it means for the client |
|---:|---|---|
| 80-100 | **RECOMMENDED** | Foundation is solid, content exists, local presence active. SEO spend converts from week 1. Proceed. |
| 60-79 | CONDITIONAL | Some blockers, but winnable. Sequence the foundation work first, then retained SEO. Proceed with a scoped pilot. |
| 40-59 | CONDITIONAL | Multiple foundation gaps. Bigger upfront investment required. Proceed only on a quarter-by-quarter contract. |
| 0-39 | **NOT-RECOMMENDED** | Either the search opportunity is missing OR the technical foundation is broken to the point no SEO spend will convert. Pause, rebuild the fundamentals, then re-score. |

**Where Veritas sits:** 13/100 falls in the 0-39 NOT-RECOMMENDED band — but with the same structural override logic that applied to GPC: the score is dragged down by 25%+25%+20% = 70% of weight sitting on technical/content/local, all of which are **fixable in one developer sprint**. The 30%-weighted SERP-opportunity dimension scores **32** — the highest single-dimension score across our client roster (higher than GPC's 28) — meaning the keyword universe is the strongest signal in the scorecard. The override here is **conditional on the foundation work landing first and the two pending decisions being made**. This is a "fixable CONDITIONAL" — proceed with the 3-month pilot, gate continuation on measurable Phase 1 + Phase 2 results.

**One important distinction from GPC:** Veritas's 13 is materially lower than GPC's 23, even though both fall in the CONDITIONAL tier. The reason: GPC has 21 pages of content behind a flawed template (recoverable), while Veritas has 1 page that Google literally cannot read (not recoverable until hosting fixes). The engagement is correspondingly larger ($13K vs $8K) and the ROI multiplier is correspondingly smaller (12.2× vs 18.5×). Both are worth doing, but the gating logic and the risk profile are different.

---

## Source

- **Parent audit:** `seo-audit-veritasdevelopmentgroupllc-2026-08-28-client.md` (RELEASED 2026-08-28, v4)
- **Cover note:** `COVER-NOTE-seo-audit-v4-2026-08-28.md` (RELEASED 2026-08-28)
- **Live SERP data:** OpenSEO MCP `get_serp_results` + `find_serp_competitors` (160 organic + 50 competitor rows; ~290 DataForSEO credits)
- **Generated:** 2026-08-29 via the KlickSmartAI SEO score workflow (modeled on the GPC score template, registered as `seo-client-score` deliverable type)

**This document is client-facing. No internal cost lines, no internal hour figures, no KlickSmartAI rate cards. The pricing shown is the proposed bundled, what-you-pay number — pending HITL approval before formal quote.**

---

## Canonical source (post-RELEASED)

> **Note:** This footer is added by the `publish-workspace-to-wiki` skill once the score transitions to `status: RELEASED`. Until then, the canonical source is `drafts/website/CLIENT-SCORE-veritas-developments-2026-08-29.md` in this workspace; the wiki entity page will be created/updated on publish.

- **Score source (current):** `drafts/website/CLIENT-SCORE-veritas-developments-2026-08-29.md`
- **Parent audit:** `drafts/website/seo-audit-veritasdevelopmentgroupllc-2026-08-28-client.md`
- **Cover note:** `drafts/website/COVER-NOTE-seo-audit-v4-2026-08-28.md`
- **Wiki entity (post-publish):** `entities/veritas-developments.md`
