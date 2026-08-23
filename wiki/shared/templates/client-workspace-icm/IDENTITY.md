# {{CLIENT_NAME}} — Workspace Identity

> {{CLIENT_ONE_LINE}}

This is a **client workspace** inside the KlickSmartAI wiki. It follows the
ICM 3-layer template at `shared/templates/client-workspace-icm/` and obeys
the wiki source-of-truth rule (drafts → HITL → projects).

---

## Folder Map

```
clients/{{CLIENT_SLUG}}/
├── IDENTITY.md            # you are here — Layer 0
├── CONTEXT.md             # Layer 1 — task routing table
├── README.md              # human-facing overview
├── _config/               # Layer 3 — voice, conventions, glossary
│   ├── voice.md           # tone, audience, do/don't
│   ├── conventions.md     # file naming, folder rules
│   └── glossary.md        # domain terms
├── projects/              # Layer 4 — validated deliverables (source of truth)
├── drafts/                # Layer 4 — AI work in progress (pre-HITL)
├── deliverables/          # Layer 4 — client-ready exports (HTML / PDF / DOCX)
├── drafts-preview/        # Layer 4 — HTML previews of drafts/
└── skills/                # client-specific skills (optional)
```

---

## Stage Map (Quick-mode — virtual stages defined in CONTEXT.md)

The default pipeline for any client deliverable is:

```
01_intake     →  02_research  →  03_draft  →  04_review  →  05_publish
   |                |              |             |             |
drafts/         drafts/         drafts/       drafts/       projects/  +  deliverables/
                                                                    (HITL gate at 04→05)
```

For client-specific multi-stage pipelines (e.g. Spectra county intelligence),
graduate to **Full-mode ICM** with physical `projects/<pipeline>/stages/NN_*/CONTEXT.md`
contracts. See the template README for guidance.

---

## Raw Source Locations

External folders that feed into this workspace. Leave empty if the client
only consumes what Hermes produces internally.

| Source | Path | Contents |
|--------|------|----------|
| _none yet_ | _add when present_ | _e.g. Notion workspace, shared Drive folder_ |

---

## Rules

1. **Source-of-truth gate.** AI-generated content ALWAYS lands in `drafts/` first. Never write directly to `projects/` or `deliverables/`. The `wiki-source-of-truth-governance` skill enforces this.
2. **HITL gate.** Before a file is promoted from `drafts/` to `projects/` (or to `deliverables/`), a human — typically Dennis — must review and explicitly approve.
3. **Routing first.** At session start, read `CONTEXT.md` to identify which folder to enter; read the relevant sub-workspace's `IDENTITY.md` only when entering that sub-workspace.
4. **Voice follows `_config/voice.md`.** Do not invent tone. If voice.md is empty, ask before writing.
5. **Citations required.** Every claim from an external source carries the URL inline.
6. **No autonomous sends.** No client communication (email, Slack, LinkedIn, etc.) goes out without an explicit "send it" from Dennis. Drafts only.
7. **Escalate uncertainty.** When a stage cannot complete (missing input, ambiguous spec, conflicting source), stop and ask. Do not invent.

---

## Escalation

| Situation | Action |
|-----------|--------|
| Need more source material from client | Draft an outreach email, save to `drafts/`, wait for Dennis |
| New multi-stage pipeline proposed | Propose it in `drafts/` first; promote to `projects/<pipeline>/` only after Dennis approves the design |
| Deliverable conflicts with voice.md | Pause; flag the conflict; ask Dennis which to honor |
| Regulated content (financial, legal, health) | Add a compliance reference to `_config/compliance.md` and consult it before writing |
| Client asks for something outside ICM boundaries | Pause; route to Dennis for triage |

---

## Memory hygiene

Durable facts about this client go in:
- `_config/` for voice, conventions, glossary (workspace-level)
- MEMORY.md (user profile / cross-workspace) for client-wide preferences only
- Never duplicate the same fact across `_config/` and MEMORY.md — pick one source of truth.
