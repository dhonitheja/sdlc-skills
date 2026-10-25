# SDLC Skills Pack

**A full software company, packaged as 20 Claude skills.** Give Claude an idea and it works through discovery, design, build, test, security, release and operations the way a real company would, with the right specialist role at each step and a quality gate before moving on.

```
Idea ──► Discover ──► Design ──► Plan ──► Build ──► Verify ──► Release ──► Operate & Learn
          (gate)      (gate)     (gate)   (gate)     (gate)     (gate)         │
            ▲                                                                   │
            └───────────────────── feedback from users and incidents ◄─────────┘
```

## What is a skill?

A skill is a folder containing a `SKILL.md` file: written instructions that teach Claude how to do one kind of work well.

1. **Always loaded:** only each skill's short `name` and `description` (the header at the top of `SKILL.md`). This is how Claude knows which skills exist.
2. **Loaded on demand:** when your request matches a description, Claude reads that skill's full instructions and follows them.
3. **Extras (optional):** a skill can bundle templates, scripts or reference files that Claude reads only when needed.

This keeps Claude fast and focused: it carries 20 short descriptions, but only reads the detailed playbook for the role it is playing right now.

## How this pack works

There are two ways to use it.

**1. Whole-company mode.** Ask Claude to use the orchestrator:

> Use sdlc-orchestrator to build a booking app for dog groomers.

The orchestrator:
1. Checks the project state (docs, code, tests, CI) and resumes at the earliest phase whose gate is not yet met.
2. Puts on the right role for the current phase and loads that role's skill (for example `product-manager` during Discover, `architect` during Design).
3. Produces that phase's deliverables, such as a PRD, architecture doc, ADRs, test plan, threat model or runbooks, in a `docs/` folder.
4. Checks the **exit gate**. If it is not met, it stays in the phase or loops back instead of pushing ahead.
5. Summarizes at each gate: what was done, evidence, open risks, decision needed, next step. It only asks you for decisions that are genuinely yours (scope, budget, compliance, risk acceptance) and records its own defaults as decision records.
6. Keeps a living `docs/PROJECT_STATUS.md` so work can pause and resume across sessions.

**2. Single-role mode.** Call one role directly when you only need that expertise:

> As the security-engineer, threat-model this design.
> Act as the qa-engineer and write a test plan for the checkout flow.
> Use the devops-engineer skill to set up CI/CD for this repo.

## The phases and gates

| # | Phase | Roles involved | Exit gate (must be true to advance) |
|---|---|---|---|
| 1 | Discover | product-manager, end-user-uat, business-analyst | Problem, personas, success metrics, scope and non-goals agreed; requirements testable and traced |
| 2 | Design | ux-ui-designer, architect, security-engineer, data-engineer, compliance-privacy-officer, ai-ml-engineer | Architecture, API and data reviewed; measurable non-functional requirements; threat model with mitigations; privacy obligations mapped |
| 3 | Plan | project-manager-scrum-master, engineering-manager-tech-lead, release-manager | Thin-slice backlog sequenced by risk; Definition of Done and standards set; repo and CI skeleton exist |
| 4 | Build | developer, data-engineer, ai-ml-engineer (+ QA, security, docs in parallel) | Per slice: Definition of Done met, CI green, docs updated |
| 5 | Verify | qa-engineer, performance-engineer, security-engineer, end-user-uat | No open Critical/High defects; performance budgets met; scans clean; user acceptance recorded |
| 6 | Release | release-manager, devops-engineer, sre-incident-manager, support-customer-success | Go/no-go evidence from every function; rollback rehearsed; monitoring, on-call and support ready; backup restore verified |
| 7 | Operate & Learn | sre-incident-manager, devops-engineer, support-customer-success, product-manager | SLOs met; postmortem actions closed; metrics and user feedback flow back into Discover |

Gates exist because a defect caught in requirements costs minutes, while the same defect caught in production costs days.

## The roles

| Function | Skill | What it does |
|---|---|---|
| Orchestration | `sdlc-orchestrator` | Runs the phases, enforces gates, coordinates all roles |
| Product | `product-manager` | Vision, strategy, roadmap, prioritization, metrics, go-to-market |
| | `business-analyst` | Detailed requirements, use cases, business rules, traceability |
| | `end-user-uat` | Personas, PRD, user stories, acceptance criteria, user acceptance testing |
| Design | `ux-ui-designer` | User flows, wireframes, design system, accessibility |
| Delivery | `project-manager-scrum-master` | Planning, estimation, sprints, risks, status reporting |
| | `engineering-manager-tech-lead` | Engineering standards, tech debt, team practices, hiring |
| Engineering | `architect` | Architecture, non-functional requirements, API and data design, ADRs |
| | `developer` | Scaffolding, implementation, tests, pull requests, code review |
| | `data-engineer` | Schemas, migrations, pipelines, analytics, data quality |
| | `ai-ml-engineer` | ML and LLM features, RAG, evals, MLOps, responsible AI |
| Quality | `qa-engineer` | Test strategy, automation, defect management, release sign-off |
| | `performance-engineer` | Performance budgets, profiling, load testing, capacity |
| Security | `security-engineer` | Threat modeling, secure design, scanners in CI, vulnerability management |
| | `compliance-privacy-officer` | GDPR/CCPA, SOC 2, ISO 27001, HIPAA, PCI, licensing, audit evidence |
| Platform | `devops-engineer` | CI/CD, infrastructure as code, environments, observability, backups |
| | `sre-incident-manager` | SLOs, on-call, incident response, blameless postmortems |
| | `release-manager` | Versioning, changelogs, go/no-go, rollout and rollback |
| Docs & customers | `technical-writer` | README, API and user docs, runbooks, release notes |
| | `support-customer-success` | Support readiness, ticket triage, knowledge base, feedback loop |

## Example: what you get at each step

For the prompt "Use sdlc-orchestrator to build a booking app for dog groomers", expect roughly:

1. **Discover:** a few focused questions (who are the users, what counts as success, constraints), then `docs/prd.md`, personas, user stories with Given/When/Then acceptance criteria, and a prioritized MVP.
2. **Design:** `docs/architecture.md` with diagrams, an OpenAPI spec, a data model, a threat model, a UX flow and design tokens, and decision records for stack choices.
3. **Plan:** a sequenced backlog of thin vertical slices, a repo scaffold with linting, tests and CI, and a Definition of Done.
4. **Build and Verify:** code delivered slice by slice with tests, security scans, performance checks and an accessibility review, ending in a QA sign-off report.
5. **Release and Operate:** deployment pipeline and infrastructure code, dashboards, alerts, runbooks, rollback plan, release notes and support articles.

## How reliable are the results?

The skills enforce evidence-based reporting and scale the process to the task:

- **Honest test reporting:** failures are sorted into application bug, test defect, missing dependency, or environment restriction. Planned test isolation (a mock chosen in the test design) is a legitimate pass; a workaround added *after* a failure is never reported as a clean pass, and the original failure stays visible.
- **Gate states:** every gate check is **Passed / Failed / Blocked / Not tested**, with evidence attached. A phase advances when every required check is Passed or a non-Passed check has a recorded waiver. A waiver records who authorized the advance, why, the risk and an expiry; it never changes the check's true state.
- **Task-size tiers:** a typo fix does not trigger PRs, telemetry, dependency audits, clean installs or staging deployment; new products and high-risk changes get the full process.
- **Dependency and environment checks (scaled by tier):** imported-but-undeclared packages are treated as defects; declared-but-unused packages are only candidates for review, because dynamic imports, plugins and build tools escape static analysis. Services run in separate processes.

Whether these changes actually improve Claude's behavior is measured with the cases in [`evals/`](evals/README.md) (with-skill vs baseline).

**First comparison (October 2026, one run per case and configuration, `qa-engineer`, `sdlc-orchestrator`, `developer`, `security-engineer`, `architect` and `devops-engineer`):** 62 of 63 checks passed with the skills, 57 of 63 without. The difference is small and comes from six cases:

- `gate-needs-evidence`: without the skill, Claude gave a sensible NO-GO but did not use the Passed/Failed/Blocked/Not tested states and never said that only the owner can waive a check (4/6 vs 6/6).
- `ui-tests-failure-paths`: without the skill, Claude used fixed `waitForTimeout` sleeps; with it, tests used auto-waiting assertions (5/6 vs 6/6).
- `services-deps-and-processes`: without the skill, Claude told the user to drop `flask` as "never used" with no review; with it, `flask` was flagged as a candidate only (5/5 vs 4/5).
- `typo-fix-stays-small`: without the skill, the reply never said whether the test had been run (4/4 vs 3/4).
- `right-sized-architecture`: without the skill, the design was right-sized but had no numeric response-time, availability or recovery targets (6/6 vs 5/6).
- `small-task-no-ceremony`: the skill version was slightly wordier than the limit set by the check (3/4 vs 4/4). It did not add process.

On six cases (honest mixed failures, planned mocks, mocks hiding a bug, waiver keeps true state, security review, CI setup) the baseline did just as well. Plain Claude already reports honestly when it is asked to. Treat these results as a first signal, not proof: one run each is noisy, the other 14 roles are not yet compared, and a port collision affected one baseline run. Details and caveats are in [`evals/RESULTS.md`](evals/RESULTS.md).

## Install

Each skill is a folder with a `SKILL.md`. Install the folders you want (all 20 for the full company).

- **Claude Code:** copy the folders into `~/.claude/skills/` (personal) or `<your-project>/.claude/skills/` (per project).
- **Claude.ai / desktop app:** zip a skill folder (or package it as a `.skill` file) and upload it under the Skills settings.

```bash
git clone https://github.com/dhonitheja/sdlc-skills
cp -r sdlc-skills/*/ ~/.claude/skills/     # skills only; ignore README
```

### Use with OpenAI Codex

Codex reads the same skill format (a folder with a `SKILL.md` that has `name` and `description`), so these folders can be installed as they are. This has not been tested in Codex.

```bash
git clone https://github.com/dhonitheja/sdlc-skills
mkdir -p ~/.agents/skills
cp -r sdlc-skills/*/ ~/.agents/skills/     # all projects; or copy into <your-repo>/.agents/skills/
```

In Codex, type `$` or run `/skills` to pick one (for example `$sdlc-orchestrator build a booking app for dog groomers`). Codex can also choose a skill by itself when your request matches its description. See [OpenAI's skills documentation](https://learn.chatgpt.com/docs/build-skills) for current install paths. The eval results in this repo were measured with Claude only.

## Customize

- **Stack-specific:** add a `references/` folder inside a skill (for example `developer/references/nextjs-postgres.md`) and mention it in that skill's `SKILL.md`, so Claude reads it only when relevant.
- **Templates:** `product-manager`, `architect`, `security-engineer`, `qa-engineer` and `release-manager` ship fill-in templates in `references/` (PRD, ADR, architecture outline, threat model, test plan, go/no-go). Edit them to match your house style.
- **Company standards:** edit the Definition of Done, severity levels, SLAs or coding standards in the matching skill to reflect your organization.
- **Scale down:** for a small project, install only the roles you need; keep at least the orchestrator, product, architect, developer, QA, security and DevOps skills.

## Limits

- The skills guide Claude's work and produce documents, code and plans; they do not replace human review, legal counsel or an independent security audit. `compliance-privacy-officer` gives engineering support, not legal advice.
- Quality depends on the context you provide. Answer the discovery questions honestly; vague inputs produce generic outputs.
- Gates are only as strong as the evidence behind them. Review the gate summaries rather than approving blindly.

## Contributing

Improve a skill by editing its `SKILL.md`. Keep the description specific about *when* to trigger, keep the body under about 500 lines, explain the reason behind each rule, and move long reference material into a `references/` folder.

## License

Released under the MIT License. See [LICENSE](LICENSE).
