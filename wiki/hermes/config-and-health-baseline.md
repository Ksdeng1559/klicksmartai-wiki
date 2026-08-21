---
title: Hermes Config & Health Baseline
created: 2026-08-12
updated: 2026-08-12
type: reference
tags: [hermes, config, health, infrastructure, baseline, system]
---

# Hermes Config & Health Baseline

Canonical snapshot of the verified Hermes Agent configuration and system health (checked 2026-08-12). Purpose: recover the exact working config if storage is lost, and give a known-good baseline to diff against when something breaks.

## Active Model Routing

| Key | Value |
|-----|-------|
| Provider | `ollama-cloud` |
| model.name | *(not set — uses provider default)* |
| Fallback | `deepseek-chat` |
| Running model | `deepseek-v4-flash:0731` |

**User profile default:** primary = `kimi-k3` via `ollama-cloud`, fallback = `deepseek-chat` (deepseek). `model.name` is intentionally not pinned so the provider default wins.

## Version

- Hermes version: `0.20.0` (doctor-consistent)
- Python: `3.11.15`
- Venv: active (`~/.hermes/hermes-agent`)

## Configured API Keys (.env)

| Provider | Status | Notes |
|----------|--------|-------|
| OpenRouter | ✓ set | fallback/search backend |
| DeepSeek | ✓ set | model fallback |
| MiniMax | ✓ set | OAuth-eligible |
| Firecrawl | ✓ set | scraping |
| Tavily | ✓ set | search backend |

**Not set (only needed if routing to those providers):** OpenAI, Google/Gemini, xAI/Grok, Anthropic, Kimi/Moonshot, StepFun, DeepInfra, NVIDIA NIM, Z.AI/GLM, MiniMax-CN, ElevenLabs, FAL, Browser Use, Browserbase, GitHub.

## Gateway & Messaging

| Platform | Status |
|----------|--------|
| Telegram | ✓ configured |
| Slack | ✓ configured |
| Discord / WhatsApp / Signal / Email / SMS / DingTalk / Feishu / WeCom / Weixin / BlueBubbles / QQBot / Yuanbao | not configured |

- **Gateway:** running via systemd (user), PID 392
- **Cron scheduler:** active, 17/17 jobs, heartbeat ~43s
- **Dashboard:** HTTP 200 on `:9119`
- **Gateway port `:8644`:** returns 404 on root — normal (serves platform/API routes, no `/` health page)

## Hermes Web UI (`hermes-webui`)

A separate web UI (distinct from the `:9119` dashboard), installed 2026-08-11.

| Item | Value |
|------|-------|
| Repo | `/mnt/g/AI - Coding Projects/Dare2drean/hermes-webui` |
| State dir | `~/.hermes/webui` |
| Bind | `http://127.0.0.1:8787` |
| Health | `ok` (verified via `./ctl.sh status`) |
| ctl | `./ctl.sh <start\|stop\|restart\|status\|logs>` (from repo root) |
| Log | `~/.hermes/webui/bootstrap-8787.log` (bootstrap), `~/.hermes/webui.log` (daemon) |
| Default workspace | `/home/denni/workspace` |
| Default model provider | `ollama-cloud` |

**Notes / caveats:**
- Runs as a background daemon NOT managed by `ctl.sh` (no `~/.hermes/webui.pid`); health probe confirms it is listening and healthy on 8787.
- **No password set** (settings `password_hash: null`). Any process on the machine can read sessions and memory via the local API. Set `HERMES_WEBUI_PASSWORD` to enable auth.
- Agent health endpoint reported `gateway_not_configured` on one probe (agent-chat gateway backend not wired) — the WebUI itself still serves fine; this is the agent-chat integration channel, not the UI.
- Config lives in `~/.hermes/webui/settings.json` (theme `dark`, `default_model_provider: ollama-cloud`).

## Databases (doctor-verified, all healthy)

| DB | Mode |
|----|------|
| state.db | WAL (784.4 MB) |
| cron/executions.db | WAL |
| projects.db | WAL |
| response_store.db | WAL |
| memory_store.db | rollback journal |
| verification_evidence.db | WAL |
| kanban.db | WAL |

## Known Non-Blocking Notes

1. **Icarus hook** — occasional `LLM extraction failed (HTTPError)` warning → falls back to legacy. Transient, self-heals.
2. **Config version** `v33 → v34` — new settings available, warn-only.
3. **Deprecated** `display.tool_progress_overrides` → replace with `display.platforms` (warn-only, not auto-migrated).
4. **Auth not logged in** (optional): Nous Portal, OpenAI Codex, MiniMax OAuth, xAI OAuth, Qwen OAuth.

## Recovery Procedure

If config is lost, restore from:
- `~/.hermes/config.yaml` (settings)
- `~/.hermes/.env` (secrets)
- `~/.hermes/auth.json` (OAuth/credential pools)

Verify after restore: `hermes doctor` → `hermes status --all` → `hermes cron status`.

---
Last verified: 2026-08-12 (full `hermes status --all` + `hermes doctor` clean pass)
