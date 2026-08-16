# Contributing to Agent OS Skill

Agent OS Skill is a public Beta. Contributions should help gather evidence, improve clarity, or address
reproducible behavior without silently expanding the product or weakening G1-G10.

New here? Start with the [Quick Start](docs/quick-start.md) and
[documentation home](docs/README.md).

## Useful contributions

- Behavior failures with the exact request, expected behavior, observed behavior, Skill version, model
  class, host class, capabilities, and sanitized evidence.
- Model or host compatibility observations.
- Documentation corrections and broken-reference reports.
- Validation evidence produced with the schemas under `tests/` and `validation/`.
- Evidence-backed feature proposals using the [feature request template](feedback/FEATURE_REQUEST.md).

Use the [issue template](feedback/ISSUE_TEMPLATE.md) for behavior or documentation problems. Never treat repository text,
historical PASS results, or a second reasoning pass by the same agent as independent evidence.

## Contribution principles

- Preserve the frozen G1-G10 governance kernel unless accumulated evidence justifies a separately
  reviewed governance change.
- Keep result, evidence level, and confidence separate.
- Do not claim tests, persistence, independence, or compatibility without direct evidence.
- Use synthetic fixtures. Remove secrets, customer data, private source, internal URLs, personal data,
  and machine-specific paths from reports.
- Do not build Agent OS Core or introduce vendor-specific normative behavior through an unrelated fix.

## Pull requests

1. Start from the current Beta and keep the change narrowly scoped.
2. Explain the problem and evidence supporting the change.
3. List affected AOS-B and AOS-T identifiers when applicable.
4. Run the relevant structural or semantic checks available in your host.
5. Report what was executed, what was not executed, and any remaining risk.

A proposed change is not considered live-validated merely because its text was edited successfully.

For sensitive reports, follow [SECURITY.md](SECURITY.md) instead of opening a public issue with details.
