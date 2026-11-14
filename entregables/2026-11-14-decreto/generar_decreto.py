"""Genera el decreto v0.4 y el resumen ejecutivo en Word.

Uso: python3 generar_decreto.py <carpeta_salida>
Base: Decreto_Depto_SD_v0.3_borrador.docx (Drive de la titular, 2026-11-11).
"""
import sys
from pathlib import Path

from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.shared import Cm, Pt, RGBColor

NAVY = RGBColor(0x14, 0x37, 0x5A)
BLUE = RGBColor(0x2F, 0x6D, 0xB5)
GRIS = RGBColor(0x5F, 0x64, 0x70)


def nuevo(fuente, tam):
    d = Document()
    s = d.sections[0]
    s.page_width, s.page_height = Cm(21.59), Cm(27.94)
    s.left_margin = s.right_margin = Cm(2.6)
    s.top_margin = s.bottom_margin = Cm(2.3)
    n = d.styles["Normal"]
    n.font.name, n.font.size = fuente, Pt(tam)
    n.paragraph_format.space_after = Pt(7)
    n.paragraph_format.line_spacing = 1.12
    return d


def p(d, partes, alin=WD_ALIGN_PARAGRAPH.JUSTIFY, sangria=0, despues=None, color=None, tam=None):
    """partes: texto, o lista de (texto, negrita)."""
    par = d.add_paragraph()
    par.alignment = alin
    if sangria:
        par.paragraph_format.left_indent = Cm(sangria)
    if despues is not None:
        par.paragraph_format.space_after = Pt(despues)
    if isinstance(partes, str):
        partes = [(partes, False)]
    for texto, negrita in partes:
        r = par.add_run(texto)
        r.bold = negrita
        if color:
            r.font.color.rgb = color
        if tam:
            r.font.size = Pt(tam)
    return par


def titulo(d, texto, tam=11, color=None, centro=False, antes=10):
    par = p(d, [(texto, True)], WD_ALIGN_PARAGRAPH.CENTER if centro else WD_ALIGN_PARAGRAPH.LEFT,
            color=color, tam=tam)
    par.paragraph_format.space_before = Pt(antes)
    par.paragraph_format.keep_with_next = True
    return par


# ───────────────────────── Decreto v0.4 ─────────────────────────

VISTOS = [
    "El Proyecto Educativo de la Universidad San Sebastián, su Plan de Desarrollo Institucional 2022–2029 y el Plan Estratégico de la Facultad de Ciencias para el Cuidado de la Salud 2025–2029;",
    "Los Decretos de Rectoría N.º 7/2026, N.º 20/2026, N.º 1/2025 y N.º 105-BIS/2024, que contienen, respectivamente, el Reglamento General, el Reglamento de Unidades Académicas, el Reglamento del Académico y el Reglamento de Docencia de Pregrado;",
    "El Modelo Educativo de la Universidad, que mantiene en observación activa los avances científicos y tecnológicos, incluida la inteligencia artificial, para actualizar responsablemente sus enfoques formativos;",
    "El Decreto de Rectoría N.º 116/2020, que oficializa la creación del Departamento Nacional de Salud Pública;",
    "Que, conforme al artículo 4 del Reglamento de Unidades Académicas, los Departamentos son unidades académicas pertenecientes a una Facultad que, de forma transversal en la Universidad, generan, desarrollan y comunican el conocimiento o la docencia en el ámbito de una disciplina, incluyendo carreras y programas de distintas Facultades;",
    "Que la Organización Mundial de la Salud, en su Estrategia Mundial sobre Salud Digital 2020–2027 y en su análisis de los marcos y estándares de competencias en salud digital, insta a desarrollar una fuerza de trabajo en salud con competencias digitales;",
    "Que las Leyes N.º 21.541, sobre telemedicina; N.º 21.668, sobre interoperabilidad de fichas clínicas, y N.º 21.719, sobre protección de datos personales, imponen al sistema de salud exigencias que requieren profesionales formados en salud digital;",
    "Que el proceso de autoevaluación institucional 2026 identificó como oportunidades de mejora, entre otras, consolidar el ecosistema digital e incorporar la inteligencia artificial en los procesos formativos, y fortalecer la articulación entre investigación, formación de pregrado y vinculación con el medio, así como la complementariedad entre sedes;",
    "La necesidad de contar con una unidad académica de carácter nacional que concentre, articule y proyecte el quehacer de la Universidad en salud digital, en todas sus sedes y en colaboración con las Facultades cuyas disciplinas concurren a ella; y",
    "Las facultades que me confieren los estatutos y la reglamentación vigente.",
]

OBJETIVOS = [
    ("1.º", "El Departamento Nacional de Salud Digital se crea con el objetivo general de constituirse en la unidad académica de referencia nacional de la Universidad San Sebastián en salud digital, entendida como el campo de conocimiento y práctica relativo al desarrollo y uso de tecnologías digitales para mejorar la salud de las personas y las poblaciones. Este campo comprende los sistemas de información e interoperabilidad en salud; la telesalud; la ciencia de datos y la inteligencia artificial aplicadas a la salud; la transformación digital de los servicios de salud; la ética, la regulación y la protección de datos en salud; la equidad y los determinantes digitales de la salud; las competencias digitales de los equipos de salud, y las demás áreas que surjan con el avance científico y tecnológico del campo. Para ello, concentrará y articulará las funciones de docencia de pregrado, postgrado y educación continua, investigación, vinculación con el medio y desarrollo de proyectos en dicho campo.", []),
    ("2.º", "El Departamento Nacional de Salud Digital tendrá presencia en todas las sedes de la Universidad y, conforme al artículo 4 del Reglamento de Unidades Académicas, desarrollará su quehacer de forma transversal, prestando servicios académicos a las carreras y programas de cualquier Facultad que los requieran. Agrupará a académicos dedicados a la docencia de pregrado, postgrado y educación continua, la investigación, la vinculación con el medio y el desarrollo de proyectos en salud digital, y articulará su trabajo con las carreras del área de la salud y con las Facultades cuyas disciplinas concurren a la salud digital, en especial la ingeniería y el derecho.", []),
    ("3.º", "En materia de docencia de pregrado, el Departamento tiene como objetivo específico que los estudiantes de la Universidad logren los desempeños en salud digital que requiere el ejercicio profesional actual y futuro, mediante una formación equivalente y de calidad en todas las sedes. Para ello:", [
        "a) Administrará las asignaturas que se le adscriban, las que tributarán a los resultados de aprendizaje y a los perfiles de egreso de las carreras que las requieran;",
        "b) Propondrá un marco común de desempeños en salud digital para los perfiles de egreso de las carreras del área de la salud, sustentado en la investigación del Departamento y en los estándares internacionales de competencias en salud digital, para su incorporación por las carreras conforme a sus procesos de diseño y actualización curricular; y",
        "c) Ofrecerá electivos, cursos u otras actividades curriculares en salud digital a estudiantes de las distintas carreras.",
    ]),
    ("4.º", "En materia de postgrado y educación continua, el Departamento tiene como objetivo específico formar capital humano avanzado en salud digital. Para ello, diseñará, ofrecerá y gestionará programas propios de postgrado y educación continua, conforme a la normativa institucional vigente, y prestará servicios académicos especializados a los programas de otras unidades académicas que incorporen contenidos de salud digital en sus asignaturas o módulos. Las unidades académicas de la Universidad que incorporen contenidos de salud digital en sus programas considerarán preferentemente al Departamento para su diseño y ejecución.", []),
    ("5.º", "En materia de investigación, el Departamento tiene como objetivo específico constituirse en un referente nacional e internacional en investigación, desarrollo e innovación en salud digital, mediante la organización y potenciación de las capacidades de sus académicos y la integración de académicos de otras Facultades a sus líneas de investigación. Para ello, propondrá líneas de investigación en el ámbito definido en el artículo 1.º, entre ellas una línea basal que sustente el marco de desempeños señalado en el artículo 3.º; acordará con sus académicos objetivos de investigación; promoverá la adjudicación de proyectos con financiamiento interno y externo, alineados con la Política de Investigación institucional, y fomentará la participación de estudiantes de pregrado y postgrado en sus actividades de investigación.", []),
    ("6.º", "En materia de vinculación con el medio, el Departamento tiene como objetivo específico aportar su especialidad en salud digital a la interacción bidireccional de la Universidad con su entorno, contribuyendo a la transformación digital del sistema de salud y al bienestar de las comunidades en los territorios donde la Universidad está presente. Para ello, trabajará en conjunto con las unidades de vinculación con el medio de la Universidad, de la Facultad y de las carreras, sin perjuicio de sus atribuciones, articulando sus iniciativas con la docencia y la investigación.", []),
]

ORGANIZACION = [
    ("7.º", "El Departamento Nacional de Salud Digital formará parte y dependerá administrativa y académicamente de la Facultad de Ciencias para el Cuidado de la Salud. Constituye una unidad académica única de carácter nacional, integrada por la Dirección Nacional, el Área de Docencia, el Área de Proyectos, las Coordinaciones de Sede y sus académicos, y contará con un Comité Consultivo. Las Áreas y las Coordinaciones de Sede son instancias internas de gestión del Departamento y no constituyen unidades académicas ni autoridades unipersonales en los términos de los artículos 1 y 9 del Reglamento de Unidades Académicas.", []),
    ("8.º", "El Departamento estará a cargo de un Director o Directora Nacional, designado conforme al Reglamento de Unidades Académicas, quien, bajo la autoridad del Decano o Decana, será el directivo académico responsable de conducir el Departamento y de ejecutar los acuerdos de la Facultad en las materias de su competencia. En caso de ausencia o impedimento, será subrogado por la Jefatura de Área que designe el Decano o Decana, a propuesta de la Dirección Nacional.", []),
    ("9.º", "El Departamento contará con un Comité Consultivo, que asesorará a la Dirección Nacional en la planificación y el seguimiento de su quehacer. Estará integrado por el Director o Directora Nacional, quien lo presidirá, las Jefaturas de Área y los Coordinadores de Sede. El Comité sesionará periódicamente, en forma ordinaria o ampliada según las materias a tratar; a las sesiones ampliadas se convocará a representantes de las Escuelas y de las Facultades con las que se articula el Departamento, en especial de las disciplinas de ingeniería y derecho. Sus actas se remitirán a la Secretaría General conforme al artículo 27 del Reglamento de Unidades Académicas.", []),
    ("10.º", "El Área de Docencia, que comprende el pregrado, el postgrado y la educación continua, tendrá por objeto el seguimiento, el análisis comparado y la formulación de propuestas para robustecer, mejorar y actualizar la formación en salud digital. El Área de Proyectos, que comprende la línea basal, la investigación y la vinculación con el medio, tendrá a su cargo la gestión de las líneas y los proyectos del Departamento en esas materias, en coordinación con las Vicerrectorías y unidades institucionales competentes. Cada Área estará a cargo de una Jefatura.", []),
    ("11.º", "En cada sede de la Universidad existirá una Coordinación de Sede del Departamento, a cargo de un Coordinador o Coordinadora que dependerá de la Dirección Nacional y seguirá los lineamientos técnicos de las Áreas en sus respectivas materias. Le corresponderá representar al Departamento en la sede y realizar el seguimiento, el monitoreo y el levantamiento de indicadores locales de su quehacer, velando por la equivalencia de la formación entre sedes.", []),
    ("12.º", "Las Jefaturas de Área y los Coordinadores de Sede serán designados por el Decano o Decana, a propuesta de la Dirección Nacional.", []),
    ("13.º", "Integrarán el Departamento los académicos adscritos a él y los académicos de otras unidades académicas de la Universidad que participen en sus actividades conforme a lo acordado con su unidad de origen.", []),
]

TRANSITORIOS = [
    ("primero", "La Directora del Departamento en funciones a la fecha del presente decreto continuará en el cargo, y el período establecido en el artículo 14 del Reglamento de Unidades Académicas se computará a contar de la fecha del presente decreto."),
    ("segundo", "Mientras no se designen las Jefaturas de Área, sus funciones serán ejercidas por la Dirección Nacional."),
    ("tercero", "Las Áreas y las Coordinaciones de Sede se instalarán gradualmente, conforme al plan de implementación que la Dirección Nacional presentará al Decano o Decana."),
]


def decreto(ruta):
    d = nuevo("Cambria", 11)
    p(d, "Propuesta de decreto · versión 0.4 · documento de trabajo", WD_ALIGN_PARAGRAPH.RIGHT, color=GRIS, tam=9)
    titulo(d, "DECRETO DE RECTORÍA N.º [●]", 13, centro=True, antes=6)
    p(d, "Santiago, [●]", WD_ALIGN_PARAGRAPH.RIGHT)
    p(d, [("MATERIA: ", True), ("Oficializa la creación del Departamento Nacional de Salud Digital, adscrito a la Facultad de Ciencias para el Cuidado de la Salud de la Universidad San Sebastián.", False)])
    titulo(d, "VISTOS Y CONSIDERANDO:")
    for i, v in enumerate(VISTOS, 1):
        p(d, f"{i}.º  {v}")
    titulo(d, "DECRETO:")
    p(d, "Créase el Departamento Nacional de Salud Digital de la Universidad San Sebastián, adscrito a la Facultad de Ciencias para el Cuidado de la Salud, a contar de esta fecha, cuyos objetivos y organización serán los siguientes:")
    for encabezado, arts in (("DE LOS OBJETIVOS:", OBJETIVOS), ("DE LA ORGANIZACIÓN:", ORGANIZACION)):
        titulo(d, encabezado)
        for num, texto, letras in arts:
            p(d, [(f"Artículo {num} ", True), (texto, False)])
            for l in letras:
                p(d, l, sangria=1.0)
    titulo(d, "ARTÍCULOS TRANSITORIOS:")
    for num, texto in TRANSITORIOS:
        p(d, [(f"Artículo {num}. ", True), (texto, False)])
    p(d, "Publíquese, comuníquese y archívese.").paragraph_format.space_before = Pt(14)
    d.save(ruta)


# ───────────────────────── Resumen ejecutivo ─────────────────────────

def resumen(ruta):
    d = nuevo("Calibri", 9.5)
    s = d.sections[0]
    s.top_margin = s.bottom_margin = Cm(1.4)
    s.left_margin = s.right_margin = Cm(2.0)
    d.styles["Normal"].paragraph_format.space_after = Pt(3)
    d.styles["Normal"].paragraph_format.line_spacing = 1.05

    def h(t):
        titulo(d, t.upper(), 9, BLUE, antes=6).paragraph_format.space_after = Pt(2)

    def b(negrita, resto):
        par = p(d, [("•  ", False), (negrita, True), (resto, False)], WD_ALIGN_PARAGRAPH.LEFT, sangria=0.3, despues=1)
        par.paragraph_format.first_line_indent = Cm(-0.3)

    p(d, "RESUMEN EJECUTIVO", WD_ALIGN_PARAGRAPH.LEFT, color=BLUE, tam=9.5, despues=0).runs[0].bold = True
    t = p(d, "Departamento Nacional de Salud Digital", WD_ALIGN_PARAGRAPH.LEFT, color=NAVY, tam=18, despues=0)
    t.runs[0].bold = True
    t.runs[0].font.name = "Cambria"
    p(d, "Propuesta de decreto de creación · Facultad de Ciencias para el Cuidado de la Salud · Universidad San Sebastián",
      WD_ALIGN_PARAGRAPH.LEFT, color=GRIS, tam=10, despues=6)

    h("Qué se propone")
    p(d, "Crear, por decreto de Rectoría, una unidad académica única de carácter nacional que concentre y articule la docencia de pregrado, postgrado y educación continua, la investigación, la vinculación con el medio y los proyectos de la Universidad en salud digital, con presencia en todas las sedes y al servicio de las carreras y programas de cualquier Facultad. El texto tiene 13 artículos y 3 transitorios, y sigue el formato del decreto que creó el Departamento Nacional de Salud Pública (DR 116/2020).",
      WD_ALIGN_PARAGRAPH.LEFT)

    h("Por qué ahora")
    b("La normativa lo permite. ", "El Reglamento de Unidades Académicas (art. 4) define a los Departamentos como unidades transversales a carreras y programas de distintas Facultades.")
    b("El sistema de salud lo exige. ", "Las leyes de telemedicina (21.541), interoperabilidad de fichas clínicas (21.668) y protección de datos personales (21.719) requieren profesionales formados en salud digital.")
    b("El estándar internacional lo pide. ", "La Estrategia Mundial sobre Salud Digital de la OMS y su análisis de marcos de competencias instan a formar equipos de salud con competencias digitales.")
    b("La autoevaluación institucional 2026 lo señala. ", "Ecosistema digital e inteligencia artificial en la formación, articulación entre investigación, pregrado y vinculación con el medio, y complementariedad entre sedes.")

    h("Qué hará el Departamento (artículos 1 a 6)")
    b("Pregrado. ", "Administra las asignaturas que se le adscriban, propone un marco común de desempeños en salud digital para los perfiles de egreso y ofrece electivos. Cada carrera lo incorpora por sus propios procesos curriculares.")
    b("Postgrado y educación continua. ", "Diseña y gestiona programas propios y presta servicios especializados a los programas de otras unidades.")
    b("Investigación. ", "Propone líneas de investigación, entre ellas una línea basal que sustenta el marco de desempeños; promueve proyectos con financiamiento interno y externo e integra a estudiantes y a académicos de otras Facultades.")
    b("Vinculación con el medio. ", "Aporta su especialidad a las unidades de vinculación existentes, sin crear una nueva.")

    h("Cómo se organiza (artículos 7 a 13)")
    b("Dependencia. ", "Forma parte de la Facultad de Ciencias para el Cuidado de la Salud y actúa bajo la autoridad de la Decana.")
    b("Dirección Nacional. ", "Conduce el Departamento, con la asesoría de un Comité Consultivo que sesiona en forma ordinaria o ampliada con Escuelas y Facultades.")
    b("Área de Docencia. ", "Pregrado, postgrado y educación continua: seguimiento, análisis comparado y propuestas.")
    b("Área de Proyectos. ", "Línea basal, investigación y vinculación con el medio, en coordinación con las Vicerrectorías competentes.")
    b("Coordinaciones de Sede. ", "Santiago, Concepción, Valdivia y Puerto Montt: seguimiento, indicadores locales y equivalencia entre sedes. Dependen de la Dirección Nacional y siguen los lineamientos técnicos de las Áreas (estructura matricial).")

    h("Lo que el decreto resguarda")
    b("No crea nuevas unidades académicas ni autoridades unipersonales: ", "las Áreas y las Coordinaciones son instancias internas de gestión (art. 7).")
    b("No interviene los planes de estudio: ", "propone, y las carreras incorporan conforme a sus procesos (art. 3).")
    b("No duplica funciones: ", "trabaja con las unidades de vinculación con el medio y con las Vicerrectorías, sin perjuicio de sus atribuciones (arts. 6 y 10).")
    b("Instalación gradual: ", "las Áreas y las Coordinaciones se instalan según un plan de implementación que la Dirección Nacional presenta a la Decana (transitorio tercero).")

    h("Qué aporta a la Universidad")
    p(d, "Una formación en salud digital equivalente en todas las sedes; una lectura ordenada de lo que requiere el mundo laboral, con propuestas de respuesta para pregrado, postgrado y educación continua; una línea de investigación en competencias digitales en salud que queda instalada en la institución, e indicadores por sede que el Departamento puede poner a disposición de cada Vicerrectoría.",
      WD_ALIGN_PARAGRAPH.LEFT)

    h("Qué buscamos en esta conversación")
    p(d, "La mirada institucional de la Vicerrectoría Académica sobre el texto antes de ajustarlo y presentarlo a las instancias que corresponda.",
      WD_ALIGN_PARAGRAPH.LEFT)
    d.save(ruta)


if __name__ == "__main__":
    salida = Path(sys.argv[1])
    salida.mkdir(parents=True, exist_ok=True)
    decreto(salida / "decreto-depto-salud-digital-v0.4.docx")
    resumen(salida / "resumen-ejecutivo.docx")
