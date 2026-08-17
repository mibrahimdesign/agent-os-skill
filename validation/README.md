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
├── schemas/      normative schema for new JSON evidence records
├── results/      new machine-readable records, grouped by run_id and attempt
├── transcripts/  sanitized observable transcripts for live evidence
├── tools/        optional maintainer validation tooling and non-evidence fixtures
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
`STATIC_REVIEW | SELF_SIMULATED | LIVE_OBSERVED | LIVE_INDEPENDENT`. Historical Markdown records retain
`evidence_level: N/A` and `validation_confidence: UNVALIDATED` for unexecuted tests. New JSON records use
`evidence_level: null` for NOT_EXECUTED; null is absence of evidence, not a new evidence level.

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

## New machine-readable evidence

The normative record contract is `schemas/evidence-result.schema.json`. New records use:

```text
validation/results/<run_id>/attempt-<NN>.json
validation/transcripts/<run_id>/attempt-<NN>.md
```

LIVE_OBSERVED and LIVE_INDEPENDENT require a sanitized transcript. The contract and content boundaries
are documented in `results/README.md` and `transcripts/README.md`. Historical Markdown evidence under
`sessions/` and `summaries/` remains unchanged and is not automatically migrated.

Maintainers can validate new records with the dependency-free standard-library tool:

```bash
python3 validation/tools/validate_evidence.py validation/results
```

This script is MAINTAINER_VALIDATION_TOOLING. It validates contract and reference integrity; it does not
decide whether a behavioral PASS is true. Python is not required to load or operate Agent OS Skill.

## Privacy

Nothing under `fixtures/`, `tools/fixtures/`, `results/`, `transcripts/`, or `sessions/` may contain
private source code, real secrets, customer information, personal information, sensitive company
information, internal URLs, or machine-specific paths. Fixtures must be synthetic and labeled. If a
real project is used later, sanitize the saved result and transcript before adding them here.
