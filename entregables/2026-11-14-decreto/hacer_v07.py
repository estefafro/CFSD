"""Crea la v0.7 del decreto a partir de la v0.6 editada por la titular, con cambios de forma y de nombre.
Uso: python3 hacer_v07.py <v0.6.docx> <v0.7.docx>"""
import sys
from docx import Document

CAMBIOS = [
    ("versión 0.6", "versión 0.7"),
    ("del campo.. Para ello", "del campo. Para ello"),
    ("integrada por la Dirección Nacional, la Dirección de Docencia y la Dirección de Proyectos, en adelante “las Direcciones de área”, las Direcciones de Sede y sus académicos, y contará",
     "integrada por la Dirección Nacional; por la Dirección de Docencia y la Dirección de Investigación, en adelante “las Direcciones de área”; por las Direcciones de Sede, y por sus académicos, y contará"),
    ("La Dirección de Proyectos, que comprende", "La Dirección de Investigación, que comprende"),
]


def reemplazar(par, viejo, nuevo):
    texto = "".join(r.text for r in par.runs)
    i = texto.find(viejo)
    if i < 0:
        return False
    j, pos, hecho = i + len(viejo), 0, False
    for r in par.runs:
        ini, fin = pos, pos + len(r.text)
        pos = fin
        if fin <= i or ini >= j:
            continue
        antes = r.text[: max(0, i - ini)]
        despues = r.text[max(0, j - ini):] if fin > j else ""
        r.text = antes + ("" if hecho else nuevo) + despues
        hecho = True
    return True


d = Document(sys.argv[1])
pars = list(d.paragraphs)
for s in d.sections:
    pars += list(s.header.paragraphs) + list(s.footer.paragraphs)
for viejo, nuevo in CAMBIOS:
    n = sum(reemplazar(p, viejo, nuevo) for p in pars)
    print(n, "·", viejo[:50])
d.save(sys.argv[2])
