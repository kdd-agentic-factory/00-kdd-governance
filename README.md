# 00-kdd-governance

Repositorio maestro de gobierno del ecosistema KDD.

Este repositorio define el modelo de gobierno KDD, las politicas de trabajo de los agentes, las plantillas obligatorias, las decisiones arquitectonicas, las metricas de control, el mapa completo de la organizacion y las reglas que deben cumplir todos los demas repositorios.

Su funcion es garantizar que el ecosistema no se convierta en una coleccion de servicios, agentes y dashboards sin trazabilidad. Todo lo que se implemente en los repositorios `01` a `17` debe estar gobernado por este repositorio.

## Principios no negociables

- Ningun agente implementa sin especificacion.
- Ningun servicio se despliega sin diseno.
- Ninguna recomendacion critica se ejecuta sin aprobacion.
- Ningun experimento es valido sin metricas.
- Ningun resultado entra al paper sin trazabilidad.

## Enfoque

KDD adopta Specification-Driven Development como mecanismo de control agentico. Los requisitos funcionales en Markdown actuan como artefacto previo y restrictivo antes de cualquier generacion de codigo.

El flujo obligatorio pasa por:

1. Requisitos.
2. Viabilidad.
3. Diseno.
4. Tareas.
5. Implementacion con TDD.
6. Verificacion as-built.
7. Medicion y trazabilidad.

`AGENTS.md` funciona como archivo maestro de contexto para agentes: un README para maquinas que declara arquitectura, convenciones, permisos, capacidades y politicas aplicables.

## Artefactos de gobierno

| Area | Artefactos |
|---|---|
| Gobierno | `AGENTS.md`, `organization-map.md`, `policies/` |
| Arquitectura | `design.md`, `adr/`, `templates/design.template.md` |
| Ciclo KDD | `kdd-lifecycle.md`, `templates/requirements.template.md`, `templates/feasibility.template.md`, `templates/tasks.template.md`, `templates/as-built.template.md` |
| Control agentico | `agentic-operating-model.md`, `policies/agent-permission-policy.md`, `policies/human-approval-policy.md` |
| Evidencia cientifica | `templates/experiment-card.template.md`, `templates/dataset-card.template.md`, `templates/paper-section.template.md` |
| Metricas | `metrics/kdd-traceability-score.md`, `metrics/documentation-completeness-score.md`, `metrics/agentic-factor-of-safety.md`, `metrics/skill-reuse-ratio.md` |
| Schemas | `schemas/` |
| Workflows | `workflows/` |
| Catalogo | `repo-catalog/` |
| Paper | `paper-alignment/` |
| Diagramas | `diagrams/` |
| Automatizacion | `scripts/`, `.github/` |

## Regla para repositorios `01` a `17`

Cada repositorio del ecosistema debe poder demostrar, antes de implementar o desplegar, que sus cambios tienen:

- Requisito aprobado.
- Viabilidad revisada.
- Diseno aprobado o ADR aplicable.
- Tareas trazadas a requisitos.
- Pruebas definidas antes o junto con la implementacion.
- Evidencia as-built tras el despliegue.
- Metricas que permitan validar resultado, seguridad y valor.

La ausencia de cualquiera de estos artefactos bloquea implementacion, despliegue o uso cientifico del resultado, segun corresponda.

## Papel dentro de la organizacion

`00-kdd-governance` es el repositorio raiz de gobierno. Los repositorios `01` a `17` implementan capacidades concretas, pero sus permisos, artefactos, decisiones, metricas y reglas de operacion nacen aqui.

Este repositorio responde a las preguntas organizativas basicas: como se trabaja, que puede o no puede hacer un agente, que requiere aprobacion humana, como se crea una feature, como se crea una skill, como se valida una AutoSkill, como se documenta una decision, como se mide la trazabilidad, como se integra cada resultado con el paper, que responsabilidad tiene cada repositorio y que significa KDD en este proyecto.

La matriz completa de responsabilidades vive en [organization-map.md](organization-map.md).

## Documentos principales

- [Ciclo de Vida KDD](kdd-lifecycle.md)
- [Principios de Diseno y Arquitectura](design.md)
- [Modelo Operativo Agentico](agentic-operating-model.md)
- [Organigrama y Mapeo de Roles](organization-map.md)
- [Registro de Agentes](AGENTS.md)
- [Estandares de Repositorio](repository-standards.md)
- [Guia de Contribucion](contribution-guide.md)
- [Glosario](glossary.md)
- [Politicas](policies/)
- [Plantillas](templates/)
- [Metricas](metrics/)
- [Schemas](schemas/)
- [Workflows](workflows/)
- [Catalogo de Repositorios](repo-catalog/)
- [Alineacion con Paper](paper-alignment/)
- [Diagramas](diagrams/)
- [Decisiones Arquitectonicas](adr/)
