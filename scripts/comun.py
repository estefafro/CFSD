"""Lo que comparten verificar.py y generar_tablero.py."""
import re
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
PRODUCCION = RAIZ / "produccion"

# carpeta de produccion/ -> valor esperado de `agente:`
CARPETAS = {
    "actualizador": "actualizador",
    "gestor-cargo": "gestor-cargo",
    "benchmark": "benchmark",
    "brechas-indicadores": "brechas-indicadores",
    "guia": "guia",
    "trayectoria": "trayectoria",
    "actas": "guia",
}


def encabezado(texto: str):
    """Devuelve (campos, cuerpo). campos es None si no hay encabezado."""
    m = re.match(r"\A---\n(.*?)\n---\n?", texto, re.S)
    if not m:
        return None, texto
    campos = {}
    for linea in m.group(1).splitlines():
        if ":" in linea and not linea.lstrip().startswith("#"):
            clave, valor = linea.split(":", 1)
            campos[clave.strip()] = valor.split(" #")[0].strip().strip("\"'")
    return campos, texto[m.end():]


def archivos_de_produccion():
    return sorted(p for p in PRODUCCION.rglob("*") if p.is_file() and p.name != ".gitkeep")
