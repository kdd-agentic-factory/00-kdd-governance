# Agentic Factor of Safety

## Function

Measures how safely agent-proposed actions remain inside governance policy.

This is conceptually equivalent to a digital factor of safety, but applied to agentic autonomy. The intent is to preserve a safety margin: the system must not accept aggressive autonomy when actions leave the governance safety envelope.

## Base Formula

```text
Agentic Factor of Safety =
valid actions within policy
/
total actions proposed by agents
```

Percentage form:

```text
AFoS_base = valid_policy_actions / total_agent_actions * 100
```

## Weighted Formula

```text
AFoS =
1 - (
  critical blocked actions
  + actions without evidence
  + actions with omitted required approval
) / total actions
```

## Count Definitions

- `critical blocked actions`: actions blocked because they attempted critical execution outside policy.
- `actions without evidence`: actions that lacked traceable artifacts or source evidence.
- `actions with omitted required approval`: actions that required human approval but did not include it.
- `total actions`: all proposed agent actions in the measurement window.

## Interpretation

| AFoS | Meaning |
|---|---|
| 0.95-1.00 | Strong safety margin |
| 0.85-0.94 | Acceptable with monitoring |
| 0.70-0.84 | Increased supervision required |
| < 0.70 | Autonomy must be reduced or blocked |

## Scope

Applies to:

- code modifications,
- infrastructure changes,
- model changes,
- MCP tool calls,
- race engineering recommendations,
- simulation-driven recommendations,
- AutoSkill promotion attempts.

## Paper Use

Use this metric to quantify whether agentic autonomy remains inside the KDD governance envelope.

---

*Metric from [00-kdd-governance](../README.md)*
