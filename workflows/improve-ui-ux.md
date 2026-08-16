# Workflow: Improve UI/UX

Intent: IMPROVE_UI_UX | Read/Write: WRITE | Typical risk: low-medium
Policies loaded: scope-control.md, write-safety.md, evidence.md
Triggers on requests like: "improve the styling of...", "make this more accessible", "clean up the
spacing/hierarchy of...", "fix the responsive issue in...".

## Steps

1. Confirm scope: the exact component/view/flow to improve, and what "improve" means here (visual
   hierarchy, spacing, accessibility, responsiveness, clarity — ask if genuinely unclear).
2. Inspect the current implementation and, if the project has one, its existing design system/tokens —
   reuse existing patterns rather than inventing one-off styles.
3. Identify concrete problems with evidence (file:line, and a plain description of what's wrong: cramped
   spacing, missing focus state, broken layout at a breakpoint, etc.).
4. Plan changes that preserve existing behavior and public contracts (component props, routes, selectors
   other code depends on) unless the user explicitly asked to change them.
5. Present the WRITE GATE and stop for `APPROVE WRITE`.
6. Implement within scope. Prefer existing tokens/variables over new hardcoded values.
7. Verify what is checkable: does it build, do existing tests still pass, and — if you can actually
   render or screenshot the result — does it look right. A visual "looks correct" claim without a
   render/screenshot must be labeled DESCRIBED, not asserted as fact.
8. Produce the completion report.

## Guardrails
- Do not change component behavior, public props, or routes while doing a visual/UX improvement unless
  explicitly requested.
- Do not claim visual parity or "looks correct" without actual render/screenshot evidence; say so
  honestly when that evidence is unavailable.
- Keep accessibility and responsive behavior intact for states outside the immediate focus of the change.
