# Del Alba S.A. — Carpeta del caso

**Origen:** llamada saliente de Alex (agente de voz SYNCON en Dapta) del **2026-09-16, 17:06 hora Bogotá**, a **Wilson Álvarez** (`walvarez@delalba.com.co`, +57 311 764 8755). Registro `call_4c5c4de7-4ec3-4d40-b755-e8a450ee10e6`.

**Resultado:** `pidio_callback` · interés **medio** · 170 s (la llamada más larga del lote de 72) · sin fecha confirmada.
**Objeción textual registrada:** *"¿Y me podrían enviar un brochure o un catálogo de la del ofrecimiento que van a hacer para saber de qué se trata exactamente?"*

**Fue el único resultado con valor comercial de las 72 llamadas del lote.**

---

## Contenido

| Archivo | Qué es | Tier | Estado |
|---|---|---|---|
| [`01-deep-research-2022-2025.md`](./01-deep-research-2022-2025.md) | Investigación de la compañía y del sector 2022–2025, con fuentes | **T1 interno** | Listo |
| [`02-muestra-mapeo-de-procesos-criticos.md`](./02-muestra-mapeo-de-procesos-criticos.md) | **La muestra** reescrita como documento especial, con eje en el mapeo de procesos críticos. Es lo que se le manda a Wilson en lugar del catálogo que pidió | **T2 · client-facing** | ⛔ **Requiere gate 3-de-3 antes de enviar** |

El análisis del lote de llamadas y el diseño del loop viven aparte, porque no son del caso Del Alba sino de la operación de Alex:
→ [`operacion/llamadas-alex/2026-09-16-analisis-lote-y-loop-2x-dia.md`](../../operacion/llamadas-alex/2026-09-16-analisis-lote-y-loop-2x-dia.md)

---

## El hallazgo que ordena el caso

En 2025 Del Alba reportó **ingresos +26,02 %** y al mismo tiempo **EBIT −12,22 %**, con **activos +36,04 %** y **deuda/capital +41,99 %** (EMIS, datos financieros 2025).

Creció una cuarta parte y ganó menos operando, en un año en que su mercado creció (+7,5 % la producción de alimentos en Colombia), su categoría crece (snacks saludables, ~USD 890 M en Colombia) y la regulación lo favorece (el impuesto a ultraprocesados llegó al 20 % y su portafolio está construido por fuera de lo que ese impuesto castiga).

**No es un problema de demanda. Es un problema de procesos que no crecieron al mismo ritmo.** Ese es el eje del documento que se le manda.

---

## Pendientes antes de volver a contactar

1. ⚠️ **Resolver la cifra de crecimiento.** La base Apollo dio `crecimiento_pct = 10` y Alex dijo "cercano al diez por ciento" en la llamada; EMIS reporta **+26,02 %**. Hay que definir cuál es correcta y dejar una sola en el documento. Decirle a un gerente un número equivocado sobre su propia empresa cuesta la reunión.
2. **Gate 3-de-3** sobre `02-…` (Cris CEO + Pipe CTO + Lorena COO) — es material T2 que viaja al cliente.
3. **Confirmar cargo y nombre completo de Wilson Álvarez.** Hoy solo tenemos nombre de pila del registro de llamada y correo corporativo.
4. **Decidir si se compra el informe EMIS completo** (USD 29,95) para llevar cifras absolutas en COP a la reunión, en vez de solo variaciones porcentuales.
5. **Agendar el callback.** Wilson dijo que el jueves tenía el día ocupado y prefería "temprano en la semana". Alex propuso lunes 9:00 a. m. y la llamada se cortó antes de confirmar.

---

## Nota de trazabilidad — el HANDOFF.md

El encargo apuntaba a `Clientes\Syncon Solutions\Base-Apollo-ICP-Calificados\Llamadas-Alex\Del-Alba\HANDOFF.md`. **Ese archivo no es accesible desde esta sesión**: no está en el repositorio, ni en Google Drive, ni en el SYNCON Brain — es una ruta local de la máquina de Lorena.

En su lugar, el caso se reconstruyó desde las fuentes primarias: **el registro completo de la llamada en Dapta** (transcripción, análisis post-llamada, variables de entrada), **el guion y el contexto del agente Alex**, y **fuentes públicas** sobre Del Alba y su sector.

Si el HANDOFF.md contenía instrucciones de formato o alcance distintas de lo que se hizo aquí, hay que contrastarlo — en particular la definición exacta de qué era "la muestra" original. La interpretación aplicada fue: *el informe que Alex promete enviar al prospecto*, reescrito de informe genérico de sector a lectura de procesos críticos de la empresa concreta.
