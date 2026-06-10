import json
from pathlib import Path

BASE = Path(__file__).parent
ROOT = BASE.parent

import graphify.build as gbuild
import graphify.cluster as gcluster
import graphify.analyze as ganalyze
import graphify.export as gexport
import graphify.report as greport

# Load merged graph
graph_data = json.loads((BASE / "graph.json").read_text(encoding="utf-8"))

# Build networkx graph from extractions list format
extractions = [graph_data]
G = gbuild.build(extractions)
print(f"Graph: {G.number_of_nodes()} nodes, {G.number_of_edges()} edges")

# Cluster
communities = gcluster.cluster(G)
print(f"Communities: {len(communities)}")

# Analyze
god_nodes = ganalyze.god_nodes(G)
surprises = ganalyze.surprising_connections(G, communities)
print(f"God nodes: {len(god_nodes)}, Surprises: {len(surprises)}")

# Community labels (simple auto-label from top node in each community)
community_labels = {}
for cid, members in communities.items():
    if members:
        # Use first member's label from graph
        n = members[0]
        label = G.nodes[n].get("label", n) if n in G.nodes else n
        community_labels[cid] = label

# Cohesion scores (simple: 1.0 for all)
cohesion_scores = {cid: 1.0 for cid in communities}

# Export HTML
html_path = str(BASE / "graph.html")
gexport.to_html(G, communities, html_path, community_labels=community_labels)
print(f"HTML written: {html_path}")

# Generate GRAPH_REPORT.md
try:
    detect_result = json.loads((BASE / ".graphify_detect.json").read_text(encoding="utf-8"))
    token_cost = {"input": 0, "output": 0}
    report_md = greport.generate(
        G, communities, cohesion_scores, community_labels,
        god_nodes, surprises, detect_result, token_cost,
        root=str(ROOT)
    )
    (BASE / "GRAPH_REPORT.md").write_text(report_md, encoding="utf-8")
    print(f"GRAPH_REPORT.md written ({len(report_md)} chars)")
except Exception as e:
    print(f"Report generation warning: {e}")

# Export graph.json (GraphRAG-ready)
gexport.to_json(G, communities, str(BASE / "graph.json"))
print("graph.json updated")

print("\nDone. Outputs in:", BASE)
