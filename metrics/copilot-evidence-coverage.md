# Copilot Evidence Coverage

## Function

Measures how many copilot responses include verifiable evidence.

This metric is used to evaluate whether the local copilot provides grounded assistance rather than unsupported claims.

## Formula

```text
Copilot Evidence Coverage =
responses with verifiable evidence
/
total responses
```

Percentage form:

```text
CEC = responses_with_verifiable_evidence / total_responses * 100
```

## Verifiable Evidence Definition

A response has verifiable evidence when it links to at least one of:

- telemetry source,
- dataset card,
- experiment card,
- model card,
- simulation record,
- ADR,
- policy,
- paper evidence artifact,
- traceable repository commit or PR.

## Interpretation

| Coverage | Meaning |
|---|---|
| 95-100% | Required for critical recommendations |
| 85-94% | Acceptable for advisory use |
| 70-84% | Needs grounding improvement |
| < 70% | Not acceptable for operational use |

## Paper Use

Use this metric to measure evidence grounding for `16-race-ai-copilot` and any agent-facing conversational UI.

---

*Metric from [00-kdd-governance](../README.md)*
