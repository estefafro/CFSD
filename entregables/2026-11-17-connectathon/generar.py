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
    "Quien se atiende en un consultorio y después en un hospital conoce la escena: la carpeta de exámenes bajo el brazo y la misma historia contada otra vez a cada profesional nuevo, porque la información suele quedarse en el lugar donde nos atendimos. Cambiar esa escena depende de sistemas que se conecten y de personas preparadas para registrar, compartir y cuidar esa información. De lo segundo hablamos poco, y las universidades tenemos mucho que aportar ahí.",
    "Chile ya tomó decisiones. La Ley 21.668, publicada en mayo de 2024, hace responsables a los prestadores, públicos y privados, de que la ficha clínica esté disponible para el profesional que nos atiende, aunque trabaje en otro establecimiento. Por su parte, el Ministerio de Salud presentó en septiembre siete proyectos de transformación digital, entre ellos una Historia Clínica Compartida, y se puso como horizonte de largo plazo que en 2030 los sistemas de los distintos establecimientos puedan compartir información. Ese horizonte también exige acordar qué competencias digitales deben demostrar quienes egresan de las carreras de la salud.",
    "Es una buena noticia y una meta exigente. Hay que lograr que sistemas muy distintos anoten los datos de la misma manera y se entiendan entre sí, con un cuidado que hoy cruza todos los sectores y del que la salud tampoco queda fuera: la información que se comparte tiene que circular protegida.",
    "Una meta así se alcanza practicando, y para eso existe la Connectathon. Durante unos días, equipos de hospitales, empresas, universidades e instituciones públicas se sientan en la misma sala, conectan sus sistemas reales y comprueban si logran intercambiar información en un idioma común. Lo que falla se corrige ahí mismo. En la edición de este año participaron más de 60 equipos, y uno de los sistemas validados allí, para gestionar los tiempos de espera de cirugías, entró en operación a mediados de año en el Hospital de Quilpué.",
    "Para una universidad, recibir ese trabajo es una oportunidad académica: acerca la enseñanza a los problemas que enfrentan los equipos cuando intentan intercambiar información clínica. Quienes hoy se forman deberán ejercer en un sistema cada vez más digital y contribuir a que la información de sus pacientes pueda compartirse de manera segura.",
    "Mi propuesta es mirar la formación con la misma altura de miras que la tecnología: que universidades, Ministerio y prestadores acordemos las competencias mínimas en salud digital que todo egresado de una carrera de la salud debería demostrar. Dos ejemplos: registrar información que le sirva al siguiente equipo para continuar el cuidado, y proteger su confidencialidad. En la Universidad San Sebastián ya empezamos: este semestre, 1.788 estudiantes de cuatro carreras cursan la asignatura Salud Digital en cuatro sedes.",
    "Con esa convicción, la Universidad San Sebastián será sede de la próxima Connectathon, del 12 al 14 de enero de 2027, en nuestro Campus Bellavista, en Santiago, organizada por HL7 Chile con la colaboración de Fonasa y CENS.",
    "Llegar a 2030 exige probar los sistemas y formar, desde hoy, a quienes usarán esa información para cuidar. Las universidades tenemos una responsabilidad concreta en ese camino.",
]


def columna(salida):
    d = nuevo()
    h1(d, "Columna de opinión sobre la Connectathon: borrador 6")
    par(d, "Para iterar con Comunicaciones USS. 18 de noviembre de 2026. Datos confirmados por la titular; ya no quedan corchetes.", cursiva=True, color=GRIS, tam=10)
    h2(d, "Idea central")
    par(d, "Las universidades tenemos la responsabilidad de preparar a quienes van a registrar, compartir y cuidar la información de los pacientes. Propuesta: que universidades, Ministerio y prestadores acuerden las competencias mínimas en salud digital de todo egresado. La Connectathon acerca esa formación a los problemas reales del sistema.")
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
    vin(d, "Medio y fecha de entrega. ", "Gabriela indicó 3.200 caracteres sin espacios y que ella le da la forma final.")
    h2(d, "Decisiones de este borrador")
    vin(d, "Cifra de listas de espera: ", "salió del texto, porque sugería que la espera se explica por la falta de conexión entre sistemas, y eso la columna no lo demuestra. Si se quisiera usar, el dato vigente es 277 días de mediana para cirugías No GES al 30 de junio de 2026 (informe Glosa 06 del segundo trimestre), no los 259 días de marzo.")
    vin(d, "Ley y meta 2030: ", "quedan separadas. La ley fija responsabilidades; el horizonte de 2030 es del Ministerio.")
    vin(d, "Hospital de Quilpué: ", "se dice que el sistema entró en operación; no se afirma que haya reducido esperas.")
    vin(d, "Connectathon y estudiantes: ", "se presenta como oportunidad académica, sin atribuir actividades de estudiantes que no están definidas.")
    vin(d, "Seguridad de datos: ", "queda en una frase del tercer párrafo.")
    vin(d, "Datos de inscripción: ", "van en el publirreportaje.")
    vin(d, "No se mencionan: ", "el reglamento de la Ley 21.668 (estado sin confirmar en fuente oficial), la ley de datos personales y el Departamento Nacional de Salud Digital.")
    h2(d, "Fuentes de lo que se afirma")
    for a, b in [
        ("Ley 21.668: ", "Diario Oficial, 28 de mayo de 2024, núm. 43.861."),
        ("“Públicos y privados”: ", "nota del Ministerio de Salud del 28 de mayo de 2024."),
        ("Siete proyectos y meta 2030: ", "comunicado del Ministerio de Salud del 2 de septiembre de 2026."),
        ("Más de 60 equipos en 2026: ", "nota de CENS del 22 de enero de 2026."),
        ("Sistema en operación en el Hospital de Quilpué: ", "nota de HL7 Chile del 3 de julio de 2026."),
        ("Connectathon 2027: ", "hl7chile.cl/fhir-connectathon-hl7-2027, leído el 17 de noviembre de 2026."),
    ]:
        vin(d, a, b)
    par(d, "Las direcciones completas están en fuentes.md e investigacion-dolores.md, en la misma carpeta.", color=GRIS, tam=10)
    d.save(salida / "columna-borrador-6.docx")
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
