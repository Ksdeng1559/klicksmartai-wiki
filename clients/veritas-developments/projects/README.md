---
type: Reference
title: "Folder contract — projects"
description: OKF v0.2 frontmatter; type/status visible to any LLM that reads the bundle.
status: stable
generated: { by: human:dennis, at: 2026-08-29T18:00:00Z }
verified: []
okf_version: "0.2"
---
# projects/ — Validated Source of Truth

**Purpose:** Promoted, HITL-approved deliverables. These are the source-of-truth artifacts for Veritas work — once a draft passes review, its final source `.md` lands here.

**Rule:** Nothing lands here directly. All content originates in `drafts/` and is promoted here **only** after Dennis (and David/Daniel for relationship facts) approves. See `../CONTEXT.md` Stage 04→05.

## Files (flat)
- `prime-lees-summit.md` — Prime Lee's Summit development card
- `stonehaven-estates.md` — Stonehaven Estates development card
- `co-sponsor-gp-target-list.md` — validated co-sponsor GP target list
- `growth-program-pilot-plan.md` — growth program pilot plan
- `prime-lees-summit-co-sponsor-brief.md` — co-sponsor brief for Prime Lee's Summit

## Promote a draft
1. Copy the approved `.md` from `drafts/` into `projects/`.
2. Remove its row from `drafts/VALIDATION_QUEUE.md`.
3. Produce the client-ready export in `deliverables/`.

## Graduate to subdirectories
When a project accumulates multiple files (cards, briefs, memos, reports), move it into `projects/<slug>/` with its own `README.md`. Do this at a natural review point, not mid-pipeline.
