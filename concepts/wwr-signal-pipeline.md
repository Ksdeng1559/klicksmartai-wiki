---
title: WWR Signal Pipeline
created: 2026-04-15
updated: 2026-04-16
type: concept
tags: [wwr, signal-processing, hermes-agent, pipeline, lead-enrichment, wealth-tech]
sources: [raw/transcripts/wwr-implementation-plan-rev3.md, raw/templates/wwr-hermes-agent-pipeline.md]
related: [entities/wealth-wire-radar, concepts/wwr-relationship-manager, concepts/wwr-proximity-scorer, concepts/wwr-battlecard-format]
---

# WWR Signal Pipeline

## Pipeline Flow (9 Steps)

```
HERMES AGENT (daily 6AM PT via cron)
 │
 ├── wwr_search ────────────→ tri_engine_search.py ✅ (Serper + Tavily + Brave fan-out)
 │                          Returns: list of raw signal dicts
 │
 ├── signal_parser ─────────→ signal_parser.py ✅
 │                          Extracts: entity_name, province, signal_type,
 │                             signal_date, company, career_years, registry_confirmed
 │
 ├── wwr_classify ──────────→ signal_classifier.py ✅ (composite score, tier, clusters)
 │
 ├── wwr_map_pv ─────────────→ preliminary_viewpoint_mapper.py ✅ (18-field PV profile, ICP gate)
 │
 ├── wwr_resolve_identity ───→ Phase 2 (Exa.ai)
 │
 ├── wwr_match_coi ─────────→ Master COI Module ✅ (mock) / coi_mapper.py ✅ (mock)
 │
 ├── wwr_generate_brief ─────→ battlecard_generator.py 📋 (Stage 11)
 │
 └── wwr_store_signal ───────→ MotherDuck ✅ (migrations 001–010 deployed)
         │
         ↓
    MotherDuck (wwr_production)
         │
         ↓
    FastAPI Backend (Railway) — Stage 8 🔜
```

## Signal Clusters

Eight signal clusters detected:

| Cluster | Signal Type | Age Modifier |
|---------|-------------|-------------|
| Director change | BC/AB Registry | ×1.20 (0–7 days) |
| Biz sale | News + Registry | ×1.10 (8–30 days) |
| Property transfer | Land Titles | ×1.00 (31–90 days) |
| CCPC succession | CRA triggers | ×0.85 (91–180 days) |

**Age Modifier Scale:**
- 0–7 days: ×1.20
- 8–30 days: ×1.10
- 31–90 days: ×1.00
- 91–180 days: ×0.85
- 181–365 days: ×0.70

## V2 Cluster Scoring

From signal classifier — dominant lever is recency. The ICP gate runs after scoring:
- QUALIFIED (≥70% NW confidence + ≥70% income confidence) → 24hr outreach
- PROBABLE (40–69%) → 72hr
- DEVELOPING → not briefed

## Built Modules

| Module | File | Status |
|--------|------|--------|
| Multi-engine search | `tri_engine_search.py` | ✅ Built |
| Signal parser | `signal_parser.py` | ✅ Built |
| Signal classifier | `signal_classifier.py` | ✅ Built |
| Preliminary viewpoint mapper | `preliminary_viewpoint_mapper.py` | ✅ Built |
| Hermes tools | `wwr_tools.py` (7 tools) | ✅ Built |
| MotherDuck schema | migrations 001–010 | ✅ Built |
| Master COI module | mock data (15 profiles) | ✅ Built |
| Relationship manager | `relationship_manager.py` | 📋 v2.0 spec |
| Pathfinder agent | `pathfinder_agent.py` | 📋 v2.0 spec |
| Proximity scorer | `proximity_scorer.py` | 📋 v2.0 spec |
| Battlecard generator | `battlecard_generator.py` | 📋 Stage 11 |

## Hermes Skills (as wired)

```
~/.hermes/skills/
├── wwr-signal-pipeline.md       ✅
├── wwr-search.md                ✅
├── wwr-signal-parser.md         ✅
├── wwr-classify.md              ✅
├── wwr-preliminary-viewpoint.md ✅
├── wwr-resolve-identity.md      ✅
├── wwr-generate-brief.md        ✅
├── wwr-store-signal.md          ✅
├── wwr-coi-master.md            ✅
├── wwr-relationship-manager.md  📋 v2.0 NEW
├── wwr-pathfinder.md            📋 v2.0 NEW
├── wwr-proximity-scorer.md      📋 v2.0 NEW
└── wwr-relationship-wiki.md     📋 wiki integration
```

## Two COI Layers

| Layer | Who | Table | Status |
|-------|-----|-------|--------|
| Master COI Network | Sean Carey (Westward Advisors) | `coi_profiles`, `coi_activations`, `coi_briefs` | ✅ Built (mock) |
| Subscriber COI Network | Each advisor's Unipile graph | `coi_network`, `coi_mappings` | ✅ Built (mock) |

**Anonymity Principle:** Prospects are never named in COI communications. Sean's brief receives pattern intelligence only.
