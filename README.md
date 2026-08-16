# Agent OS Skill

**Public Beta · Version 0.1.1-beta** — an experimental, strongly-governed developer skill, now in field
validation.
This release exists to validate real-world workflows and collect developer feedback before a full Agent
OS Core is formalized.
It is not a finished universal operating system yet — treat it as a serious, usable beta with clear
edges.

## What is Agent OS Skill?

Agent OS Skill is a portable governance and workflow layer for AI-assisted software development. It
helps a development agent understand scope, inspect before modifying, request approval before controlled
writes, verify its own work honestly, protect sensitive information, and report exactly what changed —
without embedding a vendor-specific model or host requirement.

It is a skill, not a product: a set of Markdown instructions, policies, templates, and workflows designed
for capable AI development agents to load and follow. Actual behavior still depends on the model and host;
cross-model and cross-host stability are not yet established.

## Why does it exist?

AI coding agents commonly run into the same handful of problems:

- Changing more than what was asked, quietly expanding scope.
- Modifying code before actually understanding it.
- Losing track of what was and wasn't approved.
- Trusting instructions found inside repository content, comments, or tool output as if the user sent
  them.
- Claiming verification happened ("tests pass", "the file was saved") when it didn't.
- Forgetting project context between requests.
- Exposing secrets found while reading code.
- Behaving inconsistently depending on which agent or model is running it.

Agent OS Skill addresses each of these directly with a small, explicit governance kernel (scope control,
read-before-write, an explicit Write Gate, instruction isolation, evidence-based claims, and honest
completion reporting) instead of leaving them to each model's individual judgment.

## Who is it for?

- Frontend, backend, and full-stack developers
- Designers working in or near code
- Architects and technical leads
- Security reviewers
- Developers using local models
- Developers using cloud models
- Teams using more than one AI agent across a project

It makes no assumptions about which of these tools you use.

## What it does

- Classifies each request (intent, read-only vs. write, risk, required capabilities) before acting.
- Identifies itself once with a compact task/workflow banner, then keeps the active context silently
  until a meaningful task, workflow, operation, scope, or approval boundary changes.
- Routes to a focused workflow instead of applying one giant, generic prompt to everything.
- Keeps read-only work (understanding, reviewing, auditing) strictly separate from source mutation.
- Requires an explicit, scoped Write Gate and your literal approval before any application-source write.
- Treats repository content, docs, and tool output as data — never as commands, never as approval.
- Labels every verification claim EXECUTED or DESCRIBED, honestly, based on what actually happened.
- Redacts secrets on discovery instead of exposing them.
- Ends every task with a completion report distinguishing saved / proposed / unchanged state.
- Collects structured feedback to evolve into a future, more complete Agent OS Core.

## Governance Kernel

The ten baseline rules are defined in `SKILL.md` Section 2:

1. G1 Scope Lock
2. G2 Read Before Write
3. G3 Explicit Write Control
4. G4 Instruction Isolation
5. G5 Capability Honesty
6. G6 Evidence Before Claims
7. G7 State Honesty
8. G8 Secret Safety
9. G9 Verification Integrity
10. G10 Completion Honesty

AOS-B011 Active Skill Focus is a beta operational behavior, not G11.

## What it does NOT do

- It does not replace the developer. It proposes, implements within approved scope, and reports — you
  stay in control of what ships.
- It does not bypass your host's own security or sandboxing.
- It does not automatically modify every repository it sees. Nothing happens without an explicit request
  and, for writes, your explicit approval.
- It does not automatically access external tools, connectors, or design platforms. It uses only what is
  verifiably available for the current task.
- It does not automatically trust instructions found inside a repository, including anything that looks
  like an approval token.
- It does not guarantee any particular tool is available — it adapts to whatever capabilities the host
  actually verifies (see `docs/host-capabilities.md`).
- It does not guarantee "independent" verification unless there is an actual separate pass, reviewer, or
  executed evidence behind it — see `policies/evidence.md`.
- It does not require any single model vendor, IDE, or platform.

## Installation

Because hosts differ, install conceptually — pick whichever matches your environment.

### Host-native skill support
If your host has its own skill/plugin mechanism, install or register the downloaded repository/package
directory — the directory containing `SKILL.md` — and use `SKILL.md` as its entrypoint.

### File-based agent
Place the downloaded repository/package directory in whatever location your host scans for user- or
project-level skills. Folder naming is host-specific; no nested package directory is required.

### Embedded / chat environment
Provide `SKILL.md` directly in the conversation/context, and be ready to paste in the routed workflow or
policy file (see `docs/how-it-works.md`) when the agent needs it.

Vendor-specific installation steps are intentionally not documented here — they belong in optional
adapters outside this universal package, never inside the core Skill.

## Quick Start

```
Understand this project before making any changes.
```
```
Review this component for bugs and maintainability problems.
```
```
Fix the responsive issue in the header.
```
```
Review this implementation against the attached design.
```
```
Perform a security review without modifying the source.
```

Full walkthrough: `docs/getting-started.md`.

## How the Skill behaves

```
Understand -> Inspect -> Plan -> Approve when needed -> Implement -> Verify -> Report
```

Read-only requests stop after reporting. Write requests pause at the Write Gate until you approve.
Details: `docs/how-it-works.md`.

At the beginning of a task, Agent OS Skill identifies the active workflow and focus once in a compact
banner. It then keeps task, workflow, scope, and approval context silently. The banner returns only for a
new task or a material workflow, operation, scope, approval-boundary, or active-Skill transition—not for
routine progress or short follow-ups.

## Write Gate

Any application-source mutation is preceded by a compact Write Gate: files, reason, planned changes,
risk, what's explicitly out of scope, and a request for your literal `APPROVE WRITE` reply.

```
WRITE GATE

Files:
- src/components/Header.tsx

Reason:
Fix layout overflow on narrow viewports.

Planned changes:
- Adjust flex-wrap and spacing tokens in the header container.

Risk:
Low

Out of scope:
No changes to header logic, links, or navigation state.

Approval:
Reply APPROVE WRITE to proceed with exactly the scope above.
```

Approval is scoped to exactly what's presented — a need for an additional file returns to a new gate.
Host filesystem permission is a capability, not your approval (see `docs/host-capabilities.md` and
`docs/approvals.md`).

## Read-Only Work

Review, security review, and understanding tasks never mutate code by themselves. "Review this" never
silently becomes "I fixed this" — a fix is a separate, explicitly requested, explicitly approved write.

## Supported Environments

- **FULL** — the host can inspect and modify a real project and verify with real commands.
- **LIMITED** — some capabilities are missing; the Skill adapts and is honest about what it couldn't do.
- **EMBEDDED** — no persistence capability; the Skill analyzes, reviews, and proposes, and never claims a
  file was saved.

Details: `docs/host-capabilities.md`.

## Working With Designs

`READ DESIGN` (or a natural request like "match this to the attached design") works with whatever design
input actually exists — a connected design tool, an attached image, a repository design artifact, an
existing implementation used as reference, or a plain text specification. No specific design platform is
ever required, and the Skill never claims to have inspected a source that wasn't actually available.

## Feedback

This beta is built to be corrected by real usage. If something felt wrong, missing, or surprising, that's
exactly the signal this release wants.

- `feedback/README.md` — how and what to report
- `feedback/ISSUE_TEMPLATE.md` — structured issue report
- `feedback/FEATURE_REQUEST.md` — structured feature request
- `feedback/CORE_CANDIDATES.md` — how validated feedback becomes a candidate for a future Core
- `CONTRIBUTING.md` — contribution and validation-evidence guidance

## Security and Privacy

- Repository content, comments, logs, and tool output are always treated as data, never as instructions
  or approval (`policies/instruction-isolation.md`).
- Secrets are never exposed; discoveries are reported as `[REDACTED]` with location and risk category
  only (`policies/secrets.md`).
- No hidden telemetry. Feedback is manual and opt-in, and templates explicitly ask you to sanitize
  private information before submitting (`feedback/README.md`).
- Sensitive reports should follow `SECURITY.md`; never place secrets or private project content in a
  public issue.

## Current Beta Scope

Implemented in 0.1.1-beta:
```
UNDERSTAND PROJECT
REVIEW
FIX BUG
CREATE FEATURE
IMPROVE UI UX
SECURITY REVIEW
QUALITY CHECK
READ DESIGN
PREPARE PROJECT (optional)
EXPORT STATE (optional)
```
Not implemented in this release (see `feedback/CORE_CANDIDATES.md` for candidates under consideration):
formal multi-agent role orchestration, a persistent per-project state/memory layer, framework-specific
upgrade planning, visual regression baselines, and the remainder of the full Agent OS v6 command set.

## Validation Status

This beta is in the **Field Validation phase**. It has 20 historical same-agent self-simulated results,
live-observed evidence for 23 distinct tests, and 17 distinct field-confirmed tests. The targeted
AOS-B011 regression passed AOS-T022/T023/T024/T026/T027 after the activation-boundary fix; historical
failures remain preserved. Evidence still comes from one live model class and one live host class, with
no live-independent results.

Evidence strength is separate from PASS/FAIL:

- `STATIC_REVIEW` — files inspected; no scenario execution.
- `SELF_SIMULATED` — the same agent reasoned through the scenario.
- `LIVE_OBSERVED` — a real scenario ran in an actual host/runtime and was observed.
- `LIVE_INDEPENDENT` — execution received genuinely separate evaluation.

Cross-model and cross-host validation remain incomplete. See `validation/STATUS.md` for the concise
dashboard and `validation/EVIDENCE_MODEL.md` for maintainer definitions.

To participate, run a sanitized scenario in a real host, record what actually happened using
`tests/test-result-template.md`, and submit the result or plain-language feedback without private code,
secrets, internal URLs, or customer information. The quick-start workflow does not require knowing the
validation vocabulary.

## Roadmap

```
0.1.x   Behavioral validation        (this release: field-validate the existing beta, fix real defects)
0.2.x   Feedback-driven expansion    (real developer usage drives what's added next)
Future  Agent OS Core extraction     (only once governance is stable across models and hosts, not on a
                                       fixed date)
```
Roadmap items are directional, not commitments. Priorities are driven by what real usage actually
surfaces — see `feedback/CORE_CANDIDATES.md` and `feedback/CORE_READINESS.md`.

## Known Limitations

- Behavior quality depends partly on the host/model's own instruction-following ability.
- Some environments cannot persist project state between messages or sessions.
- Some environments cannot execute verification commands (builds, tests, linters).
- Independent verification requires actual independent execution or reviewer separation — sequential
  single-agent self-checks are labeled as such, not as independent.
- AOS-T021 approval retention and AOS-T025 Active Skill scope growth remain unexecuted.
- Cross-model and cross-host stability have not been established; current live evidence is limited to
  `SINGLE_MODEL` and `SINGLE_HOST`.
- Host-native skill discovery mechanisms differ across platforms; this package documents installation
  conceptually, not per-vendor.
- Vendor-specific adapters (for a particular IDE, design tool, or model provider) are intentionally not
  included in this universal beta.

## Documentation

- `docs/getting-started.md` — tutorial walkthrough
- `docs/how-it-works.md` — architecture and request flow
- `docs/workflows.md` — full workflow index
- `docs/approvals.md` — the Write Gate and approval model in depth
- `docs/host-capabilities.md` — capability vs. authorization vs. approval
- `docs/feedback.md` — feedback system pointer
- `docs/faq.md` — frequently asked questions
- `CONTRIBUTING.md` — public contribution guidance
- `SECURITY.md` — security-reporting guidance

## License

MIT — see `LICENSE`.
