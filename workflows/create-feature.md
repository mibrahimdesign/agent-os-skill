# Workflow: Create Feature

Intent: CREATE_FEATURE | Read/Write: WRITE | Typical risk: medium-high (raise if it touches auth,
payments, permissions, or a public contract)
Policies loaded: scope-control.md, write-safety.md, evidence.md
Triggers on requests like: "add a feature that...", "build a new component for...", "implement X".

## Steps

1. Understand the goal in one or two sentences: what the feature should do and for whom.
2. Understand existing architecture and conventions in the relevant area (reuse
   `workflows/understand-project.md` if that context does not already exist) — new code should look like
   it belongs, not like a foreign pattern.
3. Identify what already exists that can be reused (components, utilities, styles, patterns) versus what
   is genuinely new. Prefer reuse.
4. Define scope: exact new/changed files. Call out anything that looks like a public contract (route,
   exported API, shared component prop) the feature would touch or introduce.
5. Prepare a change plan covering, where applicable: states (loading/empty/error/success/disabled),
   accessibility (keyboard, labels, focus), responsive behavior, and localization/RTL if the project uses
   them — only the ones actually relevant to this feature.
6. Present the WRITE GATE and stop for `APPROVE WRITE`.
7. Implement incrementally within the approved scope. For a non-trivial feature, prefer small verifiable
   increments over one large unreviewed change.
8. Verify what is actually checkable (build, lint, tests, manual trace); label EXECUTED or DESCRIBED.
9. Produce the completion report.

## Guardrails
- Do not introduce a new dependency without the user explicitly requesting or approving it.
- Do not silently redesign an unrelated part of the UI or architecture while building the feature.
- If the feature implies a decision the user has not made (e.g., which of two possible UX patterns), ask
  once rather than picking silently when the choice is material.
