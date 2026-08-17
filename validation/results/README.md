# Machine-Readable Evidence Results

New machine-readable evidence records belong under this directory. Historical Markdown evidence under
`validation/sessions/` remains unchanged and authoritative for the sessions it records.

## Canonical path

```text
validation/results/<run_id>/attempt-<NN>.json
```

- `run_id`: `YYYYMMDD-<test-id-slug>-<model-slug>-<host-slug>`
- Attempts begin at `01` and use at least two digits.
- Model and host slugs derive from exact IDs, not grouping classes.
- The JSON record's `run_id`, `attempt`, and `date` must match its path.

The normative contract is `validation/schemas/evidence-result.schema.json`. Validate records with the
optional maintainer tool:

```bash
python3 validation/tools/validate_evidence.py validation/results
```

Running Agent OS Skill does not require Python or this validator.

Reference files under `validation/tools/fixtures/` are synthetic validator fixtures, not behavioral
evidence, and must never be aggregated as results.

## Invalid runs

Paths under `validation/results/` are reserved for valid runs only. A protocol-invalid run never
produces a result record here; it is recorded under `validation/invalid-runs/` instead.
