import json
from pathlib import Path

BASE = Path(__file__).parent
ROOT = BASE.parent

# Load existing semantic + new chunk
semantic_path = BASE / ".graphify_semantic.json"
chunk2_path = BASE / ".graphify_chunk_02.json"

existing = json.loads(semantic_path.read_text(encoding="utf-8")) if semantic_path.exists() else {"nodes": [], "edges": [], "hyperedges": []}
chunk2 = json.loads(chunk2_path.read_text(encoding="utf-8"))

all_nodes = existing["nodes"] + chunk2.get("nodes", [])
all_edges = existing["edges"] + chunk2.get("edges", [])
all_hyperedges = existing.get("hyperedges", []) + chunk2.get("hyperedges", [])

# Deduplicate nodes by id
seen = set()
deduped = []
for n in all_nodes:
    if n["id"] not in seen:
        seen.add(n["id"])
        deduped.append(n)

merged = {"nodes": deduped, "edges": all_edges, "hyperedges": all_hyperedges}
semantic_path.write_text(json.dumps(merged, indent=2), encoding="utf-8")
print(f"Merged semantic: {len(deduped)} nodes, {len(all_edges)} edges, {len(all_hyperedges)} hyperedges")

# Rebuild graph
import graphify.build as gbuild
import graphify.cluster as gcluster
import graphify.analyze as ganalyze
import graphify.export as gexport
import graphify.report as greport

G = gbuild.build([merged])
print(f"Graph: {G.number_of_nodes()} nodes, {G.number_of_edges()} edges")

communities = gcluster.cluster(G)
print(f"Communities: {len(communities)}")

god_nodes = ganalyze.god_nodes(G)
surprises = ganalyze.surprising_connections(G, communities)

community_labels = {}
for cid, members in communities.items():
    if members:
        n = members[0]
        label = G.nodes[n].get("label", n) if n in G.nodes else n
        community_labels[cid] = label

cohesion_scores = {cid: 1.0 for cid in communities}

# HTML
gexport.to_html(G, communities, str(BASE / "graph.html"), community_labels=community_labels)
print(f"graph.html updated")

# GraphRAG JSON
gexport.to_json(G, communities, str(BASE / "graph.json"))
print("graph.json updated")

# Report
try:
    detect_result = json.loads((BASE / ".graphify_detect.json").read_text(encoding="utf-8"))
    token_cost = {"input": 0, "output": 0}
    report_md = greport.generate(
        G, communities, cohesion_scores, community_labels,
        god_nodes, surprises, detect_result, token_cost,
        root=str(ROOT)
    )
    (BASE / "GRAPH_REPORT.md").write_text(report_md, encoding="utf-8")
    print(f"GRAPH_REPORT.md updated ({len(report_md)} chars)")
except Exception as e:
    print(f"Report warning: {e}")

print("\nDone.")
