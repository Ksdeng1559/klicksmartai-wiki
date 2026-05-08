---
title: Claude Code Local — Apple Silicon Local AI Coding Agent
type: entity
entity_type: AI Coding Tool / Claude Code Fork
status: active
tags:
  - entity
  - claude-code
  - local-ai
  - apple-silicon
  - coding-agent
last_updated: "2026-04-20"
source: https://github.com/nicedreamzapp/claude-code-local
---

# Claude Code Local — Apple Silicon Local AI Coding Agent

**Author:** Matt Macosko (nicedreamzapp)
**GitHub:** 1.7k stars, 337 forks
**License:** MIT
**Platform:** Apple Silicon (MLX, unified memory)

---

## Core Innovation

**Problem:** Claude Code speaks Anthropic API. Local models speak OpenAI API. Everyone else bridges with a proxy (Ollama) — 3 processes, 2 translations, ~30 tok/s.

**Solution:** Custom server that eliminates the proxy entirely.

| Approach | Processes | Speed |
|----------|-----------|-------|
| ❌ Others: Claude Code → Proxy → Ollama → Model | 3 processes | ~30 tok/s |
| ✅ Claude Code Local: Claude Code → Their Server → Model | 1 process | **65 tok/s** |

**Result: 7.5× faster** (133s → 17.6s per task)

---

## Model Lineup

| Model | Params | Speed | RAM | Best For |
|-------|--------|-------|-----|---------|
| **Qwen 3.5** | 122B | **65 tok/s** | ~75 GB | Max throughput, MoE sparsity |
| **Llama 3.3** | 70B | ~7 tok/s | ~75 GB | Hardest reasoning, full precision |
| **Gemma 4** | 31B | ~15 tok/s | ~18 GB | Daily coding, fits 64GB Mac |

---

## Architecture

```
Your code → Claude Code CLI
     ↓ HTTP localhost:4000
  Their server.py (MLX)
     ↓ Metal API
  Apple GPU (unified memory)
     ↓
  Local model (Qwen/Llama/Gemma)
```

**Data never leaves the Mac** (except 1 non-blocking startup handshake to api.anthropic.com — firewall it and inference still works).

---

## Four Modes

| Mode | Description |
|------|-------------|
| 🤖 **Code** | Claude Code with local model |
| 🌐 **Browser** | Local AI controls Brave via Chrome DevTools |
| 🎤 **Voice** | Speak in, hear cloned voice out — 100% on-device |
| 📱 **Phone** | iMessage in → text/image/video out |

---

## Safety & Privacy

- Zero outbound network calls (except Claude Code startup handshake)
- LiteLLM removed after supply-chain attack concerns
- All deps re-audited
- Claude Code startup call is non-blocking and firewallable

---

## Tool-Call Reliability Fix (v2)

Local models mix XML/JSON in tool calls. Their fixes:

| Fix | Change |
|-----|--------|
| KV Cache | 4-bit → 8-bit, starts at token 1024 |
| Temperature | 0.7 → 0.2 |
| Garbled Recovery | `recover_garbled_tool_json()` function |
| Retry Logic | Up to 2 retries with explicit re-prompting |

---

## Relevance to KlickSmartAI / Dennis

**Platform limitation:** Apple Silicon only (MLX). Dennis is on Windows/WSL — not applicable directly.

**Strategic relevance:**
- Shows Claude Code can run fully local (no Anthropic API dependency)
- Qwen 3.5 122B at 65 tok/s on Apple Silicon is impressive throughput
- Browser agent mode (local AI controls Brave) is similar to Hermes Agent browser tool
- The tool-call reliability fixes (temperature, garbled recovery) are directly applicable to local LLM tool calling

**Could inspire:**
- Windows equivalent using llama.cpp + a Claude Code proxy
- The tool-call reliability patterns (KV cache, temperature, retry logic) are worth noting for local Ollama setups

---

## Related

- `entities/claude-code-guide.md` — Claude Code setup guide
- `entities/ollama.md` — Local Ollama setup
- `entities/anthropic.md` — Anthropic API / Claude
