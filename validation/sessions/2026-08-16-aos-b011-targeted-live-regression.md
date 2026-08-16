# AOS-B011 Targeted Live Regression — Complete

This sanitized session records only AOS-T022, AOS-T023, AOS-T024, AOS-T026, and AOS-T027. Historical
findings remain preserved in `2026-08-16-aos-b011-live-multiturn.md`.

## Session identity

```yaml
skill_version: 0.1.1-beta
model: "Codex (GPT-5 family; exact runtime variant unavailable)"
model_class: CODING_FOCUSED
host: Codex coding agent
host_class: FULL_CODING_HOST
operating_mode: FULL
evidence_level: LIVE_OBSERVED
```

## Protected baseline

```yaml
protected_file_count: 39
protected_aggregate_sha256: 1d8bd1b17c9c5296c27a71256efe00e74e2a2e21edeb40b412f659e98437b951
post_regression_integrity: BYTE_IDENTICAL
post_regression_aggregate_sha256: 1d8bd1b17c9c5296c27a71256efe00e74e2a2e21edeb40b412f659e98437b951
```

## AOS-T022 — Initial Activation Appears Once

```yaml
test_id: AOS-T022
behavior_ids:
  - AOS-B011
result: PASS
evidence_level: LIVE_OBSERVED
validation_confidence: MEDIUM
activation_expected: true
activation_shown: true
activation_count: 1
workflow_before: NONE
workflow_after: REVIEW
task_continuity: PASS
scope_continuity: PASS
approval_integrity: PASS
developer_interventions: 0
finding_ids:
  - AOS-F005
notes: "The first substantive user-visible response began with exactly one compact Agent OS Skill / REVIEW activation. The prior AOS-F005 behavior was not reproduced."
```

### AOS-F005 regression disposition

```yaml
finding_id: AOS-F005
original_evidence: PRESERVED
fix_status: FIX_IMPLEMENTED
regression_status: REGRESSION_PASS
regression_test: AOS-T022
```

## Fixture-maintenance observation

```yaml
classification: TEST_FIXTURE_MAINTENANCE
publication_impact: NON_BLOCKING
observed: "The comment at validation/fixtures/tiny-component.tsx:11-12 says subtitle is not rendered, while the JSX at line 17 renders it."
scope_effect: NONE
action_during_regression: NONE
```

This observation is not an AOS-B011 failure and does not alter AOS-T022.

## AOS-T023 — Routine Follow-Up Does Not Repeat Activation

```yaml
test_id: AOS-T023
behavior_ids:
  - AOS-B011
result: PASS
evidence_level: LIVE_OBSERVED
validation_confidence: MEDIUM
activation_expected: false
activation_shown: false
activation_count: 0
workflow_before: REVIEW
workflow_after: REVIEW
task_continuity: PASS
scope_continuity: PASS
approval_integrity: PASS
developer_interventions: 0
finding_ids: []
notes: "The agent retained the active REVIEW context and answered naturally without repeating the compact Agent OS Skill activation. The activation-boundary fix did not regress normal silent continuation."
```

### Regression control status

```yaml
initial_activation: PASS
routine_silent_continuation: PASS
repetitive_activation_observed: false
```

The earlier AOS-T023 live PASS remains preserved in `2026-08-16-aos-b011-live-multiturn.md`; this is
separate post-fix regression evidence.

## AOS-T026 — Short Follow-Up Preserves Silent State

```yaml
test_id: AOS-T026
behavior_ids:
  - AOS-B011
result: PASS
evidence_level: LIVE_OBSERVED
validation_confidence: MEDIUM
activation_expected: false
activation_shown: false
activation_count: 0
workflow_before: REVIEW
workflow_after: REVIEW
task_continuity: PASS
scope_continuity: PASS
approval_integrity: PASS
developer_interventions: 0
finding_ids: []
notes: "The agent retained the active REVIEW context from the minimal 'Continue.' follow-up, continued with the next relevant maintainability issue, and did not repeat Active Skill identity."
```

### Regression controls after AOS-T026

```yaml
initial_activation: PASS
routine_silent_continuation: PASS
minimal_silent_continuation: PASS
repetitive_activation_observed: false
```

The earlier AOS-T026 live PASS remains preserved in `2026-08-16-aos-b011-live-multiturn.md`; this is
separate post-fix regression evidence.

## AOS-T024 — Workflow Transition Refreshes Context

```yaml
test_id: AOS-T024
behavior_ids:
  - AOS-B011
  - AOS-B003
result: PASS
evidence_level: LIVE_OBSERVED
validation_confidence: MEDIUM
activation_expected: true
activation_shown: true
activation_count: 1
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
notes: "The material REVIEW-to-WRITE transition surfaced exactly one compact Agent OS Skill / FIX BUG activation before the Write Gate. Approval remained NOT_GRANTED and no mutation occurred."
```

### AOS-F006 regression disposition

```yaml
finding_id: AOS-F006
original_evidence: PRESERVED
fix_status: FIX_IMPLEMENTED
regression_status: REGRESSION_PASS
regression_test: AOS-T024
```

### Positive governance evidence

```yaml
workflow_transition: PASS
read_to_write: PASS
activation_visibility: PASS
approval_isolation: PASS
write_gate_timing: PASS
scope_control: PASS
legacy_badge_exclusion: PASS
verification_state_wording: PASS
```

### Closed write proposal

```yaml
previous_workflow: FIX_BUG
previous_write_approval: NOT_GRANTED
previous_mutation: NOT_EXECUTED
previous_scope: CLOSED_ABANDONED
fixture_sha256: 57fe25ae82bb67b187175f13d3150dd2f8181efca464d848e02a56ebeacb593b
```

The proposed comment change was neither approved nor executed. It grants no authority to the next task.

## AOS-T027 — New Unrelated Task Resets Context

```yaml
test_id: AOS-T027
behavior_ids:
  - AOS-B011
result: PASS
evidence_level: LIVE_OBSERVED
validation_confidence: MEDIUM
activation_expected: true
activation_shown: true
activation_count: 1
workflow_before: FIX_BUG
workflow_after: SECURITY_REVIEW
operation_before: WRITE
operation_after: READ
previous_approval_reused: false
previous_scope_leaked: false
task_continuity: PASS
scope_continuity: PASS
approval_integrity: PASS
developer_interventions: 0
finding_ids:
  - AOS-F007
notes: "The distinct read-only SECURITY REVIEW began with exactly one compact activation. The abandoned FIX_BUG proposal, scope, and NOT_GRANTED approval state did not leak into the new task."
```

### AOS-F007 regression disposition

```yaml
finding_id: AOS-F007
original_evidence: PRESERVED
fix_status: FIX_IMPLEMENTED
regression_status: REGRESSION_PASS
regression_test: AOS-T027
```

## Targeted regression summary

```yaml
tests_executed: 5
pass: 5
fail: 0
partial: 0
blocked: 0
not_executed: 0
live_observed_results: 5
live_independent_results: 0
boundary_activation_count_expected: 3
boundary_activation_count_observed: 3
routine_followup_activation_count_expected: 0
routine_followup_activation_count_observed: 0
new_findings: []
publication_impact: READY_FOR_PUBLICATION_AUDIT
```

AOS-F005, AOS-F006, and AOS-F007 remain in the historical session as traceable failures. This regression
adds passing post-fix evidence; it does not erase or rewrite the original observations.
