# drafts/deck/ — Veritas AI Work in Progress for deck

**Purpose:** AI-generated deck drafts for Veritas Development Group LLC. Pre-HITL, NOT source-of-truth.

**Gate:** Promotion to `projects/deck/` or `deliverables/deck/` requires Dennis + David (or Daniel for relationship facts) approval via the parent `drafts/VALIDATION_QUEUE.md`.

## Vertical config

- **Type:** deck
- **Default Hermes skill:** see `../../_config/deliverables.md`
- **Source format:** `.md` is canonical. Generated `.html`/`.mp4`/`.png` lives here until HITL.

## Procedure

1. Create `<artifact>-<YYYY-MM-DD>.md` here — the markdown source / spec.
2. Run the configured Hermes skill to produce the asset.
3. Add a row to `../VALIDATION_QUEUE.md` (parent `drafts/`) — artifact, type=deck, approvers, status.
4. Build any preview into `../../drafts-preview/deck/` (optional).
5. On HITL approval: `.md` → `../../projects/deck/`, asset → `../../deliverables/deck/`.
