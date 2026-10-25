# PRD template (`docs/prd.md`)

Fill every section. If a section does not apply, write "None" and why. Size to the task: a small feature needs sections 1, 3, 5, 6 and 8 only.

## 1. Problem
Who has it, how often, what it costs them today. Evidence (interviews, tickets, data), not opinion.

## 2. Users and personas
For each persona: goal, context, current workaround, technical comfort.

## 3. Goals and success metrics
| Goal | Metric | Baseline | Target | How measured | By when |
|---|---|---|---|---|---|

## 4. Non-goals
What this release deliberately does not do, and why.

## 5. Scope (MoSCoW)
- Must:
- Should:
- Could:
- Won't (this release):

## 6. User stories with acceptance criteria
**US-1** As a <persona>, I want <capability>, so that <outcome>.
- Given <state>, when <action>, then <observable result>.
- Given <failure state>, when <action>, then <clear error and recovery>.

## 7. Non-functional requirements
Performance, availability, security, privacy, accessibility, supported platforms. Each one measurable (for example "p95 under 300 ms at 100 requests per second").

## 8. Risks, assumptions, open questions
| Item | Type (risk / assumption / question) | Owner | Resolve by |
|---|---|---|---|

## 9. Launch and rollback
Rollout plan, support readiness, analytics events, the criterion that pauses or rolls back the launch.

## Review checklist
- Every Must story has at least one failure-path criterion.
- Every metric has a baseline or says how one will be taken.
- Non-goals are written down.
