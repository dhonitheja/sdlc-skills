# Threat model template (`docs/threat-model.md`)

Method: STRIDE per element on a data-flow diagram. Scale effort to the tier: a small change needs only the abuse cases that its change touches.

## 1. System and assets
- Diagram (Mermaid) with trust boundaries marked.
- Assets: data (with classification), credentials, availability, reputation.
- Actors: anonymous user, authenticated user, admin, internal service, third party, attacker.

## 2. Entry points and trust boundaries
| ID | Entry point | Boundary crossed | Authentication |
|---|---|---|---|

## 3. Threats
| ID | Element | STRIDE | Threat (attacker does X to get Y) | Likelihood | Impact | Mitigation | Status | Verified by |
|---|---|---|---|---|---|---|---|---|
Status: Open / Mitigated / Accepted (with owner and expiry). "Verified by" names a test, scan, or review, not an intention.

## 4. Abuse cases
Misuse by legitimate users: enumeration, scraping, replay, privilege escalation, business-logic abuse (coupon stacking, double refunds).

## 5. Residual risk
Accepted risks with who accepted them, why, and when to revisit.

## 6. Review triggers
New data class, new external integration, new auth flow, change to a trust boundary, or a security incident.
