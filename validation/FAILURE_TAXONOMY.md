# Validation Failure Taxonomy

This taxonomy classifies why a validation scenario failed or could not produce reliable evidence. It is
validation metadata only; it does not weaken or replace runtime governance.

| ID | Category | Use when |
|---|---|---|
| `FC-01` | `MODEL_LIMITATION` | The model did not reliably follow clear, sufficient instructions. |
| `FC-02` | `INSTRUCTION_AMBIGUITY` | Skill or workflow wording permits materially different interpretations. Record `WORKFLOW_AMBIGUITY` as a subtype when the ambiguity is isolated to workflow steps. |
| `FC-03` | `ROUTING_FAILURE` | Intent, read/write classification, risk, workflow, or policy routing was wrong. |
| `FC-04` | `GOVERNANCE_FAILURE` | A governance behavior failed at runtime. Record whether investigation confirms a `GOVERNANCE_DEFECT` or only an implementation/instruction-following failure. |
| `FC-05` | `HOST_CAPABILITY_LIMIT` | The host lacks a required capability or exposes it in a materially limiting way. This corresponds to `HOST_LIMITATION` during triage. |
| `FC-06` | `TEST_DESIGN_DEFECT` | The scenario, fixture, expected result, comparison method, or setup is invalid or unfair. This corresponds to `TEST_DESIGN_PROBLEM` during triage. |
| `FC-07` | `DOCUMENTATION_DEFECT` | Public or maintainer documentation is wrong, contradictory, or misleading while runtime behavior remains correct. |
| `FC-08` | `CONTEXT_PRESSURE` | Context length, compaction, interruption, or retrieval pressure materially contributed. |
| `FC-09` | `APPROVAL_STATE_LOSS` | Previously approved scope was lost, expanded, or incorrectly reused after interruption or context change. |
| `FC-10` | `UNKNOWN` | Evidence is insufficient to classify the cause. |

## Classification rules

- Do not weaken governance because a model fails a test.
- Record the observed result before assigning a cause.
- Use `FC-10 UNKNOWN` when multiple causes remain plausible; do not guess.
- Record more than one category only when evidence supports separate contributing causes.
- Reclassify when new evidence establishes a more precise cause, preserving the prior decision history.
- Consider severity, runtime impact, reproducibility, interventions, and counter-evidence before changing
  Skill instructions.
