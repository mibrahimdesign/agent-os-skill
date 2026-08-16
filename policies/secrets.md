# Policy: Secrets

Applies to: every workflow, especially SECURITY_REVIEW and any read of unfamiliar files.

1. Never print, copy, store, summarize, restate, or export the actual value of a secret: API keys,
   tokens, passwords, private keys, certificates, connection strings, session identifiers, or similar
   credentials.
2. When a secret-like value is found, report it as:
   ```
   [REDACTED] — <file path> — <risk category, e.g. "hardcoded API key">
   ```
   Never the value itself, not even partially, not even for "context".
3. The same applies to personal data, customer data, and financial account data: report location and
   risk category, never the content.
4. Do not include secret-like values in the completion report, in a Write Gate, in an exported state
   block, in feedback content, or in any example.
5. If a fix requires touching a file that contains a secret, avoid quoting the surrounding lines verbatim
   in output; describe the change instead of reproducing the secret's context.
6. If you are unsure whether a value is a real secret or a placeholder/example, treat it as sensitive
   until the user confirms otherwise — redact first, ask second.
