# ADR template (`docs/adr/NNNN-title.md`)

One decision per record. Never edit an accepted ADR; supersede it with a new one.

```markdown
# NNNN. <Short decision title>

Date: YYYY-MM-DD
Status: Proposed | Accepted | Superseded by NNNN | Deprecated

## Context
The forces at play: requirements, constraints, team skills, deadlines, quality attributes that matter here.

## Options considered
| Option | Pros | Cons | Cost / risk |
|---|---|---|---|
| A | | | |
| B | | | |

## Decision
We will <choice>, because <the reason that decided it>.

## Consequences
- Good:
- Bad / accepted trade-offs:
- What we must now do (migration, training, monitoring):

## Revisit when
The measurable trigger that should reopen this decision (for example "more than 50k daily users" or "team grows past 8").
```

Write an ADR for: language/framework, datastore, hosting, auth approach, sync vs async integration, any choice that is expensive to reverse.
