# Alex — Análisis del lote del 16-sep y diseño del loop 2×/día

> **Tier:** T1 interno · **Agente:** `Alex - Llamadas en frío / Ventas` (`7a31c5c8-93c6-47c4-b243-2b5b3fc09299`, Dapta, voz `aura-2-gloria-es`, es-419, gpt-4.1)
> **Lote analizado:** 72 llamadas · **2026-09-16, 16:58:07 → 17:07:22 hora Bogotá**
> **Compilado:** 2026-09-16

> ⚠️ **Nota sobre la fecha.** El encargo pedía revisar "las llamadas de Alex del 17-sep". En el workspace de Dapta **no existen llamadas del 17 de septiembre**: el histórico completo del agente son **75 llamadas** — 3 de prueba en una franja de las 11:00 y las **72 de este lote, del 16 de septiembre por la tarde**. Este análisis es sobre ese lote, que es el único lote real de producción que existe. Si hubo o va a haber un lote del 17, este documento se re-corre sobre él sin cambios de método.

---

## 1. Resultado del lote, sin adornos

**72 llamadas. 9 conversaciones con un ser humano. 0 reuniones agendadas.**

| Resultado | Llamadas | % del lote |
|---|---:|---:|
| Buzón de voz | 39 | 54,2 % |
| No contestó | 19 | 26,4 % |
| Sin resultado (no timbró) | 4 | 5,6 % |
| Persona equivocada | 3 | 4,2 % |
| No interesado | 5 | 6,9 % |
| Número malo | 1 | 1,4 % |
| **Pidió callback** | **1** | **1,4 %** |
| **Agendó** | **0** | **0 %** |

**Razón de desconexión** — buzón 38 · el prospecto colgó 18 · el agente cerró 5 · inactividad 5 · no contestó 4 · falla del proveedor telefónico 1 · destino inválido 1.

**Duración** — mediana **5,3 s**; media de las conectadas 19,6 s; la más larga **170 s** (Del Alba).

**Interés declarado** — 66 bajo · 2 medio · 4 sin dato. **Sentimiento** — 67 neutral, 1 negativo, 0 positivo.

**Consumo** — 13.914 créditos para 9 conversaciones humanas ≈ **1.546 créditos por conversación**, y ninguna reunión.

**El único resultado del día con valor comercial fue Del Alba** (Wilson, interés medio, 170 s, pidió brochure). Lleva su propia carpeta: [`clientes/del-alba/`](../../clientes/del-alba/).

---

## 2. Las cuatro causas — en orden de cuánto pesan

### Causa 1 · La hora. Es el problema más grande y el más barato de arreglar.

Las 72 llamadas salieron entre las **16:58 y las 17:07 hora Bogotá**. Es decir: **el lote entero se disparó al filo del cierre de la jornada**, cuando un gerente de PYME o ya se fue, o está cerrando el día y no toma llamadas desconocidas.

El resultado es aritmético: **80,6 % del lote no alcanzó voz humana** (buzón + no contestó + no timbró). La distribución horaria del propio agente lo confirma, aunque con muestras muy distintas:

| Franja local | Llamadas | Tasa de conexión | Tasa de éxito |
|---|---:|---:|---:|
| 11:00 | 3 | 33,3 % | 33,3 % |
| 16:00 | 72 | **20,8 %** | 5,6 % |

*(La franja de las 11 tiene n=3: es indicio, no evidencia. La de las 16 sí es concluyente.)*

Hay además una contradicción interna: **el propio prompt de Alex agenda reuniones "de lunes a viernes entre las nueve de la mañana y las cuatro de la tarde"** — y el lote salió a las 17:00, fuera de la ventana que el agente mismo ofrece.

### Causa 2 · El ritmo. 7,8 llamadas por minuto.

72 llamadas en 9 minutos y 15 segundos. Eso es concurrencia alta sostenida: muchas líneas marcando a la vez contra una base pequeña. Dos consecuencias:

- **Se quema la base entera en una sola ventana horaria.** Si esa ventana es mala —y lo fue— no queda nada para reintentar en una buena.
- **Riesgo de reputación del número saliente.** Ráfagas densas desde un mismo número (+57 350 696 8263) son exactamente el patrón que las operadoras marcan como spam. Hoy todavía timbra; con dos o tres lotes más así, puede dejar de hacerlo.

### Causa 3 · La base. Se gastó el mejor gancho primero y con datos sucios.

La base venía **ordenada**: los **primeros 19 registros traen `crecimiento_pct`; los 53 restantes vienen vacíos.** El marcador la recorrió en orden.

Resultado: **los 19 leads con el gancho fuerte se consumieron en los primeros ~2,5 minutos**, dentro de la peor franja horaria del día. Los otros 53 se llamaron con el guion degradado — el que solo puede decir "está entre las que reportaron crecimiento el año pasado", sin cifra.

Además, la calidad de los campos tiene defectos verificables:

- **3 de las 9 conversaciones humanas (33 %) fueron con la persona equivocada** — "no trabajo allá", "Diana ya no trabaja aquí", "ya no trabajo en RP Médicas". La base de contactos está desactualizada.
- **Sectores mal asignados.** `Agro-Costa` → "comercio de autopartes". `Comercial Papelera` → "ingeniería mecánica e industrial". `Alpapel` → "diseño gráfico". El gancho de apertura de Alex **depende** de `{{sector}}`: un sector equivocado hace que la primera frase suene a error, y la primera frase es todo.
- **Nombres de empresa genéricos** como `Automatización`, que no sostienen un reconocimiento creíble.
- **1 destino inválido** y **1 falla del proveedor telefónico**.
- **Discrepancia de cifra en el caso caliente:** la base dio `crecimiento_pct = 10` para Del Alba; el registro público (EMIS) reporta **+26,02 %** en ingresos netos de 2025. Alex dijo el 10 en la llamada. **Hay que resolver cuál es el número correcto antes de volver a hablar con Wilson.**

### Causa 4 · La apertura pierde a la gente en los primeros 20 segundos.

De las 5 llamadas marcadas "no interesado", **3 se cayeron antes de los 30 segundos** y una a los 61 s:

| Empresa | Duración | Qué pasó |
|---|---:|---|
| Rodamundi | 16 s | Preguntó "¿a dónde llaman?" y colgó |
| Aquaterra | 18 s | Pidió que repitieran y colgó |
| GHER Asociados | 29 s | "No" al pedido del minuto |
| Comercial Papelera | 61 s | "¿De qué se trata?" y se cortó |
| Cable Servicios | 93 s | **Única objeción real**: no hay presupuesto, no se contempló el año pasado |

Solo **una de las cinco** llegó a dar una razón de negocio. Las otras cuatro se cayeron **en el saludo**, antes de que el motivo llegara a escucharse. El guion ya anticipa el riesgo ("nunca pidas el minuto en seco"), pero cuatro de cuatro caídas ocurrieron justo ahí.

Y en la única llamada que sí funcionó —Del Alba, 170 s— **el desenlace fue una petición de material que el guion está diseñado para esquivar**: Alex respondió "lo ideal es tener primero la reunión corta" y Wilson colgó sin confirmar fecha. Interés medio convertido en nada por no tener qué mandar.

---

## 3. Qué se arregla antes de volver a marcar

Ordenado por relación entre impacto y esfuerzo. Los cinco primeros son condición para reactivar el loop.

| # | Cambio | Dónde | Por qué |
|---|---|---|---|
| 1 | **Mover la marcación a dos ventanas: 09:30–11:30 y 14:00–16:00** | Programación de campaña | Es la causa de 4 de cada 5 llamadas perdidas. Nada más importa hasta arreglar esto |
| 2 | **Bajar el ritmo a ~1 llamada cada 45–60 s por línea** | Concurrencia de campaña | Protege la reputación del número y reparte la base entre las dos ventanas |
| 3 | **Barajar la base o separar las colas por `crecimiento_pct`** | Preparación del lote | Deja de quemar los mejores leads en los primeros 2 minutos |
| 4 | **Validar `sector`, `contact_name` y `crecimiento_pct` antes de cargar** | Preparación del lote | 33 % de persona equivocada y tres sectores mal asignados verificados |
| 5 | **Producir el "informe breve del sector" que Alex promete** | Material | Hoy el agente lo ofrece en el cierre y **no existe**. Ver plantilla en `clientes/del-alba/02-…` |
| 6 | Añadir variante de apertura para cuando pregunten "¿a dónde llaman?" antes del motivo | Prompt, Flujo 1 | Cuatro caídas del lote fueron ahí |
| 7 | Revisar la regla de "no mandar material antes de la reunión" | Prompt, Objeciones | Costó el único lead caliente del día |
| 8 | Alinear la ventana de agendamiento del prompt (9:00–16:00) con la ventana real de marcación | Prompt + campaña | Hoy se contradicen |

**Sobre el punto 7 — recomendación explícita.** El guion actual trata "mándeme información" como objeción a superar con dos intentos. Con el material correcto disponible, **es mejor convertirla en el siguiente paso**: *"se lo mando hoy mismo y lo llamo el lunes a las nueve para que me diga si le hizo sentido"*. Eso convierte un `pidio_callback` sin fecha en una cita con excusa. Requiere tener el documento listo — por eso el punto 5 va antes.

---

## 4. El loop 2×/día

### 4.1 Forma general

Dos bloques diarios de marcación, de lunes a viernes, con una revisión humana entre ellos y un cierre al final del día. **Ningún bloque arranca sin que un humano haya aprobado su lista.** Los agentes proponen; la gente de SYNCON ratifica (ADR-035).

```
07:30  Preparación        (automático)  Se arma la lista del bloque A. Validaciones. Reporte a Telegram.
08:30  Puerta humana      (persona)     Lorena revisa y aprueba/corrige la lista de A.
09:30  ── BLOQUE A ──     (Alex)        Marcación, ~2 h, ritmo controlado
11:30  Cierre A           (automático)  Resultados, callbacks, cola de material a enviar
12:30  Puerta humana      (persona)     Se aprueban envíos de material y se corrige la lista de B
14:00  ── BLOQUE B ──     (Alex)        Marcación, ~2 h
16:00  Cierre B           (automático)  Reporte del día. Cola de mañana pre-armada
16:30  Revisión del día   (persona)     5 min: qué entró al pipeline, qué se manda, qué se ajusta
```

**Regla dura: nada sale después de las 16:30.** Es la franja que produjo este lote.

### 4.2 Los dos bloques no son el mismo bloque dos veces

Tienen composición distinta a propósito:

| | **Bloque A — 09:30 a 11:30** | **Bloque B — 14:00 a 16:00** |
|---|---|---|
| Propósito | Primer contacto en frío | Reintentos y seguimiento |
| Composición | 70 % leads nuevos con `crecimiento_pct` · 30 % reintentos de buzón del día anterior | 50 % leads nuevos sin `crecimiento_pct` · 30 % reintentos · 20 % **callbacks comprometidos** |
| Volumen objetivo | 25–35 llamadas | 25–35 llamadas |
| Ritmo | 1 cada 45–60 s por línea | igual |
| Por qué así | Un decisor de PYME está en su escritorio y todavía no en reuniones. Es la ventana premium: se le dan los mejores leads | Después de almuerzo baja la defensa. Y es la única franja donde cabe honrar un callback prometido "en la mañana" del día siguiente sin invadir el bloque A |

**Máximo ~60–70 llamadas/día**, no 72 en nueve minutos. Mismo volumen, cuatro horas de ventana en vez de nueve minutos.

### 4.3 Matriz de reintentos

Regla base: **nunca dos llamadas al mismo número el mismo día**, y cada reintento cambia de franja.

| Intento | Cuándo | Bloque | Condición |
|---|---|---|---|
| 1 | D+0 | A o B según cola | — |
| 2 | D+2 | **el bloque contrario al del intento 1** | Solo si el 1 fue buzón / no contestó |
| 3 | D+7 | el bloque que falte | Solo si 1 y 2 fueron buzón / no contestó |
| — | **Alto** | — | Tras 3 intentos sin voz humana → `inalcanzable`, sale de la cola activa |

**Salidas inmediatas de la cola:**
- `no_interesado` con objeción de negocio → **nurture**, no se vuelve a llamar en 90 días.
- `no_interesado` por corte en el saludo (<30 s) → **una sola** reprogramación en la franja contraria; si vuelve a caer, sale.
- `persona_equivocada` → **no se vuelve a marcar ese número.** Va a cola de re-investigación con el nombre que la persona dio, si lo dio.
- `numero_malo` / destino inválido → cola de corrección de datos.
- `pidio_callback` → se agenda en el horario que la persona pidió; si no dio horario, bloque B del siguiente día hábil.
- "No me contacten más" → baja inmediata y permanente, y queda registrado (habeas data).

### 4.4 Puertas de calidad — automáticas, antes de marcar

El preparador del lote **rechaza** un registro si:

1. `contact_name` está vacío, es genérico ("Lead", "Contacto"), son solo iniciales o contiene números.
2. `empresa` está vacío o es un término genérico.
3. `sector` está vacío **o no es coherente con el nombre de la empresa** (revisión por lista de exclusiones + muestreo humano del 10 %).
4. El teléfono no tiene formato colombiano válido.
5. El número ya fue marcado hoy, o está en lista de exclusión, o agotó sus 3 intentos.
6. `crecimiento_pct` trae dato **pero no está verificado contra el registro público**. *(Esta es la puerta que habría atrapado el 10 % de Del Alba.)*

Todo registro rechazado va a una cola de corrección con el motivo. **No se marca "por completar el lote".**

### 4.5 Qué reporta cada cierre de bloque

A Telegram, en el mismo formato que el resto de la flota:

- Llamadas hechas · conectadas · **conversaciones con voz humana** (la métrica que importa, no la de "conectadas")
- Resultados por categoría
- **Agendadas** — con empresa, persona, día y hora
- Callbacks comprometidos, con su horario
- Material pendiente de enviar (requiere aprobación humana antes de salir)
- Registros rechazados por las puertas de calidad, con motivo
- Créditos consumidos y **créditos por conversación humana**
- Anomalías: fallas del proveedor, destinos inválidos, caídas bajo 30 s por encima del umbral

### 4.6 Las métricas del loop

Se mide **por bloque**, no por día, porque la comparación A-vs-B es justamente el experimento.

| Métrica | Hoy (lote 16-sep) | Meta primer mes |
|---|---:|---|
| Conversaciones con voz humana / llamadas | **12,5 %** | ≥ 25 % |
| Buzón / llamadas | **54,2 %** | ≤ 35 % |
| Persona equivocada / conversaciones humanas | **33 %** | ≤ 10 % |
| Caídas antes de 30 s / conversaciones humanas | **44 %** | ≤ 25 % |
| Reuniones agendadas / conversaciones humanas | **0 %** | ≥ 15 % |
| Créditos por conversación humana | **~1.546** | ≤ 800 |

**La métrica de gobierno es "conversaciones con voz humana", no "llamadas conectadas".** La tasa de conexión que reporta la plataforma (40 % en el histórico del agente) cuenta como conectadas llamadas que terminaron en inactividad o en un cuelgue de dos segundos. Con esa métrica el lote del 16 se ve aceptable. Con la métrica correcta se ve como lo que fue.

### 4.7 Las dos primeras semanas son un experimento, no una operación

Con un solo lote y una franja horaria no hay evidencia para fijar las ventanas definitivas. Propuesta:

- **Semana 1–2:** correr A y B con composición balanceada y **registrar la tasa de voz humana por hora exacta**, no por bloque.
- **Al cierre de la semana 2:** `get_hourly_call_distribution` sobre el acumulado, y **mover las ventanas a las dos mejores horas reales**, que pueden no ser las propuestas aquí.
- Hasta entonces, las franjas 09:30–11:30 y 14:00–16:00 son **la mejor hipótesis disponible**, sostenida por una muestra de n=3 en la franja de las 11 y por el sentido común del horario de una PYME colombiana. **No es un dato duro y no debe presentarse como tal.**

---

## 5. Qué hay que decidir (no es decisión nuestra)

1. **¿Se detiene la marcación hasta tener los puntos 1–5 de §3 listos?** Recomendación: sí. Otro lote como el del 16-sep gasta base y reputación de número sin producir pipeline.
2. **La cifra de crecimiento de Del Alba: ¿10 % o 26 %?** Bloquea el re-contacto con Wilson y revela si la base Apollo entera tiene el mismo defecto.
3. **¿Se cambia la regla de "no mandar material antes de la reunión"?** Recomendación: sí, con material propio y un callback con fecha atado al envío.
4. **¿Quién opera la puerta humana de 08:30 y 12:30?** El loop no arranca sin dueño.
5. **¿Se compra el informe EMIS de Del Alba (USD 29,95)** para llevar cifras absolutas a la reunión, en vez de solo variaciones porcentuales?

---

## 6. Anexo — de dónde salen las cifras

Todo lo cuantitativo de este documento sale del workspace de Dapta consultado el 2026-09-16:

- `list_calls` sobre el agente `7a31c5c8-93c6-47c4-b243-2b5b3fc09299` desde 2026-09-14 → 72 llamadas, con transcripción, `call_analysis`, `custom_analysis_data`, `llm_dynamic_variables`, `disconnection_reason`, `duration_ms`, `call_cost` y `credits`.
- `get_call_analytics` sobre el mismo agente → histórico total de 75 llamadas, 30 conectadas, tasa de conexión 40 %, desglose por razón de desconexión.
- `get_hourly_call_distribution` (timezone `America/Bogota`, 2026-07-01 → 2026-09-17) → solo dos franjas con datos: 11:00 (n=3) y 16:00 (n=72).
- `get_agent` con `include_prompt` e `include_context` → guion completo, variables de entrada/salida, `post_call_analysis_data` y contexto de compañía.

Las citas textuales de prospectos provienen de las transcripciones de las llamadas correspondientes y se reproducen sin edición.
