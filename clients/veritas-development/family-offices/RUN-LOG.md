# Family Office Discovery Run — 2026-09-06

**Client:** Veritas Development (Lee's Summit, MO)
**Scope:** 25 MO-domiciled family offices / MFOs with direct real estate signals
**Method:** web_search (routes through Parallel + Exa SDKs) + web_extract for verification
**Cost ceiling:** $100 (parallel/exa SDK only — no MCP credits)

## Routing fix (2026-09-06 16:xx)
- Initial attempt: `mcp__exa__deep_search_exa` and `mcp__parallel_ai__web_search` failed
  with `search_queries[0] (type)` validation error — the MCP tool-call layer is
  double-wrapping the string array.
- Root cause: MCP wrappers around deep_search_exa/parallel expect a different
  arg shape (objective + flat search_queries[]) than what the runtime serializes.
- Fix: bypass the broken MCP layer; use the native `web_search` tool which
  dispatches through `plugins/web/parallel/provider.py` and
  `plugins/web/exa/provider.py` (already configured in config.yaml lines 747-755,
  851-855). Same provider backends, working shape, zero credits wasted on MCP.

## Status
- [x] run #1: discovery sweep (web_search × ~40 queries) — DONE
- [x] run #2: signal verification (web_extract × 18 URLs) — DONE
- [x] run #3: contact resolution — DONE (only verified contacts; blanks left blank)
- [x] finalize: CSV → wiki — DONE (2026-09-06-missouri-family-offices.csv, 9 rows)
- [x] google sheet mirror — DONE (created sheet 1Gc5KzfDM5o-OwqvNbPWunz5rDA8R8gh12CYsr52d-Q0; A1:J11 written + read-back verified 2026-09-06)
- [x] deck peer review — DONE (2026-09-06-deck-peer-review.md)
- [x] re-anchored deck rewrite (Evermont v2.0) — DONE (2026-09-06-deck-v2-evermont.md; anchored to verifiable Evermont, "tax-free" qualified with federal+§1250 recapture, US-281 corrected to US-50/MO-291/I-470)

## KEY FINDING (2026-09-06)
**25 verified MO-domiciled family offices with direct real estate signals DO NOT
exist in public sources.** Discovery returned 9 qualified rows (strong/medium/border),
not 25. Consistent with prior note (Axial MO family offices, none RE-focused) and
FINTRX's 5 industrial FO list (all out-of-state: Dallas, London, San Diego, Spain,
Chicago). Missouri's RE-holding wealth is concentrated in a handful of dynasty
developer-operators (Hunt, Kemper, Hermann/Busch, Hall/Hallmark) rather than a broad
field of allocator family offices.

## Credit tracking
| call | provider | query | cost | running total |
|------|----------|-------|------|---------------|
