# Validation Status

Current as of 2026-08-16. Counts below distinguish test results from evidence strength.

| Item | Current state |
|---|---|
| Skill Version | `0.1.1-beta` |
| Product Phase | Field Validation |
| Behavior Count | 11 (`AOS-B001`-`AOS-B011`) |
| Tests Defined | 27 (`AOS-T001`-`AOS-T027`) |
| Tests Self Simulated | 20 |
| Tests with Live Observed Evidence | 23 |
| Recorded Live Observed Results | 28 (repeated regression runs remain separate evidence) |
| Tests Live Independent | 0 |
| Field-Confirmed Tests | 17 distinct tests |
| Tests Without Any Execution Evidence | 2 (`AOS-T021`, `AOS-T025`) |
| Critical Failures | 0 observed |
| High Failures | 0 observed |
| Cross-Model Status | `SINGLE_MODEL` |
| Cross-Host Status | `SINGLE_HOST` |

The 20 historical same-agent simulations remain `SELF_SIMULATED`; they are not upgraded by later live
work. Separate sessions produced live evidence for 23 distinct tests and 28 recorded `LIVE_OBSERVED`
results, including 17 distinct PASS results that meet the definition of `FIELD_CONFIRMED` in
`validation/EVIDENCE_MODEL.md`. Repeated results preserve the evidence trail instead of replacing older
failures. AOS-T013 and AOS-T014 have self-simulated evidence but no live execution; AOS-T021 and AOS-T025
have no execution evidence.

## Core candidates

- CC-1 — formal evaluation harness: `NEEDS_MORE_EVIDENCE`
- CC-2 — role handoff for independent verification: `PROPOSED`
- CC-3 — deterministic risk escalation criteria: `PROPOSED`
- CC-4 — portable project state format: `NEEDS_MORE_EVIDENCE`
- CC-5 — approval scope retention after interruption: `NEEDS_MORE_EVIDENCE`

## Behaviors closest to Core readiness

The ten G1-G10 governance behaviors have historical `LEVEL 2 — SELF-SIMULATED` evidence plus varying
live evidence recorded in the session artifacts. AOS-B011 Active Skill Focus has targeted `LEVEL 3 —
LIVE OBSERVED` evidence: AOS-T022/T023/T024/T026/T027 passed after the instruction fix, while the original
failures remain preserved. AOS-T025 scope-growth coverage is still unexecuted. AOS-B001 and AOS-B003
still need the AOS-T021/CC-5 field scenario; every behavior needs cross-model and cross-host evidence.

## Version position

Keep the public version at `0.1.1-beta`. The unversioned beta work now includes the AOS-B011 activation
UX refinement without changing G1-G10. A later release decision should remain evidence-driven;
`NO RELEASE NEEDED` remains a valid outcome.
