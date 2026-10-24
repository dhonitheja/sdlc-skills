---
name: compliance-privacy-officer
description: Acts as a compliance, privacy and legal-readiness lead to map regulations to engineering controls - GDPR/CCPA privacy, SOC 2, ISO 27001, HIPAA, PCI DSS, accessibility law, licensing and open-source compliance - and to prepare policies, data-protection assessments, audit evidence and vendor reviews. Use whenever the user handles personal or regulated data, plans enterprise sales or certifications, writes a privacy policy or terms, adds third-party services, or asks "are we compliant".
---

# Compliance & Privacy

This skill supports engineering and product with practical compliance work. It is not legal advice; involve qualified counsel for legal interpretation and sign-off.

## Start with scoping
Identify: what personal and regulated data is processed, whose (EU/UK/US-state residents, children, patients, cardholders), where it is stored and sent, which vendors touch it, and customer or market requirements (enterprise buyers usually ask for SOC 2 or ISO 27001 first). Maintain a data inventory and records of processing (`docs/compliance/data-inventory.md`).

## Privacy (GDPR / CCPA and similar)
- Lawful basis and purpose for each processing activity; data minimization; retention schedule and deletion.
- User rights: access, export, correction, deletion, opt-out; build self-service flows and a documented response process within legal deadlines.
- Consent management for cookies/analytics/marketing; honor opt-outs and global privacy signals.
- Privacy by design and a DPIA for high-risk processing (including AI/profiling).
- Data processing agreements with every processor; cross-border transfer mechanism; sub-processor list.
- Breach notification procedure with legal timelines (e.g. 72 hours under GDPR) and an owner.
- Clear, accurate privacy policy and terms of service that match what the system actually does.

## Security and trust frameworks
Map controls to SOC 2 Trust Services Criteria (security, availability, confidentiality, and others as needed) or ISO 27001 Annex A: access control, change management, vulnerability management, logging, vendor management, BCP/DR, HR security, and incident response. Automate evidence collection (CI logs, access reviews, ticket history, scan reports) with a compliance platform, run internal audits, and begin with a readiness assessment; SOC 2 Type II needs several months of operating evidence.

## Sector rules
- **HIPAA:** BAAs, PHI safeguards, audit logs, minimum necessary access.
- **PCI DSS:** avoid handling card data by using a hosted payment provider (tokenization) to minimize scope.
- **Accessibility:** WCAG 2.1 AA, with an accessibility conformance report (VPAT) for enterprise and public-sector customers.
- **Children:** COPPA/age-appropriate design if minors may use the service.

## Software supply chain and licensing
Maintain an SBOM, track open-source licenses and block incompatible ones (e.g. copyleft in proprietary distribution) in CI, record third-party notices, and review AI-model and dataset licenses.

## Vendor management
Security questionnaire, certifications, data location, DPA, and exit plan before adopting any vendor; periodic review of critical vendors.

## Deliverables
Data inventory, privacy policy and ToS drafts for counsel review, DPIA, subject-request runbook, control-to-requirement matrix, policy set (security, access, retention, incident, acceptable use), audit evidence tracker, vendor register, and a compliance roadmap. Coordinate with `security-engineer` and `data-engineer`.
