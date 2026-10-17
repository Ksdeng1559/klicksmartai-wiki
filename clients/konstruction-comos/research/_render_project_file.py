#!/usr/bin/env python3
"""Render the OpenSEO project file markdown from the JSON written by the prior cell."""
import json, os
from pathlib import Path

ROOT = Path("/home/denni/wiki/clients/konstruction-comos/research")
data = json.load(open(ROOT / "openseo-project-file-2026-10-17.json"))
summ = data["summary"]
csum = data["cluster_summary"]
oq = data["open_questions"]
all_kw = data["all_keywords"]
bc_kw = data["bc_only_keywords"]

def fmt_cpc(v):
    return f"${v}" if v is not None else "—"

def fmt_vol(v):
    try:
        return f"{int(v):,}"
    except Exception:
        return "—"

lines = []
lines += [
    "# OpenSEO Project File — KonstructionComOS",
    "",
    f"**Compiled:** {summ['compiled_at']} by Hermes  ",
    f"**Project ID:** {summ['konstruction_comos_project_id'] or 'TBD — to be created in OpenSEO'}  ",
    f"**Domain target:** {summ['domain_target_tbd']}  ",
    f"**Primary geo:** {summ['primary_geo']}  ",
    f"**Primary market intent:** {summ['primary_market_intent']}  ",
    "",
    "---",
    "",
    "## 1. Summary",
    "",
    f"- **Total unique keywords (after dedup):** {summ['total_keywords_deduped']}",
    f"- **BC-only (geo-filtered):** {summ['total_keywords_bc_filtered']}",
    f"- **Broad-Canada (will need re-filtering):** {summ['total_keywords_broad_canada']}",
    "",
    "⚠️ **Honest caveat:** None of the three source keyword sets were originally pulled with `location_code: 20114` (BC). The 78-keyword DataForSEO pull was country-level and bled into Ontario. The 124-term BFC commercial-intent set is country-level. The 78 OpenSEO-enriched keywords are also country-level. **A BC-only re-run ($1-5 in DataForSEO spend) is the right next step before locking pillar pages.**",
    "",
    "## 2. Source Sets",
    "",
]

for k, v in summ["sources"].items():
    lines.append(f"### {k}")
    lines.append(f"- **File:** `{v['file']}`")
    lines.append(f"- **Keywords pulled:** {v['keywords']}")
    if "issues" in v:
        lines.append(f"- **Known issues:** {v['issues']}")
    if "context" in v:
        lines.append(f"- **Context:** {v['context']}")
    lines.append("")

lines += [
    "## 3. Dedup & Scoring Method",
    "",
    f"- **Dedup:** {summ['dedup_method']}",
    f"- **Intent classification:** {summ['intent_classification']}",
    f"- **Opportunity score:** `{summ['opportunity_score_formula']}`",
    "",
    "## 4. Cluster Summary (sorted by total monthly volume)",
    "",
    "| Cluster | # Keywords | Total Vol/mo | Avg CPC | Avg Opp Score |",
    "|---|---:|---:|---:|---:|",
]

for c in csum:
    lines.append(f"| {c['cluster']} | {c['n_keywords']} | {fmt_vol(c['total_vol_mo'])} | {fmt_cpc(c['avg_cpc'])} | {c['avg_opp_score']} |")

lines += [
    "",
    "## 5. Top 30 Keywords by Opportunity Score",
    "",
    "| Keyword | Vol/mo | CPC | KD | Primary Intent | Sources | Opp Score |",
    "|---|---:|---:|---:|---|---|---:|",
]

for k in all_kw[:30]:
    srcs = ", ".join(s.split(":")[0] for s in k.get("sources", []))
    kd = k.get("keyword_difficulty")
    kd_s = str(kd) if kd is not None else "—"
    lines.append(f"| {k['keyword']} | {fmt_vol(k.get('search_volume'))} | {fmt_cpc(k.get('cpc'))} | {kd_s} | {k.get('primary_intent','?')} | {srcs} | {k['opportunity_score']} |")

lines += [
    "",
    f"## 6. BC-Filtered Keywords (markers only — {len(bc_kw)} hits)",
    "",
    "These are the only keywords with explicit BC city/region markers. **This is the highest-signal sub-list — every dollar of lead-gen spend should prioritize these once BC-only re-run lands.**",
    "",
]

if bc_kw:
    lines += [
        "| Keyword | Vol/mo | CPC | KD | Sources | Opp Score |",
        "|---|---:|---:|---:|---|---:|",
    ]
    for k in bc_kw:
        srcs = ", ".join(s.split(":")[0] for s in k.get("sources", []))
        kd = k.get("keyword_difficulty")
        kd_s = str(kd) if kd is not None else "—"
        lines.append(f"| {k['keyword']} | {fmt_vol(k.get('search_volume'))} | {fmt_cpc(k.get('cpc'))} | {kd_s} | {srcs} | {k['opportunity_score']} |")
    lines.append("")
else:
    lines.append("_No BC-marker keywords in the deduped set. Re-run DataForSEO with `location_code: 20114` to fill this gap._")
    lines.append("")

lines += [
    "## 7. Recommended Next Steps (OpenSEO Workstream)",
    "",
    "1. **Create the OpenSEO project:** `konstruction-comos` does not yet appear in the 3-project list (veritas, gpcdevelopment, default). Once brand/domain finalized, run `create_project` via the OpenSEO MCP. Project file = `openseo-project-file-2026-10-17.json` (this file).",
    "2. **BC-only re-run:** Approve $1-5 DataForSEO spend to pull 100-150 BC-only commercial mortgage keywords using `location_code: 20114`, then merge into this project file.",
    "3. **Pillar page targets** (mapped from highest-opp-score broad-CA terms until BC re-run lands):",
    "   - `/commercial-mortgage-bc` (head term — placeholder until BC re-run returns true commercial-mortgage volume)",
    "   - `/business-loans-canada` (per BFC strategy doc, 14k+ vol, $46 CPC)",
    "   - `/unsecured-business-loans` (4.2k vol, $60 CPC)",
    "   - `/working-capital-loans` (660 vol, $159 CPC — highest CPC band)",
    "   - `/bdc-vs-private-lender` (comparison play)",
    "4. **Geographic overlays:** Once BC re-run lands, generate `/commercial-mortgage-vancouver`, `/commercial-mortgage-surrey`, etc. from the BC set.",
    "5. **Defer tariff cluster:** Tariff terms (22 from BFC) are event-spike triggered, not a pillar. Re-evaluate after first BC-only commercial mortgage set lands.",
    "",
    "## 8. Open Questions / Blockers",
    "",
]

for q in oq:
    lines.append(f"- {q}")

lines += [
    "",
    "## 9. File Inventory",
    "",
    "| Path | Purpose |",
    "|---|---|",
    "| `openseo-project-file-2026-10-17.json` | Machine-readable project file (267 keywords + scoring) |",
    "| `openseo-project-file-2026-10-17.md` | This summary |",
    "| `keyword-research-2026-10-17.json` | Source 1: 78-keyword DataForSEO pull (broad-CA, needs BC re-run) |",
    "| `keyword-research-2026-10-17.md` | Source 1: human-readable |",
    "| `../../../mortgagesbydenniseng/research/tariff-loan-batch/consolidated_keyword_set.json` | Source 2: 124-term BFC commercial-intent (broad-CA) |",
    "| `../../../mortgagesbydenniseng/research/tariff-loan-batch/KEYWORD_STRATEGY.md` | Source 2: human-readable strategy |",
    "| `../../../mortgagesbydenniseng/research/openseo-enrichment/raw_keyword_metrics.json` | Source 3: 78 OpenSEO-enriched commercial keywords (KD + intent) |",
    "",
    "## 10. To Push to OpenSEO",
    "",
    "Once the project is created in OpenSEO, the `openseo-project-file-2026-10-17.json` payload is ready to upload via the OpenSEO MCP `bulk_add_keywords` tool. The top-30 in §5 are the first candidates for ranking/pillar planning; the BC-filtered 9 in §6 are the highest-priority once re-confirmed with `location_code: 20114`.",
    "",
]

out = ROOT / "openseo-project-file-2026-10-17.md"
out.write_text("\n".join(lines))
print(f"wrote {out} ({os.path.getsize(out)} bytes)")
print(f"lines: {len(lines)}")
