# raw/wiki-knowledge/ consolidation — 2026-09-27

## What was here
`raw/wiki-knowledge/` was a legacy mirror of the top-level wiki tree, used to keep
a frozen snapshot during early experimentation. It contained **368 .md files**.

## What this pass did
- **356** files were bit-identical to canonical top-level files → removed via `git rm` from mirror.
- **12** files were preserved in this archive (DIFFERS or UNIQUE):
  - DIFFERS_FROM_CANONICAL: `index.md`
  - DIFFERS_FROM_CANONICAL: `log.md`
  - UNIQUE_LEGACY: `concepts/progressive-enrichment-architecture.md`
  - UNIQUE_LEGACY: `concepts/search-stack.md`
  - UNIQUE_LEGACY: `entities/swan-gtm-gtm-skills.md`
  - UNIQUE_LEGACY: `entities/leadsniper-sgi-prd.md`
  - UNIQUE_LEGACY: `templates-root/entity-template.md`
  - UNIQUE_LEGACY: `templates-root/raw-template.md`
  - UNIQUE_LEGACY: `templates-root/concept-template.md`
  - UNIQUE_LEGACY: `templates-root/project-template.md`
  - UNIQUE_LEGACY: `templates-root/pipeda-consent-screen.md`
  - UNIQUE_LEGACY: `templates-root/meeting-notes-template.md`

## Why preserve rather than delete
Per the `wiki-graphify-sync` skill convention: superseded artifacts stay on disk
under `STATUS.md` rather than being auto-deleted. Future agents reading the repo
will see this directory and know it is a curated archive, not active content.

## Impact
- Net reduction in tracked files: {len(to_remove)}
- Mirror directory retained as empty skeleton (`raw/wiki-knowledge/.gitkeep`)
- Graphify re-index after this pass will reflect canonical-only content.


## Addendum (post-pass check)
A follow-up cross-check found that 6 of the "UNIQUE_LEGACY" files (`templates-root/*.md`) were bit-identical to `templates/*.md` — the path differed (`templates-root/` vs `templates/`) but the content was the same. Those 6 entries above the line have been removed; the archive now holds only the 6 genuinely unique or differing files.
