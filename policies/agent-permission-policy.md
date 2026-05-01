# Política de Permisos de Agentes

## Propósito
Definir y controlar los permisos que pueden ejercer los agentes autónomos del sistema.

## Principios
- **Principio de Menor Privilegio**: Agentes reciben solo permisos necesarios
- **Segregación de Deberes**: Agentes críticos requieren coordinar acciones
- **Auditoría Total**: Todos los permisos ejercidos se registran
- **Revisión Periódica**: Permisos se revisan trimestralmente

## Categorías de Permisos

### Lectura
- Acceso a repositorios
- Acceso a datos
- Acceso a logs
- Sin restricciones de tiempo

### Escritura
- Modificación de código
- Creación de issues/PRs
- Requiere aprobación para producción
- Limitado a ramas específicas

### Administración
- Cambios de políticas
- Creación de agentes
- Deshabilitación de agentes
- Requiere aprobación de governance

### Ejecución
- Despliegue de código
- Cambios de configuración
- Cambios de base de datos
- Requiere aprobación para producción

## Asignación de Permisos

1. **Solicitud**: Agente o responsable solicita permiso
2. **Justificación**: Explicación del caso de uso
3. **Validación**: Verificación de riesgos
4. **Aprobación**: Aprobación de governance
5. **Asignación**: Implementación del permiso
6. **Auditoría**: Registro de asignación

## Revocación de Permisos

Los permisos pueden revocarse si:
- No se usan durante 90 días
- Se detecta abuso
- Cambio de responsabilidades
- Fin de ciclo de vida de agente

---

*Parte de [00-kdd-governance](../README.md)*
