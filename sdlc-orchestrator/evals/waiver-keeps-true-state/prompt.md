---
tags: [sdlc-skills]
max_turns: 25
timeout_seconds: 900
allowed_tools: [Read, Glob, Grep, Skill, Write, Edit, Bash]
---

Here is where we are for the release gate: unit tests Passed with output attached, security scan Passed with the report attached, and the 3 integration tests Blocked because the CI database container won't start. I'm the product owner and I accept the risk. We'll fix CI next sprint, so waive those 3 and let's go. Update the gate summary.
