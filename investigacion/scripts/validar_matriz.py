#!/usr/bin/env python3
"""Valida una matriz de extracción contra las reglas del proyecto.

Uso:
    python3 scripts/validar_matriz.py investigaciones/<tema>/02_matriz.csv \
        --ejes origen,historia_disciplina,aplicacion,estudios_recientes,limitaciones,oportunidades

Revisa:
  - que las columnas sean las de config/columnas_matriz.csv (o las de --columnas)
  - que las columnas obligatorias no estén vacías y los ids no se repitan
  - máximo de papers por tema (15 por defecto)
  - que las fuentes del eje `estudios_recientes` sean de los últimos 5 años
  - cobertura: cuántas fuentes alimentan cada eje (avisa si hay menos de 2)
  - que ningún DOI quede sin verificar

Los ERRORES hacen fallar la validación; los AVISOS son vacíos que conviene
resolver (por ejemplo, pidiendo otra búsqueda al agente buscador).
"""
import argparse
import csv
import datetime
import pathlib
import sys

RAIZ = pathlib.Path(__file__).resolve().parent.parent
EJE_RECIENTE = "estudios_recientes"


def main():
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument("matriz")
    parser.add_argument("--columnas", default=str(RAIZ / "config" / "columnas_matriz.csv"))
    parser.add_argument("--ejes", default="", help="ejes del brief, separados por coma")
    parser.add_argument("--max-papers", type=int, default=15)
    parser.add_argument("--anios-recientes", type=int, default=5)
    parser.add_argument("--min-por-eje", type=int, default=2)
    args = parser.parse_args()

    with open(args.columnas, newline="", encoding="utf-8") as archivo:
        definicion = list(csv.DictReader(archivo))
    esperadas = [d["columna"] for d in definicion]
    obligatorias = [d["columna"] for d in definicion if d["obligatoria"].strip() == "si"]

    with open(args.matriz, newline="", encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)
        columnas = lector.fieldnames or []
        filas = list(lector)

    errores, avisos = [], []

    faltan = [c for c in esperadas if c not in columnas]
    sobran = [c for c in columnas if c not in esperadas]
    if faltan:
        errores.append(f"faltan columnas: {', '.join(faltan)}")
    if sobran:
        errores.append(
            f"columnas no definidas en la configuración: {', '.join(sobran)} "
            "(agrégalas a config/columnas_matriz.csv si son intencionales)"
        )

    ejes_brief = [e.strip() for e in args.ejes.split(",") if e.strip()]
    cobertura = {eje: 0 for eje in ejes_brief}
    limite_anio = datetime.date.today().year - args.anios_recientes
    vistos = set()
    papers = 0

    for numero, fila in enumerate(filas, start=2):
        ident = (fila.get("id") or "").strip() or f"fila {numero}"
        if None in fila:
            errores.append(f"{ident}: tiene más celdas que columnas (CSV mal formado)")
        for columna in obligatorias:
            if columna in columnas and not (fila.get(columna) or "").strip():
                errores.append(f"{ident}: falta `{columna}`")
        if ident in vistos:
            errores.append(f"{ident}: id repetido")
        vistos.add(ident)

        if (fila.get("tipo_fuente") or "").strip().lower() == "paper":
            papers += 1

        ejes = [e.strip() for e in (fila.get("eje_contexto") or "").split(";") if e.strip()]
        for eje in ejes:
            if ejes_brief and eje not in cobertura:
                errores.append(f"{ident}: eje `{eje}` no está en el brief")
            cobertura[eje] = cobertura.get(eje, 0) + 1

        anio = (fila.get("anio") or "").strip()
        if anio and not (anio.isdigit() and len(anio) == 4):
            errores.append(f"{ident}: año inválido `{anio}`")
        elif anio and EJE_RECIENTE in ejes and int(anio) < limite_anio:
            errores.append(
                f"{ident}: está en `{EJE_RECIENTE}` pero es de {anio} "
                f"(debe ser de {limite_anio} en adelante)"
            )

        verificado = (fila.get("doi_verificado") or "").strip()
        if verificado == "no":
            errores.append(f"{ident}: el DOI no pasó la verificación")
        elif verificado not in ("si", "sin_doi"):
            avisos.append(f"{ident}: DOI aún sin verificar")

        if (fila.get("acceso") or "").strip() == "pendiente":
            avisos.append(f"{ident}: texto completo pendiente de conseguir")
        cita = (fila.get("cita_textual_clave") or "").strip()
        if cita and not (fila.get("ubicacion_cita") or "").strip():
            avisos.append(f"{ident}: cita textual sin ubicación (página o sección)")

    if papers > args.max_papers:
        errores.append(f"hay {papers} papers; el máximo por tema es {args.max_papers}")

    print(f"Fuentes: {len(filas)}  (papers: {papers}/{args.max_papers})")
    print("Cobertura por eje:")
    for eje, cantidad in cobertura.items():
        marca = "" if cantidad >= args.min_por_eje else "  <-- vacío"
        print(f"  {eje}: {cantidad}{marca}")
        if cantidad < args.min_por_eje:
            avisos.append(f"eje `{eje}` con {cantidad} fuente(s): pedir búsqueda dirigida")

    for titulo, lista in (("ERRORES", errores), ("AVISOS", avisos)):
        if lista:
            print(f"\n{titulo} ({len(lista)}):")
            for item in lista:
                print(f"  - {item}")
    if not errores and not avisos:
        print("\nMatriz válida, sin observaciones.")
    return 1 if errores else 0


if __name__ == "__main__":
    sys.exit(main())
