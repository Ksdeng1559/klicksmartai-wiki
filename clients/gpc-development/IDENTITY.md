# IDENTITY.md — GPC Development Workspace

This is **ICM Layer 0**. It defines the workspace map, the rules of engagement,
and the source-of-truth gate. Both Hermes Agent and Claude Code auto-load this
on folder entry.

## What this workspace is

| Field | Value |
|-------|-------|
| **Client** | GPC Development |
| **Slug** | `gpc-development` |
| **Domain** | `gpcdevelopment.ca` |
| **Market** | Canada (Vancouver, BC) — DataForSEO locationCode 2124 |
| **Language** | English |
| **Engagement type** | SEO audit + organic inbound lead generation |
| **Compliance mode** | `none` (no securities, no PII, no HIPAA — pure marketing engagement) |
| **Workspace mode** | **Quick-mode** (flat `projects/` until recurring pipeline emerges) |
| **Vertical** | `seo` (default for organic lead-gen) |
| **OpenSEO project ID** | `34afee19-d725-4073-b43f-1b76c6275c11` |
| **DuckDB mirror** | `.local_tier/clients/gpc-development.duckdb` |
| **Cron sync** | `openseo-duckdb-sync` (every 30 min, scoped to this project) |

## Folder map

```
gpc-development/
├── CLAUDE.md                  # Hermes + Claude Code entry-point (NOT YET WRITTEN — pending Dennis approval)
├── IDENTITY.md                # this file (Layer 0)
├── CONTEXT.md                 # Layer 1 — task routing + 5-stage pipeline
├── README.md                  # human-facing overview
├── _config/
│   ├── voice.md               # tone for GPC-facing artifacts
│   ├── conventions.md         # file naming, folder rules
│   ├── deliverables.md        # vertical artifact map (seo)
│   ├── glossary.md            # domain terms (multifamily, GC, GC/CI, etc.)
│   └── gtm-skills.md          # empty — no GTM use-cases for this client yet
├── projects/
│   └── seo/                   # promoted deliverables (source of truth)
├── drafts/
│   ├── seo/                   # AI work in progress (pre-HITL)
│   │   └── VALIDATION_QUEUE.md  # what's pending review
│   └── README.md
├── deliverables/
│   └── seo/                   # client-ready exports (post-HITL)
├── drafts-preview/
│   └── seo/                   # HTML previews of drafts
├── skills/
│   └── README.md              # per-client skills (none yet)
├── scripts/
│   └── render-report.py       # Markdown → styled HTML
└── .local_tier/
    ├── clients/
    │   └── gpc-development.duckdb  # analytical mirror (synced from OpenSEO D1)
    └── exports/
```

## The source-of-truth gate (binding)

**Every AI-generated artifact for this client MUST land in `drafts/` first.**

Nothing is promoted to `projects/` or `deliverables/` until Dennis (and, where `compliance_mode` is non-`none`, a qualified reviewer) explicitly approves.

This is enforced:
- by reading this IDENTITY.md + CONTEXT.md at session start (CLAUDE.md binds this)
- by the lack of any other writable path in the skill workflow — the workflow only writes `drafts/` on first pass
- by the `VALIDATION_QUEUE.md` ledger in `drafts/seo/`

If a request would write directly to `projects/` or `deliverables/`, **refuse** and offer the draft route instead.

## Engagement rules

1. **Canadian market** — use `locationCode: 2124` for all SERP/keyword/PAA calls.
2. **Vancouver-specific positioning** — read `_config/voice.md` for tone.
3. **Multifamily primary, custom-home secondary** — don't recommend custom-home-first content unless Dennis redirects.
4. **Skip branded-developer SERPs** — Bosa, Concord Pacific, etc. are uncompetitive for a single firm.
5. **Show cost plan before any spend** — every SEO skill gates credit spend on a HITL approval package.
6. **Promotion requires Dennis's signature** — move from `drafts/seo/` to `projects/seo/` only after Dennis reviews and approves.

## Current state

| Item | Status |
|---|---|
| OpenSEO project (34afee19) | Created — 83 keywords seeded, 2 audits, 3 PAA scans, 1 rank tracker |
| Audit quote sheet (`drafts/seo/audit-quote-2026-08-26-gpc-development.md`) | In drafts/, awaiting Dennis's review |
| 3 test seeds (`test seo skill 1/2/3`) | Need cleanup |
| DuckDB mirror | Pending — script copied, sync scheduled |

## Escalation

| Trigger | Action |
|---|---|
| Dennis asks for a new client workspace template | Use `icm-client-workspace-setup` skill |
| Dennis wants to add a new vertical | Add folder, update `_config/deliverables.md` |
| Dennis wants compliance mode change | Update IDENTITY.md + create `_config/compliance.md` |
| Skill found buggy | Patch immediately with `skill_manage(action='patch')` |
| OpenSEO MCP server down | Check `docker ps`, then `openseo-deploy` skill |
| DuckDB sync broken | Run `~/.hermes/scripts/sync-openseo-duckdb.py` manually |

## See also

- `CONTEXT.md` — task routing table
- `_config/voice.md` — tone rules
- `_config/deliverables.md` — vertical artifact map
- `_config/gtm-skills.md` — GTM bindings (empty)
- `~/.hermes/skills/seo-enrichment-planner/SKILL.md` — universal SEO orchestration
- `~/.hermes/skills/openseo-project-intake/SKILL.md` — onboarding procedure
