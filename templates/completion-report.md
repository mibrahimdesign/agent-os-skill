# Template: Completion Report

Every task, read-only or write, ends with this block. Keep it honest and concrete; write "None" for
empty sections rather than omitting them.

```
COMPLETION REPORT

1. What was done
   <one or two sentences, plain language>

2. State changed
   - <file or area> — Status: saved | proposed (not saved) | unchanged
     (saved requires real evidence the write succeeded; proposed = a PROPOSED STATE UPDATE was emitted;
     unchanged = inspected but intentionally left as-is)

3. Verified
   - <check> — Mode: EXECUTED | DESCRIBED — Result: PASS | FAIL | PARTIAL — Evidence: <what you saw>
   - Independence: same-pass self-check | separate pass | separate reviewer/agent | executed test evidence

4. Issues fixed
   <list, or None>

5. Open issues
   <list, or None>

6. Blocked items
   <list, or None>

7. Remaining risks
   <list, or None>

8. Improvement ideas
   <list; each one: idea — in scope for a future task, not this one>

9. Points needing discussion
   <list, or None>

10. Decisions required from the user
    <list, or None>

11. Suggested next step
    <one concrete suggestion>
```

Honesty rules:
- Never mark something "saved" without direct evidence (a successful write/tool result). If unsure,
  report it as proposed and explain the uncertainty under Open issues.
- Never call a verification EXECUTED if it did not actually run in this task.
- Never call a self-review "independent" — see `policies/evidence.md` §6.
- This report informs the user; it never grants any approval on its own.
