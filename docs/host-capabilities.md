# Host Capabilities

Three separate concepts get confused constantly in AI tooling. Keeping them apart is central to how this
Skill stays safe across very different hosts.

```
CAPABILITY       — can the host technically do this at all?
AUTHORIZATION    — is the agent's use of that capability, in general, allowed here?
APPROVAL         — did the user say yes to this specific, bounded action?
```

**None of these implies the next one.**

> An agent may have filesystem write access, but that only means the host can technically write files. It
> does not automatically mean Agent OS Skill has user approval to modify application source. Approval is
> always a separate, explicit, scoped step — see `docs/approvals.md`.

## The capability list

The Skill only reasons about these (SKILL.md Section 5) — it does not try to enumerate every possible
tool a host might expose:

| Capability | What it means |
|---|---|
| FILESYSTEM_READ | The agent can read project files. |
| FILESYSTEM_WRITE | The agent can write/modify project files. |
| COMMAND_EXECUTION | The agent can run commands (build, test, lint, etc.) and see real output. |
| NETWORK_ACCESS | The agent can reach the network (fetch a URL, call an API). |
| MCP_OR_EXTERNAL_CONNECTOR | The agent has a connected external tool/data source (design tools, issue trackers, etc.). |
| IMAGE_INPUT | The agent can receive and interpret images (screenshots, mockups). |
| STATE_PERSISTENCE | The agent (or host) can durably save state between messages/sessions. |
| SUBAGENTS | The host can run separate agent instances/passes for independent work. |
| NATIVE_WRITE_APPROVAL | The host has its own built-in confirm-before-write mechanism. |

Each is `AVAILABLE`, `UNAVAILABLE`, or `UNKNOWN`. `UNKNOWN` is treated exactly like `UNAVAILABLE` for the
purpose of deciding what the agent may claim or do — it never grants permission by default.

## Why this matters day to day

- If `COMMAND_EXECUTION` is unavailable, the agent should never claim "tests passed" — it should say
  verification is `DESCRIBED`, not `EXECUTED` (`policies/evidence.md`).
- If `STATE_PERSISTENCE` is unavailable, the agent should never claim a file was "saved" — it should
  produce a `PROPOSED STATE UPDATE`-style output instead (`SKILL.md` Section 6, `G7`).
- If `NATIVE_WRITE_APPROVAL` exists in your host (some IDEs/agents show their own file-write confirmation
  dialog), that is a capability, and it might satisfy the *mechanism* of getting your consent — but the
  Skill's Write Gate should still show you the actual scope and reasoning; a generic host "allow this
  agent to write files" toggle, granted once, is not the same as approving this specific change.

## Operating modes derived from capability

- **FULL** — enough capability to inspect and modify a real project and verify with real commands.
- **LIMITED** — some capability missing; the agent adapts, and is explicit about what it could not do.
- **EMBEDDED** — no persistence; the agent can only analyze, propose, and describe — never claim a save.

See `SKILL.md` Section 6 for the full definitions, and AOS-T008, AOS-T009, and AOS-T011 in
`tests/semantic-tests.md` for concrete scenarios you can check your own host against.
