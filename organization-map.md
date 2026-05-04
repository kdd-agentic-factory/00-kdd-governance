# Organigrama y Mapeo de Repositorios

Estructura organizacional del ecosistema KDD.

`00-kdd-governance` es el repositorio raiz de gobierno. Define reglas, politicas, plantillas, metricas y decisiones que deben cumplir todos los repositorios `01` a `17`.

```text
00-kdd-governance
    -> define reglas para
01-agent-orchestrator
02-mcp-gateway
03-rag-cag-knowledge-layer
04-skills-autoskills-registry
05-documentation-agent
06-kdd-data-pipelines
07-agentic-workflows
08-experimentation-lab
09-observability-platform
10-infra-docker
11-infra-kubernetes
12-ci-cd-security
13-ui-command-center
14-paper-reproducibility-kit
15-race-command-center
16-race-ai-copilot
17-digital-twin-simulation-lab
```

## Preguntas que Gobierna

Este repositorio debe responder de forma normativa a:

- Como se trabaja en la organizacion.
- Que puede hacer un agente.
- Que no puede hacer un agente.
- Que necesita aprobacion humana.
- Como se crea una feature.
- Como se crea una skill.
- Como se valida una AutoSkill.
- Como se documenta una decision.
- Como se mide la trazabilidad.
- Como se integra cada resultado con el paper.
- Que repositorio tiene cada responsabilidad.
- Que significa KDD en este proyecto.

## Mapa de Responsabilidades

| Repositorio | Responsabilidad principal | Gobernado por |
|---|---|---|
| `00-kdd-governance` | Gobierno raiz, politicas, plantillas, ADRs, metricas, ciclo KDD y reglas agenticas | Si mismo |
| `01-agent-orchestrator` | Orquestacion de agentes, delegacion, ejecucion coordinada y control de flujos agenticos | Politicas de agentes, permisos, aprobacion humana, trazabilidad |
| `02-mcp-gateway` | Puerta de enlace MCP para herramientas, conectores, permisos e interfaces externas | Politicas de seguridad, permisos, auditoria, diseno |
| `03-rag-cag-knowledge-layer` | Capa de conocimiento RAG/CAG, indexacion, recuperacion, contexto y memoria documental | Gobierno de datos, documentacion, trazabilidad de fuentes |
| `04-skills-autoskills-registry` | Registro de skills reutilizables y validacion de AutoSkills | Politicas de skills, validacion, seguridad y reutilizacion |
| `05-documentation-agent` | Generacion, actualizacion y verificacion de documentacion operativa y tecnica | Plantillas obligatorias, README, ADR, as-built, paper notes |
| `06-kdd-data-pipelines` | Pipelines de datos, limpieza, transformacion, validacion y contratos de datos | Gobierno de datos, metricas, trazabilidad de datasets |
| `07-agentic-workflows` | Workflows agenticos de negocio, investigacion y operaciones | Ciclo KDD, aprobaciones, tareas trazables |
| `08-experimentation-lab` | Ejecucion de experimentos, evaluacion de hipotesis y comparativas | Experiment cards, metricas, reproducibilidad |
| `09-observability-platform` | Logs, metricas, trazas, alertas, auditoria y control operacional | Metricas de gobierno, seguridad, auditoria |
| `10-infra-docker` | Runtime local, imagenes, compose, entornos reproducibles | Politicas de despliegue local, seguridad, as-built |
| `11-infra-kubernetes` | Runtime escalable, manifests, charts, despliegues y operaciones cluster | Politica Kubernetes, aprobacion humana, observabilidad |
| `12-ci-cd-security` | Pipelines CI/CD, controles de calidad, escaneo y seguridad automatizada | Politicas de seguridad, repositorios, release controlado |
| `13-ui-command-center` | UI de control, dashboards operativos y supervision humana | Politicas de aprobacion, UX operativa, trazabilidad |
| `14-paper-reproducibility-kit` | Evidencia reproducible para paper, scripts, datasets, resultados y anexos | Plantillas cientificas, trazabilidad, metricas |
| `15-race-command-center` | Centro de mando de carrera, analitica operativa y recomendaciones de setup/estrategia | Aprobacion humana, experimentos, trazabilidad, paper notes |
| `16-race-ai-copilot` | Copiloto de IA para analisis, recomendaciones y asistencia al equipo | Politicas de agentes, restricciones criticas, aprobacion |
| `17-digital-twin-simulation-lab` | Simulacion, digital twins, escenarios y evaluacion predictiva | Experimentacion, metricas, reproducibilidad |

## Roles Principales

### Governance
- Define politicas y decisiones estrategicas.
- Supervisa cumplimiento normativo.
- Mantiene plantillas, metricas y criterios de bloqueo.

### Architecture
- Define diseno de soluciones.
- Documenta decisiones tecnicas arquitectonicas.
- Valida que los servicios no se desplieguen sin SDD o ADR aplicable.

### Operations
- Gestiona operacion, monitoreo y mantenimiento.
- Ejecuta despliegues controlados.
- Mantiene evidencia as-built y auditoria.

### Development
- Implementa features, agentes y skills.
- Trabaja desde requisitos, diseno y tareas aprobadas.
- Mantiene pruebas, trazabilidad y documentacion.

### Research
- Define experimentos, metricas y criterios de validez.
- Integra resultados con paper notes y reproducibility kit.
- Rechaza resultados sin evidencia completa.

## Responsabilidades Cruzadas

- **Seguridad**: Todos.
- **Documentacion**: Todos.
- **Trazabilidad**: Todos.
- **Calidad**: Todos.
- **Reproducibilidad**: Todos los repositorios con impacto cientifico.

---

*Este documento es parte de [00-kdd-governance](README.md)*
