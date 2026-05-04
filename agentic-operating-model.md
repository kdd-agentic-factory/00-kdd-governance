# Modelo Operativo Agentico

Definicion del modelo operativo del sistema agentico KDD.

## Principios Operativos

### 1. Autonomia con Control
Los agentes operan de forma autonoma dentro de limites definidos por diseno y politicas.

### 2. Transparencia Total
Todas las acciones son registradas y pueden ser auditadas.

### 3. Escalabilidad Progresiva
El sistema crece de forma controlada y medible.

### 4. Mejora Continua
Retroalimentacion y aprendizaje iterativo.

## Reglas Operativas Obligatorias

Estas reglas aplican a todos los agentes definidos o consumidos por los repositorios `01` a `17`.

| Regla | Significado operativo | Evidencia requerida |
|---|---|---|
| Ningun agente implementa sin especificacion | El agente debe localizar o solicitar requisitos aprobados antes de modificar codigo | Documento de requisitos y tareas trazadas |
| Ningun servicio se despliega sin diseno | El agente debe verificar que existe diseno aprobado o ADR aplicable | SDD, ADR o registro de excepcion aprobado |
| Ninguna recomendacion critica se ejecuta sin aprobacion | Acciones con impacto en datos, produccion, permisos, seguridad o usuarios requieren decision humana explicita | Registro de aprobacion y auditoria |
| Ningun experimento es valido sin metricas | El agente debe declarar metricas antes de ejecutar o evaluar experimentos | Experiment card, dataset card y metricas asociadas |
| Ningun resultado entra al paper sin trazabilidad | Todo resultado cientifico debe vincularse con datos, experimento, codigo, version y metricas | Paper section template y trazabilidad completa |

## Uso de AGENTS.md

`AGENTS.md` es el archivo maestro de contexto para agentes. Cada agente debe consultarlo como fuente de verdad sobre:

- Capacidades autorizadas.
- Permisos requeridos.
- Politicas aplicables.
- Convenciones de arquitectura.
- Estado operativo.
- Responsable humano.

Cuando un agente no encuentre instrucciones suficientes en `AGENTS.md`, debe detener la accion de riesgo y solicitar especificacion, diseno o aprobacion segun corresponda.

## Ciclo Operativo del Agente

1. Inicio, trigger o evento.
2. Evaluacion de contexto.
3. Consulta de politicas, permisos y `AGENTS.md`.
4. Verificacion de especificacion, diseno, tareas y metricas aplicables.
5. Planificacion de acciones.
6. Solicitud de aprobacion humana si aplica.
7. Ejecucion de acciones autorizadas.
8. Registro de evento y auditoria.
9. Retorno de resultados con evidencia.

## Puntos de Control

- **Autenticacion**: Verificacion de identidad del agente.
- **Autorizacion**: Validacion de permisos.
- **Especificacion**: Confirmacion de requisitos aprobados.
- **Diseno**: Confirmacion de SDD o ADR aplicable.
- **Validacion**: Verificacion de integridad de datos y pruebas.
- **Aprobacion Humana**: Requerida para acciones criticas.
- **Metricas**: Requeridas para experimentos y evaluacion de impacto.
- **Auditoria**: Registro de todas las acciones.

## Monitoreo y Alertas

El sistema monitorea:

- Ejecucion de agentes.
- Uso de recursos.
- Cumplimiento de politicas.
- Cobertura de trazabilidad.
- Eventos anomalos.

---

*Este documento es parte de [00-kdd-governance](README.md)*
