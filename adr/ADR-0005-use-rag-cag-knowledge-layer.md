# ADR-0005: Uso de RAG/CAG para Capas de Conocimiento

## Estado
Aceptado

## Contexto
Los agentes requieren acceso a conocimiento contextual para tomar mejores decisiones.

## Decisión
Implementar capas de conocimiento usando RAG (Retrieval-Augmented Generation) y CAG (Contextual-Augmented Generation).

## Justificación
- Mejora calidad de decisiones de agentes
- Reduce alucinaciones del LLM
- Facilita especialización de agentes
- Centraliza gestión de conocimiento

## Consecuencias
- Requiere infraestructura de vector databases
- Necesita procesos de validación del conocimiento
- Mejora significativa en explicabilidad de decisiones

## Tipos de Conocimiento
- Políticas organizacionales
- Histórico de decisiones
- Datos de dominio
- Patrones de arquitectura
- Lecciones aprendidas

## Referencias
- [repositories-governance-policy.md](../policies/repository-governance-policy.md)
