#!/usr/bin/env python3
"""Build a deterministic knowledge graph from Markdown wikilinks and curated cross-links."""
from __future__ import annotations

import argparse
import hashlib
import html
import json
import re
from collections import Counter, defaultdict
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
KNOWLEDGE = ROOT / "plugins" / "avada-product-training" / "knowledge"
OUT = ROOT / "graphify-out"
PLUGIN_GRAPH = KNOWLEDGE / "graph"
WIKILINK = re.compile(r"\[\[([^\]|#]+)")
H1 = re.compile(r"^#\s+(.+)$", re.M)
SLUG = re.compile(r"[^a-z0-9]+")

COMMUNITY = {
    "principles": (0, "Principles", "#FA5252"),
    "progress": (1, "Progress + feedback", "#228BE6"),
    "sessions": (2, "Sessions + cases", "#15AABF"),
    "cases": (2, "Sessions + cases", "#15AABF"),
    "chase": (3, "Chase ecommerce", "#F59F00"),
    "interloka": (4, "Interloka strategy", "#7950F2"),
    "sources": (5, "Sources + learning resources", "#12B886"),
    "templates": (6, "Product argument", "#E64980"),
    "root": (7, "Avada course doctrine", "#343A40"),
}

CROSS_LINKS = [
    ("00-index.md", "course-map.md"),
    ("00-index.md", "product-operator-method.md"),
    ("00-index.md", "interactive-training.md"),
    ("00-index.md", "sources/source-map.md"),
    ("00-index.md", "sources/learning-resources.md"),
    ("00-index.md", "chase/sources/Source index.md"),
    ("00-index.md", "interloka/knowledge/framework-map.md"),
    ("product-operator-method.md", "templates/product-argument.md"),
    ("product-operator-method.md", "chase/concepts/Metric diagnosis tree.md"),
    ("product-operator-method.md", "chase/concepts/Offer economics.md"),
    ("product-operator-method.md", "interloka/knowledge/business-model-in-one-page.md"),
    ("interactive-training.md", "sources/learning-resources.md"),
    ("interactive-training.md", "principles/artifact-and-correction.md"),
    ("interactive-training.md", "principles/contrast-prevents-bias.md"),
    ("cases/2026-10-27-team-bloom.md", "chase/sources/Chase Chappell - Bloom 17M TikTok Shop Strategy.md"),
    ("cases/2026-10-27-team-bloom.md", "chase/brands/Brand atlas.md"),
    ("sessions/2026-10-27-session-3-recap.md", "cases/2026-10-27-team-bloom.md"),
    ("sessions/2026-10-27-session-3-recap.md", "progress/2026-10-27-learner-feedback-reflection.md"),
    ("sessions/2026-10-27-session-3-recap.md", "progress/2026-10-27-three-session-progress.md"),
]


def node_id(rel: str) -> str:
    return "note_" + SLUG.sub("_", rel.casefold()).strip("_")


def title(path: Path) -> str:
    text = path.read_text(encoding="utf-8", errors="ignore")
    match = H1.search(text)
    return match.group(1).strip() if match else path.stem


def community_for(rel: str):
    first = rel.split("/", 1)[0] if "/" in rel else "root"
    return COMMUNITY.get(first, COMMUNITY["root"])


def knowledge_paths():
    return sorted(
        path for path in KNOWLEDGE.rglob("*.md")
        if path.relative_to(KNOWLEDGE).parts[0] != "graph"
    )


def resolve_target(source_rel: str, raw: str, files: dict[str, Path], stems: dict[str, list[str]]):
    target = raw.strip().replace("\\", "/")
    if target.endswith(".md"):
        target = target[:-3]
    candidates = [target, target + ".md"]
    source_parent = Path(source_rel).parent
    for candidate in candidates:
        normalized = str(Path(candidate)).replace("\\", "/")
        if normalized in files:
            return normalized
        local = str(source_parent / normalized).replace("\\", "/")
        if local in files:
            return local
    stem = Path(target).name.casefold()
    matches = stems.get(stem, [])
    if len(matches) == 1:
        return matches[0]
    if matches:
        same_domain = [m for m in matches if m.split("/", 1)[0] == source_rel.split("/", 1)[0]]
        if len(same_domain) == 1:
            return same_domain[0]
    return None


def build():
    paths = knowledge_paths()
    files = {p.relative_to(KNOWLEDGE).as_posix(): p for p in paths}
    stems = defaultdict(list)
    for rel, path in files.items():
        stems[path.stem.casefold()].append(rel)

    nodes = []
    for rel, path in files.items():
        cid, cname, color = community_for(rel)
        nodes.append({
            "id": node_id(rel),
            "label": title(path),
            "source_file": rel,
            "community": cid,
            "community_name": cname,
            "color": color,
        })

    edge_map = {}
    unresolved = defaultdict(set)

    def add_edge(left, right, relation, source_file):
        if left == right or left not in files or right not in files:
            return
        a, b = sorted((left, right), key=str.casefold)
        key = (a, b, relation)
        edge_map.setdefault(key, {
            "source": node_id(a),
            "target": node_id(b),
            "relation": relation,
            "confidence": "EXTRACTED" if relation == "wikilink" else "CURATED",
            "source_file": source_file,
        })

    for rel, path in files.items():
        text = path.read_text(encoding="utf-8", errors="ignore")
        for raw in WIKILINK.findall(text):
            target = resolve_target(rel, raw, files, stems)
            if target:
                add_edge(rel, target, "wikilink", rel)
            else:
                unresolved[rel].add(raw.strip())

    for left, right in CROSS_LINKS:
        add_edge(left, right, "curated", "scripts/rebuild-graph.py")

    # Structural links make every domain navigable even when imported notes use few wikilinks.
    hubs = {
        "chase": "chase/sources/Source index.md",
        "interloka": "interloka/knowledge/00-index.md",
        "progress": "progress/2026-10-27-three-session-progress.md",
        "sessions": "sessions/2026-10-27-session-3-recap.md",
        "cases": "cases/2026-10-27-team-bloom.md",
        "principles": "00-index.md",
        "sources": "sources/source-map.md",
        "templates": "templates/product-argument.md",
        "root": "00-index.md",
    }
    for rel in files:
        domain = rel.split("/", 1)[0] if "/" in rel else "root"
        hub = hubs.get(domain, "00-index.md")
        if rel != hub:
            add_edge(rel, hub, "domain", "scripts/rebuild-graph.py")

    links = list(edge_map.values())
    return {"directed": False, "multigraph": False, "graph": {}, "nodes": nodes, "links": links}, unresolved


def write_outputs(graph, unresolved):
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "graph.json").write_text(json.dumps(graph, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    manifest = {}
    for path in knowledge_paths():
        rel = path.relative_to(KNOWLEDGE).as_posix()
        digest = hashlib.sha256(path.read_bytes()).hexdigest()
        manifest[rel] = {"sha256": digest, "bytes": path.stat().st_size}
    (OUT / "manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    degree = Counter()
    labels = {n["id"]: n["label"] for n in graph["nodes"]}
    communities = defaultdict(list)
    for n in graph["nodes"]:
        communities[(n["community"], n["community_name"])].append(n["label"])
    for edge in graph["links"]:
        degree[edge["source"]] += 1
        degree[edge["target"]] += 1

    lines = [
        f"# Graph report — Avada Product Training Brain ({date.today().isoformat()})",
        "",
        f"- {len(graph['nodes'])} nodes",
        f"- {len(graph['links'])} edges",
        f"- {len(communities)} communities",
        f"- {sum(len(v) for v in unresolved.values())} unresolved wikilinks",
        "- Edge types: extracted wikilinks, curated cross-domain links, deterministic domain links",
        "",
        "## Most connected nodes",
        "",
    ]
    for i, (nid, count) in enumerate(degree.most_common(15), 1):
        lines.append(f"{i}. `{labels[nid]}` — {count} edges")
    lines.extend(["", "## Communities", ""])
    for (_, name), members in sorted(communities.items()):
        lines.append(f"### {name} ({len(members)})")
        lines.append(", ".join(sorted(members, key=str.casefold)[:12]) + (" …" if len(members) > 12 else ""))
        lines.append("")
    if unresolved:
        lines.extend(["## Unresolved wikilinks", ""])
        for rel, targets in sorted(unresolved.items()):
            lines.append(f"- `{rel}`: " + ", ".join(sorted(targets)))
    (OUT / "GRAPH_REPORT.md").write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")

    payload = json.dumps(graph, ensure_ascii=False)
    html_doc = f"""<!doctype html>
<html><head><meta charset='utf-8'><title>Avada Product Training Brain Graph</title>
<script src='https://unpkg.com/vis-network/standalone/umd/vis-network.min.js'></script>
<style>html,body,#graph{{width:100%;height:100%;margin:0;background:#161616;color:#fff;font-family:Inter,Arial}}#meta{{position:fixed;z-index:2;top:12px;left:12px;background:#242424dd;padding:12px 16px;border-radius:10px}}#graph{{position:absolute}}small{{color:#aaa}}</style></head>
<body><div id='meta'><b>Avada Product Training Brain</b><br><small>{len(graph['nodes'])} nodes · {len(graph['links'])} edges · search/drag/zoom</small></div><div id='graph'></div>
<script>const G={payload};const nodes=new vis.DataSet(G.nodes.map(n=>({{id:n.id,label:n.label,title:n.source_file+'\n'+n.community_name,color:n.color}})));const edges=new vis.DataSet(G.links.map(e=>({{from:e.source,to:e.target,title:e.relation,width:e.relation==='curated'?3:1,color:{{opacity:e.relation==='domain'?0.18:0.55}}}})));new vis.Network(document.getElementById('graph'),{{nodes,edges}},{{nodes:{{shape:'dot',font:{{color:'#fff',size:14}},size:13}},edges:{{smooth:true}},physics:{{stabilization:{{iterations:300}}}},interaction:{{hover:true,navigationButtons:true}}}});</script></body></html>"""
    (OUT / "graph.html").write_text(html_doc, encoding="utf-8")

    PLUGIN_GRAPH.mkdir(parents=True, exist_ok=True)
    for name in ["graph.json", "manifest.json", "GRAPH_REPORT.md", "graph.html"]:
        (PLUGIN_GRAPH / name).write_bytes((OUT / name).read_bytes())


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--strict", action="store_true", help="fail on unresolved wikilinks")
    args = parser.parse_args()
    graph, unresolved = build()
    result = {"nodes": len(graph["nodes"]), "edges": len(graph["links"]), "unresolved": sum(len(v) for v in unresolved.values())}
    if args.strict and unresolved:
        print(json.dumps(result, ensure_ascii=False))
        for rel, targets in sorted(unresolved.items()):
            print(rel + ": " + ", ".join(sorted(targets)))
        return 1
    if not args.check:
        write_outputs(graph, unresolved)
    print(json.dumps(result, ensure_ascii=False, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
