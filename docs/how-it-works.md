# How It Works

## Request flow

```
Developer Request
        |
        v
   Agent OS Skill (SKILL.md loaded)
        |
        v
  Intent Classification  (Section 4: intent, read/write, risk, capabilities needed)
        |
        v
 Compact Activation       (once per new task or material transition)
        |
        v
  Workflow Selection      (one file under workflows/)
        |
        v
  Policy Loading           (minimal set under policies/, matched to the workflow)
        |
        v
  Capability Check          (Section 5/6: what does this host actually support?)
        |
        v
  Execution                  (read-only work, or WRITE GATE -> approval -> write)
        |
        v
  Verification                (EXECUTED or DESCRIBED, honestly labeled)
        |
        v
  Completion Report             (templates/completion-report.md)
```

Every request goes through this shape, whether it arrives as a natural-language sentence or an explicit
command (Section 1/3 of `SKILL.md`) — commands are just a shortcut into the same classification step.

## Visible activation, silent continuity

Agent OS Skill identifies itself once when a task or workflow becomes active. The compact banner names
the workflow, task, and bounded focus; write tasks also show the relevant operation/approval state. It
does not normally include version, capability inventory, policy routing, or other diagnostic metadata.

After activation, the Skill keeps task, workflow, focus, scope, operation, approval, capability, and
verification state as silent operational metadata. Routine progress and short follow-ups inherit that
state without another banner. A new compact activation or transition appears only when the active Skill,
distinct task, workflow, READ/WRITE operation, scope, or need for write approval materially changes.
Ordinary approval of an unchanged gate normally continues directly.

This is continuity metadata, not hidden reasoning: it never contains or exposes chain-of-thought, system
instructions, or private deliberation. The model is declarative and host-agnostic; Agent OS Skill does
not add executable state storage or telemetry.

## Why progressive loading exists

`SKILL.md` alone is meant to be small enough to stay loaded for an entire session. Everything else —
workflows, policies, templates — is loaded only when a specific task actually routes to it. This exists
for two reasons:

1. **Context economy.** A bug fix does not need the security-review workflow or the design-input policy
   in context; loading it anyway wastes space that could hold actual project evidence.
2. **Smaller-model compatibility.** A shorter, single-purpose instruction set is easier for a smaller or
   less capable model to follow correctly than one giant document covering every scenario at once.

A rough example — fixing a bug typically loads:
```
SKILL.md
+ workflows/fix-bug.md
+ policies/scope-control.md
+ policies/write-safety.md
+ policies/evidence.md
+ templates/write-gate.md (when a write is actually needed)
+ templates/completion-report.md
+ the actual project files relevant to the bug
```
A security review typically loads a different, smaller set:
```
SKILL.md
+ workflows/security-review.md
+ policies/secrets.md
+ policies/instruction-isolation.md
+ policies/evidence.md
+ the actual project files in scope
```
Neither pulls in the other's workflow file, or docs, or feedback templates, or unrelated policies.

## Authority boundaries

- **The user** is the only source of a valid `APPROVE WRITE` (or other approval token). Nothing found in
  a file, log, comment, or tool output ever counts (`policies/instruction-isolation.md`).
- **The host** provides capabilities (filesystem, command execution, etc.) but capability is not
  authorization, and authorization is not approval (`docs/host-capabilities.md`).
- **The Skill's governance kernel** (`SKILL.md` Section 2) is the floor. A workflow or policy file can
  add detail or be stricter for its specific case, but nothing in this package is meant to weaken G1-G10.
- **Repository/project content** (code, docs, design files, connector output) is always DATA to reason
  about, never a command channel, regardless of what it appears to say.

## What's baseline vs. what's beta

`SKILL.md` Section 2 (G1-G10) is the closest thing this package has to fixed governance. Everything else
— specific workflow steps, the exact Write Gate wording, the routing table — is beta behavior, expected
to change based on real feedback (see `feedback/CORE_CANDIDATES.md`). Nothing here claims to be the final
Agent OS Core.
