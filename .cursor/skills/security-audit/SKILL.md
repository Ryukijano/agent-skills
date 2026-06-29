---
name: security-audit
description: >-
  Security audit checklist for code review. Use when the user wants to check for
  vulnerabilities, audit access control, review authentication, or ensure OWASP
  compliance.
---

# Security Audit

## OWASP Top 10 Checklist
1. **Injection**: Validate all inputs, use parameterized queries
2. **Broken Authentication**: Strong passwords, MFA, session management
3. **Sensitive Data Exposure**: Encrypt at rest and in transit
4. **XXE**: Disable external entity processing in XML parsers
5. **Broken Access Control**: Verify authorization on every request
6. **Security Misconfiguration**: Disable debug, default credentials, verbose errors
7. **XSS**: Sanitize output, use CSP headers, escape user input
8. **Insecure Deserialization**: Validate serialized data integrity
9. **Known Vulnerabilities**: Check dependencies (pip audit, npm audit)
10. **SSRF**: Validate and restrict outbound URLs

## Audit Process
1. Map the attack surface (endpoints, inputs, auth boundaries)
2. Check each input for validation and sanitization
3. Review authentication and session management
4. Verify authorization checks on all protected resources
5. Check for sensitive data in logs, errors, or responses
6. Scan dependencies for known CVEs
7. Review configuration files for secrets or insecure defaults

## Common Vulnerabilities
- Hardcoded secrets in source code
- SQL injection via string concatenation
- Path traversal via unsanitized file paths
- Insecure random number generation (use `secrets` not `random`)
- Missing rate limiting on auth endpoints

## Tools
- `pip audit` — Python dependency scanner
- `bandit` — Python security linter
- `npm audit` — Node.js dependency scanner
- `gitleaks` — Secret scanner for git repos
