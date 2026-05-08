---
title: Ollama — Local LLM Runtime & API
url: https://docs.ollama.com/
pricing: Free (self-hosted), Cloud tiers available
category: ai-infrastructure
---

# Ollama

**What it is:** Local LLM runtime with a REST API, model library, and native tooling for streaming, tool calling, vision, embeddings, and web search. Runs on macOS, Windows, Linux, and Docker. Powers the local model layer in KlickSmartAI OS.

## Core Capability Table

| Capability | Details |
|-----------|---------|
| **Streaming** | Token-by-token via `/api/generate` and `/api/chat`. Default in REST API; opt-in in SDKs. |
| **Thinking models** | Qwen3, GPT-OSS, DeepSeek-R1, DeepSeek-v3.1 emit a separate `thinking` field — reasoning trace auditable or hideable independently of the answer. GPT-OSS takes `low/medium/high` trace levels. |
| **Structured Outputs** | Enforce JSON schema on responses via `format: "json"` or full schema object. Native Pydantic (Python) and Zod (JS) integration. |
| **Vision** | Accepts base64-encoded images via `images` array in chat requests. Models: gemma3, qwen3-vl, llava-family. |
| **Embeddings** | Dedicated embedding models: `embeddinggemma`, `qwen3-embedding`, `all-minilm`. L2-normalized vectors via `/api/embed`. Batch input supported. |
| **Tool Calling** | Native function calling via `tools` array in `/api/chat`. Single-shot and multi-step (accumulate thinking → call tool → re-prompt). |
| **Web Search** | Authenticated API at `https://ollama.com/api/web_search`. Returns `{results: [{title, url, content}]}`. Requires Ollama API key. Reduces hallucinations on current events. |
| **API Compatibility** | OpenAI-compatible (`/v1/chat/completions`) and Anthropic-compatible endpoints. |

## API Reference

| Endpoint | Method | Purpose |
|----------|--------|---------|
| `http://localhost:11434/api/generate` | POST | Run a single prompt |
| `http://localhost:11434/api/chat` | POST | Conversation with messages array |
| `http://localhost:11434/api/embed` | POST | Generate text embeddings |
| `http://localhost:11434/api/tags` | GET | List available models |
| `http://localhost:11434/api/ps` | GET | Show loaded models + GPU allocation |
| `https://ollama.com/api/web_search` | POST | Web search (authenticated, cloud) |
| `https://ollama.com/api` | — | Cloud model API base URL |

## Supported Model Families

| Model | Type | Notes |
|-------|------|-------|
| **qwen3** | Thinking + tool calling | Default reasoning model for KlickSmartAI local stack |
| **qwen3-vl** | Vision + thinking | Image understanding |
| **qwen3-embedding** | Embeddings | Vector generation |
| **gemma3** | Vision + tool calling | Google's model via Ollama |
| **deepseek-r1** | Thinking | Reasoner — streams thinking trace |
| **deepseek-v3.1** | Thinking | Latest DeepSeek reasoning |
| **gpt-oss** | Thinking | OpenAI-o series compatible; trace levels: low/medium/high |
| **embeddinggemma** | Embeddings | Google's embedding model |
| **all-minilm** | Embeddings | Lightweight embedding model |

## KlickSmartAI OS Relevance

| OS Layer | Role |
|---------|------|
| AI Inference Layer | Local model runtime — qwen3-vl:8b (writing), qwen2.5:3b (wiki), qwen3 (reasoning) |
| Signal Detection | Embedding models power vector similarity for ICP scoring + proximity matching |
| Outreach Engine | OpenClaw uses Ollama as the model layer |
| Enrichment | Vision models for analyzing client/referral partner content thumbnails |

## Integration Stack

```
Ollama (local) ← host.docker.internal:11434
├── OpenClaw (event router / specialist agents / outreach)
├── Hermes Agent (orchestration / cron / briefings)
├── Klick2Client OS (full GTM stack)
└── WWR v2.0 CRM (proximity scorer, pathfinder agent)
```

## Local Setup Context

- **Endpoint:** `host.docker.internal:11434` (Docker-internal host access)
- **Dennis hardware:** GTX 1660 SUPER, 16GB RAM, Ryzen 5 3600
- **Currently live models:** qwen3-vl:8b (writing), qwen2.5:3b (wiki)
- **Non-functional:** Llama-family (removed from available models)
- **Cloud API key:** Required for web search; set via `OLLAMA_API_KEY`

## Key API Usage Patterns

### Streaming with thinking detection
```python
from ollama import chat

stream = chat(model='qwen3', messages=[{'role': 'user', 'content': 'Explain X'}], think=True, stream=True)
in_thinking = False
for chunk in stream:
    if chunk.message.thinking and not in_thinking:
        in_thinking = True
        print('Thinking:\n', end='')
    elif chunk.message.content:
        if in_thinking:
            in_thinking = False
            print('\n\nAnswer:\n', end='')
        print(chunk.message.content, end='')
```

### Web search (requires API key)
```python
import ollama
response = ollama.web_search("Ollama latest release notes")
print(response['results'])
```

### Structured output with Pydantic
```python
from ollama import chat
from pydantic import BaseModel

class Country(BaseModel):
    name: str
    capital: str
    languages: list[str]

response = chat(model='gpt-oss', messages=[{'role': 'user', 'content': 'Tell me about Japan'}], format=Country.model_json_schema())
country = Country.model_validate_json(response.message.content)
```

## Sources

- Primary: https://docs.ollama.com/
- API Reference: https://docs.ollama.com/api/
- Capabilities: https://docs.ollama.com/capabilities/
- Integrations: https://docs.ollama.com/integrations/
- Cloud models: https://docs.ollama.com/cloud/
- Web Search API: https://docs.ollama.com/capabilities/web-search/
- Thinking models: https://docs.ollama.com/capabilities/thinking/
- Structured outputs: https://docs.ollama.com/capabilities/structured-outputs/