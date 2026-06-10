import json
from pathlib import Path

BASE = Path(__file__).parent

# Cache new results
try:
    from graphify.cache import save_semantic_cache
    new = json.loads((BASE / ".graphify_semantic_new.json").read_text(encoding="utf-8"))
    saved = save_semantic_cache(new.get("nodes", []), new.get("edges", []), new.get("hyperedges", []))
    print(f"Cached {saved} files")
except Exception as e:
    print(f"Cache save warning: {e}")

# Merge cached + new
cached_path = BASE / ".graphify_cached.json"
new_path = BASE / ".graphify_semantic_new.json"

cached = json.loads(cached_path.read_text(encoding="utf-8")) if cached_path.exists() else {"nodes": [], "edges": [], "hyperedges": []}
new = json.loads(new_path.read_text(encoding="utf-8")) if new_path.exists() else {"nodes": [], "edges": [], "hyperedges": []}

all_nodes = cached["nodes"] + new.get("nodes", [])
all_edges = cached["edges"] + new.get("edges", [])
all_hyperedges = cached.get("hyperedges", []) + new.get("hyperedges", [])

seen = set()
deduped = []
for n in all_nodes:
    if n["id"] not in seen:
        seen.add(n["id"])
        deduped.append(n)

merged = {
    "nodes": deduped,
    "edges": all_edges,
    "hyperedges": all_hyperedges,
    "input_tokens": new.get("input_tokens", 0),
    "output_tokens": new.get("output_tokens", 0),
}
(BASE / ".graphify_semantic.json").write_text(json.dumps(merged, indent=2), encoding="utf-8")
print(f"Merged: {len(deduped)} nodes, {len(all_edges)} edges, {len(all_hyperedges)} hyperedges")
