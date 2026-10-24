# SDLC Skills Pack - a full software company as Claude skills

20 skills that take an application from idea to production and operations. Start with `sdlc-orchestrator`; it loads the right role at each phase and enforces gates.

| Function | Skill |
|---|---|
| Orchestration | `sdlc-orchestrator` |
| Product | `product-manager`, `business-analyst`, `end-user-uat` |
| Design | `ux-ui-designer` |
| Delivery and leadership | `project-manager-scrum-master`, `engineering-manager-tech-lead` |
| Architecture and engineering | `architect`, `developer`, `data-engineer`, `ai-ml-engineer` |
| Quality | `qa-engineer`, `performance-engineer` |
| Security and governance | `security-engineer`, `compliance-privacy-officer` |
| Platform and reliability | `devops-engineer`, `sre-incident-manager`, `release-manager` |
| Docs and customers | `technical-writer`, `support-customer-success` |

## Install
Copy the folders into your Claude skills directory (each folder contains a `SKILL.md`), or package them with the skill-creator `package_skill` script and upload the `.skill` files.

## Use
"Use sdlc-orchestrator to build <your app>." Or call a role directly: "As the security-engineer, threat-model this design."

## Notes
Compliance guidance is practical engineering support, not legal advice. Add stack-specific reference files (for example Next.js + Postgres on AWS) under each skill's `references/` folder to tailor it.
