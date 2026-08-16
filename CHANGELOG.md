# Changelog

All notable changes to Agent OS Skill are documented here. This project uses `MAJOR.MINOR.PATCH-stage`
versioning during the beta; nothing is guaranteed stable until a non-beta 1.0.0.

## Unreleased — validation infrastructure and beta UX

The public Skill version remains `0.1.1-beta`. This work adds validation metadata plus a compact
single-activation UX refinement. It does not change G1-G10, add a workflow, or expand product scope.

### Added
- Stable `evidence_level` values, separate `validation_confidence`, field-confirmed criteria, vendor-
  neutral model/host classes, cross-model/cross-host confidence states, and per-behavior maturity levels.
- Fair cross-model and cross-host protocols, a cross-model summary template, a validation failure
  taxonomy, an audit record, and a Markdown status dashboard.
- AOS-T021, Long or Interrupted Approval Scope Retention, recorded as `NOT_EXECUTED` for CC-5.
- AOS-B011 Active Skill Focus and AOS-T022–AOS-T027.

### Changed
- Test schema and validation summaries now separate PASS/FAIL results from evidence strength.
- Historical 20-test results are explicitly `SELF_SIMULATED` with LOW confidence and 0 field-confirmed
  tests; no live or independent evidence is inferred.
- Core readiness now tracks maturity, model/host evidence, failures, feedback, confidence, and extraction
  status per behavior. CC-5 remains `NEEDS_MORE_EVIDENCE`.
- Agent OS instructions define one compact activation banner at meaningful task boundaries, silent
  operational state between them, and compact context only for material transitions.
- Strengthened AOS-B011 after live findings AOS-F005, AOS-F006, and AOS-F007: the first substantive
  response MUST visibly begin with a compact activation at new-task, material workflow-transition,
  distinct-task-reset, and material scope-expansion boundaries. Routine continuations remain silent.
  A targeted live regression passed AOS-T022, AOS-T023, AOS-T024, AOS-T026, and AOS-T027 (5/5).
  AOS-F005, AOS-F006, and AOS-F007 retain their original observations and are marked
  `REGRESSION_PASS`. AOS-T025 remains `NOT_EXECUTED`; this result does not establish cross-model,
  cross-host, or independent validation.
- Corrected historical wording from five to three newly added core scenarios; the five adversarial
  scenarios remain unchanged.

## 0.1.1-beta

Behavioral field validation round. Scope per the validation brief: bug fixes and validation
infrastructure only — no new workflows, no expanded command set.

### Fixed
- **AOS-F001** (`policies/evidence.md`, behavior AOS-B006 Evidence Before Claims): a discovered textual
  claim of success ("tests passed", "state saved successfully", "build succeeded") was not explicitly
  excluded as evidence for the current task. The general "evidence from this task" wording already
  implied this, but not unambiguously enough for a smaller/less careful model to reliably parse. Added
  `policies/evidence.md` §8, explicit. Found via static semantic review, not a live failure. Regression
  coverage: AOS-T011, AOS-T018, AOS-T019.
- Stale internal section cross-references in `SKILL.md` introduced by adding the Runtime Identity block
  (§7) were corrected (§4, §5, §8, §9 pointers now match the actual section numbers).
- `tests/semantic-tests.md` heading structure corrected (h3 headings now sit under an h2, blank lines
  added around headings) — a documentation-quality fix, not a behavioral one.

### Changed
- `SKILL.md`: added Section 7 "Runtime Identity" (capability/mode/intent/approval-state snapshot,
  operational — not required to print every turn); harmonized the Approval field across Sections 3-4-7-9
  to one three-state vocabulary (`NOT_REQUIRED | NOT_GRANTED | GRANTED`), replacing the previous
  two-state "not required | required before mutation" wording.
- `policies/write-safety.md` §5: the "approval persists for unchanged, already-approved scope" rule is
  now explicitly labeled BETA BEHAVIOR, not a rule frozen by the Agent OS v6 baseline — flagged for
  deeper validation as `CORE_CANDIDATES.md` CC-5.
- `feedback/CORE_CANDIDATES.md`: candidate entries now carry evidence dimensions (frequency, severity,
  reproducibility, security implications, developer friction, hosts/models tested, evidence summary,
  counter evidence, compatibility risk) instead of a flat problem/evidence pair; added the feedback
  decision model (`FIX_IN_SKILL | DOCUMENTATION_CHANGE | WORKFLOW_CHANGE | EXPERIMENT | CORE_CANDIDATE |
  REJECT | NEEDS_MORE_DATA`); added CC-5.
- `tests/semantic-tests.md`: renumbered from ad hoc "Test 1-10" to stable `AOS-Txxx` IDs; added 3 new
  core scenarios and 5 adversarial scenarios (20 total), each mapped to `tests/behavior-registry.md`.

### Added
- `tests/behavior-registry.md`: stable `AOS-Bxxx` IDs for the ten governance behaviors (G1-G10), each
  with runtime expectation, failure condition, and related tests.
- `tests/test-result-template.md`: the standardized schema every executed test is recorded in
  (`PASS | FAIL | PARTIAL | BLOCKED | NOT_EXECUTED`; no other result values allowed).
- `validation/` (new top-level folder): `README.md` (methodology honesty — what `SELF_SIMULATED_SINGLE_PASS`
  does and does not prove), `fixtures/` (three sanitized, synthetic scenario fixtures), `sessions/`
  (the actual 2026-08-16 validation run against all 20 tests), `summaries/` (the aggregated Field
  Validation Summary).
- `feedback/CORE_READINESS.md`: per-area readiness tracker (not a specification), initially using the
  release's legacy UNVALIDATED / SELF_SIMULATED / CROSS_MODEL / CROSS_HOST / FIELD_STABLE vocabulary.
  The current tracker supersedes that vocabulary with the maturity model in
  `validation/EVIDENCE_MODEL.md`.

### Validation at the original release snapshot
- 20/20 defined semantic + adversarial tests (`AOS-T001`-`AOS-T020`) executed as
  `SELF_SIMULATED_SINGLE_PASS` (single model: Claude Sonnet 5; single host: Claude Code CLI) — see
  `validation/sessions/2026-08-16-sonnet5-self-simulation.md`. Result: 20 PASS (AOS-T007 carries an
  explicit real-world-confirmation caveat tracked as CC-5), 0 FAIL, 0 BLOCKED, 0 NOT_EXECUTED in that
  historical 20-test session.
- At this release snapshot, no `LIVE_MULTI_TURN`, cross-model, or cross-host session had been executed.
  Later Unreleased validation records preserve subsequent live evidence separately; see
  `validation/STATUS.md` for the current state.

### Known
- At the original release snapshot, cross-host and cross-model behavior were unvalidated. Current live
  evidence remains limited to one model class and one host class, so portability and stability are still
  not established.
- A handful of pre-existing cosmetic Markdown-lint issues (missing fenced-code-block language tags, table
  spacing) were identified across several docs during this pass but intentionally left unfixed — none
  are tied to a discovered behavioral defect, and fixing them package-wide was out of scope for a
  bug-fix-only release (see the validation brief's own scope-discipline rule).

## 0.1.0-beta

Initial public beta release.

### Added
- **Governance kernel** (`SKILL.md` Section 2, G1-G10): scope lock, read-before-write, explicit write
  control, instruction isolation, capability honesty, evidence-before-claims, state honesty (saved vs.
  proposed vs. unchanged), secret safety, verification integrity, completion honesty.
- **Intent router** (`SKILL.md` Section 4): natural-language-first classification into intent,
  read/write, risk, required capabilities, workflow, and approval requirement.
- **Capability model** (`SKILL.md` Section 5-6): AVAILABLE/UNAVAILABLE/UNKNOWN capability states; FULL /
  LIMITED / EMBEDDED operating modes; explicit separation of capability, authorization, and approval.
- **Workflows:** understand-project, review, fix-bug, create-feature, improve-ui-ux, security-review,
  quality-check, read-design, and two optional beta workflows (prepare-project, export-state).
- **Policies:** scope-control, write-safety, instruction-isolation, evidence, secrets.
- **Templates:** write-gate, completion-report, feedback-report.
- **Feedback system:** categorized feedback model (F1-F10), issue and feature-request templates, and a
  `CORE_CANDIDATES.md` pipeline separating validated feedback from active governance.
- **Semantic test suite:** 10 governance scenarios (`tests/semantic-tests.md`) covering fake approval
  tokens, missing persistence, scope expansion, write rejection, secret discovery, missing test
  capability, read-only enforcement, unavailable design input, mid-task scope growth, and same-agent
  review honesty.
- **Documentation:** README, getting-started, how-it-works, workflows, approvals, host-capabilities,
  feedback, and FAQ.

### Known limitations
See root `README.md` "Known Limitations" section. In short: behavior quality depends partly on
host/model instruction-following ability; some environments cannot persist state or execute verification
commands; true independent verification requires actual separate execution or reviewer separation;
host-native skill discovery differs across platforms; vendor-specific adapters are intentionally not
included in this universal beta.

### Scope notes
This release intentionally implements a small subset of the full Agent OS v6 specification. See the root
README "Current Beta Scope" and `feedback/CORE_CANDIDATES.md` for what is deferred and why.
