# ADR-0004 — Use MCP as Tool Interface

## Status

Accepted

## Context

Agents need to access repositories, databases, documentation systems, experiment runners, telemetry sources, observability platforms and external services. Direct tool access would make permissions, auditability and tool behavior inconsistent.

## Decision

All agent access to external tools must pass through MCP-compatible interfaces or an approved MCP gateway.

## Consequences

Positive consequences:

- Tool access is decoupled from agent implementation.
- Permissions can be controlled centrally.
- Tool calls can be logged and audited.
- External integrations can be replaced without changing agent logic.
- Security policies can be enforced at the gateway boundary.

Negative consequences:

- Legacy tools may require adapters.
- MCP gateway availability becomes operationally important.
- Some direct integrations may need refactoring.

## Alternatives Considered

### Direct API access from agents

Rejected because it fragments permissions and audit logs.

### Custom tool protocol

Rejected because it increases maintenance cost and reduces interoperability.

### Manual-only tool execution

Rejected because it prevents scalable agentic workflows.

## Related Repositories

- `00-kdd-governance`
- `01-agent-orchestrator`
- `02-mcp-gateway`
- `09-observability-platform`
- `12-ci-cd-security`
- `16-race-ai-copilot`

## Paper Alignment

This decision supports the paper by making tool use observable, permissioned and traceable, which is necessary for reproducible agentic workflows.
