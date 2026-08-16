# Cross-Model Validation Protocol

Use this protocol to compare Agent OS Skill behavior across materially different model classes without
silently favoring one model. This protocol prepares future validation; it does not claim that any
cross-model run has occurred.

## Model groups

- Group A — `STRONG_REASONING`
- Group B — `CODING_FOCUSED`
- Group C — `SMALL_OR_LOCAL`
- Use `OTHER` only when none of the conceptual groups fit, and explain why.

Actual model names remain session metadata. Governance rules must not depend on a vendor name.

## Fixed comparison inputs

For one comparison round, keep all of the following identical:

1. Skill version and exact Skill files.
2. Synthetic project fixture and starting state.
3. Test request wording and expected behavior.
4. Test order where the host permits it.
5. Host and capability assumptions, including operating mode.
6. Approval behavior, including when and how the live operator replies.
7. Result schema from `tests/test-result-template.md`.
8. Timeouts, retry policy, and permitted tools.

If a fixed input cannot remain identical, record the difference before interpreting results. Do not
silently normalize away a model's failure or a host limitation.

## Execution procedure

1. Start each model in a clean conversation with only the same required Skill modules and scenario
   context.
2. Record actual model, `model_class`, host, `host_class`, operating mode, and relevant capability states.
3. Run the same semantic suite against the same sanitized fixtures. A live comparison requires actual
   host/runtime execution and observation; reasoning through expected output is `SELF_SIMULATED`, not a
   cross-model field result.
4. Give the same user replies at approval and scope-change points where possible.
5. Do not silently coach one model more than another. Record every corrective clarification, retry, or
   manual steering event in `developer_interventions` as a non-negative count and explain it in `notes`.
6. Record `result`, `evidence_level`, and `validation_confidence` independently for each test.
7. Classify failures with `validation/FAILURE_TAXONOMY.md`; do not assume a model failure proves a
   governance defect.
8. Have a separate evaluator review the evidence before using `LIVE_INDEPENDENT`. A second reasoning pass
   by the executing agent does not qualify.
9. Aggregate the round with `validation/templates/cross-model-summary.md`.

Interventions reduce direct comparability. They do not automatically invalidate a run, but the summary
must explain their nature and impact.

## Required comparison metrics

Record a supported assessment and evidence for:

- Routing Accuracy
- Scope Compliance
- Write Gate Compliance
- Instruction Isolation
- Capability Honesty
- Evidence Honesty
- State Honesty
- Verification Honesty
- Completion Accuracy
- Developer Intervention Count

Optional metrics:

- Context Friction
- Repeated Approval Friction
- Task Completion Quality

Do not collapse these metrics into one opaque score. A material governance failure can outweigh a high
aggregate pass count.

## Cross-model decision

Apply the states in `validation/EVIDENCE_MODEL.md`. `MULTI_MODEL` requires live passing evidence from at
least two materially different model classes. `CROSS_MODEL_STABLE` additionally requires repetition,
intended-class coverage, acceptable intervention, and no unresolved material failure.

After a round, a valid release recommendation is `NO RELEASE NEEDED`. Consider 0.1.2-beta only if live
evidence identifies a real instruction-clarity or deterministic-routing change worth making. Do not
create a release merely to follow a roadmap.

## Privacy

Use synthetic fixtures. Do not record private source code, repository content, secrets, internal URLs,
customer information, personal information, sensitive company information, or machine-specific paths.
Sanitize any evidence derived from a real project before it enters this repository.
