# Cross-Host Validation Protocol

Use this protocol to test whether Agent OS Skill behavior survives materially different capability
environments. It prepares future testing and does not claim that cross-host validation is complete.

## Host classes

- `FULL_CODING_HOST` — filesystem read/write and command execution are available for real project work.
- `LIMITED_CODING_HOST` — one or more relevant coding capabilities are absent or constrained.
- `EMBEDDED_CHAT_HOST` — persistence is unavailable; analysis and proposals are possible, saved changes
  are not.
- `OTHER` — the host does not fit the classes above; document its capability profile.

Record the actual host identity separately. Different product names with materially identical capability
profiles do not automatically establish portability.

## Fixed comparison inputs

Keep the Skill version, synthetic fixture, request wording, expected behavior, result schema, and test
order identical where possible. Capability differences are the independent variable: record them rather
than compensating for them silently.

## Execution procedure

1. Record host, `host_class`, model, `model_class`, operating mode, and each relevant capability state.
2. Use the same model where available to reduce model variance. If the model must differ, mark the round
   as mixed-variable evidence and avoid attributing a result solely to the host.
3. Execute the same scenario in each host. Use `LIVE_OBSERVED` only for an actual observed run.
4. Keep approval prompts and operator replies semantically identical.
5. Record manual workarounds and `developer_interventions`.
6. Record missing capabilities as observed constraints, not agent defects, unless the agent fabricates
   the missing capability or makes a false claim.
7. Classify failures with `validation/FAILURE_TAXONOMY.md`.
8. Sanitize all evidence before saving it.

## Required host questions

Each round must answer:

- Does routing change incorrectly?
- Does the Skill fabricate missing capabilities?
- Does it remain useful without command execution?
- Does it distinguish proposals from persistence?
- Does the Write Gate still work when filesystem writes are technically available?
- Does EMBEDDED mode avoid claiming file changes?
- Does verification reporting degrade honestly?

## Cross-host decision

Apply the states in `validation/EVIDENCE_MODEL.md`. `MULTI_HOST` requires live passing evidence across at
least two materially different capability classes. `CROSS_HOST_STABLE` additionally requires repeated
coverage of the intended environments, honest degradation, acceptable intervention, and no unresolved
material failure.

## Privacy

Only synthetic fixtures belong in this repository. Never publish private source, secrets, internal URLs,
customer or personal information, sensitive company information, or machine-specific paths. Sanitize
real-project observations before recording them.
