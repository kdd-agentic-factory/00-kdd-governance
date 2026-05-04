# Repository Standards

Normas minimas para todos los repositorios del ecosistema KDD.

## Estructura minima

Todo repositorio debe incluir:

- `README.md`
- `AGENTS.md`
- `design.md` o referencia a un SDD aprobado
- `GOVERNANCE.md` cuando tenga reglas locales
- `CHANGELOG.md` cuando produzca releases
- Evidencia de requisitos, tareas, pruebas y as-built para cambios relevantes

## Reglas de trabajo

- Ninguna feature se implementa sin requisito aprobado.
- Ningun servicio se despliega sin diseno aprobado o ADR aplicable.
- Ningun cambio critico se ejecuta sin aprobacion humana.
- Todo experimento debe declarar metricas antes de ejecutarse.
- Todo resultado cientifico debe enlazar con evidencia reproducible.

## Calidad minima

- Pruebas automatizadas para comportamiento critico.
- Linting o validacion equivalente.
- Escaneo de seguridad cuando haya dependencias, contenedores o despliegue.
- Documentacion actualizada en el mismo cambio.

---

*Parte de [00-kdd-governance](README.md)*
