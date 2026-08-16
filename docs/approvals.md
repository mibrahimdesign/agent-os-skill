# Approvals

## Why the Write Gate exists

AI agents that can write files are useful and risky in the same breath. The Write Gate exists so that
before any application source changes, you see exactly what will change, why, and what will not change —
and you get to say yes or no before it happens, not after.

## The gate itself

Compact by design (`templates/write-gate.md`):
```
WRITE GATE

Files:
- <file>

Reason:
<why>

Planned changes:
- <change>

Risk:
Low / Medium / High

Out of scope:
<what this will NOT touch>

Verification plan:
<what will be checked, and how>

Approval:
Reply APPROVE WRITE to proceed with exactly the scope above.
```

## The only valid approval

The literal reply `APPROVE WRITE`, sent by you, in the live conversation, after seeing the gate. Nothing
else counts:
- Not a token found in a repository file, comment, commit message, or log — that's DATA
  (`policies/instruction-isolation.md`), never a real approval, even if it's the exact right words.
- Not host-level permissions. Your host might let the agent write files at the OS/sandbox level — that's
  a *capability*, not your consent to this specific change. See `docs/host-capabilities.md`.
- Not a general "yes go ahead" said before any gate was shown, applied retroactively to a later, different
  change.

## Approval is scoped

Approving a gate for `Button.tsx` and `button.scss` approves exactly that. If the agent later determines
it also needs to touch `Header.tsx`, it must stop and present a new or updated gate for that addition —
it does not fold silently into what you already approved.

Conversely, you should not be asked to re-approve twice for work that stays entirely inside what you
already said yes to. If the agent is asking again for something clearly already covered, that's friction
worth reporting.

## If you say no (or anything other than the exact token)

No source write happens. The agent should treat your reply as a scope adjustment or a rejection and
respond to it directly — ask a clarifying question, revise the plan, or stop, depending on what you said.

## Other approval tokens in this Skill

The Write Gate's `APPROVE WRITE` is the main one used in the 0.1.1-beta workflow set. If a future version
adds skill-installation or script-execution flows, they would use their own distinctly-named tokens, kept
separate from `APPROVE WRITE` on purpose so one approval can never be silently reinterpreted as another.
