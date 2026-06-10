import json
from pathlib import Path

BASE = Path(__file__).parent
ROOT = BASE.parent

# Load AST (empty for doc-only corpus) + semantic
ast = {"nodes": [], "edges": []}
ast_path = BASE / ".graphify_ast.json"
if ast_path.exists():
    ast = json.loads(ast_path.read_text(encoding="utf-8"))

semantic_path = BASE / ".graphify_semantic.json"
semantic = json.loads(semantic_path.read_text(encoding="utf-8"))

# Merge
all_nodes = ast["nodes"] + semantic["nodes"]
all_edges = ast["edges"] + semantic["edges"]
all_hyperedges = semantic.get("hyperedges", [])

# Deduplicate nodes
seen = set()
deduped_nodes = []
for n in all_nodes:
    if n["id"] not in seen:
        seen.add(n["id"])
        deduped_nodes.append(n)

graph = {
    "nodes": deduped_nodes,
    "edges": all_edges,
    "hyperedges": all_hyperedges,
}

# Save graph.json (GraphRAG-ready)
(BASE / "graph.json").write_text(json.dumps(graph, indent=2), encoding="utf-8")
print(f"graph.json: {len(deduped_nodes)} nodes, {len(all_edges)} edges")

# Build via graphify library
try:
    from graphify.build import build
    result = build(graph, output_dir=str(BASE), root=str(ROOT))
    print(f"Build result: {result}")
except Exception as e:
    print(f"Build error: {e}")
    # Try alternate API
    try:
        from graphify.graph import GraphBuilder
        gb = GraphBuilder(graph)
        gb.cluster()
        gb.save(str(BASE / "graph.json"))
        print("Saved via GraphBuilder")
    except Exception as e2:
        print(f"GraphBuilder error: {e2}")
