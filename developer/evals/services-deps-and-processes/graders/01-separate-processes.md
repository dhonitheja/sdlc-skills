---
type: llm
focus: trace
weight: 1
---

The two services are started as separate processes (for example two python invocations from each service's own directory, or with distinct working directories/PYTHONPATH). They are not imported into a single interpreter or run with a shared sys.path that would make both config.py modules collide.
