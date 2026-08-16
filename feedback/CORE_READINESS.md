# Core Readiness Tracker

This is a readiness tracker, not a specification and not Agent OS Core. It records evidence per behavior
so future Core extraction decisions are based on observed stability rather than release number or prose
confidence. Evidence and maturity terms are defined in `validation/EVIDENCE_MODEL.md`.

## Extraction states

- `NOT_READY` — insufficient or absent evidence.
- `EARLY_EVIDENCE` — static or self-simulated evidence exists, but live portability is unproven.
- `PROMISING` — live evidence exists and no unresolved material failure currently blocks progression.
- `CANDIDATE_FOR_CORE` — repeated intended-environment evidence supports formal extraction review.
- `BLOCKED` — an unresolved material failure or dependency prevents responsible extraction.

`CANDIDATE_FOR_CORE` is not automatic acceptance. This tracker does not use `READY_FOR_CORE`.

## Per-behavior readiness — 2026-08-16

| Behavior | Current Validation Level | Cross-Model Evidence | Cross-Host Evidence | Known Failures | Developer Feedback | Core Candidates | Confidence | Core Extraction Status |
|---|---|---|---|---|---|---|---|---|
| AOS-B001 Scope Lock | `LEVEL 2 — SELF-SIMULATED`; live evidence recorded | `SINGLE_MODEL` | `SINGLE_HOST` | Long/interrupted scope retention untested | Live results exist; portability unproven | CC-5 | LOW | `EARLY_EVIDENCE` |
| AOS-B002 Read Before Write | `LEVEL 2 — SELF-SIMULATED`; live evidence recorded | `SINGLE_MODEL` | `SINGLE_HOST` | No unresolved behavior-specific failure recorded | Live results exist; portability unproven | — | LOW | `EARLY_EVIDENCE` |
| AOS-B003 Explicit Write Approval | `LEVEL 2 — SELF-SIMULATED`; live evidence recorded | `SINGLE_MODEL` | `SINGLE_HOST` | Approval persistence after interruption untested | Live results exist; portability unproven | CC-5 | LOW | `EARLY_EVIDENCE` |
| AOS-B004 Instruction Isolation | `LEVEL 2 — SELF-SIMULATED`; live evidence recorded | `SINGLE_MODEL` | `SINGLE_HOST` | No unresolved behavior-specific failure recorded | Live results exist; portability unproven | — | LOW | `EARLY_EVIDENCE` |
| AOS-B005 Capability Honesty | `LEVEL 2 — SELF-SIMULATED`; live evidence recorded | `SINGLE_MODEL` | `SINGLE_HOST` | Limited capability-environment coverage | Live results exist; portability unproven | — | LOW | `EARLY_EVIDENCE` |
| AOS-B006 Evidence Before Claims | `LEVEL 2 — SELF-SIMULATED`; live evidence recorded | `SINGLE_MODEL` | `SINGLE_HOST` | AOS-F001 fixed; AOS-F002 remains historical live evidence | Live results exist; portability unproven | — | LOW | `EARLY_EVIDENCE` |
| AOS-B007 State Honesty | `LEVEL 2 — SELF-SIMULATED`; live evidence recorded | `SINGLE_MODEL` | `SINGLE_HOST` | No live EMBEDDED-host test | Live results exist; portability unproven | CC-4 related | LOW | `EARLY_EVIDENCE` |
| AOS-B008 Secret Safety | `LEVEL 2 — SELF-SIMULATED`; live evidence recorded | `SINGLE_MODEL` | `SINGLE_HOST` | Synthetic fixture only | Live results exist; portability unproven | — | LOW | `EARLY_EVIDENCE` |
| AOS-B009 Verification Integrity | `LEVEL 2 — SELF-SIMULATED`; live evidence recorded | `SINGLE_MODEL` | `SINGLE_HOST` | No `LIVE_INDEPENDENT` evidence | Live results exist; portability unproven | CC-2 | LOW | `EARLY_EVIDENCE` |
| AOS-B010 Completion Honesty | `LEVEL 2 — SELF-SIMULATED`; live evidence recorded | `SINGLE_MODEL` | `SINGLE_HOST` | AOS-F002 and AOS-F003 remain historical live findings | Live results exist; portability unproven | — | LOW | `EARLY_EVIDENCE` |
| AOS-B011 Active Skill Focus | `LEVEL 3 — LIVE OBSERVED`; AOS-T025 unexecuted | `SINGLE_MODEL` | `SINGLE_HOST` | AOS-F005/F006/F007 regression-passed; scope-growth scenario unexecuted | Targeted regression 5/5 PASS | — | MEDIUM | `NOT_READY` |

## Additional readiness gaps

| Area | Current state | Evidence needed |
|---|---|---|
| Risk classification determinism | Static review only; CC-3 open | Live failures or friction showing current wording is ambiguous before governance changes are considered. |
| Cross-host persistence / EMBEDDED handling | `SINGLE_HOST` | Live execution in an `EMBEDDED_CHAT_HOST` and a materially different coding host. |
| Smaller/local-model instruction following | `SINGLE_MODEL` | Live execution in `SMALL_OR_LOCAL` under the fair comparison protocol. |
| Approval scope retention | AOS-T021 `NOT_EXECUTED`; CC-5 `NEEDS_MORE_EVIDENCE` | Long continuous, compacted, and interrupted/resumed live sessions with bounded and newly expanded scope. |

## Current honest read

The ten G1-G10 governance behaviors have historical same-agent self-simulated evidence plus varying live
evidence in one model and host class. AOS-B011's targeted boundary/continuity regression passed 5/5;
historical failures remain visible and AOS-T025 remains unexecuted. Cross-model and cross-host status
remain `SINGLE_MODEL` and `SINGLE_HOST`, with no `LIVE_INDEPENDENT` evidence. Core extraction is therefore
not ready. No Core candidate is promoted by this publication update.
