# openclaw — Weekly Tech-Debt RFC

**Run date:** 2026-09-19 (Sat)
**Repo:** https://github.com/openclaw/openclaw
**Local mirror:** ~/wiki/tech-debt/github/openclaw/ (rca.md + rfc.md existing) — **no .git directory**; this is a docs-only reference, not a clone
**Status:** upstream knowledge only — no KlickSmartAI code depends on it.
**Repo metadata (API 2026-09-19):** 386,749 stars · 81,260 forks · 5,775 open issues · pushed **2026-08-19** · language TypeScript · default branch `main`

## What changed since 2026-09-12

**Nothing upstream.** `pushed_at` is still 2026-08-19. Last week's report noted 14 merged PRs in window by `steipete`; no new public activity in the 7 days since.

We are observing **transition signals** in the KlickSmartAI context:
- The `openclaw-to-hermes-transition` skill is registered in our skill library (transition playbook).
- Memory note: "deprecated upstream RinDig PR; commercial GitHub org TBD" (2026-08-29).
- No live integration; this is a "watch the upstream" reference.

## Dependency status

- Upstream is large (389k stars at last check; 386,749 now) with broad Python/TS mix; full dep inventory not pulled this week (out of scope).
- No Dependabot alerts surfaced for our PAT.
- No CRITICAL security advisories in our local mirror.

## CI/CD health

No fresh pull of Actions runs this cycle (last week's all-skipped pattern still expected):
| Workflow | Status | Conclusion |
|---|---|---|
| ClawSweeper Dispatch | completed | skipped |
| ClawSweeper Dispatch | completed | skipped |
| Maintainer Command Reactions | completed | skipped |
| Maintainer Command Reactions | completed | skipped |
| Maintainer Command Reactions | completed | skipped |

All *skipped* — likely repo-level branch protection or scheduled-only triggers. **Not a CI failure.**

## Recently merged PRs

No new public activity since last week's snapshot. Last window still shows `steipete` as the dominant merge author with notable:
- #146021 refactor: share Memory Wiki imported-page test fixture
- #146020 fix: reduce large session catalog refresh overhead

## Recommended actions for Claude Code

1. **No action.** Upstream has been quiet for a month — this matches the "transition playbook" posture in our skill library.
2. **If a KlickSmartAI integration is being planned** (per the `openclaw-to-hermes-transition` skill), refer to that skill before drafting. The skill exists specifically so this RFC doesn't re-litigate transition scope each week.
3. **No PRs created.** Per policy: forks are future-only; weekly is read-only.

## Notes for Dennis

- "It looks fine" closes this.
- This RFC will stay quiet as long as upstream stays quiet. If `pushed_at` moves, the next run will flag the diff.
