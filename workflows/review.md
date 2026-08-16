# Workflow: Review

Intent: REVIEW | Read/Write: READ_ONLY | Typical risk: low-medium
Policies loaded: scope-control.md, evidence.md
Triggers on requests like: "review this code", "audit this component", "what's wrong with this file",
"check this for issues", "is this good quality".

## Purpose
Produce an honest, evidence-based review of the requested scope: bugs, maintainability problems,
accessibility gaps, obvious security concerns, and design/consistency issues. Review never becomes a fix
on its own — see Guardrails.

## Steps

1. Confirm scope: exact file(s), component, or area to review. Do not silently review more than asked.
2. Read the relevant code and its immediate context (types, tests, callers) — enough to judge
   correctness and impact, not the whole repository unless the request is repo-wide.
3. Evaluate against categories relevant to the scope (skip categories that do not apply):
   - Correctness / logic bugs
   - Maintainability and structure
   - Accessibility (keyboard, labels, contrast, focus, screen-reader concerns)
   - Obvious security concerns (see `workflows/security-review.md` for a dedicated deep pass)
   - Consistency with the rest of the codebase (naming, patterns, duplication)
   - Performance red flags (obvious, not micro-optimization speculation)
4. For every finding, capture: severity (Critical/High/Medium/Low/Info), file:line, evidence, impact, and
   a concrete recommendation. No finding without evidence.
5. Do not modify any file during a review. If the user wants fixes applied, that is a separate WRITE
   workflow (`workflows/fix-bug.md`, `workflows/improve-ui-ux.md`, etc.) with its own Write Gate.
6. Present findings as a table or list, most severe first. If nothing significant was found, say so
   plainly rather than inventing minor nitpicks to fill space.

## Output shape
Findings table (Severity | File:Line | Evidence | Impact | Recommendation) plus the standard completion
report. State changed = unchanged for everything; "Improvement ideas" may list follow-up work.

## Guardrails
- "Review this" must never silently become "I fixed this." If a fix looks trivial and obviously desired,
  propose it and route through the Write Gate — do not apply it inline.
- Distinguish confirmed problems (you saw it break, or it is unambiguous from reading the code) from
  suspected ones (looks risky, not proven) — label suspected findings as such.
- Do not pad the review with restated code; cite file:line instead of pasting large blocks.
