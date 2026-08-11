---
title: hermes-cron-management (skill)
created: 2026-08-11
updated: 2026-08-11
type: entity
tags: [entity, skill, cron, hermes, scheduling]
sources: []
confidence: high
---

# hermes-cron-management (skill)

**Eleventh-most-loaded skill (12 uses).** How to manage Hermes cron jobs —
create, edit, merge, delete, fix syntax, patch jobs.json directly.

## Source
`~/.hermes/skills/devops/hermes-cron-management/`

## PATH pitfall (CRITICAL for cron scripts)
Cron runs in minimal `$PATH` (usually `/usr/bin:/bin`) — user-local bins
like `/home/denni/.local/bin` are NOT inherited.

**Fix:** always export the full PATH at the top of a cron script block:
```bash
export PATH="/home/denni/.local/bin:/usr/local/bin:/usr/bin:/bin"
```

Python that imports `hermes_constants` also needs venv activation:
```bash
export PATH="/home/denni/.local/bin:/usr/local/bin:/usr/bin:/bin"
cd ~/.hermes/hermes-agent && source venv/bin/activate
PYTHONPATH=/home/denni/.hermes/hermes-agent python /path/to/script.py
```

## Cron syntax pitfalls
- Day-of-week `*/n` does NOT work: `0 8 * * */7` is invalid.
- "Every 7 days from a start date" — use daily trigger with skip logic OR
  weekly schedule (preferred).

## Git rebase pattern
When a cron job pulls from a remote and local uncommitted changes exist,
plain `git pull` rejects. Use stash → rebase → pop:
```bash
git stash --include-untracked
git pull --rebase origin main
git stash pop
```

## Jobs.json is source of truth
- Path: `~/.hermes/cron/jobs.json`
- Output logs: `~/.hermes/cron/output/`
- Edit directly with `patch` when CLI won't accept the change, then force a
  flush via `hermes cron edit <job_id> --name "<same-name>"`.

## Silent / local-only delivery
For fire-and-forget maintenance jobs:
```json
{"deliver": "local", ...}
```
Output logs go to disk but no notification fires.

## See also
- [[Hermes-Cron-Architecture]]
- [[Hermes-Environment-Map]]