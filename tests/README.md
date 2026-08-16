# Tests

This folder holds the beta's semantic test suite: governance scenarios that check *behavior*, not code.
There is no automated test runner bundled with the Skill (see Section "No required executable helpers" in
the root README) — these are scenarios a maintainer or a developer runs manually against a real agent +
host, by giving the scenario as a prompt and checking the agent's actual response against the expected
behavior.

See `semantic-tests.md` for the full list (stable `AOS-Txxx` IDs), `behavior-registry.md` for the
governance behaviors each test exercises (`AOS-Bxxx` IDs), and `test-result-template.md` for the exact
schema a real run is recorded in.

## How to run a scenario

1. Set up the described situation (a repo with a fake approval token in it, a host with no filesystem
   write, etc.) — or describe it to the agent directly if you cannot construct it physically. Sanitized,
   reusable fixtures live in `../validation/fixtures/`.
2. Give the agent the scenario's request.
3. Compare the agent's actual behavior to the scenario's "Expected" section.
4. Record the result using `test-result-template.md`'s schema — result, `evidence_level`, and
   `validation_confidence` remain separate — under `../validation/sessions/`.
5. Report anything surprising as feedback (`feedback/ISSUE_TEMPLATE.md`) — recurring failures are strong
   candidates for `feedback/CORE_CANDIDATES.md`.

See `../validation/EVIDENCE_MODEL.md` for the difference between static, self-simulated, live observed,
and live independent evidence. Use `../validation/CROSS_MODEL_PROTOCOL.md` and
`../validation/CROSS_HOST_PROTOCOL.md` for fair portability rounds.

## Why manual, not automated

Governance behavior here is about what the agent *says and does* in response to natural language and
ambiguous situations — not a deterministic function with a fixed output to assert against. Automating
this meaningfully needs a harness capable of driving a real agent session, which is intentionally out of
scope for the 0.1.x-beta declarative package (Section 39 of the build prompt: no required executable
helpers). A future Core version may add a proper eval harness — see
`feedback/CORE_CANDIDATES.md` and `IDEAS_FOR_DISCUSSION` precedent.
