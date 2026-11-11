# CFSD · Sistema de agentes de salud digital

Seis agentes que trabajan para la titular de un cargo académico en salud digital, un tablero para
consultarlos y una reunión donde cada uno informa y el Guía levanta el acta.

| # | Agente | Qué hace | Deja su producción en |
|---|--------|----------|-----------------------|
| 1 | **Actualizador** | Busca en todos los ámbitos de salud digital y resume en qué está cada uno. | `produccion/actualizador/` |
| 2 | **Gestor del cargo** | Apila las cargas de trabajo y levanta riesgos. | `produccion/gestor-cargo/` |
| 3 | **Benchmark** | Compara la docencia en salud digital en el mundo, a todo nivel. | `produccion/benchmark/` |
| 4 | **Brechas e indicadores** | Convierte el benchmark en indicadores y necesidades concretas. | `produccion/brechas-indicadores/` |
| 5 | **Guía** | Lee a todos, orienta en el cargo, fija indicadores y levanta el acta. | `produccion/guia/`, `produccion/actas/` |
| 6 | **Trayectoria** | Cuida el proyecto a 10 años: doctorado, publicaciones, posicionamiento regional. | `produccion/trayectoria/` |

## Cómo se usa

Los agentes corren dentro de Claude Code, con este repositorio abierto.

- **Consultar a un agente**: `Usa el agente benchmark para responder: <tu pregunta>`.
  El tablero arma esa frase por ti: escribe la pregunta en la tarjeta y pulsa *Consultar*.
- **Reunión**: `/reunion` (o `/reunion <foco>`). El botón *Reunión* del tablero copia el comando y lista las actas.
- **Tablero**: abre `tablero/index.html`. Se regenera con `python3 scripts/generar_tablero.py`.

El tablero es una vista sin servidor: muestra las carpetas y prepara las consultas, pero quien ejecuta a
los agentes es Claude Code.

## Antes de la primera reunión

Completa `perfil/`. Sin eso los agentes dirán que les falta contexto en lugar de suponerlo.

- `perfil/cargo.md` — el cargo, las horas reales y el proyecto a 10 años.
- `perfil/capacidades.md` — mapa de capacidades (propuesta inicial, por corregir).
- `perfil/ambitos.md` — ámbitos que sigue el Actualizador (propuesta inicial, por corregir).
- `perfil/cargas.md` — cargas de trabajo vigentes.

## Reglas

Están en [`sistema/REGLAS.md`](sistema/REGLAS.md) y se comprueban con `python3 scripts/verificar.py`
(también en cada push, vía GitHub Actions):

1. Toda afirmación con fuente y fecha, separada en `[HECHO]`, `[HIPÓTESIS]` o `[PROPUESTA]`.
2. Ningún indicador sin respaldo del benchmark.
3. Nada se sobrescribe: cada producción es un archivo nuevo y fechado; un hook bloquea la escritura sobre
   archivos ya confirmados.

## Estructura

```
.claude/agents/      los seis agentes
.claude/skills/      /reunion
.claude/settings.json  hook que impide sobrescribir produccion/
sistema/             reglas y ficha de los agentes para el tablero
perfil/              lo que la titular define y corrige
produccion/          lo que producen los agentes (solo se agrega)
scripts/             verificar.py, generar_tablero.py, no_sobrescribir.py
tablero/             plantilla.html y el index.html generado
```
