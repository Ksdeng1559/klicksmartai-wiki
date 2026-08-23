# RFC — klicksmartai-wiki (Ksdeng1559/klicksmartai-wiki)

**Audit date:** 2026-08-22 (Saturday)
**Repo:** https://github.com/Ksdeng1559/klicksmartai-wiki (public, 1 star, 4 open issues)
**Local checkout:** ~/wiki (branch master, HEAD `8ef3d65` — **0 behind origin/master**, in sync)
**Remote:** origin = GitHub (PAT-embedded URL — see Risk)

## 1. Git Status

- Branch `master`, HEAD `8ef3d65` "wiki graphify sync 2026-08-22" — **in sync with origin** (0 behind)
- Working tree: modified `graphify-out/.graphify_labels.json`, untracked `agency-agents` — normal sync artifacts
- Last pushed 2026-08-22 12:01Z (daily wiki auto-update cron active, this commit is the latest cron sync)
- `8ef3d65` is new since last cycle (last week's HEAD was `3a29d29` Veritas Growth Program pilot plan)

## 2. Dependency Health

- Pure documentation/wiki repo — no code dependencies, no package manifests
- Not applicable

## 3. CI/CD Pipeline

- No CI workflows on this repo (wiki auto-update is a cron push, not Actions)
- 4 open issues — none of a CI nature (typical wiki content requests)
- 0 open PRs

## 4. Recent Merged PRs

- No PR-based workflow — direct pushes. Last 5 commits:
```
8ef3d65 wiki graphify sync 2026-08-22  (cron auto-update)
4b92fa5 wiki auto-update
3a29d29 Add Veritas Growth Program pilot plan
20b5a80 AgentSource MCP tool inventory
```
All routine wiki auto-update commits; no human-driven content this cycle.

## 5. Recommended Actions for Claude Code

- [ ] **CRITICAL (carried from 2026-06-20, STILL OPEN): rotate the GitHub PAT embedded in the `origin` remote URL.** `git -C ~/wiki remote -v` still shows `https://Ksdeng1559:ghp_WO...Ry7t@github.com/Ksdeng1559/klicksmartai-wiki.git`. The token is in plaintext in `.git/config` and grants full access to Ksdeng1559's account. Rotate at GitHub → Settings → Developer settings → PATs, then update the remote URL (or switch to SSH/credential helper). This was flagged in the June 20 RFC and remains unfixed across 9 weekly cycles.
- [ ] No other actions this cycle

## 6. Risks / Notes

- Wiki is healthy and in sync. The cron auto-update is working as designed.
- The PAT rotation item is the only outstanding tech debt; it's also the highest-severity one. Worth a direct ask to Dennis.
