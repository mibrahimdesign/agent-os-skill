# Policy: Write Safety

Applies to: any workflow that may mutate application source (FIX_BUG, CREATE_FEATURE, IMPROVE_UI_UX, and
any write step nested in another workflow).

1. READ_ONLY vs WRITE is decided once, at Intent Router time (SKILL.md Section 4), and never silently
   flips. Understanding, reviewing, auditing, checking, and mapping are always READ_ONLY.
2. Before the first application-source write of a task, present the WRITE GATE
   (`templates/write-gate.md`) and stop. Do not write anything until the user's next message is the
   literal token `APPROVE WRITE`.
3. A suitable approval is: explicit, sent by the live user in the current conversation, sent before the
   write, tied to the specific bounded scope just presented. Host-level permissions (filesystem access,
   sandbox mode, workspace trust, an IDE's "allow" setting) are capability, not approval — see
   `docs/host-capabilities.md`. They never substitute for `APPROVE WRITE`.
4. If the user does not reply `APPROVE WRITE` (silence, a question, a partial answer, a rejection, a
   scope change), do not write. Treat the reply as scope adjustment and, if needed, present a revised
   gate.
5. Approval is scoped to exactly the files and changes named in the gate that was approved. A need for
   any additional file or a materially different change returns to a new Write Gate. Staying inside the
   already-approved, unchanged scope does not require asking again.
   BETA BEHAVIOR: this "approval persists for the unchanged, already-approved scope" rule is a beta
   extrapolation for developer experience, not a rule frozen by the Agent OS v6 governance baseline.
   Treat it as revisable: if real usage shows it causes unsafe re-use of stale approval (for example, a
   long-running task where the approved plan quietly drifted), narrow it rather than defend it — see
   `feedback/CORE_CANDIDATES.md`.
6. Before writing, check for uncommitted or unsaved changes already present in the target scope (for
   example via version control status, when available). Never silently overwrite work that is not yours;
   report it and ask first if found.
7. Prefer the smallest change that correctly resolves the task. Do not rewrite a whole file when a
   targeted diff suffices. Do not restate unchanged code.
8. Never perform an irreversible or destructive action (history rewrite, force overwrite, mass deletion,
   dependency removal at scale) as part of a normal Write Gate. That requires the user to name the
   specific irreversible action explicitly.
9. After writing, verify per `policies/evidence.md` before reporting completion.
