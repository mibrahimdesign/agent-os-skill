# Validation

This folder contains evidence about Agent OS Skill behavior: synthetic fixtures, session records,
protocols, and summaries. The project phase is Field Validation, but no test is field-confirmed until it
meets the explicit rule in `EVIDENCE_MODEL.md`.

```text
validation/
├── EVIDENCE_MODEL.md
├── FAILURE_TAXONOMY.md
├── CROSS_MODEL_PROTOCOL.md
├── CROSS_HOST_PROTOCOL.md
├── STATUS.md
├── fixtures/     synthetic, sanitized test material only
├── sessions/     one file per validation session or explicit NOT_EXECUTED record
├── summaries/    aggregated results with evidence-level counts
└── templates/    comparison summary templates
```

## Methodology honesty

Every session records:

- actual model and vendor-neutral `model_class`;
- actual host and capability-based `host_class`;
- operating mode and relevant capabilities;
- `result`, `evidence_level`, and `validation_confidence` as separate fields;
- developer intervention count;
- observed behavior and sanitized evidence;
- any failure category and related finding IDs.

Allowed results remain `PASS | FAIL | PARTIAL | BLOCKED | NOT_EXECUTED`. Evidence levels are
`STATIC_REVIEW | SELF_SIMULATED | LIVE_OBSERVED | LIVE_INDEPENDENT`. An unexecuted test uses
`evidence_level: N/A` and `validation_confidence: UNVALIDATED`.

The historical label `SELF_SIMULATED_SINGLE_PASS` maps to `evidence_level: SELF_SIMULATED`. The
historical label `LIVE_MULTI_TURN` is not sufficient by itself; a migrated record must state whether the
execution was merely observed (`LIVE_OBSERVED`) or independently evaluated (`LIVE_INDEPENDENT`).

## Current evidence

The repository preserves 20 same-agent, same-context simulated PASS results plus live observed sessions
from one model class and one host class. The targeted AOS-B011 regression passed
AOS-T022/T023/T024/T026/T027; earlier failures remain preserved as historical evidence. Current counts
are maintained in `STATUS.md`.

Cross-model and cross-host validation remain incomplete: the current portability states are
`SINGLE_MODEL` and `SINGLE_HOST`, with no `LIVE_INDEPENDENT` results. Use `CROSS_MODEL_PROTOCOL.md` and
`CROSS_HOST_PROTOCOL.md` for future rounds; do not simulate portability claims.

## Privacy

Nothing under `fixtures/` or `sessions/` may contain private source code, repository content, real
secrets, customer information, personal information, sensitive company information, internal URLs, or
machine-specific paths. Fixtures must be synthetic and labeled. If a real project is used later,
sanitize the saved result before adding it here.
