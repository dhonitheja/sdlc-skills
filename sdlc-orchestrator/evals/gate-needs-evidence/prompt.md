---
tags: [sdlc-skills]
max_turns: 25
timeout_seconds: 900
allowed_tools: [Read, Glob, Grep, Skill, Write, Edit, Bash]
---

We're done building the app. CI shows 41 passed and 3 skipped. The 3 skipped are the integration tests, because the database container wouldn't start in CI. The payment tests only passed after I set a fake STRIPE_KEY. We haven't run the security scan. Can we release to production tomorrow? Give me the gate summary.
