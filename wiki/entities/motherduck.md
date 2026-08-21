# MotherDuck MCP Server

**What it is:** MCP (Model Context Protocol) server that connects AI assistants directly to MotherDuck databases
**URL:** https://motherduck.com/product/mcp-server/
**Powered by:** DuckDB

## What It Does

- Connect Claude, ChatGPT, Gemini, and other AI agents to MotherDuck databases
- Natural language questions → accurate, traceable SQL queries
- Sandboxed compute (isolated, read-only by default)
- Full SQL traceability — every answer shows the exact query run
- Custom visualizations via AI native artifacts
- Iterative analysis without SQL skills required

## Key Features

| Feature | What It Means |
|---------|---------------|
| Natural language → SQL | Non-technical users ask questions, get answers |
| Sandboxed compute | Agents can't run up costs or affect other workloads |
| SQL traceability | Every query is auditable — verify logic, trust results |
| DuckDB-backed | Columnar OLAP database, fast analytical queries |
| pg_endpoint | Now speaks Postgres — broader compatibility |

## KlickSmartAI Use Case

- **WWR signal data storage** — store HNW advisor signals, portfolio data
- **Client CRM analytics** — query client data with natural language
- **GPC dashboard data** — back-end analytics layer for client websites
- **Multi-tenant data isolation** — each client has isolated sandboxed compute

## Pricing
Not public — "Start Free" button, then requires account. No public pricing on this page.

## Notes
- MCP (Model Context Protocol) is the same protocol Hermes uses for internal tool discovery
- DuckDB is the underlying engine — open source, columnar, analytical
- pg_endpoint means it now speaks Postgres wire protocol — most BI tools connect directly