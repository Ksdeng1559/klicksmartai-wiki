# Conventions — <client_name>

## File naming
- **Drafts (AI-generated, pre-HITL):** `drafts/<deliverable-name>-<YYYY-MM-DD>.md`
- **Multi-part deliverables:** use a numbered prefix to preserve order:
  `drafts/<name>/01_intake.md`, `02_research.md`, `03_draft.md`
- **Projects:** `projects/<project-slug>.md` (flat) or `projects/<project-slug>/` (graduated)
- **Deliverables:** `deliverables/<deliverable-name>-<YYYY-MM-DD>.md` (and `.html` / `.pdf` when a client-ready export is produced).
- **HTML previews:** `drafts-preview/<deliverable-name>-<YYYY-MM-DD>.html` + shared `styles.css` and `build.py`.

## Folder rules
- AI-generated client content ALWAYS lands in `drafts/` first.
- Nothing moves to `projects/` or `deliverables/` until Dennis approves — see `CONTEXT.md` Stage 04→05 gate.
- Keep `drafts/` and `deliverables/` clean: one primary `.md` per deliverable, plus supporting `.csv`/`.html` alongside the same base name.
- Do not put cross-client work in this workspace — that goes in the other client's workspace.

## Version convention
- A draft re-run on a new date gets a NEW filename with that date. Do not overwrite a prior dated draft — preserve history.
- The current in-progress draft is the one with the latest date.

## Promotion convention
- On HITL approval: copy the approved `.md` from `drafts/` into `projects/` (source of truth) AND produce the client-ready export in `deliverables/`.
- Remove the corresponding row from `drafts/VALIDATION_QUEUE.md`.
- Keep a link/reference to the source draft rather than deleting it.
