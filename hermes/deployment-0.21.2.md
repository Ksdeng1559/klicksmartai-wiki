---
type: TECH
created: 2026-09-12
updated: 2026-09-12
confidence: 0.95
sources: [session 20260912_080050 weekly-tech-update, session 20260912_170028 hermes-update-weekly]
related: [[config-and-health-baseline]]
tags: [hermes, deployment, wsl, graphify, devops]
status: active
---

# Hermes Agent 0.21.2 — Deployment Facts (2026-09-12)

Hermes Agent deployed at **v0.21.2 (2026.9.11, upstream `de2d6a1b`)** via weekly `hermes update`. Single install serves CLI + Desktop GUI (Electron reads the same checkout). Reusable operational facts from the 2026-09-12 update run:

## Reusable facts

- **Desktop on WSL needs `DISPLAY=:0`.** Plain `nohup ~/.local/bin/hermes-desktop` fails with "Missing X server" (WSL X11 quirk). Launch with `DISPLAY=:0` in the env — then `pgrep -af 'release/linux-unpacked/Hermes' | wc -l` should be ≥ 6.
- **`hermes skills sync` does NOT exist** in v0.21.2. Use `hermes skills update` (not `sync`); it preserves local edits unless `--force` (e.g. `baoyu-article-illustrator`).
- **`hermes services restart` is invalid** — the command is `hermes gateway restart`. Gateway restart deferred in cron by safety guard (would kill in-flight agent); it restarts after the active work unit finishes.
- **graphify upstream 0.9.59** (safishamsi/graphify, branch v8, commit 522ea966, 2026-09-12): incremental dedup node-loss fix, pool-start fallback, **47% faster extraction**. Not on PyPI — track via git only.
- **Update autostash warning**: stale autostashes >7 days old accumulate; review with `git stash show -p <entry>` and drop to avoid clutter (two existed 2026-09-12, from 2026-06-20 and 2026-05-27).

## Pending tech debt (as of 2026-09-12)

- **hermes-agent CI: every recent run returns `action_required`** (no green-build window). Likely a manual approval / secret-rotation gate — needs a maintainer/Dennis click. RFC: `tech-debt/github/hermes-agent/rfc.md`.
- **GitHub PAT lacks `security_events` scope** → Dependabot alerts API returns 403. One-time scope bump needed.
- Update pulled 169 additional commits to `de2d6a1b` in the same-day second run; gateway restarted to new code (pid 81289), desktop at 6 procs, dashboard on :9119.

Mirror of Obsidian vault note `wiki/tech/hermes-0.21-deployment.md`.
