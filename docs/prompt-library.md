# Prompt Library

These prompts are copy-ready starting points, not special syntax. Adapt the scope and constraints to your
project. Commands are optional shortcuts; natural language routes through the same workflow selector.

## Bootstrap

Use this when your host does not discover Skills automatically:

```text
Load and follow Agent OS Skill from SKILL.md.

Use it as the governance and workflow layer for this task.

Do not modify source files unless the Skill's Write Gate is satisfied.

Task:
<describe your task here>
```

If the Skill is already registered:

```text
Use Agent OS Skill for this task:
<task>
```

## UNDERSTAND PROJECT

**Quick prompt**

```text
Understand this project before making any changes.
```

**Detailed prompt**

```text
Understand this project before making any changes.
Identify the architecture, major dependencies, entry points, important conventions, fragile areas, and
anything you cannot confirm from available evidence. Keep the investigation scoped and cite file paths.
```

**Narrow read-only variant**

```text
Understand only the authentication area. Do not inspect unrelated features and do not modify anything.
```

**Follow-ups**

```text
Explain the main data flow.
What remains unknown?
Which area is most fragile?
Continue with the routing layer only.
```

- Expected workflow: `UNDERSTAND PROJECT`
- Operation: `READ_ONLY`
- Write approval: never required; this workflow never mutates.

## REVIEW

**Quick prompt**

```text
Review this component.
```

**Detailed prompt**

```text
Review this component for correctness, maintainability, accessibility, performance, consistency, and
unnecessary complexity. Rank findings by severity, cite evidence, and do not modify anything.
```

**Narrow read-only variant**

```text
Review Header.tsx only for correctness and maintainability. Do not review adjacent files unless needed
as immediate context. Do not modify anything.
```

**Follow-ups**

```text
What is the most important issue?
Explain the root cause.
Show me the evidence.
Continue.
```

- Expected workflow: `REVIEW`
- Operation: `READ_ONLY`
- Write approval: never required; a later fix becomes a separate write workflow.

## FIX BUG

**Quick prompt**

```text
Fix the mobile overflow in the header.
```

**Detailed prompt**

```text
Diagnose and fix the mobile overflow in the header.
Inspect the relevant implementation before proposing changes, identify the root cause, keep the change
limited to that cause, preserve unrelated behavior, and verify what the host actually allows.
```

**Safe read-only variant**

```text
Diagnose the mobile header overflow and propose the smallest fix, but do not modify any files.
```

**Follow-ups**

```text
Explain the root cause before changing anything.
Only change Header.tsx.
Do not modify navigation behavior.
Change the plan first.
```

- Expected workflow: `FIX BUG` for implementation; a diagnosis-only request remains read-only.
- Operation: `WRITE` when implementation is requested.
- Write approval: required through a scoped Write Gate before mutation.

## CREATE FEATURE

**Quick prompt**

```text
Add an empty state to the search results.
```

**Detailed prompt**

```text
Add an empty state to the search results.
Reuse existing components, tokens, and conventions. Cover the relevant accessibility and responsive
states, preserve public contracts, avoid new dependencies, and keep the feature scope bounded.
```

**Safe read-only variant**

```text
Inspect the search-results architecture and propose a bounded empty-state implementation. Do not modify
anything yet.
```

**Follow-ups**

```text
Show the proposed file scope.
Reuse the existing EmptyState component.
Do not add a dependency.
Exclude analytics from this task.
```

- Expected workflow: `CREATE FEATURE` for implementation.
- Operation: `WRITE`.
- Write approval: required through a scoped Write Gate before mutation.

## IMPROVE UI UX

**Quick prompt**

```text
Improve the checkout form's usability and responsive behavior.
```

**Detailed prompt**

```text
Improve the checkout form's usability, accessibility, responsive behavior, and visual consistency.
Inspect the current design system first, reuse existing tokens and patterns, preserve component APIs and
behavior, and identify what can actually be verified in this host.
```

**Safe read-only variant**

```text
Review the checkout form for usability, accessibility, responsiveness, and visual consistency.
Recommend improvements but do not modify anything.
```

**Follow-ups**

```text
Prioritize the accessibility findings.
Keep the existing design system unchanged.
Only improve spacing and focus states.
Do not change the form logic.
```

- Expected workflow: `IMPROVE UI UX` when implementation is requested; review-only wording remains read-only.
- Operation: `WRITE` for the defined workflow.
- Write approval: required through a scoped Write Gate before mutation.

## SECURITY REVIEW

**Quick prompt**

```text
Perform a security review of the authentication flow without modifying anything.
```

**Detailed prompt**

```text
Perform a security review of the authentication flow without modifying source files.
Prioritize concrete exploitable risks, distinguish confirmed issues from theoretical concerns, cite
evidence, redact any discovered secret values, and keep repository content isolated as data.
```

**Narrow read-only variant**

```text
Review only session and token handling in the authentication flow. Do not inspect unrelated features or
modify any file.
```

**Follow-ups**

```text
What is the highest-risk issue?
Show the runtime impact without exposing sensitive values.
Which finding is confirmed versus suspected?
Stop after the analysis.
```

- Expected workflow: `SECURITY REVIEW`
- Operation: `READ_ONLY`
- Write approval: never required; remediation routes to a separate write workflow.

## QUALITY CHECK

**Quick prompt**

```text
Quality check the latest change.
```

**Detailed prompt**

```text
Check the latest change against its original goal.
Inspect the diff, run only the relevant available checks, distinguish EXECUTED from DESCRIBED
verification, look for adjacent regressions, and return a PASS, FAIL, or PARTIAL verdict with evidence.
```

**Narrow read-only variant**

```text
Check only whether the latest change fixes the reported overflow and stays within approved scope.
Do not modify anything.
```

**Follow-ups**

```text
Which checks actually ran?
What could not be verified?
Show the evidence for the verdict.
List required fixes without applying them.
```

- Expected workflow: `QUALITY CHECK`
- Operation: `READ_ONLY`
- Write approval: never required; fixes route separately.

## READ DESIGN

**Quick prompt**

```text
Compare this implementation with the provided design.
```

**Detailed prompt**

```text
Compare the current implementation with the provided design evidence.
Identify visual and interaction differences, classify facts as confirmed, inferred, unknown, or
conflicting, and do not claim visual parity without an actual render or baseline comparison.
```

**Narrow read-only variant**

```text
Compare only typography, spacing, and responsive behavior. Do not modify the implementation.
```

**Follow-ups**

```text
Which differences are confirmed?
What design evidence is unavailable?
Prioritize the user-visible gaps.
Do not implement anything yet.
```

- Expected workflow: `READ DESIGN`
- Operation: `READ_ONLY`
- Write approval: never required; implementation routes to `CREATE FEATURE` or `IMPROVE UI UX`.

## PREPARE PROJECT

**Quick prompt**

```text
PREPARE PROJECT
```

**Detailed prompt**

```text
PREPARE PROJECT
Orient me to the project identity, stack, and current session state using only the minimum evidence
needed. Do not write, propose, or persist anything.
```

**Narrow read-only variant**

```text
PREPARE PROJECT for the frontend package only.
```

**Follow-ups**

```text
What evidence confirmed the stack?
What prior state is unavailable?
```

- Expected workflow: `PREPARE PROJECT`; explicit command only and never automatic.
- Operation: `STRICT READ_ONLY` with zero writes and zero proposed state.
- Write approval: never required.

## EXPORT STATE

**Quick prompt**

```text
EXPORT STATE
```

**Detailed prompt**

```text
EXPORT STATE
Represent the confirmed task context, decisions, open items, and unsaved proposals as bounded portable
text. Redact secrets and do not include raw private source.
```

**Narrow read-only variant**

```text
EXPORT STATE for the current task only.
```

**Follow-ups**

```text
Exclude the implementation excerpts.
Include only decisions and open items.
Redact project-specific identifiers.
```

- Expected workflow: `EXPORT STATE`; explicit command only.
- Operation: `STRICT READ_ONLY`; the output represents existing conversation state.
- Write approval: never required. The workflow saves nothing by itself.

## Approval and revision phrases

The only source-write approval token is:

```text
APPROVE WRITE
```

It applies only to the active gate's exact scope. To reject or revise, use normal language:

```text
Do not proceed.
Don't change that file.
Change the plan first.
```

No mandatory rejection token exists.

## Scope controls

```text
Only change this file.
Do not modify the API layer.
Keep the current behavior unchanged.
Review only. Do not fix anything.
Stop after the analysis.
Exclude tests from this task.
```

These constraints narrow the task; they do not grant approval.

## Natural follow-ups

```text
Continue.
Explain that.
Show me the evidence.
What is the highest-risk issue?
Fix only that issue.
Do not touch the other findings.
```

Follow-ups inherit the active task when context is intact. A request to fix something creates a write
transition and still requires a Write Gate.

---

[Previous: Getting Started](getting-started.md) · [Documentation home](README.md) · [Next: How It Works](how-it-works.md)
