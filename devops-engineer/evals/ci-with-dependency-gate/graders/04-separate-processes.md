---
type: llm
focus: trace
weight: 1
---

The workflow or its smoke test starts the two services as separate processes (each from its own directory or with its own environment), waits for them to be healthy, and stops them. It does not import both services into one process.
