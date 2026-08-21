# MCP Tool Routing — Hermes vs. Claude Desktop

**Date:** 2026-04-20
**Source:** experiential discovery during Insurance Direct Canada topical authority research

## Key Finding

`mcporter list` only shows servers from **Claude Desktop config** (`~/.claude.json`, `~/.claude/mcp.json`).
It does NOT show servers registered in **Hermes config** (`~/.hermes/config.yaml`).

**Result:** Calling `mcporter call exa.web_search_advanced_exa` fails with `Unknown MCP server 'exa'` — even though exa is fully wired and available.

## Correct Routing

| Server | mcporter | Native Hermes Tool |
|--------|----------|-------------------|
| yt-dlp | `mcporter call yt-dlp.youtube_search` | — |
| Serper | `mcporter call serper.google_search` | — |
| Brave | `mcporter call brave.web_search` | — |
| **Exa** | ✗ fails | **`mcp_exa_deep_search_exa`** |
| **Tavily** | ✗ fails | **`web_search`** (hermes_tools) |
| **DataForSEO** | ✗ fails | **`mcp_dataforseo_*`** |

## Verification
```bash
npx --yes mcporter list 2>&1 | grep -v "CMD.EXE\|UNC\|Defaulting"
```

## Common Errors Fixed
- `Unknown MCP server 'exa'` → use `mcp_exa_*` native tool
- `Unknown MCP server 'tavily'` → use `web_search` or check native Tavily tools
- `Invalid request parameters` on yt-dlp → mcporter needs proper handshake, use mcporter not direct stdio
- `Search query and region code and language are required` → Serper needs `num_results=N` param
