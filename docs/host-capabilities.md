# Host Capabilities

Agent OS Skill separates three concepts that are often blurred together:

```text
CAPABILITY       — can the host technically do this?
AUTHORIZATION    — may the active workflow use it in principle?
APPROVAL         — did the user accept this exact bounded action?
```

None implies the next. Filesystem access does not automatically authorize source mutation, and a
workflow that permits a write proposal still requires the user's scoped approval. See
[Approvals](approvals.md).

## Capability states

Each relevant capability is recorded as `AVAILABLE`, `UNAVAILABLE`, or `UNKNOWN`. Unknown capability is
never treated as available merely to keep a task moving.

| Capability | Meaning |
|---|---|
| `FILESYSTEM_READ` | Read project files. |
| `FILESYSTEM_WRITE` | Create or modify files. |
| `COMMAND_EXECUTION` | Run builds, tests, linters, or other commands and observe output. |
| `NETWORK_ACCESS` | Reach external network resources. |
| `MCP_OR_EXTERNAL_CONNECTOR` | Use a connected external tool or data source. |
| `IMAGE_INPUT` | Receive and interpret screenshots or other image evidence. |
| `STATE_PERSISTENCE` | Durably retain state or files through the host. |
| `SUBAGENTS` | Run separate agent instances or passes. |
| `NATIVE_WRITE_APPROVAL` | Use a host-provided confirmation mechanism. |

## Why this matters

- Without `COMMAND_EXECUTION`, the agent cannot truthfully say “tests passed.” It should label the
  suggested check `DESCRIBED`, not `EXECUTED`.
- Without `STATE_PERSISTENCE`, a change is `PROPOSED`, not `SAVED`.
- A native host confirmation can participate in the approval mechanism only when it presents the
  semantically sufficient scope. A generic “allow writes” setting is not approval for every change.
- A connector or image capability cannot be inferred because the task would benefit from it.

The detailed claim rules live in the [evidence policy](../policies/evidence.md).

## Operating modes

- **FULL** — enough verified capability to inspect and modify a real project and run relevant commands.
- **LIMITED** — one or more capabilities are missing; the agent adapts and reports the gap.
- **EMBEDDED** — no persistence; the agent analyzes, reviews, and proposes but never claims a save.

Operating mode describes the capability environment, not the model vendor or product name. Two hosts
with different names but the same material capability profile do not automatically prove portability.

See [SKILL.md](../SKILL.md) Sections 5–6 for the normative runtime definitions. AOS-T008, AOS-T009, and
AOS-T011 in the [semantic tests](../tests/semantic-tests.md) illustrate capability-honesty scenarios.

---

[Previous: Approvals](approvals.md) · [Documentation home](README.md) · [Next: FAQ](faq.md)
