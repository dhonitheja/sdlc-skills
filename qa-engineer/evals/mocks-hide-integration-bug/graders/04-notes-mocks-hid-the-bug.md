---
type: llm
focus: trace
weight: 1
---

The response points out that the mocked unit tests could not catch this problem because they replace fetch_rate entirely, so the passing unit tests say nothing about the real response shape.
