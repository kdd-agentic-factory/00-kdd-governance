# ADR-0008: Uso de Kubernetes para Runtime Escalable

## Estado
Aceptado

## Contexto
La producción requiere escalabilidad, confiabilidad y orchestración sofisticada de agentes y servicios.

## Decisión
Adoptar Kubernetes como plataforma de orchestración para runtime escalable de agentes en producción.

## Justificación
- Proporciona escalabilidad automática
- Habilita alta disponibilidad
- Facilita gestión de recursos
- Standard de industria

## Consecuencias
- Requiere expertise en Kubernetes
- Necesita CI/CD pipeline sofisticado
- Aumenta complejidad operativa
- Mejora significativa en confiabilidad

## Arquitectura Kubernetes
- Namespaces para aislamiento
- RBAC para control de acceso
- Network Policies para seguridad
- Resource Quotas para gestión
- Persistent Volumes para estado
- StatefulSets para agentes con estado

## Políticas de Cambio
Los cambios en Kubernetes requieren aprobación según [kubernetes-change-policy.md](../policies/kubernetes-change-policy.md)

## Referencias
- [ADR-0007-use-docker-for-local-runtime.md](ADR-0007-use-docker-for-local-runtime.md)
- [kubernetes-change-policy.md](../policies/kubernetes-change-policy.md)
