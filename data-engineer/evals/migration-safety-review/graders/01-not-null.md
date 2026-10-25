---
type: llm
focus: trace
weight: 1
---

The response identifies that adding a NOT NULL column without a default to a table that already has rows will fail, or force a rewrite and lock, and recommends adding it nullable (or with a default), backfilling in batches, then adding the constraint.
