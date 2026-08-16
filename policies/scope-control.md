# Policy: Scope Control

Applies to: every workflow.

1. The task scope is exactly what the user asked for: the named file(s), component(s), route(s), bug, or
   feature. Nothing wider is in scope by default.
2. READ BEFORE WRITE. Inspect the relevant existing implementation before proposing or making a change.
   Do not modify code based on assumption when the source is available to read.
3. If you notice an unrelated problem while working (dead code, a different bug, a style inconsistency),
   do not fix it. Note it under "Improvement ideas" in the completion report instead.
4. Scope expansion is allowed only when the task cannot be correctly completed without it (for example,
   the root cause of a bug lives in a file the user did not name). When this happens:
   - Stop before touching the newly-needed area.
   - State exactly what is being added to scope and why.
   - Fold it into the Write Gate (or a new one) so the user approves the actual files touched.
5. Do not re-request approval for work that stays fully inside an already-approved Write Gate scope.
   Re-gate only when a file, area, or change type outside that scope becomes necessary.
6. When genuinely unsure whether something is in scope, ask one focused question rather than guessing.
   When the ambiguity is minor and low-risk, proceed and state the assumption in the output instead of
   stopping.
