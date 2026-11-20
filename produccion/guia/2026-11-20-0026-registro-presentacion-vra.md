---
agente: guia
fecha: 2026-11-20
titulo: Registro de versiones de la presentación para la Vicerrectoría Académica (de la versión de la sesión a la ejecutiva v0.3) y de su guion v0.1
---

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

ALERTA 1. La presentación y el guion llaman "Dirección de Investigación" a lo que el decreto vigente llama "Dirección de Proyectos". [HECHO] El decreto vigente dice "la Dirección de Docencia y la Dirección de Proyectos, en adelante 'las Direcciones de área'" (artículo 7) y "La Dirección de Proyectos, que comprende la línea basal, la investigación y la vinculación con el medio" (artículo 10); la expresión "Dirección de Investigación" no aparece en ninguna parte del decreto. Fuente: entregables/2026-11-14-decreto/decreto-depto-salud-digital-v0.6.docx, artículos 7 y 10 (leído 2026-11-20)
- [HECHO] En la v0.3, "Dirección de Investigación" aparece 13 veces en texto, en las láminas 6, 11, 13, 14, 15, 16, 17, 18, 19 y 20, y "Dirección de Proyectos" no aparece ninguna vez; el guion dice "Dirección de Investigación" dos veces (lámina 7 y recordatorio de vocabulario). Fuente: conteo propio sobre el texto completo de Presentacion_VRA_ejecutiva_v0.3.pptx y de Guion_VRA_ejecutiva_v0.1.pdf (ejecutado 2026-11-20)
- [HECHO] La lámina 15 afirma que el artículo 10 establece "Dirección de Docencia y Dirección de Investigación", y la lámina 19 se titula "Dirección de Investigación" con el rótulo "RESPALDO · ARTÍCULO 10": las dos atribuyen al decreto un nombre que el decreto no tiene. Fuente: Presentacion_VRA_ejecutiva_v0.3.pptx, láminas 15 y 19, contra el artículo 10 del decreto vigente (leído 2026-11-20)
- [HECHO] La versión de la titular del 2026-11-16 todavía decía "Dirección de Proyectos" en todas partes; el cambio de nombre ocurrió entre esa versión y la v0.3, y no consta quién lo decidió ni por qué. Fuente: scripts/comparar_versiones.py entre 2026-11-16-presentacion-de-la-titular.pdf y la v0.3, y encargo de la sesión principal (ejecutado 2026-11-20)
- [HECHO] El nombre "Dirección de Proyectos" del decreto fue definido por la Decana y transmitido por la titular el 2026-11-17. Fuente: produccion/guia/2026-11-19-2207-registro-decreto.md, tabla "v0.5 → v0.6 generada" (leído 2026-11-20)
- [HIPÓTESIS] Si el Vicerrector tiene el decreto en la mano mientras ve la presentación, va a ver dos nombres para la misma unidad; y si el nombre nuevo es una decisión, el decreto necesita una v0.7 antes de circular. Lo confirmaría que la titular diga cuál de los dos nombres vale y si la Decana lo sabe.
- [PROPUESTA] Para hoy, sin tocar archivos: que la titular decida un solo nombre para decirlo en voz alta, y que si le preguntan diga que el nombre de esa Dirección está en ajuste. Se apoya en que la diferencia está en diez láminas y no se corrige en minutos.

ALERTA 2. Dentro de la misma presentación, la lámina 7 dice "Áreas" y el resto dice "Direcciones". [HECHO] El organigrama de la lámina 7 es una imagen cuyos recuadros dicen "Área de Docencia" y "Área de Investigación", con la leyenda "articulación entre áreas" y la frase "lineamientos técnicos de ambas áreas a las cuatro sedes"; el rótulo lateral sí dice "Direcciones de área". Fuente: imagen "Picture 33" de la lámina 7 de Presentacion_VRA_ejecutiva_v0.3.pptx (vista 2026-11-20)
- [HECHO] Los organigramas pequeños de las láminas 16 a 20, que son formas y no imagen, dicen "Dirección de Docencia" y "Dirección de Investigación": la lámina 7, que es la única de estructura que se expone, quedó con el vocabulario de la v0.4 del decreto. Fuente: Presentacion_VRA_ejecutiva_v0.3.pptx, láminas 16 a 20 (leído 2026-11-20)
- [HECHO] El guion hace decir en la lámina 7 "dos Direcciones de área, la Dirección de Docencia y la Dirección de Investigación", mientras la pantalla muestra "Área de Docencia" y "Área de Investigación": lo que se dice no coincide con lo que se ve. Fuente: Guion_VRA_ejecutiva_v0.1.pdf, página 2, contra la imagen de la lámina 7 (leído 2026-11-20)
- [HECHO] El recuadro "Área de Investigación" de esa imagen enumera cuatro frentes ("línea basal · investigación · vinculación con el medio · proyectos"), y las láminas 14 y 19 dicen tres ("línea basal, investigación y vinculación con el medio"), igual que el artículo 10. Fuente: imagen de la lámina 7 y láminas 14 y 19 de la v0.3, contra el artículo 10 del decreto vigente (leído 2026-11-20)
- [HIPÓTESIS] La imagen fue generada antes del cambio de nombres y nadie la rehízo porque el texto de una imagen no se corrige al buscar y reemplazar. Lo confirmaría quien armó la v0.3.
- [PROPUESTA] Si no se alcanza a rehacer la imagen, que la titular diga al mostrarla "las dos áreas, cada una con su Dirección", que es lo que la lámina muestra de verdad con su rótulo lateral. Se apoya en que es la única lámina de estructura dentro de los cinco minutos.

ALERTA 3. El archivo PowerPoint lleva dentro tres comentarios de otra persona, con nombre y correo institucional. [HECHO] La v0.3 contiene tres comentarios incrustados, escritos el 2026-11-16 por "Carolina Gonzalez Reyes" (cuenta carolina.gonzalez@uss.cl), los tres marcados como resueltos; el comparador no los muestra. Fuente: ppt/comments/ y ppt/authors.xml dentro de Presentacion_VRA_ejecutiva_v0.3.pptx (leído 2026-11-20)
- [HECHO] En la lámina 7 (organigrama): "Veo que lo dejaste igual a como lo habías planteado en nuestra ruenión y pensé que lo ibas a cambiar por el aporte de Manuel...". Fuente: ppt/comments/modernComment_110_0.xml de la v0.3 (leído 2026-11-20)
- [HECHO] En la lámina 10 (cifras del anexo): "Falta la etapa 3 en esta diapositiva". Fuente: ppt/comments/modernComment_115_0.xml de la v0.3 (leído 2026-11-20)
- [HECHO] En la lámina 14 (macro y micro): "La Dirección Nacional entrega a la Facultad la información de las funciones misionales (no a las Vicerrectorías)". Fuente: ppt/comments/modernComment_116_0.xml de la v0.3 (leído 2026-11-20)
- [HECHO] Los comentarios resueltos no se ven al proyectar, pero viajan con el archivo y cualquiera que lo abra en PowerPoint puede leerlos en el panel de comentarios; lo mismo vale para las notas del orador y para las cuatro láminas ocultas. Fuente: estructura interna de Presentacion_VRA_ejecutiva_v0.3.pptx (revisado 2026-11-20)
- [HIPÓTESIS] El comentario de la lámina 7 dice que el organigrama quedó "igual" pese a un aporte de un tercero; no sé si ese aporte se incorporó después ni quién es "Manuel". Lo confirmaría la titular; si el aporte era sobre los nombres o la forma del organigrama, es un origen de cambios que debo registrar.
- [PROPUESTA] No enviar el archivo .pptx a la Vicerrectoría: si piden la presentación, mandar un PDF exportado sin láminas ocultas ni notas, o una copia con los comentarios borrados. Se apoya en que el archivo lleva comentarios internos, notas con respuestas preparadas y láminas de trabajo.

ALERTA 4. Una ficha del anexo pone bajo "EL DECRETO DICE" palabras que el decreto no dice. [HECHO] La lámina 19 pone bajo "EL DECRETO DICE": "Gestiona la investigación, la vinculación con el medio y el desarrollo de proyectos del Departamento, en alineación de la Decanatura y con las Vicerrectorías y unidades institucionales competentes"; el artículo 10 dice que la Dirección de Proyectos "tendrá a su cargo la gestión de las líneas y los proyectos del Departamento en esas materias, en coordinación con las Vicerrectorías y unidades institucionales competentes", sin mencionar a la Decanatura ni la palabra "alineación". Fuente: Presentacion_VRA_ejecutiva_v0.3.pptx, lámina 19, contra el artículo 10 del decreto vigente (leído 2026-11-20)
- [HECHO] La lámina 17 resume el artículo 9 sin la parte que la titular agregó en la versión vigente: que el Comité Consultivo es "instancia de articulación interna" y que en él "se consolidarán la información y los indicadores levantados por las Direcciones de área y las Direcciones de Sede". Fuente: Presentacion_VRA_ejecutiva_v0.3.pptx, lámina 17, contra el artículo 9 del decreto vigente (leído 2026-11-20)
- [HECHO] La lámina 20 resume el artículo 11 sin lo que la titular agregó en la versión vigente: "mantener la relación con las carreras" y "que el Departamento conozca la realidad y la identidad de cada sede". Fuente: Presentacion_VRA_ejecutiva_v0.3.pptx, lámina 20, contra el artículo 11 del decreto vigente (leído 2026-11-20)
- [HECHO] Las láminas 16 (artículo 8) y 18 (artículo 10, Docencia) resumen fielmente el decreto; la 16 omite la subrogación, lo que no altera el sentido. Fuente: Presentacion_VRA_ejecutiva_v0.3.pptx, láminas 16 y 18, contra los artículos 8 y 10 del decreto vigente (leído 2026-11-20)
- [HECHO] Bajo "FUNCIONES", la lámina 16 atribuye a la Dirección Nacional elaborar el Plan de Desarrollo, acordar horas con las unidades de origen, proponer convenios y dar cuenta anual a la Decana y al Consejo de Facultad; ninguna de esas cuatro cosas está en el texto del decreto, que no usa las palabras "cuenta", "convenio" ni "horas". Fuente: búsqueda de texto sobre decreto-depto-salud-digital-v0.6.docx y lámina 16 de la v0.3 (ejecutado 2026-11-20)
- [HIPÓTESIS] Esas funciones vienen del documento "Funciones del director(a) del Departamento de Salud Digital" que la titular revisó el 2026-11-17, y no del decreto. Lo confirmaría la titular; conviene saberlo porque la lámina se rotula "RESPALDO · ARTÍCULO 8" y el guion la usa para responder "¿Qué recursos pide?".
- [HECHO] Las notas de la lámina 11 citan el artículo 1 sin "la gobernanza de la salud digital", que la titular pidió incluir y está en el decreto vigente; es el texto de una versión anterior, y el guion manda a esas notas para responder "¿Qué es la salud digital?". Fuente: notas de la lámina 11 de la v0.3 contra el artículo 1 del decreto vigente, y Guion_VRA_ejecutiva_v0.1.pdf, página 3 (leído 2026-11-20)
- [HECHO] La lámina 6 dice "Responde al artículo 3: un marco común de desempeños sustentado en la investigación del Departamento y en los estándares nacionales e internacionales"; el artículo 3 b) dice "en los estándares internacionales de competencias en salud digital", sin "nacionales", y la versión de la titular del 2026-11-16 decía solo "internacionales". Fuente: lámina 6 de la v0.3, artículo 3 b) del decreto vigente y 2026-11-16-presentacion-de-la-titular.pdf (leído 2026-11-20)
- [HIPÓTESIS] "Nacionales e" se agregó para hacer lugar al modelo de CENS; es razonable, pero entonces lo que quedó corto es el decreto. Lo confirmaría la titular, y sería otro cambio para una v0.7.

ALERTA 5. Tres afirmaciones de la exposición van más lejos que lo que el benchmark verificó. [HECHO] La presentación afirma que ninguno de los 35 marcos incluye IA en la lámina 2 ("que ninguno de los 35 marcos revisados por la OMS tiene"), en la 3 ("0 de 35"), en la 10 ("35 → 0 incluyen IA") y en las notas de la lámina 2; el guion lo repite tres veces. Fuente: texto completo de Presentacion_VRA_ejecutiva_v0.3.pptx y Guion_VRA_ejecutiva_v0.1.pdf (leído 2026-11-20)
- [HECHO] Lo que el benchmark verificó en el documento de la OMS es más acotado: ninguno de los 10 grupos de competencias es de IA y los términos "artificial intelligence" o "AI" no aparecen en la tabla de grupos ni en el mapeo, que además se hizo sobre 31 marcos y no sobre 35; no verificó marco por marco que ninguno mencione la IA. Fuente: produccion/benchmark/2026-11-11-1401-marcos-competencias-verificacion-primaria.md, sección 1 (leído 2026-11-20)
- [HECHO] La lámina 6 usa la formulación que sí está verificada: "Ningún grupo dedicado a inteligencia artificial". Fuente: Presentacion_VRA_ejecutiva_v0.3.pptx, lámina 6 (leído 2026-11-20)
- [HECHO] La lámina 3 dice "El único marco nacional de América Latina quedó fuera de la revisión" y la 10 "sólo existe 1 marco nacional en América Latina que no fue considerado"; el benchmark dice que el de CENS es "el único marco de competencias nacional latinoamericano encontrado", en una búsqueda que declara superficial y que no revisó Brasil, Argentina ni Uruguay, y que la OMS "no dice que existan marcos latinoamericanos excluidos". Fuente: produccion/benchmark/2026-11-11-1334-marcos-competencias-salud-digital.md, líneas 106 y 118, y produccion/benchmark/2026-11-11-1401-marcos-competencias-verificacion-primaria.md, sección 4 (leído 2026-11-20)
- [HECHO] Las versiones anteriores (la de la sesión y la de la titular del 2026-11-16) decían "ningún marco nacional es de América Latina", que es lo verificado; "el único" y "quedó fuera" aparecen recién en la ejecutiva. Fuente: scripts/comparar_versiones.py entre las versiones anteriores y la v0.3 (ejecutado 2026-11-20)
- [HECHO] El modelo de CENS salió en 2024 y en español, y la revisión de la OMS cubrió literatura en inglés de 2012 a 2022: "quedó fuera" puede oírse como una omisión de la OMS cuando en rigor no cumplía sus criterios. Fuente: produccion/benchmark/2026-11-11-1401-marcos-competencias-verificacion-primaria.md, secciones 1 y 4 (leído 2026-11-20)
- [HECHO] El benchmark registra que el marco TIGER, actualizado en 2026, recomienda tratar la IA en todos los dominios y roles de enfermería; quien conozca el tema puede oponerlo a "ningún marco incluye IA". Fuente: produccion/benchmark/2026-11-11-1401-marcos-competencias-verificacion-primaria.md, sección 2 (leído 2026-11-20)
- [HECHO] La presentación no nombra el modelo de CENS como marco (solo cita a CENS por la cifra de 3.500), y el perfil dice que el modelo de la titular "no compite con el de CENS: lo complementa" y que "CENS será citado". Fuente: texto completo de la v0.3 y perfil/cargo.md (leído 2026-11-20)
- [PROPUESTA] Decir hoy la versión verificada: "la OMS revisó 35 marcos, los ordenó en 10 grupos de competencias y ninguno de esos grupos es de inteligencia artificial; tampoco hay ningún marco nacional de América Latina; el chileno, de CENS, es de 2024 y lo vamos a complementar". Se apoya en las líneas anteriores del benchmark y en el perfil.

ALERTA 6. El guion declara corresponder a la presentación v0.1 y lo que se entregó es la v0.3. [HECHO] La segunda línea del guion dice "20 de noviembre de 2026 · Presentacion_VRA_ejecutiva_v0.1.pptx"; el archivo entregado es `Presentacion_VRA_ejecutiva_v0.3.pptx`. Fuente: Guion_VRA_ejecutiva_v0.1.pdf, página 1 (leído 2026-11-20)
- [HECHO] Según los metadatos, el PDF del guion se generó unas cuatro horas después del último guardado de la v0.3 y aun así nombra la v0.1. Fuente: pdfinfo sobre Guion_VRA_ejecutiva_v0.1.pdf y propiedades internas de la v0.3 (ejecutado 2026-11-20)
- [HECHO] Pese al rótulo, el guion calza con la v0.3 lámina por lámina en orden, títulos y cifras, con la sola excepción de la lámina 7 (alerta 2); el detalle está en la sección "Guion contra presentación". Fuente: cotejo propio de Guion_VRA_ejecutiva_v0.1.pdf contra la v0.3 (ejecutado 2026-11-20)
- [HIPÓTESIS] El guion se escribió contra la v0.1 y los cambios de la v0.2 y la v0.3 no tocaron lo que el guion describe, o el guion se regeneró sin actualizar el rótulo. No puedo distinguirlo sin la v0.1 y la v0.2; lo confirmaría quien lo redactó.

ALERTA 7. El guion hace decir cosas que no constan en ningún archivo del repositorio. [HECHO] El guion responde a "¿En qué va el decreto?" que "se presentó al Consejo de Facultad el 12 de noviembre y desde entonces se ha ajustado con sus observaciones"; en mi registro del decreto todos los cambios posteriores vienen de la titular, de la Decana o de la sesión principal, y ninguno está atribuido a observaciones del Consejo de Facultad. Fuente: Guion_VRA_ejecutiva_v0.1.pdf, página 3, y produccion/guia/2026-11-19-2207-registro-decreto.md (leído 2026-11-20)
- [HECHO] El guion responde a "¿Qué recursos pide?" que "la nueva oferta de postgrado y educación continua abre una fuente de ingresos"; esa afirmación no está en la presentación ni en el decreto. Fuente: Guion_VRA_ejecutiva_v0.1.pdf, página 3, y búsqueda de "ingresos" en la v0.3 y en el decreto vigente (ejecutado 2026-11-20)
- [HECHO] La ruta del decreto "según el precedente del DR 116" (lámina 8 y guion) no tiene respaldo en el repositorio: las notas del decreto dejan como hipótesis incluso el número del decreto 116/2020, porque nadie abrió ese documento. Fuente: entregables/2026-11-14-decreto/revision-articulo-por-articulo.md, línea 18 (leído 2026-11-20)
- [PROPUESTA] Que la titular diga "con sus observaciones" solo si el Consejo de Facultad las hizo; si no, "desde entonces se ha ajustado". Se apoya en que el Vicerrector puede preguntar cuáles fueron.

ALERTA 8. Dos nombres distintos para el plan de la Facultad. [HECHO] Las láminas 2 (notas) y 4 y el guion citan el "Plan de Desarrollo de la Facultad 2022–2029 (p. 13)"; el visto 1 del decreto cita el "Plan Estratégico de la Facultad de Ciencias para el Cuidado de la Salud 2025–2029". Fuente: Presentacion_VRA_ejecutiva_v0.3.pptx, láminas 2 y 4, Guion_VRA_ejecutiva_v0.1.pdf, página 1, y visto 1 del decreto vigente (leído 2026-11-20)
- [HECHO] Ninguno de los dos documentos de la Facultad, ni el PDI, están en el repositorio: no puedo decir si son dos planes distintos o uno mal citado, ni comprobar las páginas y los ejes que cita la lámina 2. Fuente: búsqueda de "FODA", "2025–2029" y "Eje 4" en el repositorio (ejecutado 2026-11-20)
- [HIPÓTESIS] Son dos documentos distintos (un plan de desarrollo 2022–2029 con FODA y un plan estratégico 2025–2029) y ambos nombres son correctos. Lo confirmaría la titular, que tiene los dos; si es uno solo, hay que corregir el decreto o la presentación.

ALERTA 9. Quedan restos de versiones anteriores y notas internas a la vista. Ninguno es grave por separado; los enumero porque mi definición me pide avisar.
- [HECHO] No queda ninguna "Coordinación", "Jefatura" ni "Área de Proyectos" en el texto de la v0.3; el único resto de "Áreas" es la imagen de la lámina 7 (alerta 2). Fuente: búsqueda de texto sobre el contenido completo de la v0.3 (ejecutado 2026-11-20)
- [HECHO] La lámina 12 conserva "Otras facultades: ingeniería, derecho y otras"; la titular quitó "en especial la ingeniería y el derecho" de los artículos 2 y 9 del decreto, por un motivo que sigue sin constar. Fuente: Presentacion_VRA_ejecutiva_v0.3.pptx, lámina 12, y produccion/guia/2026-11-19-2207-registro-decreto.md (leído 2026-11-20)
- [HECHO] La lámina 13 termina con una nota de diseño a la vista: "No es un proceso paso a paso: es el mapa de intercambios. Sirve como lámina de entrada antes del flujo"; además ya no es cierto, porque en la v0.3 el flujo es la lámina 12 y va antes. Fuente: Presentacion_VRA_ejecutiva_v0.3.pptx, láminas 12 y 13 (leído 2026-11-20)
- [HECHO] La lámina 14 muestra "centro de costos (en evaluación)" y la lámina 8 "El paso por Secretaría General está por confirmar": son pendientes internos escritos en pantalla; el segundo está en la exposición. Fuente: Presentacion_VRA_ejecutiva_v0.3.pptx, láminas 8 y 14 (leído 2026-11-20)
- [HECHO] Las láminas 21 a 24 están ocultas pero siguen en el archivo: tres portadillas ("Cómo se articula", "Ámbito operativo", "Qué dice el decreto actualmente") y una lámina sin título con "Limitaciones, Proyecciones, Plan de desarrollo, Plan estratégico"; esta última ya venía al final de la versión del 2026-11-16. Fuente: Presentacion_VRA_ejecutiva_v0.3.pptx y 2026-11-16-presentacion-de-la-titular.pdf (leído 2026-11-20)
- [HECHO] Erratas visibles: lámina 3, "profesionales.Y los marcos" (falta un espacio); lámina 10, "35 → 0 incluyen IA / marcos de competencias en salud digital revisó la OMS" (la frase quedó cortada al cambiar la cifra) y "Profesionales" con mayúscula a mitad de tarjeta; lámina 19, "en alineación de la Decanatura". Fuente: Presentacion_VRA_ejecutiva_v0.3.pptx, láminas 3, 10 y 19 (leído 2026-11-20)
- [HECHO] La lámina 15 dice "Más dos artículos transitorios", que es correcto frente al decreto vigente; la versión de la sesión y la del 2026-11-16 decían "tres". Fuente: scripts/comparar_versiones.py entre las versiones anteriores y la v0.3, y decreto vigente (ejecutado 2026-11-20)

ALERTA 10. Otros documentos quedaron desactualizados frente a la v0.3. [HECHO] `presentacion-vicerrector.pptx` y su PDF (Áreas, Jefaturas, Coordinaciones, "tres artículos transitorios", el nombre de la titular y "con proyección doctoral" en la lámina de la línea basal) y `generar_presentacion.py`, que los regenera, ya no corresponden a lo que la titular va a presentar. Fuente: scripts/comparar_versiones.py entre presentacion-vicerrector.pptx y la v0.3 (ejecutado 2026-11-20)
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
