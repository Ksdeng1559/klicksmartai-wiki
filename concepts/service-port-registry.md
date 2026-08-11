---
title: Service & Port Registry
created: 2026-08-11
updated: 2026-08-11
type: concept
tags: [port, network, docker, systemd, hermes-webui, leadsniper, open-seo]
sources: [raw/articles/2026-08-11-port-scan.md]
confidence: high
---

# Service & Port Registry

What's listening where on Dennis's machine (snapshot 2026-08-11). Use this
before deploying anything that binds a port.

## Loopback services (`ss -tlnp` output)

| Port | Bind | PID | Process | Backed by |
|------|------|-----|---------|-----------|
| **8787** | 127.0.0.1 | 6266 (was) → Docker now | `hermes-webui/server.py` (was) → `hermes-webui` container | Docker (`docker compose` in hermes-webui-deploy/) |
| **8644** | 127.0.0.1 | 6590 | `hermes` (gateway) | systemd `--user hermes-gateway` |
| **9119** | 127.0.0.1 | 352 | `hermes` (dashboard) | systemd `--user hermes-gateway` |
| 8000 | 0.0.0.0 | Docker | `leadsniper-30-backend` (uvicorn) | Docker |
| 3002 | 127.0.0.1 | Docker | `open-seo-open-seo-1` (DataForSEO-backed) | Docker |
| 8090 | 0.0.0.0 | Docker | `leadsniper-30-leadsniper` | Docker |
| 8080 | 0.0.0.0 | Docker | `memory-os-worker` (ARQ) | Docker |

## Rules
- **All loopback Hermes ports (8644, 8787, 9119) are 127.0.0.1 only** — not
  exposed on the LAN. Safe to leave without a password; LAN access requires
  a deliberate port mapping change + password.
- **Before binding a new port:** check this table + `ss -tlnp` to avoid conflicts.
- **Systemd-owned services** (gateway, dashboard) survive WSL logout only if
  `sudo loginctl enable-linger $USER` was set. Verify with `loginctl show-user denni`.
- **Docker Desktop container ports** are independent — adding/removing
  containers does NOT affect the systemd Hermes services.

## Restore systemctl-managed Hermes
If a systemctl restart breaks the session (per Hermes skill: in-gateway restart
kills session):
```
systemctl --user restart hermes-gateway   # from another terminal
```

## See also
- [[Hermes-Environment-Map]]
- [[Hermes-Webui-Deployment]]