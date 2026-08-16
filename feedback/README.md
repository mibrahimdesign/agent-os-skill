# Feedback

Agent OS Skill is a beta. It is designed to be corrected by real usage, not to be right on the first try.
Your feedback is the primary input for what becomes a future Agent OS Core.

## The simple version (no governance vocabulary required)

If something felt wrong while using the Skill, just describe it in plain language:
- What were you trying to do?
- What did you expect to happen?
- What actually happened?
- Anything that made you lose trust in the output?

That's a complete, useful piece of feedback. Use `ISSUE_TEMPLATE.md` if you want structure, or just write
it in your own words.

## What kinds of feedback are useful

- The agent asked for approval when it clearly didn't need to (annoying, but safe).
- The agent did NOT ask for approval when it probably should have (unsafe — high priority).
- The agent claimed something worked that you later found did not.
- The agent expanded scope beyond what you asked.
- A workflow felt clunky, slow, or confusing to follow.
- The Skill didn't work well with your particular host/agent/model.
- You wanted a workflow that doesn't exist yet (`FEATURE_REQUEST.md`).

## Categories (for structured reports)

| Code | Meaning |
|---|---|
| F1 | Workflow friction — the process was awkward or slow |
| F2 | Missing behavior — something needed didn't exist |
| F3 | Governance problem — a rule was wrong, missing, or contradictory |
| F4 | False positive — the agent blocked/flagged something that was actually fine |
| F5 | False negative — the agent missed something it should have caught |
| F6 | Context problem — the agent loaded too much, too little, or the wrong material |
| F7 | Host compatibility — didn't work well in a specific host/environment |
| F8 | Model compatibility — didn't work well with a specific model |
| F9 | Developer experience — confusing, unclear, or unpleasant to use |
| F10 | Feature request — a new capability or workflow |

## Where feedback goes

```
Feedback
  -> Classification
  -> Reproduction
  -> Evidence
  -> Impact Analysis
  -> Candidate Change
  -> Testing
  -> Decision
```

Feedback does not automatically change governance. A single report — even a good one — is a data point,
not a decision. Every feedback item resolves into one of: `FIX_IN_SKILL`, `DOCUMENTATION_CHANGE`,
`WORKFLOW_CHANGE`, `EXPERIMENT`, `CORE_CANDIDATE`, `REJECT`, or `NEEDS_MORE_DATA` — see
`CORE_CANDIDATES.md` "Feedback decision model" for what each means. Recurring, evidenced patterns become
tracked candidates in `CORE_CANDIDATES.md`, which are then evaluated across frequency, severity,
reproducibility, security impact, and cross-host/cross-model evidence — not popularity alone — before
anything is promoted into `SKILL.md` or a policy file. Overall system readiness for a future Agent OS
Core is tracked separately in `CORE_READINESS.md`.

You are not expected to fill in every field of a structured report yourself — maintainers enrich raw
feedback with severity, reproducibility, and evidence during triage. A plain description (the simple
version above) is a complete, valid submission on its own.

If you can reference specific behavior or test IDs from `tests/behavior-registry.md` /
`tests/semantic-tests.md` (e.g. "this looks like a violation of AOS-B003"), that speeds up triage, but
it is optional — describing what happened in your own words is enough.

## Privacy first

Never include real source code, secrets, credentials, customer data, private repository names, internal
URLs, or machine-specific paths in feedback. Describe the situation generically. If a reproduction
requires code, use a minimal, sanitized, synthetic example.

## How to submit

Use whatever channel the distribution of this Skill provides (repository issues, a shared feedback form,
or direct message to the maintainer). If none is set up yet, keep `ISSUE_TEMPLATE.md` /
`FEATURE_REQUEST.md` filled out locally until a channel exists.

If you want to contribute validation evidence, use a sanitized synthetic scenario and record it with
`tests/test-result-template.md`. Maintainers running model or host comparisons should follow
`validation/CROSS_MODEL_PROTOCOL.md` or `validation/CROSS_HOST_PROTOCOL.md`. A plain-language report is
still useful; contributors do not need to learn the validation vocabulary first.
