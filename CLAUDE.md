# Sistema de agentes de salud digital

Este repositorio es el sistema de seis agentes de la titular de un cargo académico en salud digital.
Lee `README.md` para el mapa completo.

@sistema/REGLAS.md

- Responde y escribe en español.
- Los agentes están en `.claude/agents/`; la reunión, en `.claude/skills/reunion/`.
- Después de que cualquier agente produzca algo: `python3 scripts/verificar.py` y `python3 scripts/generar_tablero.py`.
- `tablero/index.html` es generado; se edita `tablero/plantilla.html`.
- El Guía está en el flujo: cada vez que se cree o cambie un documento de `entregables/`, o la titular entregue un archivo, se llama al Guía para que lo registre. Hay que decirle quién sugirió cada cambio y por qué; lo que no se sepa, se le dice que no consta. Sus alertas se le transmiten a la titular completas, sin resumir.
- `python3 scripts/comparar_versiones.py <a> [<b>]` da la huella de un documento o las diferencias entre dos.
