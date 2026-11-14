"""Tres borradores de swimlane para el Departamento Nacional de Salud Digital, sobre la plantilla USS."""
import sys
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE, MSO_CONNECTOR
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.oxml.ns import qn
from lxml import etree

SRC, OUT = sys.argv[1], sys.argv[2]
NAVY, BLUE, GOLD, PALE, GRIS, LINEA, BLANCO = "14375A", "2F6DB5", "A8843A", "EAF1FA", "5F6470", "C9D3E0", "FFFFFF"
ORO_PALIDO = "F6EFDF"

prs = Presentation(SRC)
# quitar las láminas originales; se conservan patrón y diseños
ids = prs.slides._sldIdLst
for sld in list(ids):
    prs.part.drop_rel(sld.rId)
    ids.remove(sld)
LAYOUT = [l for l in prs.slide_layouts if l.name.strip() == "INTERIOR"][0]


def rgb(h):
    return RGBColor.from_string(h)


def texto(sl, x, y, w, h, t, size=11, color=NAVY, bold=False, align=PP_ALIGN.LEFT, font="Calibri", italic=False, anchor=MSO_ANCHOR.MIDDLE):
    tb = sl.shapes.add_textbox(Inches(x), Inches(y), Inches(w), Inches(h))
    tf = tb.text_frame
    tf.word_wrap = True
    tf.vertical_anchor = anchor
    for m in ("margin_left", "margin_right", "margin_top", "margin_bottom"):
        setattr(tf, m, 0)
    p = tf.paragraphs[0]
    p.alignment = align
    r = p.add_run()
    r.text = t
    r.font.size, r.font.bold, r.font.italic, r.font.name = Pt(size), bold, italic, font
    r.font.color.rgb = rgb(color)
    return tb


def forma(sl, kind, x, y, w, h, t="", fill=PALE, color=NAVY, size=10, bold=False, borde=None, nombre=None):
    sh = sl.shapes.add_shape(kind, Inches(x), Inches(y), Inches(w), Inches(h))
    sh.shadow.inherit = False
    sh.fill.solid()
    sh.fill.fore_color.rgb = rgb(fill)
    if borde:
        sh.line.color.rgb = rgb(borde)
        sh.line.width = Pt(1.25)
    else:
        sh.line.fill.background()
    if kind == MSO_SHAPE.ROUNDED_RECTANGLE:
        sh.adjustments[0] = 0.18
    tf = sh.text_frame
    tf.word_wrap = True
    tf.vertical_anchor = MSO_ANCHOR.MIDDLE
    for m in ("margin_left", "margin_right"):
        setattr(tf, m, Inches(0.05))
    tf.margin_top = tf.margin_bottom = Inches(0.02)
    p = tf.paragraphs[0]
    p.alignment = PP_ALIGN.CENTER
    r = p.add_run()
    r.text = t
    r.font.size, r.font.bold, r.font.name = Pt(size), bold, "Calibri"
    r.font.color.rgb = rgb(color)
    if nombre:
        sh.name = nombre
    return sh


def caja(sl, cx, cy, t, w=1.75, h=0.5, fill=PALE, color=NAVY, **k):
    return forma(sl, MSO_SHAPE.ROUNDED_RECTANGLE, cx - w / 2, cy - h / 2, w, h, t, fill, color, **k)


def rombo(sl, cx, cy, t, w=1.7, h=0.74, **k):
    return forma(sl, MSO_SHAPE.DIAMOND, cx - w / 2, cy - h / 2, w, h, t, BLANCO, NAVY, borde=GOLD, size=9, bold=True, **k)


SITIO = {"arriba": 0, "izq": 1, "abajo": 2, "der": 3}


def flecha(sl, a, b, sa="der", sb="izq", color=NAVY, recta=False, grosor=1.5):
    c = sl.shapes.add_connector(MSO_CONNECTOR.STRAIGHT if recta else MSO_CONNECTOR.ELBOW, 0, 0, 0, 0)
    c.begin_connect(a, SITIO[sa])
    c.end_connect(b, SITIO[sb])
    c.line.color.rgb = rgb(color)
    c.line.width = Pt(grosor)
    ln = c.line._get_or_add_ln()
    ln.append(etree.SubElement(ln, qn("a:tailEnd"), {"type": "triangle", "w": "med", "len": "med"}))
    return c


def codo(c, frac):
    """Mueve el tramo vertical del conector acodado (fracción del ancho; >1 lo saca más allá del destino)."""
    g = c._element.spPr.find(qn("a:prstGeom"))
    av = g.find(qn("a:avLst"))
    if av is None:
        av = etree.SubElement(g, qn("a:avLst"))
    for ch in list(av):
        av.remove(ch)
    etree.SubElement(av, qn("a:gd"), {"name": "adj1", "fmla": f"val {int(frac * 100000)}"})
    return c


def base(kicker, titulo):
    sl = prs.slides.add_slide(LAYOUT)
    for ph in list(sl.placeholders):
        if ph.placeholder_format.idx != 0:
            ph._element.getparent().remove(ph._element)
    t = sl.shapes.title
    t.left, t.top, t.width, t.height = Inches(0.6), Inches(0.56), Inches(12.1), Inches(0.8)
    t.text_frame.text = titulo
    r = t.text_frame.paragraphs[0].runs[0]
    r.font.name, r.font.size, r.font.bold = "Cambria", Pt(28), True
    r.font.color.rgb = rgb(NAVY)
    texto(sl, 0.6, 0.3, 11, 0.3, kicker, 11, BLUE, True)
    return sl


def carriles(sl, defs, x0=0.6, wl=1.75, x1=12.72, y0=1.88):
    """defs: [(nombre, detalle, alto, destacado)] -> dict nombre -> y centro"""
    y, cen = y0, {}
    for nombre, det, h, dest in defs:
        fondo = sl.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(x0 + wl + 0.05), Inches(y), Inches(x1 - x0 - wl - 0.05), Inches(h - 0.05))
        fondo.shadow.inherit = False
        fondo.fill.solid()
        fondo.fill.fore_color.rgb = rgb("F4F7FB" if not dest else "E4ECF7")
        fondo.line.fill.background()
        et = forma(sl, MSO_SHAPE.RECTANGLE, x0, y, wl, h - 0.05, "", NAVY if dest else PALE)
        tf = et.text_frame
        tf.paragraphs[0].runs[0].text = nombre
        tf.paragraphs[0].runs[0].font.bold = True
        tf.paragraphs[0].runs[0].font.size = Pt(11)
        tf.paragraphs[0].runs[0].font.color.rgb = rgb(BLANCO if dest else NAVY)
        if det:
            p = tf.add_paragraph()
            p.alignment = PP_ALIGN.CENTER
            r = p.add_run()
            r.text = det
            r.font.size, r.font.name = Pt(8), "Calibri"
            r.font.color.rgb = rgb("D6E2F2" if dest else GRIS)
        cen[nombre] = y + (h - 0.05) / 2
        y += h
    return cen


def fases(sl, nombres, x0=2.4, x1=12.72, y=1.5, h=0.3):
    w = (x1 - x0) / len(nombres)
    for i, n in enumerate(nombres):
        forma(sl, MSO_SHAPE.CHEVRON if False else MSO_SHAPE.RECTANGLE, x0 + i * w + 0.03, y, w - 0.06, h, n, NAVY, BLANCO, 10, True)
    return [x0 + i * w for i in range(len(nombres))], w


def nota(sl, t, y=6.72):
    texto(sl, 0.6, y, 12.1, 0.25, t, 9.5, GRIS, italic=True)


LANES = [("Vicerrectorías", "Académica · VRID · VcM y Proyectos Institucionales", 0.86, False),
         ("Facultad", "Decanato · Consejo de Facultad", 0.86, False),
         ("Departamento Nacional de Salud Digital", "Dirección · Áreas · Comité Consultivo", 1.12, True),
         ("Sedes", "Coordinaciones de Sede", 0.7, False),
         ("Carreras y escuelas", "", 0.64, False),
         ("Otras facultades", "ingeniería, derecho y otras", 0.64, False)]

# ---------------------------------------------------------------- Opción 1
sl = base("OPCIÓN 1 · BORRADOR", "El ciclo anual del Departamento, de punta a punta")
cy = carriles(sl, LANES)
xs, w = fases(sl, ["1 · Levantar", "2 · Planificar y decidir", "3 · Validar y ejecutar", "4 · Evaluar y rendir cuenta"])
xa = [x + 0.68 for x in xs]
xb = [x + 1.93 for x in xs]
VR, FA, DE, SE, CA, OT = (cy[n[0]] for n in LANES)
A = caja(sl, 3.38, CA, "Requerimientos de formación", w=1.9, h=0.44)
B = caja(sl, 3.38, OT, "Académicos y capacidades", w=1.9, h=0.44)
C = caja(sl, 4.58, SE, "La Coordinación de Sede consolida", w=1.55, h=0.5)
D = caja(sl, 5.76, DE, "Plan anual y propuestas: docencia, investigación y vinculación", w=1.8, h=0.8, fill=NAVY, color=BLANCO)
E = rombo(sl, 6.81, FA, "¿Aprueba la Decana?", w=1.6)
F = caja(sl, 8.6, VR, "Validan y coordinan según su materia", w=1.6, h=0.5)
G = caja(sl, 8.6, DE, "Programa y coordina la ejecución", w=1.6, h=0.6, fill=NAVY, color=BLANCO)
H = caja(sl, 9.55, SE, "Se ejecuta en las cuatro sedes", w=1.2, h=0.5, size=9)
I = caja(sl, 11.0, SE, "Indicadores locales", w=1.2, h=0.44)
J = rombo(sl, 11.0, DE, "¿Equivalente entre sedes?", w=1.66, h=0.94)
K = caja(sl, 12.3, DE, "Cuenta anual", w=0.8, h=0.56, fill=NAVY, color=BLANCO, size=9)
L = caja(sl, 12.3, FA, "Consejo de Facultad", w=0.8, h=0.56, size=9)
M = caja(sl, 12.3, VR, "Reciben resultados", w=0.8, h=0.56, size=9)
flecha(sl, A, C, "der", "abajo")
flecha(sl, B, C, "der", "abajo")
flecha(sl, C, D, "arriba", "izq")
flecha(sl, D, E, "arriba", "izq")
flecha(sl, E, D, "abajo", "der", color=GOLD)
flecha(sl, E, F, "der", "izq")
flecha(sl, F, G, "abajo", "arriba", recta=True)
flecha(sl, G, H, "abajo", "izq")
flecha(sl, H, I, "der", "izq", recta=True)
flecha(sl, I, J, "arriba", "abajo", recta=True)
flecha(sl, J, G, "izq", "der", color=GOLD, recta=True)
flecha(sl, J, K, "der", "izq", recta=True)
flecha(sl, K, L, "arriba", "abajo", recta=True)
flecha(sl, L, M, "arriba", "abajo", recta=True)
texto(sl, 6.95, FA + 0.38, 0.9, 0.2, "No: se ajusta", 8.5, GOLD, True)
texto(sl, 7.62, FA - 0.24, 0.3, 0.2, "Sí", 8.5, NAVY, True)
texto(sl, 9.45, DE - 0.22, 0.8, 0.2, "No: ajusta", 8.5, GOLD, True, align=PP_ALIGN.CENTER)
texto(sl, 11.76, DE - 0.22, 0.2, 0.2, "Sí", 8.5, NAVY, True)
nota(sl, "Un solo recorrido que muestra en qué momento del año interviene cada actor y qué decide.")

# ---------------------------------------------------------------- Opción 2
sl = base("OPCIÓN 2 · BORRADOR", "Tres productos, un mismo camino por el Departamento")
L2 = [("Vicerrectorías", "cada una recibe lo suyo", 1.2, False), ("Facultad", "Decanato · Consejo de Facultad", 0.72, False),
      ("Departamento Nacional de Salud Digital", "Dirección · Áreas · Comité Consultivo", 1.32, True),
      ("Sedes", "Coordinaciones de Sede", 0.54, False), ("Carreras y escuelas", "", 0.52, False), ("Otras facultades", "", 0.52, False)]
cy = carriles(sl, L2)
xs, w = fases(sl, ["Origen", "El Departamento articula", "Se decide", "Se valida", "Producto"])
xc = [x + w / 2 for x in xs]
VR, FA, DE, SE, CA, OT = (cy[n[0]] for n in L2)
COL = {"doc": NAVY, "inv": BLUE, "vcm": GOLD}
o_doc = caja(sl, xc[0], CA, "Necesidad formativa", w=1.8, h=0.38, borde=NAVY, fill=BLANCO)
o_vcm = caja(sl, xc[0], SE, "Necesidad del territorio", w=1.8, h=0.38, borde=GOLD, fill=BLANCO)
o_inv = caja(sl, xc[0], OT, "Académicos y disciplinas", w=1.8, h=0.38, borde=BLUE, fill=BLANCO)
d_doc = caja(sl, xc[1], DE - 0.41, "Área de Docencia: diseña y actualiza", w=1.9, h=0.36, fill=NAVY, color=BLANCO, size=9)
d_inv = caja(sl, xc[1], DE, "Área IVP: líneas y postulaciones", w=1.9, h=0.36, fill=BLUE, color=BLANCO, size=9)
d_vcm = caja(sl, xc[1], DE + 0.41, "Área IVP: iniciativas con las unidades de VcM", w=1.9, h=0.36, fill=GOLD, color=BLANCO, size=9)
dec = rombo(sl, xc[2], FA, "La Decana decide", w=1.6, h=0.62)
v_doc = caja(sl, xc[3], VR - 0.36, "Vicerrectoría Académica", w=1.9, h=0.3, borde=NAVY, fill=BLANCO, size=9)
v_inv = caja(sl, xc[3], VR, "VRID", w=1.9, h=0.3, borde=BLUE, fill=BLANCO, size=9)
v_vcm = caja(sl, xc[3], VR + 0.36, "VcM y Proyectos Institucionales", w=1.9, h=0.3, borde=GOLD, fill=BLANCO, size=9)
p_doc = caja(sl, xc[4] - 0.12, CA, "Asignaturas, electivos y programas", w=1.65, h=0.4, fill=NAVY, color=BLANCO, size=9)
p_vcm = caja(sl, xc[4] - 0.12, SE, "Iniciativas y alianzas", w=1.65, h=0.4, fill=GOLD, color=BLANCO, size=9)
p_inv = caja(sl, xc[4] - 0.12, OT, "Proyectos y publicaciones", w=1.65, h=0.4, fill=BLUE, color=BLANCO, size=9)
for k, o, d, v, p, f1, f3 in (("doc", o_doc, d_doc, v_doc, p_doc, 0.5, 1.10), ("inv", o_inv, d_inv, v_inv, p_inv, 0.3, 1.22), ("vcm", o_vcm, d_vcm, v_vcm, p_vcm, 0.7, 1.16)):
    codo(flecha(sl, o, d, "der", "izq", COL[k]), f1)
    flecha(sl, d, dec, "der", "abajo" if k != "doc" else "izq", COL[k])
    flecha(sl, dec, v, "der", "izq", COL[k])
    codo(flecha(sl, v, p, "der", "der", COL[k]), f3)
for i, (t, c) in enumerate((("Docencia", NAVY), ("Investigación", BLUE), ("Vinculación con el medio", GOLD))):
    forma(sl, MSO_SHAPE.RECTANGLE, 0.6 + i * 2.2, 6.74, 0.22, 0.14, "", c)
    texto(sl, 0.88 + i * 2.2, 6.68, 1.9, 0.25, t, 9.5, GRIS)
texto(sl, 7.3, 6.68, 5.4, 0.25, "Cada actor ve qué pide, por dónde pasa y qué recibe de vuelta.", 9.5, GRIS, italic=True, align=PP_ALIGN.RIGHT)

# ---------------------------------------------------------------- Opción 3
sl = base("OPCIÓN 3 · BORRADOR", "Qué aporta cada actor y qué recibe del Departamento")
filas = [("Vicerrectoría Académica", "Política y normativa académica", "Oferta equivalente entre sedes e indicadores de docencia"),
         ("VRID", "Política de Investigación y fondos internos", "Líneas, proyectos y publicaciones con afiliación"),
         ("VcM y Proyectos Institucionales", "Unidades y lineamientos de vinculación", "Aporte especializado a sus iniciativas y alianzas"),
         ("Facultad", "Autoridad de la Decana, designaciones y presupuesto", "Plan de Desarrollo, cuenta anual y actas del Comité"),
         ("Sedes", "Realidad local e indicadores", "Lineamientos técnicos y formación equivalente"),
         ("Carreras y escuelas", "Requerimientos y perfiles de egreso", "Asignaturas, electivos y marco de desempeños"),
         ("Otras facultades", "Académicos y disciplinas", "Líneas conjuntas y servicios académicos")]
y0, hf = 1.92, 0.675
texto(sl, 2.5, 1.5, 3.3, 0.3, "APORTA", 10, BLUE, True, PP_ALIGN.CENTER)
texto(sl, 9.42, 1.5, 3.3, 0.3, "RECIBE", 10, BLUE, True, PP_ALIGN.CENTER)
centro = forma(sl, MSO_SHAPE.ROUNDED_RECTANGLE, 6.3, y0, 2.6, hf * len(filas) - 0.08, "", NAVY, BLANCO)
centro.adjustments[0] = 0.06
tf = centro.text_frame
tf.paragraphs[0].runs[0].text = "Departamento Nacional de Salud Digital"
tf.paragraphs[0].runs[0].font.size = Pt(15)
tf.paragraphs[0].runs[0].font.bold = True
tf.paragraphs[0].runs[0].font.name = "Cambria"
for t in ("", "Dirección Nacional", "Área de Docencia", "Área IVP", "Coordinaciones de Sede", "Comité Consultivo", "", "articula · decide dentro de sus materias · rinde cuenta"):
    p = tf.add_paragraph()
    p.alignment = PP_ALIGN.CENTER
    r = p.add_run()
    r.text = t
    r.font.size, r.font.name = Pt(11 if not t.startswith("articula") else 9.5), "Calibri"
    r.font.italic = t.startswith("articula")
    r.font.color.rgb = rgb("D6E2F2")
for i, (n, da, rec) in enumerate(filas):
    y = y0 + i * hf
    forma(sl, MSO_SHAPE.RECTANGLE, 0.6, y, 1.8, hf - 0.08, n, PALE, NAVY, 10, True)
    a = forma(sl, MSO_SHAPE.ROUNDED_RECTANGLE, 2.5, y, 3.3, hf - 0.08, da, "F4F7FB", NAVY, 10)
    b = forma(sl, MSO_SHAPE.ROUNDED_RECTANGLE, 9.42, y, 3.3, hf - 0.08, rec, ORO_PALIDO, NAVY, 10)
    for xa_, xb_ in ((5.82, 6.28), (8.92, 9.4)):
        c = sl.shapes.add_connector(MSO_CONNECTOR.STRAIGHT, Inches(xa_), Inches(y + (hf - 0.08) / 2), Inches(xb_), Inches(y + (hf - 0.08) / 2))
        c.line.color.rgb = rgb(NAVY)
        c.line.width = Pt(1.5)
        ln = c.line._get_or_add_ln()
        ln.append(etree.SubElement(ln, qn("a:tailEnd"), {"type": "triangle", "w": "med", "len": "med"}))
nota(sl, "No es un proceso paso a paso: es el mapa de intercambios. Sirve como lámina de entrada antes del flujo.")

prs.save(OUT)
print("ok", len(prs.slides))
