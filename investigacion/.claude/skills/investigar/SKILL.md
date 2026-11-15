---
name: investigar
description: Ejecuta el flujo completo de investigación sobre un tema (búsqueda, matriz de extracción, verificación, índice, documento y versiones por audiencia) coordinando a los agentes del repositorio. Úsalo cuando la usuaria entregue un tema o keywords para investigar, o quiera retomar una investigación existente.
---

# /investigar <tema o keywords>

Tú eres el orquestador. Coordinas a los agentes `buscador`, `extractor`,
`verificador`, `redactor` y `adaptador`, y te detienes en los puntos de
aprobación. Los agentes no pueden preguntarle nada a la usuaria: todas las
consultas y aprobaciones pasan por ti.

Si `investigaciones/<tema>/` ya existe, lee `estado.md` y retoma desde la
fase pendiente en lugar de empezar de nuevo.

## Fase 0 — Brief

1. Crea `investigaciones/<slug-del-tema>/` (minúsculas, sin acentos, guiones).
2. Propón el brief en `00_brief.md`: tema, keywords en español e inglés,
   disciplina(s), ejes de contexto (parte de `config/ejes_contexto.md` y
   quita, renombra o agrega según el tema), ventana de años por eje y
   límites (15 papers; recientes = últimos 5 años).
3. Pregunta solo lo que no puedas inferir (foco, población, país de interés).
   Si el tema es claro, muestra el brief y avanza.

## Fase 1 — Búsqueda → APROBACIÓN 1 (corpus)

1. Lanza `buscador` con la ruta de la carpeta.
2. Presenta a la usuaria: tabla del corpus, cobertura por eje, pendientes de
   acceso y reserva.
3. **Detente y pide aprobación.** Ella puede quitar o agregar fuentes, o
   subir PDF a `pdfs/`. Aplica sus cambios en `01_corpus.md`.

## Fase 2 — Matriz → APROBACIÓN 2 (columnas y contenido)

1. Lanza `extractor`.
2. **Ciclo de vacíos:** si el extractor devuelve "Pedidos al buscador" o
   `validar_matriz.py` avisa de ejes cortos, lanza `buscador` con el pedido
   dirigido y luego `extractor` para las fuentes nuevas. Máximo 2 vueltas;
   si el vacío persiste, infórmalo como límite de la literatura disponible.
   Respeta siempre el tope de 15 papers: una fuente nueva puede reemplazar a
   una más débil, y ese reemplazo se le informa a la usuaria.
3. Lanza `verificador`. Las fuentes con `doi_verificado = no` se corrigen o
   se excluyen.
4. Presenta la matriz. Si hay conector de Google Sheets, ofrece copiarla a
   una hoja para revisarla cómodamente; el CSV del repositorio sigue siendo
   la versión oficial, así que si ella edita la hoja, trae los cambios de
   vuelta al CSV.
5. **Detente y pide aprobación**, mostrando también las "Sugerencias de
   columnas". Si pide cambiar columnas: actualiza
   `config/columnas_matriz.csv`, relanza `extractor` para completar las
   nuevas y vuelve a verificar.

## Fase 3 — Índice → APROBACIÓN 3

1. Lanza `redactor` en modo índice.
2. Presenta el índice con las fuentes por sección y las secciones débiles.
3. **Detente y pide aprobación.** Aplica sus ajustes en `03_indice.md`.

## Fase 4 — Documento

1. Lanza `redactor` en modo documento.
2. Si pide respaldo para alguna afirmación, corre el ciclo de vacíos
   (buscador → extractor → verificador) y relanza el redactor.
3. Comprueba que toda cita del texto esté en las referencias y viceversa, y
   que cada una corresponda a una fila de la matriz.
4. Entrega `04_documento.md`.

## Fase 5 — Audiencia (opcional)

Pregunta para qué audiencia(s) quiere versiones (ver `config/audiencias.md`)
y lanza `adaptador` una vez por audiencia, en paralelo si son varias.

## En todo momento

- Mantén `investigaciones/<tema>/estado.md`: fase actual, decisiones de la
  usuaria, vueltas del ciclo de vacíos y pendientes.
- Haz commit al cerrar cada fase, con un mensaje que nombre el tema y la fase.
- Informa con franqueza: si algo no se pudo verificar o un eje quedó débil,
  dilo en el resumen de la fase.
