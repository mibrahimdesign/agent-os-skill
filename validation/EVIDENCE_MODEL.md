# Validation Evidence Model

This document defines validation metadata for Agent OS Skill. It does not add to or modify runtime
governance in `SKILL.md`; it describes how maintainers record confidence in observed behavior.

## Result and evidence are separate

`result` records whether the expected behavior occurred:

`PASS | FAIL | PARTIAL | BLOCKED | NOT_EXECUTED`

`evidence_level` records how the result was established:

| Evidence level | Definition |
|---|---|
| `STATIC_REVIEW` | Files were inspected only. No agent task execution occurred. |
| `SELF_SIMULATED` | The same agent reasoned through or simulated the scenario. Useful early evidence, but not field validation. |
| `LIVE_OBSERVED` | A real agent executed the scenario in an actual host/runtime and its behavior was observed. |
| `LIVE_INDEPENDENT` | A live execution was independently evaluated by a separate reviewer, process, agent, or evidence source sufficient to justify independence. A second reasoning pass by the same agent is not independent. |

A `PASS` at one evidence level is not equivalent to a `PASS` at another. Never combine the two fields
into a label such as `SIMULATED_PASS`.

For a test with `result: NOT_EXECUTED`, use `evidence_level: N/A`; no behavior evidence exists.

## Validation confidence

`validation_confidence` is an optional assessment derived from the result, evidence level, repetition,
coverage, interventions, and unresolved failure severity:

| Confidence | Interpretation |
|---|---|
| `UNVALIDATED` | No execution or simulation evidence. Required for `NOT_EXECUTED`. |
| `LOW` | Static review or a single self-simulation. |
| `MEDIUM` | Stronger self-simulation with stated supporting evidence, or live observation without sufficient repetition for high confidence. |
| `HIGH` | Repeated live evidence across the intended material model/host environments, with no unresolved material failure and limited intervention. |

One successful run never automatically produces `HIGH`. Any non-default confidence assessment must state
its rationale in `notes` or the session methodology.

## Field-confirmed tests

A test is `FIELD_CONFIRMED` only when:

```text
result = PASS
and
evidence_level = LIVE_OBSERVED or LIVE_INDEPENDENT
```

A `SELF_SIMULATED` or `STATIC_REVIEW` pass is not field-confirmed.

## Model metadata

Record the actual model name as test metadata when known. Classify it separately and without vendor
assumptions:

`STRONG_REASONING | CODING_FOCUSED | SMALL_OR_LOCAL | OTHER`

The class is a comparison aid, not a quality claim about a vendor or product.

## Host metadata

Record the actual host identity when known. Classify the capability environment separately:

`FULL_CODING_HOST | LIMITED_CODING_HOST | EMBEDDED_CHAT_HOST | OTHER`

Hosts with different product names but materially identical capability profiles do not, by that fact
alone, provide strong portability evidence.

## Cross-model confidence

| State | Rule |
|---|---|
| `MODEL_UNTESTED` | No live model validation exists. |
| `SINGLE_MODEL` | One model class has live observed or stronger passing evidence. |
| `MULTI_MODEL` | At least two materially different model classes have live observed or stronger passing evidence. |
| `CROSS_MODEL_STABLE` | The behavior repeatedly passes across the intended model classes, with no unresolved material failure and acceptable intervention levels. |

Stability is not awarded by count alone. Failure severity, reproducibility, coverage, and developer
interventions remain material.

## Cross-host confidence

| State | Rule |
|---|---|
| `HOST_UNTESTED` | No live host validation exists. |
| `SINGLE_HOST` | One host class has live observed or stronger passing evidence. |
| `MULTI_HOST` | At least two materially different host capability classes have live observed or stronger passing evidence. |
| `CROSS_HOST_STABLE` | The behavior repeatedly passes across the intended capability environments, with no unresolved material failure and honest degradation where capabilities are absent. |

## Validation maturity

Validation maturity is metadata only. It is not Agent OS governance and does not alter G1-G10.
Assign it per behavior, not only to the Skill as a whole.

| Level | Name | Minimum evidence |
|---|---|---|
| `LEVEL 0` | `SPECIFIED` | Behavior is defined. |
| `LEVEL 1` | `STATICALLY REVIEWED` | Relevant files were inspected for internal consistency. |
| `LEVEL 2` | `SELF-SIMULATED` | The behavior was exercised by self-simulation. |
| `LEVEL 3` | `LIVE OBSERVED` | The behavior passed in a real observed execution. |
| `LEVEL 4` | `CROSS-MODEL OBSERVED` | Live evidence spans materially different intended model classes. |
| `LEVEL 5` | `CROSS-HOST OBSERVED` | Live evidence spans materially different intended host capability classes. |
| `LEVEL 6` | `FIELD STABLE` | Repeated real use supports stability across intended environments, with no unresolved material failure. |

Levels are evidence thresholds, not release numbers. A behavior can remain at a lower level while a
different behavior advances.
