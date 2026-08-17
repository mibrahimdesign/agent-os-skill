# Test Result Recording Contract

New machine-readable results are governed by the normative JSON Schema:

```text
validation/schemas/evidence-result.schema.json
```

Canonical storage:

```text
validation/results/<run_id>/attempt-<NN>.json
validation/transcripts/<run_id>/attempt-<NN>.md
```

See `validation/results/README.md` and `validation/transcripts/README.md` for naming and transcript
requirements. Use `STATIC_REVIEW`, never `STATIC`. New NOT_EXECUTED JSON records use
`evidence_level: null`.

The YAML shape below is retained as the historical Markdown session format. Existing files under
`validation/sessions/` remain unchanged and are not required to validate against the new JSON Schema.

```yaml
test_id:                 # AOS-Txxx
behavior_ids:            # [AOS-Bxxx, ...] — registry behaviors exercised
skill_version:           # e.g. 0.1.2-beta
date:                    # YYYY-MM-DD

host:                    # actual host identity, or N/A
host_class:              # FULL_CODING_HOST | LIMITED_CODING_HOST | EMBEDDED_CHAT_HOST | OTHER | N/A
model:                   # actual model name/family, "unknown", or N/A
model_class:             # STRONG_REASONING | CODING_FOCUSED | SMALL_OR_LOCAL | OTHER | N/A

operating_mode:          # FULL | LIMITED | EMBEDDED | N/A

capabilities:            # relevant capability states for this run, or N/A

workflow:                # workflow/policy in play, or N/A

result:                  # PASS | FAIL | PARTIAL | BLOCKED | NOT_EXECUTED
evidence_level:          # STATIC_REVIEW | SELF_SIMULATED | LIVE_OBSERVED | LIVE_INDEPENDENT | N/A
validation_confidence:   # UNVALIDATED | LOW | MEDIUM | HIGH

expected:                # one line copied from the test definition
observed:                # what actually happened; N/A for NOT_EXECUTED
evidence:                # direct supporting evidence, sanitized; N/A for NOT_EXECUTED

developer_interventions: # non-negative count; explain interventions in notes; N/A if not executed

scope_violation:         # yes | no | N/A
false_claims:            # yes | no | N/A; never reproduce secrets
approval_behavior:       # observed approval behavior, or N/A
verification_behavior:   # observed EXECUTED vs DESCRIBED behavior, or N/A

failure_category:        # FC-01 through FC-10 from validation/FAILURE_TAXONOMY.md, or N/A
finding_ids:             # [AOS-Fxxx, CC-x, ...], or []

notes:                   # rationale, intervention details, limitations, or N/A
```

## Allowed `result` values

```text
PASS           — expected behavior was observed, with cited evidence
FAIL           — expected behavior was not observed; a defect exists
PARTIAL        — expected behavior mostly held, but with a real gap worth recording (not a full FAIL)
BLOCKED        — the test could not be meaningfully run in this environment; not the same as NOT_EXECUTED
NOT_EXECUTED   — defined but never run or simulated; the honest default until evidence exists
```

Never invent a `PASS`. Migrate the legacy `execution_kind: SELF_SIMULATED_SINGLE_PASS` label to
`evidence_level: SELF_SIMULATED`. It must never be reported as `LIVE_OBSERVED`, `LIVE_INDEPENDENT`,
field-confirmed, cross-model, or cross-host evidence.

Use explicit `N/A` in historical Markdown when a field has no value for the scenario. New JSON uses null
only where the normative schema permits it, including `evidence_level: null` for NOT_EXECUTED and null
model or host identifiers/versions when they cannot be established. Never invent placeholder metadata.
Use `[]` for an applicable list with no items.
