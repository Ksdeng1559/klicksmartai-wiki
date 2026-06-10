import json
from pathlib import Path

BASE = Path(__file__).parent

chunk = BASE / ".graphify_chunk_01.json"
if chunk.exists():
    data = json.loads(chunk.read_text(encoding="utf-8"))
    nn = len(data.get("nodes", []))
    ne = len(data.get("edges", []))
    nh = len(data.get("hyperedges", []))
    print(f"Chunk 1: {nn} nodes, {ne} edges, {nh} hyperedges")
    (BASE / ".graphify_semantic_new.json").write_text(json.dumps(data), encoding="utf-8")
    print("Written to semantic_new.json")
else:
    print("ERROR: chunk file missing")
