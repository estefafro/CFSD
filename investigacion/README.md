# Investigación

Sistema de agentes de Claude Code que, a partir de un tema, busca la
literatura, la ordena en una matriz de extracción y redacta un documento
académico de divulgación en español con citas APA 7, pensado como base para
clases y presentaciones.

## Cómo se usa

Abre este repositorio en Claude Code (app, web o terminal; funciona con la
suscripción Claude Max, sin API key) y escribe:

```
/investigar microbiota intestinal y depresión
```

El sistema avanza por fases y se detiene tres veces a pedir tu aprobación:

| Fase | Agente | Produce | Tu decisión |
|---|---|---|---|
| 0. Brief | orquestador | `00_brief.md` | — |
| 1. Búsqueda | `buscador` | `01_corpus.md` | **Aprobar el corpus** |
| 2. Matriz | `extractor` + `verificador` | `02_matriz.csv`, `02_verificacion.md` | **Aprobar columnas y contenido** |
| 3. Índice | `redactor` | `03_indice.md` | **Aprobar el índice** |
| 4. Documento | `redactor` | `04_documento.md` | — |
| 5. Audiencia | `adaptador` | `05_versiones/<audiencia>.md` | Elegir audiencia(s) |

Para adaptar después una investigación ya terminada:

```
/adaptar microbiota-intestinal-y-depresion presentacion
```

## Qué garantiza el diseño

- **Contexto completo.** Cada tema se cubre por ejes: inicio, historia y
  disciplina, aplicación, estudios recientes, limitaciones y oportunidades
  (ajustables por tema en el brief). Cada fuente de la matriz indica qué eje
  alimenta, y el índice se arma desde ahí.
- **Ciclo de vacíos.** Si un eje queda con pocas fuentes o una afirmación
  necesita respaldo, el extractor o el redactor piden una búsqueda dirigida
  al buscador (hasta 2 vueltas).
- **Trazabilidad.** Cada DOI se verifica contra doi.org, cada cita textual
  guarda su página o sección, y el documento solo afirma lo que está en la
  matriz.
- **Límites.** Máximo 15 papers por tema; lo "reciente" son los últimos 5
  años; la historia no tiene límite de antigüedad.

## Qué puedes ajustar

| Para cambiar... | Edita |
|---|---|
| Columnas de la matriz | `config/columnas_matriz.csv` |
| Ejes de contexto por defecto | `config/ejes_contexto.md` |
| Perfiles de audiencia | `config/audiencias.md` |
| Comportamiento de un agente | `.claude/agents/<agente>.md` |
| Fases y aprobaciones | `.claude/skills/investigar/SKILL.md` |

## Estructura

```
.claude/agents/      buscador, extractor, verificador, redactor, adaptador
.claude/skills/      /investigar y /adaptar
config/              columnas, ejes y audiencias
scripts/             verificar_doi.py, validar_matriz.py
investigaciones/     una carpeta por tema
```

## Fuentes

Los agentes usan los conectores que tenga tu cuenta de Claude (por ejemplo
SciSpace, PubMed, Google Sheets) más la búsqueda web. Cuando no logran abrir
el texto completo de una fuente, la marcan como `pendiente`: descárgala con
tu cuenta institucional y déjala en `investigaciones/<tema>/pdfs/`.
