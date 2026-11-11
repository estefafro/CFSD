---
name: reunion
description: Convoca la reunión del sistema de agentes - cada agente informa y el Guía levanta el acta. Úsalo cuando la titular pida "reunión", "que informen todos" o "levanta el acta".
---

# Reunión de agentes

Argumento opcional: un foco para la reunión (por ejemplo `/reunion acreditación del magíster`). Si viene, pásalo a cada agente.

1. Fija el sello de la reunión con `date +%Y-%m-%d-%H%M` y úsalo en todos los archivos de esta reunión.
2. **Primera ronda, en paralelo** (una sola respuesta con cuatro llamadas a agentes): `actualizador`, `gestor-cargo`, `benchmark` y `trayectoria`. A cada uno pídele su informe para la reunión, escrito en su carpeta como `produccion/<agente>/<sello>-informe-reunion.md`, cubriendo lo nuevo desde la última acta.
3. **Segunda ronda**: `brechas-indicadores`, que necesita el benchmark recién escrito. Mismo nombre de archivo en su carpeta.
4. **Acta**: `guia` lee los cinco informes y escribe `produccion/actas/<sello>-acta.md` según su formato de acta.
5. Ejecuta `python3 scripts/verificar.py` y `python3 scripts/generar_tablero.py`. Si la verificación falla, pide al agente responsable que lo corrija con un archivo nuevo.
6. Muestra a la titular el acta: prioridades, riesgos altos, indicadores fijados y sus pendientes. Si un agente no pudo informar (por ejemplo, falta completar `perfil/`), dilo tal cual.

No confirmes ni subas cambios a git salvo que la titular lo pida.
