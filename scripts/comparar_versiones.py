#!/usr/bin/env python3
"""Huella y diferencias de texto entre versiones de un documento.

Uso:
  python3 scripts/comparar_versiones.py <archivo>            -> huella y número de palabras
  python3 scripts/comparar_versiones.py <anterior> <nuevo>   -> huellas y diferencias

Lee .docx, .pptx, .pdf y archivos de texto. La huella se calcula sobre el texto
normalizado (sin diferencias de espacios), no sobre el archivo, para que dos
copias con el mismo contenido tengan la misma huella.
"""
import difflib
import hashlib
import re
import subprocess
import sys
from pathlib import Path


def texto(ruta):
    p = Path(ruta)
    ext = p.suffix.lower()
    if ext == ".docx":
        from docx import Document
        d = Document(str(p))
        lineas = [x.text for x in d.paragraphs]
        for t in d.tables:
            for fila in t.rows:
                lineas.append(" | ".join(c.text for c in fila.cells))
    elif ext == ".pptx":
        from pptx import Presentation
        lineas = []
        for i, lam in enumerate(Presentation(str(p)).slides, 1):
            lineas.append(f"[Lámina {i}]")
            for forma in lam.shapes:
                if forma.has_text_frame:
                    lineas += [x.text for x in forma.text_frame.paragraphs]
    elif ext == ".pdf":
        salida = subprocess.run(["pdftotext", "-layout", str(p), "-"], capture_output=True, text=True, check=True)
        lineas = salida.stdout.splitlines()
    else:
        lineas = p.read_text(encoding="utf-8", errors="replace").splitlines()
    return [re.sub(r"\s+", " ", x).strip() for x in lineas if x.strip()]


def huella(lineas):
    return hashlib.sha256("\n".join(lineas).encode("utf-8")).hexdigest()[:12]


def resumen(ruta, lineas):
    palabras = sum(len(x.split()) for x in lineas)
    print(f"{ruta}\n  huella: {huella(lineas)} · {len(lineas)} párrafos · {palabras} palabras")


def main():
    if len(sys.argv) not in (2, 3):
        sys.exit(__doc__)
    a = texto(sys.argv[1])
    resumen(sys.argv[1], a)
    if len(sys.argv) == 2:
        return
    b = texto(sys.argv[2])
    resumen(sys.argv[2], b)
    if huella(a) == huella(b):
        print("\nMISMO TEXTO: las dos versiones dicen lo mismo.")
        return
    print("\nDIFERENCIAS (- anterior, + nuevo):")
    for linea in difflib.unified_diff(a, b, lineterm="", n=0):
        if linea.startswith(("---", "+++", "@@")):
            continue
        print(linea)


if __name__ == "__main__":
    main()
