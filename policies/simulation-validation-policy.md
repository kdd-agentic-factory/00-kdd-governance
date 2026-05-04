# Simulation Validation Policy

## Proposito

Definir como se validan simulaciones y digital twins antes de usarlos como evidencia.

## Reglas

- Toda simulacion debe declarar parametros, version de modelo, datos de entrada y semilla si aplica.
- Deben compararse resultados contra baseline o datos reales cuando existan.
- La validez debe medirse con `simulation-validation-score.md`.
- Las simulaciones no autorizan acciones criticas por si solas.

---

*Parte de [00-kdd-governance](../README.md)*
