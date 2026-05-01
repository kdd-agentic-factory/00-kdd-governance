# Política de Aprobación Humana

## Propósito
Establecer procesos de aprobación humana para acciones críticas en el sistema agentico.

## Alcance
Se aplica a todas las acciones que pueden impactar significativamente el sistema, datos o usuarios.

## Acciones Requieren Aprobación

### Críticas (Aprobación Inmediata)
- Cambios a políticas de seguridad
- Alteraciones de base de datos de producción
- Cambios de permisos de agentes
- Despliegues a producción
- Eliminación de datos

### Mayores (Aprobación en 24h)
- Nuevas funcionalidades de agentes
- Cambios de arquitectura
- Cambios a SDD
- Cambios de dependencias críticas

### Menores (Aprobación en 72h)
- Actualizaciones de documentación
- Correcciones de bugs menores
- Refactorización sin cambio de comportamiento
- Actualizaciones de dependencias

## Proceso de Aprobación

1. **Solicitud**: Agente o desarrollador solicita aprobación
2. **Revisión**: Equipo designado revisa en 24h
3. **Validación**: Verificación de políticas y riesgos
4. **Aprobación**: Decisión explícita
5. **Ejecución**: Implementación de cambio aprobado
6. **Auditoría**: Registro de aprobación y ejecución

## Excepciones
- Emergencias de seguridad: Aprobación posterior dentro de 4h
- Incidentes de producción: Aprobación dentro de 1h

---

*Parte de [00-kdd-governance](../README.md)*
