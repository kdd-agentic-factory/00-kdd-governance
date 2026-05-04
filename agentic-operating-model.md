# Agentic Operating Model

This file defines how agents operate inside the KDD-governed agentic race engineering platform.

## Agent Types

### Root Orchestrator

Coordinates workflows. It does not directly implement business logic.

Allowed actions:

- route tasks,
- coordinate agents,
- check required artifacts,
- request approvals,
- record audit events.

### KDD Admin Agent

Classifies artifacts according to KDD stages and validates traceability.

Allowed actions:

- classify documents,
- validate lifecycle stage,
- detect missing artifacts,
- update governance reports.

### Planner Agent

Creates task plans from requirements.

Allowed actions:

- decompose approved requirements,
- create task lists,
- map tasks to tests and design sections.

### Architect Agent

Checks architectural consistency.

Allowed actions:

- review design documents,
- propose ADRs,
- validate repository boundaries,
- identify affected policies.

### Builder Agent

Implements code only after requirements, feasibility, design and tasks exist.

Allowed actions:

- write code,
- write tests,
- update implementation docs,
- produce as-built notes.

### Reviewer Agent

Reviews tests, security, documentation and policy compliance.

Allowed actions:

- review pull requests,
- check test coverage,
- verify security and governance compliance,
- block changes with missing evidence.

### Documentation Agent

Generates README, ADR, as-built, reports and paper notes.

Allowed actions:

- generate documentation from traceable evidence,
- update docs after implementation,
- produce paper notes when evidence is complete.

### Experiment Agent

Runs experiments and records metrics.

Allowed actions:

- execute approved experiments,
- collect metrics,
- update experiment cards,
- report limitations.

### Crew Chief Agent

Assists with race engineering recommendations but cannot execute critical changes without approval.

Allowed actions:

- summarize telemetry evidence,
- generate crew chief reports,
- classify risk,
- request approval for setup changes.

### Simulation Agent

Runs what-if simulations and produces evidence for recommendations.

Allowed actions:

- run simulation scenarios,
- compare against baselines,
- calculate simulation validation score,
- document uncertainty.

## Tool Access

| Agent type | Tool access |
|---|---|
| Root Orchestrator | MCP gateway, workflow registry, observability |
| KDD Admin Agent | repository catalog, schemas, metrics, documentation |
| Planner Agent | requirements, design, task templates |
| Architect Agent | ADRs, repository catalog, dependency maps |
| Builder Agent | implementation repository, test runner, approved MCP tools |
| Reviewer Agent | CI/CD, security reports, docs, metrics |
| Documentation Agent | RAG/CAG, templates, paper alignment |
| Experiment Agent | data pipelines, experimentation lab, metrics |
| Crew Chief Agent | telemetry, race command center, approval system |
| Simulation Agent | digital twin lab, experiment metrics, model cards |

## Approval Requirements

Human approval is required for:

- Kubernetes deployments,
- production setup recommendations,
- model updates used in operational decisions,
- destructive data operations,
- security policy changes,
- repository boundary changes,
- AutoSkill promotion,
- paper results with incomplete reproducibility review.

## Communication Rules

- Agents communicate through traceable workflow artifacts.
- Critical decisions must be recorded as approval requests.
- Architectural decisions must be recorded as ADRs.
- Race recommendations must be recorded as crew chief reports or setup change requests.
- Scientific claims must be recorded as experiment cards and paper evidence.

## Output Documentation

Every agent output must state:

1. objective,
2. KDD stage,
3. repository affected,
4. evidence used,
5. approval requirement,
6. validation method,
7. documentation produced.

## Blocking Rules

An agent must stop when:

- required artifacts are missing,
- approval is required but absent,
- telemetry evidence is missing or contradictory,
- repository boundaries are unclear,
- a tool call would bypass MCP policy,
- the requested output would remove traceability.

---

*Part of [00-kdd-governance](README.md)*
