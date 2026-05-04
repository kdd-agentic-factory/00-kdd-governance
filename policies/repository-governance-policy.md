# Repository Governance Policy

## Purpose

Define how repositories are created, modified, governed and retired.

## Scope

This policy applies to all repositories `00` to `17` and any future repository added to the KDD organization.

## Repository Creation Requirements

Every repository must have:

- README.
- `AGENTS.md`.
- Clear owner.
- Purpose and repository layer.
- Maturity level.
- Minimum tests.
- CI pipeline.
- Security scan when dependencies or containers exist.
- Governance references to `00-kdd-governance`.

## Repository Modification Requirements

An ADR is required when a change:

- changes the repository map,
- creates a new repository,
- retires a repository,
- changes dependency direction,
- changes ownership boundaries,
- moves responsibilities between repositories,
- introduces a new runtime, platform or critical integration.

## Required Metadata

Repository metadata must be registered in:

- `repo-catalog/repositories.yaml`
- `repo-catalog/dependency-map.yaml`
- `repo-catalog/ownership-map.yaml`
- `repo-catalog/maturity-map.yaml`

## Maturity Levels

| Level | Meaning |
|---|---|
| planned | Defined but not implemented |
| bootstrap | Initial structure exists |
| active | Used with basic traceability |
| mature | Used with metrics, CI and operational evidence |
| retired | Archived and not used for new work |

## Minimum CI

Each implementation repository must include:

- test execution,
- lint or static validation,
- dependency/security checks when applicable,
- governance artifact check when applicable.

## Forbidden Changes

Repositories must not:

- assume responsibilities assigned to another repository without ADR,
- remove README or `AGENTS.md`,
- disable CI without approval,
- introduce unowned services,
- bypass governance rules from `00-kdd-governance`.

---

*Part of [00-kdd-governance](../README.md)*
