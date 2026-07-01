# Spec de diseño — Página "Cómo trabajamos" (`/como-trabajamos`)

**Fecha:** 2026-06-30
**Proyecto:** syncon.solutions — sitio web (`C:\Users\lilia\syncon-netlify-deploy\`)
**Design system:** SYNCON Design System v1.5 (canon CSS §12, esqueleto HTML §13)
**Estado:** aprobado por Lorena (COO) en brainstorming 2026-06-30 — pendiente de revisión del spec antes del plan de implementación.

---

## 1 · Objetivo

Crear una **página dedicada** que explique cómo trabaja Syncon, con dos ideas centrales:

1. **El loop de acompañamiento.** Consultoría → Cerebro corporativo → Software a la medida → Capacitación → Acompañamiento ocurren en un **ciclo continuo**, no en un handoff lineal. El acompañamiento es el diferenciador y la propuesta de valor central (en el canon interno se le llama "foso"; en el copy público se nombra **"la clave"**): va después de cualquier entrega y es donde la efectividad se compone vuelta a vuelta.
2. **El método detrás del diagnóstico.** La secuencia de rediseño de procesos **Eliminar → Simplificar → Optimizar → Automatizar → Medir**, más el principio "la arquitectura del proceso manda sobre la herramienta". Posiciona a Syncon como quien piensa el proceso, no solo lo automatiza.

Es una **página de conversión**: lleva CTAs y, al final, el formulario de contacto + el bloque de agenda de 30 minutos.

## 2 · Decisiones tomadas (brainstorming 2026-06-30)

- **Estructura:** página dedicada nueva (no expandir el home). Archivo `como-trabajamos.html`, URL limpia `/como-trabajamos` (Netlify sirve `.html` automáticamente, igual que `/about` y `/productos`). No requiere cambios en `_redirects`.
- **Profundidad:** loop como héroe + **sección de método completa** (secuencia de 5 etapas).
- **Alcance de esta tanda:** SOLO esta página + repunteo de enlaces. Las subpáginas de producto se revisan en una tanda aparte.
- **Espina narrativa (Enfoque A):** loop primero → método como motor interno → acompañamiento como foso → contacto.
- **Visual del loop (Opción 2):** los 5 nodos como ciclo de iguales, con **Acompañamiento resaltado en naranja** y una **flecha naranja de retorno** que reinicia el ciclo. (Descartada la Opción 1 "órbita".) Nodo 3 etiquetado **"Software e IA a la medida"**.
- **Reframe horizontal del acompañamiento (revisión 2026-06-30, Lorena):** el acompañamiento NO se ata al cerebro corporativo. Es la propuesta de valor central y va después de cualquier entrega (consultoría, implementación de IA, software a la medida, capacitación o cerebro). El loop deja explícito que "no todos los caminos pasan por todas las etapas". Se reemplaza la jerga interna "foso" por **"la clave"** en el copy público.

## 3 · Guardas de marca (Company Brain — no romper)

- No claimear clientes ni tracción (pre-ingresos). Hablar de la **oferta**, no de resultados.
- "Los agentes **proponen**; tu gente **ratifica**." Nunca "agentes autónomos" (ADR-035).
- No sobre-nombrar **HAR** hacia afuera — es el método propietario por detrás; en esta página no hace falta nombrarlo.
- "Construimos, no aconsejamos": todo diagnóstico termina en software en producción, no en un PDF.
- Voz Syncon (Outlaw + Sage): directa, con el motivo `/` slash y h2 bicolor. Se permiten em-dashes (voz Syncon, distinto del canon Dr. Osorio).
- Framing por motor: Consultoría/diagnóstico = "diagnóstico"; Cerebro/software = "construir/unificar".

## 4 · Estructura de la página (6 secciones)

Reutiliza el esqueleto HTML §13 y el CSS §12 del design system. Página autocontenida (un solo `.html` con `<style>` inline propio, como el resto del sitio).

### 4.1 Hero
- Kicker mono naranja: `Cómo trabajamos`
- H2 bicolor (patrón canon): paper `No es un proyecto con fecha de cierre.` / accent `Es un loop de acompañamiento.`
- Lede: "Consultoría, implementación de IA, software a la medida, capacitación y —cuando el caso lo pide— un cerebro corporativo completo. No los entregamos y cerramos: ocurren en un ciclo, y el acompañamiento va después de cualquiera de ellos. Ahí es donde la efectividad se compone, vuelta a vuelta."
- CTA ghost pill → `#contacto`: "Quiero diagnosticar mi operación →"

### 4.2 El loop de acompañamiento — centro visual
- Kicker + h2: `Un ciclo, no una entrega.`
- **Intro de amplitud (importante):** una línea antes o junto al diagrama deja claro que **no todos los caminos pasan por todas las etapas**. La consultoría abre y el acompañamiento cierra; en medio va lo que el caso pida: una implementación de IA, un software a la medida, una capacitación, o el cerebro corporativo completo. Ejemplo de copy: "No todos pasan por todas las etapas. Algunos hacen una consultoría y una implementación de IA; otros, software a la medida; otros, el cerebro completo. Lo constante es que diagnosticamos primero y acompañamos siempre."
- **Visual:** SVG inline del loop (Opción 2). 5 nodos en círculo, flechas grises clockwise, nodo Acompañamiento con borde + texto naranja, flecha de retorno naranja (Acompañamiento → Consultoría) con micro-etiqueta "reinicia". Paleta: `#181818` pills, borde `rgba(255,255,255,.16)`, accent `#FF6B00`, texto `#FAFAFA`. `role="img"` + `<title>`/`<desc>`.
- **Responsive (decidido):** el SVG circular escala por `viewBox` en desktop/tablet (≥641px). En `max-width:640px` se **oculta el SVG circular** (`display:none`) y se **muestra una lista vertical numerada** (1→5) que comparte el copy de los nodos, con un indicador de "reinicia el ciclo" al final que conecta 5→1. Son dos bloques hermanos conmutados por media query (no un solo SVG forzado). Validar legibilidad en preview a 360/768/1280.
- Copy por nodo (una línea):
  1. **Consultoría** — Mapeamos el proceso real y el dolor en pesos. Si no justifica el payback, te lo decimos antes de firmar.
  2. **Cerebro corporativo** — Cuando el caso lo pide: el conocimiento atrapado en WhatsApp, Excel y la cabeza de tu gente se vuelve memoria viva con agentes por rol.
  3. **Software e IA a la medida** — Implementación de IA, automatización de procesos o una plataforma a la medida. Construimos lo que el caso pida, en producción.
  4. **Capacitación** — Tu equipo aprende a operar la solución y a usar IA en su día a día. No queda dependiendo de nosotros.
  5. **Acompañamiento** — Nos quedamos con tu equipo después de cualquier entrega: ajustes, operación gobernada y ROI medido. Y reinicia el ciclo.
- Las líneas de copy de los nodos viven como tarjetas/lista debajo o al lado del diagrama (el diagrama lleva solo el nombre; el detalle va en texto, no dentro del SVG). **Nodo 3 en el diagrama: etiqueta "Software e IA a la medida".**

### 4.3 El método detrás del diagnóstico
- Kicker + h2: paper `Primero el contexto.` / accent `Después la herramienta.`
- Párrafo principio: "La arquitectura del proceso manda sobre la herramienta. Una herramienta excelente sobre un proceso mal diseñado entrega el mismo problema, más rápido. Por eso no automatizamos el desorden: primero lo rediseñamos."
- Secuencia numerada (usa `.steps`/`.step` o un patrón numerado; la numeración 1–5 está **justificada** porque el orden es el contenido — excepción explícita al anti-patrón "01/02/03 scaffold"):
  1. **Eliminar** — Quitamos los pasos que no deberían existir. La intervención de mayor impacto y menor costo.
  2. **Simplificar** — Reducimos lo que queda hasta que se explique a alguien nuevo en menos de diez minutos.
  3. **Optimizar** — Mejoramos la ejecución de los pasos que permanecen.
  4. **Automatizar** — Recién aquí entra la IA, sobre un proceso ya limpio. Antes, solo acelera el desorden.
  5. **Medir** — Cerramos el ciclo. Sobre un proceso simple, los números son señal, no ruido.

### 4.4 Por qué el acompañamiento es la clave
- Kicker + h2: paper `El acompañamiento no es un extra.` / accent `Es la clave.`
- Encuadre horizontal (no atado a un producto): el acompañamiento va después de **cualquier** entrega — una consultoría, una implementación de IA, un software a la medida, una capacitación o un cerebro corporativo completo. Es la propuesta de valor central de Syncon.
- 3 puntos (lista o cards):
  - **No desaparecemos después de la entrega.** Sea lo que sea que construimos o diagnosticamos: ajustes, operación gobernada y reporte de ROI continuo.
  - **El conocimiento queda en tu equipo, no en nosotros.** Después de la capacitación y durante el acompañamiento, tu gente queda capaz de operar sin depender de la firma.
  - **Gobernanza humana.** Cuando hay agentes de por medio, ellos proponen y tu gente ratifica; la decisión la toma un humano, siempre.
- Pills de contraste (qué NO somos): `el piloto que nunca llega a producción` · `consultoría de slides` · `pricing por horas`.
- (Opcional) CTA ghost → `/productos` "Ver qué construimos →" o → `/about` "La firma detrás del método →".

### 4.5 #contacto (conversión)
- Reutiliza **idéntico** el patrón `#contacto` del resto del sitio: columna izquierda (kicker `Empecemos por el contexto` / `Cuéntenos dónde duele` / `la operación.` + trust list) + formulario (Nombre, Empresa, Correo, `¿Dónde duele?` select) + botón "Diagnosticar mi operación" + micro-legal + **bloque agenda 30 min** (divisor "o" + `.calendly-link` + `.calendly-microcopy`). Incluye el parche `:root{--s5:20px}` y las reglas `.calendly-link/.form-divider/.calendly-microcopy` (ya canon en toda página de conversión).
- `data-pilar="como-trabajamos"` en el `.calendly-link`.

### 4.6 Nav + Footer
- Idénticos al resto del sitio. En el nav de ESTA página, "Cómo trabajamos" puede llevar estado activo.
- El form requiere el mismo JS de submit (loading state + `.form-success`) que el resto.

## 5 · Repunteo de enlaces `/#metodo` → `/como-trabajamos`

Cambiar el destino del enlace "Cómo trabajamos" (nav, mobile menu y footer) en los 6 archivos existentes:

| Archivo | Ocurrencias a repuntar |
|---|---|
| `index.html` | nav, mobile-menu, footer (eran `#metodo`) |
| `productos.html` | nav, mobile-menu, footer |
| `about.html` | nav, mobile-menu, footer |
| `productos/har.html` | nav, mobile-menu, footer |
| `productos/consultoria.html` | nav, mobile-menu, footer |
| `productos/capacitacion.html` | nav, mobile-menu, footer |

- En `index.html`, la sección `#metodo` se mantiene como **teaser** (resumen de 3 pasos ya existente) y se le añade un CTA ghost "Ver cómo trabajamos en detalle →" → `/como-trabajamos`. Los enlaces de nav/footer del home pasan de `#metodo` (ancla local) a `/como-trabajamos` (página) por consistencia con el resto del sitio.
- `about.html` conserva su propia sección `#metodo` interna sin cambios (fuera de alcance); solo se repunta su enlace de nav/footer "Cómo trabajamos".
- La nueva página se añade al nav/footer donde corresponda (ya aparece como "Cómo trabajamos").

## 6 · Restricciones del design system (no violar)

- Tokens CSS del canon (negro `#0A0A0A`, accent `#FF6B00` + hover/pressed, grises canon, `--r-full:99px`, motion quick/default).
- Cuerpo de texto mínimo 17px de #motores hacia abajo; `.lede` clamp(18,2.2vw,21).
- Anti-patrones prohibidos: sin `border-left>1px` como acento (usar borde completo + `border-top`), sin gradient text, sin glassmorphism decorativo, sin hero-metric template.
- WCAG 2.1 AA: skip link, `<nav>`/`<main>` landmarks, `aria-expanded` en dropdown/mobile, `aria-label` en menu-btn, SVG con `role="img"`+`title`/`desc`, contraste del naranja sobre negro validado.
- Reveal canon: IntersectionObserver `.reveal`/`.reveal.in-view`, sin CSS animation que rompa pestañas ocultas.

## 7 · Entregables / archivos tocados

1. **Nuevo:** `syncon-netlify-deploy/como-trabajamos.html` (autocontenido).
2. **Editados (repunteo de enlace + teaser CTA en home):** `index.html`, `productos.html`, `about.html`, `productos/har.html`, `productos/consultoria.html`, `productos/capacitacion.html`.
3. Sin cambios en `_redirects` ni en assets.

## 8 · Verificación (antes de cerrar)

- Preview local (`py -m http.server 5174`) en 360 / 768 / 1280 px: layout sin overflow, loop legible (circular en desktop, fallback en móvil).
- Los 6 enlaces "Cómo trabajamos" navegan a `/como-trabajamos`.
- Formulario: submit muestra loading + success; bloque agenda 30 min con `border-radius:99px` y `padding:16px 20px`.
- Sin hallazgos nuevos de impeccable atribuibles a esta página (los preexistentes del canon quedan como están).
- Contraste y landmarks WCAG.

## 9 · Fuera de alcance (tandas futuras)

- Recap/enlace de metodología en las 3 subpáginas de producto + verificación de sus CTAs.
- Página `/articulos`.
- Ratificación de canon de cualquier copy nuevo por Cris (CEO) si se considera T2/T3.
