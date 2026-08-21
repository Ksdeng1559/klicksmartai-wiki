---
title: LeadSniperAI CLI Conversion — Printing Press
created: 2026-08-05
updated: 2026-08-05
type: summary
tags: [technology, guide, how-to]
sources: [LeadSniper-3.0 repo, cli-printing-press v4.30.1]
related: [lead-sniperai-cli-os, leadsniperai-cli-prd, leadsniperai-gmb-signal-engine]
---

# LeadSniperAI CLI Conversion — Printing Press

Converted LeadSniperAI 3.0 (FastAPI backend) into an agent-native Go CLI using **CLI Printing Press v4.30.1** (mvanhorn/cli-printing-press). Verified working 2026-08-05.

## Toolchain

| Component | Version | Location |
|-----------|---------|----------|
| Go | 1.26.5 | `~/.local/go/go1.26.5/bin/go` |
| cli-printing-press | 4.30.1 | `~/go/bin/cli-printing-press` |
| Printing Press skills | latest | `~/.claude/skills/printing-press-*` |
| Generated CLI | 0.0.0-dev | `~/printing-press/library/leadsniper/` |
| CLI binary | — | `~/printing-press/library/leadsniper/build/stage/bin/leadsniper-pp-cli` |
| MCP binary | — | `~/printing-press/library/leadsniper/build/stage/bin/leadsniper-pp-mcp` |
| MCP bundle | — | `~/printing-press/library/leadsniper/build/leadsniper-pp-mcp-linux-amd64.mcpb` |

## Generation process

1. **OpenAPI spec**: imported FastAPI app → generated `/tmp/leadsniper-openapi.json` (43.8K chars, 25 endpoints)
2. **Spec fixes**: added `servers` (base_url), set `x-pp-resource: search_businesses` on `/search` (collides with reserved `search` template)
3. **Generate**: `cli-printing-press generate --spec <spec> --name leadsniper --output ~/printing-press/library/leadsniper`
4. **Quality gates passed**: go mod tidy, go test, govulncheck, go vet, go build, `--help`, `version`, `doctor` — all PASS

## Generated CLI surface

**25 API endpoints wrapped** as commands:
- `search-businesses` (Gemini GMB-grounding search — the `search` resource renamed to avoid reserved-template collision)
- `enrich`, `social-enrich`, `enrich-apify`, `enrich-tavily`, `enrich-tavily-full`
- `search-news`, `search-hiring`, `search-decision-makers`
- `seo-audit`, `generate-email`, `generate-script`, `generate-recommendations`
- `reverse-lookup`
- Batch: `upload-batch`, `import-batch` (+preview), `batches`, `batch` (status/retry/cancel/errors/leads), `enrichment-queue`

**Agent-native features (Printing Press standard):**
- `--agent` (JSON + non-interactive), `--json`, `--compact`, `--dry-run`, `--csv`
- Typed exit codes: 0/2/3/4/5/7/10
- `doctor`, `agent-context`, `which <capability>`, `version`
- **Local SQLite sync layer**: `sync`, `search`, `analytics`, `tail`, `export`, `import`
- **Self-learning loop**: `recall`, `teach`, `teach-pattern`, `teach-lookup`, `teach-playbook`, `learnings`, `playbook`
- **MCP server**: stdio + HTTP transports, bundled as `.mcpb` for Claude Desktop

## Verification (live)

| Test | Result |
|------|--------|
| `doctor` (backend down) | Correctly FAILs with API unreachable |
| Backend started (uvicorn :8000) | ✅ |
| `doctor` (backend up) | ✅ ALL OK — config, auth, API reachable |
| `search-businesses --dry-run` | ✅ Correct POST body built |
| `search-businesses` live | ✅ 500 passthrough w/ Gemini key error (placeholder key — expected) |
| `batches` live | ✅ `{"results": []}` — real API response |
| MCP binary | ✅ stdio + HTTP transport flags |
| `agent-context --agent` | ✅ Full JSON command surface (schema v4) |

## Env setup needed

```bash
export PATH="$HOME/.local/go/go1.26.5/bin:$HOME/go/bin:$PATH"
export GOPATH="$HOME/go"
# Backend env: GEMINI_API_KEY, APIFY_API_KEY, TAVILY_API_KEY (+ optional Supabase/GCP)
```

## Notes

- CLI version is `0.0.0-dev` until published to the Printing Press library
- Generated tree is reprint-safe: hand-edits go in `.printing-press-patches/`
- The `search` → `search-businesses` rename is the key spec fix for future regenerations
- Self-learning loop (`recall`/`teach`) is local-only; disable with `--no-learn` or `LEADSNIPER_NO_LEARN=true`

## Next steps

- Add real GEMINI_API_KEY + TAVILY_API_KEY to backend for full live searches
- Consider `emboss` second-pass to add compound insight commands (per CLI OS spec)
- Publish to Printing Press library (`publish` command)
- Wire into Hermes via MCP server or skills
