---
tokens:
  colors:
    background: "#070A0F"
    surface: "#111827"
    surface_elevated: "#1F2937"
    text_primary: "#F9FAFB"
    text_secondary: "#9CA3AF"
    accent: "#38BDF8"
    success: "#22C55E"
    warning: "#F59E0B"
    danger: "#EF4444"
    critical: "#DC2626"

  typography:
    primary: "Inter"
    mono: "JetBrains Mono"

  spacing:
    base: 4
    dense: 8
    regular: 16
    section: 24

  radius:
    card: 12
    panel: 16
---

# Design Principles

This file defines the global visual contract for the KDD-governed agentic race engineering platform.

The system must use a dark, high-density, race engineering visual language.

The interface must prioritize:

- telemetry readability,
- safety-critical alerts,
- fast comparison between sessions,
- minimal visual noise,
- predictable color semantics,
- accessibility,
- high information density.

## Semantic Colors

| Token | Meaning |
|---|---|
| `success` | Validated, approved or healthy state |
| `warning` | Degraded, uncertain or review-required state |
| `danger` | Unsafe, failed or blocked state |
| `critical` | Immediate human attention required |
| `accent` | Selection, focus or active telemetry channel |

## Typography

- Use `Inter` for operational UI.
- Use `JetBrains Mono` for telemetry tables, logs, traces, identifiers and numeric comparison.
- Avoid oversized display text in dashboards.

## Layout Rules

- Dashboards must be dense but scannable.
- Safety metrics must remain visible in primary workflows.
- Recommendation panels must show evidence, confidence, risk and approval status.
- Comparison views must align lap, sector, corner and signal references.
- Critical alerts must not compete with decorative elements.

## Critical Components

- Telemetry table.
- Session comparison chart.
- Recommendation evidence panel.
- Approval gate control.
- Risk badge.
- Model confidence indicator.
- Paper evidence link.
- Audit trail view.

## Do

- Use red only for critical or unsafe states.
- Use amber for warnings.
- Use green for validated states.
- Use monospaced typography for telemetry tables.
- Always show evidence behind recommendations.
- Keep interaction paths predictable for crew chief review.

## Do Not

- Do not use decorative gradients.
- Do not hide safety metrics in secondary menus.
- Do not represent predictions as facts.
- Do not show setup recommendations without risk level.
- Do not use color alone to communicate safety state.
- Do not generate dashboards that overload users with unranked alerts.

---

*Part of [00-kdd-governance](README.md)*
