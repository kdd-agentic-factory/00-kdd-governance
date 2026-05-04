# Organization Map

This file describes the complete repository organization for the KDD-governed agentic race engineering platform.

## Repository Layers

### Governance Layer

- `00-kdd-governance`

### Agentic Control Layer

- `01-agent-orchestrator`
- `02-mcp-gateway`
- `04-skills-autoskills-registry`
- `07-agentic-workflows`

### Knowledge and Data Layer

- `03-rag-cag-knowledge-layer`
- `06-kdd-data-pipelines`

### Runtime Layer

- `10-infra-docker`
- `11-infra-kubernetes`
- `12-ci-cd-security`

### Product Layer

- `13-ui-command-center`
- `15-race-command-center`
- `16-race-ai-copilot`
- `17-digital-twin-simulation-lab`

### Research Layer

- `08-experimentation-lab`
- `14-paper-reproducibility-kit`

## Repository Responsibilities

| Repository | Purpose |
|---|---|
| `00-kdd-governance` | Governance, policies, ADRs, templates, metrics, schemas and repository catalog |
| `01-agent-orchestrator` | Multi-agent orchestration and workflow coordination |
| `02-mcp-gateway` | MCP tool connectivity and controlled external tool access |
| `03-rag-cag-knowledge-layer` | Knowledge retrieval, cached context and source-grounded responses |
| `04-skills-autoskills-registry` | Reusable skills, AutoSkill candidates and validation records |
| `05-documentation-agent` | Documentation generation and traceability maintenance |
| `06-kdd-data-pipelines` | Data ingestion, validation, preprocessing and transformation |
| `07-agentic-workflows` | Workflow definitions for agents and governed operations |
| `08-experimentation-lab` | Scientific validation, experiment execution and metric collection |
| `09-observability-platform` | Metrics, logs, traces, audit events and alerting |
| `10-infra-docker` | Local runtime and reproducible container environments |
| `11-infra-kubernetes` | Scalable runtime and cluster deployment definitions |
| `12-ci-cd-security` | CI/CD, quality gates, dependency scanning and release security |
| `13-ui-command-center` | Shared UI component system and command center foundation |
| `14-paper-reproducibility-kit` | Paper evidence, reproducibility scripts and result packaging |
| `15-race-command-center` | Operational race dashboard and crew-chief decision support |
| `16-race-ai-copilot` | Local Ollama copilot for race engineering assistance |
| `17-digital-twin-simulation-lab` | Simulation, what-if validation and digital twin evidence |

## Dependency Rules

- Every repository depends on `00-kdd-governance`.
- Product repositories may consume data, knowledge, workflows, observability and runtime services.
- Research repositories may consume experiment, dataset, model and simulation evidence.
- Infrastructure repositories must not depend on product-layer implementation details.
- Data and knowledge repositories must not depend on UI repositories.
- Governance must define rules, not import application code from implementation repositories.

## Allowed Calls

| Caller | May call |
|---|---|
| `01-agent-orchestrator` | `02-mcp-gateway`, `04-skills-autoskills-registry`, `07-agentic-workflows`, `09-observability-platform` |
| `03-rag-cag-knowledge-layer` | `06-kdd-data-pipelines` |
| `05-documentation-agent` | `03-rag-cag-knowledge-layer`, `14-paper-reproducibility-kit` |
| `08-experimentation-lab` | `06-kdd-data-pipelines`, `17-digital-twin-simulation-lab`, `14-paper-reproducibility-kit` |
| `13-ui-command-center` | `09-observability-platform`, product APIs |
| `15-race-command-center` | `03-rag-cag-knowledge-layer`, `09-observability-platform`, `16-race-ai-copilot`, `17-digital-twin-simulation-lab` |
| `16-race-ai-copilot` | `02-mcp-gateway`, `03-rag-cag-knowledge-layer`, `04-skills-autoskills-registry` |

## Forbidden Knowledge

- `10-infra-docker`, `11-infra-kubernetes` and `12-ci-cd-security` must not encode race engineering business rules.
- `16-race-ai-copilot` must not bypass `15-race-command-center` for operational recommendations.
- `17-digital-twin-simulation-lab` must not publish recommendations as operational decisions.
- `14-paper-reproducibility-kit` must not contain untraceable results.
- `00-kdd-governance` must not contain product implementation logic.

## Implementation Order

1. `00-kdd-governance`
2. `10-infra-docker`
3. `12-ci-cd-security`
4. `02-mcp-gateway`
5. `03-rag-cag-knowledge-layer`
6. `04-skills-autoskills-registry`
7. `01-agent-orchestrator`
8. `06-kdd-data-pipelines`
9. `07-agentic-workflows`
10. `09-observability-platform`
11. `08-experimentation-lab`
12. `17-digital-twin-simulation-lab`
13. `13-ui-command-center`
14. `16-race-ai-copilot`
15. `15-race-command-center`
16. `14-paper-reproducibility-kit`
17. `11-infra-kubernetes`

---

*Part of [00-kdd-governance](README.md)*
