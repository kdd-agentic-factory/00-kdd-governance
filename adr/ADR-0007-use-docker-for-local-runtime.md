# ADR-0007: Uso de Docker para Runtime Local

## Estado
Aceptado

## Contexto
Se necesita entorno consistente para desarrollo y pruebas local de agentes.

## Decisión
Adoptar Docker como tecnología primaria para runtime local de agentes y servicios.

## Justificación
- Proporciona consistencia entre ambientes
- Facilita reproducibilidad
- Simplifica setup y onboarding
- Prepara transición a Kubernetes

## Consecuencias
- Requiere Docker en todas las máquinas de desarrollo
- Necesita Dockerfiles para cada servicio
- Mejora productividad de desarrollo

## Estándares Docker
- Base images aprobadas
- Networking interno mediante docker-compose
- Volúmenes para persistencia de datos
- Health checks obligatorios

## Transición a Kubernetes
Los contenedores Docker pueden transicionarse directamente a Kubernetes.

## Referencias
- [ADR-0008-use-kubernetes-for-scalable-runtime.md](ADR-0008-use-kubernetes-for-scalable-runtime.md)
