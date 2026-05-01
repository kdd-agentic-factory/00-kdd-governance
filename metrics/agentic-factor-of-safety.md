# Agentic Factor of Safety

## Propósito
Medir el nivel de seguridad y control en la operación de agentes autónomos.

## Definición
El Factor de Seguridad Agentico es una puntuación que indica cuán seguro es permitir que un agente opere sin supervisión humana.

## Escala

$$
\text{Factor of Safety} = \text{min}(\text{Control Score}, \text{Reliability Score}, \text{Capability Score})
$$

### Factor of Safety por Nivel

- **> 0.9**: Autónomo sin restricciones
- **0.7 - 0.9**: Autónomo con monitoreo
- **0.5 - 0.7**: Supervisado (requiere aprobación humana)
- **0.3 - 0.5**: Asistido (humano primario)
- **< 0.3**: Solo observador

## Componentes

### Control Score (0-1)

Mide qué tan bien puede controlarse el comportamiento del agente.

- **Límites Claros**: ✓/✗ (0.25 puntos)
- **Políticas Documentadas**: ✓/✗ (0.25 puntos)
- **Puntos de Aprobación**: ✓/✗ (0.25 puntos)
- **Auditoría Implementada**: ✓/✗ (0.25 puntos)

### Reliability Score (0-1)

Mide la confiabilidad del agente en entregar resultados correctos.

- **Uptime**: [%] (0.3 puntos: 99%+ = 0.3, 95%+ = 0.2, < 95% = 0)
- **Error Rate**: [%] (0.3 puntos: < 1% = 0.3, < 5% = 0.2, > 5% = 0)
- **Test Coverage**: [%] (0.2 puntos: > 80% = 0.2, > 60% = 0.1, < 60% = 0)
- **Production Incidents**: [Número] (0.2 puntos: 0 = 0.2, 1-2 = 0.1, > 2 = 0)

### Capability Score (0-1)

Mide si el agente tiene las capacidades necesarias para su misión.

- **Skill Completeness**: [%] (0.5 puntos)
- **Knowledge Base Accuracy**: [%] (0.5 puntos)

## Evaluación Periódica

| Período | Evaluación |
|---------|-----------|
| Inicial | Antes de despliegue |
| Semanal | Durante primeras 4 semanas |
| Mensual | Primeros 3 meses |
| Trimestral | Después de 3 meses |

## Acciones Basadas en Factor of Safety

- **> 0.9**: Aumentar autonomía, reducir monitoreo
- **0.7 - 0.9**: Mantener estado actual, monitoreo normalizado
- **0.5 - 0.7**: Aumentar supervisión, revisar diseño
- **0.3 - 0.5**: Limitar operaciones, investigar problemas
- **< 0.3**: Suspender operaciones, rediseñar

---

*Métrica de [00-kdd-governance](../README.md)*
