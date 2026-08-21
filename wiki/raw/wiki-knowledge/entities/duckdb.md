# DuckDB

**What it is:** Open-source analytical database (OLAP) — embeddable, columnar-vectorized, ACID-compliant
**URL:** https://duckdb.org/
**License:** MIT (DuckDB Foundation)

---

## Key Characteristics

| Property | What It Means |
|----------|---------------|
| **Embedded** | No server process — runs inside your app. High-speed data transfer, no network latency |
| **Columnar-vectorized** | Processes batches of values at once — 10-100x faster than row-by-row DBs (PostgreSQL, MySQL, SQLite) for analytical queries |
| **Single-file database** | Data stored in one `.duckdb` file, portable |
| **No dependencies** | Two files (header + implementation), compiles with any C++11 compiler |
| **Portable** | Linux, macOS, Windows, ARM, x86 — even web browsers via DuckDB-Wasm |
| **ACID (MVCC)** | Transactional guarantees, bulk-optimized |
| **Extension mechanism** | Parquet, JSON, HTTP/S, S3 — all built as extensions |
| **MIT License** | Fully open source, no commercial restrictions |

---

## Performance

DuckDB is built for **analytical workloads (OLAP)**:
- Complex, long-running queries over large datasets
- Aggregations over entire tables, multi-table joins
- Columnar-vectorized execution = minimal CPU overhead per value

**Benchmark context:** TPC-H and TPC-DS benchmarks tested, millions of CI queries, tested across SQLite/PostgreSQL/MonetDB test suites.

**vs. traditional DBs:**
- SQLite/MySQL — row-by-row, fast for transactional writes, slow for analytics
- DuckDB — columnar-vectorized, built for analytical reads

---

## KlickSmartAI OS Placement

DuckDB sits under MotherDuck at the **data engine layer**:

```
Layer 5: Data & Analytics
├── MotherDuck MCP Server  ← connects AI agents to DuckDB
└── DuckDB Engine           ← local/embedded analytical database
    ├── WWR signal data
    ├── Client CRM data
    └── Outreach logs
```

**Self-hosted DuckDB options:**
- Embed directly in a Python/Node process (no server needed)
- DuckDB-Wasm in browser
- MotherDuck (managed cloud + MCP interface)
- Self-managed on WSL via `pip install duckdb`

DuckDB is what MotherDuck is built on top of — same engine, but MotherDuck adds the MCP server interface and hosting layer.