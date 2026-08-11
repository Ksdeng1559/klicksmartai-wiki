---
title: spectra-pipeline (skill)
created: 2026-08-11
updated: 2026-08-11
type: entity
tags: [entity, skill, spectra, mcf, county, pipeline, project]
sources: []
confidence: high
---

# spectra-pipeline (skill)

**Active client: Spectra Holdings Group.** $300M Master Credit Facility
county pipeline. The umbrella skill for county-level research →
deliverable production for Spectra's MCF investment thesis.

## Source
`~/.hermes/skills/project/spectra-pipeline/`

## Trigger
`/spectra-pipeline` slash command OR any request mentioning "Spectra
county research", "MCF county brief", "investor lead discovery for <county>",
or naming a county + state with Spectra context.

## The 5-step sequence (strict order)
1. **Phase 0 — Source Inventory** (mandatory before any new research).
   Check existing wiki files first; only net-new research when absent.
2. **`/spectra-census-research <county>, <ST>`** — quantitative demographics.
3. **`/spectra-social-intelligence <county>, <ST> --depth [light|standard|deep]`** —
   qualitative landscape.
4. **Investor Lead Discovery** — CDFIs, faith-based funds, LIHTC syndicators,
   CRA banks, grant makers, private impact funds. Min 15 orgs across 6
   categories.
5. **Deliverable** — pick one based on audience:
   - `/spectra-investor-brief` — investors / CDFIs / foundations
   - `/spectra-advertorial` — faith community / churches
   - `/spectra-internal-brief` — Dennis / KlickSmartAI internal
   - `/spectra-county-official-briefing` — county officials
   - `/spectra-county-intelligence` — 12-section McKinsey-style executive briefing

## Output routing
All output → `clients/spectra-holdings/outputs/` (or `deliverables/` for
approved). Drafts held in `REVIEW_DRAFT/` until Dennis approves.

**HITL rule (non-negotiable):** no draft reaches Gmail/Slack/Telegram/LinkedIn
without Dennis's explicit approval. "Looks good" is not approval.

## Counties completed (as of 2026-08-10)
- **Whatcom WA** (2026-05-13) — Kulshan CLT pilot, gap-bridging thesis.
- **Bexar TX** (2026-05-14) — structural deficit + eviction concentration,
  Conditional Go.
- **Craig OK** (2026-05-20) — arrest-decline + tribal pathway (no county gap).
- **Jackson MO / Kansas City** (2026-08-10) — vacancy conversion, refiled to
  Veritas Developments (David Poole) per Dennis reassignment.

## Search engine stack (active)
Brave → Serper.dev → Exa.ai. Rotate on every call. Never retry exhausted.

**Deprecated:** Tavily MCP, Parallel.ai, SerpAPI, Firecrawl web_extract —
credits exhaust; no longer in active rotation.

## Faith frame
All Spectra output is faith-framed: CDFIs, Christian foundations, Kulshan CLT.
Persona file at `wiki/personas/spectra-researcher.md` (must exist before
sub-agent calls).

## Post-write protocol
```bash
cd ~/wiki && graphify update .
git add -A && git commit -m "[type]: <county> county, <ST>"
git pull --rebase && git push origin master
```

## See also
- [[Skill-B2b-Outreach]] — general outreach intelligence
- [[Client-Attribution-Refile]] — what to do when Dennis reassigns a package
- [[Gtm-Enrichment-Hitl-Gate]]