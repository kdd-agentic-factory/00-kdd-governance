# ADR-0002 — Use Multi-Repo Organization

## Status

Accepted

## Context

The platform contains governance, orchestration, MCP access, knowledge retrieval, skills, data pipelines, workflows, experimentation, observability, infrastructure, UI, race command, copilot, simulation and paper reproducibility concerns.

Combining all concerns into a single repository would blur ownership, slow independent deployment and make scientific traceability harder to audit.

## Decision

Use a multi-repository organization with explicit repository boundaries, ownership and dependency rules.

## Consequences

Positive consequences:

- Clear conceptual separation between governance, data, agents, runtime, product and research.
- Independent deployment and evolution of runtime, UI, data and experiment components.
- Scientific artifacts can be isolated and reviewed in dedicated repositories.
- Ownership is explicit per repository.
- Security and permissions can be scoped by repository.

Negative consequences:

- Cross-repository changes require coordination.
- Dependency management becomes more important.
- Shared governance must be enforced consistently.

## Alternatives Considered

### Monorepo

Rejected because it would simplify refactoring but weaken conceptual separation and repository-level ownership.

### Repository per micro-feature

Rejected because it would create excessive fragmentation and operational overhead.

### Unstructured repository growth

Rejected because it would make traceability and paper reproducibility fragile.

## Related Repositories

- `00-kdd-governance`
- `01-agent-orchestrator`
- `02-mcp-gateway`
- `03-rag-cag-knowledge-layer`
- `04-skills-autoskills-registry`
- `05-documentation-agent`
- `06-kdd-data-pipelines`
- `07-agentic-workflows`
- `08-experimentation-lab`
- `09-observability-platform`
- `10-infra-docker`
- `11-infra-kubernetes`
- `12-ci-cd-security`
- `13-ui-command-center`
- `14-paper-reproducibility-kit`
- `15-race-command-center`
- `16-race-ai-copilot`
- `17-digital-twin-simulation-lab`

## Paper Alignment

This decision supports the paper by making the organization itself part of the experimental architecture: each repository has a defined responsibility, boundary and evidence role.
