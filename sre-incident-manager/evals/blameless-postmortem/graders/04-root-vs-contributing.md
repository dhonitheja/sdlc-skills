---
type: llm
focus: trace
weight: 1
---

It separates the root cause (bad migration dropped an index) from contributing factors (no canary or staged rollout, alert paged the wrong team, 15 minutes between the alert and the checkout on-call noticing, slow diagnosis).
