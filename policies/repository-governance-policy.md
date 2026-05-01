# Política de Governance de Repositorios

## Propósito
Establecer estándares para la creación y gestión de repositorios en la organización.

## Estructura de Repositorios

### Repositorio de Governance (00-kdd-governance)
- Políticas y estándares
- Decisiones arquitectónicas
- Plantillas
- Métricas

### Repositorios de Arquitectura (01-kdd-architecture-*)
- Diseños técnicos
- Estándares de implementación
- Arquitectura de soluciones

### Repositorios de Capabilidades (02-kdd-skills, 03-kdd-agents)
- Skills reutilizables
- Agentes del sistema
- Integraciones

### Repositorios de Datos (04-kdd-data)
- Datasets
- Esquemas
- Validaciones

### Repositorios de Proyectos
- Código específico de proyectos
- Documentación de proyectos
- Artefactos del ciclo KDD

## Requerimientos para Todo Repositorio

### Documentación
- README.md con descripción clara
- GOVERNANCE.md con políticas específicas
- CONTRIBUTING.md con guías de contribución
- Changelog mantenido

### Control de Versiones
- Branch protection rules
- Require pull request reviews
- Require status checks to pass
- Restricción a branches específicas para producción

### CI/CD
- Automated testing
- Automated linting
- Automated security scanning
- Deployment pipeline

### Auditoría
- Todos los cambios requieren commit comments
- PRs requieren descripción detallada
- Histórico de cambios accesible
- Logs de auditoría centralizados

## Ciclo de Vida de Repositorio

1. **Creación**: Aprobación de governance requerida
2. **Operación**: Cumplimiento de políticas
3. **Mantenimiento**: Actualizaciones según cronograma
4. **Deprecación**: Comunicación anticipada
5. **Archivado**: Preservación de histórico

---

*Parte de [00-kdd-governance](../README.md)*
