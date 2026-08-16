# Workflow: Prepare Project (optional beta command)

Intent: PREPARE_PROJECT | Read/Write: STRICT READ-ONLY (zero writes, zero proposals) | Typical risk: low
Policies loaded: scope-control.md
Triggers on explicit command only: "prepare project" / "PREPARE PROJECT". This workflow is not triggered
by a chat starting or a project being opened — nothing here runs automatically.

## Purpose
Give a quick, honest orientation at the start of a working session: what this project is, what state it
is in, and what a sensible next step would be — without writing or proposing to write anything, even
Skill-level notes.

## Steps

1. Read only what is needed to answer: project identity (name, stack, rough size/shape), and, if
   available from prior context in this conversation, what was last worked on.
2. Do not persist anything and do not emit a PROPOSED STATE UPDATE — this workflow is strict read-only
   by design, even on hosts that support persistence.
3. Summarize plainly:
   ```
   PROJECT READY
   Project:      <name/identity, with evidence>
   Stack:        <framework/language, with evidence>
   Last state:   <from conversation context, or "no prior context in this session">
   Ready for the next scoped request.
   ```
4. If identity cannot be confirmed from available evidence, say so rather than guessing.

## Guardrails
- Never treat this as a reason to start reading the entire repository; keep it light and fast.
- Never write, propose, or persist any state as part of this workflow.
