# Test plan template (`docs/test-plan.md`)

## 1. Scope
In scope, out of scope, and the requirement IDs covered.

## 2. Risk-based priorities
| Area | Risk (likelihood x impact) | Test depth |
|---|---|---|

## 3. Test levels
| Level | What it covers | Tools | Runs when | Real or mocked dependencies |
|---|---|---|---|---|
Write every planned mock here ("payment gateway mocked in unit tests; real sandbox in nightly integration"). A mock listed here is a planned test double; one added after a failure is a workaround and is reported as such.

## 4. Environments and data
Environment, test accounts, seed data, secrets and who issues them. A missing secret is an environment restriction, not a test failure.

## 5. Entry and exit criteria
- Entry: build green, environment up, data seeded.
- Exit: required checks Passed, no open Critical/High defects, Not tested list reviewed.

## 6. Traceability
| Requirement | Test case(s) | Level | Last result (Passed / Failed / Blocked / Not tested) |
|---|---|---|---|

## 7. Failure-path coverage
For each user-facing flow: server error, network failure, validation error, timeout, retry, duplicate submission.

## 8. Reporting
Use the result format in `SKILL.md`: totals, cause per failure, planned test doubles, workarounds, Not tested.
