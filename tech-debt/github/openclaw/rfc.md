# openclaw — Weekly Tech-Debt RFC

**Run date:** 2026-09-12 (Sat)
**Repo:** https://github.com/openclaw/openclaw
**Local mirror:** ~/wiki/tech-debt/github/openclaw/ (rca.md + rfc.md existing)
**Status:** upstream knowledge only — no KlickSmartAI code depends on it.

## Dependency status

- Upstream is large (389k stars) with broad Python/TS mix; full dep inventory not pulled this week (out of scope).
- No Dependabot alerts surfaced for our PAT.

## CI/CD health

Latest 5 Actions runs (2026-09-12):
| Workflow | Status | Conclusion |
|---|---|---|
| ClawSweeper Dispatch | completed | skipped |
| ClawSweeper Dispatch | completed | skipped |
| Maintainer Command Reactions | completed | skipped |
| Maintainer Command Reactions | completed | skipped |
| Maintainer Command Reactions | completed | skipped |

All *skipped* — likely repo-level branch protection or scheduled-only triggers. Not a CI failure.

## Recently merged PRs

`steipete` is the dominant merge author. Notable in window:
- #146021 refactor: share Memory Wiki imported-page test fixture
- #146020 fix: reduce large session catalog refresh overhead
- #146019 fix: support large SQLite worker commands with bounded transport
- #146016 fix: skip transcript reads for stale fallback notices
- #146015 refactor: keep native handles out of reply admission claims

No major version releases observed in this window.

## Recommended actions for Claude Code

1. **No action needed.** openclaw is on our radar for transition to Hermes Agent (see `hermes/openclaw-to-hermes-transition` skill) but not in active production. Continue low-cadence monitoring.
2. **Document any behavior we mirror** in `rca.md` if the session-catalog refresh change (#146020) overlaps with how Hermes indexes sessions.