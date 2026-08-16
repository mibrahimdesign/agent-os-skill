# Workflow: Export State (optional beta command)

Intent: EXPORT_STATE | Read/Write: STRICT READ-ONLY (represents existing state; proposes nothing) |
Typical risk: low
Policies loaded: secrets.md
Triggers on explicit command only: "export state" / "EXPORT STATE". Useful on hosts without persistence
(EMBEDDED mode) so the user can carry task context to another session or host.

## Purpose
Serialize the useful state accumulated in this conversation (task context, decisions made, open items,
proposed-but-not-saved changes) as bounded, portable text the user can save wherever they choose. This
workflow never writes a file itself and never proposes a future state change — it only represents what
already exists in this conversation.

## Steps

1. Collect what exists in this task/conversation: confirmed project facts, decisions made and why, open
   issues, any PROPOSED STATE UPDATE blocks emitted earlier that were never confirmed saved.
2. Apply `policies/secrets.md`: never include a real secret value in the export; redact as usual.
3. Output as bounded blocks, one per logical artifact, so the user can copy each into wherever they
   persist project state:
   ```
   <<<STATE ARTIFACT: session-summary>>>
   ...content...
   <<<END STATE ARTIFACT>>>

   <<<STATE ARTIFACT: decisions>>>
   ...content...
   <<<END STATE ARTIFACT>>>
   ```
4. State plainly that this output is a representation of existing conversation state, not a saved file —
   saving it anywhere is a separate action the user (or a capable host) performs afterward.

## Guardrails
- Never claim this workflow saved anything to disk or any persistent store by itself.
- Never include secrets, credentials, or full source dumps — export summarized, useful state, not raw
  sensitive content.
