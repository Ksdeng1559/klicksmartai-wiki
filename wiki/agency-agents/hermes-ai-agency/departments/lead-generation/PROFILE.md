---
department_id: lead-generation
status: active
headcount: 1 AI
headcount_planned: 1-2 AI
employees:
  - lead-researcher
---

# Lead Generation — PROFILE

The Lead Generation department owns the top of the funnel: finding businesses that need the agency's services.

## Mission

Produce a steady stream of qualified, scored, audit-backed prospects that the Sales department can convert.

## Current state

- **Volume:** 8 qualified prospects per run (limited by DataForSEO endpoint quirk documented in OKF)
- **Quality:** All C/D tier per current rubric (rubric may need reframe)
- **Cost:** ~$2-6 per run
- **Runtime:** ~5-10 minutes per run

## What the Lead Generation department produces

1. **Ranked prospect CSVs** — `okf/leadsniperai/outputs/<run>/ranked-prospects.csv`
2. **Per-business audit JSON** — `site-audits/<place_id>.json`
3. **Reflections** — `okf/reflections/run-<date>-*.md`
4. **Pipeline improvements** — discovered endpoint quirks, scoring calibrations, etc.

## What the Lead Generation department does NOT do

- Outreach / cold email (Sales department)
- Pricing or proposal generation (Sales + Delivery)
- Building websites (Delivery)
- Marketing content (Content)

## Key files

- Primary procedure: `G:\AI - Coding Projects\RIOS-CRM\RIOS\okf\leadsniperai\playbooks\phase-1-mvp-pipeline.md`
- Scoring rubric: `G:\AI - Coding Projects\RIOS-CRM\RIOS\okf\leadsniperai\concepts\opportunity-scoring-rubric.md`
- Decisions: `G:\AI - Coding Projects\RIOS-CRM\RIOS\okf\leadsniperai\decisions.md`

## Hiring plan

- Add a second `lead-researcher` once the agency has 3+ active client engagements, to expand geographic coverage.
- Consider a `data-engineer` to maintain the scoring rubric and run analytics on pipeline health.