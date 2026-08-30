---
type: Reference
title: Conventions — Veritas Developments
description: File naming, folder rules, ICM conventions for Veritas.
tags: [conventions, naming, reference]
status: stable
generated: { by: human:dennis, at: 2026-08-23T00:00:00Z }
okf_version: "0.2"
---

# Conventions — Veritas Developments

## File naming
- **Drafts (AI-generated, pre-HITL):** `drafts/<deliverable-name>-<YYYY-MM-DD>.md`
  Example: `tam-co-sponsor-capital-2026-08-22.md`
- **Multi-part deliverables:** use a numbered prefix to preserve order:
  `drafts/<name>/01_intake.md`, `02_research.md`, `03_draft.md`
- **Projects:** `projects/<project-slug>/` where slug is kebab-case
  (`prime-lees-summit`, `stonehaven-estates`).
- **Deliverables:** `deliverables/<deliverable-name>-<YYYY-MM-DD>.md` (and
  `.html` / `.pdf` when a client-ready export is produced).
- **HTML previews:** `drafts-preview/<deliverable-name>-<YYYY-MM-DD>.html` +
  a shared `styles.css` and a build `build.py`.

## Folder rules
- AI-generated client content ALWAYS lands in `drafts/` first.
- Nothing moves to `projects/` or `deliverables/` until Dennis + David (+ Daniel for relationship facts) approve — see `CONTEXT.md` Stage 04→05 gate.
- Keep `drafts/` and `deliverables/` clean: one primary `.md` per deliverable, plus supporting `.csv`/`.html` alongside the same base name.
- Do not put marketing/SEO drafts in `drafts/` if they belong to a different client — those go in that client's workspace.
- Every multi-file reference set under `_config/` or `references/` that exceeds ~10 files gets an `_index.md` summary table.

## Version convention
- A draft re-run on a new date gets a NEW filename with that date. Do not overwrite a prior dated draft — preserve history.
- The current in-progress draft is the one with the latest date.

## Promotion convention
- On HITL approval: copy the approved `.md` from `drafts/` into `projects/<project>/` (source of truth) AND produce the client-ready export in `deliverables/`.
- Remove the corresponding row from `drafts/VALIDATION_QUEUE.md`.
- Keep a link/reference to the source draft rather than deleting it.
