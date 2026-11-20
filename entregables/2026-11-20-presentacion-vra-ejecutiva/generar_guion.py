"""Guion ajustado a 2026_11_20_Propuesta_Departamento_Salud_Digital_USS.pptx. Uso: python3 generar_guion.py <salida.docx>"""
import sys
from docx import Document
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Cm, Pt, RGBColor

NAVY, BLUE, GRIS = RGBColor(0x14, 0x37, 0x5A), RGBColor(0x2F, 0x6D, 0xB5), RGBColor(0x5F, 0x64, 0x70)
d = Document()
s = d.sections[0]
s.page_width, s.page_height = Cm(21.59), Cm(27.94)
s.left_margin = s.right_margin = Cm(2.1)
s.top_margin = s.bottom_margin = Cm(1.8)
n = d.styles["Normal"]
n.font.name, n.font.size = "Calibri", Pt(11)
n.paragraph_format.space_after = Pt(5)
n.paragraph_format.line_spacing = 1.12


def par(t, negrita=False, color=None, tam=None, fuente=None, antes=0, despues=None, cursiva=False, sangria=0, junto=False):
    p = d.add_paragraph()
    p.paragraph_format.space_before = Pt(antes)
    p.paragraph_format.keep_with_next = junto
    if despues is not None: p.paragraph_format.space_after = Pt(despues)
    if sangria: p.paragraph_format.left_indent = Cm(sangria)
    r = p.add_run(t)
    r.bold, r.italic = negrita, cursiva
    if color: r.font.color.rgb = color
    if tam: r.font.size = Pt(tam)
    if fuente: r.font.name = fuente
    return p


def lamina(num, titulo, tiempo, decir, indicacion=None):
    p = par(f"{num} · {titulo}", True, NAVY, 12.5, "Cambria", antes=9, despues=2, junto=True)
    r = p.add_run(f"   {tiempo}")
    r.font.size, r.font.color.rgb, r.bold = Pt(9.5), GRIS, False
    for t in decir:
        par("«" + t + "»", sangria=0.4)
    if indicacion:
        par(indicacion, color=GRIS, tam=9.5, cursiva=True, sangria=0.4)


def tabla(enc, filas, anchos):
    t = d.add_table(rows=1, cols=len(enc))
    t.style = "Table Grid"
    t.autofit = False
    for i, e in enumerate(enc):
        c = t.rows[0].cells[i]
        c.text = ""
        r = c.paragraphs[0].add_run(e)
        r.bold, r.font.size, r.font.color.rgb = True, Pt(9.5), RGBColor(255, 255, 255)
        sh = OxmlElement("w:shd")
        sh.set(qn("w:val"), "clear"); sh.set(qn("w:color"), "auto"); sh.set(qn("w:fill"), "14375A")
        c._tc.get_or_add_tcPr().append(sh)
    for f in filas:
        cs = t.add_row().cells
        for i, v in enumerate(f):
            cs[i].text = ""
            r = cs[i].paragraphs[0].add_run(v)
            r.font.size, r.bold = Pt(9.5), i == 0
            cs[i].paragraphs[0].paragraph_format.space_after = Pt(2)
    for i, a in enumerate(anchos):
        t.columns[i].width = Cm(a)
        for fila in t.rows:
            fila.cells[i].width = Cm(a)


par("GUION", True, BLUE, 9.5, despues=0)
par("Reunión con el Vicerrector Académico", True, NAVY, 19, "Cambria", despues=0)
par("20 de noviembre de 2026 · 2026_11_20_Propuesta_Departamento_Salud_Digital_USS.pptx · unos 5 minutos de exposición; el resto, conversación.", color=GRIS, tam=9.5, despues=3)
par("Lo que va entre «comillas» es para decirlo; lo gris son indicaciones para ti. Las láminas 1 a 8 son la exposición; de la 9 a la 20, el anexo.", color=GRIS, tam=9.5)

lamina(1, "Portada", "15 s", [
    "Vicerrector, gracias por el tiempo. Le traigo la propuesta de creación del Departamento Nacional de Salud Digital. Le muestro primero qué oportunidades abre para la Universidad y después cómo se organiza. Son cinco minutos, y lo que más me interesa es su mirada.",
])
lamina(2, "La Salud Digital como oportunidad en la USS", "1 min · la lámina más importante", [
    "Esta es la propuesta en una lámina. Son cinco oportunidades, y cada una aporta a un objetivo del Plan de Desarrollo Institucional.",
    "Posicionamiento, con un modelo de competencias en salud digital que incorpora inteligencia artificial. Empleabilidad, con egresados que tienen los desempeños digitales que pide el sistema de salud. Nueva oferta de postgrado y educación continua. Universidad digital, con formación equivalente en las cuatro sedes. E investigación, con una línea basal y publicaciones con afiliación USS.",
], "Nómbralas sin leer la tabla y detente en la que le genere preguntas.")
lamina(3, "Digitalización de la salud y demanda de profesionales", "45 s", [
    "El contexto son tres datos. Tres leyes, de telemedicina, de interoperabilidad de fichas clínicas y de protección de datos personales, ya exigen profesionales formados en salud digital.",
    "La OPS estima que en las Américas podrían faltar entre 600 mil y 2 millones de trabajadores de salud a 2030.",
    "Y la OMS revisó 35 marcos de competencias en salud digital: ninguno de sus grupos de competencias está dedicado a inteligencia artificial, y ningún marco nacional es de América Latina. En Chile existe el modelo de CENS, que es nuestra referencia local.",
    "La demanda la exige la ley y la confirma el déficit de profesionales.",
], "La lámina dice «0 de 35 incluyen IA» y «el único marco nacional de América Latina». Di la versión de arriba, que es la que respalda la fuente.")
lamina(4, "La USS tiene la base para impulsar la iniciativa", "45 s", [
    "No partimos de cero. Hoy 1.788 estudiantes cursan Salud Digital, en 31 secciones, cuatro carreras y cuatro sedes.",
    "La Facultad ya lo había identificado: su plan de desarrollo pone la salud digital a nivel nacional entre sus oportunidades.",
    "Lo que falta es medir. La Universidad mide empleabilidad, pero no en salud digital. El Departamento ordena esta base y permite medirla.",
])
lamina(5, "Track de Salud Digital", "40 s", [
    "Así trabajamos. Partimos de las necesidades del sistema de salud en desempeños digitales y hacemos una lectura del mundo laboral.",
    "Con eso, en paralelo, identificamos áreas de desarrollo académico e investigación y comparamos con marcos y programas del mundo.",
    "De ahí salen las propuestas de implementación: hoy son la actualización de la asignatura, un electivo de salud con ingeniería y un diplomado. Eso llega a los estudiantes como competencias en términos laborales, con formación equivalente en las cuatro sedes, y vuelve al mundo laboral como empleabilidad.",
], "Recorre la figura de izquierda a derecha con la mano. La flecha dorada muestra que el ciclo vuelve a empezar.")
lamina(6, "Un modelo de competencias medido", "40 s", [
    "Esta es la línea de investigación basal del Departamento. El punto de partida es la revisión de la OMS de junio de 2026: 35 marcos y 10 grupos de competencias.",
    "La línea adapta el modelo al contexto chileno y a las carreras, lo mide en los estudiantes, lo analiza por sede, carrera y cohorte, y ajusta la formación con esa evidencia. El laboratorio es la asignatura Salud Digital.",
    "Y queda instalada: la línea es del Departamento, la gestiona la Dirección de Investigación, y deja un marco común de desempeños, indicadores por sede, tesis y publicaciones.",
], "La lámina dice «cada semestre» en dos lugares. Si no quieres comprometer la frecuencia, di «periódicamente».")
lamina(7, "Estructura sobre capacidades que ya existen", "30 s", [
    "La estructura tiene tres niveles. Una Dirección Nacional, que depende del Decanato y cuenta con un Comité Consultivo.",
    "Dos Direcciones de área, la de Docencia y la de Investigación, articuladas entre sí.",
    "Y una Dirección de Sede en Santiago, Concepción, Valdivia y Puerto Montt, que recibe los lineamientos técnicos de ambas. Trabajan académicos adscritos y de otras unidades, por acuerdo con su unidad de origen. La instalación es gradual.",
], "Los recuadros del dibujo dicen «Área de Docencia» y «Área de Investigación». Tú di «Dirección», como el rótulo de la izquierda y como el decreto.")
lamina(8, "La salud digital ya está implementada y falta mejorar las competencias", "40 s y conversación", [
    "En resumen: la salud digital ya está en la formación de la USS, y la propuesta es ordenarla, medirla y hacerla crecer.",
    "La ruta del decreto sigue el precedente del Departamento Nacional de Salud Pública: propuesta de la Decana y acuerdo del Consejo de Facultad, Consejo Superior, Junta Directiva y decreto de Rectoría.",
    "Y la pregunta con la que quiero cerrar: ¿qué espera la Vicerrectoría Académica de la salud digital en la USS?",
], "Después, escucha y anota. No llenes el silencio.")

par("Si el tiempo se acorta: láminas 2 y 8. Para saltar a una lámina durante la presentación, escribe su número y presiona Enter.", color=GRIS, tam=9.5, cursiva=True, antes=6)

par("Vocabulario", True, BLUE, 10.5, antes=8, despues=2, junto=True)
par("Dirección Nacional; Dirección de Docencia y Dirección de Investigación, que son las Direcciones de área; Direcciones de Sede; Comité Consultivo, ordinario o ampliado. El decreto v0.7 usa estas mismas palabras.", tam=10)

par("Si pregunta…", True, BLUE, 10.5, antes=8, despues=3, junto=True)
tabla(["Pregunta", "Respuesta corta", "Lámina"], [
    ("¿Somos los primeros?", "La OMS no identificó ningún grupo de competencias dedicado a IA ni ningún marco nacional de América Latina. El modelo de CENS es de 2024 y quedó fuera de esa revisión. La USS tiene la base para llenar ese vacío.", "6 y 10"),
    ("¿Y en Chile?", "CENS estimó en 2019 un déficit de al menos 3.500 profesionales para la transformación digital de la salud.", "10"),
    ("¿Y el mundo laboral en general?", "El Foro Económico Mundial proyecta 170 millones de empleos nuevos a 2030 y que cambiará cerca del 40 % de las habilidades clave.", "10"),
    ("¿Qué gana la Vicerrectoría Académica?", "Oferta equivalente entre sedes e indicadores de docencia en salud digital, con detalle por sede.", "13"),
    ("¿Cómo se relaciona con la VRID y con VcM?", "Articula con ellas, sin perjuicio de sus atribuciones: líneas, proyectos y publicaciones con afiliación para la VRID, y aporte especializado a las iniciativas de vinculación.", "13"),
    ("¿Cómo se mide?", "Con indicadores de competencias digitales en salud por sede, carrera y cohorte. Se definen con el Plan de Desarrollo del Departamento, una vez aprobado el decreto.", "6 y 14"),
    ("¿Qué recursos pide?", "El decreto no pide contrataciones. La docencia se hace con horas de académicos, acordadas con su unidad de origen; el presupuesto es de la Facultad, y las Direcciones se instalan gradualmente.", "16"),
    ("¿Siete Direcciones no es mucho?", "Es la estructura completa; se instala de forma gradual, según las necesidades y la disponibilidad de la Facultad. Mientras no se designen las Direcciones de área, sus funciones las ejerce la Dirección Nacional.", "15"),
    ("¿Por qué un Departamento?", "Porque el Reglamento de Unidades Académicas define al Departamento como la unidad transversal a carreras de distintas Facultades, y eso permite conducir la salud digital en las cuatro sedes.", "11 y 15"),
    ("¿Qué es la salud digital?", "El campo de conocimiento y práctica relativo al desarrollo y uso de tecnologías digitales para mejorar la salud de las personas y las poblaciones (artículo 1).", "11"),
    ("¿En qué va el decreto?", "Se presentó al Consejo de Facultad el 12 de noviembre y se ha ajustado con las observaciones de la Decana.", "8"),
    ("¿Qué necesita de la Vicerrectoría?", "Su mirada sobre el texto antes de que siga a las instancias, y sumar las competencias digitales al seguimiento de egresados.", "8 y 10"),
], [4.2, 11.3, 1.9])

par("Tres cuidados", True, BLUE, 10.5, antes=10, despues=2, junto=True)
for t in ["Si te piden la presentación, envía un PDF, no el PowerPoint: el archivo lleva notas con respuestas preparadas y comentarios de revisión.",
          "Sobre ingresos de la nueva oferta, no afirmes nada que no esté confirmado con la Decana.",
          "El doctorado y la autoría de la línea no van hoy: primero el decreto."]:
    par("•  " + t, tam=10, sangria=0.3, despues=2)
d.save(sys.argv[1])
