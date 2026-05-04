# KDD Traceability Score

## Function

Measures how many artifacts have complete KDD traceability.

This metric is one of the origin metrics for the paper because it quantifies whether the ecosystem preserves the chain from source data to interpretation, documentation and deployment evidence.

## Formula

```text
KDD Traceability Score =
artifacts with KDD stage + source + transformation + interpretation + documentation
/
total artifacts
```

Percentage form:

```text
KTS = traceable_artifacts / total_artifacts * 100
```

## Complete Traceability Definition

An artifact is traceable only when it has:

- KDD stage.
- Source.
- Transformation record.
- Interpretation record.
- Documentation artifact.

## Scope

Applies to:

- requirements,
- feasibility documents,
- designs,
- tasks,
- datasets,
- model cards,
- experiment cards,
- simulation results,
- race recommendations,
- as-built documents,
- paper evidence.

## Interpretation

| Score | Meaning |
|---|---|
| 95-100% | Strong traceability, paper-ready evidence |
| 80-94% | Acceptable but gaps must be tracked |
| 60-79% | Governance risk |
| < 60% | Not acceptable for critical or paper evidence |

## Paper Use

Use this metric to report how much of the platform output can be traced from data/source to documented interpretation.

---

*Metric from [00-kdd-governance](../README.md)*
