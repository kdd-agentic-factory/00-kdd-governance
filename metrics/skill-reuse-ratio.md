# Skill Reuse Ratio

## Propósito
Medir el grado de reutilización de skills en la organización.

## Definición
El Ratio de Reutilización de Skills mide qué porcentaje de agentes reutilizan skills existentes versus crear skills nuevos.

## Cálculo

$$
\text{Reuse Ratio} = \frac{\text{Skills Reutilizados}}{\text{Skills Totales Utilizados}} \times 100\%
$$

También se puede expresar como:

$$
\text{Reuse Depth} = \frac{\sum \text{(Número de Agentes que usan cada Skill)}}{\text{Total de Instancias de Skills}}
$$

## Métricas Componentes

### Skills Reutilizados
- Skills que se usan en 2+ agentes
- Skills que se usan en 3+ repositorios
- Skills base que son dependencia de otros skills

### Skills Únicos
- Skills creados para un solo agente
- Skills específicos de proyecto
- Skills legacy sin reutilización

## Objetivos Organizacionales

| Período | Objetivo |
|---------|----------|
| Trimestre 1 | > 20% |
| Trimestre 2 | > 35% |
| Semestre 1 | > 50% |
| Año 1 | > 70% |
| Año 2 | > 85% |

## Beneficios de Alta Reutilización

- Reducción de costo de desarrollo
- Mejora de consistencia
- Rápido despliegue de nuevos agentes
- Mantenimiento simplificado
- Documentación centralizada

## Cómo Mejorar

### 1. Identificar Patrones
- Analizar skills comúnmente requeridos
- Identificar similitudes en comportamiento
- Documentar requisitos comunes

### 2. Crear Skills Genéricos
- Diseñar skills reutilizables
- Parámetros configurables
- Interfaz estándar

### 3. Catálogo de Skills
- Mantener catálogo actualizado
- Documentación clara
- Ejemplos de uso

### 4. Incentivos
- Reconocer reutilización
- Objetivos de equipo
- Métricas en retrospectivas

## Reporte Mensual

| Métrica | Valor | Objetivo | Tendencia |
|---------|-------|----------|-----------|
| Reuse Ratio | [X]% | [Y]% | ↑/→/↓ |
| New Skills | [N] | [N] | ↑/→/↓ |
| Reused Skills | [N] | [N] | ↑/→/↓ |
| Avg Reuse Depth | [N] | [N] | ↑/→/↓ |

---

*Métrica de [00-kdd-governance](../README.md)*
