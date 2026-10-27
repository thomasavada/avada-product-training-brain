---
name: teach-me-ecom
argument-hint: "What would you like to learn?"
description: Teach ecommerce, brand or product thinking through short, stateful, interactive lessons. Use when the user says teach me, wants to learn a brain topic, asks for a learning path, or wants practice over multiple sessions. Do not use for a one-shot brand teardown (`brand-case-clinic`) or an app ROI analysis (`app-value-deep-dive`).
---

# Teach Me — Ecommerce, Brand and Product

This is a stateful learning workflow combining:

- Pocock-style mission, lessons and learning records;
- Chase's scenario → guess → one job classroom rhythm;
- Avada's observe → hypothesis → evidence → correction loop;
- Interloka's business-model and brand-strategy dependency chain.

## Workspace

Treat cwd as learner workspace. Create only when needed:

- `MISSION.md` — why this capability matters and where it will be used;
- `RESOURCES.md` — selected primary/watch sources with viewing prompts;
- `NOTES.md` — learner preferences and open questions;
- `lessons/NNNN-<slug>.html` — one short lesson;
- `learning-records/NNNN-<slug>.md` — only after demonstrated capability;
- `reference/*.html` — durable glossary/checklist/diagram.

Do not write learning records for attendance or reading completion.

## First turn

If the user gives a topic, infer a provisional mission and start. Ask for clarification only when different missions would change the lesson materially.

Choose the source domain:

| Topic | Read |
|---|---|
| Business/ecommerce fundamentals, stage, KPI, ROI | `knowledge/course-map.md`, `knowledge/product-operator-method.md` |
| Meta ads, offer, CRO, TikTok Shop, retention | `knowledge/chase/` concept + source index |
| Business model, Blue Ocean, category, POD, positioning | `knowledge/interloka/knowledge/` + curriculum |
| Training/facilitation/Kahoot | `knowledge/interactive-training.md` |
| Chọn video/resource cho lesson | `knowledge/sources/learning-resources.md` — dùng index này trước, không scan toàn bộ source cards |
| One app/product economics | switch to `app-value-deep-dive` |
| One named brand teardown | switch to `brand-case-clinic` |

## One lesson rhythm

One lesson teaches one tightly-scoped capability.

1. **Scenario** — show one real or realistic situation.
2. **Ask** — learner predicts/diagnoses/calculates. Stop and wait.
3. **Reject generic** — name why a vague answer does not discriminate.
4. **One job** — reveal one mechanism/action, not a playbook dump.
5. **Transfer** — give a second case with changed context.
6. **Artifact** — learner writes a calculation, diagnosis, decision or revised model.
7. **Record** — only when they can explain and apply it independently.

Never reveal the answer in the same message as the first question.

## Cognitive load

- Keep working-memory load low during knowledge acquisition.
- Use retrieval difficulty during skill practice.
- Interleave related topics only after the learner can perform each separately.
- Space lessons; do not compress the entire brain into one session.

## Foundation diagnostic

When baseline is unclear, start with 8–12 short questions covering only the needed prerequisite set:

- terminology;
- denominator/grain;
- quick arithmetic;
- fact vs inference;
- metric-to-job matching.

Use results to choose what to reteach. The quiz is not a leaderboard and not capability proof.

## Lesson output

Each HTML lesson should include:

- mission link;
- scenario;
- learner's original answer;
- correction/one job;
- before/after or worked math;
- one primary/watch source;
- transfer challenge;
- evidence labels.

Reuse a shared stylesheet in `assets/` after the first lesson.

## Resource discipline

Do not send passive link lists. For each resource write:

```text
Watch/read what?
Notice what?
Apply to which case?
Submit which artifact?
```

Chase sources are claims from Chase unless independently verified. Interloka synthesis must remain separated from source-native material.

## Completion

A lesson completes when the learner can:

- name the scenario;
- select the relevant metric/framework;
- explain the mechanism;
- apply it to a changed case;
- state evidence limits.

Coverage is not learning.
