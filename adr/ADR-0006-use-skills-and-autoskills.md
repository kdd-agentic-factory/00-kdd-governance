# ADR-0006: Uso de Skills y AutoSkills

## Estado
Aceptado

## Contexto
Se necesita mecanismo para reutilizar comportamientos y capacidades entre agentes.

## Decisión
Implementar sistema de Skills (capacidades manuales) y AutoSkills (capacidades autogeneradas) como unidades reutilizables de funcionalidad.

## Justificación
- Promueve reutilización de código
- Facilita especialización de agentes
- Mejora mantenibilidad
- Habilita evolución gradual de capacidades

## Consecuencias
- Requiere estándares claros para skills
- Necesita validación de AutoSkills generados
- Mejora productividad de desarrollo

## Ciclo de Vida
- **Skill Manual**: Definición explícita, validación humana
- **AutoSkill**: Generación automática, validación incrementada

## Políticas de Validación
- Skills: Aprobación manual requerida
- AutoSkills: Validación automática + aprobación por mérito

## Referencias
- [autoskill-validation-policy.md](../policies/autoskill-validation-policy.md)
