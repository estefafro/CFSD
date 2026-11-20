"""Genera la guía para la reunión con el Vicerrector Académico. Uso: python3 generar_guia.py <salida.docx>"""
import sys
from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Cm, Pt, RGBColor

NAVY, BLUE, GRIS = RGBColor(0x14, 0x37, 0x5A), RGBColor(0x2F, 0x6D, 0xB5), RGBColor(0x5F, 0x64, 0x70)
d = Document()
s = d.sections[0]
s.page_width, s.page_height = Cm(21.59), Cm(27.94)
s.left_margin = s.right_margin = Cm(2.0)
s.top_margin = s.bottom_margin = Cm(1.8)
n = d.styles["Normal"]
n.font.name, n.font.size = "Calibri", Pt(10.5)
n.paragraph_format.space_after = Pt(5)


def par(texto, negrita=False, color=None, tam=None, fuente=None, antes=0, despues=None, cursiva=False):
    p = d.add_paragraph()
    p.paragraph_format.space_before = Pt(antes)
    if despues is not None:
        p.paragraph_format.space_after = Pt(despues)
    r = p.add_run(texto)
    r.bold, r.italic = negrita, cursiva
    if color: r.font.color.rgb = color
    if tam: r.font.size = Pt(tam)
    if fuente: r.font.name = fuente
    return p


def h1(t):
    p = par(t, True, NAVY, 15, "Cambria", antes=14, despues=4)
    p.paragraph_format.keep_with_next = True


def h2(t):
    p = par(t.upper(), True, BLUE, 9.5, antes=8, despues=3)
    p.paragraph_format.keep_with_next = True


def vin(negrita, resto=""):
    p = d.add_paragraph()
    p.paragraph_format.left_indent = Cm(0.5)
    p.paragraph_format.first_line_indent = Cm(-0.35)
    p.paragraph_format.space_after = Pt(3)
    p.add_run("•  ")
    p.add_run(negrita).bold = True
    p.add_run(resto)


def frase(t):
    p = d.add_paragraph()
    p.paragraph_format.left_indent = Cm(0.8)
    p.paragraph_format.space_after = Pt(4)
    r = p.add_run("«" + t + "»")
    r.italic = True
    r.font.color.rgb = NAVY


def tabla(encabezados, filas, anchos):
    t = d.add_table(rows=1, cols=len(encabezados))
    t.style = "Table Grid"
    t.autofit = False
    for i, e in enumerate(encabezados):
        c = t.rows[0].cells[i]
        c.text = ""
        r = c.paragraphs[0].add_run(e)
        r.bold = True
        r.font.size = Pt(9.5)
        r.font.color.rgb = RGBColor(255, 255, 255)
        sh = OxmlElement("w:shd")
        sh.set(qn("w:val"), "clear"); sh.set(qn("w:color"), "auto"); sh.set(qn("w:fill"), "14375A")
        c._tc.get_or_add_tcPr().append(sh)
    for f in filas:
        cs = t.add_row().cells
        for i, v in enumerate(f):
            cs[i].text = ""
            r = cs[i].paragraphs[0].add_run(v)
            r.font.size = Pt(9.5)
            r.bold = i == 0
            cs[i].paragraphs[0].paragraph_format.space_after = Pt(2)
    for i, a in enumerate(anchos):
        t.columns[i].width = Cm(a)
    for fila in t.rows:
        for i, a in enumerate(anchos):
            fila.cells[i].width = Cm(a)
    d.add_paragraph().paragraph_format.space_after = Pt(2)


par("GUÍA DE CONVERSACIÓN", True, BLUE, 9.5, despues=0)
par("Reunión con el Vicerrector Académico", True, NAVY, 20, "Cambria", despues=0)
par("Departamento Nacional de Salud Digital · documento de uso personal", color=GRIS, tam=10, despues=6)
par("La reunión tiene un solo propósito: que el Vicerrector conozca el borrador del decreto y aporte su experiencia institucional antes de ajustarlo y presentarlo. Esta guía ordena qué llevas resuelto, qué necesitas cerrar antes con la Decana y cómo pedirle a él lo que solo él puede dar. Las frases son propuestas: ajústalas a tu voz.")

# ───────── 1
h1("1. Lo que ya decidí y cómo lo cuento")
par("Lo decidido se afirma, no se consulta. La regla: si ya está en una lámina, no lo expliques de nuevo; si no está, una frase basta.")
tabla(["Decisión", "Dónde va", "Cómo lo digo"], [
    ("Dos Áreas con subáreas: Docencia (pregrado, postgrado, educación continua) y Proyectos (línea basal, investigación, vinculación con el medio)",
     "Lámina del organigrama y lámina de artículos",
     "«Son dos Áreas porque son dos maneras de trabajar: una mejora la formación, la otra gestiona líneas y proyectos.»"),
    ("El mismo modelo de trabajo en la sede, en las Áreas y hacia las Vicerrectorías",
     "Lámina «El mismo modelo, de la sede a las Vicerrectorías»",
     "«Lo que hace una sede en chico es lo que el Departamento entrega en grande: levantar, comparar, proponer, cuidar la calidad y medir.»"),
    ("Es escalable: se instala de forma gradual y crece según la necesidad",
     "Narrado, sin lámina nueva. Se apoya en el transitorio tercero y en el pie de la lámina de artículos",
     "«No parte completo. Parte con lo que ya existe y crece a medida que el propio Departamento levanta la necesidad y propone cómo responderla.»"),
    ("El decreto no fija plazos ni fechas",
     "No se menciona. Solo si pregunta",
     "«El decreto marca la cancha; los tiempos van en el plan de implementación, que se puede ajustar sin tocar el decreto.»"),
    ("El análisis comparado es función del Área de Docencia, con la información ordenada desde las sedes",
     "Lámina del modelo y ficha de respaldo del Área de Docencia",
     "No requiere frase: está en la lámina."),
    ("La línea basal es competencias digitales en salud, a partir de la revisión de la OMS de junio de 2026, y queda instalada en el Departamento",
     "Lámina «Competencias digitales en salud: una línea que queda instalada»",
     "«La línea es del Departamento y sigue funcionando esté quien esté. Eso es lo que la hace institucional.»"),
    ("El modelo de competencias es mi línea de investigación, con proyección doctoral",
     "Franja dorada de esa lámina, más una frase dicha por mí",
     "«El modelo que proponemos usar es mi línea de investigación y quiero desarrollarla como doctorado. La línea queda en el Departamento; la tesis y los artículos, con sus autores.»"),
    ("El modelo complementa al de CENS; CENS se cita y se estudian otros marcos",
     "Solo si pregunta",
     "«No compite con CENS: lo cita y lo complementa.»"),
    ("Ciclo de formación y empleabilidad, con tres oportunidades en curso: actualización de la asignatura, electivo de salud con ingeniería y diplomado en desarrollo",
     "Lámina del ciclo",
     "«Esto ya está andando. El Departamento le da un lugar.»"),
    ("La empleabilidad en salud digital aparece como «por medir»",
     "Lámina de cifras",
     "«La Universidad mide empleabilidad, pero no en salud digital. Es la pregunta que queremos poder responder.»"),
    ("El detalle de cada unidad queda en respaldo",
     "Fichas al final; se abren solo si pregunta por una unidad",
     "«Tengo el detalle de cada unidad si quiere verlo.»"),
], [5.2, 4.6, 7.8])

h2("Sobre «escalable»: por qué narrarlo y no hacer una lámina")
par("Una lámina de escalamiento obliga a dibujar etapas, y las etapas invitan a la pregunta «¿en cuánto tiempo?», que es justo la que decidiste no responder en el decreto. Dicho en una frase al llegar a la lámina de artículos, queda como una cualidad del diseño y no como un compromiso. Si el Vicerrector pide verlo, la lámina del modelo ya lo muestra: el mismo modelo funciona con una sede o con cuatro.")

# ───────── 2
h1("2. Lo que tiene que decidir la Decana")
par("Conviene llegar donde el Vicerrector con esto cerrado, o al menos sabiendo qué se deja abierto a propósito.")
h2("Sobre la presentación")
vin("Cuál de las tres opciones de articulación se muestra. ", "Hoy van las tres (ciclo anual, tres productos, qué aporta y qué recibe cada actor). Ante el Vicerrector es mejor una; las otras dos pasan a respaldo.")
vin("Si se menciona el centro de costos. ", "Hoy aparece como «en evaluación» en la fila del Área de Proyectos.")
vin("Quién abre y quién pide. ", "Si la Decana asiste, qué parte presenta ella y cuál tú.")
h2("Sobre el decreto")
vin("Qué instancias deben pronunciarse y en qué orden. ", "Es la pregunta que tú misma dejaste para ella.")
vin("Los vistos que se quitaron. ", "La propuesta de la Decana y el acuerdo del Consejo de Facultad salieron de la versión 0.4 por no tener respaldo documental. Ella decide si vuelven y con qué documento.")
vin("Transitorio primero. ", "Desde cuándo se cuenta el período de la Dirección. La versión 0.4 dice «a contar de la fecha del presente decreto».")
vin("Artículo 4.º ", "Hasta dónde sostener «considerarán preferentemente al Departamento» si el Vicerrector lo objeta, y qué redacción alternativa sería aceptable para la Facultad.")
vin("Subáreas en el artículo 10.º ", "Si se nombran en el decreto o solo en la presentación.")
h2("Sobre lo conversado en el Consejo de Facultad")
vin("Qué se puede decir ante el Vicerrector ", "de dotación, responsables, horas y perfil de las Coordinaciones de Sede, y qué se reserva.")
vin("El doctorado. ", "Ya lo declaraste en el Consejo. Confirmar que ella respalda que lo plantees en esta reunión como línea propia.")

# ───────── 3
h1("3. Cómo le explico las necesidades y le pido su experiencia")
h2("El encuadre")
par("No vas a pedir recursos ni aprobación. Vas a mostrar una necesidad institucional y a pedirle criterio. Eso lo pone en el lugar de quien mejora la propuesta, no de quien la autoriza o la frena.")
h2("Las necesidades, en tres frases")
vin("La de la Universidad. ", "Las leyes de telemedicina, interoperabilidad y datos personales ya exigen profesionales formados en salud digital, y la autoevaluación 2026 lo recoge como oportunidad de mejora.")
vin("La de la formación. ", "Hay 1.788 estudiantes en Salud Digital en cuatro sedes, y hoy no hay una unidad que asegure que aprenden lo mismo en todas ni que mida qué competencias logran.")
vin("La de la gestión. ", "Los requerimientos de electivos, clases y programas llegan a una persona. El Departamento convierte esa respuesta en capacidad institucional.")
h2("Cómo abrir (de la versión más sobria a la más decidida)")
frase("Vicerrector, le traigo el borrador del decreto antes de cerrarlo. Quiero su mirada institucional sobre el texto.")
frase("Tenemos un borrador que ya pasó por el Consejo de Facultad. Antes de seguir, necesito que lo mire alguien que conoce cómo funcionan estas unidades en la Universidad: usted.")
frase("Este Departamento va a funcionar bien o mal según cómo calce con lo que la Vicerrectoría ya hace. Por eso vengo antes de cerrarlo y no después.")
h2("Lo que le pido, concretamente")
par("Cinco preguntas que solo él puede responder. Elige tres para la reunión; las otras quedan por si la conversación se abre.")
tabla(["Pregunta", "Por qué a él"], [
    ("«¿Cómo debería entrar el marco de desempeños a los perfiles de egreso sin interferir con los procesos curriculares de las carreras?»",
     "Artículo 3.º. Los procesos de diseño y actualización curricular son de su Vicerrectoría."),
    ("«El artículo 4.º dice que las unidades considerarán preferentemente al Departamento. ¿Cómo lo redactaría usted para que funcione con las otras Facultades?»",
     "Es la única frase que obliga a terceros. Preguntarla tú primero la convierte en un aporte suyo y no en una objeción."),
    ("«¿Qué aprendió la Universidad con el Departamento Nacional de Salud Pública que deberíamos considerar?»",
     "Es el precedente que cita el decreto. Le da espacio para hablar desde su experiencia."),
    ("«De la información por sede que podemos levantar, ¿cuál le sirve a la Vicerrectoría Académica?»",
     "Convierte los indicadores del Departamento en algo que él recibe."),
    ("«¿Qué le falta a este texto para llegar bien a las instancias que siguen?»",
     "Pregunta de cierre. Su respuesta es, en la práctica, la lista de ajustes."),
], [9.6, 8.0])
h2("Cómo cerrar")
frase("Con lo que me ha dicho ajusto el texto y se lo hago llegar antes de presentarlo. ¿Le parece?")
par("Ese cierre deja acordado un segundo contacto y lo deja a él como parte de la versión final.")
h2("Lo que puede preguntar y una respuesta breve")
tabla(["Si pregunta…", "Respondo…"], [
    ("¿Por qué un Departamento y no un centro o un programa?",
     "«Porque el Reglamento de Unidades Académicas define al Departamento como la unidad transversal a carreras de distintas Facultades, y eso es lo que hacemos.»"),
    ("¿Cuánto cuesta?",
     "«El decreto no pide contrataciones. La dotación se conversó en el Consejo de Facultad y la instalación es gradual.»"),
    ("¿En cuánto tiempo?",
     "«El decreto no fija plazos a propósito: los tiempos van en el plan de implementación que presento a la Decana.»"),
    ("¿No duplica lo que hacen Investigación o Vinculación con el Medio?",
     "«No crea unidades nuevas: trabaja con las que existen, sin perjuicio de sus atribuciones. Lo dicen los artículos 6.º y 10.º.»"),
    ("¿Qué pasa con la línea si usted no está?",
     "«Queda andando. Los protocolos, los instrumentos y la gestión son del Área de Proyectos, no míos.»"),
    ("¿El doctorado es compatible con dirigir el Departamento?",
     "«Mi contrato contempla horas de dirección, investigación y academia, y la tesis trabaja sobre lo mismo que el Departamento necesita medir.»"),
    ("¿Usa datos de estudiantes?",
     "«No uso datos sensibles. Los protocolos de la etapa de investigación se ven con el doctorado.»"),
], [6.2, 11.4])
h2("Lo que no conviene decir")
vin("Plazos o años. ", "Ni siquiera aproximados.")
vin("Jerga de gestión de proyectos ", "que él no usa.")
vin("Que el Comité Consultivo decide. ", "Asesora; decide la Decana.")
vin("Peticiones de recursos. ", "Esa conversación ya tiene su instancia.")
d.save(sys.argv[1])
