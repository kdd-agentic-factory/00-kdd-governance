# ADR-0010 — Use Ollama Local Copilot

## Status

Proposed

## Context

Race engineering workflows may run in environments where latency, connectivity, privacy and operational resilience matter. A local conversational copilot can support pitwall, box or edge workflows without depending entirely on cloud inference.

The copilot must remain governed: it may assist analysis and recommendations, but it must not execute critical operational changes without approval.

## Decision

Use Ollama as the local AI copilot runtime for approved race engineering assistance scenarios.

## Consequences

Positive consequences:

- Lower latency for local interaction.
- Better privacy for sensitive telemetry and operational context.
- Reduced dependency on cloud availability.
- Better fit for box, pitwall and edge AI workflows.
- Easier experimentation with local models under controlled governance.

Negative consequences:

- Local model quality may vary by hardware and model version.
- Model updates require governance and validation.
- Local inference must still respect evidence, safety and approval policies.

## Alternatives Considered

### Cloud-only copilot

Rejected because it increases dependency on connectivity and may create privacy constraints for telemetry.

### No conversational copilot

Rejected because it reduces the ability to explain evidence and support rapid engineering review.

### Custom local inference runtime

Rejected initially because Ollama provides a simpler operational baseline.

## Related Repositories

- `00-kdd-governance`
- `03-rag-cag-knowledge-layer`
- `13-ui-command-center`
- `15-race-command-center`
- `16-race-ai-copilot`
- `17-digital-twin-simulation-lab`

## Paper Alignment

This decision supports the paper by enabling local, governed AI assistance for race engineering workflows while preserving privacy, evidence grounding and approval constraints.
