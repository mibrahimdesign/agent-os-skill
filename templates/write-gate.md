# Template: Write Gate

Print this before any application-source mutation. Keep it compact — do not pad it into a bureaucratic
form. Wait for the literal reply `APPROVE WRITE` before writing anything.

```
WRITE GATE

Files:
- <file>
- <file>

Reason:
<why this write is required, one or two sentences>

Planned changes:
- <change>
- <change>

Risk:
Low / Medium / High

Out of scope:
<explicitly state what this change will NOT touch, especially anything nearby that might look related>

Verification plan:
<what will be checked after writing, and whether it will be EXECUTED or DESCRIBED>

Approval:
Reply APPROVE WRITE to proceed with exactly the scope above.
```

Rules:
- List every file that will actually be touched. If you are not sure yet whether a file needs touching,
  do not include it — find out first, or note it as a possible scope addition that would need its own
  gate.
- "Out of scope" is not filler — name the specific things a reader might reasonably expect to change but
  that will not.
- If the user approves, proceed only within this exact scope (`policies/write-safety.md` §5). If new
  scope becomes necessary mid-task, stop and present a new gate for the delta.
- If the user does not reply with the exact token, do not write. Treat anything else as scope adjustment
  or rejection and respond accordingly, without writing.
