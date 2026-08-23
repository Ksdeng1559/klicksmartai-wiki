# RFC — openclaw (openclaw/openclaw)

**Audit date:** 2026-08-22 (Saturday)
**Repo:** https://github.com/openclaw/openclaw
**Local presence:** ~/wiki/tech-debt/github/openclaw — **no local clone** (directory holds only prior audit notes rca.md/rfc.md). Remote-only audit via GitHub API.

## 1. Git Status

- No local clone; remote state only
- Default branch: `main`; **387,118+ stars** (up from 385,548 last cycle, +1,570 this week), 6,079+ open issues (up from 5,635), **not archived**; last push 2026-08-22 15:00Z (active)
- Latest release: **v2026.7.1-2** (published 2026-08-04) — **unchanged for 18 days**, no new release this cycle

## 2. Dependency Health

- Not inspectable without a clone. OpenClaw is a TypeScript/Node project (large monorepo).
- Dependabot alerts API: 403 on free plan — not inspectable
- High release cadence: 5 releases in the week of 2026-08-04 (v2026.6.34 → v2026.7.1-2) — active maintenance, then a quiet ~2.5 week stretch

## 3. CI/CD Pipeline

- Last 5 runs (2026-08-22): All `ClawSweeper Dispatch` `skipped` (3x), `Auto response` `None` (in progress), `ClawSweeper Dispatch` `skipped`. No failures.
- Status: **healthy** (no failing workflows on default branch)

## 4. Recent Merged PRs (2026-08-22)

```
#127958 improve(whatsapp): reuse inbound message projection  (steipete, merged 14:51Z)
#127952 fix(agents): resolve pdf tool models through the canonical resolver  (obviyus, merged 14:32Z)
#127946 test(skills): stabilize workspace-load Windows symlink typing  (aniruddhaadak80)
#127945 test(skills): stabilize refresh Windows symlink typing  (aniruddhaadak80)
#127944 test(plugins): stabilize marketplace Windows symlink typing  (aniruddhaadak80)
#127941 test(skills): fix workspace-load Windows symlink typing  (aniruddhaadak80)
#127940 test(skills): use directorySymlinkType in refresh Windows symlink test  (aniruddhaadak80)
#127903 fix(ui): show channel probe progress while refreshing  (steipete, merged 13:32Z)
#127882 fix(mantis): pin harness pdf tool model to the catalog model  (obviyus, merged 12:48Z)
#127878 docs(mantis): script catalog-tool turns through Code Mode exec  (obviyus, merged 12:17Z)
#127877 improve(imessage): reuse prepared inbound account service  (steipete, merged 12:40Z)
#127875 fix(backup): reject malformed git log limits  (steipete, merged 12:15Z)
#127871 fix(mantis): keep caller stdin for the lease-fenced command  (obviyus, merged 11:22Z)
#127870 improve(mattermost): decode inbound websocket frames once  (steipete, merged 11:17Z)
#127859 feat(ui): render transcript footnotes as navigable endnotes  (vyctorbrzezowski)
```

**Theme this cycle:** Windows symlink test stability (5 PRs from aniruddhaadak80, all test-only), WhatsApp/iMessage/Mattermost inbound message projection improvements, mantis (Code Mode) PDF tool model resolution, UI channel-probe progress + transcript footnotes as endnotes. Active, healthy upstream.

## 5. Recommended Actions for Claude Code

- [ ] **No action required** — KlickSmartAI no longer runs OpenClaw (superseded by Hermes per memory). Tracked for awareness only.
- [ ] If OpenClaw integration is ever revived, clone from `openclaw/openclaw` and pin to release v2026.7.1-2+

## 6. Risks / Notes

- No local clone means no dependency/security audit possible from this environment without a full clone (~large monorepo)
- OpenClaw release cadence is high and fast-moving; any future integration should pin to tagged releases
- Latest release unchanged since 2026-08-04 — quietest stretch in 6+ weeks. Either a stabilization pause or a pre-release lock-in. Worth a one-line check next cycle.
- 1,570 new stars this week — community growth continues to outpace dev throughput
