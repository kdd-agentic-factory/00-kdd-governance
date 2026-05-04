# Human Approval Policy

## Purpose

Define which actions require explicit human approval before execution.

## Scope

This policy applies to all agents, workflows and repositories in the KDD-governed race engineering platform.

## Mandatory Human Approval

Human approval is required for:

- Kubernetes deployments.
- Infrastructure changes.
- Destructive GitHub actions, including branch deletion, force push, repository deletion, permission removal or history rewriting.
- AutoSkill publication or promotion to validated/production state.
- Critical setup recommendations.
- Engine map changes.
- Part recommendations that affect safety.
- Model changes used in operational prediction.
- Simulations that would substitute or override human decisions.
- Security policy changes.
- Agent permission changes.
- Production data deletion or irreversible transformation.

## Approval Levels

| Level | Description | Examples |
|---|---|---|
| Minor | Low-risk, reversible, non-operational change | Documentation update, non-behavioral refactor |
| Major | System behavior or architecture may change | New agent feature, model version update, repository boundary change |
| Critical | Safety, production, infrastructure or race decision impact | Kubernetes deployment, setup change, engine map recommendation |

## Required Approval Record

Every approval request must include:

- Request ID.
- Requester.
- Repository affected.
- KDD stage.
- Risk level.
- Evidence.
- Proposed action.
- Rollback or mitigation plan.
- Approver.
- Decision: `approved`, `rejected` or `deferred`.

## Execution Rule

Agents may prepare approval requests, but they must not execute actions requiring approval until the approval record is explicit and traceable.

## Emergency Exception

Emergency actions may proceed only when required to prevent immediate safety, security or data loss. The action must be recorded and reviewed within 4 hours.

---

*Part of [00-kdd-governance](../README.md)*
