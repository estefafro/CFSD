#!/usr/bin/env python3
"""Comprueba las reglas de sistema/REGLAS.md sobre produccion/.

Uso: python3 scripts/verificar.py
Sale con 1 si hay alguna falta.
"""
import re
import subprocess
import sys

from comun import CARPETAS, PRODUCCION, RAIZ, archivos_de_produccion, encabezado

NOMBRE = re.compile(r"^\d{4}-\d{2}-\d{2}-\d{4}-[a-z0-9][a-z0-9-]*\.md$")
FECHA = re.compile(r"\b\d{4}-\d{2}-\d{2}\b")
ETIQUETA = re.compile(r"\[(HECHO|HIP[ÓO]TESIS|PROPUESTA)\]")
INDICADOR = re.compile(r"^#{1,6}\s*Indicador\b", re.I)
TITULO = re.compile(r"^#{1,6}\s")
RESPALDO = re.compile(r"Respaldo:.*?(produccion/benchmark/[^\s)`\"']+\.md)")


def revisar_archivo(ruta, faltas):
    rel = ruta.relative_to(RAIZ).as_posix()

    def falta(msg, n=None):
        faltas.append(f"{rel}{':' + str(n) if n else ''}: {msg}")

    carpeta = ruta.relative_to(PRODUCCION).parts[0]
    if carpeta not in CARPETAS or len(ruta.relative_to(PRODUCCION).parts) != 2:
        falta("está fuera de las carpetas de agente")
        return
    if not NOMBRE.match(ruta.name):
        falta("el nombre debe ser AAAA-MM-DD-HHMM-<tema>.md (minúsculas, sin espacios)")

    campos, cuerpo = encabezado(ruta.read_text(encoding="utf-8"))
    if campos is None:
        falta("falta el encabezado (--- agente / fecha / titulo ---)")
        campos = {}
    else:
        if campos.get("agente") != CARPETAS[carpeta]:
            falta(f"`agente:` debe ser {CARPETAS[carpeta]}")
        if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", campos.get("fecha", "")):
            falta("`fecha:` debe ser AAAA-MM-DD")
        if not campos.get("titulo"):
            falta("falta `titulo:`")
        anterior = campos.get("reemplaza")
        if anterior and not (RAIZ / anterior).is_file():
            falta(f"`reemplaza:` apunta a un archivo que no existe ({anterior})")

    lineas = cuerpo.splitlines()
    desfase = len(ruta.read_text(encoding="utf-8").splitlines()) - len(lineas)
    hay_etiqueta = False
    en_codigo = False
    bloque = None  # (línea del título, texto acumulado) del indicador abierto

    def cerrar_bloque():
        if bloque is None:
            return
        n, texto = bloque
        rutas = RESPALDO.findall(texto)
        if not rutas:
            falta("indicador sin `Respaldo: produccion/benchmark/<archivo>.md`", n)
        for r in rutas:
            if not (RAIZ / r).is_file():
                falta(f"el respaldo del indicador no existe ({r})", n)

    for i, linea in enumerate(lineas, start=desfase + 1):
        if linea.lstrip().startswith("```"):
            en_codigo = not en_codigo
            continue
        if en_codigo:
            continue
        if TITULO.match(linea):
            cerrar_bloque()
            bloque = (i, "") if INDICADOR.match(linea) else None
            continue
        if bloque is not None:
            bloque = (bloque[0], bloque[1] + "\n" + linea)
        if ETIQUETA.search(linea):
            hay_etiqueta = True
        if "[HECHO]" in linea:
            if "Fuente:" not in linea:
                falta("[HECHO] sin `Fuente:` en la misma línea", i)
            elif not FECHA.search(linea.split("Fuente:", 1)[1]):
                falta("[HECHO] sin fecha AAAA-MM-DD junto a la fuente", i)
    cerrar_bloque()

    if not hay_etiqueta:
        falta("ninguna afirmación etiquetada como [HECHO], [HIPÓTESIS] o [PROPUESTA]")


def revisar_historial(faltas):
    """Nada en produccion/ puede haber sido modificado, renombrado ni borrado."""

    def git(*args):
        r = subprocess.run(["git", "-C", str(RAIZ), *args], capture_output=True, text=True)
        return r.stdout.splitlines() if r.returncode == 0 else []

    vistos = set()
    pendientes = git("status", "--porcelain", "--", "produccion")
    confirmados = git("log", "--diff-filter=MDR", "--name-status", "--format=", "--", "produccion")
    for linea in pendientes:
        estado, ruta = linea[:2], linea[3:].strip('"')
        if set(estado) & set("MDR"):
            vistos.add((ruta, "sin confirmar"))
    for linea in confirmados:
        partes = linea.split("\t")
        if len(partes) >= 2:
            vistos.add((partes[1], "en el historial"))
    for ruta, donde in sorted(vistos):
        if not ruta.endswith(".gitkeep"):
            faltas.append(f"{ruta}: fue modificado, renombrado o borrado ({donde}); nada se sobrescribe")


def main() -> int:
    faltas = []
    archivos = archivos_de_produccion()
    for ruta in archivos:
        if ruta.suffix != ".md":
            faltas.append(f"{ruta.relative_to(RAIZ).as_posix()}: la producción va en archivos .md")
            continue
        revisar_archivo(ruta, faltas)
    revisar_historial(faltas)

    if faltas:
        print(f"{len(faltas)} falta(s) contra sistema/REGLAS.md:\n")
        print("\n".join(f"  - {f}" for f in faltas))
        return 1
    print(f"Sin faltas. {len(archivos)} archivo(s) de producción revisados.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
