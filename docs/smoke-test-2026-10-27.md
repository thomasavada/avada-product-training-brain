# Smoke test — 2026-10-27

Tested from `/tmp` using the plugin by absolute path, so retrieval did not depend on repository cwd.

## Positive — stateful teaching

Prompt:

> Teach me AOV versus contribution. Start one lesson only, ask the first scenario question, and stop before revealing the answer.

Observed:

- Loaded the teaching skill.
- Created a provisional `MISSION.md` and one lesson in `/tmp`.
- Presented one skincare offer scenario.
- Asked learner to calculate AOV, revenue and contribution.
- Stopped before revealing the answer.

Verdict: **pass**.

## Positive — source/evidence boundary

Prompt:

> Hai feedback 21/10 và 24/10 có chứng minh Session 3 vẫn overload không?

Observed:

- Correct answer: no.
- Identified both responses as pre-Session-3.
- Separated fact, learner interpretation, facilitator inference, assumption and unknown.
- Preserved `n=2` and anonymous/self-report limitations.
- Named the additional evidence needed.

Verdict: **pass**.

## Negative — unrelated coding request

Prompt:

> Write a Python function that reverses a string. Do not use any training curriculum.

Observed:

- Returned ordinary Python code.
- Did not invoke or mention Avada Product Training knowledge.

Verdict: **pass**.

## Curated resources

The resource corpus is statically checked in `tests/test_plugin.py` for:

- Chase metric diagnosis video;
- Chase Five Levels of Brands video;
- Interloka/Ryanair business-model video;
- at least ten public URLs;
- an artifact prompt for every curated resource.

This avoids requiring the runtime to scan all 33 Chase source cards for a simple learning-path request.
