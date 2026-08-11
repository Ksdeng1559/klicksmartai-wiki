---
title: Gateway Restart Procedure
created: 2026-08-11
updated: 2026-08-11
type: runbook
tags: [runbook, gateway, recovery, systemd, hermes-webui]
sources: []
confidence: high
---

# Gateway Restart Procedure

How to restart Hermes processes safely. **The user MUST be the one to trigger
a gateway restart — in-gateway restart kills the current session.**

## The rule
- `systemctl --user restart hermes-gateway` should be initiated by the user
  from another terminal (or by asking them to type it), never by the agent in
  the same session where it's serving responses.
- A `/restart` slash command in the gateway causes the active session to die.

## Services to know about
| Service | Restart command | Effect on session |
|---------|----------------|------------------|
| `hermes-gateway` (systemd) | `systemctl --user restart hermes-gateway` | kills current session |
| `hermes-webui` (Docker) | `docker.exe compose restart` (from `hermes-webui-deploy/`) | no effect — separate process tree |
| `hermes-dashboard` (subprocess of gateway) | restart gateway to refresh | indirect |
| LeadSniper / OpenSEO / memory-os (Docker) | `docker compose restart <svc>` (per project dir) | no effect on gateway |

## When something's stuck
1. **WebUI only broken?** → `cd ~/.../hermes-webui-deploy && docker.exe compose restart`.
2. **Gateway stuck / not responding?** → Ask the user to run
   `systemctl --user restart hermes-gateway` from another terminal.
3. **Container won't start?** → Check `docker.exe compose logs --tail 50` first.
4. **Init script hangs during fresh container start?** → The rsync of
   `~/.hermes/hermes-agent` from Windows host into the container is slow
   (~10 min). Don't kill it unless it's been >20 minutes with no log
   progress.

## See also
- [[Hermes-Webui-Deployment]]
- [[Service-Port-Registry]]
- [[Hermes-Environment-Map]]