---
title: Wiki Sync Pipeline — How a New Note Reaches All Three Targets
created: 2026-08-21
updated: 2026-08-21
type: process / runbook
tags: [process, runbook, wiki, graphify, github, obsidian, sync]
sources: [https://github.com/Ksdeng1559/klicksmartai-wiki/blob/master/processes/wiki-sync-pipeline.md]
owner: Hermes (CoS)
status: permanent
---

# Wiki Sync Pipeline

How a new note (e.g. a competitive battlecard from scraping) flows from the local source to all three retrieval targets: **GitHub wiki**, **Obsidian vault**, and the **graphify knowledge graph**.

## The three targets

| Target | Path | Owned by |
|---|---|---|
| **KlickSmartAI wiki** (canonical) | `~/wiki/` (git origin: `https://github.com/Ksdeng1559/klicksmartai-wiki.git`, branch `master`) | Hermes |
| **Obsidian vault** (mirror) | `~/vault/` (git origin: `github-wiki:Ksdeng1559/klicksmartai-wiki.git`, branch `main`) | Dennis |
| **Graphify knowledge graph** | `~/wiki/graphify-out/graph.json` (16,964 nodes, 16,497 edges) | Hermes |

## One-time setup (already done)

- `~/wiki` is a git repo with `origin` pointing to GitHub via HTTPS (PAT in `~/.hermes/github-pat.txt`).
- `~/vault` is a git repo with `origin` pointing to GitHub via SSH (`github-wiki` SSH host alias → `klicksmartai_wiki` key).
- `~/vault/wiki/` is a manual mirror of `~/wiki/` (not auto-managed — files copied as needed).
- `graphify` CLI is installed at `~/.local/bin/graphify` (v0.9.46). The graph lives at `~/wiki/graphify-out/graph.json`.

## Permanent cron pipeline

| Cron job | Schedule | Purpose |
|---|---|---|
| `wiki-continuous-ingest` | hourly | Detects new/modified .md in `~/vault/wiki/`, hashes, queues into Redis → ARQ worker → Qdrant vector upserts |
| `Daily wiki-graphify sync` | every 6h | `cd ~/wiki && graphify update .` → detects new files via SHA256 → re-extracts → commits `graph.json` → pushes to GitHub |
| `vault-sync` (vault_sync.py) | every 6h | `cd ~/vault && git pull --rebase origin master && git add -A && git commit && git push origin main:master` |
| `Daily wiki push to GitHub` | 20:00 daily | Agent run via open-cowork-integration — full sync of `~/wiki` to GitHub |
| `daily-brain-closing` | 21:00 daily | Agent run with `wiki-graphify-sync` + `obsidian` skills — closing-time reconciliation |
| `weekly-brain-cleanup` | Sun 22:00 | Agent run with `wiki-graphify-sync` + `obsidian` skills — weekly sweep |

## Manual workflow — adding a new competitive battlecard (or any new wiki note)

1. **Drop the file in `~/wiki/`** at the right path:
   ```bash
   cp new-battlecard.md ~/wiki/competitive/new-battlecard.md
   ```

2. **Index it in the graph** (the canonical place where new docs get picked up):
   ```bash
   cd ~/wiki && graphify update .
   ```
   Graphify SHA256-diffs against its cache and only re-extracts what's new. For markdown that's never been semantically extracted, this triggers the LLM backend (Ollama/Gemini/etc.) to produce graph nodes for each section.

3. **Commit + push to GitHub**:
   ```bash
   cd ~/wiki
   git add competitive/new-battlecard.md graphify-out/graph.json graphify-out/manifest.json
   git commit -m "Add <name> competitive battlecard (scraped <date>)"
   git push origin master
   ```

4. **Mirror into Obsidian at `~/vault/wiki/`** with Obsidian-flavored frontmatter. Add at least:
   ```yaml
   ---
   title: <Page Title>
   created: <YYYY-MM-DD>
   updated: <YYYY-MM-DD>
   type: competitive / battlecard
   tags: [competitive, battlecard, <vendor>, gtm-research]
   company: <Company>
   domain: <domain.com>
   sources: [https://github.com/Ksdeng1559/klicksmartai-wiki/blob/master/competitive/...]
   related: [[entities-and-projects-index]]
   ---
   ```
   Then add a `[[wikilink]]` row to `~/vault/entities-and-projects-index.md` under the appropriate section.

5. **Commit + push vault**:
   ```bash
   cd ~/vault
   git add wiki/competitive/new-battlecard.md entities-and-projects-index.md
   git commit -m "Mirror <name> battlecard to Obsidian vault"
   git push origin main
   ```

6. **Verify** end-to-end:
   ```bash
   cd ~/wiki && graphify query "<Company> pricing" --budget 1500
   ```
   Should return the new file's nodes within the first 5 results.

## Common failure modes

| Symptom | Cause | Fix |
|---|---|---|
| New file not in graph | `graphify update .` only re-extracts **code** (AST); markdown needs full `graphify extract .` | Run `graphify extract .` (full semantic LLM pass) — costs tokens |
| `git push` rejected (non-fast-forward) | `~/wiki` master and remote diverged | `git pull --rebase origin master && git push origin master` |
| Vault push "reference already exists" | SSH session re-init | Run `git push origin main` again — usually succeeds |
| Cron run reports `error` but no Telegram message | The graph_ingest or vault_sync script is `no_agent=true` with `deliver=local` — output is silently saved | Check `~/.hermes/logs/` or run the script manually |

## Always: the source of truth is the local file

The chain is **local → GitHub → vault → graph (rebuild) → Qdrant (vector)**. If anything on GitHub looks wrong, fix the local file and re-run the manual workflow. Never edit GitHub directly.

## See also

- `wiki-graphify-sync` skill — `/wiki` command surface
- `obsidian` skill — vault conventions
- `entities-and-projects-index.md` (vault) — master wikilink index
- `wiki-folders-index.md` (vault) — folder inventory
