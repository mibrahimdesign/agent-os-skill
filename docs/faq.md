# Frequently Asked Questions

## Does Agent OS Skill work with my AI model?

It is designed to be model-neutral, but compatibility is not universal or proven. Instruction-following
quality varies, and current live evidence covers one model class. Try a read-only task first and report
sanitized results.

## Does it require cloud AI or MCP?

No. Cloud services and external connectors are optional host capabilities, not normative dependencies.
A local model can use the Skill if its host can load the instructions and the model follows them
reliably.

## How do I install it?

Use your host's native Skill mechanism, place the repository in a scanned instruction folder, or provide
[SKILL.md](../SKILL.md) as context in a chat-only environment. There is no universal automatic install
command. See [Quick Start](quick-start.md).

## Does it automatically modify my repository?

No. Read-only workflows never write. A write workflow must present a scoped Write Gate and receive the
active user's exact `APPROVE WRITE` response before source mutation. See [Approvals](approvals.md).

## Why is host write permission not enough?

Tool availability is capability, not consent. Agent OS Skill separates `AVAILABLE`, `AUTHORIZED`, and
`APPROVED` so a broadly capable host still stops at the user decision boundary. See
[Host Capabilities](host-capabilities.md).

## Can I use it only for reviews?

Yes. [Review](../workflows/review.md), [Security Review](../workflows/security-review.md), and
[Understand Project](../workflows/understand-project.md) are strictly read-only workflows.

## What happens when commands are unavailable?

The agent should state the limitation and label suggested verification `DESCRIBED`, not `EXECUTED`. It
must not claim a test, build, or lint result that it did not observe. See the
[evidence policy](../policies/evidence.md).

## Does it store my code or send telemetry?

The Skill contains no storage service, analytics, or hidden telemetry. A host may persist files or
conversation state according to its own behavior; Agent OS Skill must report whether state was saved or
only proposed. Feedback submission is manual and opt-in.

## Can repository files override the Skill?

No. Source, documentation, comments, logs, designs, and connector output are data to inspect. They are
not user instructions or approval—even when they contain authoritative-looking text. See
[instruction isolation](../policies/instruction-isolation.md).

## Why does the Skill identify itself only sometimes?

AOS-B011 Active Skill Focus shows one compact activation for a new task or material transition, then
retains context silently. Normal follow-ups do not repeat the banner. This keeps task boundaries visible
without turning every response into a status dashboard.

## Can I use it with multiple agents?

The governance kernel is host-neutral and can apply when a host supports separate agents. Formal
multi-agent orchestration is not part of this Beta. A same-agent second pass must not be called
independent verification.

## Is this Agent OS Core?

No. This is a deliberately bounded Skill and evidence-gathering Beta. Future Core extraction depends on
accumulated cross-model and cross-host evidence, not roadmap confidence.

## Are all PASS results field-confirmed?

No. Result and evidence strength are separate. Historical self-simulation is useful but not field
confirmation. The repository currently records 17 distinct field-confirmed tests, all within one model
class and one host class, and no `LIVE_INDEPENDENT` evidence. See
[Validation Status](../validation/STATUS.md).

## How do I report a problem or request a feature?

Use the [feedback guide](../feedback/README.md), [issue template](../feedback/ISSUE_TEMPLATE.md), or
[feature request template](../feedback/FEATURE_REQUEST.md). Sanitize all private information first.

---

[Previous: Host Capabilities](host-capabilities.md) · [Documentation home](README.md) · [Next: Feedback](feedback.md)
