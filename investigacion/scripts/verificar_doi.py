#!/usr/bin/env python3
"""Verifica que los DOI de una matriz existan y correspondan al título anotado.

Uso:
    python3 scripts/verificar_doi.py investigaciones/<tema>/02_matriz.csv
    python3 scripts/verificar_doi.py investigaciones/<tema>/02_matriz.csv --actualizar
    python3 scripts/verificar_doi.py --doi 10.1038/nature14539

Para cada DOI consulta doi.org: si no resuelve, el DOI no existe. Si además se
pueden obtener los metadatos, compara el título registrado con el de la matriz.
Con --actualizar escribe el resultado en la columna `doi_verificado`
(si | no | sin_doi). Solo usa la biblioteca estándar.
"""
import argparse
import csv
import difflib
import json
import re
import sys
import urllib.error
import urllib.parse
import urllib.request

UMBRAL_TITULO = 0.6
AGENTE = "verificador-doi/1.0"


class _SinRedireccion(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, *args, **kwargs):
        return None


def limpiar_doi(valor):
    """Devuelve el DOI sin prefijos, o None si el valor no es un DOI."""
    valor = (valor or "").strip()
    valor = re.sub(r"^(https?://(dx\.)?doi\.org/|doi:\s*)", "", valor, flags=re.I)
    return valor if re.match(r"^10\.\d{4,9}/\S+$", valor) else None


def existe(doi):
    """True/False si doi.org resuelve o no el DOI; None si no se pudo consultar."""
    url = "https://doi.org/" + urllib.parse.quote(doi, safe="/")
    peticion = urllib.request.Request(url, method="HEAD", headers={"User-Agent": AGENTE})
    try:
        urllib.request.build_opener(_SinRedireccion).open(peticion, timeout=20)
        return True
    except urllib.error.HTTPError as error:
        if error.code in (301, 302, 303, 307, 308):
            return True
        if error.code == 404:
            return False
        return None
    except (urllib.error.URLError, TimeoutError):
        return None


def metadatos(doi):
    """Título y año registrados para el DOI, o None si no hay acceso a ellos."""
    url = "https://doi.org/" + urllib.parse.quote(doi, safe="/")
    peticion = urllib.request.Request(
        url,
        headers={
            "User-Agent": AGENTE,
            "Accept": "application/vnd.citationstyle.csl+json",
        },
    )
    try:
        with urllib.request.urlopen(peticion, timeout=20) as respuesta:
            datos = json.load(respuesta)
    except (urllib.error.URLError, TimeoutError, ValueError):
        return None
    titulo = datos.get("title")
    if isinstance(titulo, list):
        titulo = titulo[0] if titulo else ""
    try:
        anio = str(datos["issued"]["date-parts"][0][0])
    except (KeyError, IndexError, TypeError):
        anio = ""
    return {"titulo": titulo or "", "anio": anio}


def parecido(a, b):
    def norm(texto):
        return re.sub(r"[^a-z0-9áéíóúüñ ]", "", texto.lower())

    return difflib.SequenceMatcher(None, norm(a), norm(b)).ratio()


def revisar(doi, titulo_matriz="", anio_matriz=""):
    """Devuelve (estado, detalle); estado es si | no | sin_comprobar."""
    resuelve = existe(doi)
    if resuelve is False:
        return "no", "doi.org no lo reconoce: el DOI no existe"
    if resuelve is None:
        return "sin_comprobar", "no se pudo consultar doi.org (red)"
    meta = metadatos(doi)
    if meta is None or not meta["titulo"]:
        return "si", "existe (metadatos no disponibles; comparar el título a mano)"
    if titulo_matriz and parecido(titulo_matriz, meta["titulo"]) < UMBRAL_TITULO:
        return "no", f"el DOI existe pero es de otro trabajo: «{meta['titulo']}»"
    if anio_matriz and meta["anio"] and anio_matriz.strip() != meta["anio"]:
        return "si", f"existe; ojo, año registrado {meta['anio']} ≠ matriz {anio_matriz}"
    return "si", "existe y el título coincide"


def main():
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument("matriz", nargs="?", help="ruta a 02_matriz.csv")
    parser.add_argument("--doi", action="append", help="verificar un DOI suelto")
    parser.add_argument(
        "--actualizar", action="store_true", help="escribir doi_verificado en la matriz"
    )
    args = parser.parse_args()

    if args.doi:
        fallos = 0
        for valor in args.doi:
            doi = limpiar_doi(valor)
            estado, detalle = revisar(doi) if doi else ("no", "formato de DOI inválido")
            fallos += estado != "si"
            print(f"[{estado}] {valor}: {detalle}")
        return 1 if fallos else 0

    if not args.matriz:
        parser.error("indica la ruta de la matriz o usa --doi")

    with open(args.matriz, newline="", encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)
        columnas = lector.fieldnames
        filas = list(lector)

    fallos = 0
    for fila in filas:
        doi = limpiar_doi(fila.get("doi_o_url"))
        if not doi:
            estado, detalle = "sin_doi", "sin DOI (URL u otra referencia)"
        else:
            estado, detalle = revisar(doi, fila.get("titulo", ""), fila.get("anio", ""))
        fallos += estado in ("no", "sin_comprobar")
        if estado != "sin_comprobar":
            fila["doi_verificado"] = estado
        print(f"[{estado}] {fila.get('id', '?')} {fila.get('doi_o_url', '')}: {detalle}")

    if args.actualizar:
        with open(args.matriz, "w", newline="", encoding="utf-8") as archivo:
            escritor = csv.DictWriter(archivo, fieldnames=columnas)
            escritor.writeheader()
            escritor.writerows(filas)
        print(f"\nMatriz actualizada: {args.matriz}")

    print(f"\n{len(filas)} fuentes revisadas, {fallos} con problemas.")
    return 1 if fallos else 0


if __name__ == "__main__":
    sys.exit(main())
