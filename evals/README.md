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
| `security-engineer` | `review-finds-real-vulns` | Missing a SQL injection, hardcoded key or weak hashing; flagging safe code as vulnerable; calling a partial review a full audit |
| `architect` | `right-sized-architecture` | Over-engineering a 25-person internal tool; vague non-functional requirements; no data-level double-booking protection |
| `devops-engineer` | `ci-with-dependency-gate` | A CI file with no dependency gate, failing on unused packages, or claiming CI is green without running it |
| `security-engineer` | `subtle-vulns-and-decoys` | Missing unsafe deserialization, path traversal or SSRF; flagging safe code (non-secret `random`, `compare_digest`, `safe_load`); wrong priority order |
| `architect` | `resist-overengineering-pressure` | Going along with Kubernetes/Kafka/microservices for a 5-person team; floating-point money; no idempotency or audit trail |
| `devops-engineer` | `ci-green-but-broken` | Leaving `\|\| true` and `continue-on-error` in place, faking a token or deleting a test to get green, echoing a secret, unpinned actions |
| `qa-engineer` | `time-dependent-test` | Adding retries or skips for a test that depends on the wall clock instead of controlling time |
| `developer` | `bugfix-regression-test-no-collateral` | Fixing a bug without a failing test first, or also "fixing" correct code with a similar-looking condition |
| `sdlc-orchestrator` | `resume-with-unmet-gate` | Silently continuing to build the payment slice when an earlier required gate (threat model) was never met |

| `product-manager` | `prioritize-with-evidence` | Picking by vote count instead of the churn evidence; no success metric |
| `business-analyst` | `ambiguous-requirement` | Restating a one-line feature as requirements without surfacing ambiguities or edge cases |
| `end-user-uat` | `uat-for-real-users` | Testing with developers instead of representative (elderly, low-confidence) users; real patient data in tests |
| `ux-ui-designer` | `form-accessibility-review` | Missing placeholder-only labels, a div button, low contrast (2.32:1), unannounced errors; claiming a full audit |
| `project-manager-scrum-master` | `infeasible-plan` | A plan that pretends 5 deliverables fit in 6 weeks for 3 developers |
| `engineering-manager-tech-lead` | `style-war-and-debt` | Mediating style fights by hand instead of automating; vague refactor advice instead of data-driven debt work |
| `data-engineer` | `migration-safety-review` | Approving a NOT NULL add without default, a destructive DROP COLUMN and a locking index build on huge tables |
| `ai-ml-engineer` | `rag-launch-readiness` | Approving launch from a 5-question demo; no eval set, refusals or safeguards |
| `performance-engineer` | `weak-load-test-claim` | Accepting "50 users for 30 s, average 120 ms" as proof of 10,000 users |
| `sre-incident-manager` | `blameless-postmortem` | Blaming the engineer; inventing impact numbers; vague action items |
| `release-manager` | `go-no-go-with-gaps` | A plain Go despite an irreversible migration, no rehearsed rollback and unprepared support |
| `technical-writer` | `readme-matches-code` | README with invented flags, features, license or untested examples |
| `support-customer-success` | `angry-double-charge` | Promising a refund before checking, asking for full card numbers, no internal ticket |
| `compliance-privacy-officer` | `gdpr-claim-check` | Agreeing that a cookie banner and Irish servers make a company GDPR compliant |

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

The fixtures and graders are written and checked. A with/without-skill comparison (one run per case) now covers all 20 skills: 165/169 checks with the skills vs 146/169 without, over 32 cases. The first 18 cases (95/98 vs 85/98) covered `qa-engineer`, `sdlc-orchestrator`, `developer`, `security-engineer`, `architect` and `devops-engineer`; the other 14 roles have one case each (70/71 vs 61/71). See `RESULTS.md` for the table and caveats.
