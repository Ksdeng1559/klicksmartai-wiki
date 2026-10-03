---
type: Reference
title: "Business Funding Canada — Conventions"
status: active
generated: 2026-10-02
verified: 2026-10-02
---

# Conventions

## File naming
- `drafts/<name>/<artifact>-<YYYY-MM-DD>.md` — date is local-creation date.
- `projects/<artifact>.md` — promoted from `drafts/` after HITL approval.
- `deliverables/<artifact>.{md,html,pdf}` — final exports.
- Slugs are kebab-case, lowercase, no spaces.

## Folder rules
- **Source-of-truth gate:** AI output → `drafts/`. Never `projects/` or `deliverables/` on first pass.
- **HITL gate:** No promotion without Dennis's explicit "yes" / "approve" / "send it" on the row in `drafts/VALIDATION_QUEUE.md`.
- **Vertical subfolders:** When verticals are declared, each gets `drafts/<vertical>/`, `drafts-preview/<vertical>/`, `projects/<vertical>/`, `deliverables/<vertical>/`.

## Research subfolder convention
- `research/competitors/<name>/<YYYY-MM-DD>/` for competitor scrapes.
- `research/lenders/<name>/<YYYY-MM-DD>/` for lender-anchor profiles.
- `research/industries/<vertical>/<YYYY-MM-DD>/` for industry deep-dives.

## Citation convention
- Inline `[source](url)` Markdown links for every external claim.
- Inline citations for lender name, rate range, regulator reference.
- Cite the source `.md` file path for claims derived from a scraped artifact.

## Frontmatter
Every generated `.md` carries a YAML frontmatter block with at minimum `type:` (see OKF §11). Recommended fields: `title`, `description`, `tags`, `status`, `generated`, `verified`, `sources`, `stale_after`.

## Reserved filenames (per OKF §8/§9)
- `index.md` — directory listing / bundle manifest
- `log.md` — update history

## Inheritance
- Voice: `_config/voice.md` (every vertical inherits unless overridden).
- Compliance: `_config/compliance.md` (every vertical inherits).
- Conventions: this file (always inherited).