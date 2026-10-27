#!/usr/bin/env python3
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PLUGIN = ROOT / "plugins" / "avada-product-training"
EXPECTED_VERSION = "0.3.1"


def load_json(path):
    return json.loads(path.read_text(encoding="utf-8"))


def fail(message):
    raise AssertionError(message)


def frontmatter(path):
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        fail(f"missing frontmatter: {path}")
    end = text.find("\n---\n", 4)
    if end < 0:
        fail(f"unclosed frontmatter: {path}")
    block = text[4:end]
    fields = {}
    for line in block.splitlines():
        if ":" in line and not line.startswith(" "):
            key, value = line.split(":", 1)
            fields[key.strip()] = value.strip().strip('"')
    return fields, text


def main():
    manifests = [
        PLUGIN / ".claude-plugin" / "plugin.json",
        PLUGIN / ".codex-plugin" / "plugin.json",
    ]
    markets = [
        ROOT / ".claude-plugin" / "marketplace.json",
        ROOT / ".agents" / "plugins" / "marketplace.json",
    ]
    versions = []
    for path in manifests:
        data = load_json(path)
        assert data["name"] == "avada-product-training"
        assert data["author"]["name"]
        versions.append(data["version"])
    for path in markets:
        data = load_json(path)
        assert data["name"] == "avada-training"
        entry = next(p for p in data["plugins"] if p["name"] == "avada-product-training")
        versions.append(entry["version"])
    assert set(versions) == {EXPECTED_VERSION}, versions

    skill_paths = sorted((PLUGIN / "skills").glob("*/SKILL.md"))
    command_paths = sorted((PLUGIN / "commands").glob("*.md"))
    assert len(skill_paths) == 6, skill_paths
    assert len(command_paths) == 6, command_paths
    for path in skill_paths:
        fm, text = frontmatter(path)
        assert fm.get("name") == path.parent.name
        assert fm.get("description")
        assert len(text) > 200
    for path in command_paths:
        fm, _ = frontmatter(path)
        assert fm.get("description")

    required = [
        PLUGIN / "knowledge" / "00-index.md",
        PLUGIN / "knowledge" / "course-map.md",
        PLUGIN / "knowledge" / "product-operator-method.md",
        PLUGIN / "knowledge" / "interactive-training.md",
        PLUGIN / "knowledge" / "templates" / "product-argument.md",
        PLUGIN / "knowledge" / "sources" / "source-map.md",
        PLUGIN / "knowledge" / "sources" / "learning-resources.md",
    ]
    for path in required:
        assert path.exists(), path

    chase_cards = list((PLUGIN / "knowledge" / "chase" / "sources").glob("*.md"))
    interloka_files = list((PLUGIN / "knowledge" / "interloka").rglob("*.md"))
    principles = list((PLUGIN / "knowledge" / "principles").glob("*.md"))
    assert len(chase_cards) == 34, len(chase_cards)
    assert len(interloka_files) >= 15, len(interloka_files)
    assert len(principles) == 6, len(principles)
    graph = load_json(PLUGIN / "knowledge" / "graph" / "graph.json")
    assert len(graph["nodes"]) == 101, len(graph["nodes"])
    assert len(graph["links"]) == 362, len(graph["links"])
    for name in ["GRAPH_REPORT.md", "manifest.json", "graph.html"]:
        assert (PLUGIN / "knowledge" / "graph" / name).exists(), name
    assert (PLUGIN / "scripts" / "query_graph.py").exists()

    forbidden_suffixes = {".pptx", ".pdf", ".heic", ".xlsx", ".csv"}
    secret_patterns = [
        re.compile(r"xox[bpors]-[A-Za-z0-9-]+"),
        re.compile(r"gh[pousr]_[A-Za-z0-9]{20,}"),
        re.compile(r"(?:secret|token|api[_-]?key)\s*[=:]\s*['\"][^'\"]{12,}", re.I),
    ]
    checked = 0
    for path in ROOT.rglob("*"):
        if not path.is_file() or ".git" in path.parts:
            continue
        if path.suffix.lower() in forbidden_suffixes:
            fail(f"binary/private artifact forbidden: {path}")
        if path.stat().st_size > 1_000_000:
            fail(f"file over 1MB: {path}")
        if path.suffix.lower() in {".md", ".json", ".py", ""}:
            text = path.read_text(encoding="utf-8", errors="ignore")
            for pattern in secret_patterns:
                if pattern.search(text):
                    fail(f"possible secret in {path}")
            checked += 1

    teach = (PLUGIN / "skills" / "teach-me-ecom" / "SKILL.md").read_text(encoding="utf-8")
    assert "Ask. Stop and wait" in teach or "Ask" in teach and "Stop and wait" in teach
    assert "Never reveal the answer" in teach
    source_map = (PLUGIN / "knowledge" / "sources" / "source-map.md").read_text(encoding="utf-8")
    assert "6rwsPwD50o" in source_map
    assert "1DlWuw11b6GDcsgQhCiphmpVDVzt80XlLzPQlMlrDxa4" in source_map

    print(json.dumps({
        "ok": True,
        "version": EXPECTED_VERSION,
        "skills": len(skill_paths),
        "commands": len(command_paths),
        "chase_source_cards": len(chase_cards),
        "interloka_markdown": len(interloka_files),
        "principles": len(principles),
        "graph_nodes": len(graph["nodes"]),
        "graph_edges": len(graph["links"]),
        "text_files_scanned": checked,
    }, ensure_ascii=False))


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        print(json.dumps({"ok": False, "error": str(exc)}, ensure_ascii=False))
        raise
