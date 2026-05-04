# ADR-0010: Use Ollama Local Copilot

- **Estado**: Proposed
- **Fecha**: 2026-05-04

## Contexto

Algunas tareas de asistencia pueden beneficiarse de ejecucion local por privacidad, latencia y control de costes.

## Decision

Permitir un copiloto local basado en Ollama para casos aprobados, sin acceso autonomo a acciones criticas.

## Consecuencias

- El copiloto local debe respetar `copilot-safety-policy.md`.
- Sus recomendaciones deben incluir evidencia y limites de confianza.
- No puede ejecutar cambios criticos sin aprobacion humana.

