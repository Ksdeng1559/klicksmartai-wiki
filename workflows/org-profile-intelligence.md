# Org Profile Intelligence Workflow

**Status:** Proposed — NCF/Spectra is the pilot execution  
**Type:** Reusable — runs against any target organization  
**Owner:** Dennis Eng / Hermes Agent

---

## Purpose

Produce a structured, source-grounded intelligence profile of any target organization to inform strategic outreach, partnership proposals, or capital solicitation. Output is a living wiki entity queryable by Hermes before drafting any communication to that org.

---

## When to Run

- New outreach target identified (donor, funder, partner, client)
- Strategic relationship being built (not cold prospecting)
- Capital solicitation (grant, DAF, investment, partnership)
- Any org where mission/values alignment determines the outcome

---

## Architecture

```
Input
─────
Organization URL

↓

Layer 1 — Acquisition
─────────────────────
Tool: Scrapling (scrape.py)

Pages extracted:
  homepage · mission · about · leadership
  services · news · reports · stories · public documents

Output: outputs/research/{org-slug}/raw/*.md

↓

Layer 2 — Normalization
───────────────────────
Tool: Python (normalize.py)

Operations:
  - Remove navigation chrome, headers, footers
  - Deduplicate repeated text across pages
  - Classify pages by type (mission, leadership, program, news, etc.)
  - Chunk content for AI context windows
  - Identify named entities (people, programs, locations, orgs)

Output: outputs/research/{org-slug}/normalized/*.json

↓

Layer 3 — Intelligence
──────────────────────
Tool: Claude / Ollama Cloud (analyze.py + report.py)

Generates 7 intelligence modules:

  1. Organization Profile
     Mission · Vision · Core values · Audience · Service areas

  2. Language Pattern Analysis
     Recurring phrases · Emotional drivers · Positioning language · Keywords

  3. Strategic Priorities
     Current initiatives · Community goals · Funding themes · Growth signals

  4. Outreach Intelligence
     Likely motivations · Pain points · Relationship angles
     Messaging to avoid · Suggested first-contact themes

  5. Alignment Analysis
     Spectra Holdings Group fit + confidence score
     WealthWireRadar fit + confidence score
     KlickSmartAI fit + confidence score

  6. Why Now Signals
     Recent announcements · Leadership changes
     New initiatives · Strategic timing opportunities

  7. Recommended Action
     Warm introduction path · Email angle
     Meeting narrative · Next actions

Output: outputs/research/{org-slug}/analysis/*.json
        outputs/research/{org-slug}/{org-slug}-profile.md
        outputs/research/{org-slug}/{org-slug}-profile.json

↓

Layer 4 — Deep Analysis (NotebookLM)
─────────────────────────────────────
Tool: NotebookLM MCP

Sources loaded:
  - Normalized pages (url or text)
  - PDFs: annual reports, grant docs, advisor materials
  - Profile output from Layer 3
  - Alignment tree (defined per run — see below)

Query set (adapt per org):
  - What does this org fund / prioritize?
  - Where does our offering align with their mission?
  - What vehicles exist for the relationship to flow through?
  - What language and framing do they respond to?
  - What signals indicate openness or readiness?
  - How do we enter — who is the right first contact?

Output: sourced answers → update profile modules 4–7

↓

Layer 5 — Wiki + Knowledge Graph
──────────────────────────────────
Tool: Write + graphify

Output:
  wiki/entities/{org-slug}.md     ← living entity, all 7 modules
  wiki/index.md                   ← updated
  wiki/entities/graphify-out/
    graph.html                    ← interactive knowledge graph
    graph.json                    ← GraphRAG-ready
    GRAPH_REPORT.md               ← audit trail
```

---

## Alignment Tree (Per-Run Input)

Define before Layer 4. Drives query set and modules 5–7.

```
{Org Name}
│
├── Mission
├── Audience
├── Funding / Giving Vehicles
├── Community Priorities
├── Signals (recent initiatives, leadership themes, strategic language)
│
└── Our Entity Alignment
       ├── Spectra Holdings Group
       │      └── {what maps to their priority}
       ├── WealthWireRadar
       │      └── {what maps to their priority}
       └── KlickSmartAI
              └── {what maps to their priority}
```

---

## Intelligence Module Schema

Each module outputs structured JSON:

```json
{
  "org_profile": {
    "mission": "",
    "vision": "",
    "core_values": [],
    "primary_audience": {},
    "service_areas": []
  },
  "language_patterns": {
    "recurring_phrases": [],
    "emotional_drivers": [],
    "positioning_language": [],
    "keywords": []
  },
  "strategic_priorities": {
    "current_initiatives": [],
    "community_goals": [],
    "funding_themes": [],
    "growth_signals": []
  },
  "outreach_intelligence": {
    "likely_motivations": [],
    "pain_points": [],
    "relationship_angles": [],
    "messaging_to_avoid": [],
    "first_contact_themes": []
  },
  "alignment_analysis": {
    "spectra": { "fit_score": 0.0, "rationale": "", "entry_points": [] },
    "wealthwireradar": { "fit_score": 0.0, "rationale": "", "entry_points": [] },
    "klicksmartai": { "fit_score": 0.0, "rationale": "", "entry_points": [] }
  },
  "why_now_signals": {
    "recent_announcements": [],
    "leadership_changes": [],
    "new_initiatives": [],
    "timing_opportunities": []
  },
  "recommended_action": {
    "warm_intro_path": "",
    "email_angle": "",
    "meeting_narrative": "",
    "next_actions": []
  }
}
```

---

## Tools by Layer

| Layer | Tool |
|---|---|
| 1 — Acquisition | Scrapling (`scrape.py`) |
| 2 — Normalization | Python (`normalize.py`) — **to build** |
| 3 — Intelligence | Ollama Cloud + Claude Code CLI (`analyze.py`, `report.py`) |
| 4 — Deep Analysis | NotebookLM MCP (`nlm login` if expired) |
| 5 — Wiki + Graph | Write tool + graphify skill |

---

## Pilot Execution — NCF / Spectra

| Layer | Status |
|---|---|
| 1 — Acquisition | Complete — `outputs/research/ncf-profile/raw/` |
| 2 — Normalization | Not built — raw pages fed directly to Layer 3 |
| 3 — Intelligence | Complete (modules 1–2, partial 3) — `outputs/research/ncf-profile/` |
| 4 — Deep Analysis | Proposed — NotebookLM notebook not yet created |
| 5 — Wiki + Graph | Partial — entity + graph exist; pending Layer 4 update to modules 4–7 |

Run log: [ncf-pilot-run-log.md](ncf-pilot-run-log.md)

---

## Reuse Instructions

1. Create `outputs/research/{new-org-slug}/`
2. Copy `scrape.py`, `analyze.py`, `report.py` from ncf-profile — update URLs + org name
3. Build `normalize.py` (or skip for MVP — feed raw to Layer 3)
4. Run layers 1–3
5. Define alignment tree
6. Run layer 4 (NotebookLM)
7. Run layer 5 (wiki + graphify)
