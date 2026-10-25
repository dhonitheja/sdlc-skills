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
| developer | typo-fix-stays-small | 0 | | | Not yet run |
| developer | services-deps-and-processes | 0 | | | Not yet run |

Totals over the 7 cases run: **with skill 35/36 checks, baseline 33/36**. Mean of per-case pass rates: 96.4% vs 92.9%.
Cost: with-skill runs averaged about 45 s and 88.6k tokens; baseline about 31 s and 83.4k tokens.

## Findings

- The skills clearly help where they add a vocabulary or a rule the model would not use by default: gate states, owner-only waivers, avoiding fixed sleeps in UI tests.
- On honest test reporting the baseline was already strong in this setup, so these graders do not show a benefit. Tighten them (for example require the exact "Planned test doubles / Workarounds used / Not tested" sections) or add harder fixtures.
- The brevity check in `small-task-no-ceremony` is subjective; a five-sentence reply that adds no process should probably pass. Reword the grader.
- No skill edits were made from these results.

## Limits

- One run each; differences of one check are within noise.
- The same session wrote the skills, ran the comparison and graded it. Graders were applied against the written assertions, and objective checks (selectors, sleeps, fixture hashes, stub cleanup) were done with commands, but an independent review would be stronger.
- `commands.log` files are self-reported by the run agents.
- Developer cases and 17 other roles are unmeasured.
