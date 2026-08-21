---
title: Brave Search MCP Server
type: entity
category: tool
url: https://github.com/brave/brave-search-mcp-server
pricing: free
status: active
wired_to: hermes
mcp_server: brave-search
mcp_tools: [brave_web_search, brave_local_search]
tags: [entity, brave-search, mcp, search-api, web-search, image-search, video-search, news-search, typescript, node-js]
related: [mcp, native-mcp, mcporter]
last_reviewed: 2026-04-19
---

# Brave Search MCP Server

MCP server that integrates the **Brave Search API** into any MCP-compatible AI agent. Provides web search, local search, image search, video search, news search, and AI summarization.

**Stars:** 913 | **Forks:** 148 | **Language:** TypeScript (Node.js 22+)
**Transport:** STDIO (default) or HTTP | **License:** MIT

---

## Tools (6)

### `brave_web_search`
Comprehensive web search with rich result types and advanced filtering.
- **Key params:** `query` (max 400 chars), `country`, `search_lang`, `count` (1-20), `offset` (max 9), `safesearch`, `freshness` (`pd`/`pw`/`pm`/`py`), `text_decorations`, `spellcheck`, `result_filter`, `goggles`, `units`, `extra_snippets`, `summary`
- **Summary mode:** Set `summary: true` → returns a `summary` key → pass to `brave_summarizer` for AI-grounded answer

### `brave_local_search`
Local businesses and places with ratings, hours, AI-generated descriptions.
- Same params as web search + automatic location filtering
- **Note:** Requires Pro plan for full capabilities. Falls back to web search otherwise.

### `brave_video_search`
Video search with thumbnails and comprehensive metadata.
- **Key params:** `query` (max 400 chars), `count` (1-50, default 20), `offset` (max 9), `safesearch`, `spellcheck`, `freshness`

### `brave_image_search`
Image search. **v2.x change:** No longer returns base64 (was slow and consumed context). Returns URL objects similar to Brave API response.
- **Key params:** `query`, `country`, `search_lang`, `count` (1-200, default 50), `safesearch`, `spellcheck`

### `brave_news_search`
News search with freshness controls and breaking news indicators.
- **Key params:** `query`, `country`, `search_lang`, `count` (1-50), `offset`, `safesearch`, `freshness` (default: `pd`), `extra_snippets`, `goggles`
- **Note:** Default freshness is last 24 hours (`pd`)

### `brave_summarizer`
Generates AI-powered summaries from web search results.
- **Params:** `key` (required — from `brave_web_search` summary), `entity_info`, `inline_references`
- **Usage:** First run `brave_web_search` with `summary: true`, then pass the returned `summary` key here.

---

## Configuration

### Environment Variables

| Variable | Default | Notes |
|----------|---------|-------|
| `BRAVE_API_KEY` | **required** | From api-dashboard.search.brave.com |
| `BRAVE_MCP_TRANSPORT` | `stdio` | `stdio` or `http` |
| `BRAVE_MCP_PORT` | `8080` | HTTP port |
| `BRAVE_MCP_HOST` | `0.0.0.0` | HTTP host |
| `BRAVE_MCP_LOG_LEVEL` | `info` | debug/info/notice/warning/error/critical/alert/emergency |
| `BRAVE_MCP_ENABLED_TOOLS` | all | Whitelist — only these tools enabled |
| `BRAVE_MCP_DISABLED_TOOLS` | none | Blacklist — these tools disabled |
| `BRAVE_MCP_STATELESS` | `true` | Set `true` on Amazon Bedrock Agentcore |

### CLI Options
```
node dist/index.js [options]
  --brave-api-key <string>    API key
  --transport <stdio|http>    Default: stdio
  --port <number>             Default: 8080
  --host <string>             Default: 0.0.0.0
  --logging-level <string>     Default: info
  --enabled-tools              Whitelist
  --disabled-tools             Blacklist
  --stateless <boolean>       HTTP stateless mode
```

---

## Installation Methods

### Smithery (auto-install)
```bash
npx -y @smithery/cli install brave
```

### Docker (Claude Desktop)
```json
{
  "mcpServers": {
    "brave-search": {
      "command": "docker",
      "args": ["run", "-i", "--rm", "-e", "BRAVE_API_KEY", "docker.io/mcp/brave-search"],
      "env": { "BRAVE_API_KEY": "YOUR_API_KEY_HERE" }
    }
  }
}
```

### NPX (Claude Desktop)
```json
{
  "mcpServers": {
    "brave-search": {
      "command": "npx",
      "args": ["-y", "@brave/brave-search-mcp-server", "--transport", "http"],
      "env": { "BRAVE_API_KEY": "YOUR_API_KEY_HERE" }
    }
  }
}
```

### VS Code — one-click install buttons available in README

### Local Build
```bash
git clone https://github.com/brave/brave-search-mcp-server.git
cd brave-search-mcp-server
npm install
npm run build
```

---

## API Key

1. Sign up at https://brave.com/search/api/
2. Choose plan:
   - **Search** — complete search results (URLs, text, news, images) + LLM context optimized for AI
   - **Answers** — summarized, completed answers grounded on search results
3. Generate key at https://api-dashboard.search.brave.com/app/keys

---

## For KlickSmartAI / Hermes

Dennis uses **DuckDuckGo** for web searches (per preference). Brave Search is a privacy-respecting alternative with a full MCP integration. Relevant if:
- Dennis wants an MCP-native search tool instead of the DuckDuckGo skill
- HUBERT-X or Klick2Client OS needs web search grounding
- Claude Code agents need search capability with image/video/news sub-types
- Alternative to the existing `duckduckgo-search` skill

**Key differentiator vs DuckDuckGo:** Brave has dedicated image, video, news, and local search tools — DuckDuckGo is text-only.

---

## Source

- https://github.com/brave/brave-search-mcp-server
- Stars: 913 | Forks: 148
- MIT License
