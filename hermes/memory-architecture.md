# Hermes — Memory Architecture

## Two-Layer Memory System

| Layer | Scope | Duration |
|-------|-------|----------|
| **Ephemeral** | Current session context | Until session ends |
| **Permanent** | ~/wiki (2nd brain) | Forever |

## Rule

Session facts that prove durable and recurring → upgrade to wiki.
Wiki is always consulted first. Wiki is always written back to.

## Session Behavior

1. Check ~/wiki for relevant context before answering
2. Hold session-state in ephemeral memory
3. When a fact recurs or proves durable → write to ~/wiki
4. Run graphify → push to GitHub

## Upgrade Triggers

- A fact is referenced 3+ times across sessions
- A client decision or project detail that affects future work
- A process that wasn't documented but should be
- A correction or preference the user stated

---

## Honcho v3 — Reasoning Memory Layer (added 2026-08-18)

Honcho v3 self-hosted is the cross-LLM memory layer. It extracts *conclusions* (reasoning-first), not just matching chunks, and is shared across Hermes, Claude Code, and ChatGPT via MCP.

### Deployment (Docker, self-hosted)

| Component | Detail |
|-----------|--------|
| Repo | `/mnt/g/AI-Applications/honcho` |
| API | `http://127.0.0.1:8001` (health: `/health`) |
| Postgres | pgvector, container `honcho-database-1` |
| Redis | `127.0.0.1:6380` (remapped from 6379 — RIOS owns 6379) |
| Deriver | background worker, container `honcho-deriver-1` |
| LLM (text-gen) | DeepSeek (`deepseek-chat`) — deriver, summaries, dialectic, dream |
| Embeddings | OpenRouter `text-embedding-3-small` (DeepSeek has no embedding API) |
| Auth | off (local MVP), bound to localhost only |

### MCP Bridge

- MCP server: Cloudflare Worker in `honcho/mcp/`, run via `bun run dev --port 44547`
- Points at self-hosted API via `HONCHO_API_URL=http://127.0.0.1:8001` in `mcp/.dev.vars`
- Wired into Hermes `~/.hermes/config.yaml` under `mcp_servers.honcho`
- 31 tools: workspace, peer, session, conclusion, search, chat, dream

### Workspaces (client isolation)

| Workspace | Source | Purpose |
|-----------|--------|---------|
| `klicksmartai-wiki` | `~/wiki` | KlickSmartAI wiki knowledge base |
| `obsidian-vault` | `/mnt/g/Documents/KlicksmartWiki/Klicksmartai` | Obsidian vault knowledge |
| `hermes-test` | — | smoke test |

### Ingestion

Script: `/mnt/g/AI-Applications/honcho/ingest_honcho.py`

```
python3 ingest_honcho.py <source_dir> <workspace_id> [--session <id>] [--limit N]
```

Chunks markdown on paragraph boundaries (~1500 chars), adds each chunk as a message with a `[SOURCE: <relpath>]` header. Obsidian vault fully ingested (49 files, 129 chunks). Wiki fully ingested (4,246 files, 37,272 chunks).

### Notes / Gotchas

- OpenRouter key must be valid — old key in `~/.hermes/.env` was dead ("User not found"); new key set in `honcho/.env` only.
- Port 8000 was taken by Docker Desktop backend → API on 8001.
- Port 6379 taken by RIOS Redis → Honcho Redis on 6380.
- MCP server needs `Accept: application/json, text/event-stream` header.
- AGPL-3.0 license — fine for internal use; reconsider only if shipped commercially.

---

Last updated: 2026-08-18

---

## Brain Closing — Governed Daily Pipeline (added 2026-08-18)

A **governed knowledge pipeline** (not a blind dump) that closes each day. Every session candidate is classified and routed to exactly one durable home.

### 5-Layer Model (locked)

| Layer | Role | Location | Purpose |
|-------|------|----------|---------|
| **Honcho** | Dynamic agent memory | Memory OS (Qdrant+Redis+ARQ Worker) | Primary cross-session memory — durable prefs, corrections, env facts, conventions |
| **Obsidian** | Curated durable knowledge | `/mnt/g/Documents/KlicksmartWiki/Klicksmartai` (PARA) | 2nd brain. Only decisions, architecture changes, SOPs, client facts, lessons, project status, approved research, strategy |
| **Graphify** | Derived graph/index | `~/wiki/graphify-out` | markdown-capable v0.9.46; ~71x cheaper per query than raw corpus |
| **GitHub Wiki** | Versioned shared source | `Ksdeng1559/klicksmartai-wiki` | origin master; HTTPS+PAT auth (SSH unavailable) |
| **Supabase** | Exact operational records | LeadSniper/SGI | DO NOT touch in brain-closing routine |

### Classification Rules

- **SKIP** (noise): task progress, completed-work logs, trivial exchanges, transient status → write nowhere.
- **HONCHO**: durable prefs, corrections, env facts, stable conventions → memory, not Obsidian.
- **OBSIDIAN**: decisions, architecture changes, SOPs/workflows, client facts, lessons, project status, approved research, reusable strategy → promote to PARA only.

### Routine Steps (daily cron)

1. **Decision extractor** — `session_search` sweep (query="", sort="newest").
2. **Classify significance** — SKIP / HONCHO / OBSIDIAN.
3. **Write to Obsidian** — terse markdown, correct PARA folder, [[wikilinks]], append/update if exists, write nothing if nothing qualifies.
4. **Re-index** — `cd ~/wiki && graphify update .` (only if notes written).
5. **Sync** — commit `brain closing YYYY-MM-DD`, push to GitHub origin via PAT (`~/.hermes/github-pat.txt`), rebase-first.
6. **Report** — tight owner summary: items extracted, promoted (list), skipped, graph node count, sync status.

Mirror: Obsidian note at `wiki/concepts/hermes-memory-architecture.md` (vault).

Last updated: 2026-08-18