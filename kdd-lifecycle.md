# Ciclo de Vida KDD

Metodologia del Knowledge-Driven Development.

En este proyecto, KDD no se limita a mineria de datos tradicional. KDD es el modelo administrativo del ecosistema agentico: organiza datos, documentos, repositorios, agentes, experimentos, decisiones, despliegues y evidencia cientifica.

## Ciclo KDD Adaptado

| Fase | Significado en este proyecto | Ejemplos de artefactos |
|---|---|---|
| Selection | Seleccion de datos, documentos, repositorios, sesiones, circuitos, modelos y artefactos | Dataset card, requisitos, fuentes, trazas |
| Preprocessing | Limpieza, validacion, normalizacion, anonimizacion, control de calidad y preparacion | Validaciones, reportes QA, contratos de entrada |
| Transformation | Conversion a esquemas, features, embeddings, contratos de datos y formatos reutilizables | Features, embeddings, schemas, data contracts |
| Data Mining | Deteccion de patrones, clustering, anomalias, correlaciones, prediccion y simulacion | Experimentos, modelos, simulaciones, metricas |
| Interpretation | Explicacion tecnica, recomendaciones, analisis de riesgo y evidencia | Reportes, recomendaciones, risk notes, approvals |
| Documentation | README, ADR, requirements, design, tasks, as-built, paper notes y reportes | Plantillas obligatorias y documentacion generada |
| Deployment | Docker, Kubernetes, CI/CD, observabilidad, seguridad y release controlado | Releases, manifests, dashboards, auditoria |

## Ejemplo: Recomendacion de Setup en `15-race-command-center`

| Fase | Aplicacion practica |
|---|---|
| Selection | Se seleccionan vueltas, curvas, sesiones y senales relevantes |
| Preprocessing | Se limpian outliers, timestamps, gaps y senales erroneas |
| Transformation | Se calculan features como `spin_ratio`, `lean_angle`, `brake_phase` y `drive_efficiency` |
| Data Mining | Se detecta patron de degradacion o perdida de traccion |
| Interpretation | Se propone cambiar `Mapping 2` o ajustar rebote trasero |
| Documentation | Se genera informe para el crew chief y paper-note |
| Deployment | Se registra la accion y, si procede, se despliega como regla o modelo actualizado |

## Fases del Ciclo KDD

### 1. Discovery
- Identificacion de requisitos
- Recopilacion de conocimiento
- Documentacion de necesidades

### 2. Design
- Diseno de soluciones
- Arquitectura tecnica
- Definicion de capacidades

### 3. Development
- Implementacion
- Creacion de skills
- Desarrollo de agentes

### 4. Validation
- Testing y validacion
- Aprobacion humana
- Aseguramiento de calidad

### 5. Deployment
- Despliegue a produccion
- Monitoreo inicial
- Documentacion as-built

### 6. Operations
- Operacion y mantenimiento
- Monitoreo continuo
- Mejora iterativa

### 7. Retirement
- Deprecacion
- Migracion de datos
- Archivado

## Artefactos por Fase

| Fase | Artefactos Principales |
|------|------------------------|
| Discovery | Requirements, Feasibility Study |
| Design | Design Document, ADR |
| Development | Code, Skills, Agents |
| Validation | Test Reports, Approvals |
| Deployment | Release Notes, As-Built |
| Operations | Metrics, Logs, Alerts |
| Retirement | Deprecation Notice, Archive |

## Flujo Specification-Driven Development

El ciclo KDD aplica Specification-Driven Development como secuencia obligatoria de control. Ningun repositorio del ecosistema puede saltar directamente a implementacion sin evidencia documental previa.

| Paso | Artefacto obligatorio | Plantilla | Regla de avance |
|---|---|---|---|
| 1 | Requisitos funcionales y no funcionales | `templates/requirements.template.md` | Deben estar revisados antes de evaluar viabilidad |
| 2 | Viabilidad tecnica, operativa y de datos | `templates/feasibility.template.md` | Debe identificar riesgos y decision Go/No-Go |
| 3 | Diseno tecnico | `templates/design.template.md` | Debe cubrir arquitectura, pruebas, seguridad, despliegue y observabilidad |
| 4 | Tareas trazables | `templates/tasks.template.md` | Cada tarea debe enlazar con requisitos y componentes de diseno |
| 5 | Implementacion con TDD | Repositorio responsable | Las pruebas deben evidenciar el cumplimiento de requisitos |
| 6 | Verificacion as-built | `templates/as-built.template.md` | Debe comparar diseno vs implementacion real |
| 7 | Medicion y evidencia | `metrics/` y plantillas cientificas | Debe cerrar trazabilidad hacia resultados y paper |

## Controles de Bloqueo

- Sin requisitos aprobados, no se permite implementacion.
- Sin diseno aprobado, no se permite despliegue.
- Sin aprobacion humana, no se ejecutan recomendaciones criticas.
- Sin metricas definidas, no se valida un experimento.
- Sin trazabilidad completa, ningun resultado puede incorporarse al paper.

---

*Este documento es parte de [00-kdd-governance](README.md)*
