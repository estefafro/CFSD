---
name: adaptar
description: Genera una versión de un documento de investigación ya terminado para una audiencia concreta o como guion de presentación. Úsalo cuando la usuaria pida adaptar, simplificar, o convertir en clase o charla una investigación existente.
---

# /adaptar <tema> <audiencia>

1. Ubica `investigaciones/<tema>/04_documento.md`. Si no existe, avisa que
   primero hay que completar `/investigar`.
2. Si no se indicó audiencia, muestra los perfiles de
   `config/audiencias.md` y pregunta cuál (acepta descripciones libres:
   público, duración, formato).
3. Lanza el agente `adaptador` con la carpeta y la audiencia. Varias
   audiencias se lanzan en paralelo.
4. Revisa que la versión conserve las citas y no agregue afirmaciones
   nuevas, y entrégala desde `05_versiones/`.
