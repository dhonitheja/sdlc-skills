---
type: llm
focus: trace
weight: 1
---

The response notes that creating an index on a very large table can block writes inside a transaction and recommends CREATE INDEX CONCURRENTLY (or the database's online equivalent), outside the transaction.
