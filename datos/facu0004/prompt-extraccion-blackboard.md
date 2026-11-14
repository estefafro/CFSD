# Prompt maestro: extracción de FACU0004 desde Blackboard

Para pegar en una sesión de Claude que corra en el computador de la titular (Claude in Chrome o la app de escritorio), con Blackboard de la USS abierto e iniciado. Cada semestre se cambian el periodo y la lista de NRC.

```
ROL Y OBJETIVO
Eres mi asistente para extraer datos de Blackboard. Soy la coordinadora del curso
FACU0004 Salud Digital de la Universidad San Sebastián y tengo Blackboard abierto
e iniciado en este navegador. Necesito los datos del periodo 202620 para armar una
presentación de resultados por sede y por sección. El análisis y la presentación
se harán en otra sesión: aquí solo necesito la extracción, completa y verificada.

REGLAS (no negociables)
1. Solo lectura. No modifiques, califiques, publiques, envíes ni borres nada en
   Blackboard. Si una acción pudiera cambiar algo, no la hagas y avísame.
2. Privacidad. Ningún archivo de salida puede contener nombres, RUT, correos,
   nombres de usuario ni identificadores internos de Blackboard de estudiantes.
   Reemplaza a cada estudiante por un código correlativo (E0001, E0002, …), el
   mismo en todos los archivos. No guardes ni me muestres la tabla de equivalencia.
3. No inventes ni completes datos. Si algo no se puede leer, déjalo vacío y
   anótalo en el informe final.
4. Trabaja solo con las secciones de la lista. No abras otros cursos.

SECCIONES (31)
El identificador de cada curso es USS_UG_202620_FACU0004_<NRC>_--_R.
Entre paréntesis, los inscritos al 25-09-2026, para que verifiques tus conteos.

Santiago (campus LPS): 9549 (56), 9550 (53), 9551 (50), 9552 (51), 9553 (49),
  9554 (54), 9555 (46), 9556 (58), 9557 (48), 9558 (75), 9559 (75)
Concepción (campus TPC): 17646 (67), 17647 (64), 17648 (60), 17649 (63),
  17650 (59), 17651 (64), 17652 (56), 17653 (65), 17655 (66), 17656 (68)
Valdivia (campus VAL): 18932 (62), 18933 (54), 18934 (54), 18935 (51), 18936 (49)
De la Patagonia (campus PAP): 13106 (77), 13107 (59), 13108 (48), 13109 (38),
  13110 (49)
Total esperado: 31 secciones y cerca de 1.788 estudiantes.

MÉTODO
Usa la API REST pública de Blackboard Learn con mi sesión ya iniciada, igual que
en el informe de docentes del 25-09-2026. Como referencia, suelen servir:
- /learn/api/public/v3/courses/courseId:<identificador>
- /learn/api/public/v2/courses/<id>/gradebook/columns
- /learn/api/public/v2/courses/<id>/gradebook/columns/<idColumna>/users
- /learn/api/public/v1/courses/<id>/users  (membresías, rol y último acceso)
Recorre todas las páginas de cada respuesta (paginación). Si la API no responde,
dime qué error da antes de probar otra vía; no pases a hacer clics masivos en la
interfaz sin avisarme.

Empieza con UNA sola sección (9549), muéstrame qué columnas tiene el libro de
calificaciones y cuántos estudiantes obtuviste, y espera mi visto bueno antes de
seguir con las otras 30.

QUÉ EXTRAER, POR SECCIÓN
A. Columnas del libro de calificaciones: nombre, puntaje máximo, fecha de
   vencimiento, tipo (prueba, tarea, calculada, manual), si se incluye en el
   cálculo de la nota final, y cuál es la columna de nota final o total.
B. Notas: para cada estudiante con rol de estudiante y cada columna, el puntaje o
   la nota tal como aparece, la escala (puntos, porcentaje o nota de 1,0 a 7,0) y
   el estado (sin entregar, entregado, calificado, exento).
C. Estudiantes: si la inscripción está activa o deshabilitada, y la fecha de
   último acceso al curso.
D. Si está disponible sin esfuerzo adicional: fecha de entrega de cada intento,
   para saber si fue antes o después del vencimiento.
No incluyas a docentes, ayudantes ni coordinación.

ARCHIVOS DE SALIDA (CSV, UTF-8, separador coma, decimales con punto)
1. columnas.csv
   nrc, columna, tipo, puntaje_maximo, fecha_vencimiento, cuenta_para_final,
   es_nota_final
2. notas.csv   (una fila por estudiante y columna)
   nrc, id_estudiante, columna, valor, escala, estado, fecha_entrega
3. estudiantes.csv   (una fila por estudiante)
   nrc, id_estudiante, inscripcion_activa, ultimo_acceso
4. informe_extraccion.md
   fecha y hora de la extracción; por sección: estudiantes obtenidos frente a los
   esperados y número de columnas; secciones o campos que no se pudieron leer y
   por qué; cualquier diferencia entre secciones en los nombres de las columnas.

ENTREGA
Guarda los cuatro archivos en mi Google Drive, en una carpeta nueva llamada
"FACU0004 202620 - Extracción Blackboard". Si no puedes escribir en Drive,
entrégamelos para descargar.

VERIFICACIÓN ANTES DE TERMINAR
- Que estén las 31 secciones, o la lista exacta de las que faltan.
- Que el conteo por sección sea cercano al esperado; explica las diferencias
  mayores a 5 estudiantes.
- Que ningún archivo tenga nombres, RUT, correos ni usuarios: revísalo y dímelo
  expresamente.
- Que los códigos de estudiante no se repitan entre secciones.

Termina con un resumen de cinco líneas: secciones leídas, estudiantes totales,
columnas comunes a todas las secciones, problemas encontrados y dónde quedaron
los archivos.
```
