# RFC — klicksmartai-wiki (Ksdeng1559/klicksmartai-wiki)

**Audit date:** 2026-08-08 (Saturday)
**Repo:** https://github.com/Ksdeng1559/klicksmartai-wiki (public, 1 star)
**Local checkout:** ~/wiki (branch master, HEAD `4b92fa5`, **0 behind origin/master** — in sync)
**Remote:** origin = GitHub (PAT-embedded URL — see Risk), github-wiki = local mirror ~/.hermes/wiki-github-wiki

## 1. Git Status

- Branch `master`, HEAD `4b92fa5` "wiki auto-update 2026-08-06", **in sync with origin** (0 behind)
- Working tree: modified `raw/repos/LeadSniper-3.0`, untracked `agency-agents` dir — normal sync artifacts
- Last pushed 2026-08-07 (daily wiki auto-update cron active)

## 2. Dependency Health

- Pure documentation/wiki repo — no code dependencies, no package manifests
- Not applicable

## 3. CI/CD Pipeline

- No CI workflows on this repo (wiki auto-update is a cron push, not Actions)
- No open issues of a CI nature

## 4. Recent Merged PRs

- No PR-based workflow — direct pushes. Last commits: `4b92fa5` wiki auto-update, `20b5a80` AgentSource MCP tool inventory, `95500c8` progressive enrichment architecture

## 5. Recommended Actions for Claude Code

- [ ] **CRITICAL (carried from 2026-06-20, STILL OPEN): rotate the GitHub PAT embedded in the `origin` remote URL.** `git -C ~/wiki remote -v` still shows `https://Ksdeng1559:ghp_WO...Ry7t@github.com/Ksdeng1559/klicksmartai-wiki.git`. The token is in plaintext in `.git/config` and grants full access to Ksdeng1559's account. Rotate at GitHub → Settings → Developer settings → PATs, then update the remote URL (or switch to SSH/credential helper). This was flagged in the June 20 RFC and remains unfixed.
- [ ] Address open issues: #3 "Prevent future pollution of master production memory branch", #2 "Restore master as production Hermes/wiki-llm/Graphify memory branch" — memory-branch hygiene
- [ ] Continue daily auto-update cadence (working fine)

## 6. Risks / Notes

- **PAT-in-remote-URL is a live credential exposure** — highest-severity security item in this audit. The token shown in remote -v output is partially masked in terminal output but fully present in `.git/config`
- Wiki remains the primary knowledge store and is syncing correctly
