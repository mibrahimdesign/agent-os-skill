# Getting Started

A practical, tutorial-style walkthrough. If you just want the concept, read the root `README.md` first;
come back here when you're ready to actually use the Skill.

## 1. Install the Skill

Installation depends on your host's own mechanism — Agent OS Skill does not require a specific one.

- **Host-native skill support:** register/install the `agent-os-skill/` package using your host's
  documented skill mechanism (however it discovers and loads skills).
- **File-based agent:** copy the `agent-os-skill/` folder into whatever directory your host scans for
  user or project skills.
- **Embedded/chat environment:** paste the contents of `SKILL.md` into the conversation/context, and be
  ready to paste a routed workflow or policy file in when the agent needs it.

See `docs/host-capabilities.md` if you're unsure what your host actually supports.

## 2. Verify the agent can see it

Ask directly:
```
Do you have the Agent OS Skill loaded? Summarize its governance kernel in one paragraph.
```
A correctly loaded agent should describe scope control, read-before-write, the Write Gate, instruction
isolation, and honest completion reporting — roughly `SKILL.md` Section 2, in its own words.

## 3. Start with a read-only task

Read-only work is the safest way to learn the Skill's behavior, because nothing can be mutated.
```
Understand this project before making any changes.
```
This routes to `workflows/understand-project.md`. Expect a scope confirmation, evidence-based findings,
and a completion report — no source changes, ever, for this workflow.

At task activation, expect one compact `Agent OS Skill / <WORKFLOW>` banner with the task and focus. It
should not repeat during routine follow-ups. It resurfaces only when a new task begins or the workflow,
operation, scope, approval boundary, or active Skill materially changes.

## 4. Run a review

```
Review this component for bugs and maintainability problems.
```
This routes to `workflows/review.md`. You should get a findings table (severity, file:line, evidence,
recommendation), not a rewritten file. If the agent starts editing code here, that's a bug — report it
(`feedback/ISSUE_TEMPLATE.md`).

## 5. Request a small bug fix

```
Fix the responsive issue in the header.
```
This routes to `workflows/fix-bug.md`. Watch for the sequence: problem restated -> evidence inspected ->
root cause stated -> a WRITE GATE presented -> a pause, waiting for you.

## 6. Understand the Write Gate

The gate should look roughly like `templates/write-gate.md`: files, reason, planned changes, risk, what's
explicitly out of scope, and a request for the exact reply `APPROVE WRITE`. Read it before approving —
it's meant to be readable, not a formality to skip.

## 7. Approve or reject

- To proceed: reply exactly `APPROVE WRITE`.
- To reject or adjust: reply with anything else — a correction, a question, "not now." No write happens
  until you send the exact token.

Try both once, deliberately, so you know what each feels like.

## 8. Read the completion report

After a write (or any workflow, including read-only ones), you get
`templates/completion-report.md` filled in: what changed and its real status (saved / proposed /
unchanged), what was verified and how, open issues, and a suggested next step. If a claim in here doesn't
match what you can see actually happened, that's exactly the kind of thing feedback exists for.

## 9. Try a scope-expansion moment

Ask for a fix in one file, and if the agent notices something else worth fixing nearby, watch what it
does. It should NOT touch the unrelated thing — it should mention it under "Improvement ideas" instead.
This is AOS-T015 in `tests/semantic-tests.md`; you can trigger it in real usage.

## 10. Submit feedback

Whatever felt right or wrong, write it down while it's fresh:
- Quick version: answer the four questions in `feedback/README.md`.
- Structured version: fill out `feedback/ISSUE_TEMPLATE.md` or `feedback/FEATURE_REQUEST.md`.

That's the whole loop. Everything else in this Skill is a variation on: understand -> stay in scope ->
inspect -> plan -> gate -> approve -> implement -> verify -> report.
