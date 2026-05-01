# ADR-0003: Uso de SDD como Mecanismo de Control Agentico

## Estado
Aceptado

## Contexto
Los agentes requieren directivas claras para operar de forma autónoma pero controlada.

## Decisión
Utilizar documentos SDD (Software Design Documents) como mecanismo primario de control para agentes autónomos.

## Justificación
- El diseño documentado proporciona límites claros para la ejecución
- Facilita auditoría y cumplimiento
- Permite retroalimentación humana explícita
- Escalable a múltiples agentes

## Consecuencias
- Requiere disciplina en documentación de diseño
- Los cambios de comportamiento requieren cambios de diseño
- Habilita validación automática de conformidad

## Estructura de SDD
- Requisitos funcionales
- Restricciones y políticas
- Interfaz de agente
- Puntos de control y aprobación

## Referencias
- [design.md](../design.md)
