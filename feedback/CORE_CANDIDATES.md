# Core Candidates

This file tracks behaviors observed during beta usage that may eventually become formal, permanent
requirements of a future Agent OS Core. A candidate here is a hypothesis under evaluation, not an active
rule. Nothing in `SKILL.md` or `policies/` changes because of an entry here alone — see the pipeline
below.

## Pipeline

```
Feedback -> Classification -> Reproduction -> Evidence -> Impact Analysis -> Candidate Change -> Testing -> Decision
```

A candidate needs reproducible evidence (not a single anecdote) and an impact analysis before it can move
past `PROPOSED`. **A candidate does not become `ACCEPTED` merely because it was requested frequently** —
frequency is one input among several (below), and severity/security/reproducibility evidence can outweigh
a low-frequency-but-dangerous report. Testing means running it against `tests/semantic-tests.md` (plus any
new scenario it implies) across more than one host and more than one model before `ACCEPTED`.

## Evidence dimensions

Every candidate is evaluated across these, filled in as evidence accumulates (not required to be complete
to reach `PROPOSED` — maintainers enrich during triage, reporters are not required to fill every field):

```
Frequency                  — how many independent feedback reports/sessions raised this
Severity                   — CRITICAL | HIGH | MEDIUM | LOW | UX (tests/behavior-registry.md-style)
Reproducibility            — did it reproduce consistently, or was it a one-off
Security Impact            — does this touch approval, secrets, instruction isolation, scope
Developer Friction         — how much it slowed or annoyed real usage, independent of correctness
Cross-Host Evidence        — how many distinct host types confirmed the pattern
Cross-Model Evidence       — how many distinct model classes confirmed the pattern
Workflow Impact            — which workflows are affected
Backward Compatibility     — would adopting this change existing documented behavior for someone
  Impact                     already relying on it
```

## Statuses
`PROPOSED` — recorded, not yet evaluated. `TESTING` — being evaluated against real scenarios.
`ACCEPTED` — validated, ready to fold into a future release. `REJECTED` — evaluated and declined, with
reason. `NEEDS_MORE_EVIDENCE` — plausible but not yet backed by enough real usage.

## Feedback decision model

Every feedback item resolves into exactly one of these, with a one-line reason recorded wherever the
feedback itself is logged:

```
FIX_IN_SKILL            — a defect in current governance/workflow text; fixed directly, no candidate needed
DOCUMENTATION_CHANGE    — behavior was correct, wording/docs were unclear
WORKFLOW_CHANGE         — a workflow's steps need adjusting, governance kernel untouched
EXPERIMENT              — worth trying as clearly-labeled EXPERIMENTAL BEHAVIOR before any commitment
CORE_CANDIDATE          — recorded below, goes through the full pipeline
REJECT                  — considered and declined, with reason
NEEDS_MORE_DATA         — plausible but not enough evidence yet to classify further
```

A single feature request, however well-argued, never silently becomes governance — it is routed through
one of the seven outcomes above, on the record.

## Template for new entries

```
Candidate ID:                CC-<number>
Candidate rule:
Source feedback:             <feedback ID(s) or "seed">
Problem:
Frequency:
Severity:
Reproducibility:
Security implications:
Developer friction:
Hosts tested:
Models tested:
Workflows affected:
Evidence summary:
Counter evidence:
Compatibility risk:
Status:                       PROPOSED
Decision:                     <filled in when status changes from PROPOSED>
```

## Seed candidates (from initial design and the 2026-08-16 validation pass)

```
Candidate ID:                CC-1
Candidate rule:               A formal eval-scenario harness, one scenario per governance rule, runnable
                              automatically where COMMAND_EXECUTION allows it, instead of relying on
                              self-simulated single-pass review.
Source feedback:             seed
Problem:                     Governance behavior is currently checked by self-simulated single-pass
                              review (see validation/README.md); there is no automated harness to check
                              it stayed compliant across many real runs/hosts/models.
Frequency:                    1 (design-time observation, this validation pass)
Severity:                     MEDIUM — no correctness failure caused, but confidence in "validated" is
                              weaker than it should be without this.
Reproducibility:              N/A (infrastructure gap, not a reproducible bug)
Security implications:        None directly; would improve confidence in existing rules.
Developer friction:           None yet observed; would reduce maintainer effort over time.
Hosts tested:                  0
Models tested:                 0
Workflows affected:            All.
Evidence summary:              Design-time observation; needs real multi-host usage to confirm value.
Counter evidence:              None yet.
Compatibility risk:            Would need to stay host-agnostic (no vendor-specific test runner assumed).
Status:                        NEEDS_MORE_EVIDENCE
Decision:                      —
```

```
Candidate ID:                CC-2
Candidate rule:               A lightweight role-handoff format for hosts that support subagents, so
                              "independent verification" can be more than a same-pass self-check by
                              default when the host allows it.
Source feedback:             seed
Problem:                     Multi-agent/subagent role separation (AOS-B009) is described conceptually
                              but the beta has no structured protocol for it.
Frequency:                    1 (design-time observation)
Severity:                     MEDIUM — affects verification quality/independence claims, not correctness.
Reproducibility:              N/A
Security implications:        Could strengthen review quality for sensitive changes if adopted.
Developer friction:           None yet observed.
Hosts tested:                  0
Models tested:                 0
Workflows affected:            fix-bug, create-feature, improve-ui-ux, quality-check.
Evidence summary:              Design-time observation, based on prior Agent OS team-mode material; not
                              yet validated in this beta's real usage.
Counter evidence:              None yet.
Compatibility risk:            Must degrade cleanly to single-agent sequential execution (already the
                              beta's default per AOS-B009).
Status:                        PROPOSED
Decision:                      —
```

```
Candidate ID:                CC-3
Candidate rule:               A short, explicit list of conditions that always raise risk (auth, payments,
                              public API, permissions, shared/exported components), similar to Agent OS
                              v6's router rule 3, rather than leaving risk classification to judgment
                              alone.
Source feedback:             seed
Problem:                     "Risk" in the Intent Router (SKILL.md §4) is currently a single agent
                              judgment call (low/medium/high) with no fixed criteria list.
Frequency:                    1 (design-time observation)
Severity:                     MEDIUM-HIGH — under-classifying risk on a sensitive change is a real safety
                              gap, even though no concrete failure has been observed yet.
Reproducibility:              N/A
Security implications:        Reduces risk of under-classifying a sensitive change.
Developer friction:           Low if adopted — a short fixed list is easy to follow.
Hosts tested:                  0
Models tested:                 0
Workflows affected:            fix-bug, create-feature, improve-ui-ux, security-review.
Evidence summary:              Ported concept from Agent OS v6 governance baseline; not yet stress-tested
                              in this beta's simplified router.
Counter evidence:              None yet.
Compatibility risk:            Adds a small fixed list to SKILL.md; low compatibility risk. This is the
                              leading candidate for the next validation round — see
                              feedback/CORE_READINESS.md.
Status:                        PROPOSED
Decision:                      —
```

```
Candidate ID:                CC-4
Candidate rule:               An optional, portable per-project state file format (decisions, session
                              summary, protected contracts) that any host could read/write, without
                              requiring a specific filesystem layout.
Source feedback:             seed
Problem:                     The beta has no persistent per-project memory/state layer (equivalent to the
                              v6 Project Overlay) — each task starts from conversation context only, or
                              whatever EXPORT_STATE was used to carry forward.
Frequency:                    1 (design-time observation)
Severity:                     LOW-MEDIUM — a friction/capability gap, not a governance failure; the beta
                              is honest about the absence (state honesty still holds without it).
Reproducibility:              N/A
Security implications:        Would need its own secret-handling rules (mirroring policies/secrets.md).
Developer friction:           Likely real over long sessions/multiple sessions on the same project; not
                              yet measured.
Hosts tested:                  0
Models tested:                 0
Workflows affected:            understand-project, prepare-project, export-state.
Evidence summary:              Directly inherited concept from Agent OS v5.8/v6 governance material; value
                              for THIS beta's smaller scope is still unproven — deliberately deferred per
                              the beta's scope boundary (see root README "Current Beta Scope").
Counter evidence:              None yet.
Compatibility risk:            Must not require a specific filesystem or vendor mechanism.
Status:                        NEEDS_MORE_EVIDENCE
Decision:                      —
```

```
Candidate ID:                CC-5
Candidate rule:               Require the agent to briefly restate the currently-approved Write Gate
                              scope before resuming work on it after a long gap or context compaction,
                              rather than silently trusting that GRANTED approval state carried forward
                              correctly.
Source feedback:             seed (raised while designing AOS-T007 / the write-safety.md §5 beta note
                              during the 2026-08-16 validation pass)
Problem:                     "Approval persists for unchanged, already-approved scope"
                              (policies/write-safety.md §5) is convenient but unverified over long or
                              interrupted sessions — a model could drift on what was actually approved
                              without a live re-check, especially after context compaction/summarization.
Frequency:                    1 (design-time observation during this validation pass)
Severity:                     MEDIUM — a plausible path to writing outside truly-approved scope without
                              any instruction-isolation or approval-spoofing failure being involved.
Reproducibility:              Not yet reproduced; needs a real long/interrupted session to test.
Security implications:        Directly touches AOS-B003 Explicit Write Approval; worth prioritizing.
Developer friction:           A restatement step adds minor friction on every resumed write task.
Hosts tested:                  0
Models tested:                 0
Workflows affected:            fix-bug, create-feature, improve-ui-ux.
Evidence summary:              Design-time observation; write-safety.md §5 already labels the underlying
                              rule BETA BEHAVIOR pending exactly this kind of evidence. Required field
                              evidence: a long continuous session, a context-compacted session, and an
                              interrupted/resumed session where approved unchanged scope is retained,
                              new scope is re-gated, stale approval does not expand, and approval is not
                              needlessly repeated.
Counter evidence:              None yet.
Compatibility risk:            Low; an added confirmation step, not a removed one.
Status:                        NEEDS_MORE_EVIDENCE
Decision:                      NEEDS_MORE_DATA — AOS-T021 is defined but NOT_EXECUTED; no qualifying
                              live approval-retention session exists.
```
