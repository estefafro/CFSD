# Sistema de agentes de investigación

Repositorio para investigar un tema y producir material académico de
divulgación (base para clases y presentaciones). Todo en español.

## Flujo

`/investigar <tema>` coordina cinco agentes (`.claude/agents/`):

1. `buscador` → `01_corpus.md`
2. `extractor` → `02_matriz.csv`
3. `verificador` → `02_verificacion.md` y columna `doi_verificado`
4. `redactor` → `03_indice.md` y `04_documento.md`
5. `adaptador` → `05_versiones/<audiencia>.md`

Hay tres aprobaciones de la usuaria: corpus, matriz (columnas y contenido) e
índice. No se avanza de fase sin ellas.

## Reglas del proyecto

- Máximo 15 papers por tema, más hasta 5 fuentes no-paper para contexto.
- El eje `estudios_recientes` solo admite los últimos 5 años; origen e
  historia no tienen límite de antigüedad.
- Citas y referencias en APA 7.
- Nunca se inventa una fuente, un DOI, una cita textual ni una cifra. Lo que
  no se pudo comprobar se informa como no comprobado.
- Todo lo que afirma el documento debe poder rastrearse a una fila de la matriz.
- Las columnas de la matriz se definen en `config/columnas_matriz.csv`; para
  cambiarlas se edita ese archivo, no los agentes.
- La matriz se escribe con el módulo `csv` de Python, nunca a mano.
- Si falta acceso al texto completo de una fuente, se marca `pendiente` y se
  le pide a la usuaria (tiene cuentas institucionales); sus PDF van en
  `investigaciones/<tema>/pdfs/`.

## Comprobaciones

```bash
python3 scripts/verificar_doi.py investigaciones/<tema>/02_matriz.csv --actualizar
python3 scripts/validar_matriz.py investigaciones/<tema>/02_matriz.csv --ejes <ejes del brief>
```
