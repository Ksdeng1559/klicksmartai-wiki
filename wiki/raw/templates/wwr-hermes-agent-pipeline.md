---
title: WWR Hermes Agent Pipeline Architecture
created: 2026-04-15
type: raw
source: provided by Dennis E. / KlickSmart AI — Wealth Wire Radar
---

# WWR Hermes Agent Pipeline — as architected by Dennis E.

```
HERMES AGENT (runs daily at 6AM)
            │
            ▼
    ┌─────────────────┐
    │  wwr_search     │  Searches online — Serper, Tavily, Brave
    │                 │  "BC construction company sold 2026"
    │                 │  "Alberta manufacturing acquisition"
    └────────┬────────┘
             │ raw search results
             ▼
    ┌─────────────────┐
    │ signal_parser   │  Extracts structured data from results
    │                 │  entity name, province, signal type,
    │                 │  signal date, company, career years
    └────────┬────────┘
             │ parsed signal
             ▼
    ┌─────────────────┐
    │ wwr_classify    │  Scores the signal 0-100
    │                 │  HOT / WARM / DEVELOPING
    │                 │  ICP sector tag + multiplier
    └────────┬────────┘
             │ scored signal
             ▼
    ┌─────────────────┐
    │ wwr_map_pv      │  Builds the financial profile
    │                 │  18 PV fields — net worth band,
    │                 │  retained earnings, insurance needs,
    │                 │  ICP gate QUALIFIED/PROBABLE
    └────────┬────────┘
             │ PV profile
             ▼
    ┌─────────────────┐
    │ wwr_resolve_identity │  Finds LinkedIn URL + email
    │                     │  Checks competitor gate
    │                     │  90-day deduplication
    └────────┬────────┘
             │ identity data
             ▼
    ┌─────────────────┐
    │ wwr_generate_brief │  ← BATTLE CARD GENERATOR
    │                   │  Combines everything into a
    │                   │  structured planning brief:
    │                   │  • Who they are
    │                   │  • Why they matter right now
    │                   │  • Estimated financial profile
    │                   │  • Planning angles
    │                   │  • Recommended outreach angle
    │                   │  • Draft cold email + video script
    │                   │  • COI activation recommendation
    └────────┬────────┘
             │ complete battle card
             ▼
    ┌─────────────────┐
    │ wwr_store_signal │  Writes everything to MotherDuck
    │                 │  signals table
    │                 │  entities table
    │                 │  pv_profiles table
    │                 │  outreach_queue table
    └────────┬────────┘
             │
             ▼
    MotherDuck Database
             │
             ▼
    FastAPI Backend (Railway)
             │
             ▼
    CRM Frontend (Sean's browser)
             │
             ▼
    Sean sees the battle card
    with one-click outreach approval
```

## Tool Status (from PRD)

| Tool | Status | Notes |
|------|--------|-------|
| wwr_search | 📋 Architecture written | tri_engine_search.py blocking |
| signal_parser | 🔴 Blocking next | Must be built first |
| wwr_classify | ✅ Built + validated | Part of signal_classifier.py |
| wwr_map_pv | 📋 Fully specified | preliminary_viewpoint_mapper.py |
| wwr_resolve_identity | ⏳ Phase 2 | Exa.ai neural search, competitor gate |
| wwr_generate_brief | 📋 Architecture defined | Battle card generator |
| wwr_store_signal | 📋 Architecture written | MotherDuck writes |
