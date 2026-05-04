# Agent Permission Policy

## Purpose

Define what each agent type may and may not do.

## Principles

- Least privilege.
- Separation of duties.
- Traceable tool use.
- Human approval for critical actions.
- No agent may remove traceability.

## Permission Matrix

| Agent | May | Must Not |
|---|---|---|
| Planner Agent | Read requirements, generate plans, map tasks to artifacts | Write production code, deploy, approve setup changes |
| Builder Agent | Write code in feature branches, write tests, update as-built notes | Deploy, approve PRs alone, change repository boundaries, execute setup changes |
| Reviewer Agent | Review code, tests, security, documentation and policy compliance | Approve race setup changes, bypass human approval, deploy directly |
| Crew Chief Agent | Recommend, summarize telemetry evidence, classify risk, request approvals | Execute real setup changes without human approval, invent evidence, modify models |
| Simulation Agent | Run simulations, compare scenarios, produce validation evidence | Modify real setup, replace human decision authority, publish operational rules directly |
| KDD Admin Agent | Classify artifacts, validate traceability, detect missing governance evidence | Write product code, deploy, approve critical operational decisions |
| Architect Agent | Review designs, propose ADRs, validate repository boundaries | Merge implementation without review, change infrastructure directly |
| Documentation Agent | Generate README, ADR drafts, as-built, reports and paper notes from evidence | Invent results, remove required artifacts, mark unverified evidence as final |
| Experiment Agent | Run approved experiments and record metrics | Use undocumented datasets, publish paper results without reproducibility evidence |
| Root Orchestrator | Coordinate agents, route tasks, request approvals, record audit events | Implement business logic directly, bypass policy gates |

## Tool Permission Categories

| Category | Description | Approval |
|---|---|---|
| Read | Read repositories, documentation, logs and non-sensitive data | Usually not required |
| Write | Modify files, open PRs, update docs or tests | Required when protected artifacts are affected |
| Execute | Run tests, experiments, simulations or workflows | Required for high-risk or production-like execution |
| Deploy | Release to production or cluster runtime | Always requires approval |
| Admin | Change permissions, policies, repositories or security controls | Always requires approval |

## Branch Rule

Builder agents may write only to feature branches or working branches unless a human maintainer explicitly authorizes another target.

## Revocation

Permissions must be revoked when:

- An agent changes responsibility.
- A permission is unused for 90 days.
- A policy violation occurs.
- The owning repository is retired.

---

*Part of [00-kdd-governance](../README.md)*
