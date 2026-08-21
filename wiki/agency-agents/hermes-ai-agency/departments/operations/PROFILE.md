---
department_id: operations
status: active
headcount: 1 AI
headcount_planned: 1-2 AI
employees:
  - chief-of-staff
---

# Operations — PROFILE

The Operations department owns the agency itself: vault hygiene, employee lifecycle, decision log, kanban, dashboard, and continuity between sessions.

## Mission

Make the agency legible to any future AI agent that resumes work, and to the human CEO who checks in periodically.

## Current state

- **Chief of Staff** acts as department head (acting).
- One employee: `chief-of-staff`.
- Open: a `data-engineer` if/when pipeline analytics become a bottleneck.

## What the Operations department produces

1. **`DASHBOARD.md`** — live status (updated after every meaningful action)
2. **`KANBAN.md`** — active work + backlog + done
3. **`DECISIONS.md`** — dated CEO decision log (the canonical record)
4. **`NOTES.md`** — chief-of-staff working memory
5. **`REGISTRY.md`** — departments + employees index
6. **`AGENTS.md`** — operating rules

## What the Operations department does NOT do

- Finding prospects (Lead Generation)
- Outreach / sales (Sales)
- Delivery work (Delivery)
- Marketing copy (Content)

## Key files

- Top-level governance: `~/Hermes-AI-Agency/*.md`
- Employee SOUL.md files: `~/Hermes-AI-Agency/employees/*/SOUL.md`
- Department profiles: `~/Hermes-AI-Agency/departments/*/PROFILE.md`

## Hiring plan

- Add a `data-engineer` if/when pipeline analytics become a bottleneck. Not yet needed — current pipeline volume fits in `run-summary.json` files.
- Consider a `continuity-manager` (human?) to ensure context isn't lost between major sessions.