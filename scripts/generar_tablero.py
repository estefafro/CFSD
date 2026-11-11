#!/usr/bin/env python3
"""Genera tablero/index.html a partir de sistema/, perfil/ y produccion/.

Uso: python3 scripts/generar_tablero.py
El tablero es una vista: se regenera completo cada vez y se abre sin servidor.
"""
import json
import re
from datetime import datetime

from comun import PRODUCCION, RAIZ, encabezado

PLANTILLA = RAIZ / "tablero" / "plantilla.html"
SALIDA = RAIZ / "tablero" / "index.html"


def documentos(carpeta):
    docs = []
    for ruta in sorted((PRODUCCION / carpeta).glob("*.md"), reverse=True):
        texto = ruta.read_text(encoding="utf-8")
        campos, cuerpo = encabezado(texto)
        campos = campos or {}
        docs.append({
            "ruta": ruta.relative_to(RAIZ).as_posix(),
            "titulo": campos.get("titulo") or ruta.stem,
            "fecha": campos.get("fecha") or ruta.name[:10],
            "reemplaza": campos.get("reemplaza", ""),
            "texto": cuerpo.strip(),
        })
    return docs


def capacidades():
    texto = (RAIZ / "perfil" / "capacidades.md").read_text(encoding="utf-8")
    caps = []
    for bloque in re.split(r"^## ", texto, flags=re.M)[1:]:
        nombre, _, detalle = bloque.partition("\n")
        caps.append({"nombre": nombre.strip(), "detalle": " ".join(detalle.split())})
    return caps


def main():
    agentes = json.loads((RAIZ / "sistema" / "agentes.json").read_text(encoding="utf-8"))
    for a in agentes:
        a["documentos"] = [d for c in a["carpetas"] if c != "actas" for d in documentos(c)]
    datos = {
        "generado": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "agentes": agentes,
        "actas": documentos("actas"),
        "capacidades": capacidades(),
    }
    incrustado = json.dumps(datos, ensure_ascii=False).replace("</", "<\\/")
    html = PLANTILLA.read_text(encoding="utf-8").replace("/*__DATOS__*/null", incrustado)
    SALIDA.write_text(html, encoding="utf-8")
    total = sum(len(a["documentos"]) for a in agentes)
    print(f"tablero/index.html generado: {total} documento(s), {len(datos['actas'])} acta(s).")


if __name__ == "__main__":
    main()
