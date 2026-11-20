---
agente: guia
fecha: 2026-11-20
titulo: Registro de versiones del decreto de creación del Departamento Nacional de Salud Digital (v0.3 a v0.7)
reemplaza: produccion/guia/2026-11-19-2207-registro-decreto.md
---

# Registro de versiones: decreto de creación del Departamento Nacional de Salud Digital

Este registro reemplaza al del 2026-11-19 y cuenta toda la historia, de la v0.3 a la v0.7. Primero va lo nuevo (la v0.7, creada hoy por la sesión principal); al final copio íntegro el registro anterior, sin tocar su texto, salvo que a sus alertas les antepuse "(registro 2026-11-19)" para que no se confundan con las de hoy. Hoy, 2026-11-20, es la reunión con el Vicerrector Académico.

## Qué revisé y cómo

- [HECHO] Comparé `decreto-depto-salud-digital-v0.6.docx` con `decreto-depto-salud-digital-v0.7.docx` con el comparador, saqué la huella de los dos Word y de los dos PDF, y leí completo el texto de la v0.7. Fuente: salida de scripts/comparar_versiones.py sobre entregables/2026-11-14-decreto/ (ejecutado 2026-11-20)
- [HECHO] La v0.6 no fue tocada: conserva la huella `57c2f7ad3f01` que registré el 2026-11-19, de modo que la v0.7 es un archivo nuevo con número nuevo y no un reemplazo con el mismo nombre. Fuente: scripts/comparar_versiones.py sobre decreto-depto-salud-digital-v0.6.docx (ejecutado 2026-11-20)
- [HECHO] Para comprobar que no se tocó el formato comparé, párrafo por párrafo, estilo, alineación, sangrías, espaciado y negrita, cursiva, subrayado, fuente y tamaño de cada tramo de texto, además del tamaño de página y los márgenes: no hay ninguna diferencia entre la v0.6 y la v0.7. Fuente: comparación propia con python-docx sobre los dos archivos Word (ejecutado 2026-11-20)
- [HECHO] El PDF de la v0.7 tiene exactamente el mismo texto que su Word (9.997 caracteres sin espacios en ambos), 4 páginas igual que el de la v0.6, y fue generado con LibreOffice el 2026-11-20 a las 01:06 UTC. Fuente: pdftotext y pdfinfo sobre decreto-depto-salud-digital-v0.7.pdf (ejecutado 2026-11-20)
- [HECHO] Leí `hacer_v07.py`: hace cuatro reemplazos de texto sobre el Word de la v0.6 (rótulo, errata, enumeración del artículo 7 y nombre en el artículo 10) y nada más; recibe las rutas como argumentos, así que no sobrescribe nada por sí solo. Fuente: entregables/2026-11-14-decreto/hacer_v07.py (leído 2026-11-20)
- [HECHO] La v0.7, su PDF, el guion de hoy y la presentación de hoy ya están confirmados en git (confirmación cc2af91, "Guion ajustado a la presentación del 20 de noviembre y decreto v0.7 con cambios de forma y de nombre"). Fuente: git log sobre entregables/ (revisado 2026-11-20)
- [HECHO] Quién pidió y quién aplicó cada cambio me lo informó la sesión principal al encargarme este registro; yo no presencié la conversación con la titular. Donde me dijo "no consta", escribo "no consta". Fuente: encargo de la sesión principal al Guía, que cita a la titular del cargo (conversaciones 2026-11-17 y 2026-11-20; recibido 2026-11-20)
- [HECHO] `produccion/gestor-cargo/`, `produccion/brechas-indicadores/` y `produccion/actas/` siguen vacías; no afecta a este registro. Fuente: listado de produccion/ (revisado 2026-11-20)

### Huellas

| Archivo | Rótulo interno | Huella | Párrafos | Palabras |
|---|---|---|---|---|
| `Decreto_Depto_SD_v0.3_borrador.docx` (Drive de la titular, no está en el repositorio) | v0.3 | sin huella | no consta | no consta |
| `entregables/2026-11-14-decreto/decreto-depto-salud-digital-v0.4.docx` | versión 0.4 | `0f8915b2c4ae` | 40 | 1728 |
| `entregables/2026-11-14-decreto/decreto-depto-salud-digital-v0.5.docx` | versión 0.5 | `47cde9559f0c` | 40 | 1758 |
| `versiones-recibidas/2026-11-17-0-v0.6-generada-por-sesion.docx` | versión 0.6 | `9b886f602c28` | 40 | 1780 |
| `versiones-recibidas/2026-11-17-a-v0.6-editada-por-titular.docx` | versión 0.6 | `4ed4b047dad4` | 40 | 1727 |
| `versiones-recibidas/2026-11-17-b-v0.6-iterada-por-titular.docx` | versión 0.6 | `57c2f7ad3f01` | 39 | 1807 |
| `entregables/2026-11-14-decreto/decreto-depto-salud-digital-v0.6.docx` | versión 0.6 | `57c2f7ad3f01` | 39 | 1807 |
| `entregables/2026-11-14-decreto/decreto-depto-salud-digital-v0.7.docx` (la más reciente) | versión 0.7 | `d6cc1312e4a5` | 39 | 1810 |
| `entregables/2026-11-14-decreto/decreto-depto-salud-digital-v0.7.pdf` | versión 0.7 | `0d672f44756b` (huella de PDF; no es comparable con la del Word) | 140 líneas | 1811 |
| `entregables/2026-11-14-decreto/resumen-ejecutivo.docx` | sin número | `f17771776ab6` (sin cambios) | 30 | 650 |

## Alertas de hoy

Van de mayor a menor gravedad. Todas están comprobadas en los archivos, salvo donde digo que es hipótesis.

ALERTA 1. La v0.7 cambia un nombre que definió la Decana, y lo hace dentro de un encargo que pedía "cambios mínimos, no de contenido". [HECHO] En la v0.7, "Dirección de Proyectos" pasa a "Dirección de Investigación" en los artículos 7 y 10; "Dirección de Proyectos" ya no aparece en ninguna parte del decreto y "Dirección de Investigación" aparece dos veces. Fuente: scripts/comparar_versiones.py v0.6 contra v0.7 y búsqueda de texto sobre decreto-depto-salud-digital-v0.7.docx (ejecutado 2026-11-20)
- [HECHO] El nombre "Dirección de Proyectos" entró en la v0.6 como nombre final definido por la Decana y transmitido por la titular el 2026-11-17; es, por lo tanto, un cambio ya aplicado que desaparece en la versión nueva, y mi definición me obliga a alertarlo. Fuente: produccion/guia/2026-11-19-2207-registro-decreto.md, tabla "v0.5 → v0.6 generada" (leído 2026-11-20)
- [HECHO] La titular pidió hoy "decreto en nueva versión con cambios mínimos, no de contenido"; la sesión principal aplicó el cambio de nombre como alineación con la presentación, apoyada en la regla que la titular fijó el 2026-11-17 de que el decreto use las mismas palabras que la presentación, y declara que se lo va a advertir porque puede considerarse cambio de contenido. Fuente: encargo de la sesión principal al Guía, que cita a la titular del cargo (conversaciones 2026-11-17 y 2026-11-20; recibido 2026-11-20)
- [HECHO] No consta quién decidió el nombre "Dirección de Investigación" ni si la Decana lo sabe: en la presentación apareció entre la versión de la titular del 2026-11-16 y la ejecutiva v0.3, sin atribución, y el encargo de hoy repite que no consta. Fuente: produccion/guia/2026-11-20-0026-registro-presentacion-vra.md, alerta 1, y encargo de la sesión principal al Guía (leído y recibido 2026-11-20)
- [HECHO] El cambio no es solo de rótulo, porque el artículo 10 de la v0.7 queda diciendo "La Dirección de Investigación, que comprende la línea basal, la investigación y la vinculación con el medio, tendrá a su cargo la gestión de las líneas y los proyectos del Departamento": una Dirección llamada "de Investigación" que comprende la investigación como una de tres partes y que además lleva la vinculación con el medio y los proyectos. Fuente: entregables/2026-11-14-decreto/decreto-depto-salud-digital-v0.7.docx, artículo 10 (leído 2026-11-20)
- [HECHO] La palabra "proyectos" sigue en el decreto cinco veces (artículos 1, 2, 5 y 10), como función del Departamento ("desarrollo de proyectos") y como parte de la línea basal ("de investigación y proyectos"), pero ya no da nombre a ninguna Dirección. Fuente: búsqueda de texto sobre decreto-depto-salud-digital-v0.7.docx (ejecutado 2026-11-20)
- [HIPÓTESIS] Quien lea el decreto puede preguntar por qué la vinculación con el medio y los proyectos dependen de una Dirección "de Investigación", o si con el nombre nuevo los proyectos quedaron sin dueño; con "Dirección de Proyectos" esa pregunta no existía. Lo confirmaría la lectura de la Decana o del Vicerrector.
- [HIPÓTESIS] Si la Decana sigue pensando en "Dirección de Proyectos", la v0.7 y la presentación de hoy la contradicen frente al Vicerrector. Lo confirmaría que la titular diga quién decidió el nombre nuevo y si la Decana lo aprobó.
- [PROPUESTA] Que la v0.7 no salga del repositorio (ni a la Decana, ni a la Vicerrectoría, ni a Secretaría General) hasta que la titular confirme el nombre; si el nombre no vale, se hace una v0.8 que lo devuelva, nunca otra "v0.7". Se apoya en que el nombre anterior lo definió la Decana y en la alerta 1 del registro anterior sobre tres archivos con el mismo número.
- [PROPUESTA] Si hoy el Vicerrector pide el texto del decreto, que la titular decida antes de la reunión cuál entrega: la v0.7 calza con lo que va a mostrar y decir; la v0.6 es la última que consta como decidida por ella artículo por artículo. Se apoya en las líneas anteriores.

ALERTA 2. La redacción nueva del artículo 7 nace de una observación mía y no de una petición de la titular. [HECHO] El artículo 7 pasó de "integrada por la Dirección Nacional, la Dirección de Docencia y la Dirección de Proyectos, en adelante 'las Direcciones de área', las Direcciones de Sede y sus académicos" a "integrada por la Dirección Nacional; por la Dirección de Docencia y la Dirección de Investigación, en adelante 'las Direcciones de área'; por las Direcciones de Sede, y por sus académicos". Fuente: scripts/comparar_versiones.py v0.6 contra v0.7 (ejecutado 2026-11-20)
- [HECHO] La ambigüedad que corrige (que la Dirección Nacional pudiera leerse como Dirección de área) la anoté yo el 2026-11-19 como hipótesis, bajo "lo que me llama la atención", y dije que decidía la titular; la sesión principal la aplicó hoy por su cuenta dentro del encargo de cambios mínimos. Fuente: produccion/guia/2026-11-19-2207-registro-decreto.md, sección "Lo que me llama la atención del texto vigente", y encargo de la sesión principal al Guía (leído y recibido 2026-11-20)
- [HIPÓTESIS] La redacción nueva dice lo mismo con menos riesgo de mala lectura y no cambia el fondo; aun así es un artículo de organización redactado sin que la titular lo haya visto. Lo confirmaría que ella lo lea y lo acepte.

ALERTA 3. Otros documentos quedaron desactualizados frente a la v0.7. [HECHO] `resumen-ejecutivo.docx` dice "Dirección de Proyectos" y no dice "Dirección de Investigación"; a los cinco desajustes que ya tenía con la v0.6 (alerta 2 del registro anterior) se suma ahora el nombre. Fuente: búsqueda de texto sobre entregables/2026-11-14-decreto/resumen-ejecutivo.docx (ejecutado 2026-11-20)
- [HECHO] `revision-articulo-por-articulo.md` no menciona la v0.7 ni el nombre "Dirección de Investigación": las notas de la sesión siguen terminando en la v0.6. Fuente: búsqueda de "0.7" e "Investigación" en entregables/2026-11-14-decreto/revision-articulo-por-articulo.md (ejecutado 2026-11-20)
- [HECHO] `generar_decreto.py` quedó bloqueado (se detiene con un mensaje antes de escribir), lo que resuelve la alerta 5 del registro anterior; pero el mensaje dice que "la versión vigente del decreto es la editada por la titular (decreto-depto-salud-digital-v0.6.docx)", que ya no es la más reciente. Fuente: entregables/2026-11-14-decreto/generar_decreto.py, líneas 189 a 198 (leído 2026-11-20)
- [HECHO] `perfil/cargo.md` describe la estructura como "Área de Docencia" y "Área de Proyectos" y habla de "Coordinaciones de Sede": está dos cambios de nombre atrás. Fuente: perfil/cargo.md, líneas 21 y 24 (leído 2026-11-20)
- [HECHO] Siguen sin tocar la guía y el guion del 2026-11-15 (Áreas, Jefaturas, tres transitorios), la presentación generada del 2026-11-15 y el PDF de la titular del 2026-11-16, que dice "Dirección de Proyectos"; todos quedan como históricos. Fuente: produccion/guia/2026-11-20-0026-registro-presentacion-vra.md, alerta 10, y listado de entregables/ sin cambios en esas carpetas según git log (revisado 2026-11-20)
- [PROPUESTA] Que la titular actualice `perfil/cargo.md` cuando cierre el nombre; yo no edito el perfil. Se apoya en la línea de perfil/cargo.md citada arriba.
- [PROPUESTA] No entregar el resumen ejecutivo a nadie: hoy contradice al decreto en seis puntos. Se apoya en la primera línea de esta alerta y en la alerta 2 del registro anterior.

ALERTA 4. Lo que la presentación de hoy sigue atribuyendo al decreto y la v0.7 no dice. El detalle está en el registro de la presentación de hoy; aquí dejo lo que toca al decreto.
- [HECHO] Con la v0.7, los nombres del decreto y los del texto de la presentación de hoy calzan (Dirección Nacional, Dirección de Docencia, Dirección de Investigación, Direcciones de área, Direcciones de Sede, Comité Consultivo, dos transitorios); la única excepción es la imagen de la lámina 7, que sigue diciendo "Área de Docencia" y "Área de Investigación". Fuente: decreto-depto-salud-digital-v0.7.docx y texto e imágenes de entregables/2026-11-20-presentacion-vra-ejecutiva/2026_11_20_Propuesta_Departamento_Salud_Digital_USS.pptx (leídos 2026-11-20)
- [HECHO] La lámina 19 sigue poniendo bajo "EL DECRETO DICE" la frase "en alineación de la Decanatura", que el artículo 10 de la v0.7 no contiene; las láminas 17 y 20 siguen resumiendo los artículos 9 y 11 sin lo que la titular agregó en la v0.6; y las notas de la lámina 11 citan el artículo 1 sin "la gobernanza de la salud digital". Fuente: láminas 11, 17, 19 y 20 de la presentación de hoy contra los artículos 1, 9, 10 y 11 de la v0.7 (leído 2026-11-20)
- [HECHO] El visto 1 no se tocó, por instrucción: sigue citando el "Plan Estratégico de la Facultad de Ciencias para el Cuidado de la Salud 2025–2029", y la presentación de hoy sigue citando el "Plan de Desarrollo de la Facultad 2022–2029 (p. 13)". Fuente: visto 1 de la v0.7 y láminas 2 (notas) y 4 de la presentación de hoy (leído 2026-11-20)

ALERTA 5. Un detalle técnico del archivo, sin efecto visible. [HECHO] El Word de la v0.7 contiene dos piezas internas que la v0.6 no tenía (un encabezado y un pie de página, ambos vacíos) y pesa menos (30.605 bytes contra 33.151), porque el script lo volvió a guardar con python-docx en lugar de Word; el texto, el formato párrafo por párrafo y el número de páginas del PDF son iguales. Fuente: listado interno de los dos archivos .docx y pdfinfo (ejecutado 2026-11-20)
- [HIPÓTESIS] No cambia nada a la vista; lo anoto porque el encargo dice "sin tocar el formato" y yo comparé propiedades y texto, no la imagen de cada página. Lo confirmaría que la titular abra la v0.7 en Word y la hojee.

## Qué cambió de la v0.6 a la v0.7 (2026-11-20). Aplicó: sesión principal, con `hacer_v07.py`

- [HECHO] El comparador muestra exactamente cuatro párrafos distintos (rótulo, artículo 1, artículo 7 y artículo 10) y ninguno más; el texto pasa de 1807 a 1810 palabras y mantiene 39 párrafos, 13 artículos y 2 transitorios. Fuente: scripts/comparar_versiones.py v0.6 contra v0.7 (ejecutado 2026-11-20)
- [HECHO] Comprobé que no se tocó lo que el encargo dice que no se tocó: el visto 1, el artículo 3 b) ("estándares internacionales", sin "nacionales"), el artículo 13 y los dos transitorios son idénticos en ambas versiones. Fuente: scripts/comparar_versiones.py v0.6 contra v0.7 y lectura de la v0.7 (ejecutado 2026-11-20)

| Lugar | Qué decía (v0.6) | Qué dice (v0.7) | Quién lo sugirió | Por qué | Consta en |
|---|---|---|---|---|---|
| Rótulo | "Propuesta de decreto · versión 0.6 · documento de trabajo" | "Propuesta de decreto · versión 0.7 · documento de trabajo" | Titular pidió versión nueva; el Guía había propuesto que el siguiente cambio fuera v0.7 | "Decreto en nueva versión con cambios mínimos, no de contenido" | Encargo, conversación 2026-11-20; registro anterior, alerta 1; comparador |
| Artículo 1 | "…del campo.. Para ello" | "…del campo. Para ello" | Guía (alerta 7 del registro anterior); aplicó la sesión principal | Errata | Registro anterior; encargo; comparador |
| Artículo 7 | "integrada por la Dirección Nacional, la Dirección de Docencia y la Dirección de Proyectos, en adelante 'las Direcciones de área', las Direcciones de Sede y sus académicos, y contará con un Comité Consultivo" | "integrada por la Dirección Nacional; por la Dirección de Docencia y la Dirección de Investigación, en adelante 'las Direcciones de área'; por las Direcciones de Sede, y por sus académicos, y contará con un Comité Consultivo" | Enumeración: observación del Guía (2026-11-19); redactó y aplicó la sesión principal. No consta que la titular haya visto la redacción | Que "las Direcciones de área" no incluya a la Dirección Nacional | Registro anterior, "Lo que me llama la atención"; encargo; comparador |
| Artículos 7 y 10 | "Dirección de Proyectos" | "Dirección de Investigación" | Aplicó la sesión principal como alineación de nombre. Quién decidió el nombre: no consta. Si la Decana lo sabe: no consta | Regla de la titular: el decreto usa las mismas palabras que la presentación; la presentación de hoy dice "Dirección de Investigación" | Encargo, conversaciones 2026-11-17 y 2026-11-20; comparador |

- [HIPÓTESIS] El nombre "Dirección de Investigación" lo puso la titular (o quien armó la presentación ejecutiva) entre el 2026-11-16 y el 2026-11-19, y llegó al decreto por arrastre de la regla "mismas palabras", sin una decisión expresa sobre el decreto. Lo confirmaría la titular.

## Qué quedó resuelto y qué sigue del registro anterior

| Alerta u observación del 2026-11-19 | Estado al 2026-11-20 | Comprobación |
|---|---|---|
| 1. Tres archivos distintos con el rótulo "versión 0.6" | Sigue (los tres existen); la propuesta de numerar el siguiente cambio como v0.7 se cumplió y la v0.6 no se sobrescribió | Huellas |
| 2. El resumen ejecutivo afirma un resguardo que el decreto no contiene | Sigue, y se agrava: ahora también difiere el nombre de la segunda Dirección | Búsqueda de texto en el resumen |
| 3. Guía y guion del 2026-11-15 en la v0.4 | Siguen sin tocar; hay un guion nuevo para hoy, registrado aparte | Listado y git |
| 4. La presentación del repositorio no era la última | Resuelta en lo que pedía (la del 2026-11-16 ya está) y superada: hay una presentación de hoy, registrada aparte | Registro de la presentación |
| 5. Ejecutar el generador borraría la versión vigente | Resuelta: el generador está bloqueado; su mensaje quedó desactualizado | Lectura del script |
| 6. Cambios que desaparecieron y textos que volvieron | Sin novedad en los ya anotados; se suma la desaparición de "Dirección de Proyectos" (alerta 1 de hoy) | Comparador |
| 7. Errata "campo.." en el artículo 1 | Resuelta en la v0.7, en el Word y en el PDF | Comparador y pdftotext |
| 8. Las notas de la sesión no registran todo | Sigue, y ahora tampoco registran la v0.7 | Búsqueda en las notas |
| Artículo 7: la Dirección Nacional podía leerse como Dirección de área | Resuelta en la v0.7 (alerta 2 de hoy) | Comparador |
| Transitorio primero eliminado: quién es la primera Dirección Nacional y desde cuándo corre su período | Sigue sin respuesta de la Decana | No hay cambio en los transitorios |
| Sin el resguardo, "Direcciones" y "Directores" frente a los artículos 1 y 9 del Reglamento de Unidades Académicas | Sigue; nadie ha abierto el Reglamento | Sin fuente nueva |
| Género: "académicos" solo, en los artículos 2, 5 y 7 | Sigue, por instrucción de no tocarlo | Lectura de la v0.7 |
| Números de decreto y artículos citados en los vistos, sin verificar | Sigue | Sin fuente nueva |

- [HECHO] La tabla anterior resume mi cotejo de cada alerta del registro anterior contra los archivos de hoy. Fuente: produccion/guia/2026-11-19-2207-registro-decreto.md, scripts/comparar_versiones.py y lectura de entregables/2026-11-14-decreto/ (ejecutado 2026-11-20)

## Lo que me llama la atención de la v0.7

Son observaciones mías; decide la titular.

- [HECHO] El guion de hoy afirma "El decreto v0.7 usa estas mismas palabras" sobre Dirección Nacional, Dirección de Docencia, Dirección de Investigación, Direcciones de área, Direcciones de Sede y Comité Consultivo ordinario o ampliado: lo comprobé y es cierto, término por término. Fuente: Guion_reunion_VRA_2026-11-20.docx, sección "Vocabulario", contra los artículos 7 a 11 de la v0.7 (leído 2026-11-20)
- [HECHO] El guion responde "¿Cómo se mide?" con indicadores que "se definen con el Plan de Desarrollo del Departamento, una vez aprobado el decreto", y "¿Qué recursos pide?" con "el decreto no pide contrataciones" y "el presupuesto es de la Facultad"; la v0.7 no menciona un Plan de Desarrollo del Departamento (solo el "plan de implementación" del transitorio segundo y el Plan de Desarrollo Institucional del visto 1) ni usa las palabras "presupuesto", "contratación" u "horas". Fuente: búsqueda de texto sobre decreto-depto-salud-digital-v0.7.docx y Guion_reunion_VRA_2026-11-20.docx, tabla "Si pregunta…" (ejecutado 2026-11-20)
- [HIPÓTESIS] Si la titular quiere poder decir "Plan de Desarrollo del Departamento" con respaldo del decreto, es un candidato para una versión futura (por ejemplo, entre las funciones de la Dirección Nacional del artículo 8); hoy solo lo dice la presentación. Lo decidiría la titular con la Decana.
- [HECHO] La respuesta "¿Siete Direcciones no es mucho?" del guion sí reproduce los dos transitorios de la v0.7 casi palabra por palabra (instalación gradual según necesidades y disponibilidad de la Facultad; mientras no se designen las Direcciones de área, sus funciones las ejerce la Dirección Nacional). Fuente: Guion_reunion_VRA_2026-11-20.docx, tabla "Si pregunta…", contra los transitorios primero y segundo de la v0.7 (leído 2026-11-20)

## Estado

- [HECHO] Versión más reciente: `entregables/2026-11-14-decreto/decreto-depto-salud-digital-v0.7.docx`, rótulo "versión 0.7", huella `d6cc1312e4a5`, 39 párrafos, 1810 palabras, 13 artículos y 2 transitorios; su PDF (`0d672f44756b`) tiene el mismo texto. Fuente: scripts/comparar_versiones.py y cotejo de texto Word-PDF (ejecutado 2026-11-20)
- [HECHO] La v0.7 la creó la sesión principal y no consta todavía que la titular la haya leído ni aceptado; la última versión que consta como decidida por ella punto por punto es la v0.6 (`57c2f7ad3f01`), que sigue en la carpeta sin cambios. Fuente: encargo de la sesión principal al Guía (recibido 2026-11-20) y scripts/comparar_versiones.py (ejecutado 2026-11-20)
- [PROPUESTA] Tratar la v0.7 como vigente solo cuando la titular confirme el nombre "Dirección de Investigación" y la redacción del artículo 7; hasta entonces, es la versión de trabajo que calza con la presentación de hoy. Se apoya en las alertas 1 y 2.
- [HECHO] Esta es la última versión registrada. Si la titular entrega un archivo del decreto con una huella distinta de `d6cc1312e4a5` (v0.7) o de `57c2f7ad3f01` (v0.6), corresponde alerta. Fuente: este registro, escrito 2026-11-20

### Pendientes de la titular

- [PROPUESTA] Decir quién decidió "Dirección de Investigación", por qué, y si la Decana lo sabe y lo aprueba; es lo único de la v0.7 que no tiene dueño. Se apoya en la alerta 1.
- [PROPUESTA] Leer el artículo 7 de la v0.7 y decir si acepta la redacción. Se apoya en la alerta 2.
- [PROPUESTA] Decidir qué texto del decreto entrega si el Vicerrector lo pide hoy (v0.7 o v0.6) y, después de la reunión, contar qué observó él, para registrarlo como origen de los cambios que vengan. Se apoya en la alerta 1 y en que la columna "quién lo sugirió" no tiene todavía ninguna entrada del Vicerrector.
- [PROPUESTA] Aclarar si el "Plan Estratégico 2025–2029" del visto 1 y el "Plan de Desarrollo de la Facultad 2022–2029" de la presentación son dos documentos o uno. Se apoya en la alerta 4.
- [PROPUESTA] Siguen abiertos del registro anterior: por qué quitó "ingeniería y derecho" de los artículos 2 y 9; si los cambios de los vistos 9 y 10 del archivo "a" fueron suyos; si algún "v0.6" salió del repositorio y a quién; y si el resumen ejecutivo, la guía y el guion del 2026-11-15 se rehacen o se archivan. Se apoya en que ninguno consta como respondido.

### Pendientes de confirmar con la Decana

- [PROPUESTA] El nombre de la segunda Dirección de área: ella definió "Dirección de Proyectos" y la v0.7 dice "Dirección de Investigación". Se apoya en la alerta 1.
- [PROPUESTA] Siguen abiertos del registro anterior: la eliminación del transitorio primero y cómo queda la designación de la primera Dirección Nacional; si vuelven los vistos de su propuesta y del acuerdo del Consejo de Facultad; y que conozca el texto completo y no solo el archivo "a". Se apoya en que ninguno consta como respondido.

### Pendientes de confirmar con Secretaría General o con quien revise la técnica

- [PROPUESTA] Siguen abiertos: la compatibilidad de "Direcciones" y "Directores" internos con los artículos 1 y 9 del Reglamento de Unidades Académicas, y el cotejo de los números de decreto y artículos citados en los vistos. Se apoya en que nadie ha abierto esos documentos en este sistema.

### Pendientes de la sesión principal

- [PROPUESTA] Advertir a la titular, con todas sus letras, que la v0.7 incluye un cambio de nombre que puede ser de contenido, como ya anunció que haría. Se apoya en la alerta 1.
- [PROPUESTA] Anotar la v0.7 en `revision-articulo-por-articulo.md` o remitir a este registro, y corregir el mensaje de bloqueo de `generar_decreto.py`, que nombra la v0.6. Se apoya en la alerta 3.
- [PROPUESTA] Siguen abiertos: quién redactó el artículo 13 vigente, cuál fue el argumento para eliminar el transitorio primero y la fecha exacta en que se cerró el archivo "b". Se apoya en las celdas "no consta" de las tablas del registro anterior.

# Registro anterior (2026-11-19), copiado íntegro

Lo que sigue es el texto de `produccion/guia/2026-11-19-2207-registro-decreto.md` tal como se escribió ese día. Donde dice "versión vigente" se refiere a la v0.6; el estado actual de cada alerta está en la tabla "Qué quedó resuelto y qué sigue", más arriba.

# Registro de versiones: decreto de creación del Departamento Nacional de Salud Digital

Este es el primer registro de este documento: no hay un registro anterior en `produccion/guia/`, por eso no lleva `reemplaza:`. Cuenta la historia completa desde la v0.3 hasta la versión vigente. El próximo registro copiará esta historia y agregará lo nuevo.

## Qué revisé y cómo

- [HECHO] Calculé la huella de texto de los seis archivos Word del decreto, del resumen ejecutivo, de la guía y el guion de la reunión con el Vicerrector y de la presentación, y comparé cada par consecutivo de versiones del decreto con `scripts/comparar_versiones.py`. Fuente: salida de scripts/comparar_versiones.py sobre entregables/ (ejecutado 2026-11-19)
- [HECHO] La v0.3 no está en el repositorio; lo que decía lo tomo de las notas de la sesión principal, que la leyó en el Drive de la titular. No pude compararla con el comparador. Fuente: entregables/2026-11-14-decreto/revision-articulo-por-articulo.md (leído 2026-11-19)
- [HECHO] Quién sugirió cada cambio y por qué me lo informó la sesión principal al encargarme este registro, citando la conversación con la titular. Yo no presencié esa conversación: donde la tabla dice "conversación", la fuente es ese relato. Fuente: encargo de la sesión principal al Guía, que cita a la titular del cargo (conversaciones 2026-11-14 y 2026-11-17; recibido 2026-11-19)
- [HECHO] `produccion/gestor-cargo/`, `produccion/brechas-indicadores/` y `produccion/actas/` están vacías; no afecta a este registro, pero lo dejo anotado. Fuente: listado de produccion/ (revisado 2026-11-19)

### Huellas

| Archivo | Rótulo interno | Huella | Párrafos | Palabras |
|---|---|---|---|---|
| `Decreto_Depto_SD_v0.3_borrador.docx` (Drive de la titular, no está en el repositorio) | v0.3 | sin huella | no consta | no consta |
| `entregables/2026-11-14-decreto/decreto-depto-salud-digital-v0.4.docx` | versión 0.4 | `0f8915b2c4ae` | 40 | 1728 |
| `entregables/2026-11-14-decreto/decreto-depto-salud-digital-v0.5.docx` | versión 0.5 | `47cde9559f0c` | 40 | 1758 |
| `entregables/2026-11-14-decreto/versiones-recibidas/2026-11-17-0-v0.6-generada-por-sesion.docx` | versión 0.6 | `9b886f602c28` | 40 | 1780 |
| `entregables/2026-11-14-decreto/versiones-recibidas/2026-11-17-a-v0.6-editada-por-titular.docx` | versión 0.6 | `4ed4b047dad4` | 40 | 1727 |
| `entregables/2026-11-14-decreto/versiones-recibidas/2026-11-17-b-v0.6-iterada-por-titular.docx` | versión 0.6 | `57c2f7ad3f01` | 39 | 1807 |
| `entregables/2026-11-14-decreto/decreto-depto-salud-digital-v0.6.docx` (vigente) | versión 0.6 | `57c2f7ad3f01` | 39 | 1807 |
| `entregables/2026-11-14-decreto/resumen-ejecutivo.docx` | sin número | `f17771776ab6` | 30 | 650 |
| `entregables/2026-11-15-guia-reunion-vicerrector/guia-reunion-vicerrector.docx` | cita la "versión 0.4" | `377cebe3ab7f` | 71 | 1646 |
| `entregables/2026-11-15-guia-reunion-vicerrector/guion-presentacion.docx` | sin número | `37a79aaf08ba` | 101 | 1576 |
| `entregables/2026-11-14-presentacion-vicerrector/presentacion-vicerrector.pptx` | sin número | `398c67ef716e` | 440 | 2120 |

## Alertas

Van de mayor a menor gravedad. Todas están comprobadas con el comparador, salvo donde digo que es hipótesis.

ALERTA (registro 2026-11-19) 1. Tres archivos distintos llevan el rótulo "versión 0.6". [HECHO] El archivo generado por la sesión (`9b886f602c28`), el primero que entregó la titular (`4ed4b047dad4`) y el segundo (`57c2f7ad3f01`) dicen cosas distintas y los tres llevan en la primera línea "Propuesta de decreto · versión 0.6 · documento de trabajo". Fuente: scripts/comparar_versiones.py sobre entregables/2026-11-14-decreto/versiones-recibidas/ (ejecutado 2026-11-19)
- [HECHO] La diferencia entre los tres no es de forma: entre el primero y el tercero cambian los artículos 1, 2, 3 b), 4, 5, 7, 9, 10, 11 y 13, el visto 9 y los transitorios, que pasan de tres a dos. Fuente: scripts/comparar_versiones.py, pares "0"→"a" y "a"→"b" (ejecutado 2026-11-19)
- [HECHO] En el historial de git, `decreto-depto-salud-digital-v0.6.docx` tuvo primero el texto generado (confirmación efa0b0b, 2026-11-17 13:26 UTC, huella `9b886f602c28`) y 75 minutos después fue reemplazado, con el mismo nombre, por el texto iterado (confirmación 1a12c5b, 2026-11-17 14:41 UTC). Fuente: git log y git show efa0b0b sobre entregables/2026-11-14-decreto/ (revisado 2026-11-19)
- [HIPÓTESIS] Si alguien fuera del repositorio (la Decana, la Vicerrectoría, Secretaría General) recibió un archivo "v0.6", no hay forma de saber por el nombre cuál de los tres tiene. Lo confirmaría que la titular diga qué archivo envió y a quién; con la huella de ese archivo lo identifico.
- [PROPUESTA] Que la próxima modificación, por mínima que sea, salga como v0.7, y que desde ahora ningún archivo cambie de contenido sin cambiar de número. Se apoya en que tres textos distintos comparten hoy el mismo rótulo.

ALERTA (registro 2026-11-19) 2. El resumen ejecutivo afirma un resguardo que el decreto vigente ya no contiene. [HECHO] `resumen-ejecutivo.docx` dice, bajo "Lo que el decreto resguarda": "No crea nuevas unidades académicas ni autoridades unipersonales: las Direcciones de área y de Sede son instancias internas de gestión (art. 7)"; esa frase fue eliminada del artículo 7 en el archivo "a" y sigue eliminada en la versión vigente. Fuente: scripts/comparar_versiones.py sobre resumen-ejecutivo.docx y decreto-depto-salud-digital-v0.6.docx (ejecutado 2026-11-19)
- [HECHO] El resumen fue generado junto con la v0.6 de la sesión (confirmación efa0b0b) y no se ha tocado desde entonces; su PDF tiene el mismo texto que el Word. Fuente: git log sobre entregables/2026-11-14-decreto/resumen-ejecutivo.docx y cotejo de texto Word-PDF (revisado 2026-11-19)
- [HECHO] Otros cuatro puntos del resumen no calzan con el decreto vigente: dice "13 artículos y 3 transitorios" y hoy son 2 transitorios; cita "transitorio tercero" para la instalación gradual y hoy es el segundo; dice que el Departamento "propone un marco común de desempeños" y el artículo 3 b) vigente dice que lo "elaborará" y lo "pondrá a disposición" de las carreras; y describe la línea basal solo como la que "sustenta el marco de desempeños", sin "de investigación y proyectos, de carácter permanente". Fuente: lectura del texto de resumen-ejecutivo.docx contra decreto-depto-salud-digital-v0.6.docx (leído 2026-11-19)
- [HIPÓTESIS] De todos los desajustes, este es el más delicado: si el resumen se entrega junto con el decreto vigente, quien los lea verá que el resumen promete lo que la Decana pidió sacar. Lo confirmaría saber si el resumen ya circuló y con qué versión del decreto.
- [PROPUESTA] No entregar el resumen ejecutivo a nadie hasta rehacerlo contra la versión vigente. Se apoya en los cinco desajustes anteriores.

ALERTA (registro 2026-11-19) 3. La guía y el guion de la reunión con el Vicerrector siguen en la v0.4. [HECHO] `guia-reunion-vicerrector.docx` y `guion-presentacion.docx` son del 2026-11-15 y usan "Área de Docencia", "Área de Proyectos", "Coordinaciones de Sede" y "Jefaturas de Área"; el decreto vigente dice Dirección de Docencia, Dirección de Proyectos, Direcciones de Sede y Directores o Directoras. Fuente: lectura del texto de entregables/2026-11-15-guia-reunion-vicerrector/ con scripts/comparar_versiones.py (leído 2026-11-19)
- [HECHO] El guion hace decir a la titular: "las Áreas y las Coordinaciones son instancias internas de gestión. El decreto no crea unidades académicas ni autoridades nuevas"; el decreto vigente ya no lo dice. Fuente: entregables/2026-11-15-guia-reunion-vicerrector/guion-presentacion.docx, párrafo 67 (leído 2026-11-19)
- [HECHO] La guía y el guion preparan una pregunta al Vicerrector sobre la frase "considerarán preferentemente al Departamento" del artículo 4; esa frase ya no existe: el artículo 4 vigente dice que el Departamento "estará disponible para ser consultado" y "podrá emitir opinión técnica". Fuente: guia-reunion-vicerrector.docx, párrafos 19 y 60, y guion-presentacion.docx, párrafo 72, contra decreto-depto-salud-digital-v0.6.docx (leído 2026-11-19)
- [HECHO] La guía lista como decisión para la Decana el "Transitorio primero. Desde cuándo se cuenta el período de la Dirección" y cita lo que "la versión 0.4 dice"; ese transitorio fue eliminado. La guía y el guion hablan además de "transitorio tercero" y de "tres artículos transitorios"; hoy son dos. Fuente: guia-reunion-vicerrector.docx, párrafos 18 y 49, y guion-presentacion.docx, párrafo 71 (leído 2026-11-19)
- [HIPÓTESIS] No sé si la reunión con el Vicerrector Académico ya ocurrió ni en qué fecha; si ya ocurrió, estos dos documentos son historia y basta con no reutilizarlos; si está pendiente, hay que rehacerlos. Lo confirmaría la titular.

ALERTA (registro 2026-11-19) 4. La presentación que está en el repositorio no es la última. [HECHO] `presentacion-vicerrector.pptx` (2026-11-15) usa Áreas, Jefaturas y Coordinaciones de Sede, dice "Más tres artículos transitorios" y menciona "ingeniería, derecho y otras". Fuente: lectura del texto de entregables/2026-11-14-presentacion-vicerrector/presentacion-vicerrector.pptx con scripts/comparar_versiones.py (leído 2026-11-19)
- [HECHO] Existe una presentación posterior de la titular, del 2026-11-16, con los nombres "Dirección de Docencia", "Dirección de Proyectos" y "Dirección de Sede"; no está en `entregables/`. Fuente: entregables/2026-11-14-decreto/revision-articulo-por-articulo.md, sección "De v0.5 a v0.6" (leído 2026-11-19)
- [HIPÓTESIS] La presentación del 2026-11-16 puede tener sus propios desajustes con el decreto vigente (número de transitorios, el resguardo del artículo 7, ingeniería y derecho, "consulta preferente"), porque es anterior a los archivos "a" y "b". No puedo comprobarlo sin el archivo; lo confirmaría que la titular lo deje en `entregables/` para sacarle la huella.

ALERTA (registro 2026-11-19) 5. Ejecutar el generador borraría la versión vigente. [HECHO] `generar_decreto.py` escribe sobre `decreto-depto-salud-digital-v0.6.docx` y sobre `resumen-ejecutivo.docx`; lo ejecuté en una carpeta temporal y produce el texto de huella `9b886f602c28`, es decir, la v0.6 generada por la sesión y no la vigente. Fuente: entregables/2026-11-14-decreto/generar_decreto.py, ejecutado fuera del repositorio (2026-11-19)
- [HECHO] Las notas de la sesión ya dicen que "el generador quedó desactualizado", pero el archivo sigue ahí, con el mismo nombre de salida, y su primera línea todavía dice "Genera el decreto v0.5". Fuente: entregables/2026-11-14-decreto/revision-articulo-por-articulo.md y generar_decreto.py (leído 2026-11-19)
- [PROPUESTA] Que la sesión principal no vuelva a ejecutar ese generador sobre la carpeta del decreto mientras no se actualice o se retire, y que la versión vigente se edite solo desde el Word de la titular. Se apoya en que un solo comando devolvería el decreto a un texto que la Decana y la titular ya descartaron.

ALERTA (registro 2026-11-19) 6. Cambios aplicados que desaparecieron y textos quitados que volvieron. Todos tienen explicación en lo que me informaron, salvo donde digo "no consta"; los enumero porque mi definición me pide avisar siempre que ocurre.
- [HECHO] Desapareció el resguardo del artículo 7 ("no constituyen unidades académicas ni autoridades unipersonales en los términos de los artículos 1 y 9 del Reglamento de Unidades Académicas"), que estuvo en la v0.4, la v0.5 y la v0.6 generada. Fuente: scripts/comparar_versiones.py, par "0"→"a" (ejecutado 2026-11-19)
- [HECHO] Desapareció "en especial la ingeniería y el derecho" del artículo 2 y "en especial de las disciplinas de ingeniería y derecho" del artículo 9; el motivo no consta. Fuente: scripts/comparar_versiones.py, par "0"→"a" (ejecutado 2026-11-19)
- [HECHO] Desapareció del artículo 4 la obligación de que las unidades "considerarán preferentemente al Departamento", que venía sin cambios desde la v0.3. Fuente: scripts/comparar_versiones.py, par "a"→"b", y revision-articulo-por-articulo.md (ejecutado 2026-11-19)
- [HECHO] Desapareció el transitorio primero completo; con él salió del decreto toda mención al artículo 14 del Reglamento de Unidades Académicas y a desde cuándo se cuenta el período de la Dirección Nacional. Fuente: scripts/comparar_versiones.py, par "a"→"b" (ejecutado 2026-11-19)
- [HECHO] Volvió "me confieren" en el visto 10: el archivo "a" decía "Las facultades que confieren" y el "b" restituye "que me confieren", como en la v0.4. Fuente: scripts/comparar_versiones.py, pares "0"→"a" y "a"→"b" (ejecutado 2026-11-19)
- [HECHO] Volvió en el artículo 1 la enumeración separada "la equidad y los determinantes digitales de la salud; las competencias digitales de los equipos de salud", que el archivo "a" había fundido en "la gobernanza que engloba la equidad y los determinantes digitales de la salud y las competencias digitales de los equipos de salud". Fuente: scripts/comparar_versiones.py, pares "0"→"a" y "a"→"b" (ejecutado 2026-11-19)
- [HECHO] Volvió "Director o Directora" en los artículos 10, 11 y 12, donde el archivo "a" había puesto "un(a) Director(a)", "una Director(a)" y "Lo(a)s Directore(a)s". Fuente: scripts/comparar_versiones.py, pares "0"→"a" y "a"→"b" (ejecutado 2026-11-19)
- [HECHO] Lo que se quitó en la v0.4 sigue quitado en la versión vigente: los vistos 1 al 8 son idénticos a los de la v0.4 y no reaparecen la propuesta de la Decana, el acuerdo del Consejo de Facultad, los pronunciamientos del Consejo Superior y la Junta Directiva ni el número de decreto del Modelo Educativo. Fuente: scripts/comparar_versiones.py, cadena de pares de v0.4 a v0.6 vigente (ejecutado 2026-11-19)
- [HECHO] Lo que se agregó en la v0.5 ("calidad y trazabilidad" en el artículo 10) y en la v0.6 generada (los nombres de las Direcciones) sigue en la versión vigente. Fuente: scripts/comparar_versiones.py, cadena de pares de v0.5 a v0.6 vigente (ejecutado 2026-11-19)

ALERTA (registro 2026-11-19) 7. Hay una errata en la versión vigente. [HECHO] El artículo 1 vigente tiene dos puntos seguidos: "con el avance científico y tecnológico del campo.. Para ello"; aparece en el paso de "a" a "b" y está también en el PDF. Fuente: scripts/comparar_versiones.py, par "a"→"b", y pdftotext sobre decreto-depto-salud-digital-v0.6.pdf (ejecutado 2026-11-19)

ALERTA (registro 2026-11-19) 8. Las notas de la sesión principal no registran todo lo que cambió. [HECHO] `revision-articulo-por-articulo.md` no menciona seis cambios que el comparador sí muestra: "en materias de salud digital" en el visto 9; la frase nueva del artículo 7 "en adelante 'las Direcciones de área'"; "Las Direcciones de área resguardarán" en el artículo 10; la redacción nueva del artículo 13; la condición "en la medida en que lo requieran las necesidades del Departamento y lo permita la disponibilidad de la Facultad" del transitorio; y que el Comité Consultivo ahora consolida "la información y los indicadores". Fuente: entregables/2026-11-14-decreto/revision-articulo-por-articulo.md contra la salida de scripts/comparar_versiones.py (leído 2026-11-19)
- [HECHO] Las notas presentan la versión vigente como "la versión editada por la titular" y no distinguen los dos archivos que ella entregó ni qué redacciones fueron de la sesión principal. Fuente: entregables/2026-11-14-decreto/revision-articulo-por-articulo.md, sección "v0.6 iterada por la titular" (leído 2026-11-19)
- [HECHO] Las notas fechan la versión vigente el 2026-11-17 y git la confirma ese día a las 14:41 UTC; el encargo que recibí fecha el paso de "a" a "b" como "2026-11-17/19". Fuente: git log sobre decreto-depto-salud-digital-v0.6.docx y encargo de la sesión principal (revisado 2026-11-19)
- [HIPÓTESIS] El texto vigente quedó cerrado el 2026-11-17 y lo del 19 es solo el archivado de las copias en `versiones-recibidas/`. Lo confirmaría la sesión principal.

## Historia de cambios

En las tablas, "consta en" indica de dónde sale la atribución. "Encargo" es el relato de la sesión principal al encargarme este registro (2026-11-19), que cita la conversación con la titular en la fecha indicada. "Notas" es `entregables/2026-11-14-decreto/revision-articulo-por-articulo.md`. "Comparador" es `scripts/comparar_versiones.py`.

### v0.3 → v0.4 (2026-11-14 y 15). Aplicó: sesión principal

- [HECHO] No pude comparar este paso con el comparador porque la v0.3 no está en el repositorio; el contenido de la v0.3 sale de las notas, y el de la v0.4, del archivo. Fuente: entregables/2026-11-14-decreto/revision-articulo-por-articulo.md y decreto-depto-salud-digital-v0.4.docx (leído 2026-11-19)
- [HECHO] La v0.3 era `Decreto_Depto_SD_v0.3_borrador.docx`, del 2026-11-11, base de lo presentado al Consejo de Facultad el 2026-11-12. Fuente: encargo de la sesión principal al Guía (recibido 2026-11-19)

| Lugar | Qué decía (v0.3) | Qué dice (v0.4) | Quién lo sugirió | Por qué | Consta en |
|---|---|---|---|---|---|
| Rótulo | "BORRADOR PARA REVISIÓN · v0.3 · 11 de noviembre de 2026" | "Propuesta de decreto · versión 0.4 · documento de trabajo" | Titular (criterio general) | "No hablar de tiempos, es atarse de manos" | Encargo, conversación 2026-11-14; notas |
| Número y fecha | "N.º [●]/2026", "Santiago, [●] de [●] de 2026" | "N.º [●]", "Santiago, [●]" | Titular | Mismo criterio: sin año | Encargo, conversación 2026-11-14; notas |
| Visto del Modelo Educativo | "aprobado por Decreto de Rectoría N.º [●]" | Se cita sin número de decreto | Titular | "Solo archivos verificables" | Encargo, conversación 2026-11-14; notas |
| Visto de la propuesta de la Decana | "La propuesta de la Decana […] y lo acordado por el Consejo de Facultad" | Eliminado | Titular | "Solo archivos verificables": no había documento de respaldo | Encargo, conversación 2026-11-14; notas |
| Visto del Consejo Superior y la Junta Directiva | "El pronunciamiento favorable […] adoptado en sesión de [●]" | Eliminado | Titular | "Solo archivos verificables": aún no había ocurrido | Encargo, conversación 2026-11-14; notas |
| Numeración de los vistos | Sin numerar | Numerados del 1.º al 10.º | No consta (las notas lo describen; el encargo no lo atribuye) | Poder citarlos en la conversación | Notas |
| Artículo 5 | Líneas de investigación sin línea basal; decía "anualmente" | Agrega "entre ellas una línea basal que sustente el marco de desempeños señalado en el artículo 3.º"; quita "anualmente" | Línea basal: sesión principal; la titular lo mantuvo. "Anualmente": titular | Línea basal: que el decreto sostuviera la presentación. "Anualmente": sin tiempos | Encargo; notas |
| Artículo 7 | "Área de Investigación, Vinculación con el Medio y Proyectos, en adelante 'Área IVP'" | "Área de Proyectos" | Titular | Nombre vigente | Encargo, conversación 2026-11-14; notas |
| Artículo 10 | Áreas sin subáreas | Docencia "comprende el pregrado, el postgrado y la educación continua"; Proyectos "comprende la línea basal, la investigación y la vinculación con el medio" | Titular | Las Áreas tienen subáreas | Encargo, conversación 2026-11-14; notas |
| Transitorio primero | "se computará a contar de [●]" | "a contar de la fecha del presente decreto" | Sesión principal | Sin fecha abierta; quedó marcado como decisión para la Decana | Encargo; notas |
| Transitorio tercero | "dentro de los [●] días siguientes a la fecha del presente decreto" | Eliminado ese plazo | Titular | Sin plazos | Encargo, conversación 2026-11-14; notas |

### v0.4 → v0.5 (2026-11-17). Aplicó: sesión principal

- [HECHO] El comparador muestra exactamente dos diferencias: el rótulo y una frase agregada al artículo 10; coincide con las notas. Fuente: scripts/comparar_versiones.py v0.4 contra v0.5 (ejecutado 2026-11-19)

| Lugar | Qué decía (v0.4) | Qué dice (v0.5) | Quién lo sugirió | Por qué | Consta en |
|---|---|---|---|---|---|
| Rótulo | "versión 0.4" | "versión 0.5" | Sesión principal | Cambio de versión | Comparador |
| Artículo 10 | Sin mención a calidad | Agrega: "Ambas Áreas resguardarán la calidad y la trazabilidad de los procesos a su cargo, conforme a los mecanismos de aseguramiento de la calidad de la Facultad y de la Universidad." | Titular lo pidió. La sesión principal decidió aplicarlo a las dos Áreas y no nombrar a la Dirección de Aseguramiento de la Calidad | La titular revisó el documento "Funciones del director(a) del Departamento de Salud Digital", que dedica un bloque a calidad, y el decreto no la mencionaba | Encargo, conversación 2026-11-17; notas; comparador |

### v0.5 → v0.6 generada por la sesión (2026-11-17). Aplicó: sesión principal

- [HECHO] El comparador muestra cambios en el rótulo, los artículos 7 al 12 y los transitorios segundo y tercero, todos de nombres; no hay cambios de fondo y coincide con las notas. Fuente: scripts/comparar_versiones.py v0.5 contra 2026-11-17-0-v0.6-generada-por-sesion.docx (ejecutado 2026-11-19)
- [HECHO] Los nombres son los definidos por la Decana, según la titular y su presentación del 2026-11-16. Fuente: encargo de la sesión principal al Guía, que cita a la titular del cargo (conversación 2026-11-17; recibido 2026-11-19)

| Lugar | Qué decía (v0.5) | Qué dice (v0.6 generada) | Quién lo sugirió | Por qué | Consta en |
|---|---|---|---|---|---|
| Artículo 7 | "el Área de Docencia, el Área de Proyectos, las Coordinaciones de Sede"; "Las Áreas y las Coordinaciones de Sede son instancias internas" | "la Dirección de Docencia, la Dirección de Proyectos, las Direcciones de Sede"; "Las Direcciones de área y las Direcciones de Sede son instancias internas" | Decana (nombres), transmitido por la titular | Nombres finales definidos por la Decana | Encargo, conversación 2026-11-17; notas; comparador |
| Artículo 8 | Subroga "la Jefatura de Área que designe" | Subroga "el Director o Directora de área que designe" | Decana, vía titular | Ídem | Ídem |
| Artículo 9 | "las Jefaturas de Área y los Coordinadores de Sede" | "los Directores o Directoras de área y los Directores o Directoras de Sede" | Decana, vía titular | Ídem | Ídem |
| Artículo 10 | "El Área de…", "Ambas Áreas", "Cada Área estará a cargo de una Jefatura" | "La Dirección de…", "Ambas Direcciones", "Cada Dirección de área estará a cargo de un Director o Directora" | Decana, vía titular. El genérico "Direcciones de área" lo eligió la sesión principal entre tres formas de la presentación | Ídem | Ídem |
| Artículo 11 | "Coordinación de Sede… a cargo de un Coordinador o Coordinadora… lineamientos técnicos de las Áreas" | "Dirección de Sede… a cargo de un Director o Directora… lineamientos técnicos de las Direcciones de área" | Decana, vía titular | Ídem | Ídem |
| Artículo 12 | "Las Jefaturas de Área y los Coordinadores de Sede" | "Los Directores o Directoras de área y los Directores o Directoras de Sede" | Decana, vía titular | Ídem | Ídem |
| Transitorios segundo y tercero | "Jefaturas de Área"; "Las Áreas y las Coordinaciones de Sede" | "Directores o Directoras de área"; "Las Direcciones de área y las Direcciones de Sede" | Decana, vía titular | Ídem | Ídem |

### v0.6 generada → v0.6 editada por la titular, archivo "a" (2026-11-17). Aplicó: la titular

- [HECHO] El comparador muestra cambios en los vistos 9 y 10, los artículos 1, 2, 7, 9, 10, 11, 12 y 13 y el transitorio primero; el texto baja de 1780 a 1727 palabras. Fuente: scripts/comparar_versiones.py "0" contra "a" (ejecutado 2026-11-19)

| Lugar | Qué decía (v0.6 generada) | Qué dice (archivo "a") | Quién lo sugirió | Por qué | Consta en |
|---|---|---|---|---|---|
| Visto 9 | "el quehacer de la Universidad en salud digital" | "el quehacer de la Universidad en materias de salud digital" | No consta (el archivo es de la titular; el encargo no lo menciona) | No consta | Comparador |
| Visto 10 | "Las facultades que me confieren" | "Las facultades que confieren" | No consta (ídem) | No consta | Comparador |
| Artículo 1 | "…la ética, la regulación y la protección de datos en salud; la equidad y los determinantes digitales de la salud; las competencias digitales de los equipos de salud, y las demás áreas…" | "…la ética, la regulación y la protección de datos en salud; la gobernanza que engloba la equidad y los determinantes digitales de la salud y las competencias digitales de los equipos de salud, y las demás áreas…" | Titular | Incluir la gobernanza | Encargo, conversación 2026-11-17; comparador |
| Artículo 2 | Termina en "…concurren a la salud digital, en especial la ingeniería y el derecho." | Termina en "…concurren a la salud digital." | Titular | No consta | Encargo; comparador |
| Artículo 7 | Incluía: "Las Direcciones de área y las Direcciones de Sede son instancias internas de gestión del Departamento y no constituyen unidades académicas ni autoridades unipersonales en los términos de los artículos 1 y 9 del Reglamento de Unidades Académicas." | Frase eliminada | Decana; lo aplicó la titular | "Quiere ir a lo grande; cambiar el decreto a posteriori es muy difícil" | Encargo, conversación 2026-11-17; notas; comparador |
| Artículo 9 | "…con las que se articula el Departamento, en especial de las disciplinas de ingeniería y derecho." | "…con las que se articula el Departamento." | Titular | No consta | Encargo; comparador |
| Artículo 10 | "a cargo de un Director o Directora" | "a cargo de un(a) Director(a)" | Titular | Fórmula de género | Encargo; comparador |
| Artículo 11 | "a cargo de un Director o Directora" | "a cargo de una Director(a)" | Titular | Fórmula de género | Encargo; comparador |
| Artículo 12 | "Los Directores o Directoras de área y los Directores o Directoras de Sede" | "Lo(a)s Directore(a)s de área y lo(a)s Directore(a)s de Sede" | Titular | Fórmula de género | Encargo; comparador |
| Artículo 13 | "los académicos adscritos a él y los académicos de otras unidades" | "lo(a)s académico(a)s adscritos a él y lo(a)s académico(a)s de otras unidades" | Titular | Fórmula de género | Encargo; comparador |
| Transitorio primero | "La Directora del Departamento en funciones a la fecha del presente decreto continuará en el cargo, y el período…" | "El Decano o Decana propondrá la designación del primer Director o Directora Nacional, conforme al Reglamento de Unidades Académicas, y el período…" | Titular | No le gustaba "continuará en el cargo": "te pasaste unos pueblos" | Encargo, conversación 2026-11-17; comparador |

- [HIPÓTESIS] Los cambios de los vistos 9 y 10 los hizo la titular al editar el archivo, igual que el resto; nadie me lo confirmó. Lo confirmaría ella.

### v0.6 "a" → v0.6 "b", versión vigente (2026-11-17, según git). Decidió: la titular. Redactó: sesión principal

- [HECHO] La sesión principal leyó el texto "como Vicerrector Académico" y señaló puntos; la titular decidió cada uno y la sesión redactó. Fuente: encargo de la sesión principal al Guía (recibido 2026-11-19)
- [HECHO] El comparador muestra cambios en el visto 10, los artículos 1, 3 b), 4, 5, 7, 9, 10, 11, 12 y 13 y los transitorios; el texto sube de 1727 a 1807 palabras y baja de 40 a 39 párrafos por el transitorio eliminado. Fuente: scripts/comparar_versiones.py "a" contra "b" (ejecutado 2026-11-19)
- [HECHO] El archivo "b" y `decreto-depto-salud-digital-v0.6.docx` tienen el mismo texto (huella `57c2f7ad3f01`), y el PDF `decreto-depto-salud-digital-v0.6.pdf` tiene el mismo texto que el Word. Fuente: scripts/comparar_versiones.py y cotejo de texto Word-PDF (ejecutado 2026-11-19)

| Lugar | Qué decía (archivo "a") | Qué dice (archivo "b", vigente) | Quién lo sugirió | Por qué | Consta en |
|---|---|---|---|---|---|
| Visto 10 | "Las facultades que confieren" | "Las facultades que me confieren" | Sesión principal | Recupera la fórmula original | Encargo; comparador |
| Artículo 1 | "la gobernanza que engloba la equidad y los determinantes digitales de la salud y las competencias digitales de los equipos de salud" | "la gobernanza de la salud digital; la ética, la regulación y la protección de datos en salud; la equidad y los determinantes digitales de la salud; las competencias digitales de los equipos de salud" (la gobernanza va antes de la ética) | Titular decidió; sesión redactó | "Déjalo como antes, pero incluye la gobernanza" | Encargo, conversación 2026-11-17; comparador |
| Artículo 1 | "…del campo. Para ello" | "…del campo.. Para ello" (errata) | No consta | Errata | Comparador |
| Artículo 3 b) | "Propondrá un marco común de desempeños en salud digital para los perfiles de egreso de las carreras del área de la salud, […] para su incorporación por las carreras conforme a sus procesos…" | "Elaborará un marco común de desempeños en salud digital, […] y lo pondrá a disposición de las carreras del área de la salud para que sea considerado en sus perfiles de egreso, conforme a sus procesos…" | Observación de la sesión principal; decisión de la titular | El marco "se pone a disposición" de las carreras | Encargo; comparador |
| Artículo 4 | "Las unidades académicas de la Universidad que incorporen contenidos de salud digital en sus programas considerarán preferentemente al Departamento para su diseño y ejecución." | "El Departamento, en su calidad de unidad especializada, estará disponible para ser consultado por las unidades académicas de la Universidad que incorporen contenidos de salud digital en sus programas, y podrá emitir opinión técnica sobre su diseño y ejecución." | Titular pidió; sesión redactó | Quería una frase más leve que "considerarán preferentemente" | Encargo; comparador |
| Artículo 5 | "entre ellas una línea basal que sustente el marco de desempeños señalado en el artículo 3.º" | "entre ellas una línea basal de investigación y proyectos, de carácter permanente, que sustente el marco de desempeños señalado en el artículo 3.º y oriente el quehacer del Departamento" | Titular | "El motor interno del Departamento" | Encargo; comparador |
| Artículo 7 | "…la Dirección de Docencia, la Dirección de Proyectos, las Direcciones de Sede y sus académicos" | "…la Dirección de Docencia y la Dirección de Proyectos, en adelante 'las Direcciones de área', las Direcciones de Sede y sus académicos". Sigue sin el resguardo | Resguardo fuera: Decana. Definición de "las Direcciones de área": sesión principal | Al salir la frase del resguardo, el término "Direcciones de área" quedaba sin definir | Encargo; comparador |
| Artículo 9 | "un Comité Consultivo, que asesorará a la Dirección Nacional en la planificación y el seguimiento de su quehacer." | "un Comité Consultivo, instancia de articulación interna que asesorará a la Dirección Nacional en la planificación y el seguimiento de su quehacer, y en la que se consolidarán la información y los indicadores levantados por las Direcciones de área y las Direcciones de Sede." | Titular | Comité como instancia de articulación interna que consolida información e indicadores | Encargo; comparador |
| Artículo 10 | "Ambas Direcciones resguardarán…"; "un(a) Director(a)" | "Las Direcciones de área resguardarán…"; "un Director o Directora" | Sesión principal | Usar el término definido en el artículo 7; género unificado | Encargo; comparador |
| Artículo 11 | "a cargo de una Director(a)"; "Le corresponderá representar al Departamento en la sede y realizar el seguimiento, el monitoreo y el levantamiento de indicadores locales de su quehacer, velando por la equivalencia…" | "a cargo de un Director o Directora"; "Le corresponderá representar al Departamento en la sede; mantener la relación con las carreras en que se imparta formación en salud digital; y realizar el seguimiento, el monitoreo y el levantamiento de información e indicadores locales, de modo que el Departamento conozca la realidad y la identidad de cada sede, velando por la equivalencia…" | Titular (fondo); sesión principal (género) | "Representantes locales… información de identidad local, granularidad" | Encargo; comparador |
| Artículo 12 | "Lo(a)s Directore(a)s de área y lo(a)s Directore(a)s de Sede" | "Los Directores o Directoras de área y los Directores o Directoras de Sede" | Sesión principal | Género unificado en "Director o Directora" | Encargo; comparador |
| Artículo 13 | "lo(a)s académico(a)s adscritos a él y lo(a)s académico(a)s de otras unidades" | "los académicos y las académicas adscritos a él y los de otras unidades" | No consta con precisión (el encargo solo habla de unificar "Director o Directora") | Género | Comparador |
| Transitorio primero | "El Decano o Decana propondrá la designación del primer Director o Directora Nacional, […] y el período establecido en el artículo 14 del Reglamento de Unidades Académicas se computará a contar de la fecha del presente decreto." | Eliminado | Recomendación de la sesión principal; la titular lo aplicó | No consta el argumento de la recomendación | Encargo; comparador |
| Transitorio segundo → primero | "Artículo segundo. Mientras no se designen los Directores o Directoras de área…" | "Artículo primero. Mientras no se designen…" (mismo texto, renumerado) | Consecuencia del anterior | Renumeración | Comparador |
| Transitorio tercero → segundo | "…se instalarán gradualmente, conforme al plan de implementación…" | "…se instalarán gradualmente, en la medida en que lo requieran las necesidades del Departamento y lo permita la disponibilidad de la Facultad, conforme al plan de implementación…" | Titular | "Irán incorporándose en medida de lo necesario y costos" | Encargo; comparador |

- [HIPÓTESIS] La redacción del artículo 13 ("los académicos y las académicas") la hizo la sesión principal al unificar el género. Lo confirmaría la sesión principal.

## Lo que me llama la atención del texto vigente

Son observaciones mías al leer la versión vigente completa; no son cambios ni alertas, y decide la titular.

- [HIPÓTESIS] En el artículo 7 vigente, "integrada por la Dirección Nacional, la Dirección de Docencia y la Dirección de Proyectos, en adelante 'las Direcciones de área'" admite leerse como si la Dirección Nacional también fuera una Dirección de área, porque las tres van en la misma enumeración antes de la definición. Lo confirmaría la lectura de Secretaría General o de quien revise la técnica del decreto.
- [HIPÓTESIS] Al eliminar el transitorio primero, el decreto ya no dice quién es el primer Director o Directora Nacional ni desde cuándo se cuenta su período; puede ser lo buscado (queda regido por el Reglamento de Unidades Académicas) o un vacío. En la guía del 2026-11-15 este punto estaba anotado como decisión para la Decana; no consta que ella lo haya resuelto. Lo confirmaría la Decana.
- [HIPÓTESIS] Sin el resguardo del artículo 7, llamar "Direcciones" y "Directores" a las instancias internas puede rozar los artículos 1 y 9 del Reglamento de Unidades Académicas sobre unidades académicas y autoridades unipersonales. Las notas de la sesión ya lo habían levantado cuando el resguardo aún estaba; ahora que no está, la duda pesa más. Nadie abrió el Reglamento en este sistema; lo confirmaría leerlo o consultarlo a Secretaría General.
- [HECHO] El género quedó unificado en los cargos ("Director o Directora") y en el artículo 13 ("los académicos y las académicas"), pero los artículos 2, 5 y 7 siguen diciendo solo "académicos". Fuente: lectura de entregables/2026-11-14-decreto/decreto-depto-salud-digital-v0.6.docx (leído 2026-11-19)
- [HECHO] Siguen sin verificar los números de los decretos citados en los vistos, los artículos del Reglamento de Unidades Académicas, la cita del Modelo Educativo y si la síntesis de autoevaluación del visto 8 es la versión final; las notas los dejaron como hipótesis el 2026-11-14 y nada posterior los cierra. Fuente: entregables/2026-11-14-decreto/revision-articulo-por-articulo.md (leído 2026-11-19)
- [HECHO] La numeración de los 13 artículos no cambió en ninguna versión; lo que cambió es el número de transitorios, de 3 a 2. Cualquier lámina o texto que diga "tres transitorios" o "transitorio tercero" quedó mal. Fuente: scripts/comparar_versiones.py, cadena de pares de v0.4 a v0.6 vigente (ejecutado 2026-11-19)

## Estado

- [HECHO] Versión vigente: `entregables/2026-11-14-decreto/decreto-depto-salud-digital-v0.6.docx`, rótulo "versión 0.6", huella `57c2f7ad3f01`, 39 párrafos, 1807 palabras, 13 artículos y 2 transitorios; idéntica a `versiones-recibidas/2026-11-17-b-v0.6-iterada-por-titular.docx` y a su PDF. Fuente: scripts/comparar_versiones.py (ejecutado 2026-11-19)
- [HECHO] Esta es la última versión registrada. Si la titular entrega un archivo del decreto con otra huella, corresponde alerta. Fuente: este registro, produccion/guia/2026-11-19-2207-registro-decreto.md (escrito 2026-11-19)

### Pendientes de confirmar con la Decana

- [PROPUESTA] Confirmar que la eliminación del transitorio primero es lo que ella quiere, y cómo queda la designación de la primera Dirección Nacional y el cómputo del período. Se apoya en que la guía del 2026-11-15 lo dejó como decisión suya y no consta su respuesta.
- [PROPUESTA] Confirmar si los vistos eliminados en la v0.4 (su propuesta y el acuerdo del Consejo de Facultad) vuelven y con qué documento. Se apoya en que la guía del 2026-11-15 dice "ella decide si vuelven" y no consta su respuesta.
- [PROPUESTA] Confirmar que conoce el texto vigente completo y no solo el archivo "a". Se apoya en que su indicación sobre el artículo 7 es anterior a los cambios de los artículos 3, 4, 5, 9 y 11 y no consta que haya visto el archivo "b".

### Pendientes de confirmar con Secretaría General o con quien revise la técnica

- [PROPUESTA] Consultar si las "Direcciones" y los "Directores" internos, ya sin el resguardo, son compatibles con los artículos 1 y 9 del Reglamento de Unidades Académicas. Se apoya en la hipótesis de las notas de la sesión y en que la frase fue eliminada.
- [PROPUESTA] Cotejar los números de decreto y los artículos citados en los vistos. Se apoya en que siguen como hipótesis desde el 2026-11-14.

### Pendientes de la titular

- [PROPUESTA] Decir por qué quitó "en especial la ingeniería y el derecho" de los artículos 2 y 9, para dejarlo registrado; la presentación del repositorio todavía menciona "ingeniería, derecho y otras". Se apoya en que es el único cambio de fondo sin motivo.
- [PROPUESTA] Confirmar si los cambios de los vistos 9 ("en materias de") y 10 del archivo "a" fueron suyos e intencionales. Se apoya en que el del visto 10 fue revertido y el del visto 9 sigue vigente sin que nadie lo haya comentado.
- [PROPUESTA] Decir si algún archivo "v0.6" salió del repositorio, a quién y cuál. Se apoya en la alerta 1.
- [PROPUESTA] Decir si la reunión con el Vicerrector Académico ya ocurrió y, si ocurrió, qué observó sobre el texto, para registrarlo como origen de cambios futuros. Se apoya en que la columna "quién lo sugirió" no tiene todavía ninguna entrada del Vicerrector.
- [PROPUESTA] Dejar en `entregables/` la presentación del 2026-11-16, para registrarla y compararla con el decreto. Se apoya en la alerta 4.
- [PROPUESTA] Decidir si el resumen ejecutivo, la guía y el guion se rehacen contra la versión vigente o se archivan como históricos. Se apoya en las alertas 2 y 3.

### Pendientes de la sesión principal

- [PROPUESTA] Corregir la errata "campo.." del artículo 1 en la próxima versión, que debería ser v0.7. Se apoya en las alertas 1 y 7.
- [PROPUESTA] Actualizar o retirar `generar_decreto.py`. Se apoya en la alerta 5.
- [PROPUESTA] Completar `revision-articulo-por-articulo.md` con los seis cambios que no registra, o remitir a este registro. Se apoya en la alerta 8.
- [PROPUESTA] Confirmarme quién redactó el artículo 13 vigente, cuál fue el argumento para eliminar el transitorio primero y la fecha exacta en que se cerró el archivo "b". Se apoya en las celdas "no consta" de la última tabla.
