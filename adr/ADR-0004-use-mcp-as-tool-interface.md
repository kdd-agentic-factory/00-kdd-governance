# ADR-0004: Uso de MCP como Interfaz de Herramientas

## Estado
Aceptado

## Contexto
Los agentes necesitan acceso consistente a herramientas y servicios externos.

## Decisión
Adoptar MCP (Model Context Protocol) como protocolo estándar para la interfaz de herramientas de agentes.

## Justificación
- Proporciona interfaz estándar entre agentes y herramientas
- Facilita integración de nuevas herramientas
- Mejora portabilidad de agentes
- Estandariza logging y auditoría de llamadas

## Consecuencias
- Todas las herramientas deben exponer interfaz MCP
- Requiere adaptadores para herramientas legacy
- Habilita composición flexible de herramientas

## Herramientas Soportadas
- Control de repositorios (Git)
- Sistemas de base de datos
- APIs externas
- Servicios de computación

## Referencias
- [agentic-operating-model.md](../agentic-operating-model.md)
