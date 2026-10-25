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
| developer | typo-fix-stays-small | 1 | 4/4 | 3/4 | Baseline fixed the typo correctly but its reply never said whether the test was run |
| developer | services-deps-and-processes | 1 | 5/5 | 4/5 | Both found the missing PyYAML and ran separate processes. Baseline called flask flatly 'never used' and told the user to drop it without review; the skill run called it a candidate. The baseline ran after the skill run (no port collision) |

Totals over the 9 cases: **with skill 44/45 checks, baseline 40/45**. Mean of per-case pass rates: 97.2% vs 89.4%.
Cost: with-skill runs averaged about 41 s and 87.0k tokens; baseline about 30 s and 82.4k tokens.

## Findings

- The skills clearly help where they add a vocabulary or a rule the model would not use by default: gate states, owner-only waivers, avoiding fixed sleeps in UI tests.
- On honest test reporting the baseline was already strong in this setup, so these graders do not show a benefit. Tighten them (for example require the exact "Planned test doubles / Workarounds used / Not tested" sections) or add harder fixtures.
- The brevity check in `small-task-no-ceremony` is subjective; a five-sentence reply that adds no process should probably pass. Reword the grader.
- Developer: the skill's "candidate, not defect" rule for unused dependencies made a visible difference; the typo case showed no extra process from either side.
- No skill edits were made from these results.

## Limits

- One run each; differences of one check are within noise.
- The same session wrote the skills, ran the comparison and graded it. Graders were applied against the written assertions, and objective checks (selectors, sleeps, fixture hashes, stub cleanup) were done with commands, but an independent review would be stronger.
- `commands.log` files are self-reported by the run agents.
- 17 other roles are unmeasured. The developer cases were run later, in a second batch.
