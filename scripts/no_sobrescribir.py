#!/usr/bin/env python3
"""Hook PreToolUse: impide escribir sobre un archivo que ya existe en produccion/.

Regla 3 de sistema/REGLAS.md: nada se sobrescribe. Para corregir se crea un
archivo nuevo con `reemplaza:`. Un borrador que todavía no está confirmado en
git sí puede corregirse.
"""
import json
import os
import subprocess
import sys


def main() -> int:
    try:
        evento = json.load(sys.stdin)
    except ValueError:
        return 0
    entrada = evento.get("tool_input") or {}
    ruta = entrada.get("file_path") or entrada.get("notebook_path")
    if not ruta:
        return 0

    raiz = os.environ.get("CLAUDE_PROJECT_DIR") or evento.get("cwd") or os.getcwd()
    produccion = os.path.realpath(os.path.join(raiz, "produccion"))
    destino = os.path.realpath(os.path.join(raiz, ruta))
    if os.path.commonpath([produccion, destino]) != produccion:
        return 0
    if os.path.basename(destino) == ".gitkeep" or not os.path.exists(destino):
        return 0
    en_git = subprocess.run(
        ["git", "-C", raiz, "ls-files", "--error-unmatch", "--", destino],
        capture_output=True,
    )
    if en_git.returncode != 0:
        return 0  # borrador sin confirmar

    print(
        f"Bloqueado: {os.path.relpath(destino, raiz)} ya está confirmado y nada en produccion/ "
        "se sobrescribe. Crea un archivo nuevo (AAAA-MM-DD-HHMM-<tema>.md) con "
        "`reemplaza:` apuntando a este.",
        file=sys.stderr,
    )
    return 2


if __name__ == "__main__":
    sys.exit(main())
