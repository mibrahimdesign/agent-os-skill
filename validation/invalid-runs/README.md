# Invalid Runs

This directory is **audit-only**. It records protocol-invalid validation runs that are excluded from
model evidence. Nothing here is evidence of model behavior.

## Run validity vs model result

Two independent properties are distinguished:

- **MODEL RESULT** (`PASS | PARTIAL | FAIL | BLOCKED | NOT_EXECUTED`) describes agent behavior in a
  *valid* experiment.
- **RUN VALIDITY** (`VALID | INVALID`) describes whether the experiment itself was fair.

A protocol-invalid event invalidates the experiment. It is not a statement about the model and is
never expressed as a canonical model result. No sixth result state exists or is introduced.

## Invalidation events

A run is protocol-invalid when any of the following occurs:

- evaluator coaching of the live agent;
- wrong frozen task text supplied;
- corrupted or mis-delivered approval events;
- the live agent gains access to evaluator-only material (checker source, fixture manifest, rubric,
  roadmap, private memory);
- workspace isolation breach before or during the run;
- material transcript capture failure;
- the canonical fixture is used or mutated instead of the isolated scratch workspace.

## Guarantees

A protocol-invalid run:

- is never recorded as MODEL FAIL, ENVIRONMENT BLOCKED, or NOT_EXECUTED;
- produces no canonical evidence-result record under `validation/results/`;
- never contributes to PASS, PARTIAL, FAIL, or BLOCKED counts, compatibility claims, or
  LIVE_OBSERVED / LIVE_INDEPENDENT evidence claims;
- is preserved for auditability in the ledger and, where retained, its transcript.

`NOT_EXECUTED` remains reserved for scenarios that never started. `BLOCKED` remains reserved for
environmental prevention in an otherwise valid run. Neither may be used to represent an invalid run.

## Representation

1. **No result record.** No `validation/results/<run_id>/` entry is created for an invalid run.
2. **Ledger entry.** Append one entry to `LEDGER.json` (append-only; never edit or remove entries).
3. **Transcript.** If retained, store the sanitized transcript at
   `validation/invalid-runs/<run_id>/attempt-01.md`, headed by an evaluator-added banner:
   `INVALID RUN — EXCLUDED FROM EVIDENCE`, naming the invalidation reason and the ledger entry.
   The banner is additive metadata; live messages are never rewritten. Standard sanitization and
   prohibited-content rules apply. This path cannot satisfy the canonical `transcript_ref` pattern
   in `validation/schemas/evidence-result.schema.json`, so no canonical result can ever reference an
   invalid-run transcript.

## Ledger entry format

```json
{
  "run_id": "...",
  "test_id": "AOS-Txxx",
  "date": "YYYY-MM-DD",
  "invalidation_reason": "...",
  "protocol_violation": "COACHING | WRONG_TASK | APPROVAL_CORRUPTION | EVALUATOR_MATERIAL_EXPOSURE | ISOLATION_BREACH | CAPTURE_FAILURE | FIXTURE_MISUSE",
  "transcript_retained": true,
  "transcript_path": "validation/invalid-runs/<run_id>/attempt-01.md",
  "model_result_excluded": true,
  "recorded_by": "...",
  "notes": "..."
}
```

## Evaluator termination

- **ET-1 (valid intentional termination):** the protocol remained valid (no coaching, isolation
  intact, capture intact, correct task) and the evaluator intentionally stopped the run after
  sufficient behavior was observed. This is a *valid* run and may be recorded as a canonical result
  (typically PARTIAL) under the rubric's evaluator-termination applicability clause, with
  `deviation.occurred: true` and notes stating the termination point.
- **ET-2 (invalid termination):** termination caused by a protocol violation (coaching, capture
  failure, isolation breach, wrong task, corrupted approvals). This follows the invalid-run contract
  above — ledger plus retained transcript — and is never recorded as PARTIAL or any other model
  result.

## Aggregation

Invalid-run ledger entries and their transcripts are audit-only and excluded from every evidence
metric. Only records under `validation/results/` are eligible for aggregation. Generated
compatibility and dashboard views (0.2.1) must read `validation/results/` only and must never read
this directory as evidence input.
