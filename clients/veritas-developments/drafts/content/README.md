---
type: Reference
title: "Folder contract — content"
description: OKF v0.2 frontmatter; type/status visible to any LLM that reads the bundle.
status: stable
generated: { by: human:dennis, at: 2026-08-29T18:00:00Z }
verified: []
okf_version: "0.2"
---
# drafts/content/ — Veritas AI Work in Progress for content

**Purpose:** AI-generated content drafts for Veritas Development Group LLC. Pre-HITL, NOT source-of-truth.

**Gate:** Promotion to `projects/content/` or `deliverables/content/` requires Dennis + David (or Daniel for relationship facts) approval via the parent `drafts/VALIDATION_QUEUE.md`.

## Vertical config

- **Type:** content
- **Default Hermes skill:** see `../../_config/deliverables.md`
- **Source format:** `.md` is canonical. Generated `.html`/`.mp4`/`.png` lives here until HITL.

## Procedure

1. Create `<artifact>-<YYYY-MM-DD>.md` here — the markdown source / spec.
2. Run the configured Hermes skill to produce the asset.
3. Add a row to `../VALIDATION_QUEUE.md` (parent `drafts/`) — artifact, type=content, approvers, status.
4. Build any preview into `../../drafts-preview/content/` (optional).
5. On HITL approval: `.md` → `../../projects/content/`, asset → `../../deliverables/content/`.
