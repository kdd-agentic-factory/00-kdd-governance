# Documentation Completeness Score

## Function

Measures how many mandatory documentation artifacts are present.

This metric evaluates whether a feature, repository, experiment or recommendation has the required documentation expected by the KDD governance model.

## Formula

```text
Documentation Completeness Score =
mandatory artifacts present
/
mandatory artifacts expected
```

Percentage form:

```text
DCS = mandatory_artifacts_present / mandatory_artifacts_expected * 100
```

## Mandatory Artifact Examples

For a feature:

- requirements,
- feasibility,
- design,
- tasks,
- tests,
- as-built,
- ADR when architecture changes.

For an experiment:

- experiment card,
- dataset card,
- model card when a model is used,
- metrics,
- paper section or paper note when results are reported.

For a repository:

- README,
- AGENTS.md,
- ownership metadata,
- CI definition,
- maturity level.

## Interpretation

| Score | Meaning |
|---|---|
| 95-100% | Complete |
| 80-94% | Mostly complete |
| 60-79% | Documentation debt |
| < 60% | Governance failure |

## Paper Use

Use this metric to quantify documentation discipline and artifact availability across the KDD-governed platform.

---

*Metric from [00-kdd-governance](../README.md)*
