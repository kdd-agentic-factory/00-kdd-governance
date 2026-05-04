# AutoSkill Validation Policy

## Purpose

Define how an AutoSkill moves from candidate to validated reusable skill.

## Scope

This policy applies to all AutoSkills generated, proposed or discovered by agents.

## States

| State | Meaning |
|---|---|
| candidate | Proposed by an agent or workflow |
| under_review | Being evaluated for safety, usefulness and quality |
| validated | Approved for use as a reusable skill |
| rejected | Not approved |
| archived | Retired or preserved for historical evidence |

## Validation Conditions

An AutoSkill may become `validated` only if:

- it has `skill.yaml`,
- it has tests,
- it has documentation,
- it has clear inputs and outputs,
- it does not violate policies,
- it does not require excessive permissions,
- it was approved by a human reviewer,
- it has a skill card,
- it has observable failure modes,
- it records owner and version.

## Required Review

Review must cover:

- functionality,
- security,
- permissions,
- reproducibility,
- documentation,
- test coverage,
- reuse value,
- rollback or deprecation plan.

## Forbidden Promotion

Agents must not promote AutoSkills directly to production or validated state. They may only create candidates and prepare evidence for human review.

## Archival

AutoSkills must be archived when:

- they are superseded,
- they become unsafe,
- they are unused,
- they violate updated policy,
- their dependencies are retired.

---

*Part of [00-kdd-governance](../README.md)*
