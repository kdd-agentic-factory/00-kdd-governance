# Política de Validación de AutoSkills

## Propósito
Establecer proceso de validación para skills autogenerados por agentes.

## Definición de AutoSkill
Skills generados automáticamente por agentes inteligentes en base a patrones detectados.

## Ciclo de Vida de AutoSkill

### Generación
- Agente detecta patrón reutilizable
- Genera código de skill
- Solicita validación

### Validación Técnica
- Análisis estático de código
- Testing automático
- Cobertura de código > 80%
- Sin vulnerabilidades de seguridad
- Performance acceptable

### Validación Funcional
- Comportamiento correcto
- Interfaz consistente
- Documentación presente
- Casos de uso validados

### Validación de Governance
- Cumple políticas
- Sin violaciones de permisos
- Auditoría trail completo
- Aprobación por governance

### Activación
- Skill queda disponible para todos
- Métricas de uso comienzan
- Monitoreo de performance

## Criterios de Validación

### Obligatorios
- ✓ Tests pasados
- ✓ Sin vulnerabilidades críticas
- ✓ Interfaz clara
- ✓ Documentación en inglés y español

### Muy Recomendados
- ✓ Benchmarks de performance
- ✓ Ejemplos de uso
- ✓ Casos de error bien manejados
- ✓ Métricas de observabilidad

## Monitoreo Post-Activación

- Uso de skill
- Tasa de error
- Performance
- Feedback de usuarios
- Cambios recomendados

## Deprecación de AutoSkills

AutoSkills pueden deprecarse si:
- Uso < 1% de agentes
- Tasa de error > 5%
- Mejor alternativa disponible
- Cambios de arquitectura

---

*Parte de [00-kdd-governance](../README.md)*
