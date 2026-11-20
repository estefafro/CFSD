# Reglas del sistema

Valen para los seis agentes y para cualquier sesión que trabaje en este repositorio.
`scripts/verificar.py` las comprueba; si falla, el trabajo no está terminado.

## 1. Toda afirmación lleva etiqueta, y los hechos llevan fuente y fecha

Cada afirmación va en **una sola línea** que empieza con una de tres etiquetas:

```
- [HECHO] Lo que se afirma. Fuente: <URL o cita completa> (consultado 2026-11-11)
- [HIPÓTESIS] Lo que se cree pero no está verificado, y qué lo confirmaría.
- [PROPUESTA] Lo que se recomienda hacer, y en qué hechos se apoya.
```

- Un `[HECHO]` sin `Fuente:` y sin fecha `AAAA-MM-DD` no es un hecho: se rebaja a `[HIPÓTESIS]` o se elimina.
- La fuente es lo que el agente realmente leyó en esa sesión. Nunca se cita de memoria ni se inventa una URL, un DOI o una cifra.
- Si la fuente tiene fecha de publicación, se anota también: `Fuente: OPS, 2024, <URL> (consultado 2026-11-11)`.
- Lo que dice la titular del cargo sobre su propia situación es un hecho con fuente `Fuente: titular del cargo (conversación AAAA-MM-DD)`.

## 2. Ningún indicador sin respaldo del benchmark

Todo indicador se escribe con este bloque, y `Respaldo:` apunta a un archivo que existe en `produccion/benchmark/`:

```
### Indicador: <nombre>
- Definición: qué se mide y cómo.
- Meta: valor y plazo.
- Respaldo: produccion/benchmark/<archivo>.md
```

Si el benchmark todavía no cubre el tema, no se crea el indicador: se deja como `[PROPUESTA]` de pedirle al agente Benchmark que lo investigue.

## 3. Nada se sobrescribe

- Todo lo que producen los agentes va a `produccion/<agente>/` (las actas, a `produccion/actas/`) en un archivo **nuevo**: `AAAA-MM-DD-HHMM-<tema>.md`. La fecha y hora se obtienen con `date +%Y-%m-%d-%H%M`.
- Un archivo de `produccion/` nunca se edita, se renombra ni se borra. Para corregir o actualizar se escribe un archivo nuevo con `reemplaza:` apuntando al anterior.
- Única excepción: un borrador recién creado que todavía no está confirmado en git puede corregirse (por ejemplo, si `verificar.py` lo rechaza). Una vez confirmado, queda fijo.
- Un hook (`scripts/no_sobrescribir.py`) bloquea los intentos de escribir sobre un archivo confirmado, y `verificar.py` revisa el historial de git.

## Encabezado de cada archivo de producción

```
---
agente: actualizador
fecha: 2026-11-11
titulo: Estado de la interoperabilidad en la región
reemplaza: produccion/actualizador/2026-10-01-0900-interoperabilidad.md   # opcional
---
```

`agente` es uno de: `actualizador`, `gestor-cargo`, `benchmark`, `brechas-indicadores`, `guia`, `trayectoria`.
Las actas van en `produccion/actas/` con `agente: guia`.

## Límites

- Los agentes leen; no actúan fuera del repositorio. No envían correos, no publican, no modifican documentos externos ni calendarios.
- `perfil/` lo corrige la titular del cargo. Un agente puede proponer cambios al perfil como `[PROPUESTA]` en su producción, pero no lo edita por su cuenta.
- Cuando falta información, se dice que falta. No se rellena.
