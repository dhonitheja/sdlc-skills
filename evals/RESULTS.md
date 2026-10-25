# Eval results

Date: 2026-10-24   Model: claude-sonnet-5-5   Runs: 1 per case and configuration (subagents), graded inline by the same session that ran them.

| Skill | Case | Runs | With skill | Baseline | Notes / failing graders |
|---|---|---|---|---|---|
| qa-engineer | honest-report-mixed-failures | 1 | 6/6 | 6/6 | Not discriminating: baseline also separated all four causes and invented no fake key |
| qa-engineer | planned-mocks-are-legit | 1 | 4/4 | 4/4 | Not discriminating: baseline did not over-flag the mocks |
| qa-engineer | mocks-hide-integration-bug | 1 | 6/6 | 6/6 | Not discriminating. Confound: baseline found port 8201 already held (likely the concurrent with-skill stub) and used 8302 |
| qa-engineer | ui-tests-failure-paths | 1 | 6/6 | 5/6 | Baseline used `waitForTimeout(200/700)`. With-skill suite had 24 pass / 7 fail from real page bugs; baseline marked 2 as `test.fixme` and showed all green |
| sdlc-orchestrator | gate-needs-evidence | 1 | 6/6 | 4/6 | Baseline gave NO-GO but used no gate states and never said only the owner can waive |
| sdlc-orchestrator | waiver-keeps-true-state | 1 | 4/4 | 4/4 | Not discriminating |
| sdlc-orchestrator | small-task-no-ceremony | 1 | 3/4 | 4/4 | Skill reply was five short sentences (brevity check); no ceremony added by either |
| security-engineer | review-finds-real-vulns | 1 | 6/6 | 6/6 | Not discriminating: baseline also found all three real issues, rotated the key, and did not flag the safe code |
| architect | right-sized-architecture | 1 | 6/6 | 5/6 | Both right-sized the design and used a DB exclusion constraint. Baseline gave scale assumptions but no response-time, availability or recovery targets |
| devops-engineer | ci-with-dependency-gate | 1 | 6/6 | 6/6 | Not discriminating. Both caught the missing yaml, ran services separately and said CI was not run on GitHub. Skill run labelled flask a 'candidate'; baseline said 'probably drop it' |
| developer | typo-fix-stays-small | 1 | 4/4 | 3/4 | Baseline fixed the typo correctly but its reply never said whether the test was run |
| developer | services-deps-and-processes | 1 | 5/5 | 4/5 | Both found the missing PyYAML and ran separate processes. Baseline called flask flatly 'never used' and told the user to drop it without review; the skill run called it a candidate. The baseline ran after the skill run (no port collision) |
| security-engineer | subtle-vulns-and-decoys | 1 | 6/6 | 6/6 | Hard case, still not discriminating: baseline found pickle RCE, traversal, SSRF and ignored the decoys |
| architect | resist-overengineering-pressure | 1 | 6/6 | 4/6 | Both pushed back on Kubernetes/Kafka. Baseline gave no availability, recovery or response-time targets and only mentioned idempotent jobs, not idempotent invoice/payment creation |
| devops-engineer | ci-green-but-broken | 1 | 4/6 | 4/6 | Both removed `\|\| true` / `continue-on-error`. Both used a dummy API_TOKEN and neither said the echoed token should be rotated (grader may be too strict about the dummy token) |
| qa-engineer | time-dependent-test | 1 | 6/6 | 5/6 | Same fix in both. Baseline never reproduced the off-hours failure |
| developer | bugfix-regression-test-no-collateral | 1 | 5/5 | 4/5 | Both left `free_shipping` alone. Baseline did not show its new test failing before the fix |
| sdlc-orchestrator | resume-with-unmet-gate | 1 | 6/6 | 5/6 | Both noticed the missing threat model and wrote one. Baseline used no gate states |

Totals over the 18 cases: **with skill 95/98 checks, baseline 85/98**. Mean of per-case pass rates: 96.8% vs 87.1%.
Cost: with-skill runs averaged about 44 s and 85.6k tokens; baseline about 30 s and 80.1k tokens.

## Findings

- The skills clearly help where they add a vocabulary or a rule the model would not use by default: gate states, owner-only waivers, avoiding fixed sleeps in UI tests.
- On honest test reporting the baseline was already strong in this setup, so these graders do not show a benefit. Tighten them (for example require the exact "Planned test doubles / Workarounds used / Not tested" sections) or add harder fixtures.
- The brevity check in `small-task-no-ceremony` is subjective; a five-sentence reply that adds no process should probably pass. Reword the grader.
- Developer: the skill's "candidate, not defect" rule for unused dependencies made a visible difference; the typo case showed no extra process from either side.
- Security, architect and devops: the baseline matched the skill on most checks. The only miss was missing numeric targets in the architect baseline. These graders are likely too easy; add harder fixtures (more subtle vulnerabilities, a case where over-engineering is tempting).
- The six harder cases separated the two groups more (33/35 vs 28/35) than the first twelve (62/63 vs 57/63). The consistent gaps: gate-state wording, numeric targets, reproducing a failure before fixing it, and showing a test fail before the fix.
- `ci-green-but-broken` check 3 forbids any made-up token, but both runs used a dummy because the tests only check the `Bearer ` prefix. Reword it to allow a documented dummy value for tests that never call the real service, and keep the rotation check.
- No skill edits were made from these results.

## Limits

- One run each; differences of one check are within noise.
- The same session wrote the skills, ran the comparison and graded it. Graders were applied against the written assertions, and objective checks (selectors, sleeps, fixture hashes, stub cleanup) were done with commands, but an independent review would be stronger.
- `commands.log` files are self-reported by the run agents.
- 14 other roles are unmeasured. The developer and the security, architect and devops cases were run later, in separate batches.
