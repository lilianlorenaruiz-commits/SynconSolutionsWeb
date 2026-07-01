# Design System: SYNCON Solutions Web

> Generado por taste-design · auditado contra `home-mockup.html` + `SYNCON_DESIGN_SYSTEM.md` v1.1 · 2026-06-24
> Fuente de verdad para prompts de Google Stitch y otros AI screen-generation agents.

---

## 1. Visual Theme & Atmosphere

Industrial-precision dark interface. La atmósfera es la de una firma de ingeniería bien iluminada en Bogotá: ningún elemento decorativo gratuito, cada decisión gana su lugar. El terminal del hero no es una ilustración — es el producto funcionando en vivo. "El producto es la demo."

El tono es seguro y directo: no seduce con gradientes ni deslumbra con animaciones. Habla como un ingeniero senior que ya resolvió el problema. B2B de alto valor para compradores industriales en LATAM.

- **Densidad:** 5 — Daily App Balanced. Secciones con ritmo propio, espacio para respirar entre bloques densos de información.
- **Varianza:** 7 — Offset Asymmetric. Todas las grillas usan ratios fraccionarios deliberados. Nunca columnas iguales para contenido.
- **Motion:** 5 — Fluid CSS. Reveal + typewriter terminal. Sin coreografía cinemática.

---

## 2. Color Palette & Roles

### Paleta principal

- **Off-Black Ink** (`#0A0A0A`) — Canvas primario. ~70% de todas las superficies. No es negro puro — tiene profundidad de carbón caliente.
- **Carbon Surface** (`#1A1A1A`) — Fondos de cards, sección de form, proof tiles. Capa de profundidad secundaria.
- **Steel Border** (`#444444`) — Divisores estructurales, bordes de cards, chrome de UI. Nunca decorativo.
- **Zinc Muted** (`#888888`) — Texto terciario: labels, timestamps, metadata. Desaparece cuando no es necesario.
- **Warm Gray** (`#CCCCCC`) — Texto de cuerpo secundario. Segunda línea del headline de hero. Jerarquía sin perder contraste.
- **Light Surface** (`#F2F2F2`) — Reservado para contextos light-mode (no activo en el tema oscuro actual).
- **Paper White** (`#FAFAFA`) — Texto primario sobre canvas oscuro. Texto del logo. No es blanco puro — ligeramente cálido.
- **Industrial Orange** (`#FF6B00`) — EL único accent. Slash+punto del logo, CTAs, kickers, bordes de tiles, marcadores FAQ, focus rings. **BRAND CANON — no modificar bajo ninguna circunstancia.**
- **Orange Hover** (`#FF8833`) — Estado hover sobre accent. Shift hacia más claro.
- **Orange Pressed** (`#CC5500`) — Estado active/pressed. Burn más oscuro.

### Colores semánticos de agentes *(solo para terminal y protocolo HAR)*

- **CEO Cyan** (`#00E5FF`) — Agente CEO en terminal. Informacional exclusivamente.
- **COO Amber** (`#FFB300`) — Agente COO. Informacional exclusivamente.
- **CTO Green** (`#00E676`) — Agente CTO. Informacional exclusivamente.

> **Regla de alcance:** Los colores de agente están estrictamente circunscritos al widget de terminal y displays del protocolo HAR. Nunca como accents secundarios, nunca en layout chrome, nunca como color decorativo.

### Nota de override de brand canon

El accent `#FF6B00` tiene saturación del 100%, lo cual excede el límite genérico de taste-design (80%). Esto es un **override deliberado de brand canon** — viene de `themes/syncon.css` (producción) y es intocable. No suavizar el naranja. No reducir saturación. Es distintivo por diseño.

---

## 3. Typography Rules

### Fuentes

- **Display/Headlines:** Geist (variable weight 400–800). Track muy cerrado. Jerarquía a través de peso y cambio de color — no solo escala masiva.
- **Body:** Geist 400. Ritmo relajado. Máximo 68 caracteres por línea.
- **Mono:** Geist Mono — para kickers, etiquetas de cards/steps, terminal, proof tile numbers, labels de form, metadata, footer labels. Cuando un número comunica credibilidad, usa Geist Mono.

### Escala tipográfica

| Elemento | Fuente | Peso | Tamaño | Tracking | Color |
|---|---|---|---|---|---|
| H1 hero | Geist | 800 | `clamp(40px, 6.4vw, 82px)` | -0.045em | Paper White |
| H1 línea 2 | Geist | 800 | (mismo) | -0.045em | Warm Gray |
| H2 secciones | Geist | 800 | `clamp(28px, 3.6vw, 40px)` | -0.03em | Paper White |
| Lede/subtítulo | Geist | 400 | `clamp(18px, 2.2vw, 21px)` | base | Warm Gray |
| Cuerpo | Geist | 400 | 17px / lh 1.5 | -0.01em | Paper White |
| Kicker | Geist Mono | 400 | 12px | +0.14em | Industrial Orange |
| Tags cards/steps | Geist Mono | 400 | 11px | +0.10em | Industrial Orange |
| Nav links | Geist | 400 | 15px | base | Warm Gray |
| Números proof | Geist Mono | 700 | `clamp(28px, 3.4vw, 40px)` | base | Paper White / Orange |
| Metadata/footer | Geist Mono | 400 | 11–13px | +0.08–0.10em | Zinc Muted |
| Terminal body | Geist Mono | 400–700 | 14px / lh 1.7 | base | según rol |

### Tipografía prohibida

- ❌ Inter como fuente primaria (aparece en posición 4 del font-stack como fallback técnico únicamente — nunca debe renderizar en producción)
- ❌ Serifs genéricos (Times New Roman, Georgia, Garamond, Palatino)
- ❌ Fuentes de sistema para headings

---

## 4. Component Stylings

### Logo wordmark
`/syncon.solutions` en Geist Mono 700, 19px. Slash (`/`) y punto (`.`) en Industrial Orange (`#FF6B00`). Texto negro o blanco sobre fondo transparente. Este ES el logo — no es un elemento decorativo. **LOCKED: cambio requiere 3-de-3 aprobación de fundadores (Cris + Lorena + Pipe).**

### Botones

**Primary:** Fill Industrial Orange (`#FF6B00`), texto Off-Black (`#0A0A0A`). Border-radius 2px (sharp, industrial — no pill, no rounded). Min-height 48px. Hover: `#FF8833`. Active: `translateY(1px)` + `#CC5500` (empuje tácito hacia abajo). Sin outer glow jamás.

**Ghost:** Fondo transparente, texto Paper White, borde Steel Border (`#444444`). Hover: borde + texto → Industrial Orange. Mismo radius sharp, mismo active tácito.

**Excepción hero:** Los botones de `.hero-actions` usan `border-radius:99px` (pill) como referencia visual al lenguaje pill del kicker. `font-size:14px`, `padding:0 18px`, `white-space:nowrap`, gap entre botones `12px`. El primary hero sí tiene glow en hover: `box-shadow:0 0 28px rgba(255,107,0,.55),0 0 60px rgba(255,107,0,.22)`.

**Regla de CTAs:** Máximo 1 CTA primary por sección. El botón ghost funciona como CTA secundario si se necesita, pero nunca debe competir visualmente con el primary.

### Hero section — patrones aprobados

**H1 glow (título naranja):** `text-shadow` en `.hero h1 .line1` — emana directamente de las letras, no de un pseudo-elemento de fondo. Capas: `0 0 60px rgba(255,107,0,.40)`, `0 0 120px rgba(255,107,0,.15)`, `0 0 260px rgba(255,107,0,.06)`. El `::after` de `.hero` existe solo como ambient mínimo (`rgba(255,107,0,.04)`). `.hero-grid` tiene `position:relative;z-index:1` para quedar sobre el ambient.

**Kicker pill:** `border-radius:99px`, borde `rgba(255,107,0,.28)`, fondo `rgba(255,107,0,.04)`, texto `var(--paper)` (blanco), dot naranja con animación `pulse-dot`. Geist Mono 12px uppercase.

**Frame (columna derecha):** Estructura `.frame-col` (flex-direction:column, gap:var(--s3)) que contiene en orden:
1. `.frame-label` — badge "LIVE COMPANY BRAIN". Geist Mono 11px, uppercase, letter-spacing 0.10em, `color:var(--muted)`. Rec-dot naranja 6px pulsante. Flujo normal (NO position:absolute — no puede ir encima del video).
2. `.frame-wrapper` — contenedor del video. Borde 1px `rgba(255,107,0,.28)`, `border-radius:8px`, triple box-shadow de glow naranja (40px/100px/260px en opacidades .28/.16/.09). Corner brackets 22×22px en accent. Video `width:100%;display:block`.

### Terminal widget (centerpiece del hero)

Fondo Off-Black (`#0A0A0A`) con borde Steel Border (1px), border-radius 8px. Barra superior: 3 puntos círculo (Steel, decorativos), label en Geist Mono. Cuerpo: Geist Mono 14px, lh 1.7, salida coloreada por rol de agente. Animación typewriter a 18ms/carácter, pausa de 360ms entre líneas. Cursor bloque parpadeante (9px) en Industrial Orange. **El terminal solo muestra datos operacionales reales — nunca datos inventados.**

### Cards (bento / motores)

Fondo Carbon Surface (`#1A1A1A`), borde 1px Steel Border, border-radius 8px. Hover: borde → Industrial Orange (flash industrial de reconocimiento). Sin box-shadow. Usadas exclusivamente para definición de producto/servicio. Nunca para testimonios, feature lists genéricas o contenido decorativo.

### Proof tiles (receipts / sección de credibilidad)

Fondo Carbon Surface + borde izquierdo 3px Industrial Orange. Border-radius asimétrico: 0 8px 8px 0 (industrial, no simétrico). Números en Geist Mono 700 via clamp. Números destacados en Industrial Orange; números neutros en Paper White. Fecha/fuente en Zinc Muted. **Regla absoluta: cada número tiene que ser real, datado, atribuido. Nunca un número inventado.**

### Steps (metodología)

3 columnas iguales en desktop (borde-top en naranja, no cards). Border-top 2px Industrial Orange como ancla visual. Nombre de fase en Geist Mono accent 12px. Título en Geist 700 19px. Descripción en Warm Gray. Estos no son cards — usan border-top, no superficie de card.

### Pills (enemigos / posicionamiento)

Borde Industrial Orange 1px + texto naranja sobre transparente/oscuro. Shape pill (99px radius). Geist Mono 13px. Solo para la lista de desplazamiento competitivo — nunca como etiquetas genéricas de categoría.

### Anti-statement block

Borde izquierdo 3px Industrial Orange + fondo Carbon Surface. Texto de tamaño statement (`clamp(18px, 2.2vw, 22px)`), Geist 600. Máximo 46 caracteres de ancho. Se usa una vez por página, como el claim de posicionamiento más filoso.

### Inputs / Formulario

Label encima (Geist Mono 12px, uppercase, Zinc Muted). Input sobre fondo Off-Black (hundido en la superficie). Borde 1px Steel Border. Min-height 48px. Focus: 2px outline Industrial Orange + borde naranja. Sin labels flotantes. Estado de error: **pendiente de definición** (`[PENDIENTE]`).

### FAQ (details/summary nativo)

Toggle `+`/`–` en Geist Mono Industrial Orange. Border-bottom entre ítems en Carbon Surface. Sin marcadores custom. El switch `+` → `–` no tiene transición de transform — transición implícita del browser.

---

## 5. Layout Principles

**Container:** max-width 1240px, centrado, 24px de padding horizontal.

**Grillas — ratios asimétricos deliberados:**

| Sección | Columnas | Razón del ratio |
|---|---|---|
| Hero | `1.05fr / 0.95fr` | Copy ligeramente dominante sobre terminal |
| Problema / Producto | `0.85fr / 1.15fr` | Quote corta a la izquierda, cuerpo a la derecha |
| Bento (motores) | `1.4fr / 1fr` | Motor A (comercial) ligeramente dominante |
| Cierre / form | `1fr / 1fr` | Ambos lados con igual peso de conversión |

**Padding de sección:** `clamp(64px, 9vw, 120px)` vertical. Separación entre secciones: `border-bottom: 1px solid #1A1A1A`.

**Escala de espaciado:** 4 / 8 / 12 / 16 / 24 / 32 / 48 / 64px (base 8px con micro de 4px).

**Border radius:** 2px (sharp, industrial — botones, inputs) o 8px (estructural — cards, console). Nunca radios grandes en elementos primarios de UI.

Sin `flexbox + calc()` de porcentajes. Sin stacking de elementos absolute. Cada elemento en su propia zona espacial limpia.

---

## 6. Motion & Interaction

Filosofía de motion: restringida y propositiva. Cada animación comunica estado, no decoración.

**Reveal al montar (`.reveal`):** `opacity: 0 + translateY(20px) → 1 + translateY(0)`. 600ms. `cubic-bezier(0.2, 0, 0, 1)`. Delays escalonados 50–350ms. Headlines aparecen antes que el texto de soporte.

**Typewriter del terminal:** Caracteres a 18ms/char. 360ms de pausa entre líneas. 700ms de delay inicial (respira antes de empezar).

**Cursor blinking:** Bloque 9px en Industrial Orange. `steps(2)` 1s infinite. Permanece visible después de que terminan las líneas.

**Header al hacer scroll:** `backdrop-filter: blur(8px)` siempre activo. Con scroll > 24px: `background` sube a 92% opacidad + aparece borde Steel inferior. Transición 200ms ease-out.

**Botones:** Hover = shift de color (150ms). Active = `translateY(1px)` (push táctico, 150ms). Sin spring physics en implementación CSS actual.

**Cards:** Hover = border → Industrial Orange (150ms). Sin scale transform. Sin shadow.

**`prefers-reduced-motion`:** Disable total — `animation: none!important`, `transition: none!important`, `scroll-behavior: auto!important`. Cursor escondido. Terminal muestra todas las líneas de inmediato (sin typewriter).

**Aceleración por hardware:** Todas las animaciones vía `opacity` y `transform` únicamente. Sin animar `top`, `left`, `width`, `height`.

---

## 7. Responsive Rules

**Breakpoint principal:** 900px (justificado por el contenido — el layout de 2 columnas funciona hasta 900px; debajo de eso, 1 columna es la única opción legible).

**Colapso en móvil (< 900px):**
- Todas las grillas multi-columna → `grid-template-columns: 1fr`
- Nav links y botón de nav → `display: none`
- Menu button → visible, mínimo 44×44px
- Terminal console → `order: -1` (aparece antes del copy en móvil)

**Overflow horizontal:** Nunca. Si aparece scroll horizontal en móvil = fallo crítico.

**Tipografía:** Headlines via `clamp()`. Texto de cuerpo mínimo 17px (nunca menor a 14px). Sin tamaños fijos en headings.

**Touch targets:** Todos los elementos interactivos mínimo 44×44px (botones, nav menu, FAQ summaries, inputs 48px).

---

## 8. Anti-Patterns (Banned)

### AI tells generales

- ❌ Emojis en cualquier texto, heading o elemento de UI
- ❌ Inter como fuente primaria
- ❌ Negro puro (`#000000`) — siempre Off-Black (`#0A0A0A`) o Carbon Surface (`#1A1A1A`)
- ❌ Neon outer glow shadows o efectos bloom
- ❌ Gradient text decorativo (`background-clip: text`) en headings
- ❌ Custom mouse cursors
- ❌ Scroll arrows, "Scroll to explore", chevrons bounce, indicadores de scroll
- ❌ Elementos superpuestos — toda zona espacial debe ser limpia y no superpuesta
- ❌ Grid de 3 cards iguales horizontales (usar grillas asimétricas, steps con border-top, o tiles)
- ❌ Clichés de copy IA: "Eleva", "Seamless", "Desata", "Next-Gen", "Soluciones innovadoras", "Potencia tu negocio"
- ❌ Métricas fabricadas o datos inventados — todo número debe ser real, datado y atribuido. Si no existe el dato: `[pendiente]`
- ❌ Secciones de "KEY STATISTICS" o "SYSTEM METRICS" con datos inventados
- ❌ Formato `LABEL // AÑO` ("SISTEMA // 2024")
- ❌ Nombres placeholder genéricos ("Empresa ABC", "Juan Pérez", "Acme Corp")
- ❌ Links rotos de Unsplash — usar `picsum.photos` o SVG avatars
- ❌ Heroes centrados — siempre split asimétrico

### Prohibiciones específicas de SYNCON

- ❌ Accents secundarios en layout chrome — los colores de agente (cyan/amber/green) son solo para el terminal
- ❌ Lenguaje de "piloto" — todo va a producción
- ❌ "Transformación digital" — término deprecado en brand canon desde 2025
- ❌ "Chatbot con tu logo" — Company Brain no es un chatbot
- ❌ Pricing por horas
- ❌ Modificar el accent orange a "algo más suave" — `#FF6B00` es brand canon, 100% saturación es intencional
- ❌ Cambiar el logo wordmark (`/syncon.solutions`) sin aprobación 3-de-3 de fundadores

---

## Flags detectados en auditoría (2026-06-24)

Estos no son errores críticos pero deben resolverse antes de producción:

1. **Inter en font-stack:** `var(--sans)` incluye `'Inter'` como posición 4 de fallback. Mientras Geist cargue desde Google Fonts el riesgo es mínimo, pero en producción debería reemplazarse por `ui-sans-serif` para eliminar la dependencia de Inter como fallback.

2. **Saturación del accent:** `#FF6B00` tiene 100% de saturación — excede el límite genérico de taste-design (80%). Este es un **override de brand canon justificado** y documentado. Cualquier herramienta de design system que marque esto como "error" debe ignorarse.

3. **Inter en font-stack fallback de Inter:** Ver punto 1.

4. **Cascada de reveal en listas:** Los steps, cards y pills no tienen stagger individual — aparecen todos a la vez. Para la versión de producción se recomienda añadir cascade delays en estos grupos.

5. **Estado de error no definido:** Los inputs del form no tienen estilos de validación de error definidos. `[PENDIENTE]` antes de producción.
