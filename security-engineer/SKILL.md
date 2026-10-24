---
name: security-engineer
description: Acts as an application and cloud security engineer to threat-model a design, set secure coding requirements, review code and configuration for vulnerabilities, configure SAST/DAST/SCA/secret scanning, harden infrastructure, manage vulnerabilities, and prepare for compliance and incident response. Use whenever the user asks about security, auth, secrets, OWASP, compliance (SOC 2, GDPR, HIPAA, PCI), pen-test readiness, hardening, or "is this secure", and during the Design, Build, Verify and Release phases of any project.
---

# Security Engineer

Security is a set of controls chosen by risk and verified continuously, not a final audit. Shift left: finding a flaw in design costs a fraction of finding it in production. This skill is defensive; it covers building and verifying secure systems.

## 1. Threat modeling (Design phase, output `docs/threat-model.md`)
- Draw data-flow diagrams with trust boundaries; list assets (data, credentials, availability) and actors (users, admins, attackers, insiders, third parties).
- Apply STRIDE per element (Spoofing, Tampering, Repudiation, Information disclosure, Denial of service, Elevation of privilege).
- Rate each threat (likelihood x impact), assign a mitigation, owner, and a test that verifies it. Revisit when the design changes.
- Classify data (public, internal, confidential, regulated) and define handling, retention, and encryption per class.

## 2. Secure design requirements
- **AuthN:** OIDC/OAuth 2.1 via a proven provider; MFA; strong password hashing (Argon2id/bcrypt) if local; secure session cookies (HttpOnly, Secure, SameSite); short-lived tokens with rotation; account lockout/rate limiting.
- **AuthZ:** deny by default, enforce on the server for every request, object-level checks (prevent IDOR/BOLA), least privilege roles, tenant isolation tests.
- **Data:** TLS 1.2+ everywhere, encryption at rest, field-level encryption for sensitive data, key management via KMS, secrets in a secret manager with rotation.
- **Input/output:** validate on server with allowlists, parameterized queries, output encoding, safe file upload handling, SSRF protections, CSRF defenses, strict CORS, security headers (CSP, HSTS, X-Content-Type-Options, frame protections).
- **Resilience:** rate limits, quotas, request size limits, timeouts.
- **Audit:** log security events (auth, permission changes, data export) with tamper resistance; never log secrets or full PII.
- **Privacy by design:** data minimization, consent, deletion/export flows.

## 3. Secure SDLC controls (put in CI)
| Control | Purpose | Gate |
|---|---|---|
| Secret scanning (gitleaks, pre-commit + CI) | stop leaked credentials | block on finding |
| SAST (Semgrep/CodeQL) | code flaws | block on High+ |
| SCA / dependency audit (OSV, Dependabot, npm/pip audit) | vulnerable libraries | block on Critical/High with fix |
| Container/IaC scan (Trivy, Checkov, tfsec) | misconfig, CVEs | block on High+ |
| DAST (OWASP ZAP) against staging | runtime flaws | review before release |
| SBOM (CycloneDX/Syft) + signed artifacts (cosign), pinned actions/digests | supply chain | required for release |
| Branch protection, required reviews, signed commits | integrity | always |

## 4. Code review focus (map to OWASP Top 10 and ASVS)
Broken access control, cryptographic failures, injection, insecure design, misconfiguration, vulnerable components, auth failures, integrity failures, logging failures, SSRF. Also: mass assignment, unsafe deserialization, race conditions, business-logic abuse, and trust of client-side data. Report each finding with location, impact, proof (safe reproduction), and a concrete fix.

## 5. Infrastructure and cloud hardening
Least-privilege IAM, no long-lived keys, private networking with minimal ingress, WAF, managed DB not publicly reachable, encrypted backups with tested restore, hardened minimal container images running as non-root with read-only filesystems, patching cadence, separate accounts/projects per environment, CIS benchmarks.

## 6. Vulnerability management
Triage by severity and exploitability with SLAs (e.g. Critical 48 h, High 7 d, Medium 30 d). Track in the backlog, document accepted risks with an owner and expiry, and verify fixes with a regression test.

## 7. Incident response and compliance
Maintain an IR plan (detect, triage, contain, eradicate, recover, post-incident review), contact tree, and log retention. Provide a `SECURITY.md` with a disclosure policy. Map controls to the relevant framework (SOC 2, ISO 27001, GDPR, HIPAA, PCI DSS) and keep evidence generated automatically where possible.

## Release security gate
No open Critical/High findings, threat-model mitigations verified, secrets rotated and stored properly, scans green, logging/alerting for security events live, and backup/restore and incident contacts confirmed.
