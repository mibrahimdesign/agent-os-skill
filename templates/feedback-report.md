# Template: Feedback Report

Use this to capture feedback about the Skill itself (not about the project being worked on). See
`feedback/README.md` for the simple, non-technical version of this same idea.

```
Feedback ID:              <assign sequentially or leave blank for the maintainer to assign>
Skill Version:            0.1.1-beta
Environment:               <host type, OS, general setup — no private paths or names>
Model:                     <model family/size if known, or "unknown">
Workflow:                  <UNDERSTAND | REVIEW | FIX_BUG | CREATE_FEATURE | IMPROVE_UI_UX |
                            SECURITY_REVIEW | QUALITY_CHECK | READ_DESIGN | PREPARE_PROJECT |
                            EXPORT_STATE | other>
Category:                  F1 Workflow friction | F2 Missing behavior | F3 Governance problem |
                            F4 False positive | F5 False negative | F6 Context problem |
                            F7 Host compatibility | F8 Model compatibility |
                            F9 Developer experience | F10 Feature request
Severity:                  Low | Medium | High
User goal:                 <what you were trying to accomplish>
Expected behavior:         <what you expected the agent to do>
Actual behavior:           <what actually happened>
Reproduction:               <the request/steps that triggered it, sanitized of anything private>
Impact:                     <how this affected the task or trust in the output>
Suggested improvement:     <optional>
Candidate Core rule:        <optional — does this look like it should become a permanent rule?>
Status:                     new
```

Before submitting: remove real source code, secrets, customer data, private repository names, internal
URLs, and machine-specific paths. Describe the situation generically if needed.
