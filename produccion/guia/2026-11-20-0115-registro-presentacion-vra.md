---
agente: guia
fecha: 2026-11-20
titulo: Registro de versiones de la presentación para la Vicerrectoría Académica (hasta la entregada el 2026-11-20) y de su guion (v0.1 y guion del 2026-11-20)
reemplaza: produccion/guia/2026-11-20-0026-registro-presentacion-vra.md
---

# Registro de versiones: presentación para la Vicerrectoría Académica y su guion

Este registro reemplaza al de las 00:26 de hoy y cuenta toda la historia. Primero va lo nuevo: la presentación que la titular entregó hoy y con la que presenta, y el guion que la sesión principal escribió hoy ajustado a ella. Al final copio íntegro el registro anterior, sin tocar su texto, salvo que a sus alertas les antepuse "(registro 2026-11-20 00:26)". Entre un registro y otro cambió también el decreto: hoy existe una v0.7 que dice "Dirección de Investigación" (registro del decreto de hoy, en esta misma carpeta), y por eso varias cosas que el registro anterior marcaba como "no calza" hoy calzan.

## Qué revisé y cómo

- [HECHO] Comparé `Presentacion_VRA_ejecutiva_v0.3.pptx` con `2026_11_20_Propuesta_Departamento_Salud_Digital_USS.pptx` con el comparador y saqué las huellas de ambos, del guion v0.1 y del Word y el PDF del guion nuevo. Fuente: salida de scripts/comparar_versiones.py sobre entregables/2026-11-20-presentacion-vra-ejecutiva/ (ejecutado 2026-11-20)
- [HECHO] Como el comparador no lee grupos, tablas, notas del orador, comentarios ni imágenes, extraje además todo el texto de las dos presentaciones recorriendo grupos y notas y los comparé línea por línea: las únicas diferencias son las que lista la tabla de cambios de más abajo; las notas del orador son idénticas en las dos. Fuente: extracción propia con python-pptx y diff sobre los dos archivos (ejecutado 2026-11-20)
- [HECHO] Comparé las siete imágenes incrustadas por su suma de verificación: son las mismas, byte por byte, en la v0.3 y en el archivo de hoy; volví a abrir la de la lámina 7 para leerla. Fuente: md5sum sobre ppt/media/ de ambos archivos e imagen de la lámina 7 del archivo de hoy (vista 2026-11-20)
- [HECHO] Los metadatos del archivo de hoy dicen: última modificación 2026-11-20 01:03 UTC, guardado por la cuenta de la titular, revisión 504 (la v0.3 era la 503), 20 láminas, 0 ocultas, 8 láminas con página de notas. Fuente: docProps/core.xml y docProps/app.xml de 2026_11_20_Propuesta_Departamento_Salud_Digital_USS.pptx (leído 2026-11-20)
- [HECHO] Leí completo el guion nuevo en el Word, comprobé que cada párrafo y cada celda del Word está en el PDF, y lo cotejé frase por frase contra la presentación de hoy, el decreto v0.7, `fuentes-cifras.md`, los dos archivos del benchmark y `perfil/cargo.md`. Fuente: Guion_reunion_VRA_2026-11-20.docx y .pdf, decreto-depto-salud-digital-v0.7.docx, fuentes-cifras.md, produccion/benchmark/ y perfil/cargo.md (leídos 2026-11-20)
- [HECHO] Quién hizo cada cambio y por qué me lo informó la sesión principal al encargarme este registro; yo no presencié la conversación con la titular. El encargo atribuye a la titular los títulos nuevos; de los demás cambios del archivo no dice nada, y ahí escribo "no consta". Fuente: encargo de la sesión principal al Guía, que cita a la titular del cargo (conversación 2026-11-20; recibido 2026-11-20)

### Huellas

| Archivo | Rótulo | Huella | Párrafos | Palabras |
|---|---|---|---|---|
| `entregables/2026-11-14-presentacion-vicerrector/presentacion-vicerrector.pptx` (generada por la sesión principal, 2026-11-15) | sin número | `398c67ef716e` | 440 | 2120 |
| `entregables/2026-11-14-presentacion-vicerrector/2026-11-16-presentacion-de-la-titular.pdf` | sin número | `448f03da26ac` | 275 | 2375 |
| Presentación ejecutiva v0.1 y v0.2 (no están en el repositorio) | v0.1, v0.2 | sin huella | no consta | no consta |
| `entregables/2026-11-20-presentacion-vra-ejecutiva/Presentacion_VRA_ejecutiva_v0.3.pptx` | v0.3 | `fea2d05b9a2b` | 449 | 2574 |
| `entregables/2026-11-20-presentacion-vra-ejecutiva/2026_11_20_Propuesta_Departamento_Salud_Digital_USS.pptx` (la que se presenta) | sin número; fecha en el nombre | `2d3da8bb6107` | 434 | 2483 |
| `entregables/2026-11-20-presentacion-vra-ejecutiva/Guion_VRA_ejecutiva_v0.1.pdf` | v0.1 | `15d9a8930129` (sin cambios) | 103 | 1249 |
| `entregables/2026-11-20-presentacion-vra-ejecutiva/Guion_reunion_VRA_2026-11-20.docx` (guion vigente) | sin número; fecha en el nombre | `d4c419aca308` | 61 | 1384 |
| `entregables/2026-11-20-presentacion-vra-ejecutiva/Guion_reunion_VRA_2026-11-20.pdf` | ídem | `4ec1999c69ff` (huella de PDF; no es comparable con la del Word) | 113 líneas | 1358 |
| `entregables/2026-11-14-decreto/decreto-depto-salud-digital-v0.7.docx` (decreto de hoy) | versión 0.7 | `d6cc1312e4a5` | 39 | 1810 |

## Alertas de hoy

Van primero las que el Vicerrector puede ver o escuchar hoy. Todas están comprobadas en los archivos, salvo donde digo que es hipótesis.

ALERTA 1. El archivo que entregó la titular no coincide con la última versión registrada. [HECHO] La última presentación registrada era la v0.3, de huella `fea2d05b9a2b`; el archivo de hoy tiene huella `2d3da8bb6107`, otro nombre y ningún número de versión. Fuente: scripts/comparar_versiones.py sobre los dos archivos (ejecutado 2026-11-20)
- [HECHO] No es un error: la titular lo entregó como la versión con la que presenta, y los cambios frente a la v0.3 son acotados (títulos de las láminas 2 a 8, cuatro textos sueltos y la eliminación de las cuatro láminas ocultas); mi definición me obliga a decirlo igual. Fuente: encargo de la sesión principal al Guía (recibido 2026-11-20) y comparación propia de los dos archivos (ejecutado 2026-11-20)
- [PROPUESTA] Tratar este archivo como la versión que sigue a la v0.3 e identificarlo por su fecha y su huella, ya que no lleva número. Se apoya en la línea anterior.

ALERTA 2. El archivo sigue llevando dentro los tres comentarios de otra persona, con nombre y correo institucional. [HECHO] El archivo de hoy conserva los tres comentarios incrustados del 2026-11-16, de "Carolina Gonzalez Reyes" (cuenta carolina.gonzalez@uss.cl), marcados como resueltos, en las láminas 7, 10 y 14, con el mismo texto que registré a las 00:26. Fuente: ppt/comments/, ppt/authors.xml y relaciones de las láminas en 2026_11_20_Propuesta_Departamento_Salud_Digital_USS.pptx (leído 2026-11-20)
- [HECHO] Las láminas ocultas ya no están: el archivo tiene 20 láminas y ninguna oculta, lo que confirma lo que vio la sesión principal; las notas del orador sí siguen, con las respuestas preparadas. Fuente: docProps/app.xml y recorrido de las 20 láminas del archivo de hoy (ejecutado 2026-11-20)
- [HECHO] El guion nuevo ya lo advierte bajo "Tres cuidados": "Si te piden la presentación, envía un PDF, no el PowerPoint". Fuente: Guion_reunion_VRA_2026-11-20.docx, sección "Tres cuidados" (leído 2026-11-20)
- [PROPUESTA] Mantener ese cuidado: no enviar el .pptx; si lo piden, PDF exportado sin notas. Se apoya en las tres líneas anteriores.

ALERTA 3. La lámina 7 sigue mostrando "Área de Docencia" y "Área de Investigación". [HECHO] La imagen del organigrama es exactamente la misma de la v0.3: recuadros "Área de Docencia" y "Área de Investigación", leyenda "articulación entre áreas", pie "lineamientos técnicos de ambas áreas a las cuatro sedes", y a la izquierda los rótulos "Dirección Nacional", "Direcciones de área" y "Direcciones de Sede". Fuente: md5sum de ppt/media/image7.png en ambos archivos e imagen de la lámina 7 (vista 2026-11-20)
- [HECHO] El recuadro "Área de Investigación" enumera cuatro frentes ("línea basal · investigación · vinculación con el medio · proyectos"); el artículo 10 de la v0.7 y las láminas 14 y 19 dicen tres, sin "proyectos". Fuente: imagen de la lámina 7, láminas 14 y 19 del archivo de hoy y artículo 10 de decreto-depto-salud-digital-v0.7.docx (leído 2026-11-20)
- [HECHO] El guion nuevo lo resuelve en voz alta: hace decir "Dos Direcciones de área, la de Docencia y la de Investigación" y agrega la indicación "Los recuadros del dibujo dicen «Área de Docencia» y «Área de Investigación». Tú di «Dirección», como el rótulo de la izquierda y como el decreto". Fuente: Guion_reunion_VRA_2026-11-20.docx, lámina 7 (leído 2026-11-20)
- [HIPÓTESIS] Lo que se dice y lo que se ve siguen sin coincidir en la única lámina de estructura de la exposición; con la indicación del guion es manejable, pero si el Vicerrector pregunta "¿Áreas o Direcciones?" conviene tener la respuesta lista: son Direcciones, cada una a cargo de un área. Lo confirmaría la titular.

ALERTA 4. Tres frases nuevas en pantalla dicen más de lo que alguna fuente del repositorio sostiene, y el guion no advierte sobre ellas. [HECHO] La lámina 3 cierra ahora con "La demanda es estructural: la exige la ley, la confirma el déficit de profesionales y nadie ha resuelto cómo formarla"; la v0.3 terminaba en "Y los marcos que revisó la OMS aún no incluyen IA". Fuente: comparación propia de la lámina 3 en ambos archivos (ejecutado 2026-11-20)
- [HECHO] "Nadie ha resuelto cómo formarla" no está en `fuentes-cifras.md` ni en el benchmark, que por el contrario registra marcos de competencias vigentes, entre ellos el de CENS (versión 2.0, junio de 2024) y el TIGER de enfermería actualizado en 2026. Fuente: entregables/2026-11-14-presentacion-vicerrector/fuentes-cifras.md y produccion/benchmark/2026-11-11-1334-marcos-competencias-salud-digital.md, líneas 59, 78 y 94 (leídos 2026-11-20)
- [HECHO] El guion hace decir en esa lámina solo "La demanda la exige la ley y la confirma el déficit de profesionales", sin la tercera parte, y su nota sobre la lámina 3 advierte de "0 de 35" y de "el único marco", pero no de esta frase. Fuente: Guion_reunion_VRA_2026-11-20.docx, lámina 3 (leído 2026-11-20)
- [HECHO] La lámina 10 dice ahora "cerca del 40% de las habilidades clave va a cambiar a competencias digitales"; la v0.3 decía "va a cambiar, y las tecnológicas son las que más crecen", y lo que consta de la fuente es solo que "cerca del 40% de las habilidades clave cambiará", por un informe que nadie abrió. Fuente: comparación propia de la lámina 10 y entregables/2026-11-14-presentacion-vicerrector/fuentes-cifras.md, línea 6 (leído 2026-11-20)
- [HECHO] El guion dice sobre esa cifra lo que la fuente respalda: "cambiará cerca del 40 % de las habilidades clave", sin "a competencias digitales". Fuente: Guion_reunion_VRA_2026-11-20.docx, tabla "Si pregunta…" (leído 2026-11-20)
- [HECHO] El título de la lámina 8 es ahora "La salud digital ya está implementada y faltan mejorar las competencias": tiene una falta de concordancia ("faltan mejorar" por "falta mejorar"), y el guion lo transcribe corregido ("falta mejorar"), de modo que el título del guion no es el de la pantalla. Fuente: lámina 8 del archivo de hoy y Guion_reunion_VRA_2026-11-20.docx, encabezado de la lámina 8 (leído 2026-11-20)
- [HIPÓTESIS] "Ya está implementada" puede jugar en contra en la lámina de cierre: si ya está implementada, el Vicerrector puede preguntar para qué un Departamento; la v0.3 decía "ya está en la USS: ahora puede liderarla". El guion lo encamina bien en voz alta ("ya está en la formación de la USS, y la propuesta es ordenarla, medirla y hacerla crecer"). Decide la titular; es su título.
- [PROPUESTA] En la lámina 3, decir lo que trae el guion y no leer el cierre de la pantalla; si preguntan por "nadie ha resuelto", responder con lo verificado: la OMS no identificó ningún grupo de competencias dedicado a IA ni ningún marco nacional de América Latina. Se apoya en las líneas anteriores y en el benchmark.

ALERTA 5. Siguen en pantalla las dos afirmaciones que van más lejos que el benchmark; el guion las corrige en voz alta, pero no en todas las láminas. [HECHO] "Ninguno de los 35 marcos… tiene [IA]" sigue en la lámina 2 y en sus notas, "0 de 35… incluyen IA" en la lámina 3 y "35 → 0 incluyen IA" en la lámina 10; "El único marco nacional de América Latina quedó fuera de la revisión" sigue en la lámina 3 y "sólo existe 1 marco nacional en América Latina que no fue considerado" en la lámina 10. Fuente: texto completo de 2026_11_20_Propuesta_Departamento_Salud_Digital_USS.pptx (leído 2026-11-20)
- [HECHO] Lo verificado sigue siendo más acotado: ninguno de los 10 grupos de competencias es de IA, el mapeo se hizo sobre 31 marcos, ningún marco nacional de los revisados es de América Latina, y el de CENS es "el único marco de competencias nacional latinoamericano encontrado" en una búsqueda con vacíos que el propio benchmark declara. Fuente: produccion/benchmark/2026-11-11-1401-marcos-competencias-verificacion-primaria.md, línea 32, y produccion/benchmark/2026-11-11-1334-marcos-competencias-salud-digital.md, líneas 106 y 115 a 118 (leídos 2026-11-20)
- [HECHO] El guion hace decir en la lámina 3 la versión verificada ("ninguno de sus grupos de competencias está dedicado a inteligencia artificial, y ningún marco nacional es de América Latina"), nombra a CENS y advierte en una nota que la lámina dice otra cosa; en la lámina 2 hace decir "un modelo de competencias en salud digital que incorpora inteligencia artificial", que también es sostenible, pero ahí no advierte que la pantalla dice "que ninguno de los 35 marcos revisados por la OMS tiene". Fuente: Guion_reunion_VRA_2026-11-20.docx, láminas 2 y 3 (leído 2026-11-20)
- [HIPÓTESIS] La lámina 2 es, según el propio guion, "la lámina más importante" y la que queda más tiempo en pantalla; es donde más probable resulta que el Vicerrector lea "ninguno de los 35". Lo confirmaría la reunión; conviene que la titular lo sepa antes.

ALERTA 6. El guion nuevo dice algunas cosas que ni el decreto v0.7 ni la presentación sostienen del todo. Ninguna es grave; las enumero porque el encargo lo pide y porque son respuestas a preguntas del Vicerrector.
- [HECHO] "¿Cómo se mide?": el guion responde que los indicadores "se definen con el Plan de Desarrollo del Departamento, una vez aprobado el decreto"; el decreto v0.7 no menciona un Plan de Desarrollo del Departamento (solo el "plan de implementación" del transitorio segundo), y la presentación lo nombra en las láminas 13, 14 y 16 como función, bajo "FUNCIONES" y no bajo "EL DECRETO DICE". Fuente: Guion_reunion_VRA_2026-11-20.docx, tabla "Si pregunta…", búsqueda de texto sobre decreto-depto-salud-digital-v0.7.docx y láminas 13, 14 y 16 del archivo de hoy (ejecutado 2026-11-20)
- [HIPÓTESIS] "Una vez aprobado el decreto" es además un compromiso de secuencia, y la titular fijó el criterio de no atarse a tiempos. Lo confirmaría ella.
- [HECHO] "¿Qué recursos pide?": el guion responde "El decreto no pide contrataciones", "horas de académicos, acordadas con su unidad de origen" y "el presupuesto es de la Facultad"; el decreto no usa las palabras "contratación", "horas" ni "presupuesto": lo que dice es que integran el Departamento académicos de otras unidades "conforme a lo acordado con su unidad de origen" (artículo 13) y que las Direcciones se instalan gradualmente (transitorio segundo); el presupuesto aparece solo en la lámina 13, como aporte de la Facultad. Fuente: búsqueda de texto sobre decreto-depto-salud-digital-v0.7.docx, artículo 13 y transitorio segundo, y lámina 13 del archivo de hoy (ejecutado 2026-11-20)
- [HIPÓTESIS] "No pide contrataciones" es cierto en la letra, pero el decreto crea siete cargos de Director o Directora; si el Vicerrector lo hace notar, la respuesta honesta es la de los transitorios (instalación gradual y funciones ejercidas por la Dirección Nacional), que el guion ya trae en la pregunta siguiente. Lo confirmaría la titular, que según el perfil ya conversó dotación y horas en el Consejo de Facultad.
- [HECHO] "¿En qué va el decreto?": el guion responde "se ha ajustado con las observaciones de la Decana", que corrige la frase del guion v0.1 ("con sus observaciones", por el Consejo de Facultad) y que sí consta para la v0.6; pero el último ajuste, el nombre "Dirección de Investigación" de la v0.7, no consta que venga de la Decana ni que ella lo conozca. Fuente: Guion_reunion_VRA_2026-11-20.docx, tabla "Si pregunta…", y registro del decreto de hoy en produccion/guia/, alerta 1 (leído 2026-11-20)
- [HECHO] Lámina 8: el guion hace afirmar "La ruta del decreto sigue el precedente del Departamento Nacional de Salud Pública"; nadie en este sistema ha abierto el Decreto de Rectoría 116, las notas de la lámina 8 siguen diciendo "falta confirmar el paso por Secretaría General", y esa salvedad ya no está en la pantalla (la titular la quitó) ni en el guion. Fuente: Guion_reunion_VRA_2026-11-20.docx, lámina 8, notas de la lámina 8 del archivo de hoy y entregables/2026-11-14-decreto/revision-articulo-por-articulo.md, línea 18 (leído 2026-11-20)
- [PROPUESTA] Si el Vicerrector pregunta por la ruta, decir que es la que se entiende del precedente y que el paso por Secretaría General está por confirmar; él es quien mejor puede confirmarla. Se apoya en la línea anterior.
- [HECHO] "¿Qué necesita de la Vicerrectoría?": el guion pide "sumar las competencias digitales al seguimiento de egresados"; en el guion v0.1 iba marcado como "[propuesta]" y ahora no; no hay indicador con respaldo del benchmark y `produccion/brechas-indicadores/` sigue vacía. Fuente: Guion_reunion_VRA_2026-11-20.docx y Guion_VRA_ejecutiva_v0.1.pdf, tablas "Si pregunta…", y listado de produccion/ (revisado 2026-11-20)
- [HECHO] "¿Por qué un Departamento?": el guion cita lo que el Reglamento de Unidades Académicas "define"; eso sale del visto 5 del decreto, y nadie en este sistema ha abierto el Reglamento. Fuente: Guion_reunion_VRA_2026-11-20.docx, tabla "Si pregunta…", y visto 5 de decreto-depto-salud-digital-v0.7.docx (leído 2026-11-20)
- [HECHO] Lámina 5: el guion hace decir "un electivo de salud con ingeniería", que es lo que muestra la imagen; la titular quitó "en especial la ingeniería y el derecho" de los artículos 2 y 9 del decreto por un motivo que sigue sin constar, y la lámina 12 conserva "ingeniería, derecho y otras". Fuente: Guion_reunion_VRA_2026-11-20.docx, lámina 5, lámina 12 del archivo de hoy y registro del decreto de hoy en produccion/guia/ (leído 2026-11-20)
- [HECHO] Lámina 3: el guion dice que el modelo de CENS "es nuestra referencia local"; lo que la titular dijo es que su modelo "no compite con el de CENS: lo complementa" y que "CENS será citado". Fuente: Guion_reunion_VRA_2026-11-20.docx, lámina 3, y perfil/cargo.md, línea 35 (leído 2026-11-20)
- [HIPÓTESIS] "Referencia local" y "lo complementa" no se contradicen, pero la primera es redacción de la sesión principal; si la titular prefiere su propia fórmula, es "lo complementamos". Lo confirmaría ella.

ALERTA 7. Las fichas del anexo siguen poniendo bajo "EL DECRETO DICE" cosas que el decreto no dice; el cambio de nombre del decreto resolvió una parte. [HECHO] Resuelto por la v0.7: la lámina 15 (el artículo 10 establece "Dirección de Docencia y Dirección de Investigación") y el título de la lámina 19 ("Dirección de Investigación · RESPALDO · ARTÍCULO 10") ahora coinciden con el decreto. Fuente: láminas 15 y 19 del archivo de hoy contra los artículos 7 y 10 de decreto-depto-salud-digital-v0.7.docx (leído 2026-11-20)
- [HECHO] Resuelto por la titular: la lámina 6 ya no tiene la línea "Responde al artículo 3: un marco común de desempeños sustentado en… los estándares nacionales e internacionales", que no calzaba con el artículo 3 b). Fuente: comparación propia de la lámina 6 en ambos archivos (ejecutado 2026-11-20)
- [HECHO] Sigue: la lámina 19 pone bajo "EL DECRETO DICE" que la Dirección gestiona "la investigación, la vinculación con el medio y el desarrollo de proyectos del Departamento, en alineación de la Decanatura y con las Vicerrectorías"; el artículo 10 de la v0.7 dice "la gestión de las líneas y los proyectos del Departamento en esas materias, en coordinación con las Vicerrectorías y unidades institucionales competentes", sin Decanatura y sin "alineación". Fuente: lámina 19 del archivo de hoy contra el artículo 10 de la v0.7 (leído 2026-11-20)
- [HECHO] Siguen: la lámina 17 resume el artículo 9 sin "instancia de articulación interna" ni la consolidación de "la información y los indicadores"; la lámina 20 resume el artículo 11 sin "mantener la relación con las carreras" ni "la realidad y la identidad de cada sede"; la lámina 16 lista bajo "FUNCIONES" el Plan de Desarrollo, las horas, los convenios y la cuenta anual, que no están en el decreto; y las notas de la lámina 11 citan el artículo 1 sin "la gobernanza de la salud digital". Fuente: láminas 11, 16, 17 y 20 del archivo de hoy contra los artículos 1, 8, 9 y 11 de la v0.7 (leído 2026-11-20)
- [HECHO] El guion nuevo ya no manda a las notas de la lámina 11 para definir la salud digital: da la primera frase del artículo 1, que es exacta. Fuente: Guion_reunion_VRA_2026-11-20.docx, tabla "Si pregunta…", contra el artículo 1 de la v0.7 (leído 2026-11-20)

ALERTA 8. Siguen los dos nombres para el plan de la Facultad. [HECHO] Las láminas 2 (notas) y 4 citan el "Plan de Desarrollo de la Facultad 2022–2029 (p. 13)" y el visto 1 de la v0.7, que no se tocó, cita el "Plan Estratégico de la Facultad de Ciencias para el Cuidado de la Salud 2025–2029"; el guion nuevo esquiva el problema diciendo "su plan de desarrollo", sin años. Fuente: láminas 2 y 4 del archivo de hoy, visto 1 de decreto-depto-salud-digital-v0.7.docx y Guion_reunion_VRA_2026-11-20.docx, lámina 4 (leído 2026-11-20)
- [HIPÓTESIS] Son dos documentos distintos y ambos nombres son correctos; sigue sin confirmarse porque ninguno está en el repositorio. Lo confirmaría la titular.

ALERTA 9. Restos y detalles que siguen o aparecen en el archivo de hoy. Ninguno es grave por separado.
- [HECHO] Dentro de la presentación conviven ahora dos palabras para lo mismo: la lámina 2 dice "Oportunidades" (antes "GANANCIA") y la lámina 8 conserva "LO QUE GANA LA USS"; además, "LA VENTAJA DE LA USS" (lámina 4) y las notas de la lámina 2 ("Cada ganancia se apoya…") quedaron con el vocabulario anterior. Fuente: láminas 2, 4 y 8 y notas de la lámina 2 del archivo de hoy (leído 2026-11-20)
- [HECHO] El título de la lámina 6 ya no dice "cada semestre" ("Un modelo de competencias medido"), pero el cuerpo lo conserva en dos lugares ("Un modelo de competencias, medido cada semestre" y "en los estudiantes, cada semestre"); el guion lo advierte y ofrece decir "periódicamente". Fuente: lámina 6 del archivo de hoy y Guion_reunion_VRA_2026-11-20.docx, lámina 6 (leído 2026-11-20)
- [HECHO] La lámina 5 se titula ahora "Track de Salud Digital"; la palabra "Track" no aparece en el decreto, en el resto de la presentación ni en lo que el guion hace decir, y el rótulo de la misma lámina sigue siendo "CICLO DE FORMACIÓN Y EMPLEABILIDAD". Fuente: búsqueda de "Track" en el archivo de hoy, en decreto-depto-salud-digital-v0.7.docx y en Guion_reunion_VRA_2026-11-20.docx (ejecutado 2026-11-20)
- [HIPÓTESIS] "Track" puede entenderse como una mención o ruta curricular para estudiantes, que no es lo que muestra la figura (el ciclo de trabajo del Departamento). Lo confirmaría la titular, que eligió el título.
- [HECHO] Siguen de la v0.3: "ingeniería, derecho y otras" (lámina 12); la nota de diseño a la vista en la lámina 13 ("Sirve como lámina de entrada antes del flujo"); "centro de costos (en evaluación)" (lámina 14); en la lámina 10, "35 → 0 incluyen IA / marcos de competencias en salud digital revisó la OMS" y "Profesionales" con mayúscula; y "en alineación de la Decanatura" (lámina 19). Fuente: texto completo del archivo de hoy (leído 2026-11-20)
- [HECHO] Resueltos frente a la v0.3: la errata "profesionales.Y" de la lámina 3 (la frase fue reemplazada), "El paso por Secretaría General está por confirmar" en la pantalla de la lámina 8 (sigue en las notas), la palabra "liviana" del título de la lámina 7 y las cuatro láminas ocultas. Fuente: comparación propia de los dos archivos (ejecutado 2026-11-20)
- [HECHO] En la portada, el nombre de la titular y "Noviembre de 2026" están en el mismo cuadro separados por un salto de línea; no es una errata. Fuente: ppt/slides/slide1.xml del archivo de hoy (leído 2026-11-20)

ALERTA 10. Documentos que quedaron desactualizados frente a los de hoy. [HECHO] `Presentacion_VRA_ejecutiva_v0.3.pptx` y `Guion_VRA_ejecutiva_v0.1.pdf` siguen en la misma carpeta que los archivos de hoy: el guion v0.1 tiene los títulos antiguos, "fuente de ingresos" y "con sus observaciones", y no debe usarse. Fuente: listado de entregables/2026-11-20-presentacion-vra-ejecutiva/ y Guion_VRA_ejecutiva_v0.1.pdf (leído 2026-11-20)
- [HECHO] Hay dos archivos llamados `generar_guion.py`, uno en `entregables/2026-11-15-guia-reunion-vicerrector/` (guion de la v0.4) y otro en `entregables/2026-11-20-presentacion-vra-ejecutiva/` (guion de hoy); el de hoy recibe la ruta de salida como argumento y no sobrescribe nada por sí solo. Fuente: listado de entregables/ y entregables/2026-11-20-presentacion-vra-ejecutiva/generar_guion.py (leído 2026-11-20)
- [HECHO] Siguen desactualizados, como ya constaba: la presentación generada del 2026-11-15 y su generador, la guía y el guion del 2026-11-15, `fuentes-cifras.md` (no cubre PDI, FODA, leyes ni las frases nuevas de hoy) y `perfil/cargo.md` ("Área de Proyectos", "Coordinaciones de Sede"). Fuente: registro anterior, alerta 10, y git log sin cambios en esas rutas (revisado 2026-11-20)

## Coherencia entre el decreto v0.7, la presentación de hoy y el guion de hoy

| Tema | Decreto v0.7 (`d6cc1312e4a5`) | Presentación de hoy (`2d3da8bb6107`) | Guion de hoy (`d4c419aca308`) | Estado |
|---|---|---|---|---|
| Dirección Nacional | "Director o Directora Nacional" (art. 8) | Igual | "Una Dirección Nacional, que depende del Decanato" | Calza |
| Primera Dirección de área | "Dirección de Docencia" (arts. 7 y 10) | Igual en texto; "Área de Docencia" en la imagen de la lámina 7 | "la de Docencia" | Calza, salvo la imagen |
| Segunda Dirección de área | "Dirección de Investigación" (arts. 7 y 10) | "Dirección de Investigación" (13 veces); "Área de Investigación" en la imagen | "Dirección de Investigación" | Calza, salvo la imagen. Antes no calzaba |
| Frentes de la segunda Dirección | Tres: línea basal, investigación, vinculación con el medio (art. 10) | Tres en las láminas 14 y 19; cuatro en la imagen de la lámina 7 (suma "proyectos") | No los enumera | No calza la imagen |
| Genérico | "las Direcciones de área" (art. 7) | Igual; "áreas" en la imagen | "Direcciones de área" | Calza, salvo la imagen |
| Sedes | "Direcciones de Sede" (art. 11) | Igual | "una Dirección de Sede en Santiago, Concepción, Valdivia y Puerto Montt" | Calza |
| Comité | "Comité Consultivo", ordinario o ampliado, articulación interna e indicadores (art. 9) | Nombre igual; ficha sin articulación ni indicadores | "Comité Consultivo, ordinario o ampliado" | Calza el nombre; ficha incompleta |
| Transitorios | Dos: funciones por la Dirección Nacional mientras no haya Direcciones de área; instalación gradual | "Más dos artículos transitorios, que ordenan la instalación gradual" (lámina 15) | "La instalación es gradual"; respuesta a "¿Siete Direcciones?" con ambos transitorios | Calza |
| Lo que la ficha pone bajo "EL DECRETO DICE" | Arts. 8 a 11 | Láminas 16 y 18 fieles; 17 y 20 incompletas; 19 con "en alineación de la Decanatura" | No cita las fichas | No calza la lámina 19 |
| Marco de desempeños | "estándares internacionales" (art. 3 b) | La línea que decía "nacionales e internacionales" fue eliminada | No lo cita | Ya no hay desajuste |
| Definición de salud digital | Art. 1, con "la gobernanza de la salud digital" | Notas de la lámina 11, sin la gobernanza | Primera frase del art. 1, exacta | Calza el guion; notas desactualizadas |
| Plan de la Facultad | "Plan Estratégico… 2025–2029" (visto 1) | "Plan de Desarrollo de la Facultad 2022–2029" | "su plan de desarrollo" | Sin resolver |
| Leyes | 21.541, 21.668 y 21.719 (visto 7) | Las mismas (lámina 3) | Las mismas, por materia | Calza |
| Ingeniería y derecho | Quitados de los arts. 2 y 9 | "ingeniería, derecho y otras" (lámina 12); "electivo de salud con ingeniería" (imagen de la lámina 5) | "un electivo de salud con ingeniería" | Resto en la presentación y en el guion |
| Plan de Desarrollo del Departamento | No existe en el decreto | Láminas 13, 14 y 16 | "Se definen con el Plan de Desarrollo del Departamento" | Solo lo sostiene la presentación |
| Recursos | Art. 13 ("lo acordado con su unidad de origen") y transitorio segundo | "presupuesto" como aporte de la Facultad (lámina 13); "acuerda horas" (lámina 16) | "no pide contrataciones… presupuesto de la Facultad" | Parcial: el decreto no habla de presupuesto ni de contrataciones |

- [HECHO] La tabla anterior resume el cotejo que hice del texto completo de los tres documentos. Fuente: decreto-depto-salud-digital-v0.7.docx, 2026_11_20_Propuesta_Departamento_Salud_Digital_USS.pptx y Guion_reunion_VRA_2026-11-20.docx (leídos 2026-11-20)

## Guion de hoy contra la presentación de hoy, lámina por lámina

| Lámina | Título en pantalla | Lo que hace decir el guion | Calza |
|---|---|---|---|
| 1 | "Departamento Nacional de Salud Digital" · "Propuesta para la Vicerrectoría Académica" | Saludo; "qué oportunidades abre… y después cómo se organiza" | Sí |
| 2 | "La Salud Digital como oportunidad en la USS" | "Cinco oportunidades", en el orden de la lámina; "incorpora inteligencia artificial" | Sí; la pantalla dice además "que ninguno de los 35 marcos… tiene" (alerta 5) |
| 3 | "Digitalización de la salud y demanda de profesionales" | Tres leyes; OPS con la formulación de la fuente ("las Américas", "podrían faltar", "trabajadores de salud"); OMS con la formulación verificada; CENS | Título sí; lo dicho difiere de la pantalla a propósito, con nota; el cierre de la pantalla ("nadie ha resuelto cómo formarla") no se dice ni se advierte (alerta 4) |
| 4 | "La USS tiene la base para impulsar la iniciativa" | 1.788 estudiantes, 31 secciones, cuatro carreras, cuatro sedes; plan de la Facultad; falta medir | Sí |
| 5 | "Track de Salud Digital" (imagen sin cambios) | Recorre la figura: necesidades, lectura, áreas y benchmarking en paralelo, propuestas, competencias, empleabilidad | Sí con la imagen; el guion no usa la palabra "Track" |
| 6 | "Un modelo de competencias medido" | 35 marcos, 10 grupos; adaptar, medir, analizar, ajustar; "la gestiona la Dirección de Investigación" | Sí; omite "cada semestre" a propósito, con nota |
| 7 | "Estructura sobre capacidades que ya existen" (imagen sin cambios) | Tres niveles; "Dos Direcciones de área, la de Docencia y la de Investigación" | La imagen dice "Área"; el guion lo advierte (alerta 3) |
| 8 | "La salud digital ya está implementada y faltan mejorar las competencias" | Resumen, ruta del decreto y la pregunta de cierre | El guion escribe "falta" donde la pantalla dice "faltan"; no nombra las cinco ganancias que la lámina lista |
| 9 a 20 | Anexo | Tabla "Si pregunta…" remite a las láminas 6, 8, 10, 11, 13, 14, 15 y 16 | Sí: cada remisión lleva a una lámina que trata el tema; las láminas 12 y 17 a 20 quedan sin pregunta que lleve a ellas |

- [HECHO] Los tiempos del guion suman 5 minutos y 15 segundos (15 + 60 + 45 + 45 + 40 + 40 + 30 + 40 segundos) y se presenta como "unos 5 minutos"; declara que las láminas 1 a 8 son la exposición y de la 9 a la 20 el anexo, lo que coincide con el archivo. Fuente: suma propia sobre Guion_reunion_VRA_2026-11-20.docx y recorrido de las láminas del archivo de hoy (ejecutado 2026-11-20)
- [HECHO] La segunda línea del guion nombra el archivo correcto ("2026_11_20_Propuesta_Departamento_Salud_Digital_USS.pptx"), lo que resuelve la alerta 6 del registro anterior (el guion v0.1 declaraba corresponder a la presentación v0.1). Fuente: Guion_reunion_VRA_2026-11-20.docx, párrafo 3 (leído 2026-11-20)
- [HECHO] Comprobé las decisiones que la sesión principal declaró: el guion nombra a CENS (lámina 3 y dos respuestas), no afirma nada sobre "fuente de ingresos" (solo el cuidado de no afirmarlo), no menciona el doctorado ni la autoría de la línea salvo para decir que no van hoy, no cita la Estrategia Nacional de Salud y agrega la pregunta "¿Siete Direcciones no es mucho?". Fuente: lectura completa de Guion_reunion_VRA_2026-11-20.docx (leído 2026-11-20)
- [HECHO] Las cifras que el guion hace decir calzan con `fuentes-cifras.md`: OPS, "entre 600 mil y 2 millones de trabajadores de salud" en "las Américas", "podrían faltar"; CENS, "al menos 3.500"; Foro Económico Mundial, 170 millones y cerca del 40 %; Blackboard, 1.788 estudiantes en 31 secciones. Fuente: Guion_reunion_VRA_2026-11-20.docx contra entregables/2026-11-14-presentacion-vicerrector/fuentes-cifras.md, líneas 5 a 8 (leído 2026-11-20)
- [HECHO] En la pantalla, en cambio, las láminas 3 y 10 siguen diciendo "profesionales de la salud que faltarán en América… si no hay intervenciones" y "3.500" sin "al menos": el guion dice la versión de la fuente y la lámina otra. Fuente: láminas 3 y 10 del archivo de hoy (leído 2026-11-20)

## Qué cambió

"Encargo" es el relato de la sesión principal al encargarme este registro (recibido 2026-11-20), que cita la conversación con la titular de hoy. "Comparación" es el comparador más mi extracción completa del texto.

### Presentación: ejecutiva v0.3 → archivo del 2026-11-20. Aplicó: la titular (el archivo es suyo)

- [HECHO] La titular dijo que los títulos de la v0.3 "están malísimos" y que prefiere "los que eran a la antigua, sin IA, como muy pragmático"; la sesión principal le propuso títulos sobrios en el chat, pero los del archivo son de ella y no los propuestos. Fuente: encargo de la sesión principal al Guía, que cita a la titular del cargo (conversación 2026-11-20; recibido 2026-11-20)
- [HECHO] El encargo menciona títulos nuevos en las láminas 2 a 8 y que ya no hay láminas ocultas; la comparación muestra además seis cambios que el encargo no menciona: la portada, los rótulos de la lámina 2, el cierre de la lámina 3, la línea eliminada de la lámina 6, la línea eliminada de la lámina 8 y la tarjeta 1 de la lámina 10. Fuente: comparación propia de los dos archivos contra el encargo de la sesión principal (ejecutado 2026-11-20)

| Lámina | Qué decía (v0.3) | Qué dice (2026-11-20) | Quién lo sugirió | Por qué | Consta en |
|---|---|---|---|---|---|
| 1 | "Salud digital: una oportunidad que la USS puede liderar" · "Propuesta para la Vicerrectoría Académica · noviembre de 2026" · nombre de la titular | Sin esa bajada; "Propuesta para la Vicerrectoría Académica"; nombre de la titular y, debajo, "Noviembre de 2026" | No consta (archivo de la titular; el encargo no lo menciona) | No consta | Comparación |
| 2 | Título "Lo que gana la USS con la salud digital"; rótulo "LA PROPUESTA EN UNA LÁMINA"; columna "GANANCIA" | Título "La Salud Digital como oportunidad en la USS"; sin ese rótulo; columna "Oportunidades" | Título: titular. Rótulos: no consta | Títulos "a la antigua, sin IA, como muy pragmático" | Encargo; comparación |
| 3 | Título "La salud se digitaliza y faltan profesionales"; cierre "…la exige la ley y la confirma el déficit de profesionales.Y los marcos que revisó la OMS aún no incluyen IA." | Título "Digitalización de la salud y demanda de profesionales"; cierre "…la exige la ley, la confirma el déficit de profesionales y nadie ha resuelto cómo formarla." | Título: titular. Cierre: no consta | Título: ídem. Cierre: no consta | Encargo; comparación |
| 4 | "La USS ya partió: tiene la base para liderar" | "La USS tiene la base para impulsar la iniciativa" | Titular | Ídem | Encargo; comparación |
| 5 | "Leemos el mundo laboral y lo convertimos en formación" | "Track de Salud Digital" (imagen sin cambios) | Titular | Ídem | Encargo; comparación; suma de verificación de la imagen |
| 6 | Título "Un modelo propio de competencias, medido cada semestre"; línea "Responde al artículo 3: un marco común de desempeños sustentado en la investigación del Departamento y en los estándares nacionales e internacionales." | Título "Un modelo de competencias medido"; esa línea, eliminada | Título: titular. Línea eliminada: no consta | Título: ídem. Línea: no consta; el Guía había alertado que "nacionales e" no calzaba con el artículo 3 b) | Encargo; registro anterior, alerta 4; comparación |
| 7 | "Una estructura liviana sobre capacidades que ya existen" | "Estructura sobre capacidades que ya existen" (imagen sin cambios) | Titular | Ídem; la sesión principal había observado "estructura liviana" frente a siete Direcciones | Encargo; registro anterior; comparación |
| 8 | Título "La salud digital ya está en la USS: ahora puede liderarla"; línea "El paso por Secretaría General está por confirmar." | Título "La salud digital ya está implementada y faltan mejorar las competencias"; esa línea, eliminada de la pantalla (sigue en las notas) | Título: titular. Línea eliminada: no consta | Título: ídem. Línea: no consta; el Guía la había señalado como pendiente interno a la vista | Encargo; registro anterior, alerta 9; comparación |
| 10 | "…cerca del 40% de las habilidades clave va a cambiar, y las tecnológicas son las que más crecen." | "…cerca del 40% de las habilidades clave va a cambiar a competencias digitales." | No consta | No consta; el Guía había señalado que "las tecnológicas son las que más crecen" no tenía respaldo | Registro anterior, tabla de cifras; comparación |
| 21 a 24 | Cuatro láminas ocultas ("Cómo se articula", "Ámbito operativo", "Qué dice el decreto actualmente" y una sin título) | Eliminadas | No consta (archivo de la titular) | No consta; el Guía había alertado que viajaban con el archivo | Registro anterior, alertas 3 y 9; comparación |
| 5 y 7 (imágenes), notas del orador, comentarios | — | Sin cambios | — | — | Sumas de verificación; comparación |

- [HIPÓTESIS] Las eliminaciones de las láminas 6 y 8 y de las ocultas responden a mis alertas de las 00:26, que la sesión principal debía transmitir completas; nadie me lo confirmó. Lo confirmaría la titular o la sesión principal.

### Guion: v0.1 (PDF, autor no consta) → guion del 2026-11-20. Escribió: la sesión principal, a pedido de la titular

- [HECHO] La titular pidió un "guion ajustado a la presentación"; la sesión principal lo escribió hoy sobre la estructura del guion v0.1, con `generar_guion.py`, y lo dejó en Word y PDF. Fuente: encargo de la sesión principal al Guía, que cita a la titular del cargo (conversación 2026-11-20; recibido 2026-11-20), y entregables/2026-11-20-presentacion-vra-ejecutiva/generar_guion.py (leído 2026-11-20)

| Lugar | Qué decía (guion v0.1) | Qué dice (guion de hoy) | Quién lo sugirió | Por qué | Consta en |
|---|---|---|---|---|---|
| Encabezado | "Presentacion_VRA_ejecutiva_v0.1.pptx" | "2026_11_20_Propuesta_Departamento_Salud_Digital_USS.pptx" | Titular (guion ajustado a la presentación) | Corresponder al archivo que se presenta | Encargo; lectura |
| Títulos de las láminas 2 a 8 | Los de la v0.3 | Los del archivo de hoy (en la 8, "falta" por "faltan") | Titular (títulos); sesión principal (transcripción) | Ídem | Lectura |
| Lámina 2 | "ganancias" | "oportunidades" | Sesión principal, siguiendo la lámina | Ídem | Lectura |
| Lámina 3 | "ninguno de los 35 marcos incluye IA"; "el único marco nacional de América Latina"; sin CENS como marco | "ninguno de sus grupos de competencias está dedicado a inteligencia artificial, y ningún marco nacional es de América Latina. En Chile existe el modelo de CENS"; nota de que la lámina dice otra cosa | Sesión principal, sobre la alerta 5 del Guía | Usar en voz alta lo que respalda la fuente | Encargo; registro anterior, alerta 5 |
| Lámina 3, OPS | "profesionales… que faltarán en América" | "en las Américas podrían faltar entre 600 mil y 2 millones de trabajadores de salud" | Sesión principal | Formulación de la fuente | Encargo; `fuentes-cifras.md` |
| Lámina 6 | "medido cada semestre" | Sin frecuencia; nota: "si no quieres comprometer la frecuencia, di «periódicamente»" | Sesión principal, sobre su propia observación del 2026-11-19 | No comprometer frecuencia | Registro anterior; lectura |
| Lámina 7 | "la Dirección de Docencia y la Dirección de Investigación", sin advertir la imagen | Igual, más la nota sobre los recuadros "Área" | Sesión principal, sobre la alerta 2 del Guía | Que lo dicho calce con el decreto | Registro anterior, alerta 2; lectura |
| Vocabulario | Recordatorio de nombres | Agrega "El decreto v0.7 usa estas mismas palabras" | Sesión principal | El decreto se alineó hoy | Lectura; registro del decreto de hoy |
| "¿En qué va el decreto?" | "se ha ajustado con sus observaciones" (del Consejo de Facultad) | "se ha ajustado con las observaciones de la Decana" | Sesión principal, sobre la alerta 7 del Guía | No atribuir observaciones al Consejo | Registro anterior, alerta 7 |
| "¿Qué recursos pide?" | Incluía "abre una fuente de ingresos" | Sin ingresos; cuidado aparte: "no afirmes nada que no esté confirmado con la Decana" | Sesión principal, sobre la alerta 7 del Guía | No estaba en la presentación ni en el decreto | Encargo; registro anterior, alerta 7 |
| "¿Siete Direcciones no es mucho?" | No existía | Respuesta con los dos transitorios | Sesión principal, sobre una propuesta del Guía | El Vicerrector puede contar las Direcciones | Encargo; registro anterior, sección de cifras |
| "¿Cómo se mide?" | "Indicadores de competencias digitales en salud cada semestre, por sede, carrera y cohorte, y la empleabilidad medida también en salud digital" | "Con indicadores de competencias digitales en salud por sede, carrera y cohorte. Se definen con el Plan de Desarrollo del Departamento, una vez aprobado el decreto" | Sesión principal | Quitar la frecuencia; el resto no consta | Lectura de ambos guiones |
| "¿Por qué un Departamento?" | "Para que la salud digital tenga una unidad de referencia nacional que la conduzca en las cuatro sedes: formación equivalente, medición cada semestre, nueva oferta e investigación… (artículo 1)" | "Porque el Reglamento de Unidades Académicas define al Departamento como la unidad transversal a carreras de distintas Facultades…" | Sesión principal | No consta | Lectura de ambos guiones |
| "¿Qué necesita de la Vicerrectoría?" | "[propuesta] Respaldo a la propuesta en su paso por las instancias, y sumar las competencias digitales al seguimiento de egresados" | "Su mirada sobre el texto antes de que siga a las instancias, y sumar las competencias digitales al seguimiento de egresados", sin la marca "[propuesta]" | Sesión principal | No consta | Lectura de ambos guiones |
| Cuidados | No existían | PDF y no PowerPoint; ingresos; doctorado y autoría "no van hoy: primero el decreto" | Sesión principal; lo del doctorado sigue lo dicho por la titular ("primero que salga el decreto") | Alertas 3 y 7 del Guía | Encargo; registro anterior |

## Qué quedó resuelto y qué sigue del registro anterior (00:26)

| Alerta del registro anterior | Estado ahora | Cómo lo comprobé |
|---|---|---|
| 1. "Dirección de Investigación" contra "Dirección de Proyectos" del decreto | Resuelta entre documentos: el decreto v0.7 dice "Dirección de Investigación". Sigue abierto quién decidió el nombre y si la Decana lo sabe | Comparador sobre el decreto; conteo: 13 veces en la presentación, 2 en el decreto |
| 2. Lámina 7 con "Áreas" | Sigue en pantalla (misma imagen); el guion lo advierte | Suma de verificación e imagen |
| 3. Comentarios incrustados, notas y láminas ocultas | Comentarios y notas siguen; láminas ocultas eliminadas; el guion pide enviar PDF | Estructura interna del archivo |
| 4. Fichas "EL DECRETO DICE" | Láminas 15 y 19 (nombre) resueltas por la v0.7; línea de la lámina 6 eliminada; siguen la 19 ("Decanatura"), la 17, la 20, la 16 y las notas de la 11 | Lectura contra la v0.7 |
| 5. "0 de 35" y "el único marco" | Siguen en las láminas 2, 3 y 10; el guion dice la versión verificada y nombra a CENS | Lectura |
| 6. El guion declaraba corresponder a la v0.1 | Resuelta: el guion nuevo nombra el archivo de hoy | Lectura |
| 7. "Con sus observaciones", "fuente de ingresos", ruta según el DR 116 | Las dos primeras, resueltas en el guion nuevo; la ruta sigue sin respaldo y ahora sin la salvedad en pantalla | Lectura |
| 8. Dos nombres para el plan de la Facultad | Sigue | Lectura |
| 9. Restos y notas internas a la vista | Resueltos: errata de la lámina 3, línea de Secretaría General, ocultas. Siguen: láminas 10, 12, 13, 14 y 19 | Comparación |
| 10. Otros documentos desactualizados | Sigue; se suman la v0.3 y el guion v0.1 como históricos | Listado |
| Cinco observaciones de la sesión principal del 2026-11-19 | Nombre: resuelto vía decreto. "0 de 35" y "el único": resuelto en la voz, no en la pantalla. "Cada semestre": fuera del título, sigue en el cuerpo. Plan 2022–2029: sigue. "Estructura liviana": resuelto en el título y con pregunta preparada | Lectura |

- [HECHO] La tabla anterior resume mi cotejo de cada alerta del registro anterior contra los archivos de hoy. Fuente: produccion/guia/2026-11-20-0026-registro-presentacion-vra.md, 2026_11_20_Propuesta_Departamento_Salud_Digital_USS.pptx, Guion_reunion_VRA_2026-11-20.docx y decreto-depto-salud-digital-v0.7.docx (leídos 2026-11-20)

## Estado

- [HECHO] Presentación vigente: `entregables/2026-11-20-presentacion-vra-ejecutiva/2026_11_20_Propuesta_Departamento_Salud_Digital_USS.pptx`, sin número de versión, huella `2d3da8bb6107`, 434 párrafos y 2483 palabras según el comparador, 20 láminas (1 a 8 exposición, 9 a 20 anexo), ninguna oculta, con tres comentarios incrustados y notas en las láminas 2, 3, 4, 8 y 11. Fuente: scripts/comparar_versiones.py y estructura interna del archivo (ejecutado 2026-11-20)
- [HECHO] Guion vigente: `entregables/2026-11-20-presentacion-vra-ejecutiva/Guion_reunion_VRA_2026-11-20.docx`, huella `d4c419aca308`, y su PDF de 3 páginas, huella `4ec1999c69ff`, con el mismo texto. Fuente: scripts/comparar_versiones.py, pdfinfo y cotejo Word-PDF (ejecutado 2026-11-20)
- [HECHO] Si la titular entrega una presentación o un guion con otra huella, corresponde alerta; la huella no cubre imágenes, grupos ni comentarios, de modo que un cambio solo en la imagen de la lámina 7 no la movería y habría que mirarla de nuevo. Fuente: scripts/comparar_versiones.py (leído 2026-11-20)
- [HECHO] No hay indicadores fijados ni actas: este es un registro de versiones. Fuente: listado de produccion/guia/ y produccion/actas/ (revisado 2026-11-20)

### Pendientes de la titular, para hoy antes de la reunión

- [PROPUESTA] En la lámina 3, no leer el cierre "nadie ha resuelto cómo formarla"; en la 2, saber que la pantalla dice "ninguno de los 35 marcos… tiene". Se apoya en las alertas 4 y 5.
- [PROPUESTA] En la lámina 7, decir "Direcciones" aunque el dibujo diga "Áreas", como indica el guion. Se apoya en la alerta 3.
- [PROPUESTA] En la lámina 8 y si preguntan por la ruta, no darla por confirmada: falta el paso por Secretaría General y nadie abrió el decreto del precedente. Se apoya en la alerta 6.
- [PROPUESTA] Decidir si dirá "se definen con el Plan de Desarrollo del Departamento, una vez aprobado el decreto" y "el decreto no pide contrataciones", sabiendo que el decreto no menciona ese Plan y sí crea siete cargos de dirección de instalación gradual. Se apoya en la alerta 6.
- [PROPUESTA] No enviar el .pptx; PDF sin notas. Se apoya en la alerta 2.
- [PROPUESTA] No convertir hoy "empleabilidad medida en salud digital" ni "indicadores por sede" en un compromiso con cifra o fecha: no hay indicador con respaldo del benchmark. Se apoya en la regla 2 del sistema y en que `produccion/brechas-indicadores/` sigue vacía.

### Pendientes de la titular, después de la reunión

- [PROPUESTA] Decir quién decidió "Dirección de Investigación" y si la Decana lo sabe. Se apoya en la alerta 1 del registro del decreto de hoy.
- [PROPUESTA] Confirmar si los cambios que no son títulos (cierre de la lámina 3, tarjeta 1 de la lámina 10, líneas eliminadas de las láminas 6 y 8, portada, láminas ocultas) los hizo ella y por qué, para cerrar las celdas "no consta". Se apoya en la tabla de cambios.
- [PROPUESTA] Contar qué dijo el Vicerrector, lámina por lámina si puede, para registrarlo como origen de los cambios que vengan. Se apoya en que todavía no hay ninguna entrada suya en la columna "quién lo sugirió".
- [PROPUESTA] Siguen abiertos del registro anterior: quién redactó la ejecutiva y el guion v0.1 y si existen la v0.1 y la v0.2; qué era "el aporte de Manuel" sobre el organigrama; si los dos planes de la Facultad son dos documentos; y rehacer la imagen de la lámina 7 con "Dirección" y tres frentes. Se apoya en que ninguno consta como respondido.

### Pendientes de la sesión principal

- [PROPUESTA] Transmitir a la titular estas alertas completas y, en particular, las dos que el guion no cubre: el cierre de la lámina 3 y "ninguno de los 35" en la lámina 2. Se apoya en las alertas 4 y 5.
- [PROPUESTA] Confirmarme si la titular vio las alertas de las 00:26 antes de editar el archivo de hoy, para atribuir las eliminaciones. Se apoya en la hipótesis de la tabla de cambios.
- [PROPUESTA] Actualizar `fuentes-cifras.md` con lo que la presentación agregó (PDI, FODA, leyes, Estrategia Nacional de Salud) o declararlo no verificado, y anotar que "a competencias digitales" y "nadie ha resuelto cómo formarla" no tienen fuente. Se apoya en las alertas 4 y 10.

### Encargos que sugiero a otros agentes

- [PROPUESTA] Siguen los dos del registro anterior: al Benchmark, verificar marco por marco los 35 de la OMS y buscar marcos nacionales en Brasil, Argentina, Uruguay y Colombia; a Brechas e indicadores, con respaldo del Benchmark, un indicador de competencias digitales y uno de empleabilidad en salud digital antes de que la presentación los prometa con meta. Se apoya en la alerta 5 y en la regla 2 del sistema.

# Registro anterior (2026-11-20, 00:26), copiado íntegro

Lo que sigue es el texto de `produccion/guia/2026-11-20-0026-registro-presentacion-vra.md` tal como se escribió. Donde dice "decreto vigente" se refiere a la v0.6, que decía "Dirección de Proyectos"; donde dice "versión vigente" de la presentación se refiere a la v0.3. El estado actual de cada alerta está en la tabla "Qué quedó resuelto y qué sigue", más arriba.

# Registro de versiones: presentación para la Vicerrectoría Académica y su guion

Este es el primer registro de la presentación: no hay un registro anterior de este documento en `produccion/guia/`, por eso no lleva `reemplaza:`. El registro del decreto (`produccion/guia/2026-11-19-2207-registro-decreto.md`) sigue vigente y no cambia: el decreto no fue tocado. Hoy, 2026-11-20, es la reunión con el Vicerrector Académico; por eso las alertas están ordenadas por lo que se ve en pantalla o se dice en voz alta, y cada una dice qué se puede hacer en minutos.

## Qué revisé y cómo

- [HECHO] Calculé la huella de los dos archivos entregados y de las dos versiones anteriores de la presentación con `scripts/comparar_versiones.py`, y comparé cada versión anterior con la v0.3. Fuente: salida de scripts/comparar_versiones.py sobre entregables/ (ejecutado 2026-11-20)
- [HECHO] El comparador no lee el texto que está dentro de formas agrupadas ni de tablas de PowerPoint, ni las notas del orador, ni los comentarios incrustados; para no dejar nada fuera, extraje además todo el texto de la v0.3 recorriendo los grupos, las notas y los comentarios. La huella que registro es la del comparador. Fuente: scripts/comparar_versiones.py y extracción propia con python-pptx sobre Presentacion_VRA_ejecutiva_v0.3.pptx (ejecutado 2026-11-20)
- [HECHO] Las láminas 5 y 7 son imágenes; las abrí y las leí yo mismo, no me quedé con el relato de la sesión principal. Fuente: imágenes "Picture 43" (lámina 5) y "Picture 33" (lámina 7) extraídas de Presentacion_VRA_ejecutiva_v0.3.pptx (vistas 2026-11-20)
- [HECHO] Leí completo el decreto vigente (huella `57c2f7ad3f01`, la misma que registré el 2026-11-19: no cambió), el guion v0.1, `fuentes-cifras.md` y los dos archivos del benchmark. Fuente: entregables/2026-11-14-decreto/decreto-depto-salud-digital-v0.6.docx, entregables/2026-11-20-presentacion-vra-ejecutiva/Guion_VRA_ejecutiva_v0.1.pdf, entregables/2026-11-14-presentacion-vicerrector/fuentes-cifras.md y produccion/benchmark/ (leídos 2026-11-20)
- [HECHO] Quién sugirió cada cambio y por qué me lo informó la sesión principal al encargarme este registro; yo no presencié la conversación con la titular. Donde la sesión me dijo "no consta", escribo "no consta". Fuente: encargo de la sesión principal al Guía, que cita a la titular del cargo (conversación 2026-11-19; recibido 2026-11-20)
- [HECHO] Las versiones v0.1 y v0.2 de la presentación ejecutiva no están en el repositorio: no puedo decir qué cambió entre ellas ni entre la v0.2 y la v0.3. Fuente: listado de entregables/2026-11-20-presentacion-vra-ejecutiva/ (revisado 2026-11-20)

### Huellas

| Archivo | Rótulo | Huella | Párrafos | Palabras |
|---|---|---|---|---|
| `entregables/2026-11-14-presentacion-vicerrector/presentacion-vicerrector.pptx` (generada por la sesión principal) | sin número | `398c67ef716e` | 440 | 2120 |
| `entregables/2026-11-14-presentacion-vicerrector/2026-11-16-presentacion-de-la-titular.pdf` (versión de la titular) | sin número | `448f03da26ac` | 275 | 2375 |
| `Presentacion_VRA_ejecutiva_v0.1.pptx` (no está en el repositorio) | v0.1 | sin huella | no consta | no consta |
| Presentación ejecutiva v0.2 (no está en el repositorio) | v0.2 | sin huella | no consta | no consta |
| `entregables/2026-11-20-presentacion-vra-ejecutiva/Presentacion_VRA_ejecutiva_v0.3.pptx` (vigente) | v0.3 | `fea2d05b9a2b` | 449 | 2574 |
| `entregables/2026-11-20-presentacion-vra-ejecutiva/Guion_VRA_ejecutiva_v0.1.pdf` | v0.1; declara corresponder a la presentación v0.1 | `15d9a8930129` | 103 | 1249 |
| `entregables/2026-11-14-decreto/decreto-depto-salud-digital-v0.6.docx` (decreto vigente, sin cambios) | versión 0.6 | `57c2f7ad3f01` | 39 | 1807 |

- [HECHO] La huella de `presentacion-vicerrector.pptx` es la misma que registré el 2026-11-19 y su última confirmación en git es del 2026-11-15 (1e2ce10); el encargo la describe como "última del 2026-11-19", pero el archivo no cambió desde el 15. Fuente: scripts/comparar_versiones.py y git log sobre entregables/2026-11-14-presentacion-vicerrector/ (ejecutado 2026-11-20)
- [HECHO] El PDF de la titular lleva "2026-11-16" en el nombre y sus metadatos dicen que fue creado el 2026-11-17 a las 13:25 UTC. Fuente: pdfinfo sobre 2026-11-16-presentacion-de-la-titular.pdf (ejecutado 2026-11-20)
- [HECHO] Los metadatos de la v0.3 dicen: última modificación 2026-11-19 19:50, guardada por la cuenta de la titular, revisión 503, 24 láminas, 4 ocultas; el PDF del guion fue creado el 2026-11-19 a las 23:48 UTC con un navegador sin interfaz (HeadlessChrome), es decir, lo generó una herramienta y no Word ni PowerPoint. Fuente: propiedades internas de Presentacion_VRA_ejecutiva_v0.3.pptx y pdfinfo sobre Guion_VRA_ejecutiva_v0.1.pdf (ejecutado 2026-11-20)

## Alertas

Van primero las que el Vicerrector puede ver o escuchar hoy. Todas están comprobadas en los archivos, salvo donde digo que es hipótesis.

ALERTA (registro 2026-11-20 00:26) 1. La presentación y el guion llaman "Dirección de Investigación" a lo que el decreto vigente llama "Dirección de Proyectos". [HECHO] El decreto vigente dice "la Dirección de Docencia y la Dirección de Proyectos, en adelante 'las Direcciones de área'" (artículo 7) y "La Dirección de Proyectos, que comprende la línea basal, la investigación y la vinculación con el medio" (artículo 10); la expresión "Dirección de Investigación" no aparece en ninguna parte del decreto. Fuente: entregables/2026-11-14-decreto/decreto-depto-salud-digital-v0.6.docx, artículos 7 y 10 (leído 2026-11-20)
- [HECHO] En la v0.3, "Dirección de Investigación" aparece 13 veces en texto, en las láminas 6, 11, 13, 14, 15, 16, 17, 18, 19 y 20, y "Dirección de Proyectos" no aparece ninguna vez; el guion dice "Dirección de Investigación" dos veces (lámina 7 y recordatorio de vocabulario). Fuente: conteo propio sobre el texto completo de Presentacion_VRA_ejecutiva_v0.3.pptx y de Guion_VRA_ejecutiva_v0.1.pdf (ejecutado 2026-11-20)
- [HECHO] La lámina 15 afirma que el artículo 10 establece "Dirección de Docencia y Dirección de Investigación", y la lámina 19 se titula "Dirección de Investigación" con el rótulo "RESPALDO · ARTÍCULO 10": las dos atribuyen al decreto un nombre que el decreto no tiene. Fuente: Presentacion_VRA_ejecutiva_v0.3.pptx, láminas 15 y 19, contra el artículo 10 del decreto vigente (leído 2026-11-20)
- [HECHO] La versión de la titular del 2026-11-16 todavía decía "Dirección de Proyectos" en todas partes; el cambio de nombre ocurrió entre esa versión y la v0.3, y no consta quién lo decidió ni por qué. Fuente: scripts/comparar_versiones.py entre 2026-11-16-presentacion-de-la-titular.pdf y la v0.3, y encargo de la sesión principal (ejecutado 2026-11-20)
- [HECHO] El nombre "Dirección de Proyectos" del decreto fue definido por la Decana y transmitido por la titular el 2026-11-17. Fuente: produccion/guia/2026-11-19-2207-registro-decreto.md, tabla "v0.5 → v0.6 generada" (leído 2026-11-20)
- [HIPÓTESIS] Si el Vicerrector tiene el decreto en la mano mientras ve la presentación, va a ver dos nombres para la misma unidad; y si el nombre nuevo es una decisión, el decreto necesita una v0.7 antes de circular. Lo confirmaría que la titular diga cuál de los dos nombres vale y si la Decana lo sabe.
- [PROPUESTA] Para hoy, sin tocar archivos: que la titular decida un solo nombre para decirlo en voz alta, y que si le preguntan diga que el nombre de esa Dirección está en ajuste. Se apoya en que la diferencia está en diez láminas y no se corrige en minutos.

ALERTA (registro 2026-11-20 00:26) 2. Dentro de la misma presentación, la lámina 7 dice "Áreas" y el resto dice "Direcciones". [HECHO] El organigrama de la lámina 7 es una imagen cuyos recuadros dicen "Área de Docencia" y "Área de Investigación", con la leyenda "articulación entre áreas" y la frase "lineamientos técnicos de ambas áreas a las cuatro sedes"; el rótulo lateral sí dice "Direcciones de área". Fuente: imagen "Picture 33" de la lámina 7 de Presentacion_VRA_ejecutiva_v0.3.pptx (vista 2026-11-20)
- [HECHO] Los organigramas pequeños de las láminas 16 a 20, que son formas y no imagen, dicen "Dirección de Docencia" y "Dirección de Investigación": la lámina 7, que es la única de estructura que se expone, quedó con el vocabulario de la v0.4 del decreto. Fuente: Presentacion_VRA_ejecutiva_v0.3.pptx, láminas 16 a 20 (leído 2026-11-20)
- [HECHO] El guion hace decir en la lámina 7 "dos Direcciones de área, la Dirección de Docencia y la Dirección de Investigación", mientras la pantalla muestra "Área de Docencia" y "Área de Investigación": lo que se dice no coincide con lo que se ve. Fuente: Guion_VRA_ejecutiva_v0.1.pdf, página 2, contra la imagen de la lámina 7 (leído 2026-11-20)
- [HECHO] El recuadro "Área de Investigación" de esa imagen enumera cuatro frentes ("línea basal · investigación · vinculación con el medio · proyectos"), y las láminas 14 y 19 dicen tres ("línea basal, investigación y vinculación con el medio"), igual que el artículo 10. Fuente: imagen de la lámina 7 y láminas 14 y 19 de la v0.3, contra el artículo 10 del decreto vigente (leído 2026-11-20)
- [HIPÓTESIS] La imagen fue generada antes del cambio de nombres y nadie la rehízo porque el texto de una imagen no se corrige al buscar y reemplazar. Lo confirmaría quien armó la v0.3.
- [PROPUESTA] Si no se alcanza a rehacer la imagen, que la titular diga al mostrarla "las dos áreas, cada una con su Dirección", que es lo que la lámina muestra de verdad con su rótulo lateral. Se apoya en que es la única lámina de estructura dentro de los cinco minutos.

ALERTA (registro 2026-11-20 00:26) 3. El archivo PowerPoint lleva dentro tres comentarios de otra persona, con nombre y correo institucional. [HECHO] La v0.3 contiene tres comentarios incrustados, escritos el 2026-11-16 por "Carolina Gonzalez Reyes" (cuenta carolina.gonzalez@uss.cl), los tres marcados como resueltos; el comparador no los muestra. Fuente: ppt/comments/ y ppt/authors.xml dentro de Presentacion_VRA_ejecutiva_v0.3.pptx (leído 2026-11-20)
- [HECHO] En la lámina 7 (organigrama): "Veo que lo dejaste igual a como lo habías planteado en nuestra ruenión y pensé que lo ibas a cambiar por el aporte de Manuel...". Fuente: ppt/comments/modernComment_110_0.xml de la v0.3 (leído 2026-11-20)
- [HECHO] En la lámina 10 (cifras del anexo): "Falta la etapa 3 en esta diapositiva". Fuente: ppt/comments/modernComment_115_0.xml de la v0.3 (leído 2026-11-20)
- [HECHO] En la lámina 14 (macro y micro): "La Dirección Nacional entrega a la Facultad la información de las funciones misionales (no a las Vicerrectorías)". Fuente: ppt/comments/modernComment_116_0.xml de la v0.3 (leído 2026-11-20)
- [HECHO] Los comentarios resueltos no se ven al proyectar, pero viajan con el archivo y cualquiera que lo abra en PowerPoint puede leerlos en el panel de comentarios; lo mismo vale para las notas del orador y para las cuatro láminas ocultas. Fuente: estructura interna de Presentacion_VRA_ejecutiva_v0.3.pptx (revisado 2026-11-20)
- [HIPÓTESIS] El comentario de la lámina 7 dice que el organigrama quedó "igual" pese a un aporte de un tercero; no sé si ese aporte se incorporó después ni quién es "Manuel". Lo confirmaría la titular; si el aporte era sobre los nombres o la forma del organigrama, es un origen de cambios que debo registrar.
- [PROPUESTA] No enviar el archivo .pptx a la Vicerrectoría: si piden la presentación, mandar un PDF exportado sin láminas ocultas ni notas, o una copia con los comentarios borrados. Se apoya en que el archivo lleva comentarios internos, notas con respuestas preparadas y láminas de trabajo.

ALERTA (registro 2026-11-20 00:26) 4. Una ficha del anexo pone bajo "EL DECRETO DICE" palabras que el decreto no dice. [HECHO] La lámina 19 pone bajo "EL DECRETO DICE": "Gestiona la investigación, la vinculación con el medio y el desarrollo de proyectos del Departamento, en alineación de la Decanatura y con las Vicerrectorías y unidades institucionales competentes"; el artículo 10 dice que la Dirección de Proyectos "tendrá a su cargo la gestión de las líneas y los proyectos del Departamento en esas materias, en coordinación con las Vicerrectorías y unidades institucionales competentes", sin mencionar a la Decanatura ni la palabra "alineación". Fuente: Presentacion_VRA_ejecutiva_v0.3.pptx, lámina 19, contra el artículo 10 del decreto vigente (leído 2026-11-20)
- [HECHO] La lámina 17 resume el artículo 9 sin la parte que la titular agregó en la versión vigente: que el Comité Consultivo es "instancia de articulación interna" y que en él "se consolidarán la información y los indicadores levantados por las Direcciones de área y las Direcciones de Sede". Fuente: Presentacion_VRA_ejecutiva_v0.3.pptx, lámina 17, contra el artículo 9 del decreto vigente (leído 2026-11-20)
- [HECHO] La lámina 20 resume el artículo 11 sin lo que la titular agregó en la versión vigente: "mantener la relación con las carreras" y "que el Departamento conozca la realidad y la identidad de cada sede". Fuente: Presentacion_VRA_ejecutiva_v0.3.pptx, lámina 20, contra el artículo 11 del decreto vigente (leído 2026-11-20)
- [HECHO] Las láminas 16 (artículo 8) y 18 (artículo 10, Docencia) resumen fielmente el decreto; la 16 omite la subrogación, lo que no altera el sentido. Fuente: Presentacion_VRA_ejecutiva_v0.3.pptx, láminas 16 y 18, contra los artículos 8 y 10 del decreto vigente (leído 2026-11-20)
- [HECHO] Bajo "FUNCIONES", la lámina 16 atribuye a la Dirección Nacional elaborar el Plan de Desarrollo, acordar horas con las unidades de origen, proponer convenios y dar cuenta anual a la Decana y al Consejo de Facultad; ninguna de esas cuatro cosas está en el texto del decreto, que no usa las palabras "cuenta", "convenio" ni "horas". Fuente: búsqueda de texto sobre decreto-depto-salud-digital-v0.6.docx y lámina 16 de la v0.3 (ejecutado 2026-11-20)
- [HIPÓTESIS] Esas funciones vienen del documento "Funciones del director(a) del Departamento de Salud Digital" que la titular revisó el 2026-11-17, y no del decreto. Lo confirmaría la titular; conviene saberlo porque la lámina se rotula "RESPALDO · ARTÍCULO 8" y el guion la usa para responder "¿Qué recursos pide?".
- [HECHO] Las notas de la lámina 11 citan el artículo 1 sin "la gobernanza de la salud digital", que la titular pidió incluir y está en el decreto vigente; es el texto de una versión anterior, y el guion manda a esas notas para responder "¿Qué es la salud digital?". Fuente: notas de la lámina 11 de la v0.3 contra el artículo 1 del decreto vigente, y Guion_VRA_ejecutiva_v0.1.pdf, página 3 (leído 2026-11-20)
- [HECHO] La lámina 6 dice "Responde al artículo 3: un marco común de desempeños sustentado en la investigación del Departamento y en los estándares nacionales e internacionales"; el artículo 3 b) dice "en los estándares internacionales de competencias en salud digital", sin "nacionales", y la versión de la titular del 2026-11-16 decía solo "internacionales". Fuente: lámina 6 de la v0.3, artículo 3 b) del decreto vigente y 2026-11-16-presentacion-de-la-titular.pdf (leído 2026-11-20)
- [HIPÓTESIS] "Nacionales e" se agregó para hacer lugar al modelo de CENS; es razonable, pero entonces lo que quedó corto es el decreto. Lo confirmaría la titular, y sería otro cambio para una v0.7.

ALERTA (registro 2026-11-20 00:26) 5. Tres afirmaciones de la exposición van más lejos que lo que el benchmark verificó. [HECHO] La presentación afirma que ninguno de los 35 marcos incluye IA en la lámina 2 ("que ninguno de los 35 marcos revisados por la OMS tiene"), en la 3 ("0 de 35"), en la 10 ("35 → 0 incluyen IA") y en las notas de la lámina 2; el guion lo repite tres veces. Fuente: texto completo de Presentacion_VRA_ejecutiva_v0.3.pptx y Guion_VRA_ejecutiva_v0.1.pdf (leído 2026-11-20)
- [HECHO] Lo que el benchmark verificó en el documento de la OMS es más acotado: ninguno de los 10 grupos de competencias es de IA y los términos "artificial intelligence" o "AI" no aparecen en la tabla de grupos ni en el mapeo, que además se hizo sobre 31 marcos y no sobre 35; no verificó marco por marco que ninguno mencione la IA. Fuente: produccion/benchmark/2026-11-11-1401-marcos-competencias-verificacion-primaria.md, sección 1 (leído 2026-11-20)
- [HECHO] La lámina 6 usa la formulación que sí está verificada: "Ningún grupo dedicado a inteligencia artificial". Fuente: Presentacion_VRA_ejecutiva_v0.3.pptx, lámina 6 (leído 2026-11-20)
- [HECHO] La lámina 3 dice "El único marco nacional de América Latina quedó fuera de la revisión" y la 10 "sólo existe 1 marco nacional en América Latina que no fue considerado"; el benchmark dice que el de CENS es "el único marco de competencias nacional latinoamericano encontrado", en una búsqueda que declara superficial y que no revisó Brasil, Argentina ni Uruguay, y que la OMS "no dice que existan marcos latinoamericanos excluidos". Fuente: produccion/benchmark/2026-11-11-1334-marcos-competencias-salud-digital.md, líneas 106 y 118, y produccion/benchmark/2026-11-11-1401-marcos-competencias-verificacion-primaria.md, sección 4 (leído 2026-11-20)
- [HECHO] Las versiones anteriores (la de la sesión y la de la titular del 2026-11-16) decían "ningún marco nacional es de América Latina", que es lo verificado; "el único" y "quedó fuera" aparecen recién en la ejecutiva. Fuente: scripts/comparar_versiones.py entre las versiones anteriores y la v0.3 (ejecutado 2026-11-20)
- [HECHO] El modelo de CENS salió en 2024 y en español, y la revisión de la OMS cubrió literatura en inglés de 2012 a 2022: "quedó fuera" puede oírse como una omisión de la OMS cuando en rigor no cumplía sus criterios. Fuente: produccion/benchmark/2026-11-11-1401-marcos-competencias-verificacion-primaria.md, secciones 1 y 4 (leído 2026-11-20)
- [HECHO] El benchmark registra que el marco TIGER, actualizado en 2026, recomienda tratar la IA en todos los dominios y roles de enfermería; quien conozca el tema puede oponerlo a "ningún marco incluye IA". Fuente: produccion/benchmark/2026-11-11-1401-marcos-competencias-verificacion-primaria.md, sección 2 (leído 2026-11-20)
- [HECHO] La presentación no nombra el modelo de CENS como marco (solo cita a CENS por la cifra de 3.500), y el perfil dice que el modelo de la titular "no compite con el de CENS: lo complementa" y que "CENS será citado". Fuente: texto completo de la v0.3 y perfil/cargo.md (leído 2026-11-20)
- [PROPUESTA] Decir hoy la versión verificada: "la OMS revisó 35 marcos, los ordenó en 10 grupos de competencias y ninguno de esos grupos es de inteligencia artificial; tampoco hay ningún marco nacional de América Latina; el chileno, de CENS, es de 2024 y lo vamos a complementar". Se apoya en las líneas anteriores del benchmark y en el perfil.

ALERTA (registro 2026-11-20 00:26) 6. El guion declara corresponder a la presentación v0.1 y lo que se entregó es la v0.3. [HECHO] La segunda línea del guion dice "20 de noviembre de 2026 · Presentacion_VRA_ejecutiva_v0.1.pptx"; el archivo entregado es `Presentacion_VRA_ejecutiva_v0.3.pptx`. Fuente: Guion_VRA_ejecutiva_v0.1.pdf, página 1 (leído 2026-11-20)
- [HECHO] Según los metadatos, el PDF del guion se generó unas cuatro horas después del último guardado de la v0.3 y aun así nombra la v0.1. Fuente: pdfinfo sobre Guion_VRA_ejecutiva_v0.1.pdf y propiedades internas de la v0.3 (ejecutado 2026-11-20)
- [HECHO] Pese al rótulo, el guion calza con la v0.3 lámina por lámina en orden, títulos y cifras, con la sola excepción de la lámina 7 (alerta 2); el detalle está en la sección "Guion contra presentación". Fuente: cotejo propio de Guion_VRA_ejecutiva_v0.1.pdf contra la v0.3 (ejecutado 2026-11-20)
- [HIPÓTESIS] El guion se escribió contra la v0.1 y los cambios de la v0.2 y la v0.3 no tocaron lo que el guion describe, o el guion se regeneró sin actualizar el rótulo. No puedo distinguirlo sin la v0.1 y la v0.2; lo confirmaría quien lo redactó.

ALERTA (registro 2026-11-20 00:26) 7. El guion hace decir cosas que no constan en ningún archivo del repositorio. [HECHO] El guion responde a "¿En qué va el decreto?" que "se presentó al Consejo de Facultad el 12 de noviembre y desde entonces se ha ajustado con sus observaciones"; en mi registro del decreto todos los cambios posteriores vienen de la titular, de la Decana o de la sesión principal, y ninguno está atribuido a observaciones del Consejo de Facultad. Fuente: Guion_VRA_ejecutiva_v0.1.pdf, página 3, y produccion/guia/2026-11-19-2207-registro-decreto.md (leído 2026-11-20)
- [HECHO] El guion responde a "¿Qué recursos pide?" que "la nueva oferta de postgrado y educación continua abre una fuente de ingresos"; esa afirmación no está en la presentación ni en el decreto. Fuente: Guion_VRA_ejecutiva_v0.1.pdf, página 3, y búsqueda de "ingresos" en la v0.3 y en el decreto vigente (ejecutado 2026-11-20)
- [HECHO] La ruta del decreto "según el precedente del DR 116" (lámina 8 y guion) no tiene respaldo en el repositorio: las notas del decreto dejan como hipótesis incluso el número del decreto 116/2020, porque nadie abrió ese documento. Fuente: entregables/2026-11-14-decreto/revision-articulo-por-articulo.md, línea 18 (leído 2026-11-20)
- [PROPUESTA] Que la titular diga "con sus observaciones" solo si el Consejo de Facultad las hizo; si no, "desde entonces se ha ajustado". Se apoya en que el Vicerrector puede preguntar cuáles fueron.

ALERTA (registro 2026-11-20 00:26) 8. Dos nombres distintos para el plan de la Facultad. [HECHO] Las láminas 2 (notas) y 4 y el guion citan el "Plan de Desarrollo de la Facultad 2022–2029 (p. 13)"; el visto 1 del decreto cita el "Plan Estratégico de la Facultad de Ciencias para el Cuidado de la Salud 2025–2029". Fuente: Presentacion_VRA_ejecutiva_v0.3.pptx, láminas 2 y 4, Guion_VRA_ejecutiva_v0.1.pdf, página 1, y visto 1 del decreto vigente (leído 2026-11-20)
- [HECHO] Ninguno de los dos documentos de la Facultad, ni el PDI, están en el repositorio: no puedo decir si son dos planes distintos o uno mal citado, ni comprobar las páginas y los ejes que cita la lámina 2. Fuente: búsqueda de "FODA", "2025–2029" y "Eje 4" en el repositorio (ejecutado 2026-11-20)
- [HIPÓTESIS] Son dos documentos distintos (un plan de desarrollo 2022–2029 con FODA y un plan estratégico 2025–2029) y ambos nombres son correctos. Lo confirmaría la titular, que tiene los dos; si es uno solo, hay que corregir el decreto o la presentación.

ALERTA (registro 2026-11-20 00:26) 9. Quedan restos de versiones anteriores y notas internas a la vista. Ninguno es grave por separado; los enumero porque mi definición me pide avisar.
- [HECHO] No queda ninguna "Coordinación", "Jefatura" ni "Área de Proyectos" en el texto de la v0.3; el único resto de "Áreas" es la imagen de la lámina 7 (alerta 2). Fuente: búsqueda de texto sobre el contenido completo de la v0.3 (ejecutado 2026-11-20)
- [HECHO] La lámina 12 conserva "Otras facultades: ingeniería, derecho y otras"; la titular quitó "en especial la ingeniería y el derecho" de los artículos 2 y 9 del decreto, por un motivo que sigue sin constar. Fuente: Presentacion_VRA_ejecutiva_v0.3.pptx, lámina 12, y produccion/guia/2026-11-19-2207-registro-decreto.md (leído 2026-11-20)
- [HECHO] La lámina 13 termina con una nota de diseño a la vista: "No es un proceso paso a paso: es el mapa de intercambios. Sirve como lámina de entrada antes del flujo"; además ya no es cierto, porque en la v0.3 el flujo es la lámina 12 y va antes. Fuente: Presentacion_VRA_ejecutiva_v0.3.pptx, láminas 12 y 13 (leído 2026-11-20)
- [HECHO] La lámina 14 muestra "centro de costos (en evaluación)" y la lámina 8 "El paso por Secretaría General está por confirmar": son pendientes internos escritos en pantalla; el segundo está en la exposición. Fuente: Presentacion_VRA_ejecutiva_v0.3.pptx, láminas 8 y 14 (leído 2026-11-20)
- [HECHO] Las láminas 21 a 24 están ocultas pero siguen en el archivo: tres portadillas ("Cómo se articula", "Ámbito operativo", "Qué dice el decreto actualmente") y una lámina sin título con "Limitaciones, Proyecciones, Plan de desarrollo, Plan estratégico"; esta última ya venía al final de la versión del 2026-11-16. Fuente: Presentacion_VRA_ejecutiva_v0.3.pptx y 2026-11-16-presentacion-de-la-titular.pdf (leído 2026-11-20)
- [HECHO] Erratas visibles: lámina 3, "profesionales.Y los marcos" (falta un espacio); lámina 10, "35 → 0 incluyen IA / marcos de competencias en salud digital revisó la OMS" (la frase quedó cortada al cambiar la cifra) y "Profesionales" con mayúscula a mitad de tarjeta; lámina 19, "en alineación de la Decanatura". Fuente: Presentacion_VRA_ejecutiva_v0.3.pptx, láminas 3, 10 y 19 (leído 2026-11-20)
- [HECHO] La lámina 15 dice "Más dos artículos transitorios", que es correcto frente al decreto vigente; la versión de la sesión y la del 2026-11-16 decían "tres". Fuente: scripts/comparar_versiones.py entre las versiones anteriores y la v0.3, y decreto vigente (ejecutado 2026-11-20)

ALERTA (registro 2026-11-20 00:26) 10. Otros documentos quedaron desactualizados frente a la v0.3. [HECHO] `presentacion-vicerrector.pptx` y su PDF (Áreas, Jefaturas, Coordinaciones, "tres artículos transitorios", el nombre de la titular y "con proyección doctoral" en la lámina de la línea basal) y `generar_presentacion.py`, que los regenera, ya no corresponden a lo que la titular va a presentar. Fuente: scripts/comparar_versiones.py entre presentacion-vicerrector.pptx y la v0.3 (ejecutado 2026-11-20)
- [HECHO] `guion-presentacion.docx` y `guia-reunion-vicerrector.docx`, del 2026-11-15, siguen en la v0.4 y describen otra presentación, con otro orden; siguen valiendo para ellos las observaciones de la alerta 3 del registro del decreto. Fuente: produccion/guia/2026-11-19-2207-registro-decreto.md, alerta 3, y huella `37a79aaf08ba` sin cambios (revisado 2026-11-20)
- [HECHO] `perfil/cargo.md` todavía describe la estructura como "Área de Docencia" y "Área de Proyectos" y habla de "Coordinaciones de Sede". Fuente: perfil/cargo.md, sección "Contexto institucional" (leído 2026-11-20)
- [PROPUESTA] Que la titular actualice `perfil/cargo.md` cuando cierre el nombre de la segunda Dirección; yo no edito el perfil. Se apoya en la línea anterior.
- [HECHO] La alerta 4 de mi registro del decreto pedía dejar en `entregables/` la presentación de la titular del 2026-11-16; ya está, y mi hipótesis de entonces se confirma: esa versión decía "tres artículos transitorios", "Coordinaciones de Sede", "Jefaturas" y mezclaba nombres ("la Dirección, las Jefaturas de Dirección y los Coordinadores de Sede"). Fuente: entregables/2026-11-14-presentacion-vicerrector/2026-11-16-presentacion-de-la-titular.pdf (leído 2026-11-20)

## Coherencia con el decreto vigente, punto por punto

| Tema | Decreto vigente (v0.6, `57c2f7ad3f01`) | Presentación v0.3 | Guion v0.1 | Estado |
|---|---|---|---|---|
| Dirección Nacional | "Director o Directora Nacional" (art. 8) | Igual | Igual | Calza |
| Primera Dirección de área | "Dirección de Docencia" (arts. 7 y 10) | "Dirección de Docencia"; en la imagen de la lámina 7, "Área de Docencia" | "Dirección de Docencia" | No calza en la lámina 7 |
| Segunda Dirección de área | "Dirección de Proyectos" (arts. 7 y 10) | "Dirección de Investigación" (13 veces); en la imagen de la lámina 7, "Área de Investigación" | "Dirección de Investigación" | No calza |
| Genérico | "las Direcciones de área" (art. 7) | "Direcciones de área"; en la lámina 7, además, "áreas" | "las Direcciones de área" | Calza, salvo la imagen |
| Sedes | "Direcciones de Sede" (art. 11) | Igual; la imagen dice "Sede Santiago", etc., con el rótulo "Direcciones de Sede" | "una Dirección de Sede" | Calza |
| Comité | "Comité Consultivo", articulación interna, consolida información e indicadores (art. 9) | "Comité Consultivo"; la ficha omite articulación e indicadores | No lo menciona en la exposición | Calza el nombre; ficha incompleta |
| Transitorios | Dos | "Más dos artículos transitorios" (lámina 15) | No los menciona | Calza |
| Número de artículos | 13 | "ARTÍCULOS 7 A 13", "ARTÍCULOS 1 A 6" | Cita el artículo 1 | Calza |
| Marco de desempeños | "estándares internacionales" (art. 3 b) | "estándares nacionales e internacionales" (lámina 6) | No lo cita | No calza |
| Definición de salud digital | Incluye "la gobernanza de la salud digital" (art. 1) | Notas de la lámina 11, sin la gobernanza | Cita solo la primera frase | Notas desactualizadas |
| Plan de la Facultad | "Plan Estratégico… 2025–2029" (visto 1) | "Plan de Desarrollo de la Facultad 2022–2029" | "su plan 2022–2029" | Sin resolver (alerta 8) |
| Leyes | 21.541, 21.668 y 21.719 (visto 7) | Las mismas, con la misma frase (lámina 3) | Las mismas | Calza |
| Ingeniería y derecho | Quitados de los arts. 2 y 9 | "ingeniería, derecho y otras" (lámina 12); "Electivo de salud con ingeniería" (imagen de la lámina 5) | No lo menciona | Resto en la lámina 12 |

- [HECHO] La tabla anterior resume el cotejo que hice del texto completo de los tres documentos. Fuente: decreto-depto-salud-digital-v0.6.docx, Presentacion_VRA_ejecutiva_v0.3.pptx y Guion_VRA_ejecutiva_v0.1.pdf (leídos 2026-11-20)

## Guion contra presentación, lámina por lámina

| Lámina | Título en la v0.3 | Lo que dice el guion | Calza |
|---|---|---|---|
| 1 | "Departamento Nacional de Salud Digital" · "Salud digital: una oportunidad que la USS puede liderar" | "Portada"; la estructura va al final | Sí |
| 2 | "Lo que gana la USS con la salud digital" | Cinco ganancias, en el mismo orden y casi con las mismas palabras; en Empleabilidad el guion omite "y empleabilidad medida también en salud digital" | Sí |
| 3 | "La salud se digitaliza y faltan profesionales" · "EL POTENCIAL" | Tres leyes; 0,6 a 2 millones (OPS); ninguno de los 35 marcos incluye IA; frase de cierre idéntica a la de la lámina | Sí (con la alerta 5) |
| 4 | "La USS ya partió: tiene la base para liderar" | 1.788 estudiantes, 31 secciones, cuatro carreras, cuatro sedes; plan 2022–2029; empleabilidad de primer año; frase de cierre idéntica | Sí (con la alerta 8) |
| 5 | "Leemos el mundo laboral y lo convertimos en formación" (imagen) | Describe la figura: necesidades, lectura, identificación de áreas y benchmarking en paralelo, propuestas (asignatura, electivo, diplomado), competencias, empleabilidad y la flecha dorada de vuelta | Sí; la imagen tiene esos siete pasos y esa flecha |
| 6 | "Un modelo propio de competencias, medido cada semestre" | 35 marcos, 10 grupos, sin marco de América Latina ni grupo de IA; adaptar, medir cada semestre, analizar, ajustar; productos | Sí |
| 7 | "Una estructura liviana sobre capacidades que ya existen" (imagen) | "dos Direcciones de área, la Dirección de Docencia y la Dirección de Investigación" | No: la imagen dice "Área de Docencia" y "Área de Investigación" |
| 8 | "La salud digital ya está en la USS: ahora puede liderarla" | Cinco ganancias, ruta del decreto y la pregunta, con el mismo texto | Sí |
| 9 | "Anexo" | "el anexo parte en la 9" | Sí |
| 10 | "Las cifras detrás del mundo laboral: oportunidades" | 3.500 (CENS), 170 millones y 40 % (Foro Económico Mundial) | Sí |
| 11 | "Objetivos y mirada del Departamento" | Definición del artículo 1 "en las notas" | Sí; las notas existen, con texto anterior (alerta 4) |
| 13 | "Qué aporta cada actor y qué recibe del Departamento" | Lo que recibe la VRA, la VRID y VcM | Sí, con las mismas palabras |
| 14 | "El mismo modelo, de la sede a las Vicerrectorías" | Indicadores por sede | Sí |
| 15 a 20 | Artículos en el organigrama y fichas de respaldo | "cada Dirección tiene su lámina de respaldo" | Sí |
| 16 | "Dirección Nacional" | "¿Qué recursos pide?": horas acordadas con la unidad de origen | Parcial: las horas están; el presupuesto está en la lámina 13 y los "ingresos" no están en ninguna |

- [HECHO] El guion suma 5 minutos y 20 segundos de exposición (10 + 60 + 45 + 45 + 40 + 40 + 30 + 40 segundos) y se presenta como "unos 5 minutos". Fuente: suma propia de los tiempos de Guion_VRA_ejecutiva_v0.1.pdf (ejecutado 2026-11-20)
- [HECHO] El guion no menciona las láminas 12 ni 21 a 24; la 12 queda en el anexo sin pregunta que lleve a ella. Fuente: Guion_VRA_ejecutiva_v0.1.pdf, tabla "Si pregunta…" (leído 2026-11-20)

## Cifras y afirmaciones frente a las fuentes

| Cifra o afirmación | Dónde | Qué dice la fuente del repositorio | Estado |
|---|---|---|---|
| 1.788 estudiantes, 31 secciones, 4 carreras, 4 sedes; Blackboard, 25 de septiembre de 2026 | Láminas 2, 4, 6 y 10; guion | Igual, periodo 202620 | Calza con `fuentes-cifras.md` |
| "0,6 a 2 M profesionales de la salud que faltarán en América a 2030 si no hay intervenciones" | Láminas 3 y 10; guion | "podrían enfrentar un déficit de entre 600.000 y 2 millones de trabajadores de salud a 2030" en "las Américas" | La cifra calza; cambió "trabajadores" por "profesionales", "las Américas" por "América" y "podrían" por "faltarán"; "si no hay intervenciones" no está en `fuentes-cifras.md` |
| "170 M empleos nuevos… cerca del 40% de las habilidades clave va a cambiar" | Lámina 10; notas de la 3; guion | Igual, pero "vía buscador, sin abrir el informe" | Calza, con fuente no abierta |
| "y las tecnológicas son las que más crecen" | Lámina 10 | No está en `fuentes-cifras.md` | Sin respaldo en el repositorio |
| "3.500 profesionales con competencias digitales que faltaban en Chile" (CENS, 2019) | Lámina 10; notas de la 3; guion | "al menos 3.500 profesionales", por prensa que cita a CENS; "con competencias digitales" no está en la fuente | Calza la cifra; se perdió "al menos" y la fuente es secundaria |
| 35 marcos, 10 grupos, sin grupo de IA, sin marco nacional de América Latina, solo inglés 2012–2022; OMS, junio de 2026 | Lámina 6 | Igual; la ficha de la OMS lo fecha el 14 de junio de 2026 | Calza con el benchmark |
| "0 de 35 marcos incluyen IA" | Láminas 2, 3 y 10; notas de la 2; guion | Ningún grupo es de IA; mapeo sobre 31 marcos | Va más lejos que lo verificado (alerta 5) |
| "El único marco nacional de América Latina quedó fuera" | Láminas 3 y 10; guion | "único encontrado", búsqueda superficial; la OMS no dice que haya excluidos | Va más lejos que lo verificado (alerta 5) |
| "3 leyes" 21.541, 21.668 y 21.719 | Lámina 3; guion | Mismo texto que el visto 7 del decreto; ningún agente abrió las leyes | Calza con el decreto; sin verificación propia en el repositorio |
| PDI 2022–2029, ejes y objetivos (pp. 25–32) y diagnóstico (p. 18) | Láminas 2 y 4 | El PDI no está en el repositorio | No lo puedo comprobar |
| FODA del Plan de Desarrollo de la Facultad 2022–2029 (p. 13), con dos citas textuales | Lámina 4 | El documento no está en el repositorio | No lo puedo comprobar |
| Estrategia Nacional de Salud al 2030, resultado 8.7.2 | Notas de la lámina 3; guion | No está en `fuentes-cifras.md` ni en la producción de ningún agente | Sin respaldo en el repositorio |
| "La USS mide empleabilidad, pero no en salud digital" | Láminas 4 y 10 | Dicho por la titular el 2026-11-14 | Calza con `fuentes-cifras.md` |
| Ruta del decreto según el DR 116 | Lámina 8; guion | Nadie abrió el DR 116 | Sin respaldo en el repositorio (alerta 7) |

- [HECHO] La tabla anterior resume el cotejo de cada cifra de la v0.3 y del guion contra `fuentes-cifras.md` y los dos archivos del benchmark. Fuente: entregables/2026-11-14-presentacion-vicerrector/fuentes-cifras.md, produccion/benchmark/2026-11-11-1401-marcos-competencias-verificacion-primaria.md y produccion/benchmark/2026-11-11-1334-marcos-competencias-salud-digital.md (leídos 2026-11-20)
- [HECHO] `fuentes-cifras.md` es del 2026-11-14 y no cubre nada de lo que la ejecutiva agregó: PDI, FODA de la Facultad, Estrategia Nacional de Salud, las tres leyes, "las tecnológicas son las que más crecen" ni "el único marco nacional". Fuente: entregables/2026-11-14-presentacion-vicerrector/fuentes-cifras.md (leído 2026-11-20)
- [HIPÓTESIS] Las citas del PDI y del plan de la Facultad son correctas, porque traen página y cita textual y la titular tiene esos documentos; lo que digo es que este sistema no los ha visto. Lo confirmaría dejar ambos PDF en el repositorio.
- [HECHO] "Medido cada semestre" aparece cinco veces en la v0.3 (título de la lámina 6 incluido) y tres en el guion; ya estaba en la versión de la sesión y en la del 2026-11-16, así que no es nuevo, pero ahora está en un título y el decreto no fija frecuencia por decisión de la titular ("no hablar de tiempos, es atarse de manos"). Fuente: conteo propio sobre la v0.3 y el guion, y produccion/guia/2026-11-19-2207-registro-decreto.md, tabla "v0.3 → v0.4" (ejecutado 2026-11-20)
- [HECHO] La lámina 7 se titula "Una estructura liviana" y el decreto crea una Dirección Nacional, dos Direcciones de área y una Dirección de Sede por cada una de las cuatro sedes: siete Direcciones, con instalación gradual según el transitorio segundo. Fuente: lámina 7 de la v0.3 y artículos 7, 10 y 11 y transitorio segundo del decreto vigente (leído 2026-11-20)
- [PROPUESTA] Si el Vicerrector cuenta las Direcciones, responder con el transitorio segundo: se instalan gradualmente, "en la medida en que lo requieran las necesidades del Departamento y lo permita la disponibilidad de la Facultad", y mientras tanto las funciones de las Direcciones de área las ejerce la Dirección Nacional. Se apoya en los dos transitorios del decreto vigente.

## Historia de cambios

"Encargo" es el relato de la sesión principal al encargarme este registro (recibido 2026-11-20), que cita la conversación con la titular. "Comparador" es `scripts/comparar_versiones.py`. "Lectura" es mi lectura del texto completo y de las imágenes.

### Versión de la sesión (2026-11-14 y 15) → versión de la titular (2026-11-16)

- [HECHO] La versión de la sesión tiene 19 láminas y la de la titular 19 páginas, pero no en el mismo orden ni con las mismas láminas: la titular puso las cifras antes del ciclo y la línea basal antes de "macro y micro", quitó "Tres productos, un mismo camino por el Departamento", rotuló dos láminas como "OPCIÓN 1" y "OPCIÓN 3", agregó portadillas y cambió los nombres. Fuente: scripts/comparar_versiones.py entre presentacion-vicerrector.pptx y 2026-11-16-presentacion-de-la-titular.pdf, y pdfinfo (ejecutado 2026-11-20)

| Lugar | Qué decía (sesión) | Qué dice (titular, 16 de noviembre) | Quién lo sugirió | Por qué | Consta en |
|---|---|---|---|---|---|
| Todas las láminas de estructura | "Área de Docencia", "Área de Proyectos" | "Dirección de Docencia", "Dirección de Proyectos" | Decana (nombres), transmitido por la titular | Nombres definidos por la Decana | Registro del decreto, tabla "v0.5 → v0.6 generada"; comparador |
| Varias láminas | "Coordinaciones de Sede", "Jefaturas" | Quedaron sin cambiar, o mezcladas ("Jefaturas de Dirección", "Direccións") | No consta | Reemplazo incompleto | Comparador |
| Lámina de la línea basal | "Modelo propuesto: línea de investigación de Estefanía Fröhlich, con proyección doctoral" | "Modelo propuesto: línea de investigación" | Titular | "Primero que salga el decreto" | Encargo, que fecha la conversación el 2026-11-19; comparador |
| Lámina de la línea basal | "La gestiona el Área de Proyectos" | "La gestiona el Dirección de Proyectos" | Consecuencia del cambio de nombres | Ídem | Comparador |
| Portada | Sin nombre de la titular | "Estefanía Fröhlich - Directora Salud Digital" | No consta | No consta | Comparador |
| Orden | Ciclo, cifras, macro y micro, línea basal, articulación, organigrama, fichas | Cifras, ciclo, línea basal, macro y micro, organigrama, articulación, artículos, objetivos, fichas | No consta (el archivo es de la titular) | No consta | Lectura página por página |
| Lámina "Tres productos, un mismo camino por el Departamento" | Existía (lámina 8) | Eliminada | No consta | No consta | Lectura página por página |
| Láminas de articulación | Sin rótulo de opción | "OPCIÓN 1" (ciclo anual) y "OPCIÓN 3" (qué aporta cada actor) | No consta | No consta; sugiere que se estaba eligiendo entre alternativas | Lectura página por página |
| Final | "Coordinaciones de Sede" era la última | Agrega una página con "Limitaciones, Proyecciones, Plan de desarrollo, Plan estratégico" | No consta (el archivo es de la titular) | No consta | Comparador |

- [HECHO] El nombre de la titular y "con proyección doctoral" ya no estaban en la lámina de la línea basal en el archivo del 2026-11-16, y el encargo fecha esa decisión en la conversación del 2026-11-19: o la decisión es anterior y el 19 solo se comentó, o la fecha del archivo no es la que dice su nombre. Fuente: 2026-11-16-presentacion-de-la-titular.pdf, página de la línea basal, y encargo de la sesión principal (leído 2026-11-20)
- [HECHO] La lámina 6 de la v0.3 conserva "Tesis de pregrado, postgrado y doctorado" como producto de la línea; es una mención general a tesis, no a la proyección doctoral de la titular. Fuente: Presentacion_VRA_ejecutiva_v0.3.pptx, lámina 6 (leído 2026-11-20)

### Versión de la titular (2026-11-16) → ejecutiva v0.3 (entregada 2026-11-20), pasando por v0.1 y v0.2 que no tengo

- [HECHO] La presentación pasó de 19 a 24 láminas, con una exposición nueva de 8 láminas delante, un anexo de 12 y 4 ocultas; el comparador muestra el texto de las láminas 1 a 4 y 8 como enteramente nuevo. Fuente: scripts/comparar_versiones.py entre 2026-11-16-presentacion-de-la-titular.pdf y la v0.3 (ejecutado 2026-11-20)

| Lugar (v0.3) | Qué decía (16 de noviembre) | Qué dice (v0.3) | Quién lo sugirió | Por qué | Consta en |
|---|---|---|---|---|---|
| Orden general | Ciclo, cifras, línea basal, estructura, fichas | Primero lo que gana la USS (láminas 2 a 4), luego ciclo y modelo, estructura en la 7, cierre en la 8, resto al anexo | Titular | "Importa más la presentación que el decreto"; primero lo que gana la USS, la estructura al final | Encargo |
| Redacción de la ejecutiva y del guion | No aplica | Láminas 1 a 4 y 8 nuevas; guion nuevo | No consta (no fue la sesión principal; puede ser otra herramienta o sesión) | No consta | Encargo |
| Portada | "Formación, articulación y línea de investigación" | "Salud digital: una oportunidad que la USS puede liderar" · "Propuesta para la Vicerrectoría Académica" | No consta | Enfoque ejecutivo | Comparador |
| Lámina 2 (nueva) | No existía | Cinco ganancias ligadas al PDI 2022–2029 | No consta | No consta | Comparador |
| Lámina 3 (nueva) | No existía | Tres leyes, 0,6 a 2 M, 0 de 35 | No consta | No consta | Comparador |
| Lámina 4 (nueva) | No existía | 1.788 estudiantes, FODA de la Facultad, empleabilidad sin medir | No consta | No consta | Comparador |
| Lámina 5 (ciclo) | Formas con texto; paso 3 "Selección de oportunidades"; "Diplomado, en desarrollo"; pie con "Coordinaciones de Sede" y "Comité Consultivo y Decana: priorizan y deciden" | Imagen; paso 3 "Identificación de áreas de desarrollo académico e investigación", en paralelo con el benchmarking; "Diplomado"; sin ese pie | No consta | No consta | Lectura de la imagen; comparador |
| Lámina 6 (línea basal) | Título "Competencias digitales en salud: una línea que queda instalada" | Título "Un modelo propio de competencias, medido cada semestre" | No consta | No consta | Comparador |
| Lámina 6 | "La gestiona el Dirección de Proyectos" | "La gestiona la Dirección de Investigación" | No consta | No consta | Encargo; comparador |
| Lámina 6 | "en los estándares internacionales" | "en los estándares nacionales e internacionales" | No consta | No consta | Comparador |
| Lámina 7 (organigrama) | Título "Organigrama: una estructura matricial"; formas con "Dirección de Docencia", "Dirección de Proyectos", "Coordinaciones de Sede" | Imagen con "Área de Docencia", "Área de Investigación", rótulo "Direcciones de área" y "Direcciones de Sede"; título "Una estructura liviana sobre capacidades que ya existen" | No consta | No consta | Lectura de la imagen |
| Lámina 8 (nueva) | No existía | Cierre con las cinco ganancias, la pregunta y la ruta del decreto según el DR 116 | No consta | No consta | Comparador |
| Lámina 10 (cifras) | Seis tarjetas con "etapa N del ciclo"; "ningún marco nacional es de América Latina"; pie "La etapa 7 es la oportunidad" | Sin etapas; "35 → 0 incluyen IA… sólo existe 1 marco nacional en América Latina que no fue considerado"; "las tecnológicas son las que más crecen" | Quitar las etapas responde al comentario "Falta la etapa 3" (Carolina Gonzalez Reyes, 2026-11-16); el resto no consta | No consta | Comentario incrustado en la v0.3; comparador |
| Lámina 14 | "Entrega a decanatura FCCS lo…" | "Entrega a decanatura FCCS que eleva a VRA, VRID, VcM y Proyectos Institucionales" | Comentario de Carolina Gonzalez Reyes, 2026-11-16: la Dirección Nacional entrega a la Facultad, no a las Vicerrectorías | Lo dice el comentario | Comentario incrustado en la v0.3; comparador |
| Todas las láminas de estructura | "Dirección de Proyectos" | "Dirección de Investigación" | No consta | No consta | Encargo; comparador |
| Todas las láminas de estructura | "Coordinaciones de Sede", "Jefaturas", "Coordinadores" | "Direcciones de Sede", "Directores de área y de Sede" | Decana (nombres), vía titular; quién terminó el reemplazo no consta | Nombres del decreto vigente | Registro del decreto; comparador |
| Lámina 15 | "Más tres artículos transitorios" | "Más dos artículos transitorios" | No consta | Calza con el decreto vigente | Comparador |
| Láminas 12 y 13 | Rótulos "OPCIÓN 1" y "OPCIÓN 3" | Sin rótulo de opción; quedan las dos, en el anexo | No consta | No consta | Lectura |
| Láminas 21 a 23 (ocultas) | "Cómo se articula" y "Que dice el decreto actualmente" eran portadillas visibles | Las mismas, ocultas, más "Ámbito operativo", que es nueva | No consta | No consta | Lectura |

- [HIPÓTESIS] La sesión principal, o la herramienta que redactó la ejecutiva, respondió a los comentarios del 2026-11-16 en las láminas 10 y 14; la atribución de la tabla sale de comparar el comentario con el cambio, nadie me la confirmó. Lo confirmaría la titular.
- [HIPÓTESIS] El comentario del 2026-11-16 en la lámina 14 ya estaba resuelto en el PDF del 16 ("Entrega a decanatura FCCS…"), lo que sugiere que ese PDF es posterior al comentario; calza con que sus metadatos digan 2026-11-17. Lo confirmaría la titular.

### Revisión del guion por la sesión principal (2026-11-19), sin cambios en el archivo

- [HECHO] La sesión principal revisó el guion el 2026-11-19 y señaló cinco puntos: "Dirección de Investigación" contradice al decreto; "ninguno de los 35 marcos incluye IA" y "el único marco nacional de América Latina" van más lejos que el benchmark; "cada semestre" es un compromiso de frecuencia; "plan 2022–2029 de la Facultad" no calza con el visto 1; "estructura liviana" frente a siete Direcciones. Fuente: encargo de la sesión principal al Guía (recibido 2026-11-20)
- [HECHO] Comprobé los cinco puntos contra los archivos y los cinco se sostienen; los cinco siguen presentes en la v0.3 y en el guion entregados, es decir, la revisión no produjo cambios. Fuente: cotejo propio de la v0.3 y del guion contra el decreto vigente y el benchmark (ejecutado 2026-11-20)
- [HECHO] No consta si la titular vio esas observaciones ni qué decidió sobre cada una. Fuente: encargo de la sesión principal al Guía (recibido 2026-11-20)

## Lo que me llama la atención

Son observaciones mías; decide la titular.

- [HIPÓTESIS] El título de la lámina 14, "El mismo modelo, de la sede a las Vicerrectorías", todavía sugiere lo que el comentario del 2026-11-16 pidió corregir (que el Departamento no entrega directo a las Vicerrectorías, sino a la Facultad); el cuerpo ya lo corrige. Lo confirmaría la autora del comentario.
- [HIPÓTESIS] La lámina 13 dice que la Facultad recibe "actas del Comité" y el artículo 9 dice que las actas se remiten a la Secretaría General; pueden ser ambas cosas, pero la lámina 17 dice lo del decreto y la 13 otra cosa. Lo confirmaría la titular.
- [HIPÓTESIS] "Un modelo propio de competencias" (título de la lámina 6) y "Posicionamiento" (lámina 2) empujan la idea de ser los primeros; las notas de la lámina 2 ya advierten que "ser los primeros es una aspiración", pero la frase que proponen en su lugar es justamente la que excede al benchmark (alerta 5). Lo resolvería cambiar esa nota por la formulación de la lámina 6.
- [HECHO] La portada lleva el nombre de la titular y su cargo como "Directora Salud Digital"; la decisión de no poner su nombre se refería a la lámina de la línea basal, y ahí no está. Fuente: Presentacion_VRA_ejecutiva_v0.3.pptx, láminas 1 y 6, y encargo de la sesión principal (leído 2026-11-20)
- [HECHO] La propuesta de pedir a la Vicerrectoría "sumar las competencias digitales al seguimiento de egresados" va marcada como "[propuesta]" en el guion; `fuentes-cifras.md` ya advertía que definir ese indicador requiere respaldo del benchmark, y `produccion/brechas-indicadores/` sigue vacía. Fuente: Guion_VRA_ejecutiva_v0.1.pdf, página 3, entregables/2026-11-14-presentacion-vicerrector/fuentes-cifras.md y listado de produccion/ (revisado 2026-11-20)
- [PROPUESTA] Que nadie convierta hoy "empleabilidad medida en salud digital" ni "indicadores cada semestre" en un compromiso con cifra: no hay indicador con respaldo del benchmark. Se apoya en la regla 2 del sistema y en que Brechas e indicadores no ha producido nada.

## Estado

- [HECHO] Versión vigente de la presentación: `entregables/2026-11-20-presentacion-vra-ejecutiva/Presentacion_VRA_ejecutiva_v0.3.pptx`, rótulo v0.3, huella `fea2d05b9a2b`, 449 párrafos y 2574 palabras según el comparador, 24 láminas (1 a 8 exposición, 9 a 20 anexo, 21 a 24 ocultas), con tres comentarios incrustados. Fuente: scripts/comparar_versiones.py y propiedades internas del archivo (ejecutado 2026-11-20)
- [HECHO] Versión vigente del guion: `entregables/2026-11-20-presentacion-vra-ejecutiva/Guion_VRA_ejecutiva_v0.1.pdf`, rótulo v0.1, huella `15d9a8930129`, 3 páginas; declara corresponder a la presentación v0.1. Fuente: scripts/comparar_versiones.py y pdfinfo (ejecutado 2026-11-20)
- [HECHO] Estas son las primeras versiones registradas de ambos documentos. Si la titular entrega una presentación o un guion con otra huella, corresponde alerta; y como la huella no cubre imágenes, grupos ni comentarios, un cambio solo en la imagen de la lámina 7 no la movería: habrá que mirarla de nuevo. Fuente: este registro, produccion/guia/2026-11-20-0026-registro-presentacion-vra.md (escrito 2026-11-20)
- [HECHO] El decreto vigente sigue siendo la v0.6 de huella `57c2f7ad3f01`; ninguno de los pendientes de mi registro del 2026-11-19 consta como resuelto, salvo que la presentación del 2026-11-16 ya está en `entregables/`. Fuente: produccion/guia/2026-11-19-2207-registro-decreto.md y scripts/comparar_versiones.py (revisado 2026-11-20)

### Pendientes de la titular, para hoy antes de la reunión

- [PROPUESTA] Decidir qué nombre dirá en voz alta: "Dirección de Investigación" (presentación) o "Dirección de Proyectos" (decreto). Se apoya en la alerta 1.
- [PROPUESTA] Decidir cómo presentará la lámina 7, cuya imagen dice "Áreas". Se apoya en la alerta 2.
- [PROPUESTA] Decir la versión verificada sobre la IA y sobre América Latina, y nombrar a CENS. Se apoya en la alerta 5.
- [PROPUESTA] No decir "con sus observaciones" ni "fuente de ingresos" si no tiene con qué sostenerlo. Se apoya en la alerta 7.
- [PROPUESTA] No enviar el .pptx tal como está. Se apoya en la alerta 3.

### Pendientes de la titular, después de la reunión

- [PROPUESTA] Decir quién decidió "Dirección de Investigación" y por qué, y si la Decana lo sabe; si el nombre queda, el decreto necesita una v0.7 en los artículos 7 y 10. Se apoya en la alerta 1 y en que el nombre anterior lo definió la Decana.
- [PROPUESTA] Decir quién redactó la ejecutiva y el guion (herramienta o sesión), y dejar en `entregables/` la v0.1 y la v0.2 si existen, para completar la historia. Se apoya en las celdas "no consta" de la última tabla.
- [PROPUESTA] Decir qué era "el aporte de Manuel" sobre el organigrama y si se incorporó. Se apoya en la alerta 3.
- [PROPUESTA] Aclarar si el "Plan de Desarrollo de la Facultad 2022–2029" y el "Plan Estratégico 2025–2029" son dos documentos, y dejar en el repositorio el PDI y el plan de la Facultad para comprobar páginas y citas. Se apoya en la alerta 8.
- [PROPUESTA] Decir si "estándares nacionales e internacionales" es intencional; si lo es, pasa al artículo 3 b) en la v0.7. Se apoya en la alerta 4.
- [PROPUESTA] Contar qué dijo el Vicerrector, para registrarlo como origen de los cambios que vengan: todavía no hay ninguna entrada suya en la columna "quién lo sugirió". Se apoya en este registro y en el del decreto.

### Pendientes de la sesión principal

- [PROPUESTA] Confirmarme si la titular vio las cinco observaciones del 2026-11-19 sobre el guion y qué decidió sobre cada una. Se apoya en que siguen todas en los archivos entregados.
- [PROPUESTA] Confirmarme la fecha de la decisión sobre el nombre y la proyección doctoral, porque el archivo del 2026-11-16 ya no los traía. Se apoya en la tabla de la primera transición.
- [PROPUESTA] Actualizar `fuentes-cifras.md` con las fuentes que la ejecutiva agregó (PDI, FODA, Estrategia Nacional de Salud, leyes), o declararlas no verificadas. Se apoya en la sección de cifras.
- [PROPUESTA] No volver a ejecutar `generar_presentacion.py` como si produjera la versión vigente: genera la del 2026-11-15. Se apoya en la alerta 10.

### Encargos que sugiero a otros agentes

- [PROPUESTA] Pedir al Benchmark que verifique marco por marco si alguno de los 35 de la OMS incluye competencias de IA y que busque marcos nacionales en Brasil, Argentina, Uruguay y Colombia, para poder sostener o corregir "0 de 35" y "el único". Se apoya en la alerta 5 y en los vacíos que el propio benchmark declara.
- [PROPUESTA] Pedir a Brechas e indicadores, con respaldo del Benchmark, un indicador de competencias digitales por semestre y uno de empleabilidad en salud digital antes de que la presentación los prometa con meta. Se apoya en que la regla 2 no permite crear indicadores sin respaldo.
