"""Genera los dos documentos Connectathon. Uso: python3 generar.py <carpeta de salida>"""
import re, sys
from pathlib import Path
from docx import Document
from docx.enum.text import WD_COLOR_INDEX
from docx.shared import Cm, Pt, RGBColor

NAVY, BLUE, GRIS = RGBColor(0x14, 0x37, 0x5A), RGBColor(0x2F, 0x6D, 0xB5), RGBColor(0x5F, 0x64, 0x70)


def nuevo():
    d = Document()
    s = d.sections[0]
    s.page_width, s.page_height = Cm(21.59), Cm(27.94)
    s.left_margin = s.right_margin = Cm(2.3)
    s.top_margin = s.bottom_margin = Cm(2.0)
    n = d.styles["Normal"]
    n.font.name, n.font.size = "Calibri", Pt(11)
    n.paragraph_format.space_after = Pt(7)
    return d


def texto(p, t, negrita=False, cursiva=False, color=None, tam=None):
    """Escribe t; lo que va entre [corchetes] queda resaltado (dato por confirmar)."""
    for trozo in re.split(r"(\[[^\]]+\])", t):
        if not trozo:
            continue
        r = p.add_run(trozo)
        r.bold, r.italic = negrita, cursiva
        if color: r.font.color.rgb = color
        if tam: r.font.size = Pt(tam)
        if trozo.startswith("["):
            r.font.highlight_color = WD_COLOR_INDEX.YELLOW


def par(d, t, **k):
    p = d.add_paragraph()
    texto(p, t, **k)
    return p


def h1(d, t):
    p = par(d, t, negrita=True, color=NAVY, tam=17)
    p.paragraph_format.space_before, p.paragraph_format.keep_with_next = Pt(6), True


def h2(d, t):
    p = par(d, t.upper(), negrita=True, color=BLUE, tam=10)
    p.paragraph_format.space_before, p.paragraph_format.keep_with_next = Pt(12), True


def vin(d, negrita, resto=""):
    p = d.add_paragraph()
    p.paragraph_format.left_indent, p.paragraph_format.first_line_indent = Cm(0.6), Cm(-0.4)
    p.paragraph_format.space_after = Pt(4)
    p.add_run("•  ")
    texto(p, negrita, negrita=True)
    texto(p, resto)


TITULO = "La salud conectada de 2030 se forma desde hoy"
COLUMNA = [
    "Al 31 de marzo de este año, la mitad de las personas que aguardaban una cirugía en el sistema público llevaba más de 259 días en la lista, según el informe del Ministerio de Salud al Congreso. A esa espera se suma una escena conocida: la carpeta de exámenes bajo el brazo y la misma historia contada otra vez a cada profesional nuevo, porque la información suele quedarse en el lugar donde nos atendimos.",
    "Chile ya tomó decisiones para cambiar esa escena. Desde mayo de 2024, la Ley 21.668 hace responsables a los prestadores, públicos y privados, de que la ficha clínica esté disponible para el profesional que nos atiende, aunque trabaje en otro establecimiento. En septiembre, el Ministerio de Salud presentó siete proyectos de transformación digital, entre ellos una Historia Clínica Compartida y el apoyo digital a la gestión de las listas de espera. El horizonte que se fijó es 2030: para entonces, los sistemas de todos los establecimientos deberían poder compartir información.",
    "Es una buena noticia y una meta exigente. Cuatro años pasan rápido cuando hay que lograr que sistemas muy distintos anoten los datos de la misma manera y se entiendan entre sí, con un cuidado que hoy cruza todos los sectores y del que la salud tampoco queda fuera: la información que se comparte tiene que circular protegida.",
    "Una meta así se alcanza practicando, y para eso existe la Connectathon. Durante unos días, equipos de hospitales, empresas, universidades e instituciones públicas se sientan en la misma sala, conectan sus sistemas reales y comprueban si logran intercambiar información en un idioma común. Lo que falla se corrige ahí mismo. En la edición de este año participaron más de 60 equipos, y uno de los sistemas validados allí, para gestionar los tiempos de espera de cirugías, entró en operación a mediados de año en el Hospital de Quilpué.",
    "Hay una parte de esta meta de la que hablamos poco: las personas. Cada dato que viaja entre un consultorio y un hospital fue registrado por alguien del equipo de salud, y que ese registro sea completo, comprensible para otro equipo y cuidadoso con la privacidad es hoy parte de saber cuidar. Quien está en primer año de una carrera de la salud va a titularse en torno a 2030 y trabajará toda su vida en ese sistema conectado. Mi propuesta es mirar la formación con la misma altura de miras que la tecnología: que el camino a 2030 incluya qué debe saber de salud digital cada persona que egresa de una carrera de la salud, y que universidades, Ministerio y prestadores lo definamos juntos. En la Universidad San Sebastián ya empezamos: este semestre, 1.788 estudiantes de cuatro carreras cursan la asignatura Salud Digital en cuatro sedes.",
    "Con esa convicción, la Universidad San Sebastián será sede de la próxima Connectathon, del 12 al 14 de enero de 2027, en nuestro Campus Bellavista, en Santiago, organizada por HL7 Chile con la colaboración de Fonasa y CENS.",
    "La universidad es un buen lugar para este trabajo: aquí se forman quienes van a cuidar, y aquí pueden sentarse a probar sus sistemas quienes ya los construyen, junto a las instituciones públicas que fijan el rumbo. 2030 está a cuatro eneros de distancia. El primero es este.",
]


def columna(salida):
    d = nuevo()
    h1(d, "Columna de opinión sobre la Connectathon: borrador 5")
    par(d, "Para iterar con Comunicaciones USS. 18 de noviembre de 2026. Datos confirmados por la titular; ya no quedan corchetes.", cursiva=True, color=GRIS, tam=10)
    h2(d, "Idea y hilo conductor")
    par(d, "Idea única: el país ya tiene ley, proyectos y una meta a 2030; para llegar hacen falta práctica y personas formadas. Propuesta de la autora: que la formación en salud digital sea parte del camino a 2030, definida entre universidades, Ministerio y prestadores.")
    par(d, "El hilo es el camino hacia 2030. Cada párrafo es un paso: la escena que vive el paciente, lo que el país ya decidió, por qué la meta es exigente, cómo se practica (Connectathon), la propuesta sobre formación y el anuncio. El cierre vuelve a 2030 y a enero.")
    h2(d, "Borrador")
    par(d, TITULO, negrita=True, color=NAVY, tam=15)
    for t in COLUMNA:
        par(d, t)
    par(d, "Estefanía Fröhlich, Directora del Departamento de Salud Digital, Facultad de Ciencias para el Cuidado de la Salud, Universidad San Sebastián", cursiva=True)
    n = sum(len(re.sub(r"[\[\]]", "", t).split()) for t in COLUMNA)
    c = sum(len(re.sub(r"\s", "", t)) for t in COLUMNA)
    ct = c + len(re.sub(r"\s", "", TITULO))
    par(d, f"Extensión: {c} caracteres sin espacios ({ct} con el título), {n} palabras. Límite del medio: 3.200 caracteres sin espacios.", color=GRIS, tam=10)
    h2(d, "Qué falta confirmar")
    vin(d, "Fonasa y cifra de estudiantes. ", "Confirmados por ti el 18 de noviembre: Fonasa es colaborador y los 1.788 estudiantes se pueden publicar.")
    vin(d, "Cifra de espera. ", "Los 259 días son la mediana de espera de cirugías No GES al 31 de marzo de 2026, del informe más reciente publicado por el Ministerio. Si sale uno nuevo antes de la entrega, hay que actualizarla.")
    vin(d, "Medio y fecha de entrega. ", "Falta saber en qué medio sale y cuándo se entrega. Gabriela indicó 3.200 caracteres sin espacios y que ella le da la forma final.")
    h2(d, "Decisiones de este borrador")
    vin(d, "Seguridad de datos: ", "queda en una frase del tercer párrafo, sin mencionar la ley de datos personales ni el ciberataque.")
    vin(d, "Ministerio de Salud: ", "se nombra su agenda de septiembre y la meta de 2030 como punto de partida, en tono de apoyo.")
    vin(d, "Reglamento de la Ley 21.668: ", "no se menciona; no pude confirmar su estado en fuente oficial.")
    vin(d, "Departamento Nacional de Salud Digital: ", "no se menciona, porque está en trámite.")
    vin(d, "Datos de inscripción: ", "salieron de la columna para que no se lea como publicidad; van en el publirreportaje.")
    vin(d, "“Va a titularse en torno a 2030”: ", "supone carreras de cinco años para quien cursa primer año en 2026. Ajústalo si prefieres otra forma de decirlo.")
    h2(d, "Fuentes de lo que se afirma")
    for a, b in [
        ("259 días de espera: ", "Ministerio de Salud, informe Glosa 06 del primer trimestre de 2026."),
        ("Ley 21.668 y cita textual: ", "Diario Oficial, 28 de mayo de 2024, núm. 43.861."),
        ("“Públicos y privados”: ", "nota del Ministerio de Salud del 28 de mayo de 2024."),
        ("Siete proyectos y meta 2030: ", "comunicado del Ministerio de Salud del 2 de septiembre de 2026."),
        ("Más de 60 equipos en 2026: ", "nota de CENS del 22 de enero de 2026."),
        ("Sistema en operación en el Hospital de Quilpué: ", "nota de HL7 Chile del 3 de julio de 2026."),
        ("Connectathon 2027: ", "hl7chile.cl/fhir-connectathon-hl7-2027, leído el 17 de noviembre de 2026."),
    ]:
        vin(d, a, b)
    par(d, "Las direcciones completas están en fuentes.md e investigacion-dolores.md, en la misma carpeta.", color=GRIS, tam=10)
    d.save(salida / "columna-borrador-5.docx")
    return n


def publirreportaje(salida):
    d = nuevo()
    h1(d, "Publirreportaje en La Tercera Digital: estructura e insumos")
    par(d, "Tema: cómo la USS prepara la Connectathon. Publicación en diciembre de 2026, después de la columna. Esto es solo la estructura: no se redacta hasta tener los datos.", cursiva=True, color=GRIS, tam=10)
    h2(d, "Estructura propuesta")
    for a, b in [
        ("1. Titular y bajada. ", "El hecho: la USS recibe en enero la Connectathon. La bajada dice en una frase para qué sirve a los pacientes."),
        ("2. Entrada con una escena. ", "Un equipo o una sala del campus preparándose, o un caso concreto de lo que cambia cuando los sistemas comparten información."),
        ("3. Qué es una Connectathon y por qué importa ahora. ", "Explicación en simple y el vínculo con la ley de interoperabilidad de fichas clínicas."),
        ("4. Cómo se prepara la USS. ", "El centro del texto: qué está haciendo la universidad, quiénes participan, qué espacios y equipos dispone, qué talleres previos hay."),
        ("5. Estudiantes y docentes. ", "Cómo se suman y qué aprenden; la formación en salud digital de la Facultad."),
        ("6. Voces. ", "Dos o tres citas: una autoridad de la USS, la organización y, si se puede, un estudiante o un equipo participante."),
        ("7. Recuadro de servicio. ", "Fechas, lugar, a quién está dirigida y cómo inscribirse."),
    ]:
        vin(d, a, b)
    h2(d, "Insumos que hay que pedir")
    for a, b in [
        ("Formato del medio: ", "extensión, número de fotos, fecha de cierre, si lleva enlace de inscripción y quién aprueba el texto final."),
        ("Datos confirmados del evento: ", "fechas, campus y salas, organizador, colaboradores y auspiciadores, y cómo debe nombrarse a cada uno. Hoy solo están los del sitio de HL7 Chile."),
        ("Qué hace la USS en la preparación: ", "equipo a cargo, tareas, conectividad y espacios, apoyo de sedes, hitos de aquí a enero. No tengo ningún dato de esto."),
        ("Participación de la comunidad USS: ", "si habrá equipos de estudiantes o docentes, voluntarios, y de qué carreras."),
        ("Cifras: ", "inscritos o cupos, equipos esperados, datos de ediciones anteriores validados por la organización, y estudiantes de Salud Digital que se puedan publicar."),
        ("Voceros y citas: ", "quién habla por la USS (Decana, tú u otra autoridad), quién por HL7 Chile, y si Fonasa o CENS quieren aparecer. Cada cita necesita aprobación de quien la da."),
        ("Fotos: ", "del campus y de las salas, del equipo organizador, de ediciones anteriores con permiso de uso, y logos en buena resolución."),
        ("Lo que se puede y no se puede decir: ", "si se menciona el Departamento Nacional de Salud Digital, y qué mensajes quiere destacar la Facultad."),
    ]:
        vin(d, a, b)
    h2(d, "Orden sugerido")
    par(d, "Primero cerrar la columna, porque fija el mensaje y los datos. Con esos mismos datos confirmados y los insumos de esta lista se redacta el publirreportaje.")
    d.save(salida / "publirreportaje-estructura.docx")


if __name__ == "__main__":
    salida = Path(sys.argv[1])
    print("palabras columna:", columna(salida))
    publirreportaje(salida)
