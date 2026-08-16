# Quick Start

You can try Agent OS Skill in two to five minutes. It is a declarative package: Markdown and JSON, with
no installer, telemetry, or background process.

## 1. Load the Skill

Use the mechanism your agent host supports:

- **Native Skills:** register this repository or its `SKILL.md` through the host's Skill mechanism.
- **Local instruction folders:** place the repository where the host scans for user or project
  instructions.
- **Chat-only environments:** provide `SKILL.md` as context. Include the routed workflow or policy file
  if the agent cannot read repository files itself.

Automatic discovery is host-specific. If you are unsure, use this bootstrap prompt:

```text
Load and follow Agent OS Skill from SKILL.md.

Use it as the governance and workflow layer for this task.

Do not modify source files unless the Skill's Write Gate is satisfied.

Task:
<describe your task here>
```

## 2. Start with a review

```text
Review this component for bugs and maintainability problems.
Do not modify anything.
```

### Expected result

The first substantive response should begin with one compact activation:

```text
Agent OS Skill / REVIEW

Task:
Review the component for bugs and maintainability problems.

Focus:
Read-only analysis.
```

The agent should inspect evidence, report findings, and leave source files unchanged. Routine follow-ups
such as `Explain the highest-risk issue` or `Continue` should not repeat the activation.

> If you do not see the activation, confirm that your host actually loaded `SKILL.md`, then begin a new
> distinct task after loading it. Do not assume the Skill is active merely because the file exists.

## 3. Ask for a fix

```text
Fix the most important issue you found.
```

This changes the operation from read to write. You should see a compact workflow transition, followed by
inspection and a scoped Write Gate. The agent must stop before source mutation.

```text
WRITE GATE

Files:
- src/components/Card.tsx

Reason:
Fix the confirmed rendering defect.

Planned changes:
- Apply the smallest root-cause correction.

Risk:
Low

Out of scope:
- Unrelated components and refactors.

Verification plan:
- Inspect the resulting diff and run the relevant check when available.

Approval:
Reply APPROVE WRITE to proceed with exactly the scope above.
```

The host may technically allow writes, but that capability is not approval. Review the gate and reply
with the exact token only if the scope is acceptable:

```text
APPROVE WRITE
```

Any different reply withholds approval or changes the conversation. If an additional file becomes
necessary, the agent must stop and request expanded approval.

## 4. Read the completion report

After implementation, expect a short evidence-based report:

```text
Changed
- Card rendering: SAVED

Verified
- EXECUTED — inspected the diff; only the approved file changed.

Not verified
- DESCRIBED — project build was unavailable in this host.

Unchanged
- Related components and configuration.
```

`SAVED`, `PROPOSED`, and `UNCHANGED` describe persistence. `EXECUTED` and `DESCRIBED` distinguish checks
that actually ran from checks that are only explained.

## What to try next

- Pick a prompt from the [Prompt Library](prompt-library.md).
- Follow the deeper [Getting Started tutorial](getting-started.md).
- Learn the [approval model](approvals.md) before a larger write.
- Check [host capabilities](host-capabilities.md) if tools or persistence are unavailable.

---

[Documentation home](README.md) · [Next: Getting Started](getting-started.md)
