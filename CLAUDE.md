# Sistema de agentes de salud digital

Este repositorio es el sistema de seis agentes de la titular de un cargo académico en salud digital.
Lee `README.md` para el mapa completo.

@sistema/REGLAS.md

- Responde y escribe en español.
- Los agentes están en `.claude/agents/`; la reunión, en `.claude/skills/reunion/`.
- Después de que cualquier agente produzca algo: `python3 scripts/verificar.py` y `python3 scripts/generar_tablero.py`.
- `tablero/index.html` es generado; se edita `tablero/plantilla.html`.
