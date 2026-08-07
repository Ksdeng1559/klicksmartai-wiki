# Pre-M&A Search Algorithm — Executive Summary

**Test:** Austin, TX — Commercial HVAC · **Date:** 2026-08-06
**Method:** LeadSniperAI Pre-M&A Search Thesis Playbook (validated as runnable algorithm)

---

## TL;DR

The algorithm works. Running it on Austin commercial HVAC surfaced **one emerging pre-M&A candidate** (Wansley Refrigeration — an 82-year-old family business showing classic succession exposure) from **indirect signals only** — no "for sale" listings. This is exactly the off-market pattern the playbook targets.

**Cost of full test:** ~5 credits (1 discovery + 3 mention scans + 1 deep semantic).

---

## Funnel Results

| Stage | Count |
|-------|-------|
| Grounded businesses (Google Maps, Place IDs) | 20 |
| Independents (after chain/PE exclusion) | ~13 |
| Deep-scanned candidates | 3 |
| **Scored pre-M&A candidates** | **3** |
| Classified EMERGING (65-79) | 1 |
| Classified WATCHLIST (50-64) | 1 |
| Classified WEAK (35-49) | 1 |

---

## Ranked Candidates

### 1. Wansley Refrigeration — 🎯 79/100 · EMERGING (relationship campaign)
**The strongest off-market signal in the cohort.**
- **Founded 1944** — 82-year-old, family-owned commercial refrigeration + HVAC business
- **Ownership restructuring:** incorporated as **Roctex LLC in 2013** (a decade of ownership formalization — classic pre-transition structure)
- **Founder dependency:** owner **Dana Rocco** (since 2013) present on job sites; no visible successor; Bailey Rodriguez is a technician/manager, not ownership
- **Digital value-creation gap:** gmail-era contact, 29 Google reviews, **1 employee on LinkedIn** despite 80 years of operation
- **Reputation:** stable (BBB A+ accredited since 1979, 1 resolved complaint)
- **Commercial refrigeration = recurring, mandated demand** (restaurants, grocery, medical — health-code compliance)
- **Evidence level: L2** (2 signal families corroborated: succession exposure + digital gap; no direct succession language found — correctly NOT escalated to diligence)

**Recommended action:** relationship-first outreach to Dana Rocco. Conversation angle: *modernization + growth capital + continuity*, NOT "we want to buy you."

### 2. Airtech Energy Systems — 62/100 · WATCHLIST
- 41-year family business ($5M revenue) but **external President since 2014** (Jon Hyatt) — institutionalization signal
- Not BBB accredited; small digital footprint
- **Entity-resolution win:** algorithm rejected 3 false-positive "Airtech" matches (CA bankruptcy, Louisville bankruptcy, IDEX acquisition) — identity package works
- **Monitor quarterly** for ownership change or leadership transition.

### 3. Gold Eagle Services — 45/100 · WEAK
- Founded 2017, founder (Keating Kuhn) fully active — too early for succession
- One recent negative BBB review ("avoid at all costs") — mild blip, not a pattern
- **Not a candidate now**; revisit in 3-5 years or on owner-retirement signals.

---

## What Validated

1. **Indirect-signal thesis confirmed** — the top candidate emerged from ownership age + structural restructuring + digital gap, not a sale listing
2. **Entity resolution is essential** — 3 of 4 "Airtech" search hits were different companies; domain + Place ID + owner matching rejected all false positives
3. **Scoring discipline works** — Wansley correctly held at L2 (relationship tier) rather than over-claimed as a diligence-ready seller

## Cost Efficiency

| Engine | Calls | Credits |
|--------|-------|---------|
| Deepline openwebninja (discovery) | 1 | ~1 |
| Parallel exact-mention scans | 3 | 3 |
| Exa deep semantic | 1 | ~1 |
| **Total** | **5** | **~5** |

Scale projection (playbook pilot): 2,000-5,000 grounded → ~500 independents → ~300 enriched → 50-100 verified → 25-50 theses → **10+ human-validated conversations** — all credit-gated via `gtm-enrichment-planner` (pilot → approval → full run).

---

## Recommended Next Steps

1. **Relationship outreach to Wansley** (Dana Rocco, LinkedIn-verified owner) — modernization + growth + continuity framing
2. **Add Wansley + Airtech to a quarterly monitoring watchlist** (re-run mention scans on a cadence)
3. **Expand the pilot** to the full Texas Triangle (DFW, Houston, San Antonio) per the playbook
4. **Score the remaining ~10 independents** from the grounded universe (~3 credits)

*All candidates are hypotheses, not confirmed sellers. No "for sale" claims made without credible source per playbook governance.*
