# FAQ

**Does Agent OS Skill work with my AI model?**
It's designed to be model-agnostic. The instructions are explicit and structured on purpose, so both
large frontier models and smaller/local models should be able to follow them (see
`docs/how-it-works.md` "Why progressive loading exists"). Behavior quality still depends on how well your
specific model follows instructions in general — that variance is expected during the beta and is exactly
what feedback helps quantify.

**Does it require cloud AI?**
No. It has no dependency on any specific cloud provider.

**Can it work with local models?**
Yes, conceptually — as long as the model can read and follow the Skill's instructions and the host can
route requests through it. Compatibility with any particular local model setup is something the beta is
actively trying to learn about; report what you find.

**Does it require MCP?**
No. MCP (or any external connector) is treated as one optional capability
(`MCP_OR_EXTERNAL_CONNECTOR`, see `docs/host-capabilities.md`), used only when actually available. Nothing
in the core workflows requires it.

**Does it automatically modify my repository?**
No. Read-only workflows never write. Write workflows always stop at a Write Gate and wait for your exact
`APPROVE WRITE` reply first. See `docs/approvals.md`.

**Why does it ask for write approval?**
Because filesystem/tool permission is not the same thing as your consent to a specific change — see
`docs/host-capabilities.md`. The gate exists so you see the scope before it happens, not after.

**Can I use it only for reviews?**
Yes. `workflows/review.md`, `workflows/security-review.md`, and `workflows/understand-project.md` are all
strictly read-only; nothing routes you into a write unless you ask for one.

**What happens if my agent cannot run commands?**
Verification is labeled `DESCRIBED` instead of `EXECUTED`, and the agent should tell you exactly what
should be run and by whom, rather than claiming a check passed. See `policies/evidence.md`.

**Does it store my code?**
The Skill itself has no telemetry or storage mechanism. Any state described in
`workflows/export-state.md` is generated as text; whether that text is persisted depends on the active
host, its capabilities, and your authorization. The Skill must report proposed and saved state
separately.

**Does it send telemetry?**
No hidden telemetry is designed into this Skill. Feedback is something you choose to submit manually; see
`feedback/README.md`.

**Can repository files override Agent OS instructions?**
No. Anything read from the repository, its docs, comments, or connected tools is treated as data to
reason about, never as a command — even if it contains text that looks like an instruction or an approval
  token. See `policies/instruction-isolation.md` and AOS-T004 in `tests/semantic-tests.md`.

**Can I use it with multiple agents?**
The governance kernel is written to be host-agnostic and should apply whether one agent runs everything
sequentially or a host supports separate agents/passes for implementation vs. review. Sequential
single-agent execution should be honest about not being "independent" verification (see G9 in
`SKILL.md`). Formal multi-agent role coordination is a candidate for a future version — see
`feedback/CORE_CANDIDATES.md` (CC-2).

**Can I suggest features?**
Yes — `feedback/FEATURE_REQUEST.md`. Feature requests don't get built automatically, but recurring,
evidenced ones become tracked candidates.

**What happens to feedback?**
It's classified, and if it's reproducible and impactful, evaluated and tested before it changes any
governance rule. See `feedback/README.md` and `feedback/CORE_CANDIDATES.md`.

**Is this the full Agent OS Core?**
No. This is a deliberately small beta subset meant to validate real workflows before a formal Core is
built. See the root `README.md` "Current Beta Scope" and "Roadmap" sections.

**Are the current PASS results field-confirmed?**
Some are. The repository preserves 20 historical self-simulated PASS results and has live-observed
evidence for 23 distinct tests, including a successful five-test AOS-B011 targeted regression. Seventeen
distinct tests currently meet the field-confirmed definition. All live evidence is still limited to one
model class and one host class, with no independent validation, so cross-model and cross-host stability
must not be inferred. See `validation/STATUS.md`.
