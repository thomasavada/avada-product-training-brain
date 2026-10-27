---
name: app-value-deep-dive
description: Turn one ecommerce app or product idea into an evidence-led mechanism, KPI, economic value, pricing and proof contract. Use when analyzing why an app sells, whether it is expensive, what metric it changes, whether to build it, or preparing the Avada app deep-dive assignment. Do not use for broad brand diagnosis (`brand-case-clinic`).
---

# App Value Deep Dive

## Read first

- `knowledge/templates/product-argument.md`
- `knowledge/product-operator-method.md`
- `knowledge/principles/metric-to-value.md`
- any relevant Chase/Interloka concept

## Procedure

### 1. Name the job

Write one sentence:

> For [ICP/stage], at [journey moment], the app removes [economic leak] by [mechanism].

Reject category labels such as “survey app” or “AOV app” as problem statements.

### 2. Lock baseline

Specify:

- metric formula;
- source and grain;
- denominator;
- time window;
- eligible volume;
- current workaround and spend.

If unavailable, use a range and name the evidence needed.

### 3. Explain mechanism

Map:

```text
trigger/context
→ app action
→ user/merchant behavior
→ observable event
→ business KPI
```

A UI element or feature list is not a mechanism.

### 4. Close to economics

```text
eligible volume
× expected lift
× contribution or avoided cost per outcome
= modeled gross value

modeled gross value
− cost/risk/operations
= modeled net value
```

Run downside/base/upside. Use tools for arithmetic.

### 5. Judge price

Compare current price with:

- risk-adjusted value;
- substitute cost;
- implementation/adoption friction;
- cost-to-serve;
- confidence;
- merchant value-capture share.

Do not call an app expensive from sticker price alone.

### 6. Verify market claim

Check:

- ICP in marketing/case studies;
- promise and mechanism alignment;
- pricing/packaging;
- competitor/substitute;
- case-study methodology and selection bias;
- whether claims are associated, modeled or incremental.

### 7. Design proof

Specify primary metric, guardrails, cohort/control, window, read-back and stop rule.

### 8. Verdict

Choose exactly one:

- BUILD
- TEST MORE
- REPOSITION
- STOP

“Need more data” is incomplete unless the exact missing data and cheapest test are named.

## Output contract

Use the full template in `knowledge/templates/product-argument.md`. End with evidence status and source list.
