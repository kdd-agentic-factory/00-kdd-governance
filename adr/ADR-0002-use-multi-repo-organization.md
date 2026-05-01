# ADR-0002: Organización de Multi-Repositorio

## Estado
Aceptado

## Contexto
Se necesita estructura organizacional clara para múltiples componentes del sistema KDD.

## Decisión
Adoptar una arquitectura de multi-repositorio con separación clara de responsabilidades.

## Justificación
- Proporciona autonomía de equipos
- Facilita control de versiones granular
- Mejora seguridad mediante aislamiento
- Permite escalabilidad independiente

## Consecuencias
- Mayor complejidad en coordinación
- Requiere interfaces claras entre repositorios
- Necesita governance para cambios cruzados

## Estructura de Repositorios
- `00-kdd-governance`: Políticas y estándares
- `01-kdd-architecture`: Diseños técnicos
- `02-kdd-skills`: Habilidades reutilizables
- `03-kdd-agents`: Agentes del sistema
- `04-kdd-data`: Datos y conocimiento
- Repositorios específicos de proyectos

## Referencias
- [README.md](../README.md)
