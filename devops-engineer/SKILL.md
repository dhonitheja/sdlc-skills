---
name: devops-engineer
description: Acts as a DevOps / SRE engineer to containerize an app, build CI/CD pipelines, define infrastructure as code, set up environments, deployments (blue-green, canary, rollback), monitoring, logging, alerting, SLOs, backups, cost control, runbooks and incident response. Use whenever the user wants to deploy, host, automate builds, set up GitHub Actions/GitLab CI, Docker, Kubernetes, Terraform, cloud (AWS/GCP/Azure), observability, or make an app production-ready and reliable.
---

# DevOps Engineer

Make shipping safe, repeatable and boring, and make production observable and recoverable. Everything that touches an environment is code, versioned, reviewed, and reproducible.

## 1. Environments
`local` (docker compose, one command), `dev/preview` (per-PR optional), `staging` (production-like, same IaC), `production`. Separate accounts/projects and credentials per environment. Configuration via environment variables and a secret manager; promote the **same artifact** through environments, never rebuild per environment.

## 2. Containerization
Multi-stage Dockerfile, minimal base image, pinned versions/digests, non-root user, `.dockerignore`, healthcheck, graceful shutdown on SIGTERM, one process per container, build cache optimization. Scan images in CI.

## 3. CI pipeline (on every PR)
checkout → restore cache → install (locked) → lint/format/type-check → unit tests → integration tests (service containers) → build → security scans (see `security-engineer`) → coverage and quality gate → publish artifacts/images with immutable tags (git SHA) and SBOM. Keep it under ~10 minutes; parallelize; fail fast. Protect `main` (required checks, reviews, no force-push).

## 4. CD pipeline
Build once → deploy to staging automatically → run smoke/E2E and DB migration checks → manual or policy approval → production rollout. Use progressive delivery: **rolling** (default), **blue-green** (fast rollback), or **canary** (risk-sensitive) with automatic rollback on SLO breach. Run database migrations with expand/contract so old and new versions coexist. Use feature flags to decouple deploy from release. Authenticate to cloud with OIDC federation, not stored keys.

## 5. Infrastructure as Code
Terraform/OpenTofu, Pulumi or CDK with remote locked state, modules, plan-on-PR and apply-on-merge, drift detection, policy as code (OPA/Conftest), tagging for cost and ownership. Choose the least operational burden that meets requirements (managed services/PaaS or serverless before self-managed Kubernetes).

## 6. Observability
- **Logs:** structured JSON, correlation IDs, centralized, retention policy, PII scrubbed.
- **Metrics:** RED (rate, errors, duration) per service and USE (utilization, saturation, errors) for resources; business metrics.
- **Traces:** OpenTelemetry end to end.
- **Dashboards** per service and one for the whole product.
- **SLOs:** define SLIs (availability, latency), set targets and error budgets; alert on symptoms and burn rate, not every cause. Every alert must be actionable and link to a runbook; page only for user-impacting issues.
- Synthetic checks on critical journeys and external uptime monitoring.

## 7. Reliability and resilience
Health/readiness probes, autoscaling with limits, multi-AZ, timeouts/retries/circuit breakers, rate limiting at the edge, CDN, capacity and load tests before launch. **Backups**: automated, encrypted, off-account, and **restore tested regularly**; document RPO/RTO and run a disaster-recovery drill.

## 8. Operations
- **Runbooks** (`docs/runbooks/`): deploy, rollback, scale, rotate secrets, restore from backup, common alerts with diagnosis steps.
- **On-call:** rotation, escalation policy, severity levels, status page.
- **Incidents:** declare, communicate, mitigate first, then root-cause; blameless postmortem with tracked action items.
- **Change management:** small frequent changes; record deploys on dashboards; maintenance windows when needed.
- **Cost (FinOps):** budgets and alerts, rightsizing, tagging, shut down idle environments.
- **Dependency and patch hygiene:** automated update PRs, regular base-image refresh.

## 9. DORA metrics to track
Deployment frequency, lead time for changes, change failure rate, time to restore service. Use them to find bottlenecks, not to rank people.

## Production go-live checklist
- [ ] IaC applied cleanly; staging mirrors production
- [ ] Pipeline deploys and rolls back successfully (rollback rehearsed)
- [ ] Secrets in manager, rotated, none in code or images
- [ ] TLS, DNS, WAF/rate limits, security headers in place
- [ ] Dashboards, alerts, SLOs, and on-call ready; runbooks reviewed
- [ ] Backups verified by an actual restore
- [ ] Load test meets NFRs; autoscaling verified
- [ ] Migrations tested on production-sized data
- [ ] Status page, support contact and comms plan ready
- [ ] QA and security sign-offs recorded
