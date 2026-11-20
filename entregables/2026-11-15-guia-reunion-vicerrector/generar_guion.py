"""Guion de la presentación al Vicerrector, en el orden real de las láminas. Uso: python3 generar_guion.py <salida.docx>"""
import sys
from docx import Document
from docx.shared import Cm, Pt, RGBColor

NAVY, BLUE, GRIS, GOLD = RGBColor(0x14, 0x37, 0x5A), RGBColor(0x2F, 0x6D, 0xB5), RGBColor(0x5F, 0x64, 0x70), RGBColor(0xA8, 0x84, 0x3A)
d = Document()
s = d.sections[0]
s.page_width, s.page_height = Cm(21.59), Cm(27.94)
s.left_margin = s.right_margin = Cm(2.2)
s.top_margin = s.bottom_margin = Cm(1.9)
n = d.styles["Normal"]
n.font.name, n.font.size = "Calibri", Pt(11.5)
n.paragraph_format.space_after = Pt(6)
n.paragraph_format.line_spacing = 1.15


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


def bloque(t):
    par(t.upper(), True, GOLD, 10, antes=16, despues=2, junto=True)


def lamina(num, titulo, parrafos, nota=None):
    par(f"LÁMINA {num}", True, BLUE, 9, antes=10, despues=0, junto=True)
    par(titulo, True, NAVY, 13, "Cambria", despues=3, junto=True)
    for t in parrafos:
        par(t)
    if nota:
        par(nota, color=GRIS, tam=9.5, cursiva=True, sangria=0.5)


par("GUION", True, BLUE, 9.5, despues=0)
par("Presentación al Vicerrector Académico", True, NAVY, 20, "Cambria", despues=0)
par("Departamento Nacional de Salud Digital · en el orden real de las 19 láminas", color=GRIS, tam=10, despues=4)
par("El texto en negro es lo que dices. Las notas en gris son para ti. Las láminas 1 a 13 son la presentación; de la 14 a la 19 son respaldo y solo se abren si el Vicerrector pregunta por una unidad.", color=GRIS, tam=10)

bloque("Apertura")
lamina(1, "Departamento Nacional de Salud Digital", [
    "Vicerrector, gracias por el espacio. Le traigo el borrador del decreto que crea el Departamento Nacional de Salud Digital antes de cerrarlo, porque quiero su mirada institucional sobre el texto.",
    "Le voy a mostrar tres cosas: para qué existe el Departamento, cómo trabaja y cómo se organiza. Y al final le voy a pedir su opinión sobre algunos puntos concretos.",
])

bloque("Para qué existe")
lamina(2, "Del mundo laboral a la sala de clases, y de vuelta", [
    "Parto por el sentido. El sistema de salud se está digitalizando y le falta personal preparado. Esa necesidad es la que el Departamento lee, y la convierte en formación.",
    "El recorrido es este: leemos el mundo laboral, seleccionamos oportunidades, comparamos con lo que existe en el mundo, proponemos cómo implementarlo, y eso llega a los estudiantes como competencias. Con esas competencias egresan y vuelven al sistema de salud, que cambia y vuelve a pedir.",
    "Esto ya está andando. Hoy tenemos tres oportunidades en curso: la actualización de la asignatura de Salud Digital, un electivo de salud con ingeniería y un diplomado en desarrollo.",
    "Y cada paso tiene dueño: el Área de Docencia hace el seguimiento y las propuestas, el Comité Consultivo asesora y la Decana prioriza y decide.",
], "Si quieres un ejemplo concreto de competencia, este es el lugar: una derivación entre profesionales, qué información falta, qué se registra y qué se comunica.")
lamina(3, "Las cifras detrás del ciclo", [
    "Algunas cifras para dimensionarlo. En el mundo se proyectan 170 millones de empleos nuevos a 2030. En las Américas, la OPS estima que podrían faltar entre 600 mil y 2 millones de trabajadores de salud. Y en Chile, CENS estimó en 2019 un déficit de al menos 3.500 profesionales para la transformación digital de la salud.",
    "La OMS revisó 35 marcos de competencias en salud digital, y ninguno de los marcos nacionales es de América Latina. Ahí hay un espacio.",
    "Nosotros partimos con algo concreto: 1.788 estudiantes cursando Salud Digital en las cuatro sedes.",
    "Y hay una cifra que no tenemos. La Universidad mide empleabilidad, pero no en salud digital. Es la pregunta que queremos poder responder.",
], "La cifra de CENS es de 2019: dilo así, con el año.")

bloque("Cómo trabaja")
lamina(4, "El mismo modelo, de la sede a las Vicerrectorías", [
    "Así trabajamos. Son cinco pasos: levantar y ordenar, comparar, crear y proponer, cuidar la calidad y la trazabilidad, y medir y elevar.",
    "Lo importante es que el modelo es el mismo en todos los niveles. La Coordinación de Sede levanta la información local y la entrega ordenada. Las Áreas la consolidan y la trabajan. Y la Dirección Nacional la eleva.",
    "El resultado es que cada Vicerrectoría recibe indicadores de competencias digitales en salud, con detalle por sede.",
    "Y como el modelo es el mismo en chico y en grande, el Departamento no parte completo: parte con lo que ya existe y crece a medida que levanta la necesidad y propone cómo responderla.",
], "Aquí va «escalable», narrado. No menciones plazos.")
lamina(5, "Competencias digitales en salud: una línea que queda instalada", [
    "Para que ese modelo se sostenga en evidencia, el Departamento necesita una línea de investigación basal. Proponemos que sea competencias digitales en salud, a partir de la revisión que la OMS publicó en junio de 2026.",
    "La línea funciona como un ciclo: adaptar un modelo de competencias, medir, analizar y ajustar la formación. Y el laboratorio ya existe: es el curso de Salud Digital, con sus 1.788 estudiantes.",
    "Aquí quiero decirle algo en primera persona. El modelo que proponemos usar es mi línea de investigación, y quiero desarrollarla como doctorado.",
    "Lo diseñé para que las dos cosas convivan: la línea es del Departamento, la gestiona el Área de Proyectos y sigue funcionando esté quien esté. La tesis y los artículos son de sus autores, con afiliación al Departamento.",
], "Haz una pausa después de «como doctorado». Si pregunta por CENS: «no compite, lo cita y lo complementa».")

bloque("Cómo se articula")
lamina(6, "Cómo se articula (portadilla)", [
    "Ahora, cómo se relaciona el Departamento con el resto de la Universidad.",
], "Hoy hay tres maneras de mostrarlo. Si la Decana elige una, di solo esa y pasa las otras a respaldo.")
lamina(7, "Opción 1. El ciclo anual del Departamento, de punta a punta", [
    "Esta lámina muestra un año del Departamento en un solo recorrido: en qué momento interviene cada actor y qué decide.",
    "Las sedes y las carreras levantan requerimientos, el Departamento los ordena y propone, la Decana decide, las Vicerrectorías validan lo que corresponde a cada una, y lo que se ejecuta vuelve como indicadores.",
])
lamina(8, "Opción 2. Tres productos, un mismo camino por el Departamento", [
    "Aquí se ve lo mismo desde los productos. Una necesidad formativa de una carrera, una necesidad del territorio o el interés de académicos de otra disciplina entran al Departamento por caminos distintos, pero recorren el mismo trayecto.",
    "El Área que corresponde lo trabaja, la Decana decide, la Vicerrectoría competente lo valida, y sale un producto: una asignatura o programa, un proyecto de investigación, o una iniciativa de vinculación.",
])
lamina(9, "Opción 3. Qué aporta cada actor y qué recibe del Departamento", [
    "Y esta es la versión más directa: qué pone cada uno y qué recibe.",
    "En el caso de la Vicerrectoría Académica: aporta la política y la normativa académica, y recibe una oferta equivalente entre sedes e indicadores de docencia.",
], "Esta es la que más le habla a él. Detente en su fila.")

bloque("Cómo se organiza")
lamina(10, "El Departamento por dentro (portadilla)", [
    "Con eso claro, le muestro la estructura.",
])
lamina(11, "Organigrama: una estructura matricial", [
    "El Departamento depende de la Facultad y actúa bajo la autoridad de la Decana. Lo conduce una Dirección Nacional, asesorada por un Comité Consultivo.",
    "Tiene dos Áreas, porque son dos maneras de trabajar. El Área de Docencia cubre pregrado, postgrado y educación continua. El Área de Proyectos cubre la línea basal, la investigación y la vinculación con el medio.",
    "Y tiene una Coordinación en cada sede. Es matricial: las Coordinaciones dependen de la Dirección Nacional y siguen los lineamientos técnicos de las Áreas.",
    "Un punto importante: las Áreas y las Coordinaciones son instancias internas de gestión. El decreto no crea unidades académicas ni autoridades nuevas.",
])
lamina(12, "Cada artículo, en su lugar del organigrama", [
    "Y así calza el decreto con esa estructura. Son 13 artículos. Los seis primeros son los objetivos: qué hace el Departamento en pregrado, postgrado, investigación y vinculación. Los siete siguientes son la organización: cada uno corresponde a una parte del organigrama que acaba de ver.",
    "Los tres artículos transitorios establecen que la instalación es gradual.",
    "Hay un artículo sobre el que quiero su opinión especialmente: el cuarto, que dice que las unidades que incorporen contenidos de salud digital considerarán preferentemente al Departamento. Me interesa cómo lo redactaría usted para que funcione bien con las otras Facultades.",
], "Entrégale aquí el decreto impreso y el resumen ejecutivo, si los llevas.")

bloque("Cierre")
lamina(13, "Cierre", [
    "Eso es lo que quería mostrarle. Ahora me gustaría escucharlo. Tengo tres preguntas.",
    "Una: ¿cómo debería entrar el marco de desempeños a los perfiles de egreso sin interferir con los procesos curriculares de las carreras?",
    "Dos: ¿qué aprendió la Universidad con el Departamento Nacional de Salud Pública que deberíamos considerar?",
    "Y tres: ¿qué le falta a este texto para llegar bien a las instancias que siguen?",
    "Con lo que me diga ajusto el texto y se lo hago llegar antes de presentarlo. ¿Le parece?",
], "Las preguntas están en la guía de conversación; cámbialas por las que elijas. Después de preguntar, espera: no llenes el silencio.")

bloque("Respaldo: solo si pregunta")
lamina(14, "Respaldo (portadilla)", ["Tengo el detalle de cada unidad si quiere verlo."])
lamina(15, "Dirección Nacional · artículo 8", [
    "La Dirección Nacional conduce el Departamento bajo la autoridad de la Decana: planifica, propone Jefaturas y Coordinaciones, programa la docencia de las asignaturas adscritas, identifica requerimientos y rinde cuenta a la Decana y al Consejo de Facultad.",
])
lamina(16, "Comité Consultivo · artículo 9", [
    "El Comité asesora a la Dirección en la planificación y el seguimiento. Lo integran la Dirección, las Jefaturas de Área y los Coordinadores de Sede. Puede sesionar en forma ampliada, con las Escuelas o con otras Facultades, según el tema. No decide: asesora.",
])
lamina(17, "Área de Docencia · artículo 10", [
    "El Área de Docencia hace el seguimiento de la formación, la compara con lo que existe en Chile y en el mundo, y formula propuestas para robustecerla, mejorarla y actualizarla, en pregrado, postgrado y educación continua. Las carreras incorporan esas propuestas por sus propios procesos.",
])
lamina(18, "Área de Proyectos · artículo 10", [
    "El Área de Proyectos gestiona la línea basal, la investigación y la vinculación con el medio, en coordinación con las Vicerrectorías y las unidades competentes. No reemplaza a ninguna: trabaja con ellas.",
])
lamina(19, "Coordinaciones de Sede · artículo 11", [
    "Cada Coordinación representa al Departamento en su sede, hace el seguimiento y levanta los indicadores locales, y cuida que la formación sea equivalente entre sedes: mismos resultados de aprendizaje, considerando la realidad de cada una.",
])
d.save(sys.argv[1])
