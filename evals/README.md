# Evaluating the skills

Checking that a `SKILL.md` has valid structure proves only that it loads. It does not show the skill changes Claude's behavior for the better. These evals measure that by comparing **with the skill** against a **baseline without it** on realistic tasks.

## What is here

Cases live inside the skill they test, in `<skill>/evals/<case-name>/`:

| Skill | Case | Failure it targets |
|---|---|---|
| `qa-engineer` | `honest-report-mixed-failures` | Reporting a clean pass or lumping causes together when there is a real bug, a wrong test, a missing dependency, and a missing secret |
| `qa-engineer` | `ui-tests-failure-paths` | Brittle selectors, no failed-request / visible-error / retry coverage, fixed sleeps, claiming tests pass without running them |
| `developer` | `typo-fix-stays-small` | Heavy process (PR, CI, telemetry, docs, staging) on a one-word fix |
| `developer` | `services-deps-and-processes` | Undeclared vs unused dependencies, and two services with same-named modules colliding in one process |
| `sdlc-orchestrator` | `gate-needs-evidence` | Advancing on skipped tests, a workaround pass, and an un-run security scan |
| `sdlc-orchestrator` | `small-task-no-ceremony` | Running phases and documents for a trivial edit |

Each case folder contains `prompt.md` (what the user types), `case.yaml` (what success looks like), `graders/` (one checkable statement per file) and, where the task needs files, `files/` plus `place-files.sh`. The fixtures are small but deliberately realistic: for example the QA project fails for four different reasons, and the service fixtures really run (verified: apple order returns 200, pear returns 409).

## How to run the comparison

Requires Claude Code with the `claude plugin eval` command (v2.1.269 or later). Runs are real, billed model sessions.

```bash
./evals/run-baseline.sh            # every skill that has evals
./evals/run-baseline.sh developer  # one skill
```

For each case the runner executes the prompt twice, with the skill and without it, grades both against `graders/`, and writes a report under `<skill>/evals/results/`. Copy the numbers into `evals/RESULTS.md`.

You can also run a case by hand: give the contents of `prompt.md` to Claude with and without the skill installed, copy `files/` into an empty working directory first, and score each grader statement as pass or fail.

## How to read the results

- **Delta matters, not the absolute score.** A grader the baseline also passes every time does not show the skill helps; tighten it or drop it.
- **Run each case 3 or more times.** Model output varies, so one run can mislead. Report the pass rate per configuration.
- **Read transcripts for the failures.** A grader failure shows the skill is unclear or incomplete on that point; fix the wording, then rerun.
- **Add cases when you meet a real failure.** Turn it into a fixture and a grader so it cannot regress silently.

## Status

The fixtures and graders are written and the fixtures were checked to behave as designed. **No with/without-skill comparison has been run yet**, so the effectiveness of the current skills is unmeasured until `RESULTS.md` is filled in.
