---
title: Hermes Environment Map (Dennis's Setup)
created: 2026-08-11
updated: 2026-08-11
type: concept
tags: [environment, wsl, docker, windows, port, path, key]
sources: [raw/articles/2026-08-11-environment-discovery.md]
confidence: medium
---

# Hermes Environment Map

Where everything Hermes-related lives on Dennis's WSL+Windows machine.

## Hosts and OS
- **Host:** Windows 11 / WSL2 (Ubuntu distro)
- **WSL home:** `/home/denni`
- **Windows C: drive:** `/mnt/c/Users/denni/`
- **Windows G: drive:** `/mnt/g/`

## Hermes State (`HERMES_HOME`)
- **Path:** `/home/denni/.hermes/` (same path in both WSL and Hermes)
- **Agent source:** `/home/denni/.hermes/hermes-agent/` (git-installed, run_agent.py + hermes_cli/ + tools/ + gateway/)
- **Skills:** `/home/denni/.hermes/skills/` (~266 installed)
- **Config:** `~/.hermes/config.yaml`; secrets in `~/.hermes/.env`
- **Sessions:** `~/.hermes/sessions/` (SQLite, FTS5)
- **State:** `~/.hermes/webui/` (created 2026-08-11 by hermes-webui)

## Hermes Processes
| Process | Port | Backed by |
|---------|------|-----------|
| Gateway | 127.0.0.1:8644 | systemd `--user hermes-gateway` (NOT Docker) |
| Dashboard | 127.0.0.1:9119 | systemd `--user hermes-gateway` (subprocess) |
| **WebUI** | **127.0.0.1:8787** | **Docker container `hermes-webui`** (deployed 2026-08-11) |

^ All three read/write the same `~/.hermes/`. The webui is bind-mounted into the
container from `C:\Users\denni\.hermes` (Docker Desktop translates).

## Docker on this machine
- **Docker Desktop** runs on Windows (engine live). Several long-running
  containers: leadsniper-backend (:8000), open-seo (:3002), leadsniper-production
  (:8090), memory-os-worker (:8080).
- **This Ubuntu distro has NO WSL integration** mounted at
  `/run/guest-services/distro-services`. Symptom: `docker` is a dangling symlink,
  `docker.exe` works.
- **Workaround:** invoke `docker.exe` from WSL — binds to the Windows engine
  via named pipe. Bind-mounts use Windows paths (`C:\...`, `G:\...`), NOT `/mnt/c/...`.
- **Don't enable WSL integration** without user OK — it requires Docker Desktop
  restart which bounces the live containers.

## See also
- [[Wsl-Docker-Mounts]] — Windows ↔ WSL path translation rules
- [[Hermes-Webui-Deployment]] — how the Docker webui was set up 2026-08-11
- [[Service-Port-Registry]] — full port map (Docker containers + Hermes + other)