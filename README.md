# 00-kdd-governance

This repository defines the governance layer for the KDD-governed agentic race engineering platform.

It provides:

- KDD lifecycle rules.
- Agent operating model.
- Specification-Driven Development templates.
- Architecture Decision Records.
- Human approval policies.
- Repository catalog.
- Metrics definitions.
- Paper alignment artifacts.
- Safety and traceability rules.

No implementation repository may bypass the governance rules defined here.

## Repository Map

`00-kdd-governance` governs repositories `01` to `17`.

| Layer | Repositories |
|---|---|
| Governance | `00-kdd-governance` |
| Agentic Control | `01-agent-orchestrator`, `02-mcp-gateway`, `04-skills-autoskills-registry`, `07-agentic-workflows` |
| Knowledge and Data | `03-rag-cag-knowledge-layer`, `06-kdd-data-pipelines` |
| Runtime | `10-infra-docker`, `11-infra-kubernetes`, `12-ci-cd-security` |
| Product | `13-ui-command-center`, `15-race-command-center`, `16-race-ai-copilot`, `17-digital-twin-simulation-lab` |
| Research | `08-experimentation-lab`, `14-paper-reproducibility-kit` |

See [organization-map.md](organization-map.md) and [repo-catalog/repositories.yaml](repo-catalog/repositories.yaml).

## KDD Lifecycle

KDD is the administrative lifecycle for data, documents, models, agents, experiments, recommendations and deployments:

1. Selection.
2. Preprocessing.
3. Transformation.
4. Data Mining.
5. Interpretation.
6. Documentation.
7. Deployment.

See [kdd-lifecycle.md](kdd-lifecycle.md).

## SDD Flow

Every feature must follow Specification-Driven Development:

1. `requirements.md`
2. `feasibility.md`
3. `design.md`
4. `tasks.md`
5. tests
6. implementation
7. `as-built.md`
8. ADR update when architecture changes

Templates live in [templates/](templates/). The operational workflow is [workflows/sdd-feature-lifecycle.md](workflows/sdd-feature-lifecycle.md).

## Mandatory Policies

The following policy groups are mandatory:

- Human approval: [policies/human-approval-policy.md](policies/human-approval-policy.md)
- Agent permissions: [policies/agent-permission-policy.md](policies/agent-permission-policy.md)
- Repository governance: [policies/repository-governance-policy.md](policies/repository-governance-policy.md)
- Data governance: [policies/data-governance-policy.md](policies/data-governance-policy.md)
- Model governance: [policies/model-governance-policy.md](policies/model-governance-policy.md)
- AutoSkill validation: [policies/autoskill-validation-policy.md](policies/autoskill-validation-policy.md)
- MCP tool use: [policies/mcp-tool-use-policy.md](policies/mcp-tool-use-policy.md)
- Kubernetes changes: [policies/kubernetes-change-policy.md](policies/kubernetes-change-policy.md)
- Copilot safety: [policies/copilot-safety-policy.md](policies/copilot-safety-policy.md)
- Race engineering decisions: [policies/race-engineering-decision-policy.md](policies/race-engineering-decision-policy.md)
- Telemetry data: [policies/telemetry-data-policy.md](policies/telemetry-data-policy.md)
- Simulation validation: [policies/simulation-validation-policy.md](policies/simulation-validation-policy.md)
- Security: [policies/security-policy.md](policies/security-policy.md)

## How to Create a New ADR

1. Copy [templates/adr.template.md](templates/adr.template.md).
2. Create `adr/ADR-XXXX-short-title.md`.
3. Define context, decision, alternatives and consequences.
4. Link affected repositories and policies.
5. Request review when the decision affects architecture, security, data, deployment or repository boundaries.

## How to Create a New Feature

1. Create requirements with [templates/requirements.template.md](templates/requirements.template.md).
2. Create feasibility with [templates/feasibility.template.md](templates/feasibility.template.md).
3. Create design with [templates/design.template.md](templates/design.template.md).
4. Create tasks with [templates/tasks.template.md](templates/tasks.template.md).
5. Implement with tests.
6. Produce as-built evidence with [templates/as-built.template.md](templates/as-built.template.md).
7. Update metrics and paper evidence if applicable.

## How to Validate an AutoSkill

1. Register the candidate with [templates/autoskill-candidate.template.md](templates/autoskill-candidate.template.md).
2. Follow [workflows/autoskill-validation-lifecycle.md](workflows/autoskill-validation-lifecycle.md).
3. Validate permissions, tests, safety and reuse value.
4. Convert to [templates/skill-card.template.md](templates/skill-card.template.md) only after approval.

## How to Register Paper Evidence

1. Link the result to a research question in [paper-alignment/research-questions.md](paper-alignment/research-questions.md).
2. Register experiment, dataset, model and code version.
3. Use [templates/experiment-card.template.md](templates/experiment-card.template.md), [templates/dataset-card.template.md](templates/dataset-card.template.md), [templates/model-card.template.md](templates/model-card.template.md) and [templates/paper-section.template.md](templates/paper-section.template.md).
4. Store reproducibility evidence in `14-paper-reproducibility-kit`.
5. Record limitations in [paper-alignment/threat-to-validity.md](paper-alignment/threat-to-validity.md).

## Core Documents

- [AGENTS.md](AGENTS.md)
- [design.md](design.md)
- [organization-map.md](organization-map.md)
- [kdd-lifecycle.md](kdd-lifecycle.md)
- [agentic-operating-model.md](agentic-operating-model.md)
- [repository-standards.md](repository-standards.md)
- [contribution-guide.md](contribution-guide.md)
- [glossary.md](glossary.md)
