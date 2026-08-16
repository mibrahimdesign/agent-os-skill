# Feedback (doc index)

The full feedback system lives under `feedback/`. This page is a short pointer, since feedback is central
enough to the beta that it deserves a doc entry too.

- `feedback/README.md` — what to report, why, and the categories (F1-F10).
- `feedback/ISSUE_TEMPLATE.md` — structured template for something that felt wrong.
- `feedback/FEATURE_REQUEST.md` — structured template for something you wish existed.
- `feedback/CORE_CANDIDATES.md` — how validated feedback becomes a candidate for a future Agent OS Core,
  and what's already being tracked.

## The short version

If you don't want to use any template: just say what you tried, what you expected, and what actually
happened. That's enough to be useful. Sanitize any real code, secrets, or private identifiers first.

## What happens after you submit

Feedback is classified, and if it looks reproducible and impactful, it gets tested against real scenarios
before it changes anything (`feedback/README.md`'s pipeline diagram). No single report — no matter how
convincing — silently edits `SKILL.md` or a policy file. This is deliberate: governance changes need
evidence, not just a strong opinion, even the maintainer's own.
