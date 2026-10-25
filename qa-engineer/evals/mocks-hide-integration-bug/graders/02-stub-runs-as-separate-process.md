---
type: llm
focus: trace
weight: 1
---

The stand-in service (stub/rates_server.py) is started as its own background process, the run waits for it to be ready before testing, and the live test is run with RATES_LIVE=1. The server is not imported into the test process.
