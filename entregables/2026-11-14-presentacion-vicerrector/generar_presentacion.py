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
    titulo = prs.part.related_part(sld.rId).slide.shapes.title
    _sl = prs.part.related_part(sld.rId).slide
    if _sl.slide_layout.name.strip() == "PORTADA":
        continue  # se conserva la portada original, con texto nuevo
    if titulo is not None and titulo.text_frame.text.startswith("Organigrama"):
        continue  # se conserva el organigrama matricial original
    prs.part.drop_rel(sld.rId)
    ids.remove(sld)
assert len(ids) == 2, "no se encontraron la portada y el organigrama originales"
# renombrar las láminas conservadas para que no choquen con los nombres de las nuevas
from pptx.opc.packuri import PackURI
for _i, _sld in enumerate(ids, start=1):
    prs.part.related_part(_sld.rId).partname = PackURI("/ppt/slides/slide%d.xml" % _i)
_portada = prs.part.related_part(ids[0].rId).slide
_sub = [ph for ph in _portada.placeholders if ph.placeholder_format.idx == 1][0]
_runs = [r for par in _sub.text_frame.paragraphs for r in par.runs]
assert len(_runs) == 2, len(_runs)
_runs[0].text = "Formación, articulación y línea de investigación"
_runs[1].text = "Vicerrectoría Académica · noviembre de 2026"
_org = prs.part.related_part(ids[1].rId).slide
_cambios = {"Área IVP": "Área de Proyectos", "investigación · vinculación con el medio · proyectos": "línea basal · investigación · vinculación con el medio",
            "seguimiento · análisis comparado · propuestas": "pregrado · postgrado · educación continua"}
_hechos = 0
for _sh in _org.shapes:
    if _sh.has_text_frame:
        for _p in _sh.text_frame.paragraphs:
            for _r in _p.runs:
                if _r.text in _cambios:
                    _r.text = _cambios[_r.text]
                    _hechos += 1
        if _sh.name == "Área IVP":
            _sh.name = "Área de Proyectos"
assert _hechos == 3, _hechos
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
    t.text_frame.margin_left = t.text_frame.margin_right = 0
    t.text_frame.vertical_anchor = MSO_ANCHOR.TOP
    k = texto(sl, 0.6, 0.3, 11, 0.3, kicker, 11, BLUE, True, anchor=MSO_ANCHOR.TOP)
    k.text_frame.paragraphs[0].runs[0]._r.get_or_add_rPr().set("spc", "180")  # mismo espaciado que la plantilla
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
sl = base("OPCIÓN 1", "El ciclo anual del Departamento, de punta a punta")
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
sl = base("OPCIÓN 2", "Tres productos, un mismo camino por el Departamento")
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
d_inv = caja(sl, xc[1], DE, "Área de Proyectos: investigación", w=1.9, h=0.36, fill=BLUE, color=BLANCO, size=9)
d_vcm = caja(sl, xc[1], DE + 0.41, "Área de Proyectos: vinculación con el medio", w=1.9, h=0.36, fill=GOLD, color=BLANCO, size=9)
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
sl = base("OPCIÓN 3", "Qué aporta cada actor y qué recibe del Departamento")
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
for t in ("", "Dirección Nacional", "Área de Docencia", "Área de Proyectos", "Coordinaciones de Sede", "Comité Consultivo", "", "articula · decide dentro de sus materias · rinde cuenta"):
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

# ---------------------------------------------------------------- Ciclo de formación y empleabilidad
sl = base("CICLO DE FORMACIÓN Y EMPLEABILIDAD", "Del mundo laboral a la sala de clases, y de vuelta")
# dos bandas: mundo laboral arriba, universidad abajo
for y, h, nombre, det, osc in ((1.62, 1.55, "Mundo laboral", "sistema de salud · empleadores", False), (3.3, 3.2, "Universidad", "Departamento Nacional de Salud Digital", True)):
    f = sl.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(2.4), Inches(y), Inches(10.32), Inches(h))
    f.shadow.inherit = False
    f.fill.solid()
    f.fill.fore_color.rgb = rgb("E4ECF7" if osc else ORO_PALIDO)
    f.line.fill.background()
    et = forma(sl, MSO_SHAPE.RECTANGLE, 0.6, y, 1.75, h, "", NAVY if osc else GOLD)
    tf = et.text_frame
    tf.paragraphs[0].runs[0].text = nombre
    tf.paragraphs[0].runs[0].font.bold = True
    tf.paragraphs[0].runs[0].font.size = Pt(13)
    tf.paragraphs[0].runs[0].font.color.rgb = rgb(BLANCO)
    p = tf.add_paragraph()
    p.alignment = PP_ALIGN.CENTER
    r = p.add_run()
    r.text = det
    r.font.size, r.font.name = Pt(9), "Calibri"
    r.font.color.rgb = rgb(BLANCO)


def estacion(sl, n, cx, cy, titulo, det, w=1.86, oscuro=False, oro=False, lado=None):
    fill = GOLD if oro else (NAVY if oscuro else BLANCO)
    col = BLANCO if (oro or oscuro) else NAVY
    sh = forma(sl, MSO_SHAPE.ROUNDED_RECTANGLE, cx - w / 2, cy - 0.33, w, 0.66, titulo, fill, col, 11, True, borde=None if (oro or oscuro) else NAVY)
    num = forma(sl, MSO_SHAPE.OVAL, cx - w / 2 - 0.13, cy - 0.47, 0.34, 0.34, str(n), GOLD if not oro else NAVY, BLANCO, 10, True)
    if lado == "der":
        texto(sl, cx + w / 2 + 0.15, cy + 0.1, 2.3, 0.6, det, 9.5, NAVY, anchor=MSO_ANCHOR.TOP)
    elif lado == "izq":
        texto(sl, cx - w / 2 - 2.45, cy + 0.1, 2.3, 0.6, det, 9.5, NAVY, align=PP_ALIGN.RIGHT, anchor=MSO_ANCHOR.TOP)
    else:
        texto(sl, cx - w / 2, cy + 0.4, w, 0.75, det, 9.5, GRIS, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.TOP)
    return sh


ML, UN = 2.2, 4.25
xs5 = [3.5, 5.53, 7.56, 9.59, 11.62]
e1 = estacion(sl, 1, xs5[0], ML, "Necesidades", "Un sistema de salud que se digitaliza y al que le falta personal", oro=True, lado="der")
e7 = estacion(sl, 7, xs5[4], ML, "Empleabilidad", "Egresados que el sistema necesita y sabe reconocer", oro=True, lado="izq")
e2 = estacion(sl, 2, xs5[0], UN, "Lectura del mundo laboral", "Seguimiento de tendencias, normativa y demanda")
e3 = estacion(sl, 3, xs5[1], UN, "Selección de oportunidades", "")
for j, op in enumerate(("Actualización de la asignatura", "Electivo de salud con ingeniería", "Diplomado, en desarrollo")):
    forma(sl, MSO_SHAPE.ROUNDED_RECTANGLE, xs5[1] - 0.93, UN + 0.42 + j * 0.3, 1.86, 0.26, op, ORO_PALIDO, NAVY, 9, borde=GOLD)
e4 = estacion(sl, 4, xs5[2], UN, "Benchmarking", "Comparar con marcos y programas del mundo")
e5 = estacion(sl, 5, xs5[3], UN, "Propuestas de implementación", "Asignaturas, electivos, programas y marco de desempeños")
e6 = estacion(sl, 6, xs5[4], UN, "Competencias en los estudiantes", "Formación equivalente en las cuatro sedes", oscuro=True)
flecha(sl, e1, e2, "abajo", "arriba", recta=True, grosor=2)
for a_, b_ in ((e2, e3), (e3, e4), (e4, e5), (e5, e6)):
    flecha(sl, a_, b_, "der", "izq", recta=True, grosor=2)
flecha(sl, e6, e7, "arriba", "abajo", recta=True, grosor=2)
flecha(sl, e7, e1, "izq", "der", color=GOLD, recta=True, grosor=2)
texto(sl, 5.4, ML - 0.32, 4.4, 0.24, "el mundo laboral cambia y vuelve a pedir", 9.5, GOLD, True, PP_ALIGN.CENTER, italic=True)
# franja: quién lo hace en el Departamento
forma(sl, MSO_SHAPE.ROUNDED_RECTANGLE, 2.57, 5.62, 7.95, 0.62, "Área de Docencia: seguimiento, análisis comparado y propuestas (artículo 10)  ·  Comité Consultivo y Decana: priorizan y deciden", NAVY, BLANCO, 10)
forma(sl, MSO_SHAPE.ROUNDED_RECTANGLE, 10.69, 5.62, 1.86, 0.62, "Coordinaciones de Sede: equivalencia", NAVY, BLANCO, 9.5)
nota(sl, "El ciclo se repite: lo que el sistema de salud pide hoy define lo que se enseña mañana, y los egresados cambian lo que el sistema puede hacer.")

# ---------------------------------------------------------------- Cifras del ciclo
sl = base("CICLO DE FORMACIÓN Y EMPLEABILIDAD", "Las cifras detrás del ciclo")
cifras = [("1", "170 M", "empleos nuevos en el mundo a 2030; cerca del 40% de las habilidades clave va a cambiar", "Foro Económico Mundial, Future of Jobs 2025"),
          ("1", "0,6 a 2 M", "trabajadores de salud faltarán en las Américas a 2030 si no hay intervenciones", "OPS, 30 de abril de 2025"),
          ("2", "3.500", "profesionales faltaban en Chile para la transformación digital de la salud", "CENS, estimación de 2019"),
          ("4", "35 → 0", "marcos de competencias en salud digital revisó la OMS; ningún marco nacional es de América Latina", "OMS, junio de 2026"),
          ("6", "1.788", "estudiantes cursan Salud Digital este semestre: 31 secciones, 4 carreras, 4 sedes", "Blackboard USS, 25 de septiembre de 2026"),
          ("7", "Por medir", "la USS mide empleabilidad, pero no en salud digital ni en competencias digitales", "Oportunidad: sumar esa mirada al seguimiento de egresados")]
w, h, g = 3.9, 2.25, 0.2
for i, (et, num, lab, fu) in enumerate(cifras):
    x = 0.6 + (i % 3) * (w + g)
    y = 1.62 + (i // 3) * (h + g)
    ult = i == 5
    forma(sl, MSO_SHAPE.ROUNDED_RECTANGLE, x, y, w, h, "", ORO_PALIDO if ult else PALE).adjustments[0] = 0.08
    forma(sl, MSO_SHAPE.OVAL, x + 0.2, y + 0.2, 0.36, 0.36, et, GOLD, BLANCO, 10, True)
    texto(sl, x + 0.7, y + 0.16, w - 0.9, 0.45, "etapa " + et + " del ciclo", 9.5, GRIS)
    texto(sl, x + 0.25, y + 0.62, w - 0.5, 0.7, num, 34 if not ult else 28, GOLD if ult else NAVY, True, font="Cambria")
    texto(sl, x + 0.25, y + 1.32, w - 0.5, 0.56, lab, 11, NAVY, anchor=MSO_ANCHOR.TOP)
    texto(sl, x + 0.25, y + 1.9, w - 0.5, 0.25, fu, 8.5, GRIS, italic=True)
nota(sl, "La etapa 7 es la oportunidad: medir la empleabilidad en salud digital cierra el ciclo.")

# ---------------------------------------------------------------- Mismo modelo, macro y micro
sl = base("MACRO Y MICRO", "El mismo modelo, de la sede a las Vicerrectorías")
pasos = ["1 · Levantar y ordenar", "2 · Comparar", "3 · Crear y proponer", "4 · Calidad y trazabilidad", "5 · Medir y elevar"]
niveles = [
    ("Dirección Nacional", "nivel macro", True,
     ["Integra lo que elevan las Áreas", "Lee el mundo laboral y el sistema de salud", "Levanta la necesidad y propone cómo responder", "Plan de Desarrollo y cuenta anual",
      "Entrega a cada Vicerrectoría lo suyo: Académica, VRID, VcM y Proyectos Institucionales"]),
    ("Área de Docencia", "pregrado · postgrado · educación continua", False,
     ["Consolida la información de las sedes", "Benchmarking nacional e internacional", "Creación y actualización de asignaturas y programas", "Calidad, trazabilidad, competencias y resultados de aprendizaje",
      "Eleva a la Dirección Nacional"]),
    ("Área de Proyectos", "línea basal · investigación · vinculación con el medio", False,
     ["Capacidades, líneas y socios", "Fondos, convocatorias y referentes", "Formula proyectos e iniciativas", "Seguimiento de proyectos; centro de costos (en evaluación)",
      "Eleva a la Dirección Nacional"]),
    ("Coordinación de Sede", "nivel micro", False,
     ["Requerimientos de las carreras e información local ordenada", "Equivalencia frente a las otras sedes", "Propone ajustes locales", "Seguimiento y monitoreo en la sede",
      "Eleva a las Áreas y a la Dirección"]),
]
x0, x1, wl = 0.6, 12.2, 1.95
wc = (x1 - x0 - wl - 0.06) / 5
for j, p in enumerate(pasos):
    forma(sl, MSO_SHAPE.RECTANGLE, x0 + wl + 0.06 + j * wc + 0.03, 1.5, wc - 0.06, 0.32, p, NAVY, BLANCO, 10, True)
hr = 1.02
for i, (n, det, osc, celdas) in enumerate(niveles):
    y = 1.9 + i * hr
    et = forma(sl, MSO_SHAPE.RECTANGLE, x0, y, wl, hr - 0.07, "", NAVY if osc else PALE)
    tf = et.text_frame
    tf.paragraphs[0].runs[0].text = n
    tf.paragraphs[0].runs[0].font.bold = True
    tf.paragraphs[0].runs[0].font.size = Pt(12)
    tf.paragraphs[0].runs[0].font.color.rgb = rgb(BLANCO if osc else NAVY)
    p = tf.add_paragraph()
    p.alignment = PP_ALIGN.CENTER
    r = p.add_run()
    r.text = det
    r.font.size, r.font.name = Pt(8.5), "Calibri"
    r.font.color.rgb = rgb("D6E2F2" if osc else GRIS)
    for j, c in enumerate(celdas):
        ult = j == 4
        forma(sl, MSO_SHAPE.ROUNDED_RECTANGLE, x0 + wl + 0.06 + j * wc + 0.03, y, wc - 0.06, hr - 0.07, c,
              (ORO_PALIDO if ult else ("E4ECF7" if osc else "F4F7FB")), NAVY, 9.5, bold=(osc and ult)).adjustments[0] = 0.1
# flecha ascendente
fl = sl.shapes.add_shape(MSO_SHAPE.UP_ARROW, Inches(12.3), Inches(1.9), Inches(0.42), Inches(4 * hr - 0.07))
fl.shadow.inherit = False
fl.fill.solid()
fl.fill.fore_color.rgb = rgb(GOLD)
fl.line.fill.background()
tb = texto(sl, 10.72, 3.72, 3.6, 0.3, "la información sube ordenada", 9, BLANCO, True, PP_ALIGN.CENTER)
tb.rotation = -90
forma(sl, MSO_SHAPE.ROUNDED_RECTANGLE, 0.6, 6.03, 12.12, 0.5, "Resultado: indicadores de competencias digitales en salud, con detalle por sede, para cada Vicerrectoría", NAVY, BLANCO, 11, True)
nota(sl, "Los cinco pasos son los mismos en cada nivel; cambia la escala. Las Áreas crecen porque levantan la necesidad antes de proponer la respuesta.", y=6.6)

# ---------------------------------------------------------------- Línea de investigación basal
sl = base("LÍNEA DE INVESTIGACIÓN BASAL", "Competencias digitales en salud: una línea que queda instalada")


def panel(sl, x, y, w, h, fill):
    p = sl.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(x), Inches(y), Inches(w), Inches(h))
    p.shadow.inherit = False
    p.fill.solid()
    p.fill.fore_color.rgb = rgb(fill)
    p.line.fill.background()
    p.adjustments[0] = 0.05
    return p


# 1. punto de partida
panel(sl, 0.6, 1.55, 3.0, 4.35, NAVY)
texto(sl, 0.8, 1.68, 2.6, 0.3, "PUNTO DE PARTIDA", 10, "D6E2F2", True)
texto(sl, 0.8, 1.98, 2.6, 0.62, "Revisión de la OMS, junio de 2026", 15, BLANCO, True, font="Cambria", anchor=MSO_ANCHOR.TOP)
for j, (n, t) in enumerate((("35", "marcos de competencias en salud digital revisados"), ("10", "grupos de competencias identificados"))):
    texto(sl, 0.8, 2.72 + j * 0.72, 0.85, 0.6, n, 28, "E3C98A", True, font="Cambria")
    texto(sl, 1.62, 2.72 + j * 0.72, 1.85, 0.6, t, 10, BLANCO)
texto(sl, 0.8, 4.22, 2.6, 0.26, "LO QUE DEJA ABIERTO", 9.5, "D6E2F2", True)
for j, t in enumerate(("Ningún marco nacional de América Latina", "Ningún grupo dedicado a inteligencia artificial", "Solo literatura en inglés, 2012 a 2022")):
    texto(sl, 0.8, 4.5 + j * 0.42, 2.6, 0.4, "· " + t, 10, BLANCO)

# 2. la línea, como ciclo
panel(sl, 3.78, 1.55, 5.5, 4.35, "E4ECF7")
texto(sl, 3.98, 1.68, 5.1, 0.3, "LA LÍNEA BASAL DEL DEPARTAMENTO", 10, BLUE, True)
texto(sl, 3.98, 1.98, 5.1, 0.4, "Un modelo de competencias, medido cada semestre", 15, NAVY, True, font="Cambria")
pasos4 = [("Adaptar", "el modelo al contexto chileno y a las carreras"), ("Medir", "en los estudiantes, cada semestre"),
          ("Analizar", "por sede, carrera y cohorte"), ("Ajustar", "la formación con evidencia")]
cx4 = [4.56, 5.87, 7.18, 8.49]
cajas4 = []
for j, (t, d) in enumerate(pasos4):
    b = forma(sl, MSO_SHAPE.ROUNDED_RECTANGLE, cx4[j] - 0.58, 2.85, 1.16, 0.55, t, NAVY, BLANCO, 12, True)
    forma(sl, MSO_SHAPE.OVAL, cx4[j] - 0.7, 2.72, 0.3, 0.3, str(j + 1), GOLD, BLANCO, 9, True)
    texto(sl, cx4[j] - 0.6, 3.48, 1.2, 0.75, d, 9.5, NAVY, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.TOP)
    cajas4.append(b)
for j in range(3):
    flecha(sl, cajas4[j], cajas4[j + 1], "der", "izq", recta=True, grosor=2)
c = sl.shapes.add_connector(MSO_CONNECTOR.STRAIGHT, Inches(8.49), Inches(2.6), Inches(4.75), Inches(2.6))
c.line.color.rgb = rgb(GOLD)
c.line.width = Pt(2)
ln = c.line._get_or_add_ln()
ln.append(etree.SubElement(ln, qn("a:tailEnd"), {"type": "triangle", "w": "med", "len": "med"}))
texto(sl, 5.3, 2.36, 2.5, 0.22, "y se vuelve a medir", 9, GOLD, True, PP_ALIGN.CENTER, italic=True)
forma(sl, MSO_SHAPE.ROUNDED_RECTANGLE, 3.98, 4.45, 5.1, 0.62, "Laboratorio: la asignatura Salud Digital, con 1.788 estudiantes de 4 carreras en 4 sedes", BLANCO, NAVY, 10.5, True, borde=NAVY)
forma(sl, MSO_SHAPE.ROUNDED_RECTANGLE, 3.98, 5.18, 5.1, 0.6, "Modelo propuesto: línea de investigación de Estefanía Fröhlich, con proyección doctoral", GOLD, BLANCO, 10.5, True)

# 3. por qué queda andando
panel(sl, 9.46, 1.55, 3.26, 4.35, ORO_PALIDO)
texto(sl, 9.66, 1.68, 2.9, 0.3, "QUEDA ANDANDO PORQUE", 10, GOLD, True)
texto(sl, 9.66, 1.98, 2.9, 0.85, "La línea es del Departamento; cada producto, de sus autores", 14, NAVY, True, font="Cambria", anchor=MSO_ANCHOR.TOP)
for j, t in enumerate(("La gestiona el Área de Proyectos", "Protocolo e instrumentos documentados", "Datos en un repositorio del Departamento", "Las sedes levantan la información", "Tesis de pregrado, postgrado y doctorado")):
    forma(sl, MSO_SHAPE.ROUNDED_RECTANGLE, 9.66, 2.95 + j * 0.57, 2.86, 0.47, t, BLANCO, NAVY, 10, borde=GOLD)

forma(sl, MSO_SHAPE.ROUNDED_RECTANGLE, 0.6, 6.03, 12.12, 0.5, "Productos: marco común de desempeños  ·  indicadores de competencias por sede  ·  tesis y publicaciones con afiliación al Departamento", NAVY, BLANCO, 11, True)
nota(sl, "Responde al artículo 3: un marco común de desempeños sustentado en la investigación del Departamento y en los estándares internacionales.", y=6.6)

# ---------------------------------------------------------------- Fichas: el Departamento por dentro
PORT = [l for l in prs.slide_layouts if l.name.strip() == "PORTADILLA"][0]


def portadilla(titulo, sub):
    sl = prs.slides.add_slide(PORT)
    sl.shapes.title.text_frame.text = titulo
    r = sl.shapes.title.text_frame.paragraphs[0].runs[0]
    r.font.name, r.font.bold = "Cambria", True
    r.font.color.rgb = rgb(NAVY)
    t = sl.shapes.title
    texto(sl, t.left / 914400, (t.top + t.height) / 914400 + 0.05, 8, 0.4, sub, 14, GRIS)
    return sl


def organigrama(sl, foco):
    """Organigrama pequeño; `foco` pinta en color la unidad que se explica."""
    def nodo(clave, cx, cy, w, h, t, size=10):
        on = clave == foco
        return forma(sl, MSO_SHAPE.ROUNDED_RECTANGLE, cx - w / 2, cy - h / 2, w, h, t, NAVY if on else "EEF1F5", BLANCO if on else GRIS, size, on,
                     borde=GOLD if on else None)

    def linea(x1, y1, x2, y2, punteada=False):
        c = sl.shapes.add_connector(MSO_CONNECTOR.STRAIGHT, Inches(x1), Inches(y1), Inches(x2), Inches(y2))
        c.line.color.rgb = rgb(LINEA)
        c.line.width = Pt(1.25)
        if punteada:
            ln = c.line._get_or_add_ln()
            etree.SubElement(ln, qn("a:prstDash"), {"val": "dash"})

    linea(2.75, 2.0, 2.75, 2.42)
    linea(2.75, 2.95, 2.75, 3.3)
    linea(1.75, 3.3, 3.95, 3.3)
    linea(1.75, 3.3, 1.75, 3.5)
    linea(3.95, 3.3, 3.95, 3.5)
    linea(2.75, 4.05, 2.75, 4.45)
    linea(1.15, 4.45, 4.75, 4.45)
    for x in (1.15, 2.35, 3.55, 4.75):
        linea(x, 4.45, x, 4.62)
    linea(3.7, 2.68, 4.1, 2.68, punteada=True)
    nodo("dec", 2.75, 1.8, 1.9, 0.42, "Decanato FCCS")
    nodo("dir", 2.75, 2.68, 1.9, 0.52, "Dirección Nacional", 11)
    nodo("com", 4.75, 2.68, 1.3, 0.52, "Comité Consultivo", 9.5)
    nodo("doc", 1.75, 3.78, 2.0, 0.56, "Área de Docencia", 11)
    nodo("ivp", 3.95, 3.78, 2.0, 0.56, "Área de Proyectos", 11)
    for x, n in ((1.15, "Santiago"), (2.35, "Concepción"), (3.55, "Valdivia"), (4.75, "Puerto Montt")):
        nodo("sedes", x, 4.88, 1.1, 0.5, n, 9)
    texto(sl, 0.6, 5.2, 4.8, 0.25, "Coordinaciones de Sede", 9, NAVY if foco == "sedes" else GRIS, foco == "sedes", PP_ALIGN.CENTER)
    forma(sl, MSO_SHAPE.ROUNDED_RECTANGLE, 0.6, 5.6, 4.8, 0.42, "Académicos adscritos y de otras unidades", "EEF1F5", GRIS, 9.5)


def ficha(foco, articulo, titulo, resumen, funciones, pie=None):
    sl = base("RESPALDO · " + articulo.upper(), titulo)
    organigrama(sl, foco)
    panel(sl, 5.8, 1.55, 6.92, 1.7, "E4ECF7")
    texto(sl, 6.05, 1.66, 6.4, 0.28, "EL DECRETO DICE", 10, BLUE, True)
    texto(sl, 6.05, 1.96, 6.4, 1.2, resumen, 12.5, NAVY, font="Cambria", anchor=MSO_ANCHOR.TOP)
    panel(sl, 5.8, 3.4, 6.92, 2.62, "F4F7FB")
    texto(sl, 6.05, 3.51, 6.4, 0.28, "FUNCIONES", 10, BLUE, True)
    for j, (a, b) in enumerate(funciones):
        y = 3.86 + j * (2.05 / len(funciones))
        forma(sl, MSO_SHAPE.OVAL, 6.05, y + 0.06, 0.16, 0.16, "", GOLD)
        tb = texto(sl, 6.32, y - 0.04, 6.2, 0.4, "", 11.5, NAVY)
        p = tb.text_frame.paragraphs[0]
        p.runs[0].text = a + (". " if b else "")
        p.runs[0].font.bold = True
        if b:
            r2 = p.add_run()
            r2.text = b
            r2.font.size, r2.font.name = Pt(11.5), "Calibri"
            r2.font.color.rgb = rgb(NAVY)
    if pie:
        nota(sl, pie, y=6.15)
    return sl


ficha("dir", "Artículo 8", "Dirección Nacional",
      "Un Director o Directora Nacional que, bajo la autoridad de la Decana, conduce el Departamento y ejecuta los acuerdos de la Facultad en las materias de su competencia.",
      [("Conduce", "Planifica y coordina todas las funciones y sedes; elabora el Plan de Desarrollo."),
       ("Articula personas", "Propone Jefaturas y Coordinaciones y acuerda horas con las unidades de origen."),
       ("Programa la docencia", "Planifica las asignaturas adscritas y propone programas."),
       ("Gestiona recursos y alianzas", "Identifica requerimientos y propone convenios."),
       ("Rinde cuenta", "Preside el Comité Consultivo y da cuenta anual a la Decana y al Consejo de Facultad.")])
ficha("com", "Artículo 9", "Comité Consultivo",
      "Asesora a la Dirección Nacional en la planificación y el seguimiento. Lo integran la Dirección, las Jefaturas de Área y los Coordinadores de Sede, y sesiona en forma ordinaria o ampliada.",
      [("Ordinario", "Seguimiento del quehacer del Departamento."),
       ("Ampliado con Escuelas", "Programación, equivalencia y perfiles de egreso."),
       ("Ampliado con Facultades", "Proyectos, programas y trabajo entre facultades."),
       ("Actas", "Se remiten a la Secretaría General.")])
ficha("doc", "Artículo 10", "Área de Docencia",
      "Seguimiento, análisis comparado y formulación de propuestas para robustecer, mejorar y actualizar la formación en salud digital de pregrado, postgrado y educación continua.",
      [("Benchmarking", "Compara la oferta con referentes nacionales e internacionales."),
       ("Creación", "Diseña y actualiza asignaturas y programas."),
       ("Calidad y trazabilidad", "Da seguimiento a la oferta formativa en todas las sedes."),
       ("Competencias y resultados de aprendizaje", "Cuida que tributen a los perfiles de egreso."),
       ("Eleva", "Consolida la información de las sedes y la entrega a la Dirección Nacional.")],
      pie="Trabaja en tres frentes: pregrado, postgrado y educación continua.")
ficha("ivp", "Artículo 10", "Área de Proyectos",
      "Gestiona la investigación, la vinculación con el medio y el desarrollo de proyectos del Departamento, en coordinación con las Vicerrectorías y unidades institucionales competentes.",
      [("Línea basal", "Sostiene la línea de competencias digitales en salud como base del Departamento."),
       ("Investigación", "Propone y organiza líneas; integra a estudiantes de pregrado y postgrado."),
       ("Vinculación con el medio", "Trabaja en conjunto con las unidades de la Universidad, la Facultad y las carreras."),
       ("Fondos y alianzas", "Promueve postulaciones con financiamiento interno y externo."),
       ("Eleva", "Entrega resultados y afiliación a la Dirección Nacional.")],
      pie="Trabaja en tres frentes: línea basal, investigación y vinculación con el medio.")
ficha("sedes", "Artículo 11", "Coordinaciones de Sede",
      "En cada sede, un Coordinador o Coordinadora que depende de la Dirección Nacional y sigue los lineamientos técnicos de las Áreas. Representa al Departamento y vela por la equivalencia de la formación entre sedes.",
      [("Representa", "Es la cara del Departamento en la sede."),
       ("Mide", "Seguimiento, monitoreo e indicadores locales."),
       ("Cuida la equivalencia", "Que la formación sea la misma en las cuatro sedes."),
       ("Levanta", "Los requerimientos de las carreras y los académicos que pueden sumarse."),
       ("Informa", "A las Áreas y a la Dirección, e integra el Comité Consultivo.")])

# ---------------------------------------------------------------- Artículos y organigrama
sl = base("EL DEPARTAMENTO POR DENTRO", "Cada artículo, en su lugar del organigrama")
filas_art = [("1 y 2", "Objetivo general y alcance nacional y transversal", "Todo el Departamento, en todas las sedes", "obj"),
             ("3 y 4", "Pregrado, postgrado y educación continua", "Área de Docencia", "obj"),
             ("5 y 6", "Investigación y vinculación con el medio", "Área de Proyectos", "obj"),
             ("7", "Integración y dependencia", "Decanato FCCS", "org"),
             ("8", "Dirección Nacional", "Dirección Nacional", "org"),
             ("9", "Comité Consultivo", "Comité Consultivo", "org"),
             ("10", "Las Áreas", "Área de Docencia y Área de Proyectos", "org"),
             ("11", "Coordinaciones de Sede", "Santiago, Concepción, Valdivia y Puerto Montt", "org"),
             ("12", "Designación", "Jefaturas de Área y Coordinaciones de Sede", "org"),
             ("13", "Integrantes", "Académicos adscritos y de otras unidades", "org")]
texto(sl, 0.6, 1.5, 1.2, 0.26, "ARTÍCULO", 10, BLUE, True)
texto(sl, 1.95, 1.5, 4.6, 0.26, "QUÉ ESTABLECE", 10, BLUE, True)
texto(sl, 7.55, 1.5, 5.1, 0.26, "DÓNDE ESTÁ EN EL ORGANIGRAMA", 10, BLUE, True)
hf = 0.418
for i, (num, que, donde, grupo) in enumerate(filas_art):
    y = 1.82 + i * hf
    obj = grupo == "obj"
    forma(sl, MSO_SHAPE.ROUNDED_RECTANGLE, 0.6, y, 1.2, hf - 0.07, num, GOLD if obj else NAVY, BLANCO, 11, True)
    forma(sl, MSO_SHAPE.ROUNDED_RECTANGLE, 1.95, y, 4.9, hf - 0.07, que, ORO_PALIDO if obj else "F4F7FB", NAVY, 11)
    c = sl.shapes.add_connector(MSO_CONNECTOR.STRAIGHT, Inches(6.9), Inches(y + (hf - 0.07) / 2), Inches(7.5), Inches(y + (hf - 0.07) / 2))
    c.line.color.rgb = rgb(NAVY)
    c.line.width = Pt(1.5)
    ln = c.line._get_or_add_ln()
    ln.append(etree.SubElement(ln, qn("a:tailEnd"), {"type": "triangle", "w": "med", "len": "med"}))
    forma(sl, MSO_SHAPE.ROUNDED_RECTANGLE, 7.55, y, 5.17, hf - 0.07, donde, "E4ECF7", NAVY, 11, True)
for j, (t, c_) in enumerate((("Objetivos: para qué existe", GOLD), ("Organización: cómo funciona", NAVY))):
    forma(sl, MSO_SHAPE.RECTANGLE, 0.6 + j * 2.6, 6.16, 0.22, 0.14, "", c_)
    texto(sl, 0.9 + j * 2.6, 6.1, 2.3, 0.26, t, 9.5, GRIS)
texto(sl, 6.2, 6.1, 6.52, 0.26, "Más tres artículos transitorios, que ordenan la instalación gradual.", 9.5, GRIS, italic=True, align=PP_ALIGN.RIGHT)

# ---------------------------------------------------------------- Orden: ciclo, cifras, macro-micro, línea basal · articulación · fichas
p_art = portadilla("Cómo se articula", "Tres maneras de mostrarlo")
p_dep = portadilla("El Departamento por dentro", "Estructura y relaciones")
p_res = portadilla("Respaldo", "Cada unidad: qué dice el decreto y qué hace")
ids = prs.slides._sldIdLst
CIERRE = [l for l in prs.slide_layouts if l.name.strip() == "CIERRE"][0]
prs.slides.add_slide(CIERRE)
el = list(ids)  # 0 portada, 1 organigrama, 2-4 swimlanes, 5 ciclo, 6 cifras, 7 macro-micro, 8 línea basal, 9-13 fichas, 14 artículos, 15-17 portadillas, 18 cierre
# organigrama, artículos y cierre; el respaldo queda detrás del cierre
orden = [el[0], el[5], el[6], el[7], el[8], el[15], el[2], el[3], el[4], el[16], el[1], el[14], el[18], el[17]] + el[9:14]
assert len(orden) == len(el)
for e in el:
    ids.remove(e)
for e in orden:
    ids.append(e)

prs.save(OUT)
print("ok", len(prs.slides))
