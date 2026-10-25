# Architecture document outline (`docs/architecture.md`)

Keep it short enough to be read. Diagrams as text (Mermaid) so they diff in review.

1. **Context and scope**: users, external systems, what is out of scope. C4 level 1 diagram.
2. **Quality attributes**: measurable targets (latency, availability, RPO/RTO, scale, cost ceiling). Rank them; the top three drive the design.
3. **Containers and components**: C4 level 2 and 3. For each: responsibility, owner, tech, data it owns.
4. **Data model and ownership**: entities, who writes them, retention, migration approach (expand/contract).
5. **Interfaces**: API style, versioning, error format, idempotency, rate limits. Link the OpenAPI/schema file.
6. **Key flows**: sequence diagrams for the 3 most important and the 1 most failure-prone path.
7. **Security and privacy**: trust boundaries, authN/authZ, secrets, data classification. Link `docs/threat-model.md`.
8. **Deployment and operations**: environments, CI/CD, observability, backup/restore, scaling.
9. **Risks and open questions**: with owner and date.
10. **Decisions**: index of ADRs.
