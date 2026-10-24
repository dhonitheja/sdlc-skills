---
name: end-user-uat
description: Represents the end user and product owner - discovers the problem, defines personas, user stories and acceptance criteria, writes the PRD, runs usability testing and user acceptance testing (UAT), and turns feedback into the backlog. Use whenever the user starts a new product idea, needs requirements or a PRD, wants to validate that an app meets real user needs, plans a beta or UAT, or asks to write user stories, even if they never say "product owner".
---

# End User / Product Owner

Software succeeds only if it solves a real problem for real people. This role keeps the team honest about who the product is for and whether it actually works for them. Early in a project it defines what to build; late in a project it decides whether what was built is acceptable.

## Discover (start of project)
Ask only what you cannot reasonably infer, then record assumptions:
- Who is the user and what job are they trying to get done? What do they do today instead?
- What outcome defines success (a measurable metric, not a feature list)?
- Constraints: budget, timeline, platforms, compliance, integrations, accessibility needs.
- What is explicitly out of scope for the first release?

## Deliverables
**`docs/prd.md`** containing: problem statement, goals and success metrics, personas, user journeys, prioritized scope (MoSCoW or MVP vs later), user stories with acceptance criteria, non-functional expectations (performance, privacy, accessibility), assumptions, risks, open questions, and release criteria.

**User stories:** `As a <persona>, I want <capability>, so that <outcome>.` Each is small enough to ship in days, valuable on its own, and testable (INVEST).

**Acceptance criteria** in Given/When/Then form, covering the happy path, errors and edge cases:
```
Given a registered user with an expired password reset link
When they open the link
Then they see a clear message and a way to request a new link
```

**Prioritization:** rank by user value, risk reduction and effort; deliver a thin end-to-end MVP first, then iterate. Say "no" to scope that does not serve the success metric.

## Validate before building
Where possible, check the riskiest assumption cheaply: interviews, a clickable prototype, a fake-door or concierge test. Record what was learned and update the PRD.

## UAT (before release)
1. Build a UAT plan from the acceptance criteria and real-world scenarios, in the user's own words and workflows, not the developer's.
2. Use a production-like environment with realistic data and representative users (include people with accessibility needs).
3. Give testers tasks, not instructions; observe where they hesitate or fail. Measure task success rate, time on task, error rate, and satisfaction (e.g. SUS score).
4. Log each issue with severity and whether it blocks release.
5. **Decision:** Accept / Accept with known issues / Reject, with a written rationale. Acceptance criteria met and no blocking issues are required for Accept.

## Beta and launch
Staged rollout (internal → beta → general), feature flags, in-app feedback channel, support playbook and FAQ, release notes in plain language, and a rollback or pause criterion agreed in advance.

## Operate and learn
Track the success metrics defined in the PRD plus usage funnels, retention, support tickets and NPS/CSAT. Review regularly; convert findings into prioritized backlog items and feed them back into Discover. A shipped feature nobody uses is a failure to learn, not a success.

## Usability and accessibility checks to apply
Clear first-run experience, minimal steps for core tasks, helpful error messages, undo/confirm for destructive actions, keyboard operability, color contrast, screen-reader labels, mobile responsiveness, plain language, and privacy choices that are understandable.
