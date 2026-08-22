---
title: "Projects — Source-of-Truth Deliverables"
type: directory-readme
status: ACTIVE — boundary rules in effect
created: 2026-08-22
---

# Projects Directory — Veritas Lee's Summit

## What goes here

**Source-of-truth deliverables** — files that have been:
1. Confirmed by David Poole (client primary contact) **OR** confirmed by an external authoritative source
2. Validated by Daniel Bailey for relationship-based assumptions (where applicable)
3. Promoted from `drafts/` via the HITL gate documented in `drafts/VALIDATION_QUEUE.md`

## What does NOT go here

- Working hypotheses built from public web research
- AI-inferred strategy based on assumptions about client relationships
- Unverified TAM data, channel research, or outreach playbooks
- Anything pending David + Daniel feedback

Those files live in `drafts/` until promoted.

## Current contents (5 files, all confirmed or input specs)

| File | Status | Last validation |
|---|---|---|
| `co-sponsor-gp-target-list.md` | David-provided input spec (pre-2026-08-22) | Validated on file |
| `prime-lees-summit-co-sponsor-brief.md` | Project brief (pre-2026-08-22) | Validated on file |
| `prime-lees-summit.md` | Project description (pre-2026-08-22) | Validated on file |
| `stonehaven-estates.md` | Project description (pre-2026-08-22) | Validated on file |
| `growth-program-pilot-plan.md` | Growth plan (pre-2026-08-22) | Validated on file |

## Recently moved to drafts/ (5 files, awaiting HITL validation)

See `drafts/VALIDATION_QUEUE.md` for the full validation questions per file.

| Moved to drafts/ on | Status |
|---|---|
| `tam-co-sponsor-capital-2026-08-22.csv` | ⏳ Awaiting David |
| `tam-co-sponsor-capital-2026-08-22.md` | ⏳ Awaiting David |
| `kc-family-office-law-firm-channel-2026-08-22.md` | ⏳ Awaiting David |
| `team-profile-daniel-bailey-2026-08-22.md` | ⏳ Awaiting Daniel |
| `7-touch-outreach-playbook-2026-08-22.md` | ⏳ Awaiting David + Daniel |

## Promotion rules

1. Only files in `drafts/` can be promoted to `projects/`
2. Promotion requires explicit HITL approval from David (for client-facing content) or Daniel (for relationship-validation)
3. Promoted files must add `status: APPROVED — promoted from draft` to frontmatter
4. Promoted files must specify `validated_by` (David, Daniel, or external source) + `validation_date`
6. After promotion, files get committed + pushed to klicksmartai-wiki master
7. After promotion, files may also be pushed to veritasdevelopment-wiki main (if client-visible)

## De-promotion rules

If a promoted file is later found to be incorrect or invalid:
1. Move it back to `drafts/` immediately
2. Update frontmatter: `status: DE_PROMOTED — requires re-validation`
3. Commit + push the demotion

---

*This boundary is enforced by the KlickSmartAI Hermes Agent governance rules. Any file added to `projects/` without going through the drafts/ + HITL validation gate is a violation.*