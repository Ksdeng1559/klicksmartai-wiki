---
title: Source Notes — Environment Discovery (2026-08-11)
created: 2026-08-11
updated: 2026-08-11
type: source
tags: [source, environment, discovery]
sources: []
confidence: high
---

# Source Notes — Environment Discovery (2026-08-11)

Raw observations captured while deploying hermes-webui in Docker. This is a
"source" entry (not a wiki page) — quoted observations become claims on the
real wiki pages with provenance pointers.

## Observations
- `ls /mnt/c/Users/denni/` → user confirmed via Windows mount (path = `/c/Users/denni/`).
- `id -u && id -g` → 1000:1000.
- `docker --version` in WSL: "command not found". `docker.exe --version` →
  "Docker version 29.6.1, build 8900f1d".
- Docker Desktop container list (4 long-running): leadsniper-30-backend (:8000),
  open-seo-open-seo-1 (:3002), leadsniper-30-leadsniper (:8090), memory-os-worker (:8080).
- WSL distro list: `Ubuntu *`, `docker-desktop` — both Running v2.
- `find /mnt/wsl/docker-desktop -name "*.sock"` → empty (no /run/guest-services mount).
- `/usr/bin/docker` is dangling symlink to `/mnt/wsl/docker-desktop/cli-tools/usr/bin/docker`
  (target missing).
- Mount smoke test: `docker.exe run --rm -v 'C:\Users\denni/.hermes:/test' alpine ls /test`
  → returned config.yaml, cache, profiles, knowledge-config.json, etc. (real HERMES_HOME).
- Same with `\\wsl.localhost\Ubuntu\home\denni\.hermes:/test` → failed:
  "stat /run/guest-services/distro-services/ubuntu.sock: no such file or directory".
- `ss -tlnp` from WSL showed 8644 (hermes), 9119 (hermes), 8787 (python3 webui),
  then later 8787 (Docker container).

## Decisions made
1. **Use `docker.exe` from WSL**, not native `docker`. Avoid enabling WSL
   integration (bounces live containers).
2. **Use Windows paths (`C:\...`, `G:\...`)** for bind-mounts, not `/mnt/...`.
3. **Single-container compose**, not two/three-container — to avoid a second
   hermes-agent image competing with the existing gateway service.
4. **Bind-mount real HERMES_HOME RW** (Dennis approved explicit confirmation
   before the bind).
5. **No password initially**, port bound to 127.0.0.1 only.

## Verification evidence
- `curl http://127.0.0.1:8787/health` → `{"status": "ok", ...}` after ~12min.
- `docker inspect hermes-webui --format '{{.State.Health.Status}}'` → `healthy`.
- Logs show `/api/crons/recent`, `/api/dashboard/status`, `/api/health/agent`,
  `/api/settings` all responding 200.