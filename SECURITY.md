# Security Policy

## Supported version

Agent OS Skill `0.1.2-beta` is the current supported Beta. It is experimental and is not a security
certification or a substitute for project-specific security controls.

## Reporting a security issue

If GitHub Private Vulnerability Reporting is enabled for the repository, use it for vulnerabilities or
sensitive reports. If no private channel is available, do not post secrets, exploit details, private
source, customer information, or internal URLs in a public issue. Open a minimal sanitized issue asking
the maintainers to provide a private reporting channel.

For non-sensitive behavioral failures, use the [issue template](feedback/ISSUE_TEMPLATE.md).

Include, when safe:

- affected Skill version and behavior/test IDs;
- model class, host class, operating mode, and relevant capabilities;
- sanitized reproduction steps, expected behavior, and observed behavior;
- whether approval, instruction isolation, secrets, state, evidence, or completion honesty was affected.

Never include real credentials or proprietary repository content in validation artifacts.
