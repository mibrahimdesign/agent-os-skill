# Workflow: Quality Check

Intent: QUALITY_CHECK | Read/Write: READ_ONLY | Typical risk: low
Policies loaded: evidence.md
Triggers on requests like: "check the last change", "did that fix actually work", "QC this", "verify
this is good before I ship it".

## Purpose
Independently check a change that was just made (by this agent or otherwise) against the original goal,
without assuming it is correct just because it was written.

## Steps

1. Identify what changed: the specific files/diff in question. If not explicitly given, use the most
   recent relevant change in this task's context.
2. Re-state the original goal the change was supposed to achieve.
3. Check the change against the goal:
   - Does it plausibly do what was asked, based on reading it?
   - Run whatever verification is actually possible (build/lint/tests/manual trace) — EXECUTED if run,
     DESCRIBED if not.
   - Check for obvious regressions in adjacent behavior, not just the target of the change.
   - Check accessibility/responsive/security impact only if relevant to the change.
4. Give a clear PASS / FAIL / PARTIAL verdict with evidence, not just a vibe.
5. If the same agent implemented the change earlier in this task, label this check accordingly — it is a
   self-check, not independent verification (`policies/evidence.md` §6).
6. Do not modify source during a quality check. If a required fix is found, hand off to
   `workflows/fix-bug.md` with its own Write Gate.

## Output shape
PASS/FAIL/PARTIAL verdict, checks table (Check | Mode | Result | Evidence), required fixes if any, plus
the standard completion report.
