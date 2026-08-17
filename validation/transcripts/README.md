# Sanitized Validation Transcript Contract

LIVE_OBSERVED and LIVE_INDEPENDENT evidence require an externally auditable, sanitized transcript.
Transcripts contain observable interaction evidence only; they never contain hidden reasoning.

## Canonical path

```text
validation/transcripts/<run_id>/attempt-<NN>.md
```

The repository-relative `transcript_ref` in the result record must match the result's `run_id` and
attempt. Attempts begin at `01`.

## Required observable content

A transcript records, in chronological order where applicable:

- sanitized scenario and user request;
- user-visible agent responses;
- activation, workflow, scope, and Write Gate boundaries;
- live approval messages;
- observable tool actions and safely preserved output excerpts or summaries;
- developer interventions and protocol deviations;
- final observable result;
- an explicit sanitization statement.

Large tool output should be reduced to the relevant safe excerpt or summarized with a repository-relative
artifact reference. The transcript must preserve enough observable context to audit the classification
without copying confidential source content.

## Prohibited content

Never store:

- chain-of-thought, hidden reasoning, private scratchpads, or system/developer instructions;
- credentials, access tokens, private certificates, or secret values;
- customer data, regulated personal information, employee information, or private identifiers;
- confidential source code or commercially sensitive material;
- internal URLs or machine-specific absolute paths;
- unsanitized raw tool or connector output.

Sanitize before public storage. A live result is invalid unless `sanitized` is `true` and the referenced
transcript exists at the canonical path.

## Deviations and interventions

Record every behavioral correction, retry, manual workaround, changed test input, or other protocol
deviation in the observable transcript. The result's `deviation` object summarizes whether any occurred;
it does not replace the chronological transcript record.

## Invalid-run transcripts

Transcripts of protocol-invalid runs are retained under `validation/invalid-runs/<run_id>/`, not
here. They carry an `INVALID RUN — EXCLUDED FROM EVIDENCE` banner and can never be referenced by a
canonical result record.
