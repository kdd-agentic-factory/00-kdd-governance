# Race Engineering Decision Policy

## Purpose

Govern recommendations and decisions related to setup, tires, brakes, electronics, engine maps, telemetry interpretation and safety-affecting parts.

## Decision Classes

| Class | Meaning | Approval |
|---|---|---|
| informational | Describes evidence or system state without recommending action | Not required |
| advisory | Suggests an interpretation or option for human review | Not required, but evidence required |
| actionable | Recommends a concrete setup, strategy, model or component change | Required |
| critical | May affect safety, production operation, engine map, braking, tires or race execution | Required before execution |

Only `informational` and `advisory` outputs may be produced without approval. `actionable` and `critical` recommendations require human approval before execution.

## Required Evidence

Every recommendation must include:

- selected telemetry or data source,
- preprocessing performed,
- features used,
- pattern or model output,
- metric or confidence value,
- risk level,
- affected component,
- approval requirement,
- documentation output.

## Critical Domains

Approval is mandatory for recommendations involving:

- setup changes,
- tire strategy changes during operation,
- brake configuration,
- electronics,
- engine maps,
- safety-affecting parts,
- model changes used in operational prediction,
- simulation outputs used as substitutes for human decisions.

## Execution Rule

Agents may generate a setup change request, crew chief report or simulation evidence. Agents must not execute a real setup change, publish a critical operational rule or modify a race model without explicit human approval.

## Required Artifacts

- `templates/crew-chief-report.template.md`
- `templates/setup-change-request.template.md`
- `templates/experiment-card.template.md` when the recommendation is experimental
- `templates/model-card.template.md` when a model is involved

---

*Part of [00-kdd-governance](../README.md)*
