---
name: brain-graph
description: Navigate the Avada Product Training knowledge graph, find connected concepts, shortest paths, hubs and affected notes. Use when the user asks how topics connect, wants a graph/path between ideas, asks for god nodes, or wants to browse the Graphify output. Do not use when a direct source file already answers the question.
---

# Brain Graph

Graph artifacts are bundled in `${CLAUDE_PLUGIN_ROOT}/knowledge/graph/`:

- `graph.json` — nodes and edges;
- `GRAPH_REPORT.md` — corpus summary and hubs;
- `graph.html` — interactive visualization;
- `manifest.json` — source hashes.

## Procedure

1. Run the bundled query script first; it returns a compact path instead of loading the full graph:

```bash
python "${CLAUDE_PLUGIN_ROOT}/scripts/query_graph.py" path "A" "B"
python "${CLAUDE_PLUGIN_ROOT}/scripts/query_graph.py" neighbors "A"
python "${CLAUDE_PLUGIN_ROOT}/scripts/query_graph.py" god-nodes --top 10
```

2. Read `GRAPH_REPORT.md` for broader hub/community context only when needed.
3. If `graphify` CLI is installed, its optional equivalents are:

```bash
graphify path "A" "B" --graph "${CLAUDE_PLUGIN_ROOT}/knowledge/graph/graph.json" --undirected
graphify explain "A" --graph "${CLAUDE_PLUGIN_ROOT}/knowledge/graph/graph.json"
graphify god-nodes --graph "${CLAUDE_PLUGIN_ROOT}/knowledge/graph/graph.json" --top 10
```

4. Read the actual Markdown notes on the returned path before explaining the relationship.
5. Distinguish edge type:
   - `wikilink` — extracted from source notes;
   - `curated` — deliberate cross-domain teaching connection;
   - `domain` — navigation edge to a domain hub.

## Boundaries

The graph is a retrieval map, not doctrine. An edge does not prove a causal relationship. Source notes remain authoritative.

## Output

- Path or neighbor list.
- Edge types.
- Plain-language explanation.
- Source files to read.
- Evidence limitation.
