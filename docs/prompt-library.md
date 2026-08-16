# Prompt Library

These prompts are starting points, not special commands. Adapt the scope and constraints to your
project. Agent OS Skill routes natural language to the appropriate workflow.

## Bootstrap

Use this when your host does not discover Skills automatically:

```text
Load and follow Agent OS Skill from SKILL.md.

Use it as the governance and workflow layer for this task.

Do not modify source files unless the Skill's Write Gate is satisfied.

Task:
<describe your task here>
```

If the host already has the Skill loaded, the short form is enough:

```text
Use Agent OS Skill for this task:
<task>
```

## Understand a project

```text
Understand this project before making any changes.
Identify the architecture, major dependencies, risks, and important development conventions.
```

Expected mode: read-only `UNDERSTAND PROJECT`.

## Review code

```text
Review this component for bugs, maintainability, accessibility, and unnecessary complexity.
Do not modify anything.
```

Expected mode: read-only `REVIEW`.

## Fix a bug

```text
Fix the responsive issue in the header.
Keep the change limited to the root cause and preserve unrelated behavior.
```

Expected mode: controlled-write `FIX BUG`; source mutation waits at the Write Gate.

## Create a feature

```text
Add an empty state to the search results.
Reuse existing patterns and keep the scope limited to this feature.
```

Expected mode: controlled-write `CREATE FEATURE`.

## Improve UI/UX

```text
Review this interface for usability, responsive behavior, accessibility, and visual consistency.
Do not change the design system unless necessary.
```

Expected mode: `IMPROVE UI UX`; analysis may be read-only, while implementation requires a Write Gate.

## Security review

```text
Perform a security review of this implementation without modifying source files.
Prioritize concrete exploitable risks over theoretical concerns.
```

Expected mode: read-only `SECURITY REVIEW`.

## Quality check

```text
Run the most relevant available quality checks for this change.
Report what was actually executed, what could not run, and any remaining risk.
```

Expected mode: `QUALITY CHECK`, limited by verified host capabilities.

## Compare a design

```text
Compare the current implementation with the provided design.
Identify visual and interaction differences before proposing changes.
```

Expected mode: read-only `READ DESIGN` until implementation is explicitly requested and approved.

## Natural follow-ups

These inherit the active task when context is intact:

```text
Continue.
```

```text
Explain the highest-risk issue.
```

```text
Fix the most important issue.
```

```text
Do not change that file.
```

The third example creates a material read-to-write transition and requires a new scoped Write Gate. The
fourth narrows scope; it is not approval.

## Useful constraints

Add these when they matter:

```text
Preserve public APIs and unrelated behavior.
```

```text
Use only the existing dependencies and design tokens.
```

```text
If another file becomes necessary, stop and request expanded approval before changing it.
```

```text
Do not claim tests passed unless you executed them and observed the result.
```

---

[Previous: Getting Started](getting-started.md) · [Documentation home](README.md) · [Next: How It Works](how-it-works.md)
