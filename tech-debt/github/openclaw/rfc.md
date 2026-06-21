# RFC — openclaw (KlickSmartAI internal wiki mirror)

**Audit date:** 2026-06-20
**Repo:** https://github.com/Ksdeng1559/klicksmartai-wiki.git
**Local clone:** ~/wiki/tech-debt/github/openclaw
**Current branch:** master
**Local HEAD:** `a565e35` — Daily sync: 2026-06-19 20:00:01
**Upstream sync source:** `github-wiki` remote → `/home/denni/.hermes/wiki-github-wiki`

## 1. Dependency Status

This is **not a software project** — it's a markdown wiki mirror. No `package.json`, no `pyproject.toml`, no manifest at the repo root.

- Working tree is essentially **empty** — only `rca.md` (1711 bytes) and `rfc.md` (3221 bytes) are present, both untracked artifacts from prior audits.
- Subdirectory `../graphify` and `../hermes-agent` show as untracked from this clone's perspective (cross-listed via symlinks or parent listing), but they are siblings, not children.

## 2. CI/CD Health

- No `.github/workflows` content (not inspected — clone is bare content).
- Daily sync cron appears to be the "CI": commits every 24h with message `Daily sync: YYYY-MM-DD HH:MM:SS`. Last 5:
  ```
  a565e35 Daily sync: 2026-06-19 20:00:01
  aaff473 Daily sync: 2026-06-18 20:00:07
  29c7826 Daily sync: 2026-06-17 20:00:45
  0e92795 Daily sync: 2026-06-16 20:00:24
  861961b Daily sync: 2026-06-14 20:00:52
  ```
- The cron is **functional** but note: today (2026-06-20) has no commit yet. May still sync later, or may have failed silently — flag for follow-up tomorrow.

## 3. Recent Upstream Activity

`git fetch` against `github-wiki` advanced 7f09b82..11c0f52 on master. `origin` remote (KlicksmartAI fork) has 3 feature branches:
- `spectra-advertorial-os`
- `test/capital-feasibility-algorithm-san-antonio`
- `workflow/sbir-rios-grantfunding-ai`

## 4. Recently Merged PRs

Not applicable — wiki repo, no PR-based workflow.

## 5. Recommended Actions for Claude Code

1. **Audit remote credential exposure** — `git remote -v` revealed the `origin` remote URL embeds a GitHub PAT in plaintext (`Ksdeng1559:ghp_WO...Ry7t@github.com/...`). **This is a security finding** — the token grants `Ksdeng1559`'s access scope. Rotate the token and switch to SSH or credential helper immediately.
2. **Verify today's daily sync** runs at 20:00 UTC; if missing, check the cron service.
3. **Clean up untracked `rca.md` and `rfc.md`** from this clone OR move them to `~/wiki/tech-debt/github/openclaw/` parent — they don't belong in a wiki mirror.
4. **No code-level PR work needed** — wiki mirror.

## 6. Risks / Notes

- **CRITICAL: leaked PAT in `origin` remote URL** — see §5.1.
- Daily sync cadence is ~24h with one gap (no 2026-06-13 commit in last 5). Low severity — likely skipped.
- This clone has no remote-tracking for `origin/HEAD` — confirms it's a working/wiki repo, not a development fork.
