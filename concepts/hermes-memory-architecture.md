---
type: CONCEPT
created: 2026-08-18
updated: 2026-08-18
confidence: 0.85
sources: [session 20260817_073210, session 20260817_151154, session 20260818_134402, Hermes agent governance]
related: [[hermes-chief-of-staff-os]], [[business-context-md]]
tags: [hermes, memory, architecture, honcho, obsidian, graphify, github-wiki, supabase]
status: active
---

# Hermes Memory Architecture (Layer Model)

A **governed knowledge pipeline** — not a blind dump. Five layers, each with a distinct role. Governed by the "brain closing" routine (daily cron) that classifies every item and routes it to exactly one durable home.

## The 5 Layers

| Layer | Role | Location | Purpose |
|-------|------|----------|---------|
| **Honcho** | Dynamic agent memory | External memory provider | Primary cross-session memory — durable preferences, corrections, environment facts, stable conventions |
| **Obsidian** | Curated durable knowledge | `/mnt/g/Documents/KlicksmartWiki/Klicksmartai` (PARA) | 2nd brain. Only decisions, architecture changes, SOPs/workflows, client facts, lessons, project status, approved research, reusable strategy |
| **Graphify** | Derived graph/index | `/home/denni/wiki/graphify-out` | markdown-capable v0.9.46; ~71x cheaper per query than raw corpus |
| **GitHub Wiki** | Versioned shared source | `https://github.com/Ksdeng1559/klicksmartai-wiki` | origin master; PAT auth (SSH unavailable for this repo) |
| **Supabase** | Exact operational records | LeadSniper/SGI | DO NOT touch in brain-closing routine |

## Classification Rules (brain closing)

For each candidate item from session sweeps:
- **SKIP** (noise): task progress, completed-work logs, trivial exchanges, transient status → write nowhere.
- **HONCHO**: durable preferences, corrections, environment facts, stable conventions → Hermes memory, not Obsidian.
- **OBSIDIAN**: decisions, architecture changes, SOPs/workflows, client facts, lessons learned, project status, approved research, reusable strategy → promote only these to PARA.

## PARA Structure (Obsidian)

`agents/`, `wiki/` (clients, concepts, inbox, lessons, processes, products, sources, synthesis, tech), `raw/` (exports, notes, pdfs). Notes use frontmatter (type/created/updated/confidence/sources/related/tags/status) and [[wikilinks]].

## Re-index + Sync (Step 4-5)

- Re-index: `cd /home/denni/wiki && graphify update .` (only if notes written).
- Sync: commit `brain closing YYYY-MM-DD`, push to GitHub origin via PAT at `~/.hermes/github-pat.txt`. Rebase before push if remote is ahead.
- Do NOT commit regenerable cache (`graphify-out/cache/`, `converted/` are gitignored).

## Key Facts

- Honcho = **primary** memory (permanence). Honcho platform integration was **deprecated** — use Memory OS stack (Qdrant + Redis + ARQ Worker) for external memory instead.
- **2026-08-18:** Honcho entry removed from `~/.hermes/config.yaml` `mcp_servers:` (was pointing at `localhost:44547`, nothing listening). Config backup preserved at `~/.hermes/config.yaml.bak-20260818-143716`. `hermes mcp list` now shows 14 enabled servers, no honcho. Runtime reconciles the MCP tree on its own reconnect cycle — no `mcp reload` subcommand exists.
- Graphify CLI: always `cd /home/denni/wiki && graphify update .` — `--output` syntax does not exist.
- GitHub PAT at `~/.hermes/github-pat.txt` (Ksdeng1559). Use HTTPS+PAT via curl, NOT .netrc/gh CLI.
- Graph JSON: node-link format (`nodes`, `links` keys — NOT `edges`).

## Brain Closing Routine (daily cron)

1. **Decision extractor** — `session_search` sweep today's sessions (query="", sort="newest").
2. **Classify significance** — SKIP / HONCHO / OBSIDIAN per rules above.
3. **Write to Obsidian** — terse markdown into correct PARA folder; append/update if note exists; write nothing if nothing qualifies.
4. **Re-index** — `graphify update .` (only if Obsidian notes written).
5. **Sync to GitHub** — commit `brain closing YYYY-MM-DD`, push via PAT, rebase-first.
6. **Report** — tight owner summary: items extracted, promoted (list notes), skipped, graph node count, sync status.

See [[hermes-chief-of-staff-os]] for the broader CoS operating layer this memory architecture serves.
