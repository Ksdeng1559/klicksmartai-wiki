---
title: Hermes WebUI Deployment
created: 2026-08-11
updated: 2026-08-11
type: runbook
tags: [deploy, docker, hermes-webui, recovery, pattern]
sources: [raw/articles/2026-08-11-webui-deployment.md]
confidence: high
---

# Hermes WebUI Deployment

How the Hermes WebUI (https://github.com/nesquena/hermes-webui) was deployed
in Dennis's environment on 2026-08-11, replacing the previous `python3 bootstrap.py`
process on port 8787.

## Topology
**Single-container Docker** (from `docker-compose.yml` in the repo). One container
runs the agent + webui together. Chosen because:

- The existing hermes-gateway systemd service already owns cron/gateway on :8644.
  Adding a second hermes-agent image (two/three-container compose) would create
  a second gateway competing for cron/state.
- Bind-mounting the real `~/.hermes` into one container mirrors the
  `python3 bootstrap.py` single-process model Dennis already ran.

## Files
- **Source:** `/mnt/g/AI - Coding Projects/Dare2drean/hermes-webui/` (git clone)
- **Compose dir:** `/mnt/g/AI - Coding Projects/Dare2drean/hermes-webui-deploy/`
  - `.env` — UID/GID/HERMES_HOME paths
  - `docker-compose.yml` — single-service, port 8787, bind-mounts
- **Image:** `hermes-webui-deploy-hermes-webui:latest` (local build, no registry)
- **Container:** `hermes-webui`

## Mount paths (Docker Desktop on Windows)
```yaml
volumes:
  - ${HERMES_HOME}:/home/hermeswebui/.hermes      # C:\Users\denni\.hermes
  - ${HERMES_WORKSPACE}:/workspace                 # G:\AI - Coding Projects
```

`C:\...` form worked when smoke-tested; `/mnt/c/...` did not (no WSL integration).

## Day-to-day commands
Run from the compose dir:
```
docker.exe compose ps              # status
docker.exe compose logs -f         # tail logs
docker.exe compose restart         # bounce container
docker.exe compose down            # stop + remove container
docker.exe compose up -d           # start again
docker.exe compose pull && docker.exe compose up -d --build  # upgrade image
```

## Startup time
- **First boot:** ~12 minutes — init script rsyncs `~/.hermes/hermes-agent/`
  source into `/app/hermes-agent-src/`, then `uv pip install` for the agent's
  pyproject deps into `/app/venv`. Logs show the rsync warning about the
  agent source being writable.
- **Subsequent restarts:** ~30 seconds — `/app/venv` is cached, init skips
  the dependency install.

## Caveats
- **Logs only go to container stdout** — `docker.exe compose logs -f` is the way
  to watch. CLI session in WSL does not see them.
- **Old CLI webui must be stopped first** — `python3 bootstrap.py` binds :8787
  directly via the host agent venv. Kill it (e.g. `pkill -f hermes-webui/server.py`)
  before `docker compose up -d`.
- **No password set** — only `127.0.0.1:8787` is exposed (localhost-only).
  For LAN access, set `HERMES_WEBUI_PASSWORD=*** in `.env` and drop `127.0.0.1:`
  from the port mapping.
- **SQLite WAL warning** on every start: `cron/executions.db` uses
  `journal_mode=DELETE` because the bundled SQLite 3.46.1 has the WAL-reset
  corruption bug. Fix with `hermes update` (not blocking).

## See also
- [[Hermes-Environment-Map]] — where everything lives
- [[Wsl-Docker-Mounts]] — path translation
- [[Service-Port-Registry]] — port conflict check before deploy