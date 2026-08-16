# Workflow: Fix Bug

Intent: FIX_BUG | Read/Write: WRITE | Typical risk: medium (raise to high if the fix touches auth,
payments, a public API, or a shared component)
Policies loaded: scope-control.md, write-safety.md, evidence.md
Triggers on requests like: "fix this bug", "this is broken", "fix the responsive issue in this
component", "why is X failing and can you fix it".

This is a production-quality workflow. Follow every step in order; do not jump from request to mutation.

## Sequence

```
User Request
  -> Understand Problem
  -> Inspect Relevant Evidence
  -> Determine Root Cause
  -> Define Scope
  -> Prepare Change Plan
  -> WRITE GATE
  -> User Approval
  -> Implement
  -> Verify
  -> Review Changed Scope
  -> Completion Report
```

## Steps

1. Understand the problem. Restate what is broken and the expected behavior in one or two sentences. If
   the report is vague ("it's broken"), ask for the minimum detail needed (what happens vs. what should
   happen) rather than guessing at symptoms.
2. Inspect relevant evidence. Read the implicated code, its tests (if any), and anything that calls or
   depends on it. Reproduce the problem if the environment allows it (EXECUTED); otherwise reason from
   the code and say so (DESCRIBED).
3. Determine root cause — not just the symptom. State the actual mechanism causing the bug, with
   file:line evidence. If multiple plausible causes exist, say which is most likely and why, or ask.
4. Define scope. Name exactly which file(s) need to change. Apply `policies/scope-control.md`: nothing
   wider than what fixing the root cause actually requires.
5. Prepare a change plan: the smallest correct change, plus what must NOT change (behavior, public
   contracts, unrelated styling, etc.).
6. Present the WRITE GATE (`templates/write-gate.md`) and stop.
7. Wait for the literal `APPROVE WRITE` reply. Anything else is not approval — see
   `policies/write-safety.md`.
8. Implement exactly the approved scope. Smallest diff that correctly fixes the root cause.
9. Verify: run whatever check is actually possible (build, test, lint, manual trace) and label it
   EXECUTED or DESCRIBED. Never claim a test passed without having run it.
10. Review the changed scope once more against the original problem statement and against
    `policies/scope-control.md` (nothing extra crept in).
11. Produce the completion report.

## Output shape
Root cause explanation -> Write Gate -> (after approval) diff summary -> verification results ->
`templates/completion-report.md`.

## Guardrails
- Never patch a symptom you cannot explain; find the mechanism first.
- Never expand the fix into a refactor of nearby code "while you're in there" without a separate,
  explicitly approved scope addition.
- If the user rejects or does not approve the gate, make no source change and say so plainly.
- If verification capability is unavailable, say exactly what should be run and by whom, and mark the
  report accordingly — do not claim a pass.
