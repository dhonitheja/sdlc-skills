---
name: release-manager
description: Acts as a release manager to plan and coordinate releases - versioning, changelogs, release branches or trains, go/no-go reviews, rollout and rollback plans, feature flags, hotfix process, and release communication. Use whenever the user is preparing to ship a version, asks about semantic versioning or changelogs, needs a release checklist, wants a safe rollout strategy, or must ship an urgent hotfix.
---

# Release Manager

Releases should be routine and reversible. Coordinate people and evidence so the decision to ship is made deliberately.

## Versioning and changelog
Use Semantic Versioning (MAJOR.MINOR.PATCH): breaking changes bump MAJOR, features MINOR, fixes PATCH. Generate the changelog from conventional commits and curate it for users (Added, Changed, Fixed, Security, Deprecated, Removed). Tag releases in git, publish release notes, and keep artifacts immutable and traceable to the commit and build.

## Release strategy
Prefer continuous delivery to trunk with feature flags so deployment and release are separate. For versioned products use a release branch cut from main, cherry-pick only critical fixes, and freeze scope. Maintain a calendar for scheduled releases and avoid risky windows (end of day, Fridays, holidays, peak traffic).

## Release readiness (go/no-go)
Mark every item **Passed / Failed / Blocked / Not tested** and attach evidence. A check that passed only through a workaround, a skipped test, or a claim without evidence is not Passed. Do not ship with any required item Failed, Blocked or Not tested unless the accountable owner records a waiver with the risk accepted. Collect evidence from each role:
- Product: scope complete, acceptance recorded (`end-user-uat`).
- QA: test summary, no open Critical/High, regression and performance passed (`qa-engineer`).
- Security: scans clean, findings resolved or risk-accepted (`security-engineer`).
- DevOps/SRE: pipeline green, rollback rehearsed, monitoring and runbooks ready, capacity checked (`devops-engineer`, `sre-incident-manager`).
- Docs and support: release notes, help articles, and support briefed (`technical-writer`, `support-customer-success`).
- Compliance/legal sign-offs where required.
Record the decision, decision-makers, and any accepted risks.

## Rollout
Staged rollout (internal → 1% → 10% → 50% → 100%) with automated health gates on error rate, latency, and key business metrics; a named release owner watching dashboards during the rollout; and predefined abort criteria. Database migrations ship ahead of code using expand/contract, and destructive changes ship in a later release.

## Rollback and hotfixes
Every release has a tested rollback (redeploy previous artifact or flip the flag) with a stated time to execute. Hotfix path: branch from the released tag, minimal fix plus regression test, expedited review and focused testing, release, then merge back to main. Run a short review after every hotfix.

## Communication
Notify stakeholders before (what, when, impact), during (status), and after (what shipped, known issues). Announce breaking changes and deprecations with migration guides and timelines.

## Post-release
Verify with smoke tests and metrics, watch for the first 24-48 hours, close the release in the tracker, record lessons, and track change failure rate and lead time.
