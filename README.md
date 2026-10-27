# Avada Product Training Brain

Public Claude Code, Codex and Grok plugin for learning and applying:

- ecommerce/business economics;
- merchant stages and KPI diagnosis;
- brand/business-model strategy;
- product mechanism, value, ROI and pricing;
- active case clinics and stateful teaching.

It combines three curated layers:

1. **Avada Product Training** — Session 1–4, learner artifacts, progress and feedback.
2. **Chase Chappell brain** — selected ecommerce metrics, offer, CRO, TikTok Shop, retention and source-video index.
3. **Interloka synthesis** — selected Integrated Brand Strategy and Business Model frameworks.

Raw private transcripts, source photos, credentials and binary training decks are not published here.

## Install

### Claude Code

```text
/plugin marketplace add https://github.com/thomasavada/avada-product-training-brain.git
/plugin install avada-product-training@avada-training
```

### Codex

```bash
codex plugin marketplace add thomasavada/avada-product-training-brain
codex plugin add avada-product-training@avada-training
```

### Grok

```bash
grok plugin marketplace add thomasavada/avada-product-training-brain
grok plugin install avada-product-training --trust
grok plugin enable avada-product-training
```

Start a new session after install/update.

## Commands

| Command | Job |
|---|---|
| `/product-training` | Query the source-grounded brain |
| `/teach-me` | Stateful, interactive learning: one scenario, guess, correction, transfer |
| `/analyze-brand` | Evidence-led brand/store case clinic |
| `/analyze-app` | App mechanism, KPI, value, ROI, pricing and proof |
| `/learning-habit` | Build a 30-day mission, source queue, practice cadence and review loop |
| `/brain-graph` | Navigate Graphify paths, hubs and connected knowledge |

## What ships

```text
plugins/avada-product-training/
├── skills/       reusable agent workflows
├── commands/     thin slash-command adapters
└── knowledge/
    ├── principles/
    ├── progress/
    ├── sessions/
    ├── cases/
    ├── chase/       curated public Chase material
    ├── interloka/   synthesized framework notes, no raw course photos/OCR
    ├── graph/       101-node knowledge graph, report and interactive HTML
    └── sources/
```

Knowledge remains Markdown next to the skills. Agents must read the files instead of guessing.

## Teaching model

```text
Mission
→ foundation diagnostic
→ one short scenario
→ learner predicts
→ one correction/job
→ transfer case
→ artifact
→ learning record
→ spaced repetition
```

Coverage is not learning. Attendance is not learning. A lesson completes when the learner can apply the idea to a changed case and explain evidence limits.

## Channels and learning habit

`knowledge/sources/channel-guide.md` curates Chase Chappell, Operators Podcast, Limited Supply, Shopify Masters, The Unofficial Shopify Podcast, The CPG Guys, Chew On This and the Interloka worked videos. Every source has a learning job, caution and required artifact.

`/learning-habit` turns that corpus into a weekly routine. It limits the queue to five resources and measures retrieval, live-source inspection, artifacts, challenge and revision instead of watch time.

## Graphify

The committed graph is rebuilt deterministically from Markdown wikilinks plus explicit cross-domain teaching links:

```bash
python3 scripts/rebuild-graph.py
python3 scripts/rebuild-graph.py --check --strict
graphify path "Product operator method" "Metric diagnosis tree" \
  --graph graphify-out/graph.json --undirected
```

Current graph: **101 nodes · 362 edges · 0 unresolved wikilinks**. The same graph artifacts ship inside the plugin at `knowledge/graph/`, so `/brain-graph` works after marketplace installation.

## Evidence rules

- Distinguish observed fact, learner interpretation, assumption, vendor claim, modeled value and experiment-verified incrementality.
- Chase numbers remain Chase/vendor claims unless independently verified.
- Interloka notes are synthesis; raw proprietary photographs/OCR are excluded.
- Learner artifacts prove what learners presented, not that every claim is true.
- Two feedback responses before Session 3 are qualitative signals, not cohort-level proof.

## Provenance

See [`SOURCES.md`](SOURCES.md) and [`THIRD_PARTY_NOTICES.md`](THIRD_PARTY_NOTICES.md).

## License

MIT for original plugin code and Avada-authored synthesis. Third-party source material retains its original rights; this repository links to primary videos/sources and marks derived material.
