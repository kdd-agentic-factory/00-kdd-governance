# ADR-0001 — Use KDD Governance

## Status

Accepted

## Context

The platform is a multi-repository, multi-agent race engineering software factory. It combines telemetry data, agentic workflows, RAG/CAG knowledge retrieval, MCP tools, skills, AutoSkills, simulation, operational dashboards and academic reproducibility.

Without a governance model, implementation repositories can drift into disconnected services, dashboards and agents with no traceability between data, decisions, models, simulations and paper evidence.

## Decision

The entire organization is governed by KDD. KDD is used as the administrative lifecycle for selecting, preprocessing, transforming, mining, interpreting, documenting and deploying artifacts across the ecosystem.

## Consequences

Positive consequences:

- Requirements, data, models, simulations, recommendations and paper results become traceable.
- Data and model governance are part of the same lifecycle.
- Agent actions are constrained by documented artifacts.
- Scientific evidence can be linked to implementation and operational results.
- Race engineering recommendations must include data, metrics, risk and approval status.

Negative consequences:

- Teams must maintain more documentation.
- Changes are slower when required artifacts are missing.
- Governance checks must be integrated into CI/CD and agent workflows.

## Alternatives Considered

### Ad hoc repository governance

Rejected because it would not provide a shared lifecycle across data, agents, simulation and paper evidence.

### Pure agile issue tracking

Rejected because tickets alone do not preserve traceability from datasets and models to scientific claims.

### Agent-only governance

Rejected because autonomous agents need external constraints, approval rules and auditable artifacts.

## Related Repositories

- `00-kdd-governance`
- `01-agent-orchestrator`
- `06-kdd-data-pipelines`
- `08-experimentation-lab`
- `14-paper-reproducibility-kit`
- `15-race-command-center`
- `17-digital-twin-simulation-lab`

## Paper Alignment

This decision supports the paper contribution by defining KDD as the unifying lifecycle that connects data, agents, simulation, operational recommendations and reproducible academic evidence.
