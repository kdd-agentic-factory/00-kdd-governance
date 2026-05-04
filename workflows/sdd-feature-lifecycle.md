# SDD Feature Lifecycle

These are governance process rules, not executable workflows.

```text
Request
-> Requirements
-> Feasibility
-> Design
-> Tasks
-> Tests
-> Implementation
-> Review
-> As-built
-> Documentation
-> Optional ADR
```

## Required Controls

- Requirements must exist before feasibility.
- Design must exist before implementation.
- Tests must be defined before or alongside implementation.
- As-built must close the gap between design and implementation.
- ADR is required when architecture or repository boundaries change.
