# Product/app deep-dive contract

Use this template for one market app or an Avada app.

## 1. Problem

- What merchant/customer job is failing?
- What is the current workaround?
- What happens if nothing changes?

## 2. ICP and stage

- Who buys?
- Survival, Growth or Scale?
- Which volume/AOV/CLV/CVR/order assumptions follow from that ICP?
- What buying trigger makes the problem urgent?

## 3. Baseline and eligible volume

```text
metric definition
source + grain
baseline/window
eligible cohort/volume
```

If no internal data, state estimate range, clues and data required.

## 4. Mechanism

```text
Who?
→ at what journey moment?
→ sees/does what?
→ why behavior changes?
→ which event confirms movement?
```

UI is not mechanism.

## 5. Economics

```text
eligible volume
× expected lift
× contribution or cost per outcome
= modeled gross value

modeled gross value
− implementation / operations / risk cost
= modeled net value
```

Run downside/base/upside and sensitivity.

## 6. Pricing

- Current price.
- Alternative/substitute cost.
- Risk-adjusted verified value.
- Value-capture share.
- Cost-to-serve.
- Pricing ceiling and confidence.

“Expensive” means expensive relative to value, not a high absolute sticker price.

## 7. Evidence boundary

Label each claim:

- observed fact;
- learner interpretation;
- assumption;
- vendor claim;
- benchmark;
- modeled value;
- experiment-verified incremental result;
- unknown.

## 8. Guardrails

What cannot get worse?

- conversion;
- margin;
- unsubscribe/consent;
- refund/cancel;
- reliability;
- fulfillment/payment/inventory safety;
- support/cost-to-serve.

## 9. Proof plan

- exposed/control or phased rollout;
- primary metric;
- guardrails;
- measurement window;
- minimum sample/volume;
- stop rule;
- read-back/data-quality check.

## 10. Verdict

Choose one:

```text
BUILD
TEST MORE
REPOSITION
STOP
```

Do not return “need more data” without naming the exact data and cheapest discriminating test.
