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


TITULO = "La ley ya lo dice. Ahora tienen que conversar los sistemas"
COLUMNA = [
    "A casi todos nos ha pasado. Llegamos a una consulta con una carpeta de exámenes bajo el brazo, o le repetimos a un médico nuevo la misma historia que ya les contamos a otros tres: qué remedios tomamos, de qué nos operaron, a qué somos alérgicos. Y si el examen quedó en otra clínica o en otro hospital, muchas veces toca hacerlo de nuevo.",
    "No es falta de voluntad de quienes nos atienden. Es que nuestra información de salud vive en sistemas que no conversan entre sí. Lo que se anotó en el consultorio muchas veces no se ve desde la urgencia del hospital, y lo de la clínica tampoco se ve desde el consultorio. Quien termina llevando los datos de un lado a otro es la persona enferma.",
    "Chile ya decidió que esto tiene que cambiar. En mayo de 2024 se publicó la Ley 21.668, que modificó la ley de derechos y deberes de los pacientes. Dice que la ficha clínica existe para permitir “una atención continua, coordinada y centrada en las personas”, y hace responsables a los prestadores de salud, públicos y privados, de adoptar las medidas para que la información de sus fichas esté disponible para el profesional que nos atiende, aunque trabaje en otro lugar. La palabra técnica es interoperabilidad. En simple: que la información siga al paciente, y no al revés.",
    "Pero una ley no conecta sistemas. Eso lo hacen personas: equipos de informática, de enfermería, de medicina y de gestión que tienen que ponerse de acuerdo en algo tan básico como anotar los datos de la misma manera, y después probar que funciona. Probarlo antes, no el día en que el paciente llega a la urgencia.",
    "Para eso existe la Connectathon. El nombre suena raro, pero la idea es sencilla: durante unos días, equipos de hospitales, empresas, universidades e instituciones públicas se sientan en la misma sala, conectan sus sistemas de verdad y comprueban si logran intercambiar información en un idioma común. Lo que falla se corrige ahí mismo. En la edición de este año participaron más de 60 equipos, y uno de los sistemas que se validaron allí, para gestionar los tiempos de espera de cirugías, entró en operación a mediados de año en el Hospital de Quilpué.",
    "Las personas son también lo que más falta. Quienes hoy estudian una carrera de la salud van a trabajar toda su vida con fichas electrónicas, atención a distancia y datos. No todos se van a dedicar a la salud digital, y está bien, pero nadie puede quedar fuera. En la Universidad San Sebastián, [este semestre 1.788 estudiantes de cuatro carreras cursan la asignatura Salud Digital en cuatro sedes].",
    "Por eso me alegra contar que la Universidad San Sebastián será sede de la próxima Connectathon, que se realizará [del 12 al 14 de enero de 2027] en [nuestro Campus Bellavista, en Santiago], [organizada por HL7 Chile con la colaboración de Fonasa y CENS]. [La participación es gratuita, con inscripción previa.]",
    "Abrimos las puertas porque creemos que la universidad es el lugar natural para este trabajo: aquí se forman quienes van a cuidar, y aquí pueden sentarse a probar sus sistemas quienes ya los construyen. La ley fijó el rumbo. En enero nos toca ponernos a trabajar.",
]


def columna(salida):
    d = nuevo()
    h1(d, "Columna de opinión sobre la Connectathon: borrador 1")
    par(d, "Para iterar con Comunicaciones USS. 17 de noviembre de 2026. Lo resaltado entre corchetes depende de datos por confirmar.", cursiva=True, color=GRIS, tam=10)
    h2(d, "Tres enfoques posibles")
    vin(d, "A. Desde el paciente (recomendado): ", "la ley ya manda que la información siga a la persona; la Connectathon es donde eso se prueba de verdad.")
    vin(d, "B. Desde la formación: ", "la interoperabilidad la hacen personas, y la universidad es donde se forman; por eso la Connectathon llega a un campus.")
    vin(d, "C. Desde la región: ", "las Américas están conectando su salud y Chile no parte de cero; la Connectathon es el paso local de esa ruta.")
    par(d, "Recomiendo el A: parte de algo que cualquier lector ha vivido, explica la ley sin jerga y deja el anuncio como consecuencia natural. Recoge del B el párrafo sobre los estudiantes.")
    h2(d, "Borrador (enfoque A)")
    par(d, TITULO, negrita=True, color=NAVY, tam=15)
    for t in COLUMNA:
        par(d, t)
    par(d, "[Firma: Estefanía Fröhlich, Directora del Departamento de Salud Digital, Facultad de Ciencias para el Cuidado de la Salud, Universidad San Sebastián]", cursiva=True)
    n = sum(len(re.sub(r"[\[\]]", "", t).split()) for t in COLUMNA)
    par(d, f"Extensión: {n} palabras sin título ni firma.", color=GRIS, tam=10)
    h2(d, "Qué falta confirmar")
    vin(d, "Datos de la Connectathon. ", "Fecha, campus, organizador y colaboradores están tomados del sitio de HL7 Chile (hl7chile.cl, leído el 17 de noviembre). Falta que confirmes que es esa la Connectathon, que los datos son definitivos y cómo se nombra el rol de la USS: el sitio la muestra como sede y colaboradora.")
    vin(d, "La ley. ", "Usé la Ley 21.668, leída en el Diario Oficial del 28 de mayo de 2024. Falta confirmar que es la que Gabriela tiene en mente.")
    vin(d, "Reglamento. ", "La ley dio 18 meses al Ministerio de Salud para actualizar el reglamento de fichas clínicas. El resumen que pegaste dice que el plazo venció y el reglamento sigue pendiente; lo mismo dicen una columna de abogados en EstadoDiario (20 de octubre de 2026) y un blog comercial, pero ninguno cita una fuente oficial y LeyChile no dejó leerse. Por eso la columna no lo afirma. Si lo confirmas con el Ministerio o con HL7 Chile, se puede agregar al cuarto párrafo: [“El reglamento que debe fijar las reglas comunes todavía está pendiente”]. Es una frase que apunta al Ministerio: conviene decidirla con la Decana.")
    vin(d, "Ley de datos personales. ", "No la menciono. El resumen que pegaste dice que rige desde el 1 de diciembre de 2026, pero al 11 de noviembre el Congreso tramitaba postergarla a octubre de 2027 y hoy no pude leer el sitio de la Cámara para ver en qué quedó.")
    vin(d, "Cifra de estudiantes. ", "Los 1.788 estudiantes vienen de tu informe con datos de Blackboard al 25 de septiembre de 2026. Falta confirmar que puede publicarse.")
    vin(d, "Medio, extensión y plazo. ", "Escribí para 500 a 600 palabras. Si el medio pide menos, el párrafo más fácil de cortar es el de los estudiantes.")
    vin(d, "Firma. ", "Está en tu voz. Si firma la Decana, cambian tres cosas: el párrafo de los estudiantes habla de toda la Facultad, “me alegra contar” pasa a un anuncio institucional, y conviene que la Decana revise el cierre.")
    vin(d, "Departamento Nacional de Salud Digital. ", "No se menciona, porque está en trámite.")
    h2(d, "Fuentes de lo que se afirma")
    for a, b in [
        ("Ley 21.668 y cita textual: ", "Diario Oficial, 28 de mayo de 2024, núm. 43.861."),
        ("“Públicos y privados”: ", "nota del Ministerio de Salud del 28 de mayo de 2024."),
        ("Más de 60 equipos en 2026: ", "nota de CENS del 22 de enero de 2026."),
        ("Sistema en operación en el Hospital de Quilpué: ", "nota de HL7 Chile del 3 de julio de 2026."),
        ("Connectathon 2027: ", "hl7chile.cl/fhir-connectathon-hl7-2027, leído el 17 de noviembre de 2026."),
    ]:
        vin(d, a, b)
    par(d, "Las direcciones completas están en fuentes.md, en la misma carpeta.", color=GRIS, tam=10)
    d.save(salida / "columna-borrador-1.docx")
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
