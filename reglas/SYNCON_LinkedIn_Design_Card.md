# SYNCON · LinkedIn Design Card
> Referencia rápida para producción de piezas en LinkedIn. Todo token viene del Design System v1.5 CERRADO.
> Canal: `linkedin.com/company/syncon-solutions` · Actualizado: 2026-06-27

---

## Colores primarios

| Token | Hex | Uso en LinkedIn |
|---|---|---|
| `--ink` | `#0A0A0A` | Fondo dominante de todas las piezas |
| `--paper` | `#FAFAFA` | Texto principal, titulares |
| `--accent` | `#FF6B00` | Números clave, kickers, slash del logo, CTAs, dot animado |
| `--accent-hover` | `#FF8833` | Estados secundarios, datos complementarios |

---

## Colores secundarios

| Token | Hex | Uso en LinkedIn |
|---|---|---|
| `--bg-2` | `#1A1A1A` | Slides internas (alternado con `#0A0A0A`), fondos de datos |
| `--fg-2` | `#CCCCCC` | Texto de cuerpo en slides, bullets, descripciones |
| `--muted` | `#888888` | Fechas en receipts, labels terciarios, subtítulos técnicos |
| `--border` | `#444444` | Divisores, bordes de tiles, separadores entre slides |

**Colores de carril de agente** (solo en piezas de producto/HAR — nunca como accent general):
- CEO `#00E5FF` · COO `#FFB300` · CTO `#00E676`

**Prohibidos en LinkedIn:** magenta `#FF0055` · "AI purple"/neon · cualquier gradiente de color · fondos blancos o claros · beige · azules SaaS genéricos.

---

## Tipografía

| Elemento | Familia | Peso | Tamaño orientativo |
|---|---|---|---|
| Titular portada (slide 1) | Geist Sans | 800 | 32–40px |
| Titular slides internas | Geist Sans | 700 | 24–28px |
| Cuerpo / desarrollo | Geist Sans | 400 | 16–18px |
| Kicker / etiquetas / logo | Geist Mono | 400–700 | 11–13px |
| Números grandes (receipts) | Geist Mono | 700 | 40–56px |
| Wordmark `/syncon.solutions` | Geist Mono | 700 | Proporcional al formato |

**Reglas fijas:**
- Sentence case en todos los titulares. Nunca Title Case.
- Tracking `.14em` en kickers y labels mono uppercase.
- Cuerpo mínimo 16px — nunca bajar en ningún formato.
- Fallback: `-apple-system, 'Inter', sans-serif` / `'JetBrains Mono', monospace`.

---

## Logo

**Wordmark canónico:** `/syncon.solutions` en Geist Mono 700.
- El slash `/` y el punto `.` siempre en naranja `#FF6B00`.
- El resto del texto en `#FAFAFA` (sobre fondo oscuro) o `#0A0A0A` (variante light, uso muy limitado).

| Variante | Fondo permitido | Uso en LinkedIn |
|---|---|---|
| Primary dark (inverse) | `#0A0A0A` / `#1A1A1A` | **Estándar** — portadas, slides, banner, infografías |
| Primary light | `#FAFAFA` | Solo si el contexto externo lo exige (nunca en slides propias) |
| Favicon `/` standalone | Cualquier fondo oscuro | Avatar de página, foto de perfil si aplica |

**Posición en piezas:** esquina inferior izquierda o inferior derecha de cada slide. Nunca centrado, nunca en la zona de lectura principal.

**Don'ts del logo:**
- Sin gradientes sobre el wordmark.
- Sin drop-shadow.
- Sin recolorar slash/punto fuera de las variantes.
- Sin reescribir en otra fuente.
- Sin rotación ni distorsión.

---

## Formatos LinkedIn — specs por tipo de pieza

### Banner de empresa (1128 × 191 px)
- Fondo `#0A0A0A`.
- Tagline en Geist Sans 800, `#FAFAFA`, alineado a la izquierda.
- Logo `/syncon.solutions` en esquina inferior derecha.
- Barra inferior con 2–3 elementos de validación en Geist Mono 11px `#888888`.
  - Ejemplo: `Bogotá, Colombia · Firma nativa en IA · Company Brain en producción desde 2025`
- El banner opera como el primer activo de mitigación de riesgo: enuncia la transformación operativa, el ICP y la credibilidad en menos de 3 segundos.
- Sin gradientes. Sin stock. Sin robots decorativos. Sin eslóganes vacíos.

---

### Foto de perfil de empresa (300 × 300 px)
- Logo `/` (favicon standalone) sobre fondo `#0A0A0A`.
- Alto contraste: garantiza legibilidad en 36px (tamaño miniatura en comentarios).
- Sin texto adicional. Sin borde externo.

---

### Carrusel / Document Post (PDF · 1080 × 1080 px)
Máximo 10 slides recomendado; mínimo 3. El PDF se sube directamente a LinkedIn — cada página del PDF = una card deslizable.

> **Por qué el carrusel es el formato ancla:** genera el mayor dwell time de la plataforma, activa la acción de guardado (señal algorítmica de alta calidad) y funciona como lead magnet pasivo. Es el estándar de oro para contenido educativo, metodología y receipts de datos. — *Blueprint LinkedIn IA B2B 2026*

**Slide 1 — Portada (obligatoria)**
```
Fondo: #0A0A0A
┌──────────────────────────────────────┐
│  [KICKER MONO 13px #FF6B00]          │
│                                      │
│  Titular principal                   │  Geist Bold 32–40px #FAFAFA
│  última línea puede ir en naranja.   │  Geist Bold 32–40px #FF6B00
│                                      │
│  /syncon.solutions        [núm / N]  │  Geist Mono 11px #888888
└──────────────────────────────────────┘
```
La portada debe funcionar sola como imagen de post. Si el lector no desliza, ya entregó valor.
El gancho de la portada sigue el patrón de las firmas de mayor conversión: destruye una creencia del sector o enuncia el costo de un problema operativo real.

**Slides 2–(N-1) — Contenido**
```
Fondo: #0A0A0A o #1A1A1A (alternado)
┌──────────────────────────────────────┐
│  [slide X / total]    esquina sup-der│  Geist Mono 11px #888888
│                                      │
│  Una sola idea por slide.            │  Geist Bold 24–28px #FAFAFA
│                                      │
│  Desarrollo máx. 2–3 líneas.         │  Geist Sans 16–18px #CCCCCC
│                                      │
│  [dato o receipt si aplica]          │  Geist Mono #FF6B00 si es número clave
│                                      │
│  /syncon.solutions                   │  esquina inferior
└──────────────────────────────────────┘
```

**Slide final — CTA (obligatoria)**
```
Fondo: #0A0A0A
┌──────────────────────────────────────┐
│  [KICKER MONO] "¿Qué sigue?"         │  Geist Mono 13px #FF6B00
│                                      │
│  Acción específica en una línea.     │  Geist Bold 28–32px #FAFAFA
│                                      │
│  ▸ Comenta [PALABRA CLAVE]           │  Geist Sans 16px #FF6B00
│    para recibir [activo concreto]    │
│                                      │
│  /syncon.solutions                   │
└──────────────────────────────────────┘
```
El CTA de la slide final = CTA del texto del post. Siempre consistentes.

**Reglas del carrusel:**
- Una idea por slide. Dos ideas = dos slides.
- Máximo 40 palabras por slide.
- Sin bullets en cascada — una línea por slide o dato visual.
- Números grandes: Geist Mono 40–56px en `#FF6B00`.
- El wordmark aparece en todas las slides sin excepción.
- Peso del PDF exportado: menos de 8 MB.
- Revisar legibilidad a 375px (móvil) antes de publicar.

---

### Post fijado — lead magnet ancla (carrusel 8–10 slides)
> El post fijado es el mecanismo pasivo de captura de leads más crítico de la página. Visible para todo visitante en cualquier momento, sin dependencia del algoritmo. — *Análisis CRO LinkedIn IA B2B 2026*

- Mismo formato que el carrusel estándar (1080 × 1080 px, PDF).
- Estructura específica: portada con promesa que el ICP no puede ignorar → 5–7 slides de valor (síntomas, diagnóstico, marco) → 1 slide de definición del producto → slide CTA con hand-raiser.
- CTA del post: `Comenta [PALABRA CLAVE] y te lo enviamos por mensaje directo.` — nunca un link a formulario en el primer contacto.
- Se reemplaza cada 4–6 semanas con un carrusel de mayor profundidad o un caso de estudio con receipt actualizado.
- No cuenta en el calendario editorial semanal — es adicional y permanente.

---

### Post con imagen individual / infografía (1200 × 627 px landscape · 1080 × 1080 px cuadrado)
- Fondo `#0A0A0A` o `#1A1A1A`.
- Un solo mensaje visual: dato grande + label + fecha, o diagrama de proceso limpio.
- Números en Geist Mono 700 `#FF6B00` — tamaño máximo posible dentro del frame.
- Sin ilustraciones decorativas. Sin redes neuronales. Sin íconos de stock.
- Logo en esquina inferior.
- Texto en imagen: máximo 20 palabras. El desarrollo va en el texto del post.
- Usar landscape (1200 × 627) para diagramas de arquitectura con flujo horizontal; cuadrado (1080 × 1080) para datos y receipts.

**Tipos de imagen que sí van:**
- Diagrama de arquitectura técnica: entrada → orquestación → Company Brain/HAR → salida.
- Proof tile de receipt: número grande + label + fecha.
- Matriz 2×2 de decisión (qué automatizar primero, qué esperar).
- Tabla comparativa "es / no es" (Company Brain vs. chatbot genérico).
- Captura real del sistema (difuminada si necesario) con overlay de contexto.

---

### Screencast / video (60–90 segundos · 16:9 o 1:1)
> La falta de producción es la señal. Los screencasts sin edición demuestran que el sistema existe y funciona — es la táctica "show, don't tell" adaptada a B2B. — *Blueprint LinkedIn IA B2B 2026*

- Sin producción. Pantalla real del sistema: el Company Brain siendo consultado, un agente respondiendo por Telegram, un proceso siendo mapeado en tiempo real.
- Overlay de contexto si aplica: Geist Sans/Mono, fondo `rgba(10,10,10,0.8)`, texto `#FAFAFA`.
- Subtítulos obligatorios (LinkedIn reproduce sin audio por defecto).
- No grabar pantallas con datos de clientes reales sin aprobación 2-of-2.
- Fallback si el video no carga: thumbnail con dato ancla del sistema.

---

### Post de texto nativo
- Sin imagen adjunta, o imagen mínima de refuerzo.
- **Primera línea visible sin expandir = el gancho más fuerte del post.** El algoritmo de LinkedIn muestra ~140 caracteres antes del "ver más". Esa línea es el activo más valioso del post.
- Frases ≤ 25 palabras. Verbos activos. Sin exclamaciones B2B.
- Usted en externo formal. Nunca vos/vosotros.
- Sentence case siempre.
- Máximo 1 emoji funcional si aporta escaneo (▸, ↳) — nunca decorativo.
- Párrafos cortos: máximo 3 líneas seguidas, luego espacio en blanco. LinkedIn no es un blog.

---

## Elementos gráficos

### Patrones visuales canónicos
- **Glow naranja** en tiles y datos clave: `0 0 24px rgba(255,107,0,.22), 0 0 64px rgba(255,107,0,.08)`. Como acento en datos ancla — nunca decorativo general.
- **Borde completo tenue naranja** en tiles de datos: `1px solid rgba(255,107,0,.25)`. Nunca solo el lado izquierdo.
- **Slash `/` como separador** visual entre datos. Color `#FF6B00`.
- **Dot pulsante** (6px, `#FF6B00`) como indicador de sistema en vivo.
- **Fondo con grid sutil** (opacity .16, máscara radial desde el cuadrante superior izquierdo) — atmosférico, nunca protagónico.
- **Corner markers** naranja en el frame de pantalla o video: `2px solid #FF6B00` en las 4 esquinas.

### Iconografía
- **Marcador de lista:** triángulo `▸` en naranja. Nunca bullets circulares genéricos.
- **Separadores:** slash `/` naranja. Nunca guiones ni pipes grises.
- **Indicador de dato con fecha:** `/` + dato fuerte + label mono + fecha muted.
- **Flecha de acción:** `→` en texto cuando el movimiento es parte del significado (no decorativo).

### Proof tiles — receipts visuales
El proof tile es el componente de credibilidad más importante en LinkedIn. Reemplaza los logo walls.

```
┌─────────────────────────────────┐
│  482                            │  Geist Mono 700 · 40–56px · #FAFAFA o #FF6B00
│  PÁGINAS · COMPANY BRAIN        │  Geist Mono · 11px · uppercase · #CCCCCC
│  salud 99/100 · jun 2026        │  Geist Mono · 11px · #888888
└─────────────────────────────────┘
  border: 1px solid rgba(255,107,0,.25)
  border-radius: 8px
  background: #1A1A1A
```

Reglas del proof tile:
- El dato grande va primero. Siempre.
- La fecha es obligatoria — nunca un receipt sin fecha.
- El modificador `.am` (número en naranja) solo en logros propios de SYNCON — datos contextuales van en blanco.
- Nunca fabricar datos. Nunca aproximar sin indicarlo.

### Estilo de imagen / fotografía
- Plantas colombianas e industriales **reales**: Yumbo, Mamonal, Sabana, Barranquilla.
- Manos en teclado, cascos, espaldas — nunca caras sonriendo a cámara.
- Grading: alto contraste + desaturado + tinte naranja en accents.
- Cero "startup office diverso". Cero cerebros brillantes. Cero robots IA.
- Capturas de pantalla reales del sistema (difuminadas si necesario) > cualquier mockup decorativo.

### Diagramas y flujos técnicos
- Líneas limpias, iconografía estandarizada, sin ornamentos.
- Flujo canónico: `entrada de datos → capa de orquestación → Company Brain/HAR → salida`.
- Fondo `#0A0A0A`, nodos en `#1A1A1A` con borde `#444444`, conexiones en `#FF6B00`.
- Tipografía de etiquetas: Geist Mono 11px `#CCCCCC`.
- Los diagramas demuestran maestría de arquitectura — reemplazan las promesas abstractas.

---

## Common patterns de conversión B2B (de la investigación)

Estos son los patrones que las firmas de mayor conversión en LinkedIn aplican consistentemente. No son tendencias — son mecánicas probadas en el ecosistema IA B2B 2025–2026.

### 1. Portada que funciona sola
La portada del carrusel debe poder publicarse como imagen independiente. Si el lector no desliza, ya recibió valor. El gancho sigue una de estas estructuras:
- Destruye una creencia: *"El 80% de los proyectos de IA en empresas medianas fallan en el mismo punto. No es el modelo."*
- Enuncia el costo de no actuar: *"Su empresa pierde conocimiento crítico cada vez que alguien se va. Esto es lo que cuesta."*
- Plantea la pregunta que el ICP ya tiene pero no formula: *"¿Cuánto sabe su operación cuando usted no está?"*

### 2. Hand-raiser (palabra clave en comentarios)
En lugar de un link a formulario (alta fricción), el CTA pide comentar una palabra clave. El COO responde por DM con el activo + una pregunta de descubrimiento.

- Formato: `Comenta DIAGNÓSTICO y te enviamos el checklist por mensaje directo.`
- La pregunta de seguimiento en el DM no es un pitch — es curiosidad genuina: *"¿Cuál de los 5 síntomas generó más ruido interno en tu equipo?"*
- Este punto de contacto humano escala orgánicamente hacia una llamada de consultoría.

### 3. Proof social = receipts dateados, no logos
Las páginas de mayor conversión no usan logo walls. Usan cápsulas de datos reales con fecha visible. Aplicado a SYNCON:
- `482 páginas · salud 99/100 · jun 2026`
- `4 agentes de rol read-only · en producción`
- `CRIS.I.AM operando desde ene 2026`

Nunca datos sin fecha. Nunca datos sin fuente verificable. El receipt reemplaza al testimonio.

### 4. Una idea por slide — densidad deliberada
Las firmas de élite (Neurons Lab, Every, Anthropic) no llenan slides. Ponen una afirmación, un dato, o una pregunta por slide. La densidad baja genera mayor retención cognitiva y más guardados.

Patrón aplicado:
- Slide = una afirmación fuerte
- Desarrollo = máximo 2 líneas de contexto
- Dato o receipt = si aplica, en naranja
- Nada más

### 5. Diagrama técnico como activo de credibilidad
Las consultoras de mayor autoridad (Neurons Lab, Artefact, LeewayHertz) publican diagramas de arquitectura como posts, no como anexos. El diagrama demuestra que la firma tiene sistemas internos, no solo opiniones.

Tipos de diagrama SYNCON para LinkedIn:
- Arquitectura Company Brain + HAR: cómo fluye el conocimiento, quién puede mutarlo, cómo se audita.
- Proceso de diagnóstico contextual: 5h → mapa de procesos → intervención → retainer.
- Comparativa "IA gobernada vs. wrapper de ChatGPT": qué tiene cada uno, qué garantiza cada uno.

### 6. Screencast sin producción = autenticidad
Las firmas que muestran pantallas reales generan más confianza que las que muestran mockups producidos. La baja producción no es un defecto — es la prueba de que el sistema existe.

Guion de screencast SYNCON:
- Plano 1: la pregunta operativa real que un gerente haría.
- Plano 2: el Company Brain siendo consultado (en tiempo real, sin cortes).
- Plano 3: la respuesta con contexto, fecha de la fuente, y carril del agente.
- Sin música. Sin transiciones. Sin voz en off producida.

### 7. El perfil de empresa como landing page
Antes de que el prospecto lea un post, ya evaluó el perfil. Banner → Tagline → About → CTA es la secuencia de conversión del perfil. Sin esta arquitectura, los posts excelentes apuntan a un perfil sin embudo.

Ruta de conversión completa:
`Post → Perfil empresa → CTA → Landing AI Adoption Diagnostic → Formulario 4 campos → Calendly`

### 8. Mix de formatos — no todo es texto
Las páginas de alto rendimiento distribuyen formatos deliberadamente. Publicar solo texto limita el alcance y elimina los activos de generación de leads.

| Formato | % del mix | Función |
|---|---|---|
| Carrusel (Document Post PDF) | 35% | Educación profunda, lead magnet, retención |
| Texto nativo | 30% | Tesis, opinión contraria, interacción |
| Infografía / imagen individual | 20% | Arquitectura técnica, datos, proceso en 1 imagen |
| Screencast / video 60–90s | 10% | Demo viva del sistema |
| Evento / lead magnet promocional | 5% | Captura directa: webinar, descarga |

### 9. Interacción estructurada = pre-calificación
Las encuestas y dilemas no son engagement por engagement. Son escucha activa que expone el dolor real del mercado y pre-califica prospectos antes de una llamada.

Estructura de encuesta SYNCON:
- Pregunta con 4 opciones, cada una revela una prioridad presupuestaria diferente.
- Respuesta en comentarios: el COO responde a cada opción con una pregunta de seguimiento personalizada.
- Máximo 1 encuesta por semana.

### 10. Contenido de autoridad técnica = mitigación de riesgo
El escepticismo ante la IA es la fricción más alta en el ciclo de ventas B2B. El contenido técnico no es para demostrar conocimiento — es para eliminar el miedo del comité de compras.

Temas de autoridad técnica que reducen riesgo percibido en LATAM:
- Qué pasa con los datos propietarios del cliente dentro de un agente IA.
- Cómo el HAR controla quién puede mutar el Company Brain.
- Por qué human-in-the-loop es una garantía operativa, no una limitación del sistema.
- Qué significa que los agentes sean read-only por defecto.

---

## Lo que nunca va

### Colores
- Magenta `#FF0055` (deprecado desde abr 2026).
- "AI purple", neon, cualquier color eléctrico que no sea el accent naranja.
- Gradientes de color (incluyendo gradient text).
- Fondos blancos, beige, gris claro, azul corporativo genérico.
- Saturación de foto al estilo vibrante/colorido.

### Tipografía y copy
- Title Case en titulares en español.
- Exclamaciones B2B ("¡Estamos emocionados de anunciar!").
- "Transformación digital", "soluciones innovadoras", "de clase mundial", "game-changer".
- "Chatbot" o "asistente virtual" → usar "agente de rol".
- "Red de agentes" / "A2A autónomo" (no está en producción).
- Arrogancia sin receipt: cualquier claim sin número + fecha.
- ROI garantizado sin diagnóstico contextual previo.
- Frases > 25 palabras.
- Clientes nombrados sin aprobación 2-of-2 (Cris CEO + Lorena COO).
- "Me complace compartir" / "el futuro de la IA" / "revolucionario".

### Gráfica
- Glassmorphism decorativo.
- `border-left` aislado como único acento de color (side-stripe prohibido).
- Drop-shadows en el logo o el wordmark.
- Ilustraciones vectoriales de robots, cerebros brillantes, redes neuronales, nubes con engranajes.
- Stock photos / "diverse startup office" / sonrisas falsas.
- Logo walls / "Trusted by" vacío sin receipt.
- Más de 40 palabras por slide.
- Bullets en cascada dentro de una slide.
- Más de 2 colores de texto por slide (`#FAFAFA` y `#FF6B00` máximo).
- Slide sin el wordmark `/syncon.solutions`.
- CTA final genérico ("síguenos para más contenido").
- Numeración 01/02/03 como scaffold decorativo sin significado real en la secuencia.
- Imágenes de cerebros, robots, íconos de IA genéricos, redes neuronales decorativas.
- Carrusel con más de 10 slides.

---

## Checklist pre-publicación

### Carrusel
- [ ] Portada funciona sola como imagen de post
- [ ] Cada slide tiene una sola idea
- [ ] Ninguna slide supera 40 palabras
- [ ] El CTA de la última slide coincide con el CTA del texto del post
- [ ] El wordmark aparece en todas las slides
- [ ] El PDF exportado pesa menos de 8 MB
- [ ] Vista a 375px revisada (móvil)
- [ ] Ningún claim sin receipt dateado
- [ ] Ningún cliente nombrado sin aprobación 2-of-2

### Cualquier pieza
- [ ] Primera línea del texto del post funciona como gancho sin expandir
- [ ] El dato principal tiene fecha visible
- [ ] No hay promesas de ROI sin diagnóstico
- [ ] El logo está en la posición correcta
- [ ] No hay más de 2 colores de texto
- [ ] El CTA es específico (palabra clave, enlace concreto, o pregunta de descubrimiento) — nunca "síguenos"

---

*Fuentes: SYNCON Design System v1.5 · Brand Wiki v1.3 · Plan Corrección LinkedIn 2026-06-26 · Análisis CRO LinkedIn IA B2B 2026 · Blueprint Estrategia LinkedIn IA Consultoría 2026*
