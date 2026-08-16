# Workflow: Understand Project

Intent: UNDERSTAND | Read/Write: READ_ONLY | Typical risk: low
Policies loaded: scope-control.md
Triggers on requests like: "Understand this project", "explain how this works", "what does this
codebase do", "orient me in this repo/component/flow", "explain this file".

## Purpose
Build an accurate, evidence-based picture of the requested scope (a whole project, a folder, a
component, or a flow) without changing anything. This is usually the first workflow run in a new task,
and it produces context other workflows can reuse.

## Steps

1. Confirm scope. Is this the whole project, or a named area? If unstated and the request implies "the
   project", use whatever root is available (do not silently narrow or widen it without saying so).
2. Inspect only what is needed to answer the request, starting narrow:
   - Entry points and structure (root config, package manifest, framework markers, folder layout).
   - The specific area named, if any (component, module, flow).
   - Only go broader (full dependency graph, whole-repo read) if the request is explicitly project-wide
     or the narrow read leaves the question unanswered.
3. Identify, with evidence (file:line or file path), as many of the following as are relevant and
   discoverable:
   - Stack/framework, language, package manager, build/test tooling.
   - Architecture and folder responsibilities.
   - Key components, routes, or modules relevant to the request.
   - State management, API/service boundaries, if visible.
   - Design system or styling approach, if visible.
   - Anything that looks explicitly protected or fragile (public API, shared component, auth code) —
     flag it, do not treat that as authorization to touch it.
4. Mark anything you could not confirm as "Unknown, not enough evidence" rather than guessing. Do not
   present an inference as a fact.
5. Do not modify any file. This workflow never reaches the Write Gate.
6. Summarize in the completion report: what the project/scope is, what evidence supports each claim, and
   what remains unknown.

## Output shape
A short structured summary (identity, architecture, notable areas, unknowns) plus the standard
completion report (`templates/completion-report.md`, State changed = unchanged for everything).

## Guardrails
- Never treat this as approval to modify anything discovered.
- Never assert a fact about the codebase without a file reference.
- If the project is large, prefer a scoped map (names, structure, entry points) over reading everything;
  say what was intentionally not read and why.
