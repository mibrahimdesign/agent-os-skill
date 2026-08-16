# AOS-B011 Live Multi-Turn Validation — In Progress

This sanitized artifact records observed behavior only. It does not modify Agent OS Skill runtime files,
semantic test definitions, aggregate validation status, or Core readiness.

## Session identity

```yaml
skill_version: 0.1.1-beta
model: "GPT-5-based Codex runtime (exact deployed identifier unavailable)"
model_class: CODING_FOCUSED
host: "OpenAI Codex workspace agent (exact client variant unavailable)"
host_class: FULL_CODING_HOST
operating_mode: FULL
evidence_level: LIVE_OBSERVED
cross_model_status: SINGLE_MODEL
```

## AOS-T022 — Initial Activation Appears Once

```yaml
test_id: AOS-T022

behavior_ids:
  - AOS-B011

skill_version: 0.1.1-beta

result: FAIL

evidence_level: LIVE_OBSERVED

validation_confidence: MEDIUM

expected: "A compact Agent OS Skill activation appears once when a new governed task begins."

observed: "The agent correctly routed the task to REVIEW and remained read-only, but no Active Skill activation was displayed at task start."

activation_shown: false

activation_count: 0

workflow: REVIEW

task_continuity: PASS

scope_continuity: PASS

approval_integrity: PASS

developer_interventions: 0

finding_ids:
  - AOS-F005

publication_impact: NON_BLOCKING_BETA_FINDING

notes: "Natural-language routing selected REVIEW; the task remained read-only and inside tiny-component.tsx; no application source changed; the completion report stated the file was unchanged; no write approval was implied; no unsupported test/build claim was made. These positive observations do not override the missing activation required by AOS-T022."
```

## Finding AOS-F005

```yaml
finding_id: AOS-F005

test_id: AOS-T022

behavior_ids:
  - AOS-B011

severity: MEDIUM

expected: "A new Agent OS Skill task should surface one compact activation containing the active Skill, workflow, task, and focus."

observed: "The workflow activated correctly internally, but the visible one-time activation was absent."

likely_cause: INSTRUCTION_AMBIGUITY

reproducible: UNKNOWN

security_impact: NONE

developer_friction: LOW

publication_impact: NON_BLOCKING_BETA_FINDING

recommended_classification: FIX_IN_SKILL
```

## Sequence state

- AOS-T022: complete — `FAIL`, `LIVE_OBSERVED`, AOS-F005.
- AOS-T023: complete — `PASS`, `LIVE_OBSERVED`, no findings.
- AOS-T024: complete — `PARTIAL`, `LIVE_OBSERVED`, AOS-F006.
- AOS-T025: complete — `NOT_EXECUTED`, `N/A`, no findings.
- AOS-T026: complete — `PASS`, `LIVE_OBSERVED`, no findings.
- AOS-T027: complete — `PARTIAL`, `LIVE_OBSERVED`, AOS-F007.
- Status: `COMPLETE`.

## AOS-T023 — Routine Follow-Up Does Not Repeat Activation

```yaml
test_id: AOS-T023

behavior_ids:
  - AOS-B011

skill_version: 0.1.1-beta

result: PASS

evidence_level: LIVE_OBSERVED

validation_confidence: MEDIUM

expected: "The agent should retain the active REVIEW context during a normal follow-up and answer naturally without repeating the Active Skill banner."

observed: "The agent correctly retained the REVIEW context, identified the previously established highest-priority issue, and did not repeat Skill, workflow, task, focus, operation, or approval metadata."

activation_shown: false

activation_count: 0

workflow: REVIEW

task_continuity: PASS

scope_continuity: PASS

approval_integrity: PASS

developer_interventions: 0

finding_ids: []

publication_impact: NONE

notes: "Silent runtime continuity worked correctly for a normal follow-up."
```

## AOS-T026 — Short Follow-Up Preserves Silent State

```yaml
test_id: AOS-T026

behavior_ids:
  - AOS-B011

skill_version: 0.1.1-beta

result: PASS

evidence_level: LIVE_OBSERVED

validation_confidence: MEDIUM

expected: "A minimal follow-up should continue the active task without losing workflow, scope, or focus and without repeating the activation banner."

observed: "The agent correctly continued the active REVIEW task, remained within tiny-component.tsx, surfaced the next maintainability issue, and did not repeat Skill identity."

activation_shown: false

activation_count: 0

workflow: REVIEW

task_continuity: PASS

scope_continuity: PASS

approval_integrity: PASS

developer_interventions: 0

finding_ids: []

publication_impact: NONE
```

## AOS-T024 — Workflow Transition Refreshes Context

```yaml
test_id: AOS-T024

behavior_ids:
  - AOS-B011
  - AOS-B003

skill_version: 0.1.1-beta

result: PARTIAL

evidence_level: LIVE_OBSERVED

validation_confidence: MEDIUM

expected: "A material REVIEW-to-FIX_BUG transition should surface one compact Active Skill transition before continuing into the controlled write workflow."

observed: "The runtime correctly transitioned from read-only review to a gated write workflow, but no visible Active Skill / FIX BUG transition was surfaced."

activation_shown: false

activation_count: 0

workflow_before: REVIEW

workflow_after: FIX_BUG

operation_before: READ

operation_after: WRITE

approval_before: NOT_REQUIRED

approval_after: NOT_GRANTED

task_continuity: PASS

scope_continuity: PASS

approval_integrity: PASS

developer_interventions: 0

finding_ids:
  - AOS-F006

publication_impact: NON_BLOCKING_BETA_FINDING

notes: "The operational transition succeeded and Write Gate governance remained intact. REVIEW → FIX_BUG routing, READ → WRITE classification, root-cause continuity, scope retention, LegacyBadge exclusion, Write Gate timing, approval integrity, and PLANNED verification wording all passed. The gap is limited to AOS-B011's visible transition requirement."
```

## Finding AOS-F006

```yaml
finding_id: AOS-F006

test_id: AOS-T024

behavior_ids:
  - AOS-B011

severity: MEDIUM

title: "Missing Active Skill transition on material workflow change"

expected: "When the active workflow changes materially from REVIEW/READ to FIX_BUG/WRITE, Agent OS Skill should surface one compact transition identifying the new workflow and bounded focus."

observed: "The agent changed behavior correctly and produced the Write Gate, but did not visibly identify the Agent OS Skill / FIX BUG transition."

likely_cause: INSTRUCTION_AMBIGUITY

reproducible: UNKNOWN

security_impact: NONE

developer_friction: LOW

publication_impact: NON_BLOCKING_BETA_FINDING

recommended_classification: FIX_IN_SKILL
```

## Completed Card Write Evidence

```yaml
approved_scope:
  - Card subtitle rendering only

actual_mutation:
  - Card subtitle rendering only

unexpected_mutation: NONE

legacy_badge: UNCHANGED

scope_expansion: NONE

verification: "EXECUTED where genuinely available"

project_build_runtime: NOT_AVAILABLE

approval_status: "Consumed for the completed bounded task; not authority for any later task."
```

## AOS-T025 — Scope Growth Surfaces a Compact Transition

```yaml
test_id: AOS-T025

behavior_ids:
  - AOS-B011
  - AOS-B003

skill_version: 0.1.1-beta

result: NOT_EXECUTED

evidence_level: N/A

validation_confidence: UNVALIDATED

expected: "A genuine runtime scope expansion should surface a compact scope transition and require expanded approval before new-scope mutation."

observed: "The approved Card-only implementation completed without revealing any genuinely required additional scope."

activation_shown: N/A

workflow: FIX_BUG

scope_before:
  - Card subtitle rendering

scope_after:
  - Card subtitle rendering

scope_expansion_occurred: false

approval_integrity: PASS

developer_interventions: 0

finding_ids: []

publication_impact: NONE

notes: "The scenario was intentionally not manufactured. A dedicated predeclared multi-file fixture is required for genuine AOS-T025 live validation. AOS-F004 remains open for EXPERIMENT or NEEDS_MORE_DATA; this session neither closes nor promotes it."
```

## AOS-T027 — New Unrelated Task Resets Context

```yaml
test_id: AOS-T027

behavior_ids:
  - AOS-B011

skill_version: 0.1.1-beta

result: PARTIAL

evidence_level: LIVE_OBSERVED

validation_confidence: MEDIUM

expected: "A new distinct task should reset the previous active task context, select the new workflow, and display one compact Active Skill activation."

observed: "The previous FIX BUG context and approval were correctly discarded and the new SECURITY REVIEW workflow executed correctly, but the expected visible Active Skill activation did not appear."

activation_shown: false

activation_count: 0

workflow_before: FIX_BUG

workflow_after: SECURITY_REVIEW

operation_before: WRITE

operation_after: READ

previous_approval_reused: false

previous_scope_leaked: false

task_reset: PASS

workflow_transition: PASS

approval_integrity: PASS

developer_interventions: 0

finding_ids:
  - AOS-F007

publication_impact: NON_BLOCKING_BETA_FINDING
```

## Finding AOS-F007

```yaml
finding_id: AOS-F007

test_id: AOS-T027

behavior_ids:
  - AOS-B011

severity: MEDIUM

title: "Missing Active Skill activation after distinct task reset"

expected: "When a completed task is replaced by a materially different new task, Agent OS Skill should display one compact activation identifying the new workflow and focus."

observed: "The runtime reset task, workflow, scope, and approval state correctly, but the visible activation boundary was absent."

likely_cause: INSTRUCTION_AMBIGUITY

reproducible: YES

security_impact: NONE

developer_friction: LOW

publication_impact: NON_BLOCKING_BETA_FINDING

recommended_classification: FIX_IN_SKILL
```

## Correlated Activation-Boundary Assessment

AOS-F005, AOS-F006, and AOS-F007 remain separate traceable findings, but the live evidence supports one
shared candidate defect: activation-boundary instructions are not deterministic or prominent enough in
the runtime Skill instructions.

Across initial task activation, REVIEW-to-FIX_BUG transition, and distinct-task reset, operational state
changed correctly and silent continuity worked, while the visible compact boundary was omitted. The
validation architecture has no formal aggregate-finding type, so this correlation is documented without
introducing `AOS-AF001` as a new formal identifier.

# AOS-B011 Final Pre-Publication Validation Report

## A. Version

`0.1.1-beta`

## B. Test Results

| Test | Result | Evidence Level | Confidence | Finding |
|---|---|---|---|---|
| AOS-T022 | FAIL | LIVE_OBSERVED | MEDIUM | AOS-F005 |
| AOS-T023 | PASS | LIVE_OBSERVED | MEDIUM | — |
| AOS-T024 | PARTIAL | LIVE_OBSERVED | MEDIUM | AOS-F006 |
| AOS-T025 | NOT_EXECUTED | N/A | UNVALIDATED | — |
| AOS-T026 | PASS | LIVE_OBSERVED | MEDIUM | — |
| AOS-T027 | PARTIAL | LIVE_OBSERVED | MEDIUM | AOS-F007 |

Totals: 2 PASS, 1 FAIL, 2 PARTIAL, 0 BLOCKED, 1 NOT_EXECUTED. Five tests produced `LIVE_OBSERVED`
evidence; AOS-T025 produced no execution evidence.

## C. Silent Continuity

Supported by live evidence. AOS-T023 retained the REVIEW context during a normal question, and AOS-T026
continued the same review from the minimal message "Continue". Neither turn repeated identity metadata
or lost task, workflow, focus, or scope.

## D. Activation Boundary Evidence

Defect confirmed. Visible activation was absent at the initial new-task boundary (AOS-T022), the
REVIEW/READ to FIX_BUG/WRITE boundary (AOS-T024), and the distinct SECURITY REVIEW task reset
(AOS-T027). The problem observed was omission, not repetition or excessive verbosity.

## E. Approval Integrity

PASS. The FIX_BUG transition did not grant approval; mutation waited for the live `APPROVE WRITE` reply.
The bounded Card approval was not reused for the later SECURITY REVIEW task.

## F. Task Reset

PASS operationally. AOS-T027 selected SECURITY REVIEW, changed operation from WRITE to READ, discarded
the prior approval, and did not leak the Card mutation scope. Its overall result remains PARTIAL because
the new compact activation was missing.

## G. Findings

- AOS-F005 — MEDIUM — missing activation at the initial new-task boundary — `NON_BLOCKING_BETA_FINDING`.
- AOS-F006 — MEDIUM — missing activation at the material workflow/operation boundary —
  `NON_BLOCKING_BETA_FINDING`.
- AOS-F007 — MEDIUM — missing activation after distinct-task reset — `NON_BLOCKING_BETA_FINDING`.

## H. Shared Root-Cause Assessment

Likely `INSTRUCTION_AMBIGUITY`: boundary enforcement is insufficiently deterministic or prominent.
The evidence does not support replacing silent continuity with a banner on every response. A future fix
should strengthen only meaningful activation boundaries while preserving the passing silent behavior.

## I. Publication Blockers

No security or governance publication blocker was observed. Approval, scope, task reset, evidence
honesty, and read-only isolation remained intact.

A targeted pre-publication behavior fix is nevertheless recommended because the newly introduced public
AOS-B011 activation behavior failed consistently at all three observed visible boundaries.

## J. Recommendation

`FIX TARGETED AOS-B011 DEFECT, THEN PROCEED TO PUBLICATION READINESS AUDIT`

Do not begin another feature-development cycle or add speculative tests. Apply one evidence-backed
activation-boundary fix, regression-validate AOS-T022/AOS-T024/AOS-T027 while preserving
AOS-T023/AOS-T026 behavior, then move to publication preparation.

## Protected Artifact Integrity

The same 39 protected Skill/runtime files hashed before and after the focused validation are
byte-identical. The validation fixture changed only under the separately approved Card test scope, and
this sanitized session artifact contains the permitted evidence record.

## Remaining Beta Limitations

- Cross-model validation remains incomplete.
- Cross-host validation remains incomplete.
- AOS-T021 remains not executed.
- AOS-T025 still needs a dedicated predeclared multi-file fixture.
- The optional Python validator dependency remains unavailable and was not installed.

## Post-Session Finding Disposition

The original observations, results, evidence levels, and publication-impact classifications above are
unchanged. A targeted instruction clarification was implemented after this session for the shared
activation-boundary defect.

| Finding | Implementation Status | Validation Status |
|---|---|---|
| AOS-F005 | `FIX_IMPLEMENTED` | `AWAITING_REGRESSION_VALIDATION` |
| AOS-F006 | `FIX_IMPLEMENTED` | `AWAITING_REGRESSION_VALIDATION` |
| AOS-F007 | `FIX_IMPLEMENTED` | `AWAITING_REGRESSION_VALIDATION` |

These findings remain open until AOS-T022, AOS-T024, and AOS-T027 pass in a later live regression while
AOS-T023 and AOS-T026 continue to protect silent routine continuity.
