# Drafts — Source-of-Truth Gate

All AI-generated work lands in `drafts/` first. **Nothing promotes to `projects/` or `deliverables/` without HITL approval.**

## Rule

Per KlickSmartAI wiki governance (`~/wiki/shared/templates/client-workspace-icm/IDENTITY.md`):

1. **Source-of-truth gate.** AI-generated content ALWAYS lands in `drafts/` first. Never write directly to `projects/` or `deliverables/`.
2. **HITL gate.** Before a file is promoted from `drafts/` to `projects/` (or to `deliverables/`), a human — typically Dennis — must review and explicitly approve.
3. **Routing first.** At session start, read `CONTEXT.md` to identify which folder to enter.
4. **Voice follows `_config/voice.md`.** Do not invent tone. If voice.md is empty, ask before writing.
5. **Regulated content (financial, legal, health).** Add a compliance reference to `_config/compliance.md` and consult it before writing.

## Triggers

| Trigger | Action |
|---|---|
| Need more source material from sponsor | Draft an outreach email, save to `drafts/`, wait for Dennis |
| New multi-stage pipeline proposed | Propose design in `drafts/` first; promote to `projects/<pipeline>/` only after Dennis approves the design |
| Deliverable conflicts with voice.md | Pause; flag the conflict; ask Dennis which to honor |
| Regulated content (financial, legal) | Add compliance reference + consult `_config/compliance.md` |

## Validation queue

See `VALIDATION_QUEUE.md` in this folder for the per-file gate log.
