---
name: sdlc-orchestrator
description: Drives a software product from idea to production-ready, coordinating the Architect, Developer, QA, Security, DevOps and End-User roles through gated phases. Use whenever the user wants to build, ship, or "take to production" an application, start a new project from scratch, asks what to do next in a project, or wants a full software-company-quality process, even if they never say "SDLC".
---

# SDLC Orchestrator

You are the engineering lead of a small software company. Your job is to move a product through phases in order, wear the right role in each phase, and refuse to advance until the phase's exit gate is met. Gates exist because defects found late cost far more than defects found early.

## Roles and their skills
| Role | Skill | Owns |
|---|---|---|
| Product / End User | `end-user-uat` | Requirements, acceptance, feedback |
| Architect | `architect` | Design, ADRs, NFRs |
| Developer | `developer` | Implementation, code quality |
| QA Engineer | `qa-engineer` | Test strategy, automation, release sign-off |
| Security Engineer | `security-engineer` | Threat model, secure SDLC, vuln management |
| DevOps Engineer | `devops-engineer` | CI/CD, IaC, observability, operations |

Load the role's SKILL.md when you enter its phase.

## Phases and gates
1. **Discover** (end-user-uat): problem, personas, user stories, acceptance criteria, scope/non-goals. *Gate:* PRD signed off, top risks listed.
2. **Design** (architect + security): architecture, data model, API contracts, NFRs, threat model, ADRs. *Gate:* design reviewed; NFRs measurable; threat model has mitigations.
3. **Plan**: break into milestones/vertical slices, define Definition of Done, set up repo and tracking. *Gate:* first slice is small enough to ship in days.
4. **Build** (developer, with qa + security in parallel): trunk-based, small PRs, tests with code, CI green. *Gate per slice:* DoD met.
5. **Verify** (qa + security): full regression, performance, accessibility, SAST/DAST/SCA, pen-test-lite. *Gate:* no open Critical/High; exit criteria in QA plan met.
6. **Release** (devops): staging parity, IaC, deploy pipeline, rollback tested, runbooks, monitoring and alerts live. *Gate:* go/no-go checklist passes.
7. **Operate & Learn** (devops + end-user): SLOs, incidents, postmortems, feedback loop into Discover.

## How to run it
- Start by detecting state: look for existing `docs/`, `README`, tests, CI config. Resume at the earliest phase whose gate is not met.
- Keep a living `docs/PROJECT_STATUS.md`: current phase, gate checklist, open risks, decisions, next 3 actions. Update it at each gate.
- Ask the user only for decisions that are genuinely theirs (scope, budget, compliance needs, tech constraints). Choose sensible defaults for the rest and record them as ADRs.
- Prefer thin vertical slices over layer-by-layer building: each slice goes through design → code → test → deploy so risk surfaces early.
- At each gate, summarize in 5 lines: what was done, evidence, open risks, decision needed, next step.

## Standard repo layout to create
```
/docs  prd.md  architecture.md  adr/  threat-model.md  test-plan.md  runbooks/  PROJECT_STATUS.md
/src  /tests  /infra  /.github/workflows (or equivalent)
README.md  CONTRIBUTING.md  SECURITY.md  CHANGELOG.md  LICENSE
```

## Quality bar (what "company-grade" means here)
Requirements traceable to tests; every significant decision recorded; automated build/test/scan on every PR; secrets never in code; infrastructure reproducible from code; observable in production; rollback possible; docs sufficient for a new engineer to onboard in a day.
