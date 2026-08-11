---
title: Hermes Gateway Architecture
created: 2026-08-11
updated: 2026-08-11
type: concept
tags: [codebase, concept, gateway, platform, cli]
sources: [raw/articles/2026-08-11-hermes-source-tour.md]
confidence: high
---

# Hermes Gateway Architecture

How Hermes ingests messages from many platforms and routes them into agent
sessions.

## Layout
- `gateway/run.py` (~16,800 lines) — main runner. Owns session lifecycle,
  message queue, agent cache, restart recovery.
- `gateway/platforms/` — adapter modules per platform. Each implements a
  common interface (see `gateway/platforms/base.py`).
- `gateway/session.py` (~1444 lines) — session data model and store.
- `gateway/api_server.py` — Open WebUI / HTTP API adapter (lets webui talk
  to the gateway via REST).
- `gateway/webhook.py` — generic webhook ingress for webhook subscriptions.

## Supported platforms
Telegram, Discord, Slack, WhatsApp, Signal, Matrix, Mattermost, Home
Assistant, DingTalk, Feishu (Lark), WeCom, BlueBubbles (iMessage), Weixin
(WeChat), Email, SMS, API Server, Webhooks, QQBot, Yuanbao.

That's 15+ messaging platforms + API Server for the WebUI. See
`hermes gateway setup` for actual wiring.

## Message flow
1. Adapter receives a message from the platform.
2. Adapter normalizes to a `MessageEvent` with a `SessionSource`.
3. `GatewayRunner` looks up or creates the `session_key`/`session_id`.
4. Agent invocation is queued (per-session FIFO).
5. Agent runs; intermediate events stream back via the adapter's outbound
   helpers (typing indicators, edit-in-place, reactions).
6. Final response is delivered back through the adapter.

## Restart / recovery
- `lifecycle_guard.py` and the `GatewayRunner` track in-flight jobs.
- `agent.restart_drain_timeout: 60` (s) — wait for in-flight to finish before
  hard exit.
- Mid-session: pending messages queue; completed assistant messages don't
  get redelivered.

## Watch out
- `systemctl --user restart hermes-gateway` kills the active session
  (in-gateway restart path).
- See [[Gateway-Restart-Procedure]] for the safe pattern.

## See also
- [[Hermes-Session-Lifecycle]]
- [[Cron-Architecture]]
- [[Hermes-Webui-Deployment]] (WebUI talks to gateway over the API Server adapter)