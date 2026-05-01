# Política de Cambios en Kubernetes

## Propósito
Establecer proceso controlado para cambios en infraestructura Kubernetes de producción.

## Alcance
Se aplica a todos los cambios en clusters Kubernetes que afecten a producción.

## Cambios Requieren Aprobación

### Críticos (Aprobación Inmediata)
- Cambios de RBAC o security policies
- Cambios de persistencia de datos
- Cambios de network policies
- Cambios de resource limits
- Updates de kernel o sistema operativo

### Mayores (Aprobación en 4h)
- Deployment de nuevas versiones
- Cambios de replica counts
- Cambios de storage
- Updates de dependencias críticas

### Menores (Aprobación en 24h)
- Cambios de configuración menor
- Updates de patches
- Cambios de labels/annotations
- Scaling manual

## Proceso de Cambio

### 1. Planificación
- Descripción clara del cambio
- Justificación del cambio
- Plan de rollback
- Ventana de tiempo

### 2. Aprobación
- Revisión de operaciones
- Revisión de seguridad
- Revisión de arquitectura
- Aprobación final

### 3. Pruebas
- Testing en staging
- Validación de rollback
- Smoke tests preparados
- Alertas configuradas

### 4. Ejecución
- Cambio en ventana aprobada
- Monitoreo en tiempo real
- Rollback inmediato si es necesario
- Comunicación de status

### 5. Validación
- Verificación de change
- Verificación de health
- Verificación de performance
- Documentación

### 6. Auditoría
- Registro de cambio
- Registro de aprobación
- Registro de ejecución
- Lecciones aprendidas

## Estándares de Cambio

- GitOps para infraestructura como código
- Pull requests para todos los cambios
- Automated testing requerido
- Changelist clara y trazable
- Observabilidad instrumentada

## Excepciones

**Emergencias de seguridad**: Cambios pueden ejecutarse inmediatamente con aprobación de 1 persona + auditoría posterior en 4h.

---

*Parte de [00-kdd-governance](../README.md)*
