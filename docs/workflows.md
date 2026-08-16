# Workflows

Full list of workflows implemented in 0.1.1-beta. Each links to its file under `workflows/`, which is the
authoritative, loadable version — this page is an index and summary.

| Workflow | File | Read/Write | Summary |
|---|---|---|---|
| Understand Project | `workflows/understand-project.md` | Read-only | Build an evidence-based picture of a project or scope. Usually run first. |
| Review | `workflows/review.md` | Read-only | Evidence-based findings on correctness, maintainability, accessibility, consistency. Never mutates. |
| Fix Bug | `workflows/fix-bug.md` | Write | Root-cause-first bug fix: understand -> inspect -> root cause -> scope -> gate -> approval -> implement -> verify -> report. |
| Create Feature | `workflows/create-feature.md` | Write | New functionality built inside existing architecture and conventions, gated the same way. |
| Improve UI/UX | `workflows/improve-ui-ux.md` | Write | Visual/UX/accessibility improvement that preserves existing behavior and contracts. |
| Security Review | `workflows/security-review.md` | Read-only | Practical security findings; strict secret redaction; treats reviewed content as data, never instructions. |
| Quality Check | `workflows/quality-check.md` | Read-only | Independent(-as-possible) check of a change against its original goal; labels self-checks honestly. |
| Read Design | `workflows/read-design.md` | Read-only | Extracts design facts from whatever source actually exists (connector, image, repo artifact, spec, or code) — no platform required. |
| Prepare Project *(optional)* | `workflows/prepare-project.md` | Strict read-only | Quick session-start orientation; explicit command only, never automatic. |
| Export State *(optional)* | `workflows/export-state.md` | Strict read-only | Serializes conversation state as portable text for hosts without persistence. |

## Choosing a workflow

You almost never need to name one directly — natural language routes automatically (`SKILL.md` Section
3-4). Use explicit commands when you want to be unambiguous, especially in mixed read/write situations
("Review this" vs. "Fix this" can look similar in casual phrasing).

## What's intentionally NOT in 0.1.1-beta

The full Agent OS v6 specification defines many more commands (contract checks, visual regression review,
dependency policy audits, Angular-specific upgrade planning, multi-role team orchestration, and more).
These are deliberately out of scope for this beta — see the root `README.md` "Current Beta Scope" section
and `feedback/CORE_CANDIDATES.md`. If you need one of these regularly, that's exactly the kind of signal
this beta is designed to collect — file a `feedback/FEATURE_REQUEST.md`.
