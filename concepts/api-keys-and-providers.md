---
title: API Keys & Provider Catalog
created: 2026-08-11
updated: 2026-08-11
type: concept
tags: [environment, key, provider, model]
sources: []
confidence: high
---

# API Keys & Provider Catalog

What credentials and providers are wired into Dennis's Hermes install (snapshot
2026-08-11). Verify before any paid-enrichment or model-swap work.

## Source of truth
- `~/.hermes/.env` — all API keys (shell source). Permissions should be 600.
- `~/.hermes/config.yaml` — provider routing, model default, fallback chain.
- Use `hermes doctor` to detect missing/outdated config.

## Active providers (from config)
| Provider | Default model | Notes |
|----------|---------------|-------|
| `ollama-cloud` | `kimi-k3` (default) | base_url `https://ollama.com/v1`, api_key `ollama` |
| `deepseek` | `deepseek-chat` | Fallback when kimi-k3 unavailable |

## Keys present in `.env`
- `OPENROUTER_API_KEY`
- `SLACK_BOT_TOKEN`, `SLACK_APP_TOKEN`
- `TELEGRAM_BOT_TOKEN`, `TELEGRAM_ALLOWED_USERS`
- `GROQ_API_KEY` (Whisper)
- `BRAVE_API_KEY` (default web search)
- `SERPER_API_KEY` (Google/SerpApi)
- `TAVILY_API_KEY` (deep research)
- `DATAFORSEO_USERNAME`, `DATAFORSEO_PASSWORD` (LeadSniper provider)
- `EXA_API_KEY` (deep/people search)
- `FIRECRAWL_API_KEY`
- `MINIMAX_API_KEY`
- `OLLAMA_API_KEY`
- `PARALLEL_API_KEY` (Parallel.ai; + `MCP_PARALLEL_AI_API_KEY` for MCP)
- `DEEPSEEK_API_KEY`
- `SEARXNG_URL`

## Configuration knobs to know
- `agent.max_turns: 90` — hard cap on tool-call loops per turn.
- `agent.gateway_timeout: 1800` (s); warning at 900s.
- `agent.clarify_timeout: 600` (s); how long a `clarify` waits for user.
- `terminal.timeout: 600` (s); shell command default.
- `max_live_sessions: 16`; max concurrent sessions in store.
- `model.context_length: 131072` for kimi-k3.

## See also
- [[Search-Provider-Rotation]]
- [[Hermes-Environment-Map]]
- [[Model-Routing]]