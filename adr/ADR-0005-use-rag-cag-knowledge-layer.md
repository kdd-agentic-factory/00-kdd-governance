# ADR-0005 — Use RAG/CAG Knowledge Layer

## Status

Accepted

## Context

Agents need both stable context and dynamic evidence. Stable governance rules, architecture decisions and repository maps should be available without repeated prompt expansion. Dynamic evidence such as telemetry, experiment results, model cards and paper notes must be retrieved with source traceability.

Using only model memory or prompt text increases hallucination risk and weakens evidence tracking.

## Decision

Use a combined RAG/CAG knowledge layer:

- RAG retrieves dynamic, source-grounded knowledge.
- CAG provides stable cached context for governance, policies, repository maps and operating rules.

## Consequences

Positive consequences:

- Reduces hallucinations by grounding responses in retrieved sources.
- Separates stable governance context from dynamic evidence.
- Improves traceability of recommendations and paper claims.
- Allows agents to work with smaller prompts while still following governance.
- Enables evidence-linked crew chief reports and experiment summaries.

Negative consequences:

- Requires indexing, freshness checks and source quality controls.
- Retrieval failures must be detected and handled.
- Cached context must be versioned and invalidated when governance changes.

## Alternatives Considered

### Prompt-only knowledge

Rejected because it creates token pressure and stale context.

### RAG-only knowledge

Rejected because stable governance context would be repeatedly retrieved and could vary across runs.

### Static documentation only

Rejected because agents need operational access to dynamic evidence.

## Related Repositories

- `00-kdd-governance`
- `03-rag-cag-knowledge-layer`
- `05-documentation-agent`
- `06-kdd-data-pipelines`
- `08-experimentation-lab`
- `14-paper-reproducibility-kit`
- `16-race-ai-copilot`

## Paper Alignment

This decision supports the paper by providing a traceable knowledge architecture that links governance context, retrieved evidence and generated recommendations.
