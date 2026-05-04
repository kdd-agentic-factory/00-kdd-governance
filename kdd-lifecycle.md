# KDD Lifecycle

KDD is the organizational lifecycle for the KDD-governed agentic race engineering platform. It applies to data, documents, repositories, agents, sessions, models, experiments, recommendations, simulations and deployment artifacts.

## Selection

Selection defines which data, documents, repositories, sessions, models, telemetry signals or experiments are admitted into the system.

Required artifacts:

- `dataset-card.md`
- source declaration
- ownership metadata
- quality constraints
- intended use

## Preprocessing

Preprocessing prepares raw inputs.

Typical operations:

- timestamp normalization,
- missing data handling,
- signal validation,
- document cleaning,
- metadata extraction,
- outlier detection.

## Transformation

Transformation converts preprocessed data into reusable representations.

Examples:

- telemetry features,
- embeddings,
- vector indexes,
- schemas,
- event contracts,
- simulation inputs.

## Data Mining

Data Mining extracts patterns and models.

Examples:

- clustering,
- anomaly detection,
- tire degradation prediction,
- setup correlation,
- sequence mining,
- simulation-based inference.

## Interpretation

Interpretation translates model outputs into engineering meaning.

Examples:

- setup recommendations,
- crew chief reports,
- risk classification,
- evidence summaries.

## Documentation

Documentation generates traceable artifacts:

- ADR,
- README,
- as-built,
- paper notes,
- experiment cards,
- model cards.

## Deployment

Deployment controls execution:

- Docker,
- Kubernetes,
- CI/CD,
- observability,
- rollback,
- approval gates.

## Specification-Driven Development Overlay

Implementation work must follow:

1. requirements,
2. feasibility,
3. design,
4. tasks,
5. tests,
6. implementation,
7. as-built,
8. metrics and paper evidence when applicable.

## Example: Race Setup Recommendation

| KDD stage | Race engineering application |
|---|---|
| Selection | Select laps, corners, sessions and telemetry signals |
| Preprocessing | Clean outliers, timestamps, gaps and invalid signals |
| Transformation | Compute `spin_ratio`, `lean_angle`, `brake_phase` and `drive_efficiency` |
| Data Mining | Detect degradation, traction loss or setup correlation |
| Interpretation | Propose mapping, rebound or strategy adjustment with risk level |
| Documentation | Generate crew chief report and paper note |
| Deployment | Register the decision and deploy rule/model only after approval |

---

*Part of [00-kdd-governance](README.md)*
