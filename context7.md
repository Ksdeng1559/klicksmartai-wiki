---
title: Context7 - Upstash Real-Time Library Docs for LLMs
created: 2026-06-10
updated: 2026-06-10
type: concept
tags: [technology, how-to, guide, research]
sources: [https://github.com/upstash/context7]
---

# Context7

Up-to-date, version-specific code documentation delivered straight into LLM prompts. Built by Upstash. Replaces the "hallucinated API" problem when models generate code from stale training data.

**Repository:** https://github.com/upstash/context7
**License:** MIT
**Latest release:** `ctx7@0.5.1` (2026-06-05) | 83 total releases
**Stars:** 57,103 | Forks: 2,697 | Contributors: 120
**Primary language:** TypeScript (92.4%)

## Why It Exists

Without Context7:
- Code examples are outdated (year-old training data)
- LLMs hallucinate APIs that don't exist
- Generic answers for old package versions

With Context7:
- Fetches live docs and code examples into the prompt
- No tab-switching, no hallucinated APIs, no stale code

## Trigger Phrases

Add any of these to a prompt to fetch live docs:

```
Create a Next.js middleware that checks for a valid JWT... use context7
Configure a Cloudflare Worker script to cache JSON... use context7
Show me the Supabase auth API for email/password sign-up.
```

Skip the matching step with explicit library IDs:

```
Implement basic authentication with Supabase. use library /supabase/supabase for API and docs.
```

## Operating Modes

1. **CLI + Skills** — installs a `ctx7` CLI; agent fetches docs via shell commands (no MCP required)
2. **MCP** — registers a Context7 MCP server; agent calls doc tools natively

## Installation (One-Command)

```bash
npx ctx7 setup
```

What it does:
- OAuth authentication
- Generates an API key (saved to https://context7.com/dashboard)
- Installs the appropriate skill
- Choose between CLI+Skills or MCP mode
- Flags: `--cursor`, `--claude`, `--opencode` to target a specific agent

Uninstall:

```bash
npx ctx7 remove
npm uninstall -g ctx7   # if globally installed
```

## Requirements

- Node.js 18+
- Free API key from https://context7.com/dashboard (recommended for higher rate limits)

## Manual Configuration

- **Server URL:** `https://mcp.context7.com/mcp`
- **API key header:** `CONTEXT7_API_KEY`
- See https://context7.com/docs/resources/all-clients for 30+ client setups

For Hermes Agent specifically:
- Add the MCP server via `hermes mcp add context7 --url https://mcp.context7.com/mcp`
- Or set the API key in `~/.hermes/.env`: `CONTEXT7_API_KEY=***
- See [[hermes-agent-mcp]] for general MCP setup

## Available Tools

### CLI commands

| Command | Description |
|---|---|
| `ctx7 library <name>` | Searches Context7 index by library name; returns matching IDs |
| `ctx7 docs <libraryId>` | Retrieves documentation (e.g., `/mongodb/docs`, `/vercel/next.js`) |

### MCP tools

**`resolve-library-id`** — Resolves a general library name into a Context7 library ID
- `query` (required): the user's question/task — used to rank results
- `libraryName` (required): name of the library to search for

**`query-docs`** — Retrieves docs for a library using a Context7 library ID
- `libraryId` (required): exact Context7 ID (e.g., `/mongodb/docs`)
- `query` (required): the question or task

## Auto-Trigger Rule

Add to your agent's config so Context7 activates automatically for library/API questions:

- **Cursor:** `Cursor Settings > Rules`
- **Claude Code:** `CLAUDE.md`

Example rule:

```
Always use Context7 when I need library/API documentation, code generation,
setup or configuration steps without me having to explicitly ask.
```

For Hermes Agent, this would go in `~/.hermes/AGENTS.md` or `~/.hermes/CLAUDE.md`.

## Packages

| Package | Purpose |
|---|---|
| [`@upstash/context7-mcp`](https://www.npmjs.com/package/@upstash/context7-mcp) | MCP server |
| [`ctx7`](https://www.npmjs.com/package/ctx7) | CLI |
| [`@upstash/context7-sdk`](https://www.npmjs.com/package/@upstash/context7-sdk) | TypeScript SDK |
| [`@upstash/context7-tools-ai-sdk`](https://www.npmjs.com/package/@upstash/context7-tools-ai-sdk) | Vercel AI SDK tools |
| [`@upstash/context7-pi`](https://www.npmjs.com/package/@upstash/context7-pi) | pi.dev extension |

## Related

- [[hermes-agent]] — local Hermes Agent setup
- [[hermes-agent-mcp]] — connecting Hermes to MCP servers
- [[hermes-skills-hub]] — full list of Hermes skills (exa's search/tavily are similar)
- [[exa]] — competing semantic search backend (already configured)
- [[tavily]] — competing AI search backend (already configured)

## References

- [GitHub](https://github.com/upstash/context7)
- [CLI Reference](https://context7.com/docs/clients/cli)
- [MCP Clients](https://context7.com/docs/resources/all-clients)
- [Adding Libraries](https://context7.com/docs/adding-libraries)
- [Troubleshooting](https://context7.com/docs/resources/troubleshooting)
- [REST API](https://context7.com/docs/api-guide)
- [Run Locally](https://context7.com/docs/resources/developer)
