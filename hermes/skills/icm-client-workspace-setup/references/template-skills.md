# Skills Registry — <client_name>

This file lists every **client-specific skill slot** that this workspace owns. Each slot binds a vertical (e.g. websites, video ads) to the Hermes / Claude Code skill that produces it, and to the folder in `deliverables/` where outputs land.

When a deliverable-vertical is added, an entry appears in the table below.

| Vertical | Hermes/Claude skill binding | Output folder | Status |
|----------|------------------------------|---------------|--------|
| _none yet_ | — | — | scaffold |

## Conventions

- **Every vertical gets a folder convention** under `deliverables/<vertical>/` (e.g. `deliverables/websites/<site-name>/`, `deliverables/video-ads/<campaign-name>/`).
- **Every vertical's working drafts go under `drafts/<vertical>/`** (e.g. `drafts/websites/<site-name>-<date>.md` plus generated `.html`).
- **Voice is per-vertical**, stored as `drafts/<vertical>/voice.md` (e.g. ad copy is punchier than whitepapers). Inherit defaults from `_config/voice.md`.
- **Compliance check** (Reg D, PII, etc.) runs before any deliverable under any vertical if `_config/compliance.md` is present.
- **HITL gate** is identical across verticals — drafts → reviews → projects + deliverables.

## Adding a new vertical

1. Add a row to the table above.
2. Create `drafts/<vertical>/README.md` and `deliverables/<vertical>/README.md`.
3. Add a vertical entry to `CONTEXT.md` task routing table.
4. Update `_config/deliverables.md` if the folder convention differs.
