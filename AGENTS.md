# AGENTS.md

## Mission

You are operating inside a KDD-governed, multi-agent, race engineering software factory.

The platform combines:

- KDD governance.
- RAG/CAG knowledge retrieval.
- MCP tool access.
- Skills and AutoSkills.
- Docker and Kubernetes orchestration.
- Race Command Center.
- Local Ollama AI Copilot.
- Digital Twin Simulation Lab.
- Scientific reproducibility kit.

## Mandatory Rule

No agent may write production code, modify infrastructure, create a deployment, update a model, or generate a race engineering recommendation without a traceable artifact.

## Mandatory SDD Flow

Every feature must follow:

1. `requirements.md`
2. `feasibility.md`
3. `design.md`
4. `tasks.md`
5. tests
6. implementation
7. `as-built.md`
8. ADR update if architecture changes

## Forbidden Actions

Agents must not:

- deploy to Kubernetes without approval;
- modify production setup recommendations without crew chief approval;
- invent telemetry evidence;
- create AutoSkills directly in production;
- bypass MCP when using external tools;
- modify repository boundaries without ADR;
- remove documentation or traceability files;
- execute destructive commands without explicit approval.

## Required Answer Pattern

When an agent proposes a change, it must include:

1. Objective.
2. KDD stage.
3. Repository affected.
4. Required artifacts.
5. Required skills.
6. Required MCP tools.
7. Approval requirement.
8. Validation method.
9. Documentation output.

## Repository Context Index

| Repository | Purpose |
|---|---|
| `00-kdd-governance` | Governance, policies, ADRs, templates |
| `01-agent-orchestrator` | Multi-agent orchestration |
| `02-mcp-gateway` | Tool connectivity |
| `03-rag-cag-knowledge-layer` | Knowledge retrieval and cached context |
| `04-skills-autoskills-registry` | Reusable skills |
| `05-documentation-agent` | Documentation generation |
| `06-kdd-data-pipelines` | Data lifecycle and pipelines |
| `07-agentic-workflows` | Workflow definitions |
| `08-experimentation-lab` | Scientific validation |
| `09-observability-platform` | Metrics, logs and traces |
| `10-infra-docker` | Local runtime |
| `11-infra-kubernetes` | Scalable runtime |
| `12-ci-cd-security` | CI/CD and security |
| `13-ui-command-center` | UI component system |
| `14-paper-reproducibility-kit` | Paper and reproducibility |
| `15-race-command-center` | Operational dashboard |
| `16-race-ai-copilot` | Local Ollama copilot |
| `17-digital-twin-simulation-lab` | Simulation and what-if validation |

## Policy Index

- Human approval: `policies/human-approval-policy.md`
- Agent permissions: `policies/agent-permission-policy.md`
- MCP tool use: `policies/mcp-tool-use-policy.md`
- Copilot safety: `policies/copilot-safety-policy.md`
- Race engineering decisions: `policies/race-engineering-decision-policy.md`
- Simulation validation: `policies/simulation-validation-policy.md`
- Security: `policies/security-policy.md`

## Agent Output Rule

Agent outputs must be documented in the artifact that corresponds to the KDD stage. Recommendations must include evidence, risk level, approval requirement and the repository where follow-up work belongs.

---

*Part of [00-kdd-governance](README.md)*

<!-- INSFORGE:START -->
## InsForge backend

This project uses [InsForge](https://insforge.dev): an all-in-one, open-source Postgres-based backend (BaaS) that gives this app a database, authentication, file storage, edge functions, realtime, an AI model gateway, and payments through one platform.

- **Skills:** these InsForge skills are installed for supported coding agents. Reach for them before implementing any InsForge feature instead of guessing the API:
  - `insforge`: app code with the `@insforge/sdk` client (database CRUD, auth, storage, edge functions, realtime, AI, email, and Stripe payments).
  - `insforge-cli`: backend and infrastructure via the `insforge` CLI (projects, SQL, migrations, RLS policies, storage buckets, functions, secrets, payment setup, schedules, deploys).
  - `insforge-debug`: diagnosing failures (SDK/HTTP errors, RLS denials, auth and OAuth issues) and running security or performance audits.
  - `insforge-integrations`: wiring external auth providers (Clerk, Auth0, WorkOS, Better Auth, etc.) for JWT-based RLS, or the OKX x402 payment facilitator.
  - `find-skills`: discovering additional skills on demand.
- **Credentials:** app code reads keys from `.env.local`; the CLI reads `.insforge/project.json`. Never hardcode or commit keys.

Key patterns:

- Database inserts take an array: `insert([{ ... }])`.
- Reference users with `auth.users(id)`; use `auth.uid()` in RLS policies.
- For storage uploads, persist both the returned `url` and `key`.
<!-- INSFORGE:END -->
