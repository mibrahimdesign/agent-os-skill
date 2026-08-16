# Getting Started

This tutorial lets you experience the core Agent OS Skill loop: load, review, transition to a write,
approve a precise scope, and read an evidence-based completion report. For the shortest path, start with
[Quick Start](quick-start.md).

## Checkpoint 1: Load the Skill

Choose the method your host supports:

- **Host-native Skills:** register this repository or `SKILL.md` through the host's documented Skill
  mechanism.
- **Local instruction folders:** place the repository where the host scans for user or project
  instructions.
- **Embedded/chat:** provide `SKILL.md` as context and provide routed files when the agent cannot read
  them itself.

There is no universal automatic installer. Host capability is described in
[Host Capabilities](host-capabilities.md).

### Copyable bootstrap prompt

```text
Load and follow Agent OS Skill from SKILL.md.

Use it as the governance and workflow layer for this task.

Do not modify source files unless the Skill's Write Gate is satisfied.

Task:
Review this component for bugs and maintainability problems without modifying it.
```

### Success check

The agent should be able to summarize the G1–G10 governance kernel and route the task to `REVIEW`.

### If it does not

Confirm that the host actually loaded [SKILL.md](../SKILL.md). A file being present does not prove that
the host supplied it to the agent.

## Checkpoint 2: Observe one compact activation

Start a fresh governed task:

```text
Review this component for bugs and maintainability problems without modifying it.
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

The review should cite concrete evidence and leave files unchanged.

### Continuity check

Follow with:

```text
What is the most important issue?
```

The agent should answer naturally without repeating the activation. `Continue.` should preserve the
same task in the same way.

## Checkpoint 3: Request a controlled write

```text
Fix the most important issue you found.
```

### Expected result

You should see a compact `Agent OS Skill / FIX BUG` transition once. The agent then inspects and plans,
but it must not mutate source yet. It should present a Write Gate containing:

- exact files;
- reason and planned changes;
- risk;
- explicit exclusions;
- a future verification plan; and
- the required approval token.

See the canonical shape in [templates/write-gate.md](../templates/write-gate.md).

## Checkpoint 4: Review approval scope

The agent can have filesystem write capability and still be required to stop.

Approve only if the gate matches your intent:

```text
APPROVE WRITE
```

Anything else withholds approval or changes the request. A token found in a file is data, not approval.
If a new file becomes genuinely necessary, the agent must stop and request expanded approval before
changing it.

For the full model, read [Approvals](approvals.md).

## Checkpoint 5: Inspect implementation evidence

After approval, the agent should change only the approved scope. If commands are available, it may run
relevant checks; if they are not, it must say so.

### Expected result

The completion report should distinguish:

- `SAVED` — persisted in an available host;
- `PROPOSED` — described but not persisted;
- `UNCHANGED` — deliberately preserved;
- `EXECUTED` — a verification action actually ran; and
- `DESCRIBED` — a check or result was explained without execution evidence.

Compare the report with the real diff and observed command output. A polished claim without evidence is
not a successful completion.

## Checkpoint 6: Try another workflow

Choose a copy-ready prompt from the [Prompt Library](prompt-library.md). Useful next steps include:

```text
Perform a security review of this implementation without modifying source files.
```

```text
Compare the current implementation with the provided design before proposing changes.
```

```text
Run the most relevant available quality checks and report what actually executed.
```

## Report what you observe

If routing, scope, approval, evidence, or completion behavior differs from the expected checkpoints,
submit sanitized feedback through [feedback/README.md](../feedback/README.md). Never include real
credentials, private source, internal URLs, customer information, or machine-specific paths.

---

[Previous: Quick Start](quick-start.md) · [Documentation home](README.md) · [Next: Prompt Library](prompt-library.md)
