# OpenSEO — Glossary

| Term | Meaning |
|---|---|
| **D1** | Cloudflare's distributed SQLite-compatible database. Used as OpenSEO's primary data store in self-host mode (via miniflare). |
| **miniflare** | Local development environment for Cloudflare Workers — provides local D1, R2, KV, DO bindings that match the production runtime. |
| **PAA** | "People Also Ask" — Google SERP feature that surfaces related questions. The PAA module mines social discussion around these questions for demand-discovery. |
| **Demand discovery** | Approach to keyword research that focuses on language patterns and angles surfaced from social threads, not raw search volume. PAA itself doesn't create new demand — the value is in mining what people actually say about the questions. |
| **Dormant module** | BYO API key missing → corresponding module is hidden entirely (no sidebar, no route, no MCP tool). Distinct from "disabled". |
| **LANPubs** | `lanpublications/open-seo` — upstream fork that contributed the On-Page.ai Content Optimization module (cherry-picked 6 commits). |
| **Social proxy** | Tiny Python HTTP server (`/home/denni/bin/social-proxy.py`) that wraps rdt-cli (Reddit), V2EX public API, Bilibili search. Runs on the host; container reaches it via `host.docker.internal:9876`. |
| **rdt-cli** | Python CLI for Reddit, requires browser cookie extraction via `rdt login`. Gives high-fidelity thread content with comments. |
| **Fusion / PAA fallback** | When `gl=ca` (or AU/NZ/IE/IN/BR/MX/ZA/JP) returns 0 PAA from Serper, the client retries with `gl=us` and surfaces the `paaSourceRegion` field. Honest attribution in the report. |
| **ICM** | "Intelligent Client Manager" — the 3-layer + source-of-truth workspace template used for KlickSmartAI client projects. OpenSEO is an ICM client (Quick mode — single workspace). |
| **SOCIAL_SOURCES** | Const tuple in `src/shared/paa-mining.ts`: `["reddit", "quora", "v2ex", "bilibili"]`. Drives the source-checkboxes in the PAA UI. |
| **MAX_PAA_QUESTIONS** | 10 — cap on PAA extraction per scan. |
| **MAX_SOCIAL_THREADS_PER_QUESTION** | 3 — cap on social threads mined per question. |
| **Drizzle** | TypeScript ORM. OpenSEO uses it for D1 + Postgres schemas (dual-target). |