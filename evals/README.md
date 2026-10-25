# Evaluating the skills

Checking that a `SKILL.md` has valid structure proves only that it loads. It does not show the skill changes Claude's behavior for the better. These evals measure that by comparing **with the skill** against a **baseline without it** on realistic tasks.

## What is here

Cases live inside the skill they test, in `<skill>/evals/<case-name>/`:

| Skill | Case | Failure it targets |
|---|---|---|
| `qa-engineer` | `honest-report-mixed-failures` | Reporting a clean pass or lumping causes together when there is a real bug, a wrong test, a missing dependency, and a missing secret |
| `qa-engineer` | `planned-mocks-are-legit` | Over-correction: flagging a planned mock as a workaround or downgrading a legitimate unit-test pass (also checks that a skipped live test is not counted as a pass) |
| `qa-engineer` | `mocks-hide-integration-bug` | A runnable live test against a local stand-in service: mocked unit tests pass legitimately, the live test fails on a response-shape bug the mocks hid; checks cause classification, separate-process service handling, and not overstating a stub result as vendor verification |
| `qa-engineer` | `ui-tests-failure-paths` | Brittle selectors, no failed-request / visible-error / retry coverage, fixed sleeps, claiming tests pass without running them |
| `developer` | `typo-fix-stays-small` | Heavy process (PR, CI, telemetry, docs, staging, dependency audit, clean install) on a one-word fix |
| `developer` | `services-deps-and-processes` | Undeclared imports as real defects, unused declarations as review candidates only, and two services with same-named modules colliding in one process |
| `sdlc-orchestrator` | `gate-needs-evidence` | Advancing on skipped tests, a workaround pass, and an un-run security scan |
| `sdlc-orchestrator` | `waiver-keeps-true-state` | Rewriting a waived check as Passed, or refusing a legitimate owner waiver; the waiver must be recorded separately and the check keep its true state |
| `sdlc-orchestrator` | `small-task-no-ceremony` | Running phases and documents for a trivial edit |

Each case folder contains `prompt.md` (what the user types), `case.yaml` (what success looks like), `graders/` (one checkable statement per file) and, where the task needs files, `files/` plus `place-files.sh`. The fixtures are small but deliberately realistic: for example the QA project fails for four different reasons, and the service fixtures really run (verified: apple order returns 200, pear returns 409).

## Fixture notes and limits

- **`planned-mocks-are-legit` uses a placeholder URL on purpose.** Its live test points at `rates.example.invalid`, a reserved domain that can never resolve, and is skipped unless `RATES_LIVE=1`. That case tests reporting behavior only: a planned mock is a legitimate pass, and a skipped live test is reported as "real API not exercised", not as a pass. It cannot verify a real integration, and forcing the live test on would fail loudly instead of reaching a real service.
- **`mocks-hide-integration-bug` is the runnable counterpart.** Its live test talks over HTTP to `stub/rates_server.py` on 127.0.0.1:8201, which a run must start as a separate process. The code reads `json["rate"]` while the documented contract nests it under `json["data"]["rate"]`, so the unit tests (mocked) pass and the live test fails with a `KeyError`. Even a passing live run against a local stub only validates the code against the documented contract, not against the vendor's real service; the grader checks that the response says so.
- **Fixtures are checked to behave as intended**, but they are small, synthetic projects. Passing them shows a behavior, not general quality; add cases from real failures over time.

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

The fixtures and graders are written and checked. A first with/without-skill comparison (one run per case) covered `qa-engineer` and `sdlc-orchestrator`: 35/36 checks with the skills vs 33/36 without. The `developer` cases and the other roles are not yet compared. See `RESULTS.md` for the table and caveats.
