# RFC — openclaw (openclaw/openclaw)

**Audit date:** 2026-08-15 (Saturday)
**Repo:** https://github.com/openclaw/openclaw
**Local presence:** ~/wiki/tech-debt/github/openclaw — **no local clone** (directory holds only prior audit notes rca.md/rfc.md). Remote-only audit via GitHub API.

## 1. Git Status

- No local clone; remote state only
- Default branch: `main`; **385,548+ stars**, 5,635+ open issues; **not archived**; last push 2026-08-15 (active)
- Latest release: **v2026.7.1-2** (published 2026-08-04) — unchanged since last cycle

## 2. Dependency Health

- Not inspectable without a clone. OpenClaw is a TypeScript/Node project (large monorepo).
- Dependabot alerts API: 403 on free plan — not inspectable
- High release cadence: 5 releases in the week of 2026-08-04 (v2026.6.34 → v2026.7.1-2) — active maintenance

## 3. CI/CD Pipeline

- Last 5 runs (2026-08-15): Test Performance Agent (pending), Docs Agent (pending), Maintainer Command Reactions (skipped), ClawSweeper Dispatch (skipped), Docs Agent (cancelled). No failures
- Status: **healthy** (no failing workflows on default branch)

## 4. Recent Merged PRs (2026-08-15)

```
#120527 fix(telegram): restore account-scoped reply mode (steipete)
#120611 fix: Telegram Crabbox proof uses resolved SSH target (steipete)
#120613 fix(release): dispatch validation through client-pushed target ref (steipete)
#120511 feat(macos): control motorized camera pan, tilt, zoom (steipete)
#120594 fix(codex): support app-server 0.147.0 (vincentkoc)
#120430 fix(cli): avoid missing-facing camera snap failures (steipete)
#120075 fix: gateway stalls for tens of seconds after each agent turn on multi-agent (sercada)
#120493 fix(ui): bulk session archive no longer stalls per thread (steipete)
```

Theme: Telegram reply mode fix, macOS camera control, codex app-server compat, gateway multi-agent stall fix, UI session-archive perf. Active, healthy upstream.

## 5. Recommended Actions for Claude Code

- [ ] **No action required** — KlickSmartAI no longer runs OpenClaw (superseded by Hermes per memory). Tracked for awareness only.
- [ ] If OpenClaw integration is ever revived, clone from `openclaw/openclaw` and pin to release v2026.7.1-2+

## 6. Risks / Notes

- No local clone means no dependency/security audit possible from this environment without a full clone (~large monorepo)
- OpenClaw release cadence is high and fast-moving; any future integration should pin to tagged releases
- Latest release unchanged since 2026-08-04 — no new release this cycle
