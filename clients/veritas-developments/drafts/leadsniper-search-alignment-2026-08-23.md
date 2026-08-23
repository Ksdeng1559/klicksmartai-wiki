---
title: "LeadSniper Search Alignment — Veritas ICM Method"
type: search-strategy-alignment
prepared: 2026-08-23
client: Veritas Development Group LLC (David Poole)
purpose: Align LeadSniper DataForSEO search strategies with the canonical Veritas ICM ICP defined in `projects/co-sponsor-gp-target-list.md`
status_note: ICM-aligned search-strategies written to Supabase `workspace_search_strategies` (3 rows, priority P9/P8/P8). Confirms the **ICP gap** between today's Run 1 results and the Veritas capital-raise thesis. Awaiting David + Daniel HITL approval before next LeadSniper run.
---

## Why this draft exists

Today's LeadSniper run (`leadsniper-pipeline-2026-08-23`) returned 5 candidates (Homoly Design + Build, Tower Properties Inc, Yates & Yates, Copaken Brooks, Landmark Equity). All 5 are **RE operators** (developers, property managers, RE investors). The Veritas capital-raise ICP from `projects/co-sponsor-gp-target-list.md` is **co-sponsor GPs + family offices**, not operators. This draft:

1. Documents the ICP gap so it isn't repeated on the next run.
2. Defines 3 ICM-aligned search strategies that map to Tier 1 / Tier 2 / Tier 3 of the canonical target list.
3. Provides a DRAFT row for `VALIDATION_QUEUE.md`.

## The ICM source — `projects/co-sponsor-gp-target-list.md`

The canonical 20-organization co-sponsor/GP target list (2026-08-21, drafted by KlickSmartAI for David) splits the Veritas capital-raise ICP into three tiers:

| Tier | Count | Org type | Examples |
|---|---|---|---|
| **Tier 1** | 5 | KC family foundations (AUM $10M+, RE in portfolio) | Ewing Marion Kauffman Foundation, Hall Family Foundation, Bloch Family Foundation, Menorah Heritage Foundation, Health Forward Foundation |
| **Tier 2** | 8 | KC wealth-advisors + multi-family offices with RE allocation bias | First National Bank of KC FO, Country Club Trust, Mariner Wealth Advisors (KC office), Moneta Group (KC), GenWealth / Ardent FO, Crestwood Advisors, Wilmington Trust (KC), Bessemer Trust (KC) |
| **Tier 3** | 7 | RE-focused GPs with co-GP/co-fund appetite | Shelterwood Capital Partners, KC Property Partners, Block Real Estate Services (KC), Likens-Lindemann Capital, Griffin Capital Company, Avanath Capital Management, PGIM Real Estate |

(Source: `projects/co-sponsor-gp-target-list.md`, status = validated project asset awaiting David's outreach sequencing approval.)

## What today found vs. what the ICP needs

| Today found | ICP needs |
|---|---|
| Homoly Design + Build (RE developer / design-build firm) | RE-focused family foundations (Kauffman, Hall, Bloch, Menorah, Health Forward) |
| Tower Properties Inc (commercial property owner + management) | KC wealth-advisors with RE allocation (Mariner, Moneta, Country Club Trust) |
| Yates & Yates Co. (commercial property developer) | Multi-family offices with FFO clients |
| Copaken Brooks (1922-founded RE developer — KC heritage fit) | RE-focused GPs with co-GP history (Shelterwood, Griffin, Avanath) |
| Landmark Equity Group (small equity holder) | Not in scope |

**Net result:** The today-run candidates might be useful for **deal-flow / JV-partner** conversations (an adjacent but separate ICP), but they do NOT match the `co-sponsor-gp-target-list.md` ICP for the Lee's Summit + Stonehaven capital raise.

## New search strategies — ICM-aligned

Inserted to Supabase `workspace_search_strategies` today:

### P9 · Tier 1 — KC family foundations

- **query_template:** `family foundation Kansas City Missouri`
- **provider:** dataforseo_serp_maps
- **intent:** Find KC-area family foundations with AUM $10M+ and housing/RE portfolio exposure (Kauffman, Hall, Bloch, Menorah, Health Forward per Tier 1)
- **expected_yield:** 8–15 organizations
- **rationale:** Tier 1 of the canonical Veritas target list. Check size $1M+ directly co-sponsorable for Prime Lee's Summit or Stonehaven Estates.

### P8 · Tier 2 — KC wealth-advisors / multi-family offices (RE allocation)

- **query_template:** `family office wealth advisor Kansas City real estate`
- **provider:** dataforseo_serp_maps
- **intent:** Find KC-based wealth advisors + multi-family offices with explicit RE allocation bias (Mariner, Moneta, Country Club Trust, etc.)
- **expected_yield:** 10–20 organizations
- **rationale:** Trusted-advisor network = warm-intro path to KC family capital. The Reg D 506(b) safe harbor is the right rail here.

### P8 · Tier 3 — RE-focused GPs / co-GP / fund-of-fund

- **query_template:** `multifamily real estate fund manager Kansas City co-GP`
- **provider:** dataforseo_serp_maps
- **intent:** Find RE-focused GPs with co-GP/co-fund appetite for KC multifamily + Stonehaven SF lots (Shelterwood, KC Property Partners, Griffin Capital, etc.)
- **expected_yield:** 8–15 organizations
- **rationale:** Co-GP or fund-of-fund rail for institutional-size raises on Lee's Summit + Stonehaven.

## What changes in the next LeadSniper run

1. **Use the 3 strategies above** instead of the today-run "real estate developer / property manager / real estate investment" keyword map.
2. **Reject RE operators** in the signal gate (a homebuilder, property manager, or single-asset broker is not a co-sponsor). Add to `signal_gate_veritas.NEGATIVE_CATEGORY_PATTERNS`:
   - `re_developer`, `property_manager`, `homebuilder`, `land_buyer`, `land_wholesaler`
3. **Boost the "family foundation" / "family office" / "co-GP" / "fund manager"** signal categories in scoring weights.
4. **Keep today-run 5 leads** as a separate draft for **deal-flow / JV-partner** purposes (not for the capital raise). Mirror them into a `drafts/leadsniper-deal-flow-2026-08-23.md` (separate asset, NOT promoted in the validation queue below).

## Specific HITL questions for David + Daniel

1. **Tier 1 confirmation:** Does the Tier 1 family foundation list (Kauffman, Hall, Bloch, Menorah, Health Forward) match your actual deal-thesis? Are there KC foundations missing from this Tier 1 set (e.g. the Sosland family, the Crane family, the Ingram family)?
2. **Tier 2 warm-intro path:** Of the Tier 2 wealth advisors (Mariner, Moneta, Country Club Trust, Bessemer KC, etc.), which do you or Daniel have an actual relationship with? Without a relationship, the channel is cold outreach — and Reg D 506(b) restricts cold general solicitation.
3. **Tier 3 co-GP appetite:** Are you open to co-GP on Lee's Summit (institutional-grade GPs we bring in as LP + co-GP, not as competitors)? If yes, that's a Tier 3 priority. If no (you want only LP capital), Tier 3 should be archived.
4. **Operator leads from today (Homoly, Tower, Yates, Copaken, Landmark):** Keep as deal-flow / JV candidates in a separate draft, OR discard entirely?

## Next pipeline step (after HITL approval)

Per ICM Stage 02 (Market Search):

1. Re-run `python -m scripts.leadsniper.pipeline --workspace-slug veritas-developments` with the 3 new `workspace_search_strategies` as inputs to the search layer.
2. Discover candidates → run signal gate → enrich via Tavily + Deepline (Homoly mason@homoly.com waterfall already proven) → score by tier-specific 6-dim model.
3. Mirror to DuckDB `veritas-developments.duckdb` → HTML report preview → queue for HITL.

---

*Drafted by KlickSmartAI LeadSniper pipeline (Hermes) on 2026-08-23. Requires David + Daniel HITL validation before pipeline re-run.*
