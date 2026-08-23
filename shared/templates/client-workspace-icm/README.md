# Client Workspace Template (ICM 3-Layer + Source-of-Truth Gate)

Use this template to create a new client workspace under `/home/denni/wiki/clients/<client-slug>/`.

It implements **ICM Quick-mode** (3 layers) on top of the KlickSmartAI wiki source-of-truth rule:
- **AI-generated client content ALWAYS lands in `drafts/`** first.
- **Nothing moves to `projects/` or `deliverables/` until Dennis validates** (HITL).
- The `wiki-source-of-truth-governance` skill enforces this gate.

## How to instantiate

```bash
# 1. Copy template to new client location
CLIENT=acme-ventures
cp -r /home/denni/wiki/shared/templates/client-workspace-icm /home/denni/wiki/clients/$CLIENT

# 2. Replace placeholders in all 4 markdown files
cd /home/denni/wiki/clients/$CLIENT
for f in IDENTITY.md CONTEXT.md README.md _config/*.md; do
  sed -i "s/{{CLIENT_SLUG}}/$CLIENT/g; s/{{CLIENT_NAME}}/Acme Ventures/g; s/{{CLIENT_ONE_LINE}}/Replace this with a one-sentence description/g" "$f"
done

# 3. Tell Hermes about it
hermes config set clients.active $CLIENT   # optional — for whichever client you're working on today
```

## What you get

```
clients/<client-slug>/
├── IDENTITY.md           # Layer 0 — workspace map, rules, escalation
├── CONTEXT.md            # Layer 1 — task routing table
├── README.md             # human-facing overview (optional, mirrors IDENTITY.md)
├── _config/              # Layer 3 — voice, conventions, glossary
│   ├── voice.md          # tone, audience, do/don't
│   ├── conventions.md    # file naming, folder rules, version conventions
│   └── glossary.md       # domain terms (CDFI, MCF, CLT, …)
├── projects/             # validated deliverables only — promoted from drafts/
│   └── README.md
├── drafts/               # AI-generated work in progress — gate before projects/
│   └── README.md
├── deliverables/         # final, client-ready exports (HTML, PDF, DOCX)
│   └── README.md
├── drafts-preview/       # HTML previews of drafts/ (auto-built by build.py)
│   └── README.md
└── skills/               # client-specific skills (optional)
    └── README.md
```

## Layer mapping

| ICM Layer | This template |
|-----------|---------------|
| 0 — Identity | `IDENTITY.md` (always loaded at session start) |
| 1 — Routing | `CONTEXT.md` (task → destination table) |
| 2 — Stage contracts | Use `projects/<pipeline>/stages/NN_*/CONTEXT.md` when you build a multi-stage pipeline. Quick-mode clients do not require physical stage folders. |
| 3 — References | `_config/` (cross-stage) and `<stage>/references/` (per-stage) |
| 4 — Outputs | `drafts/` (pre-HITL), `deliverables/` (post-HITL, final), `projects/` (validated source artifacts) |

## Source-of-truth rule (HARD GATE)

1. **AI generates → `drafts/`** (Markdown source + optional `drafts-preview/` HTML render).
2. **Dennis reviews** (or designated human approver).
3. **Validated file → `projects/`** (the source-of-truth artifact) **and** `deliverables/` (the client-ready export).

The `wiki-source-of-truth-governance` skill enforces this rule on every agent. Do not bypass.

## When to graduate to Full-mode ICM

If a client workspace develops a multi-stage pipeline that runs repeatedly (e.g. Spectra's county intelligence pipeline), add `projects/<pipeline>/stages/NN_*/CONTEXT.md` contracts. Until then, stay in Quick-mode — earn complexity.
