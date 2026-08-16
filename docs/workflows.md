# Workflows

Natural-language requests route to the closest supported workflow. You usually do not need to name the
workflow yourself; explicit names are useful when a request could reasonably mean either review or
implementation.

| Workflow | Authoritative file | Operation | Purpose |
|---|---|---|---|
| Understand Project | [understand-project.md](../workflows/understand-project.md) | Read-only | Build an evidence-based picture of architecture, dependencies, risks, and conventions. |
| Review | [review.md](../workflows/review.md) | Read-only | Report evidence-backed correctness, maintainability, accessibility, and consistency findings. |
| Fix Bug | [fix-bug.md](../workflows/fix-bug.md) | Write-gated | Find the root cause, bound the change, obtain approval, implement, verify, and report. |
| Create Feature | [create-feature.md](../workflows/create-feature.md) | Write-gated | Add focused functionality within existing architecture and conventions. |
| Improve UI/UX | [improve-ui-ux.md](../workflows/improve-ui-ux.md) | Write-gated for implementation | Improve usability, accessibility, responsiveness, or visual consistency while preserving contracts. |
| Security Review | [security-review.md](../workflows/security-review.md) | Read-only | Prioritize concrete risks, redact secrets, and treat reviewed content as data. |
| Quality Check | [quality-check.md](../workflows/quality-check.md) | Read-only | Run available checks and report execution and independence honestly. |
| Read Design | [read-design.md](../workflows/read-design.md) | Read-only | Extract facts from available design evidence without assuming a particular platform. |
| Prepare Project *(optional Beta)* | [prepare-project.md](../workflows/prepare-project.md) | Strict read-only | Perform explicit session-start orientation; never runs automatically. |
| Export State *(optional Beta)* | [export-state.md](../workflows/export-state.md) | Strict read-only | Describe portable conversation state for hosts without persistence. |

## Routing examples

| Request | Route | What to expect |
|---|---|---|
| “Understand this project before changing anything.” | `UNDERSTAND PROJECT` | Inspection and orientation, no mutation. |
| “Review this component.” | `REVIEW` | Findings and recommendations, no mutation. |
| “Fix the issue you found.” | `FIX BUG` | Read-to-write transition, then a scoped Write Gate. |
| “Perform a security review without modifying files.” | `SECURITY REVIEW` | Evidence-backed security findings and redaction. |
| “Compare this implementation with the design.” | `READ DESIGN` | Differences based only on available design evidence. |

Read-only requests never silently become write operations. A follow-up that explicitly requests a fix
creates a visible workflow transition and is governed by the Write Gate.

## Current Beta scope

These ten workflows are the full 0.1.2-beta set. The broader Agent OS v6 specification contains ideas
that are intentionally not implemented here, including formal multi-agent role orchestration and a
persistent project-state layer. Recurring evidence is tracked in
[Core Candidates](../feedback/CORE_CANDIDATES.md), not added automatically.

Need a starting request? Use the [Prompt Library](prompt-library.md).

---

[Previous: How It Works](how-it-works.md) · [Documentation home](README.md) · [Next: Approvals](approvals.md)
