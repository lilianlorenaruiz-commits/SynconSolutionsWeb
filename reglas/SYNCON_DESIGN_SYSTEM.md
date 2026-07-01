# SYNCON · Design System canónico de la web

> **Estado:** v1.3 — home mockup CERRADO (2026-06-25). Listo para producción de páginas nuevas.
> **v1.1 (2026-06-24):** resueltos sede, AI Adoption, carriles de agente, par tipográfico. Tesis de producto `[PROPUESTO]` (pendiente co-firma de Cris).
> **v1.2 (2026-06-25):** home completado (#contacto, select CSS states). Ver §10 para decisiones de implementación web.
> **v1.3 (2026-06-25):** audit post-impeccable aplicado. Ver §11 para anti-patrones de implementación, patrones aprobados y estado de archivos.
> **Naturaleza:** este documento es el **canon de diseño de la web** de SYNCON Solutions S.A.S. Toda decisión visual, de voz o de conversión de la web futura se valida contra él.
> **Regla de construcción:** cada ítem trae **Decisión · Fuente · Razón**. Donde una fuente no existe o dos fuentes chocan sin resolución trazable, el campo dice `[PENDIENTE]`. Cero inferencias, cero defaults, cero estructura impuesta.

---

## 0. Meta — cómo leer y gobernar este documento

### 0.1 Jerarquía de fuentes (canon)

**Decisión.** Orden de autoridad cuando dos insumos chocan: (1) `themes/syncon.css` + `tokens/*.json` DTCG (producción) → (2) `brand-wiki-syncon-v1.2-interno-cerrado.md` (CERRADO, reconciliado) → (3) `voice-brand-syncon-operativo-v0.2-reconciliado.md` (v0.2, más reciente que el manual) → (4) `manual-de-marca-syncon-v2.1.0.html` (DRAFT) y decks Marp `01–06` → (5) `Análisis UX_UI Ecosistema IA.md` y `Optimización de Conversión en IA.md` (investigación: apropiable solo donde no choca con 1–4).

**Fuente.** `04-visual-identity.html` declara *"Fuentes: tokens/*.json · themes/syncon.css"*; `brand-wiki-syncon-v1.2` §0 declara *"En cualquier conflicto, manda la Constitución v2.0.0"* y se marca CERRADO; `voice-brand v0.2` está fechado 2026-06-23 (posterior al manual, 2026-06-11).

**Razón.** Producción > documento derivado; documento cerrado y reciente > draft. Resuelve conflictos sin opinión.

### 0.2 Convención de etiquetas (heredada del canon)

- **[CANON]** verificado verbatim contra producción o Company Brain.
- **[CONFIRMED]** decisión de fundadores ya tomada, consistente con el canon.
- **[PROPUESTO]** propuesta no ratificada; no es verdad corporativa todavía.
- **[PENDIENTE]** sin fuente trazable o conflicto sin resolver → requiere decisión humana.

**Fuente.** `brand-wiki-syncon-v1.2` §"Convención de etiquetas".
**Razón.** Mantener la honestidad de canon: nada se presenta como verdad si no lo es.

### 0.3 Governance del Design System

| Cambio | Quórum | Semver |
|---|---|---|
| Constitución, categoría, enemigo, **logo**, posicionamiento mayor, pricing | **3-de-3** (Cris, Lorena, Pipe) | MAJOR |
| Claims de marketing públicos (web/LinkedIn) | **2-of-2** (Cris CEO + Lorena COO) + receipt dateado | — |
| Vocabulario, persona, canal nuevo | Brand Owner (Lorena) | MINOR |
| Typos, ejemplos, claridad | Cualquier owner | PATCH |

**Owners:** Marca/voz/contenido → Lorena (COO, Brand Owner) · Tokens/repo/claims técnicos → Cris (CEO) · Infra técnica de marca → Pipe (CTO, consultado) · Validación de outputs de agentes → SynCon hub (Brand Guardian).

**Fuente.** `brand-wiki-syncon-v1.2` §12; `manual-de-marca-syncon-v2.1.0` §19; reconciliación de quórum en `voice-brand v0.2` §15.
**Razón.** El documento es canon vivo: necesita un proceso de cambio explícito (pilar de brand governance: estándares + procesos + auditoría).

---

## 1. Fundamento de marca (lo que el diseño debe servir)

> El diseño no decora: expresa una categoría y un método. Estas leyes condicionan toda decisión visual y de voz.

**1.1 Identidad.**
**Decisión.** SYNCON Solutions S.A.S. — **firma de ingeniería contextual** ("contextual engineering for intelligent LATAM operations"). El nombre es el método: **SYN** (síntesis) + **CON** (contexto) + **Solutions** (a producción).
**Fuente.** `brand-wiki-syncon-v1.2` §1; `manual-de-marca-syncon-v2.1.0` §1.
**Razón.** La web debe leerse como firma de ingeniería, no como agencia de IA ni SaaS.

**1.2 Categoría propia.**
**Decisión.** **Company Brains para LATAM** = memoria corporativa gobernada + agentes de rol bajo protocolo **HAR** (Hierarchy Agent Reporting), con human-in-the-loop. Escribir siempre *Company Brain + HAR*.
**Fuente.** `brand-wiki-syncon-v1.2` §3–4; `voice-brand v0.2` §4.1.
**Razón.** Es el white space que la web instala; gobierna la sección de producto.

**1.3 Tagline master (hero de la firma).**
**Decisión.** **"Ingeniería contextual. Operaciones inteligentes."**
**Fuente.** `brand-wiki-syncon-v1.2` §3; `manual-de-marca-syncon-v2.1.0` §2/§7.
**Razón.** Es el hero de FIRMA. El hero de PRODUCTO usa la tesis de §3.2 de este documento.

**1.4 Sistema de taglines.**
**Decisión.** Master: "Ingeniería contextual. Operaciones inteligentes." · Categoría: "Company Brains para LATAM." · Producto: "Tu empresa deja de olvidar." · Comercial: "No te vendemos IA. Te vendemos tu retorno." · Filosófico: "Nativos en IA. Veteranos en industria." · Motor consultoría: "Entendemos tu operación. Construimos la solución."
**Fuente.** `manual-de-marca-syncon-v2.1.0` §7; `voice-brand v0.2` §4.5.
**Razón.** Cada superficie usa el tagline correcto a su intención.

**1.5 ICP (a quién le habla la web).**
**Decisión.** Mid-market industrial y de servicios LATAM, **USD 5–25M** de facturación; dolor operacional **≥ 100M COP/año**; conocimiento fragmentado (cabezas, correos, WhatsApp, Excel).
**Fuente.** `manual-de-marca-syncon-v2.1.0` §2; `brand-wiki-syncon-v1.2` §3 (bandas de revenue).
**Razón.** El hero y los textos deben calificar y **repeler wrong-fit** (Quality Gate §8.4).

**1.6 Arquetipo.**
**Decisión.** **Outlaw** (primario) + **Sage** (secundario) — tensión operada como *arrogante-con-propósito*.
**Fuente.** `manual-de-marca-syncon-v2.1.0` §2 (tabla Posicionamiento).
**Razón.** Define el carácter visual (industrial, directo, con filo) y verbal (§3).

**1.7 Modelo de negocio (estructura la oferta en la web).**
**Decisión.** **2 motores activos:** (Motor 2) Consultoría contextual + software a la medida; (Motor 3) Company Brain + HAR. La ingeniería contextual/diagnóstico es la entrada a ambos. **No es SaaS self-service** → firma de implementación + retainer.
**Fuente.** `voice-brand v0.2` §10-bis (decisión Lorena+Cris 2026-06-23); `brand-wiki-syncon-v1.2` §5.
**Razón.** La sección de servicios es un bento de 2 motores, no un catálogo. (El motor de plataformas verticales ex-INDUTECH está dormido, NDA 2026-06-02 → no aparece en web.)

**1.8 Sede y alcance.**
**Decisión.** SYNCON es una **firma latinoamericana** de ingeniería contextual; **sede principal: Bogotá, Colombia**. Yumbo, Mamonal, Sabana y Barranquilla son **geografías industriales** de referencia (fotografía, casos), no sedes.
**Fuente.** Ratificación de Lorena (COO, Brand Owner) 2026-06-24, resolviendo el `[VERIFICAR]` de `voice-brand v0.2` §1/§18 (que evitaba afirmar ciudad sin confirmar). Geografías industriales de `manual` §12 / `04-visual-identity` (Photography direction).
**Razón.** Cierra la ciudad del footer/about y alinea el alcance LATAM ("Company Brains para LATAM") con un HQ concreto, sin confundir sede con las plantas de los casos.

---

## 2. Leyes constitucionales (gobiernan todo el diseño)

> SYNCON es **constitucional, no rule-based**: 7 principios priorizados. El principio N supera al N+1 en conflicto. Toda decisión de diseño/copy se valida contra ellos por prioridad.

**Decisión.** Orden vinculante:
1. **ROI antes que features** — todo artefacto externo responde "¿cuánto $ se ahorra o se gana?".
2. **Peso técnico + de planta** — cada claim con número + vocabulario industrial (turno, paro, MTBF, OEE).
3. **Nativos en IA, no traductores** — español-colombiano primero; tech terms sin conjugar.
4. **Nombramos al enemigo** — al menos un enemigo de categoría por activo; nunca un competidor por nombre.
5. **Publicamos los recibos** — números reales, públicos, dateados; página `/receipts`.
6. **Llaves viejas no abren puertas nuevas** — nada copiable de plantillas 2010s; sin "me complace", sin logo walls, sin "trusted by" vacío, sin stock photos.
7. **La ingeniería contextual manda. Nunca vendemos catálogo** — primero contexto/ROI, luego solución.

**Fuente.** `brand-wiki-syncon-v1.2` §2 (Constitución v2.0.0, ORDENADA).
**Razón.** Son las leyes que el sistema visual y de voz materializan; cada sección posterior cita el principio que sirve.

> **Conflicto resuelto.** `manual-de-marca-syncon-v2.1.0` §3 lista el Principio 7 como *"El agente es el producto"*. El Brand Wiki v1.2 (CERRADO, posterior) lo reemplazó por *"La ingeniería contextual manda"* y documenta el cambio en su log de auditoría §13.A #1. **Canon vigente = Wiki v1.2.** (El espíritu "el agente es producto/demo" sobrevive en el Principio de dogfooding y en §5 de este documento.)

**Quality Gate (test booleano, publicar con ≥ 4/5).**
**Decisión.** (1) ¿Afirma algo específico (número, enemigo, claim audaz)? (2) ¿Un competidor puede copiar-pegar esto sin cambiar una palabra? → reescribir. (3) ¿Repele al menos un buyer wrong-fit? (4) ¿Hay un receipt a un clic? (5) ¿Suena a SYNCON o a cualquier consultoría de IA?
**Fuente.** `brand-wiki-syncon-v1.2` §11; `manual` §18; `voice-brand v0.2` §16.
**Razón.** Filtro objetivo para toda pieza de la web antes de publicar.

---

## 3. Identidad verbal (voz de la web)

> La **voz no cambia**; el **tono cambia por canal**. (Pilar de brand-voice + governance.)

### 3.1 Voz fija — 7 traits

**Decisión.** Disruptivo (incomoda con tesis, no con pose) · Técnico (números, no adjetivos) · Arrogante-con-propósito (solo con receipt) · Nativo en IA (idioma materno) · ROI-first (cada frase termina en $) · Directo (verbos activos, sin hedges) · Humano-industrial (español colombiano con peso de planta). Posición NN/g: serio-con-humor-seco · casual-profesional (usted) · respetuoso-con-filo · matter-of-fact.
**Fuente.** `manual-de-marca-syncon-v2.1.0` §4; `brand-wiki-syncon-v1.2` §9; `voice-brand v0.2` §1.
**Razón.** Regla madre de copy: **claim + receipt + fecha**. Sin receipt, baja el tono o márcalo hipótesis.

### 3.2 Tono por canal — web (matriz cuantificada)

| Superficie | Disruptivo | Técnico | Arrogante | Directo | Humano-ind. |
|---|---|---|---|---|---|
| **Web hero** | MAXED | MEDIUM | MEDIUM | MAXED | MEDIUM |
| **Web producto** | — | HIGH | — | — (ROI HIGH) | MEDIUM |
| **Producto / UI** | LOW | MEDIUM | NONE | MAXED | MEDIUM |
| **Soporte / errores** | LOW | MEDIUM | NONE | HIGH | MAXED |

**Tesis de hero de PRODUCTO** `[PROPUESTO — candidata vigente; pendiente co-firma de Cris (CEO) para completar 2-of-2]`: *"Tu empresa ya tiene un cerebro. Está repartido en cabezas que un día se van. Nosotros lo construimos como software."*
**Fuente.** `manual-de-marca-syncon-v2.1.0` §5 (matriz); `voice-brand v0.2` §3 y §8.1; estatus [PROPUESTO] en `brand-wiki-syncon-v1.2` §1 y `voice-brand v0.2` §4.5.
**Razón.** El hero de firma usa el tagline master (CANON); el de producto usa la tesis (cuando se ratifique).

### 3.3 Vocabulario

**Decisión.**
- **USAR:** Company Brain · Cerebro Corporativo · memoria corporativa gobernada · HAR (Hierarchy Agent Reporting, acuñado por SYNCON) · agente de rol · human-in-the-loop · ingeniería contextual · ROI · payback · turno · paro de planta · MTBF · OEE · orden de trabajo · dogfooding · deploy.
- **EVITAR → usar:** "transformación digital" → "operación inteligente"; "chatbot/asistente virtual" → "agente de rol"; "agencia de IA" → "firma de ingeniería contextual"; "stakeholders" → "involucrados"; "engagement/leverage", "revolucionario/game-changer/state-of-the-art/best-in-class" → un número; "me complace compartir" → ve al punto.
- **NUNCA en público:** vulgaridades; mexicanismos/argentinismos; "red de agentes" / "A2A autónomo" (mesh DISABLED); Title Case inglés en hero español.
**Fuente.** `manual-de-marca-syncon-v2.1.0` §6; `voice-brand v0.2` §4–5.
**Razón.** El vocabulario es activo distintivo (shibboleth industrial) y filtro anti-genérico (Principio 6).

### 3.4 Gramática y mecánica

**Decisión.** Tesis en línea 1 · número antes que adjetivo · frases ≤ 25 palabras (mejor ≤ 20) · verbos activos · cero exclamaciones B2B · **usted** en externo formal (tú solo peer-tech/interno; vos/vosotros nunca) · **headings en sentence case, nunca Title Case** · cifras siempre que el dato venda · moneda COP local / USD regional · **formato entregable HTML > PDF**.
**Fuente.** `manual-de-marca-syncon-v2.1.0` §8; `voice-brand v0.2` §2.
**Razón.** Da ritmo "piso de planta" y consistencia entre humanos y agentes.

### 3.5 Microcopy de la web

| Contexto | Copy canónico |
|---|---|
| CTA principal | **"Diagnosticar mi operación"** |
| CTA secundario | **"Ver cómo opera nuestro Company Brain"** |
| Formulario | "Cuéntenos dónde duele la operación." |
| Error | "Algo se rompió de nuestro lado. Ya estamos revisando." |
| Éxito | "Recibido. Ahora vamos a mirar el contexto." |
| Pricing | "Rangos de planeación. El precio final sale del diagnóstico contextual." |

**Fuente.** `voice-brand v0.2` §10 (microcopy web), corroborado por `manual-de-marca-syncon-v2.1.0` §16 (Error UI con nombre humano).
**Razón.** Cada superficie (incluido el error y la factura) lleva el rigor del hero (táctica "every surface as essay").

---

## 4. Identidad visual (tokens de producción)

> **Filosofía:** negro dominante (~70% del canvas), un solo accent (industrial orange), grayscale como workhorse de jerarquía. Estética industrial honesta: **cero gradientes, cero drop-shadows en identidad, cero photo-tricks**. "Visual como código: parametrizado, versionado, tokenizado."
> **Fuente:** `04-visual-identity.html` (filosofía + tokens); `manual-de-marca-syncon-v2.1.0` §10; `brand-wiki-syncon-v1.2` §10.1.

### 4.1 Color — tokens primitivos (verbatim de `themes/syncon.css`)

| Token | Hex | Rol semántico |
|---|---|---|
| `--syncon-black` | `#0A0A0A` | `--bg-primary` (fondo dominante, ~70%) |
| `--syncon-gray-900` | `#1A1A1A` | `--bg-secondary` (superficies elevadas, cards) |
| `--syncon-gray-700` | `#444444` | `--border-subtle` (bordes, divisores) |
| `--syncon-gray-500` | `#888888` | `--fg-muted` (texto terciario) |
| `--syncon-gray-300` | `#CCCCCC` | `--fg-secondary` (texto secundario sobre oscuro) |
| `--syncon-gray-100` | `#F2F2F2` | superficie sutil sobre claro |
| `--syncon-white` | `#FAFAFA` | `--fg-primary` (texto) / lienzo del logo |
| `--syncon-orange-500` | `#FF6B00` | `--accent` (único: slash+dot, CTAs, focus, números) |
| `--syncon-orange-400` | `#FF8833` | `--accent-hover` |
| `--syncon-orange-600` | `#CC5500` | accent pressed |

**Fuente.** Bloque `:root` de producción inyectado en `04-visual-identity.html` (`@import '../themes/syncon.css'`), confirmado verbatim por `brand-wiki-syncon-v1.2` §10.3.
**Razón.** Tokens únicos y versionados; el naranja es ownable en IA-LATAM (heritage Caterpillar/Hilti/Husqvarna).

> **Conflicto resuelto.** `manual-de-marca-syncon-v2.1.0` muestra grises `#8A8A8A / #3A3A3A` en su propio `:root`. Esos eran el **styling del documento-manual**, no los tokens de producto. `syncon.css` (producción) usa `#888888 / #444444`, coincidiendo con el Wiki v1.2. **Canon = valores de producción de esta tabla.**

> **Prohibido.** Magenta `#FF0055` (deprecado 2026-04-16, "leía consumer/fashion") · paletas suaves · degradados genéricos · look "AI purple" · beige premium · fondos SaaS clonables · gradientes/drop-shadows en el wordmark · saturación de foto.
> **Fuente.** `brand-wiki-syncon-v1.2` §10.3; `manual` §9 Don'ts; `04-visual-identity.html` slide Philosophy. Refuerzo de lente `taste-design`/`frontend-design`: el "AI purple/neon" está baneado.

**Colores reservados por carril de agente (señales funcionales, NO colores de marca generales):**
**Decisión.** Triada de identificación de agentes en UI oscura: **CEO cyan `#00E5FF`** · **COO amber `#FFB300`** · **CTO green `#00E676`**. Tokens: `--agent-ceo` / `--agent-coo` / `--agent-cto`. Uso exclusivo para distinguir agentes/carriles; **nunca como accent de marca ni como fill de CTA** (el CTA es siempre orange `#FF6B00`).
**Fuente.** cyan `#00E5FF` es CANON (`manual` §10 `:root --cyan`; `brand-wiki` §10.3). amber/green **derivados por diseño** (Lorena delegó la reconciliación 2026-06-24): el canon fijaba los nombres (amber=COO, green=CTO) pero no el hex. Estado: `[PROPUESTO]` para co-firma de Cris (owner de tokens).
**Razón (taste).** (1) **amber `#FFB300`** se empuja al dorado (hue ~42°) para **no confundirse con el orange de marca `#FF6B00`** (hue ~25°); por eso queda restringido a identificar agente, jamás a CTA. (2) **green `#00E676`** rima con el cyan en la familia electric `#00E…`, formando una triada de señal coherente para un "centro de control". (3) Las tres pasan AA/AAA sobre `#0A0A0A` (≈10–13:1), consistentes con la regla "color vivo solo sobre fondo oscuro" (§4.2).

### 4.2 Reglas de contraste / accesibilidad (objetivo WCAG AA en todos los pares)

| Par | Uso | Regla |
|---|---|---|
| Paper `#FAFAFA` sobre Ink `#0A0A0A` | Texto body | ✅ AAA — par principal |
| Orange `#FF6B00` sobre Ink | Accents, links, números | ✅ AA (~6.9:1) — apto para texto |
| Orange sobre Paper `#FAFAFA` | Solo accents grandes / iconos / slash+dot | ⚠️ ~2.8:1 — **NUNCA texto de cuerpo** (falla AA) |
| Información solo-por-color | — | ❌ Prohibido: siempre acompañar con texto/ícono |

**Otros:** focus ring **2px orange** en interactivos · min tap target **44×44px** · body mínimo **16px** · `prefers-reduced-motion` respetado (solo fades, sin slides).
**Fuente.** `04-visual-identity.html` slide Accessibility; `manual-de-marca-syncon-v2.1.0` §10/§12; `brand-wiki-syncon-v1.2` §10.3.
**Razón.** El naranja es seductor pero falla como texto sobre blanco; la regla evita el error de accesibilidad más probable.

### 4.3 Tipografía

**Decisión.**
- **Display + body:** Geist Sans (400–800). Sentence case en headings; tracking −0.03 a −0.06em en hero.
- **Mono + tech + logo:** Geist Mono (400/500/700) — wordmark, código, números-receipt, kickers, etiquetas técnicas, proof tiles, prompts.
- **Fallback:** `-apple-system, BlinkMacSystemFont, 'Inter', sans-serif` / `'JetBrains Mono', ui-monospace, Consolas, monospace`.
- **Escala:** modular **ratio 1.25, base 16px**. Hero **72–96px**; h2 ~39px; h3 ~25px; body 16–20px **line-height 1.5**; kicker 12px mono uppercase letter-spacing .14em (orange).
**Fuente.** `manual-de-marca-syncon-v2.1.0` §11; `04-visual-identity.html` slide Typography; `brand-wiki-syncon-v1.2` §10.4.
**Razón.** El par Geist Sans/Mono es activo distintivo; el mono ancla la estética "nativo en desarrollo/IA". (Las cifras h1 56px / lead 96px / big-number 240px de `04-visual-identity` son tamaños de **slide Marp**, no de web — no usar como escala web.)

> **Tensión investigación ↔ canon (resuelta a favor del canon).** La investigación premia serif editorial para autoridad (`Análisis UX_UI` §5; ejemplo Claude). El canon SYNCON es Geist Sans/Mono, sin serif. **Se mantiene Geist** (identidad bloqueada); la autoridad editorial se logra con el sistema mono-receipt + big-number, no con serif. (El par Geist Sans/Mono figura como "proposal" en `04-visual-identity` asset #3; **se recomienda ratificarlo 3-de-3** — ya es de-facto producción: vive en `syncon.css`, el logo, el manual y los decks. Ver §9.)

### 4.4 Espaciado (grid 8-point)

**Decisión.** `--space-1:4px` · `--space-2:8px` · `--space-3:12px` · `--space-4:16px` · `--space-6:24px` · `--space-8:32px` · `--space-12:48px` · `--space-16:64px`. Base unit **8px**.
**Fuente.** `themes/syncon.css` (inyectado en `04-visual-identity.html`).
**Razón.** Ritmo industrial consistente; tokens versionados exportables a Tailwind/Figma.

### 4.5 Grid de layout

**Decisión.** Desktop **12 col / 24px gutter / 1440px max-width** · Tablet **8 col / 20px gutter** · Mobile **4 col / 16px gutter**.
**Fuente.** `04-visual-identity.html` slide Grid & spacing; `manual-de-marca-syncon-v2.1.0` §12.
**Razón.** Contención y armonía; el max-width 1440 evita líneas de lectura infinitas.

### 4.6 Radii (esquinas)

**Decisión.** **0px default** (sharp industrial) · **2px** botones (`sm`) · **8px** cards (`md`) · **full** solo avatars.
**Fuente.** `04-visual-identity.html` slide Grid & spacing; `manual-de-marca-syncon-v2.1.0` §12; `:root` del manual (`--r-sm:2px; --r-md:8px`).
**Razón.** El borde recto comunica "industrial honesto, no startup decorativa".

### 4.7 Motion

| Token | Spec | Uso |
|---|---|---|
| `instant` | 0ms | toggles |
| `--motion-quick` | **150ms** ease-out | hover / focus |
| `--motion-default` | **200ms** ease-out | button / modal |
| `emphasized` | 300ms `cubic-bezier(.2,0,0,1)` | transición de página |
| `hero` | 400ms `cubic-bezier(.22,1,.36,1)` | hero reveal |

**Easing base:** `--ease-out: cubic-bezier(0.2, 0, 0, 1)`. **Signature "assertive confirmation":** slide-up 20px + fade, 200ms ease-out, en cada state commit. `prefers-reduced-motion` → solo fades.
**Fuente.** `04-visual-identity.html` slide Motion language; `themes/syncon.css`; `manual-de-marca-syncon-v2.1.0` §12.
**Razón.** Motion como activo distintivo (#8): confirmación asertiva, sin animación decorativa.

### 4.8 Logo system (LOCKED)

**Decisión.** El logo **es la URL**: `/syncon.solutions` en **Geist Mono 700**, letter-spacing 0, 17 caracteres; **slash `/` y dot `.` en naranja `#FF6B00`**. Variantes: primary light (lienzo blanco `#FAFAFA`, ~90% de usos) · inverse dark (~10–15%: decks, video, dark UI) · mono light/dark. **Favicon:** `/` standalone (16–64px). **Clear space:** altura de un carácter mono. **Mínimo:** 64px digital / 10mm print. **Agent marks:** sufijo `.I.AM` (personal: CRIS.I.AM) + `Syncon.<ROL>` (agentes de rol).
**Don'ts:** sin gradientes · sin drop-shadows · sin rotación/distorsión · no recolorear slash/dot fuera de variantes · no reescribir en otra fuente (el mono ES la identidad) · sin magenta.
**Fuente.** `manual-de-marca-syncon-v2.1.0` §9; `04-visual-identity.html` slide Logo system; `brand-wiki-syncon-v1.2` §10.2; assets `Syncon.solution_logo.png` y `Logo blanco.jpeg` (confirman el render).
**Razón.** Lee como path de terminal (`$ /syncon.solutions`): nativo en desarrollo/IA y CTA embebido. Cambiar el logo requiere quórum 3-de-3.

> **Assets.** Rasters provistos (`Syncon.solution_logo.png`, `Logo blanco.jpeg`) = variante **primary light**. SVGs **generados** en `assets/logo/`: `syncon-primary-light.svg`, `syncon-primary-dark.svg` (inverse) y `syncon-favicon.svg` (`/`). **Nota de producción:** usan `<text>` con la familia Geist Mono; para fidelidad total, **convertir el texto a paths (outline)** con la fuente real antes del uso final, o embeber `@font-face`.

### 4.9 Fotografía

**Decisión.** Plantas colombianas **reales** (no stock): Yumbo, Mamonal, Sabana, Barranquilla · manos en teclado, cascos, espaldas · **cero sonrisas falsas, cero "startup office diverso"** · grading alto contraste + desaturado + tinte orange en accents.
**Fuente.** `manual-de-marca-syncon-v2.1.0` §12 (Fotografía); `04-visual-identity.html` slide Photography direction.
**Razón.** La foto prueba "veteranos en industria" (Principio 2) y repele la estética genérica de consultora.

### 4.10 Distinctive Asset Graph (JKR — 9 átomos)

**Decisión.** (1) Wordmark `/syncon.solutions` · (2) Color `#0A0A0A` + `#FF6B00` · (3) Par Geist Sans/Mono *(recomendado ratificar 3-de-3 — de-facto en producción)* · (4) Writing rhythm (tesis línea 1 + número) · (5) Proof-point tile (`83.3%` LoCoMo) *(status: pending design)* · (6) Agent suffix `.I.AM` + `Syncon.<ROL>` · (7) Grid 8-point sharp · (8) Motion 200ms "assertive confirmation" · (9) Sonic 1.6s *(status: roadmap)*.
**Fuente.** `manual-de-marca-syncon-v2.1.0` §13; `04-visual-identity.html` slide Distinctive Asset Graph.
**Razón.** Cualquiera de los 9 gatilla reconocimiento por sí solo; el logo es solo uno. (Status no-ratificado de #3/#5/#9 → ver `[PENDIENTE]` §9.)

### 4.11 Arquitectura de tokens (DTCG)

**Decisión.** 3 capas: `tokens/primitive.json` (raw) → `tokens/semantic.json` (role-based) → `tokens/component.json` (component-specific). Export automático a **CSS vars · Tailwind config · Figma Variables · SwiftUI/Kotlin**.
**Fuente.** `04-visual-identity.html` slide "Tokens machine-readable"; `manual-de-marca-syncon-v2.1.0` §10/§20 (provenance `tokens/*.json`).
**Razón.** La web debe consumir los tokens versionados, no hardcodear hex; un cambio de token se propaga a toda superficie.

---

## 5. Componentes y "UI feel"

> **Sensación objetivo:** un **centro de control sobrio**, no una landing de promesa abstracta.
> **Fuente:** `brand-wiki-syncon-v1.2` §10.6.

**5.1 Componentes canónicos de la web.**
**Decisión.** proof tiles (con fecha) · módulos de servicio · diagramas de flujo · comparativas antes/después · bloques "qué es / qué no es" · CTAs directos · estados de sistema · receipts dateados · FAQ citables · rutas de conversión por intención.
**Fuente.** `brand-wiki-syncon-v1.2` §10.6.
**Razón.** Estos componentes materializan los principios (receipts = P5; "qué no es" = repele wrong-fit; CTAs directos = P1).

**5.2 Especificaciones por componente** (tokens §4 + lente `taste-design`/`design-system`; estados = default/hover/active/disabled/loading/error donde aplique):

- **Botón primario.** Fill `--accent` `#FF6B00`, texto `--bg-primary` `#0A0A0A`, radius `sm` 2px, hover `--accent-hover` `#FF8833` (150ms), active translate sutil ("assertive confirmation"), **sin outer-glow ni neon**. Focus ring 2px orange. **Fuente:** `:root` y `.badge` del `manual`; motion §4.7; accesibilidad §4.2.
- **Botón secundario / ghost.** Borde 1px `--accent`, texto `--accent`, fondo transparente. **Fuente:** `.badge.ghost` del `manual`.
- **Card.** Fondo `--bg-secondary` `#1A1A1A`, borde 1px `--border-subtle` `#444444`, radius `md` 8px, padding `--space-6/8`. Sombra solo si la elevación comunica jerarquía (estética: sin drop-shadow decorativo). **Fuente:** `.card` del `manual` §10; radii §4.6.
- **Input/Form.** Label arriba, helper opcional, **error debajo**; focus ring orange 2px; min 16px; tap 44px. **Fuente:** accesibilidad §4.2; microcopy §3.5; lente `design-system`.
- **Receipt / proof tile.** Mono, `border-left: 3px solid --accent`, fondo `--bg-secondary`, **fecha visible siempre**. **Fuente:** `.receipt` de `themes/syncon.css`; Principio 5.
- **Tag / pill.** Mono, uppercase, letter-spacing .04em; `hot` = borde/texto orange. **Fuente:** `.tag`/`.pill` del `manual` y `syncon.css`.
- **Bloque quote.** `border-left: 3–4px solid --accent`, fondo `--bg-secondary`. **Fuente:** `.q`/`blockquote` del `manual` y `syncon.css`.
- **Loading.** Skeletons que respetan dimensiones del layout (no spinners genéricos). **Fuente:** lente `taste-design`/`Análisis UX_UI` §microinteracciones (apropiable, no choca con canon).

**Razón.** Componer con tokens y estados explícitos evita reinventar y mantiene el "centro de control" coherente.

### 5.3 Proof-tile (asset distintivo #5)

**Decisión.** Tile de prueba con jerarquía estricta: **dato grande** (Geist Mono/display, en `--accent` `#FF6B00` o `--fg-primary`) + **label corto** (mono, uppercase, `--fg-muted`, letter-spacing .1em) + **fecha** (mono, `--fg-muted`). Fondo `--bg-secondary` `#1A1A1A`, `border-left: 3px solid --accent`, radius `md` 8px, padding `--space-6`, sin sombra decorativa. Ejemplo: `83.3%` / `MEMORIA LoCoMo` / `paper publicado · jun 2026`.
**Fuente.** Asset #5 de `manual` §13 y `04-visual-identity` ("Proof-point tile · 83.3% LoCoMo", status pending design); estilo derivado de `.receipt` de `themes/syncon.css` + escala `big-number` de `04-visual-identity`. Lente `taste-design`: "no fabricated data" → el dato siempre de un receipt real y dateado.
**Razón.** Convierte el Principio 5 (publicar recibos) en un componente reutilizable y escaneable en 2s; sustituye al testimonio vacío.

---

## 6. Leyes de conversión y UX para la web

> Patrones validados en la investigación del ecosistema IA (16 sitios), **filtrados por el canon**: se adopta la *mecánica* de conversión; la *identidad* (negro-dominante, Geist, sin logo walls) manda.
> **Fuente:** `Análisis UX_UI Ecosistema IA.md` + `Optimización de Conversión en IA.md`, reconciliados con `brand-wiki-syncon-v1.2` y `voice-brand v0.2` §10.

**6.1 "El producto es la demo" en el hero.**
**Decisión.** Hero con un componente interactivo que muestre el Company Brain / un agente de rol en acción (dogfooding), no un mockup estático.
**Fuente.** `Optimización de Conversión` §5 Bloque 1 + "El auge de 'El producto es la demo'"; alineado a `manual` §1 ("Somos nuestra propia demo: SYNCON runs on SYNCON").
**Razón.** Mayor retención above-the-fold y, además, **es la prueba** (P5 + dogfooding). Encaja con la identidad sin importarla de afuera.

**6.2 Prueba social = receipts dateados, NO logo walls.**
**Decisión.** La barra de credibilidad usa **cápsulas de ROI/receipts** (ej. "482 págs · salud 99/100 · jun 2026", "4 agentes de rol read-only", "83.3% LoCoMo · paper publicado") en lugar de logos de clientes.
**Fuente.** Investigación pide "logo bar + chunking de métricas" (`Análisis UX_UI` §6 Bloque 3; `Optimización` §5 Bloque 2). **Canon override:** Principio 6 prohíbe logo walls / "trusted by" vacío y SYNCON tiene 0 clientes externos publicables (`manual` §15 receipts).
**Razón.** Se conserva la *mecánica* (chunking numérico escaneable en 2s) y se respeta la *ley* (no inventar prueba social).

**6.3 Sección "Cómo trabajamos" / Metodología.**
**Decisión.** Sección deductiva tipo blueprint que mapea el método (Diagnóstico contextual → Rediseño/Implementación → Acompañamiento/Retainer).
**Fuente.** Patrón en 6/8 sitios B2B (`Análisis UX_UI` §4/§6 Bloque 5; `Optimización` Every/Neurons Lab); contenido = 3 capas de entrega de `brand-wiki-syncon-v1.2` §5.
**Razón.** Reduce el miedo técnico del C-level y materializa el Principio 7 (contexto antes que solución).

**6.4 Bento grid de servicios = 2 motores.**
**Decisión.** Mosaico asimétrico (no 3 cards iguales), cada módulo: **dolor del ICP → función → beneficio en $**. Revelación progresiva al hover.
**Fuente.** `Optimización` §5 Bloque 3; `Análisis UX_UI` §6 Bloque 4; oferta = 2 motores de `voice-brand v0.2` §10-bis. Lente `taste-design`: prohibido el "3-column equal cards".
**Razón.** Descomprime servicios complejos en jerarquía escaneable.

**6.5 FAQ optimizada para motores conversacionales (AEO/GEO).**
**Decisión.** Bloque FAQ con **FAQPage Schema (JSON-LD)**, respuestas fácticas de **40–150 palabras**, preguntas en lenguaje natural de compradores reales.
**Fuente.** `Optimización` §5 Bloque 5 + checklist #2; alineado a "FAQ citables" de `brand-wiki-syncon-v1.2` §10.6 y al Principio 5.
**Razón.** El tráfico referido por asistentes IA convierte mucho más alto que orgánico tradicional; SYNCON (nativo en IA) debe ser citable.

**6.6 Formularios de fricción cero (footer / cierre).**
**Decisión.** Formulario al pie de páginas de contenido y al cierre, **≤ 3–4 campos** (correo corporativo + URL + selector de necesidad/presupuesto). Sin pop-ups. Micro-copy mitigador honesto: ej. "Respondemos con viabilidad en 24h" (**sin prometer ROI garantizado**).
**Fuente.** `Optimización` checklist #1 (+120% leads al reducir campos) y §5 Bloque 6; `Análisis UX_UI` §7; copy alineado a `voice-brand v0.2` §10/§5 (prohibido ROI garantizado).
**Razón.** Capitaliza el pico de interés sin fricción ni promesas que el canon prohíbe.

**6.7 Pricing visible (no "contact sales").**
**Decisión.** Página de pricing con **rangos de planeación** + frase de cierre obligatoria: *"El pricing final depende del alcance y se define en el diagnóstico contextual."* (Rangos no vinculantes; no precio final sin diagnóstico.)
**Fuente.** `manual-de-marca-syncon-v2.1.0` §14/§16; `voice-brand v0.2` §6.
**Razón.** Transparencia (P5) y anti-"contact sales" (P6), sin violar la regla de pricing por ROI.

**6.8 Higiene técnica y de interacción.**
**Decisión.** Touch targets 44×44 · LCP sub-segundo (lazy-load, CDN, imágenes comprimidas) · **sin carruseles** (grillas estáticas + métricas duras) · progressive disclosure · header sticky translúcido→opaco on-scroll · menú anclado, no mega-menú caótico · móvil colapsa a 1 columna, sin scroll horizontal.
**Fuente.** `Análisis UX_UI` §5/§7; `Optimización` checklist #3; accesibilidad canon §4.2; lente `taste-design` (sin carruseles, `min-h-[100dvh]`).
**Razón.** Rendimiento y claridad son parte del posicionamiento ("operación inteligente").

**6.9 Tensión documentada — modo oscuro vs. lectura larga.**
**Decisión.** La web se mantiene **negro-dominante** (identidad bloqueada). En superficies de **lectura larga** (blog, `/receipts`, docs) se mitiga el "halo borroso" con **medida ≤ 72ch + line-height ≥ 1.5** (ya en el canon: `p{max-width:72ch}`, line-height 1.5/1.55 en el manual). Si tras pruebas la fatiga persiste, **decisión de Lorena (Brand Owner)**.
**Fuente.** Investigación recomienda light-mode para blogs B2B (`Análisis UX_UI` §Q9/Q13, Blend B2B); canon es negro-dominante y rechaza fondos claros SaaS (`04-visual-identity` Philosophy; `manual` §10).
**Razón.** No se importa una decisión que contradice la identidad; se documenta la tensión y se mitiga dentro del canon, dejando la última palabra al owner.

---

## 7. Arquitectura de la página principal (home)

**Decisión.** Orden recomendado, reconciliando la estructura del canon con el blueprint de conversión:
1. **Hero (firma):** tagline master "Ingeniería contextual. Operaciones inteligentes." + las dos líneas (consultoría/desarrollo + Company Brain) + CTA "Diagnosticar mi operación". Tono: Disruptivo MAXED · Directo MAXED.
2. **Dolor:** "la empresa que olvida".
3. **Producto:** Company Brain + HAR (tesis de producto cuando se ratifique) + componente "producto es la demo".
4. **Receipts:** 482 págs · salud 99/100 (jun 2026) · 4 agentes read-only · CRIS.I.AM desde ene 2026 · web live desde abr 2026 — **valores dateados**.
5. **2 motores activos:** (A) Consultoría contextual + software a la medida; (B) Company Brain + HAR (bento §6.4).
6. **Cómo trabajamos:** metodología en 3 capas (§6.3).
7. **Enemigos / "qué no somos":** consultoría de slides, pricing por horas, wrappers de ChatGPT.
8. **Para quién:** mid-market industrial y de servicios LATAM (repele wrong-fit).
9. **FAQ AEO/GEO** (§6.5).
10. **Cierre + formulario calificado** (§6.6).

**Fuente.** `voice-brand v0.2` §10 (estructura recomendada de home, 8 secciones) fusionada con `Optimización` §5 (blueprint 6 bloques) y `Análisis UX_UI` §6; receipts vivos de `voice-brand v0.2` §6/§10.
**Razón.** Sigue la secuencia de persuasión del canon (contexto → producto → prueba → oferta → límites → conversión) sin importar plantillas ajenas.

> **Receipts = valores vivos.** Render siempre dateado (`get_health`); **nunca hardcodear**. El manual citaba "420+/100" (snapshot 11-jun); Voice Brand v0.2 (23-jun) corrige a **482/99**. Conflicto resuelto a favor del dato más reciente + regla "ningún receipt sin fecha".

### 7.1 Página pública `/receipts`

**Decisión.** Página dedicada que materializa el Principio 5. Estructura: (1) hero corto ("Publicamos lo que otros esconden"); (2) **grid/tabla de receipts** con el esquema canónico — **Claim · Receipt · Fecha · Qué prueba · Qué no prueba todavía · Status · Próxima actualización**; (3) proof-tiles (§5.3) para los datos ancla; (4) nota de cadencia; (5) cierre con CTA a diagnóstico. Modo oscuro con la mitigación de lectura de §6.9. Cada fila lleva fecha; nada sin receipt.
**Fuente.** Esquema de receipt verbatim de `brand-wiki-syncon-v1.2` §7; cadencia "mensual, primer lunes" y go-live sugerido Q3 2026 de `brand-wiki` §7 / `voice-brand v0.2` §18 / `manual` §15.
**Razón.** Es el activo de confianza central de SYNCON (sustituye logo walls, §6.2). El diseño está cerrado; **faltan datos de fundadores** (ver §9.2): lista de receipts iniciales y fecha de go-live. No se inventan.

---

## 8. Anti-patrones (lo que la web nunca hace)

**Decisión.**
- **Verbal:** "me complace anunciar" · "soluciones innovadoras/de clase mundial" · "transformación digital" · "chatbot/asistente virtual" · arrogancia sin receipt · ROI garantizado · "red de agentes/A2A autónomo" · nombrar clientes sin aprobación 2-of-2 · Title Case inglés en hero español · exclamaciones B2B.
- **Visual:** magenta `#FF0055` · "AI purple"/neon glows · gradientes/drop-shadows en identidad · stock photos / "diverse startup office" · logo walls / "trusted by" vacío · 3 cards iguales · carruseles · saturación de foto · plantillas 2010s copiables.
- **Producto/claims (T4):** "N agentes autónomos en producción" · "Company Brain production-ready/multi-tenant" · "HAR es categoría establecida" · pricing final sin diagnóstico · trayectorias de personas que ya no están.
**Fuente.** `voice-brand v0.2` §5/§7; `manual-de-marca-syncon-v2.1.0` §6/§14; `brand-wiki-syncon-v1.2` §9/§11; lentes `taste-design` y `frontend-design` (anti-slop) que coinciden con el canon.
**Razón.** Los anti-patrones son tan canon como las reglas: definen qué está fuera (brand governance).

**Quality Gate de salida:** ninguna pieza se publica sin pasar ≥ 4/5 del test booleano (§2) y la ratificación de claims (2-of-2 marketing / 3-de-3 estructural).

---

## 9. Estado de decisiones (ratificación 2026-06-24)

> Lorena (COO, Brand Owner) ratificó/delegó los pendientes el 2026-06-24. Lo que es 2-of-2 / 3-de-3 **no se auto-ratifica**: queda listo para co-firma.

### 9.1 Resueltas

| # | Decisión | Resolución | Vía |
|---|---|---|---|
| 1 | HQ / sede | **Bogotá, Colombia** — firma latinoamericana, sede principal. Yumbo/Mamonal/Sabana/Barranquilla = geografías industriales (foto/casos), no sedes. Ver §1.8. | Lorena (COO) |
| 3 | AI Adoption Diagnostic | **5 horas** (modular). Cierra el 4h vs 5h. | Lorena (COO) |
| 4 | Hex de carriles de agente | CEO `#00E5FF` · COO **`#FFB300`** · CTO **`#00E676`** (amber/green derivados por diseño, ver §4.1). `[PROPUESTO]` para co-firma de Cris (owner de tokens). | Lorena delegó → derivado |
| 5 | Par tipográfico Geist | **Recomendado ratificar 3-de-3** (de-facto en producción). Ver §4.3/§4.10. | Lorena delegó → reconciliado |
| 9 | SVG inverse del logo | **Generado**: `assets/logo/syncon-primary-dark.svg` (+ `-light` y favicon). Ver §4.8 y nota de outline. | Generado por instrucción |

### 9.2 Abiertas — qué falta para cerrar

| # | Pendiente | Qué se necesita |
|---|---|---|
| 2 | **Tesis de hero de producto** "Tu empresa ya tiene un cerebro…" | **Co-firma de Cris (CEO)** para completar 2-of-2 (Lorena la sostiene como candidata vigente). Sin eso sigue `[PROPUESTO]`: usable en mockups internos, no en publicación externa. |
| 6 | **Proof-tile** (asset #5) | Diseño **cerrado** en §5.3. Falta solo confirmar la **métrica ancla** (sugerido `83.3% LoCoMo` o `482 págs · salud 99`); el dato debe ser un receipt real y dateado. |
| 7 | **Identidad sónica** (1.6s, asset #9) | Fuera del alcance de un design system (producción de audio). Para producirla: brief de mood (industrial, "assertive confirmation", 1.6s, mapeado al motion §4.7) + sound designer. **Recomiendo diferir** (roadmap). |
| 8 | **Página `/receipts`** | Arquitectura **cerrada** en §7.1. Faltan datos de fundadores: (a) lista de receipts iniciales + status; (b) cadencia y fecha de go-live. No se inventan. |
| — | **Colores semánticos de estado** *(detectado)* | `syncon.css` no define success/warning/error (solo negro/gris/blanco/naranja); las specs de formularios/estados (§5) los requieren. Definir: ¿error en naranja-accent, en un rojo nuevo, o grayscale + ícono? No lo invento; lo marco. |

---

## 10. Procedencia (trazabilidad del documento)

**Insumos leídos (12):** `brand-wiki-syncon-v1.2-interno-cerrado.md` · `manual-de-marca-syncon-v2.1.0.html` · `04-visual-identity.html` (+ `themes/syncon.css`) · `voice-brand-syncon-operativo-v0.2-reconciliado.md` · `01-brand-overview.html` · `02-constitution.html` · `03-voice-tone.html` · `05-disruptive-playbook.html` · `06-roadmap.html` · `Análisis UX_UI Ecosistema IA.md` · `Optimización de Conversión en IA.md` · `Syncon.solution_logo.png` + `Logo blanco.jpeg`.

**Fuentes raíz del canon (citadas por los insumos, fuera de esta carpeta):** `brand.json v2.1.0` · `constitution.md` (v2.0.0) · `voice.yaml` + `llms.txt` · `tokens/*.json` (DTCG) · Company Brain (`get_health`).

**Paso 3 (web):** omitido — las investigaciones locales ya cubren la lista de URLs del prompt.

**Método:** extracción pura con lentes de diseño activas (`design-system`, `brand-governance`, `digital-brand-strategy`, `frontend-design`, `brand-voice`, `taste-design`). Cero inferencias: cada ítem trae fuente; los huecos se marcan `[PENDIENTE]`.

---

---

## 11. Implementación web — decisiones de diseño (home mockup v1.3 · 2026-06-25)

> Esta sección registra decisiones tomadas durante la construcción del home mockup. Son canon para todas las páginas nuevas.

### 11.1 Tokens CSS adicionales (producción)

| Token | Valor | Uso |
|---|---|---|
| `--r-full` | `99px` | Pill buttons, pills de kicker, tags, card-cta |
| `--r-sm` | `2px` | Inputs, botón primary cuadrado |
| `--r-md` | `8px` | Cards, tiles, dropdown, console |

### 11.2 Anti-patrones de implementación (absolutos — nunca usar)

Estos complementan los anti-patrones verbales/visuales de §8:

- **`border-left > 1px` como acento de color** en cards, tiles o callouts. Reemplazar con borde completo (`border:1px solid`) + `border-top:2px solid var(--accent)` para acento direccional. Razón: side-stripe es AI scaffold 2023.
- **`background-clip:text` con gradiente** (gradient text). Usar color sólido. Siempre.
- **Glassmorphism decorativo** (`backdrop-filter:blur` como estética por defecto). Solo para capas de modal/overlay con propósito funcional.
- **Kicker standalone (`<span class="kicker">`) encima de cada h2**. Canon: el kicker vive DENTRO del h2 como primer `<span>` hijo (kicker-fusionado). Única excepción: labels de columnas de datos (ej. "Somos nuestro primer caso de uso" en receipts).
- **`opacity:0` como estado base con CSS animation gated por clase JS**. Usar IntersectionObserver + CSS transition (`.reveal` / `.reveal.in-view`). Razón: CSS animations pausan en pestañas ocultas al cargar.
- **`querySelectorAll('li')` en nav cursor JS** sin `:scope >`. Captura descendientes del dropdown y produce cursor incorrecto. Usar `:scope > li:not(#nav-cursor)`.

### 11.3 Patrones aprobados (reutilizar en páginas nuevas)

**Estructura HTML semántica obligatoria:**
- `<a class="skip-link" href="#main-content">` antes del `<header>`
- `<nav aria-label="Navegación principal">` (no `<div>`)
- `<main id="main-content">` envolviendo todas las secciones entre mobile-menu y footer

**Kicker fusionado (canon desde #enemigos):**
```html
<h2>
  <span style="display:block;font-family:var(--mono);font-size:11px;font-weight:400;color:var(--accent);letter-spacing:.14em;text-transform:uppercase;margin-bottom:var(--s3)">KICKER</span>
  <span style="display:block;color:var(--paper)">Título blanco</span>
  <span style="display:block;color:var(--accent)">Remate naranja.</span>
</h2>
```

**H2 bicolor de sección:** `font-size:clamp(28px,3.6vw,40px)` · `font-weight:800` · `letter-spacing:-0.04em` · `line-height:1.06`

**Trust list slash:** `<ul>` + `<li style="font-family:var(--mono);font-size:13px;color:var(--fg-2)"><span class="accent">/ </span>texto</li>` · `gap:var(--s3)` · `margin-top:var(--s8)`

**Select color states (pure CSS):**
```css
select:invalid { color: var(--muted) }
select:valid   { color: var(--accent) }
option         { color: var(--fg-2); background: var(--ink) }
option:checked { color: var(--accent) }
```
Requiere `required` en el select y `value="" disabled selected` en el placeholder.

**Reveal (IntersectionObserver):**
```css
.reveal { opacity:0; transform:translateY(20px); transition:opacity .6s var(--ease),transform .6s var(--ease) }
.reveal.in-view { opacity:1; transform:none }
```
```js
var obs = new IntersectionObserver(function(entries){
  entries.forEach(function(e){
    if(!e.isIntersecting) return;
    e.target.style.transitionDelay = e.target.dataset.delay || '0s';
    e.target.classList.add('in-view');
    obs.unobserve(e.target);
  });
}, {threshold:0.08});
document.querySelectorAll('.reveal').forEach(function(el){ obs.observe(el); });
```
Stagger vía `data-delay=".1s"` en el elemento HTML (no `animation-delay`).

**Glow hover en tiles y cards:**
```css
box-shadow: 0 0 24px rgba(255,107,0,.22), 0 0 64px rgba(255,107,0,.08)
```

**Form success state:** `id="form-container"` → JS reemplaza innerHTML con `.form-success` div.

**Mobile menu:** `<div id="mobile-menu" class="mobile-menu">` + JS toggle + `aria-expanded` + cierre en Escape y click de links.

### 11.4 Tipografía canon (mínimos de la web)

| Elemento | Tamaño | Peso | Color |
|---|---|---|---|
| Body / párrafos | 17px mínimo | 400 | `var(--fg-2)` |
| `.lede` | `clamp(18px,2.2vw,21px)` | 400 | `var(--fg-2)` |
| H1 hero | `clamp(38px,5.2vw,72px)` | 800 | paper / accent |
| H2 sección | `clamp(28px,3.6vw,40px)` | 800 | paper + accent |
| H3 card | `clamp(22px,2.4vw,28px)` | 700 | paper |
| Kicker mono | 11px | 400 | `var(--accent)` |
| Tags / labels | 11–13px Geist Mono | 400–500 | `var(--accent)` / `var(--fg-2)` |
| `.anti` callout | `clamp(17px,1.6vw,20px)` | 600 | paper |

### 11.5 Estado de archivos del home

| Archivo | Estado |
|---|---|
| `home-mockup.html` | **CERRADO** — post-audit v1.3 (2026-06-25) |
| `home-mockup-v3-pre-audit-2026-06-25.html` | Snapshot pre-audit (comparación) |
| `home-mockup-v2-2026-06-24.html` | Snapshot sesión anterior |

**Canal de distribución aprobado:** web (`psychevaluations.net` → no aplica; dominio SYNCON pendiente) + **LinkedIn** (`linkedin.com/company/syncon-solutions`). LinkedIn en footer columna Contacto. Ningún otro canal social en el home.

**Páginas siguientes en cola:**
1. ✅ `/productos` — landing de los 3 productos · CERRADA 2026-06-30
   - ✅ `/productos/har` · CERRADA 2026-06-30 (video Arquitectura_y_cerebro.mp4, CTA 'Construir mi cerebro corporativo')
   - ✅ `/productos/consultoria` · CERRADA 2026-06-30 (frame-static log proceso, CTA 'Diagnosticar mi operación')
   - ✅ `/productos/capacitacion` · CERRADA 2026-06-30 (frame-static agenda 6 módulos, CTA 'Solicitar plan de capacitación')
2. ✅ `/about` — La firma · CERRADA 2026-06-30
3. `/articulos` — Blog CIO/GIO · pendiente

---

---

## 12. Reglas de implementación CSS/UI — cerradas en el home (2026-06-25/26)

> Esta sección es la **fuente de verdad para construir páginas nuevas**. Cada regla fue cerrada durante la construcción del home mockup y validada visualmente. No son sugerencias — son el estándar.

---

### 12.1 Contenedor canónico y overflow

```css
/* Contenedor universal de todas las secciones */
.wrap { max-width: 1240px; margin: 0 auto; padding: 0 24px; }

/* Overflow horizontal — SIEMPRE clip, NUNCA hidden */
html { overflow-x: clip; }
```

**Por qué `clip` y no `hidden`:** `overflow-x:hidden` en `html`/`body` crea un nuevo scroll container y rompe `position:sticky` del header. `overflow-x:clip` recorta visualmente sin crear scroll container.

**Regla crítica de padding:** Si un elemento tiene AMBAS clases `.wrap` y una clase propia con padding (ej. `.hero-grid`), usar `padding-top`/`padding-bottom` INDIVIDUALES en la clase propia — NUNCA el shorthand `padding: A B`. El shorthand de la clase posterior sobreescribe TODOS los lados, incluyendo el `padding:0 24px` del `.wrap`, eliminando los márgenes laterales.

```css
/* CORRECTO */
.hero-grid { padding-top: clamp(56px,8vw,104px); padding-bottom: clamp(56px,8vw,104px); }

/* INCORRECTO — elimina el padding lateral del .wrap */
.hero-grid { padding: clamp(56px,8vw,104px) 0; }
```

---

### 12.2 Secciones — padding y fondos alternos

```css
/* Padding vertical + separador visual de TODAS las secciones excepto hero y cierre */
section { padding: clamp(64px,9vw,120px) 0; border-bottom: 1px solid var(--bg-2); }

/* Hero y cierre anulan el border-bottom via inline style="border-bottom:none" */

/* Fondos alternos para separar secciones visualmente */
/* fondo oscuro base */   --bg:   #0A0A0A   → secciones impares / hero
/* fondo elevado */       --bg-2: #1A1A1A   → secciones pares / cierre / footer

/* Ejemplo */
.cierre { background: var(--bg-2); }
```

Nunca usar un tercer fondo. El `border-bottom:1px solid var(--bg-2)` es el único separador entre secciones — la línea es casi invisible en dark mode pero ancla visualmente el cambio de contexto.

---

### 12.3 Sistema de botones (implementación web canónica)

**Arquitectura de border-radius:**
- La clase base `.btn` usa `border-radius:var(--r-sm)` (2px — sharp industrial).
- Las CTAs públicas de la web reciben pill **vía selector específico** o inline override, no desde la base.
- **Excepción única con r-sm (no pill):** el botón de submit del formulario (hereda la base sin override).

| Contexto | Selector que añade pill | Resultado |
|---|---|---|
| Hero CTAs | `.hero-actions .btn` | pill |
| Nav CTA | `.nav-cta .btn-primary` | pill |
| Mobile menu CTA | `.mobile-menu-cta` | pill (clase directa) |
| Botones en secciones | `style="border-radius:var(--r-full)"` inline | pill |
| Card CTA | `.card-cta` (clase propia) | siempre pill |
| Form submit | sin override | **r-sm 2px** |

```css
/* Base compartida — r-sm por defecto */
.btn {
  display: inline-flex; align-items: center; justify-content: center;
  gap: 8px;
  font-family: var(--sans); font-weight: 600; font-size: 16px;
  border-radius: var(--r-sm);   /* 2px — sharp base */
  min-height: 48px; padding: 0 22px;
  border: 1px solid transparent;
  transition: background var(--quick) var(--ease),
              transform var(--quick) var(--ease),
              border-color var(--quick) var(--ease);
  cursor: pointer; text-decoration: none; text-align: center;
}

/* Primario — naranja sólido */
.btn-primary { background: var(--accent); color: var(--ink); }
.btn-primary:hover { background: var(--accent-hover); }
.btn-primary:active { transform: translateY(1px); background: var(--accent-pressed); }

/* Ghost — borde gris var(--border) */
.btn-ghost { background: transparent; color: var(--paper); border-color: var(--border); }
.btn-ghost:hover {
  border-color: var(--accent);
  color: var(--accent);                          /* texto cambia a naranja */
  box-shadow: 0 0 18px rgba(255,107,0,.25);      /* glow suave */
}

/* Flecha animada dentro del ghost */
.btn-ghost span { display: inline-block; transition: transform var(--quick) var(--ease); }
.btn-ghost:hover span { transform: translateX(4px); }

/* Hero/nav/sección: pill override */
.hero-actions .btn,
.nav-cta .btn-primary { border-radius: var(--r-full); }

/* Hero CTA primario — glow fuerte (solo en hero) */
.hero-actions .btn-primary:hover,
.nav-cta .btn-primary:hover {
  background: var(--accent-hover);
  box-shadow: 0 0 28px rgba(255,107,0,.55), 0 0 60px rgba(255,107,0,.22);
}

/* Hero CTAs: font-size reducido en el hero */
.hero-actions .btn { padding: 0 18px; font-size: 14px; }

/* Focus ring accesible */
.btn:focus-visible { outline: 2px solid var(--accent); outline-offset: 3px; }
```

**CTA de card (`.card-cta`):**
```css
.card-cta {
  display: inline-flex; align-items: center; gap: 8px;
  font-family: var(--sans); font-size: 14px; font-weight: 600;
  color: var(--paper); padding: 0 20px; min-height: 44px;
  border: 1px solid var(--border); border-radius: var(--r-full);
  transition: border-color var(--quick) var(--ease),
              color var(--quick) var(--ease),
              box-shadow var(--quick) var(--ease);
}
.card-cta:hover {
  border-color: var(--accent); color: var(--accent);
  box-shadow: 0 0 18px rgba(255,107,0,.25);
}
.card-cta span { display: inline-block; transition: transform var(--quick) var(--ease); }
.card-cta:hover span { transform: translateX(4px); }
```

---

### 12.4 Glow y efectos visuales

**Glow en tiles/cards al hover:**
```css
/* Tarjetas de producto, bento tiles */
.tile:hover {
  box-shadow: 0 0 24px rgba(255,107,0,.22), 0 0 64px rgba(255,107,0,.08);
  border-color: var(--accent);
}
```

**Glow del botón primario al hover:** ver §12.3.

**Glow del frame del hero (Company Brain):**
```css
.frame-wrapper {
  box-shadow: 0 0 40px rgba(255,107,0,.28),
              0 0 100px rgba(255,107,0,.16),
              0 0 260px rgba(255,107,0,.09);
}
```
Este glow extendido requiere que la sección padre tenga `overflow:hidden` para no contaminar el layout horizontal.

**Regla de glow:** los radios de glow son siempre **naranja `rgba(255,107,0,…)`**. Opacidades descendentes: `.28 → .16 → .09` (tres capas). Nunca glow en identidad (logo, wordmark).

**H1 hero — text-shadow glow:**
```css
.hero h1 .line1 {
  text-shadow: 0 0 60px rgba(255,107,0,.40),
               0 0 120px rgba(255,107,0,.15),
               0 0 260px rgba(255,107,0,.06);
}
```
Solo en la línea naranja del hero. Nunca en body text ni h2/h3.

---

### 12.5 Grids de contenido (patrones de layout)

Todos los grids de contenido usan `gap:clamp(mínimo, vw, máximo)` para ser fluidos.

```css
/* Hero — leve asimetría (texto ligeramente más ancho que el frame) */
.hero-grid {
  display: grid;
  grid-template-columns: 1.05fr .95fr;
  gap: clamp(32px,5vw,72px);
  align-items: center;
  padding-top: clamp(56px,8vw,104px);    /* NUNCA shorthand padding — rompe .wrap lateral */
  padding-bottom: clamp(56px,8vw,104px);
}

/* Split 2-col asimétrico (sección dolor) — la col de texto es más estrecha que la de copy */
.split { display:grid; grid-template-columns:.85fr 1.15fr; gap:clamp(28px,5vw,64px); align-items:start; }

/* Bento simétrico (motores — 2 cards de igual peso) */
.bento { display:grid; grid-template-columns:1fr 1fr; gap:var(--s4); margin-top:var(--s8); }

/* Producto+receipts (texto + tile-stack) — gap amplio para separar conceptualmente */
.producto-grid { display:grid; grid-template-columns:1fr 1fr; gap:clamp(40px,5vw,80px); align-items:stretch; }

/* Steps — 3 columnas fijas (la metodología es exactamente 3 pasos) */
.steps { display:grid; grid-template-columns:repeat(3,1fr); gap:var(--s8); margin-top:var(--s8); }

/* Who — auto-fit para escalar con el número de perfiles */
.who { display:grid; grid-template-columns:repeat(auto-fit,minmax(240px,1fr)); gap:var(--s6); margin-top:var(--s8); }

/* Cierre / contacto */
.cierre-grid { display:grid; grid-template-columns:1fr 1fr; gap:clamp(32px,5vw,64px); align-items:center; }
```

**Regla `min-width:0`:** todo grid child que contenga texto largo o inputs DEBE tener `min-width:0`. Sin esto, el item expande la columna más allá de su `fr` asignado (comportamiento por defecto de CSS Grid: `min-width:auto`).

---

### 12.6 Tipografía — valores exactos de producción

Estos valores reemplazan la escala teórica de §4.3 en el contexto web:

| Elemento | CSS exacto | Notas |
|---|---|---|
| H1 hero línea 1 | `clamp(38px,5.2vw,72px)` · weight 800 · tracking `-0.04em` · lh `1.04` | Color: `var(--accent)` |
| H1 hero línea 2 | `clamp(26px,3.4vw,50px)` · weight 700 · tracking `-0.025em` | Color: `var(--paper)` |
| H2 sección | `clamp(28px,3.6vw,40px)` · weight 800 · tracking `-0.04em` · lh `1.06` | Bicolor: paper + accent |
| H3 card | `clamp(22px,2.4vw,28px)` · weight 700 | Color: `var(--paper)` |
| `.lede` | `clamp(18px,2.2vw,21px)` · weight 400 · lh `1.6` · `max-width:62ch` | Color: `var(--fg-2)` |
| Body mínimo | `17px` · weight 400 · lh `1.6` | Nunca bajar de 17px en secciones |
| Kicker mono (h2 fusionado) | `11px` · Geist Mono · weight 400 · tracking `.14em` · uppercase | Color: `var(--accent)` |
| Tags / labels UI | `11–13px` · Geist Mono | `var(--accent)` o `var(--fg-2)` |
| `.anti` callout | `clamp(17px,1.6vw,20px)` · weight 600 | Nunca bajar de 17px |
| Steps h4 | `clamp(20px,2.2vw,26px)` | — |
| Nav links | `15px` | Color: `var(--fg-2)` |

---

### 12.7 Cards y tiles

**Card base:**
```css
.card {
  background: var(--bg-2);
  border: 1px solid var(--border);     /* gris neutro por defecto */
  border-radius: var(--r-md);          /* 8px */
  padding: var(--s8) var(--s6);
}
.card:hover {
  border-color: var(--accent);
  box-shadow: 0 0 24px rgba(255,107,0,.22), 0 0 64px rgba(255,107,0,.08);
}
```

**Tile de producto (tile-lg):** borde completo naranja tenue `border:1px solid rgba(255,107,0,.25)`. NO `border-left` aislado.

**Anti (callout de enemigo):**
```css
.anti {
  border: 1px solid var(--border);
  border-top: 2px solid var(--accent);   /* acento solo arriba */
}
```

**Nunca:** `border-left:3px solid var(--accent)` como único acento — side stripe prohibido (§11.2).

---

### 12.8 Kicker pill (hero standalone)

El kicker del hero es el único kicker que vive FUERA del h2, como elemento independiente antes del h1.

```css
.kicker-pill {
  display: inline-flex; align-items: center; gap: 8px;
  font-family: var(--mono); font-size: 11px; font-weight: 400;
  letter-spacing: .14em; text-transform: uppercase;
  color: var(--paper);                       /* texto blanco — el color lo da el kicker-dot */
  border: 1px solid rgba(255,107,0,.28);     /* borde naranja tenue .28 */
  background: rgba(255,107,0,.04);           /* bg naranja muy sutil .04 */
  border-radius: var(--r-full);              /* pill en desktop */
  padding: 5px 14px 5px 10px;               /* asimétrico: más espacio izq para el dot */
}

/* Dot animado dentro del pill */
.kicker-dot {
  display: inline-block; width: 6px; height: 6px;
  border-radius: 50%; background: var(--accent);
  margin-right: 8px; vertical-align: middle;
  animation: pulse-dot 2s ease-in-out infinite;
}
@keyframes pulse-dot { 0%,100%{opacity:1} 50%{opacity:.35} }

/* En móvil (≤640px): badge rectangular */
@media (max-width:640px) {
  .kicker-pill {
    border-radius: var(--r-md);   /* 8px — badge, no pill */
    display: inline-block;
    max-width: 100%;              /* nunca desborda el contenedor */
    font-size: 11px;
    letter-spacing: .10em;
    padding: 6px 12px;
  }
}
```

La diferencia desktop/móvil: en desktop el texto cabe en una línea → pill se ve bien. En móvil el texto es largo y wrappea → pill multilinea se ve roto → badge rectangular.

**Importante:** `color:var(--paper)` (blanco), NO `var(--accent)`. El naranja lo aporta el `.kicker-dot` y el borde. El texto en paper sobre fondo oscuro con borde naranja es más legible que texto naranja puro.

---

### 12.9 Nav sticky

```css
header {
  position: sticky; top: 0; z-index: 50;
  backdrop-filter: blur(8px);              /* 8px inicial — sutil */
  background: rgba(10,10,10,.6);           /* .6 inicial — semitransparente */
  border-bottom: 1px solid transparent;
  transition: background var(--default) var(--ease),
              border-color var(--default) var(--ease);
}
header.scrolled {
  background: rgba(10,10,10,.92);          /* .92 al scroll — casi opaco */
  border-bottom-color: var(--bg-2);
}

/* La altura de 72px viene del .nav, no del header */
.nav { display: flex; align-items: center; justify-content: space-between; height: 72px; }
```

JS añade `.scrolled` cuando `window.scrollY > 24` (no 0 — pequeño margen antes de activar). Nunca usar `position:fixed` — rompe el flujo del documento y genera saltos en secciones al-anchor.

**Nav cursor (floating pill):** el `#nav-cursor` es un `<li>` con position absolute dentro de `.nav-links` que sigue al ítem bajo el mouse via JS (`item.offsetLeft`, `item.offsetWidth`, `opacity:1`).

```css
#nav-cursor {
  position: absolute; top: 50%; transform: translateY(-50%);
  height: 36px; border-radius: var(--r-full);
  background: rgba(255,107,0,.08); border: 1px solid rgba(255,107,0,.28);
  pointer-events: none; opacity: 0; z-index: 0;
  transition: left 200ms var(--ease), width 200ms var(--ease), opacity var(--quick) var(--ease);
}
```

---

### 12.10 Formulario — reglas de implementación

```css
/* SIEMPRE width:100% en inputs dentro de grid */
.field input,
.field select {
  width: 100%;             /* obligatorio — sin esto, browsers móviles usan ancho intrínseco */
  box-sizing: border-box;  /* previene overflow con padding */
  min-height: 48px;        /* tap target WCAG */
}

/* .field es grid para label + input alineados */
.field { display: grid; gap: 6px; }

/* Label */
.field label {
  font-family: var(--mono); font-size: 11px;
  letter-spacing: .10em; text-transform: uppercase;
  color: var(--muted);
}
```

**Regla:** `width:100%` va en el selector global, no solo en media queries. Los replaced elements (`input`, `select`) no heredan el ancho de su contenedor grid automáticamente en todos los browsers.

---

### 12.11 Responsive — 3 tiers + gotchas críticos

#### Breakpoints

| Breakpoint | Trigger | Cambios principales |
|---|---|---|
| `≤900px` (tablet) | Hamburger nav | Hero stays 2-col; hero-actions wrappean; `min-width:0` en hero-grid children |
| `≤640px` (mobile) | Todo colapsa | Todos los grids → 1 col; frame-col sube (`order:-1`); botones full-width |

#### CSS completo

```css
@media (max-width:900px) {
  .nav-links, .nav .btn { display: none; }
  .menu-btn { display: inline-flex; }
  .hero-strip-wrap { flex-wrap: wrap; }
  .steps { grid-template-columns: 1fr 1fr; }

  /* Previene que botón ghost (nowrap ~340px) expanda la columna del hero */
  .hero-grid > * { min-width: 0; }
  .hero-actions { flex-wrap: wrap; }
  .hero-actions .btn { white-space: normal; }
}

@media (max-width:640px) {
  .hero-grid, .split, .bento, .cierre-grid, .producto-grid { grid-template-columns: 1fr; }
  .steps { grid-template-columns: 1fr; }
  .frame-col { order: -1; }   /* video sube al top del hero */

  /* min-width:0 en TODOS los grid children — regla universal */
  .hero-grid > *, .cierre-grid > *, .split > *, .bento > *, .producto-grid > * { min-width: 0; }

  /* Hero: padding vertical reducido */
  .hero-grid { padding-top: 48px; padding-bottom: 48px; gap: 24px; }

  /* Botones hero: full-width apilados */
  .hero-actions { flex-wrap: wrap; gap: 12px; }
  .hero-actions .btn { white-space: normal; text-align: center; width: 100%; }

  /* Kicker pill → badge en móvil */
  .kicker-pill { border-radius: 8px; display: inline-block; max-width: 100%; }

  /* Footer: apilado vertical */
  .foot-grid { flex-direction: column; }
}
```

#### Gotchas críticos (nunca repetir)

1. **`overflow-x:clip` vs `overflow-x:hidden`** — Solo `clip`. Ver §12.1.
2. **Shorthand `padding:A B` en elemento con `.wrap`** — Rompe el padding lateral. Usar `padding-top`/`padding-bottom`. Ver §12.1.
3. **`min-width:auto` en grid children** — Default de CSS Grid. Siempre agregar `min-width:0` a items que contengan texto largo o contenido de ancho variable.
4. **`white-space:nowrap` en flex items** — Un botón `nowrap` dentro de un grid col fuerza a la columna a expandirse más allá del viewport. Solo usar `nowrap` si la columna es suficientemente ancha en TODOS los breakpoints.
5. **`width:100%` en `<input>` y `<select>`** — No es opcional. Replaced elements no se estiran solos en grid/flex en browsers móviles.
6. **`frame-col{order:-1}` requiere que el padre sea flex o grid** — Funciona porque `.hero-grid` es `display:grid`. En otros contextos, verificar el display del padre antes de usar `order`.

---

### 12.12 Accesibilidad — implementación (WCAG 2.1 AA)

```html
<!-- Skip link: primer elemento del body -->
<a href="#main-content" class="skip-link">Saltar al contenido</a>

<!-- Nav como landmark -->
<nav aria-label="Navegación principal">

<!-- Main como landmark -->
<main id="main-content">
```

```css
.skip-link { position: absolute; top: -100%; left: 24px; }
.skip-link:focus { top: 0; }

/* Focus visible en todos los interactivos */
:focus-visible { outline: 2px solid var(--accent); outline-offset: 3px; }

/* Reduced motion */
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after { animation: none !important; transition: none !important; }
  .reveal, .reveal.in-view { opacity: 1; transform: none; transition: none; }
}
```

- `aria-expanded` en trigger del mobile menu y dropdown — actualizar vía JS en cada toggle.
- `aria-label` en `.menu-btn` — cambiar entre "Abrir menú" / "Cerrar menú".
- `aria-hidden="true"` en elementos decorativos (flecha `→`, frame-wrapper, cursores animados).
- `aspect-ratio:16/9` en `video` — reserva espacio antes de cargar (previene CLS).

---

### 12.13 Hero section — estructura completa

```html
<section class="hero" style="border-bottom:none; padding:0">
  <div class="wrap hero-grid">
    <!-- Columna texto (DOM primero, visual segundo en desktop) -->
    <div>
      <span class="kicker kicker-pill">...</span>
      <h1><span class="line1">Línea naranja.</span><br><span class="line2">Línea blanca.</span></h1>
      <p class="lede">...</p>
      <div class="hero-actions">
        <a href="#contacto" class="btn btn-primary">CTA primario</a>
        <a href="#producto" class="btn btn-ghost">CTA secundario <span aria-hidden="true">→</span></a>
      </div>
    </div>
    <!-- Columna frame (DOM segundo, visual segundo en desktop, PRIMERO en móvil por order:-1) -->
    <div class="frame-col">
      <div class="frame-label"><span class="rec-dot"></span>LIVE COMPANY BRAIN</div>
      <div class="frame-wrapper">...</div>
    </div>
  </div>
  <!-- Hero strip (fuera del grid) -->
  <div class="hero-strip">
    <div class="wrap hero-strip-wrap">
      <span>/ <strong>482 páginas</strong></span> ...
    </div>
  </div>
</section>
```

`padding:0` inline en la sección anula el `section{padding:clamp(64px,...)}` — el hero maneja su propio padding via `.hero-grid`.

---

---

### 12.14 Base styles y manejo de links

```css
/* Reset base */
*, *::before, *::after { margin: 0; padding: 0; box-sizing: border-box; }

/* Scroll + overflow */
html { scroll-behavior: smooth; overflow-x: clip; }  /* ver §12.1 */

/* Body */
body {
  background: var(--ink); color: var(--paper);
  font-family: var(--sans); font-size: 17px; line-height: 1.5;
  -webkit-font-smoothing: antialiased; letter-spacing: -0.01em;
}

/* Selection */
::selection { background: var(--accent); color: var(--ink); }

/* Links — herencia de color, sin subrayado por defecto */
a { color: inherit; text-decoration: none; }

/* Headings base */
h1, h2, h3, h4 { letter-spacing: -0.03em; line-height: 1.08; }

/* Párrafo — max-width global de legibilidad */
p { max-width: 68ch; }

/* Imagen responsive */
img { max-width: 100%; }

/* Focus ring universal */
:focus-visible { outline: 2px solid var(--accent); outline-offset: 3px; }
```

**Manejo de links — hover → naranja en todos los contextos:**

| Contexto | Selector |
|---|---|
| Nav principal | `.nav-links > li > a:hover { color: var(--accent) }` |
| Dropdown | `.dropdown li a:hover { color: var(--accent) }` |
| Mobile menu | `.mobile-menu-links > li > a:hover { color: var(--accent) }` |
| Mobile sub-links | `.mobile-menu-sub li a:hover { color: var(--accent) }` |
| Footer | `.foot-links a:hover { color: var(--accent) }` |

Regla general: **cualquier link sobre fondo oscuro hace hover a `var(--accent)`**. No hay links con underline en la web. Los CTAs (`.btn`, `.card-cta`) tienen su propio tratamiento de hover (ver §12.3).

---

### 12.15 Logo wordmark

```css
.logo {
  font-family: var(--mono);
  font-weight: 700;
  letter-spacing: 0;
  white-space: nowrap;
  font-size: 19px;
  color: var(--paper);        /* texto base blanco */
}
.logo .a { color: var(--accent); }   /* el slash "/" y el punto "." son naranja */
```

HTML: `<a class="logo"><span class="a">/</span>syncon<span class="a">.</span>solutions</a>`

El wordmark es el logo — no hay imagen SVG en el header. El SVG existe como asset (`/assets/logo/*.svg`) para otros medios. En la web, el wordmark es texto Geist Mono puro.

---

### 12.16 Dropdown de navegación

```css
/* Contenedor del ítem con dropdown */
.has-dropdown { position: relative; }
/* Bridge invisible para que el mouse no pierda el dropdown al salir del link */
.has-dropdown::after { content:''; position:absolute; top:100%; left:0; right:0; height:12px; }

/* Panel del dropdown */
.dropdown {
  display: none; position: absolute; top: calc(100% + 8px); left: 0;
  background: var(--bg-2); border: 1px solid var(--border);
  border-radius: var(--r-md); min-width: 220px;
  padding: var(--s2) 0; list-style: none; z-index: 100;
}
.has-dropdown:hover .dropdown,
.has-dropdown:focus-within .dropdown { display: block; }

/* Items del dropdown */
.dropdown li a { display:block; padding: var(--s3) var(--s6); font-size:14px; color:var(--fg-2); }
.dropdown li a:hover { color: var(--accent); }

/* Dropdown cursor (floating pill — mismo patrón que nav-cursor) */
#dropdown-cursor {
  position: absolute; left: 6px; right: 6px;
  border-radius: var(--r-md); background: rgba(255,107,0,.08);
  border: 1px solid rgba(255,107,0,.28);
  pointer-events: none; opacity: 0; z-index: 0;
  transition: top 200ms var(--ease), height 200ms var(--ease), opacity var(--quick) var(--ease);
}
```

**aria-expanded:** el trigger `<a aria-haspopup="true" aria-expanded="false">` se actualiza via JS en mouseenter/focusin → `"true"`, en mouseleave/focusout → `"false"`.

---

### 12.17 Mobile menu — CSS + JS completo

```css
/* Menú cerrado por defecto */
.mobile-menu { display: none; background: var(--bg-2); border-bottom: 1px solid var(--border); }
.mobile-menu.open { display: block; }

.mobile-menu-inner { padding: var(--s4) 0 var(--s8); }
.mobile-menu-links { list-style: none; }
.mobile-menu-links > li > a {
  display: block; padding: var(--s4) 0; color: var(--fg-2);
  font-size: 17px; border-bottom: 1px solid rgba(255,255,255,.06);
}
.mobile-menu-links > li > a:hover { color: var(--accent); }

.mobile-menu-sub { list-style: none; padding: var(--s2) 0 var(--s2) var(--s6); }
.mobile-menu-sub li a {
  display: block; padding: var(--s3) 0; color: var(--muted);
  font-size: 15px; border-bottom: 1px solid rgba(255,255,255,.04);
}
.mobile-menu-sub li a:hover { color: var(--accent); }

/* CTA en mobile menu — pill completo */
.mobile-menu-cta { margin-top: var(--s6); display: block; text-align: center; border-radius: var(--r-full); }

/* Botón hamburger */
.menu-btn {
  display: none;   /* visible solo en ≤900px */
  background: none; border: 1px solid var(--border); border-radius: var(--r-sm);
  color: var(--paper); min-height: 44px; min-width: 44px;
  font-size: 18px; cursor: pointer;
}
.menu-btn:hover { border-color: var(--accent); color: var(--accent); }
```

**JS pattern:**
```js
var btn = document.querySelector('.menu-btn');
var menu = document.getElementById('mobile-menu');
btn.addEventListener('click', function(){
  var isOpen = menu.classList.toggle('open');
  btn.setAttribute('aria-expanded', isOpen);
  menu.setAttribute('aria-hidden', !isOpen);
  btn.textContent = isOpen ? '✕' : '≡';
  btn.setAttribute('aria-label', isOpen ? 'Cerrar menú' : 'Abrir menú');
});
// Cierre en links del menú y tecla Escape
menu.querySelectorAll('a').forEach(function(link){ link.addEventListener('click', close); });
document.addEventListener('keydown', function(e){ if(e.key==='Escape') close(); });
```

---

### 12.18 Hero — fondo decorativo

El hero tiene 2 pseudo-elementos decorativos — ninguno es visible conscientemente, pero establecen la atmósfera:

```css
/* Grid sutil de fondo — visible solo desde el lado izquierdo via mask */
.hero::before {
  content: "";
  position: absolute; inset: 0;
  background-image:
    linear-gradient(var(--bg-2) 1px, transparent 1px),
    linear-gradient(90deg, var(--bg-2) 1px, transparent 1px);
  background-size: 48px 48px;
  opacity: .16;
  pointer-events: none;
  mask-image: radial-gradient(circle at 30% 25%, #000, transparent 75%);
}

/* Glow naranja ambiental — ellipse en el cuadrante superior izquierdo */
.hero::after {
  content: "";
  position: absolute; inset: 0;
  background: radial-gradient(ellipse 35% 28% at 20% 38%, rgba(255,107,0,.04) 0%, transparent 68%);
  pointer-events: none; z-index: 0;
}
```

Ambos requieren `position:relative` en `.hero` y que el content del hero tenga `position:relative;z-index:1` para quedar por encima.

---

### 12.19 Frame del Company Brain — corners + label + video

```css
/* Wrapper del frame */
.frame-wrapper {
  position: relative; border-radius: var(--r-md); overflow: hidden;
  border: 1px solid rgba(255,107,0,.28);
  background: var(--ink);
  box-shadow: 0 0 40px rgba(255,107,0,.28),
              0 0 100px rgba(255,107,0,.16),
              0 0 260px rgba(255,107,0,.09);
}

/* Corner markers — esquinas naranja */
.corner { position: absolute; width: 22px; height: 22px; z-index: 3; pointer-events: none; }
.corner.tl { top:-1px; left:-1px;  border-top:2px solid var(--accent); border-left:2px solid var(--accent); }
.corner.tr { top:-1px; right:-1px; border-top:2px solid var(--accent); border-right:2px solid var(--accent); }
.corner.bl { bottom:-1px; left:-1px;  border-bottom:2px solid var(--accent); border-left:2px solid var(--accent); }
.corner.br { bottom:-1px; right:-1px; border-bottom:2px solid var(--accent); border-right:2px solid var(--accent); }

/* Video */
.frame-wrapper video { width:100%; height:auto; display:block; border-radius:var(--r-md); aspect-ratio:16/9; }

/* Columna del frame */
.frame-col { display:flex; flex-direction:column; gap:var(--s3); }

/* Label superior: LIVE COMPANY BRAIN */
.frame-label {
  display: inline-flex; align-items: center; gap: 6px;
  font-family: var(--mono); font-size: 11px; letter-spacing: .10em;
  color: var(--muted); text-transform: uppercase; align-self: flex-start;
}

/* Rec dot — pulsante naranja (frame label y kicker-pill) */
.rec-dot {
  width: 6px; height: 6px; border-radius: 50%;
  background: var(--accent); flex-shrink: 0;
  animation: pulse-dot 1.5s ease-in-out infinite;
}
```

**Video fallback JS:** si el video falla (`video.addEventListener('error', ...)`) → `video.style.display='none'` + muestra `.console` (terminal animado).

---

### 12.20 Hero strip (barra de stats)

La hero strip vive FUERA del grid, separada por un border-top, dentro de la sección hero:

```css
.hero-strip {
  border-top: 1px solid var(--bg-2);
  padding: var(--s3) 0;
  font-family: var(--mono); font-size: 13px;
  color: var(--muted); letter-spacing: .02em;
}
.hero-strip strong { color: var(--fg-2); font-weight: 500; }
.hero-strip .slash { color: var(--accent); }

/* Desktop: distribuido con space-between */
.hero-strip-wrap { display: flex; justify-content: space-between; align-items: center; }

/* Tablet/móvil: wrappea y alinea al inicio */
@media (max-width:900px) {
  .hero-strip-wrap { flex-wrap: wrap; gap: var(--s2) var(--s6); justify-content: flex-start; }
}
```

HTML pattern: `<span><span class="slash">/</span>&nbsp;<strong>482 páginas</strong></span>`

---

### 12.21 Big-quote (sección dolor)

```css
.big-quote {
  font-size: clamp(26px,3.6vw,44px);
  font-weight: 700;
  letter-spacing: -0.03em;
  line-height: 1.12;
  max-width: 18ch;    /* restricción de ancho para crear tensión visual */
}
```

Usado en la sección `#dolor`: la columna izquierda es una frase corta y contundente. La derecha es el copy largo. Esta asimetría es intencional y explica por qué `.split` usa `.85fr 1.15fr`.

---

### 12.22 Tiles y receipts (datos de prueba)

```css
/* Grid de tiles pequeños */
.tiles { display:grid; grid-template-columns:repeat(auto-fit,minmax(220px,1fr)); gap:var(--s4); margin-top:var(--s8); }

/* Tile pequeño (receipts grid) */
.tile { background:var(--bg-2); border:1px solid rgba(255,107,0,.25); border-radius:var(--r-md); padding:var(--s6); }
.tile .num { font-family:var(--mono); font-weight:700; font-size:clamp(28px,3.4vw,40px); color:var(--paper); line-height:1; }
.tile .num.am { color:var(--accent); }        /* modificador: número en naranja */
.tile .lbl { font-family:var(--mono); font-size:11px; text-transform:uppercase; letter-spacing:.1em; color:var(--fg-2); margin-top:var(--s3); }
.tile .date { font-family:var(--mono); font-size:11px; color:var(--muted); margin-top:var(--s2); }

/* Tile-stack — columna de tiles apilados (producto+receipts) */
.tile-stack { display:flex; flex-direction:column; flex:1; justify-content:space-between; }

/* Tile grande (tile-lg) — num grande + meta a la derecha */
.tile-lg { background:var(--bg-2); border:1px solid rgba(255,107,0,.25); border-radius:var(--r-md); padding:var(--s6) var(--s8); display:flex; align-items:center; gap:var(--s8); transition:border-color var(--quick) var(--ease),box-shadow var(--quick) var(--ease); }
.tile-lg:hover { border-color:var(--accent); box-shadow:0 0 24px rgba(255,107,0,.22),0 0 64px rgba(255,107,0,.08); }
.tile-lg .num { font-family:var(--mono); font-weight:700; font-size:clamp(30px,3.8vw,50px); color:var(--paper); line-height:1; flex-shrink:0; white-space:nowrap; min-width:2.8ch; }
.tile-lg .num.am { color:var(--accent); }
.tile-lg .meta { display:flex; flex-direction:column; gap:var(--s2); }
.tile-lg .lbl { font-family:var(--mono); font-size:12px; text-transform:uppercase; letter-spacing:.1em; color:var(--fg-2); }
.tile-lg .date { font-family:var(--mono); font-size:11px; color:var(--muted); }
```

**Modificador `.am`:** aplica `color:var(--accent)` al número. Se usa cuando el dato es un logro propio de SYNCON destacable (482, 83.3%, etc.).

---

### 12.23 Bento cards — sub-componentes

```css
/* Card base del bento */
.card { background:var(--bg-2); border:1px solid var(--border); border-radius:var(--r-md); padding:clamp(24px,3vw,40px); display:flex; flex-direction:column; transition:border-color var(--quick) var(--ease),box-shadow var(--quick) var(--ease); }
.card:hover { border-color:var(--accent); box-shadow:0 0 24px rgba(255,107,0,.22),0 0 64px rgba(255,107,0,.08); }

/* Tag de motor/producto (kicker dentro de la card) */
.card .tag { font-family:var(--mono); font-size:11px; text-transform:uppercase; letter-spacing:.1em; color:var(--accent); display:block; margin-bottom:var(--s3); }

/* H3 con subtítulo mono (diseñado a la medida / HAR) */
/* El subtítulo es un <span style="display:block;font-family:var(--mono);font-size:11px;..."> inline en el h3 */

/* Lista de features dentro de la card */
.card ul { list-style:none; margin-top:var(--s4); display:grid; gap:var(--s2); }
.card ul li { padding-left:18px; position:relative; color:var(--fg-2); font-size:17px; }
.card ul li::before { content:"▸"; position:absolute; left:0; color:var(--accent); } /* marcador triángulo naranja */

/* Wrap del CTA al fondo de la card */
.card-cta-wrap { margin-top:auto; padding-top:var(--s8); }   /* margin-top:auto ancla al fondo */
```

---

### 12.24 Steps — sub-componentes

```css
.step { border-top:2px solid var(--accent); padding-top:var(--s6); display:flex; flex-direction:column; }
.step .n { font-family:var(--mono); font-size:12px; color:var(--accent); letter-spacing:.1em; }   /* "Diagnóstico" */
.step h4 { font-size:clamp(20px,2.2vw,26px); font-weight:700; color:var(--paper); margin:var(--s3) 0 var(--s3); letter-spacing:-0.02em; }
.step .step-sub { font-family:var(--mono); font-size:11px; color:var(--accent); letter-spacing:.08em; text-transform:uppercase; }   /* "ROI antes de comprometerse" */
.step p { font-size:17px; color:var(--fg-2); margin-top:auto; padding-top:var(--s8); line-height:1.6; }
/* margin-top:auto en .step p ancla el body-copy al fondo, alineando los párrafos entre columnas */
```

---

### 12.25 Pills de enemigos

Las pill-tags de la sección `#enemigos` son distintas del kicker-pill del hero:

```css
/* Contenedor */
.pills { display:flex; flex-wrap:wrap; gap:var(--s3); margin-top:var(--s6); }

/* Pill individual — borde LLENO naranja (no tenue) */
.pill {
  font-family: var(--mono); font-size:13px;
  padding: 8px 14px;
  border: 1px solid var(--accent);         /* borde naranja sólido — más agresivo que kicker-pill */
  color: var(--paper);
  border-radius: var(--r-full);
  background: rgba(255,107,0,.06);
}
```

**Diferencia clave vs. kicker-pill:** el `.pill` usa `border:1px solid var(--accent)` (naranja sólido completo). El `.kicker-pill` usa `border:1px solid rgba(255,107,0,.28)` (naranja tenue). Los pills de enemigos son más agresivos — están listando lo que SYNCON rechaza.

---

### 12.26 Who grid

```css
.who { display:grid; grid-template-columns:repeat(auto-fit,minmax(240px,1fr)); gap:var(--s6); margin-top:var(--s8); }
.who div { border-top:2px solid var(--accent); padding-top:var(--s6); }
.who div h4 { font-family:var(--mono); font-size:13px; color:var(--accent); text-transform:uppercase; letter-spacing:.08em; margin-bottom:var(--s3); }
.who div p { font-size:17px; color:var(--fg-2); }
```

Mismo patrón que `.step` (border-top naranja 2px + padding) pero en auto-fit para escalar con el número de perfiles. El h4 es mono + accent (como los step `.n`).

---

### 12.27 FAQ accordion (details/summary)

Usa HTML nativo `<details>/<summary>` — sin JS, sin dependencias:

```css
.faq { max-width: 820px; }   /* limita el ancho de las preguntas para legibilidad */
details { border-bottom: 1px solid var(--bg-2); }
summary {
  cursor: pointer; list-style: none;
  padding: var(--s6) 0;
  font-size: clamp(17px,2vw,20px); font-weight: 600;
  display: flex; justify-content: space-between; gap: 16px; align-items: center;
}
summary::-webkit-details-marker { display: none; }   /* elimina triángulo nativo */
summary::after { content: "+"; font-family:var(--mono); color:var(--accent); font-size:24px; transition:transform var(--quick) var(--ease); }
details[open] summary::after { content: "–"; }           /* cambia + a – cuando abierto */
details[open] summary { color: var(--accent); }           /* pregunta se vuelve naranja cuando abierta */
details p { padding: 0 0 var(--s6); color:var(--fg-2); font-size:17px; }
```

`details[open]` es estado nativo del browser — no requiere JS. El indicador `+`/`–` está en `::after`, CSS puro.

---

### 12.28 Footer

```css
footer { padding: var(--s16) 0 var(--s12); }  /* s16=64px, s12=48px */

.foot-grid {
  display: flex; justify-content: space-between;
  gap: var(--s8); flex-wrap: wrap; align-items: flex-start;
}
.foot-grid .tagline { font-family:var(--mono); color:var(--muted); font-size:13px; margin-top:var(--s4); max-width:30ch; }

.foot-links { display: flex; gap: var(--s12); flex-wrap: wrap; }
.foot-links h5 { font-family:var(--mono); font-size:11px; text-transform:uppercase; letter-spacing:.1em; color:var(--muted); margin-bottom:var(--s4); }
.foot-links a { display:block; color:var(--fg-2); font-size:14px; padding:5px 0; }
.foot-links a:hover { color: var(--accent); }

.legal { margin-top:var(--s12); padding-top:var(--s6); border-top:1px solid var(--bg-2); font-family:var(--mono); font-size:12px; color:var(--muted); }
```

**Responsive footer:**
```css
@media (max-width:640px) {
  .foot-grid { flex-direction: column; gap: var(--s6); }
  .foot-links { gap: var(--s6); }
  .foot-links a { overflow-wrap: break-word; }  /* emails largos no rompen layout */
}
```

Estructura HTML: logo + tagline (col izquierda) / 3 grupos de links (col derecha): Productos · La empresa · Contacto. El email y el LinkedIn están en la columna Contacto.

---

### 12.29 Reveal animation — CSS + JS completo

```css
/* Estado inicial: invisible y desplazado 20px hacia abajo */
.reveal { opacity: 0; transform: translateY(20px); transition: opacity .6s var(--ease), transform .6s var(--ease); }
/* Estado final: visible y en posición */
.reveal.in-view { opacity: 1; transform: none; }
```

```js
/* IntersectionObserver — evita que los elementos queden invisible en pestañas ocultas al cargar */
(function(){
  var reduce = matchMedia('(prefers-reduced-motion:reduce)').matches;
  if(reduce){
    document.querySelectorAll('.reveal').forEach(function(el){ el.classList.add('in-view'); });
    return;
  }
  var obs = new IntersectionObserver(function(entries){
    entries.forEach(function(e){
      if(!e.isIntersecting) return;
      var el = e.target;
      el.style.transitionDelay = el.dataset.delay || '0s';  /* stagger via data-delay=".1s" */
      el.classList.add('in-view');
      obs.unobserve(el);  /* una vez visible, deja de observar */
    });
  }, { threshold: 0.08 });
  document.querySelectorAll('.reveal').forEach(function(el){ obs.observe(el); });
})();
```

**Stagger:** `data-delay=".05s"` / `".1s"` / `".2s"` / `".3s"` etc. en el elemento HTML. Nunca usar CSS `animation-delay` — no respeta `prefers-reduced-motion` correctamente.

**Por qué IntersectionObserver y no CSS animation + JS clase:** las CSS animations se pausan en pestañas ocultas pero el estado inicial `opacity:0` persiste, por lo que al volver a la pestaña el elemento puede quedar invisible. IO + CSS transition evita esto.

---

### 12.30 `.frame-static` — composición visual hero sin video

**Decisión:** Componer hero-frames sin video usando tabla/log mono. Reutilizable en cualquier página donde el visual del hero deba comunicar un patrón (proceso descubierto, agenda, jerarquía) sin reclamar data específica.
**Fuente:** Subpáginas de producto 2026-06-30 (`/productos/consultoria` y `/productos/capacitacion`).
**Razón:** Receipts vivos son solo para HAR (Company Brain dogfooding). Pilares sin data robusta requieren composición visual que enseñe sin reclamar.

```css
.frame-static {
  border: 1px solid var(--border);
  background: var(--ink);
  padding: var(--s8) var(--s6);
  border-radius: var(--r-md);
  font-family: var(--sans);
  font-size: 14px;
  color: var(--fg-2);
  display: flex; flex-direction: column;
  gap: var(--s3);
  transition: border-color var(--default) var(--ease),
              box-shadow var(--default) var(--ease);
}
.frame-static:hover {
  border-color: rgba(255,107,0,.4);
  box-shadow: 0 0 24px rgba(255,107,0,.12);
}
.frame-static-head,
.frame-static-row,
.frame-static-foot {
  display: grid; gap: var(--s4);
  align-items: baseline;
  padding-bottom: var(--s3);
  border-bottom: 1px dashed rgba(255,255,255,.06);
}
.frame-static--consultoria .frame-static-head,
.frame-static--consultoria .frame-static-row,
.frame-static--har .frame-static-head,
.frame-static--har .frame-static-row {
  grid-template-columns: 1.4fr 1fr 1fr;
}
.frame-static--capacitacion .frame-static-head { grid-template-columns: 1fr 1fr; }
.frame-static--capacitacion .frame-static-row { grid-template-columns: auto 1fr auto; }
.frame-static-foot {
  border-bottom: none; padding-top: var(--s3); margin-top: auto;
  color: var(--muted);
}
.mono-label {
  font-family: var(--mono); font-size: 11px; font-weight: 400;
  text-transform: uppercase; letter-spacing: .14em;
  color: var(--accent);
}
.mono-label.muted { color: var(--muted); }
.frame-static-row .mono { font-family: var(--mono); }
.frame-static-row .accent {
  color: var(--accent); font-family: var(--mono); font-size: 13px;
}
@media (max-width: 640px) {
  .frame-static { padding: var(--s6) var(--s4); font-size: 13px; }
  .frame-static--consultoria .frame-static-head,
  .frame-static--consultoria .frame-static-row {
    grid-template-columns: 1fr 1fr;
  }
  .frame-static--consultoria .frame-static-row > :nth-child(3) {
    grid-column: 1 / -1;
  }
}
```

**Accesibilidad:** elementos con grid de datos deben llevar `role="img"` + `aria-label` descriptivo. Variantes con `--{pilar}` cambian solo el grid-template, no la apariencia base.

---

### 12.31 `.form-divider` + `.calendly-link` — conversión dual form + Calendly

**Decisión:** El form `#contacto` puede ofrecer una segunda vía de conversión (Calendly directo) sin competir con el primary CTA. Usar `.form-divider` ("o" entre form y link) + `.calendly-link` (ghost pill 14px).
**Fuente:** Subpáginas de producto 2026-06-30.
**Razón:** Form-first preserva qualification (3 campos visibles + Dolor pre-cargado oculto). Calendly fallback rescata high-intent sin sacrificar data. Patrón Linear/Stripe.

```css
.form-divider {
  display: flex; align-items: center; gap: var(--s4);
  margin: var(--s8) 0;
  font-family: var(--mono); font-size: 11px;
  color: var(--muted); text-transform: uppercase;
  letter-spacing: .14em;
}
.form-divider::before, .form-divider::after {
  content: ""; flex: 1; height: 1px; background: var(--border);
}
.calendly-link {
  display: flex; align-items: center; justify-content: center;
  gap: var(--s3); width: 100%;
  font-family: var(--sans); font-size: 16px; font-weight: 600;
  color: var(--paper); text-decoration: none;
  padding: var(--s4) var(--s5);
  border: 1px solid rgba(255,107,0,.35);
  background: rgba(255,107,0,.04);
  border-radius: var(--r-full);
  transition: color var(--default) var(--ease),
              border-color var(--default) var(--ease),
              background var(--default) var(--ease);
  min-height: 48px;
}
.calendly-link:hover {
  color: var(--accent); border-color: var(--accent);
  background: rgba(255,107,0,.08);
}
.calendly-link:hover .arrow { transform: translateX(2px); }
.calendly-link .cal-icon { color: var(--accent); flex-shrink: 0; }
.arrow { transition: transform var(--quick) var(--ease); display: inline-block; }
.calendly-microcopy {
  display: block; text-align: center; margin-top: var(--s3);
  font-family: var(--mono); font-size: 11px;
  color: var(--muted); letter-spacing: .12em; text-transform: uppercase;
}
```

**Estructura HTML (canónica para subpáginas de producto):**

```html
<a class="calendly-link" href="..." target="_blank" rel="noopener" data-pilar="...">
  <svg class="cal-icon" width="18" height="18" viewBox="0 0 24 24" fill="none"
       stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
    <rect x="3" y="4" width="18" height="18" rx="2" ry="2"/>
    <line x1="16" y1="2" x2="16" y2="6"/>
    <line x1="8" y1="2" x2="8" y2="6"/>
    <line x1="3" y1="10" x2="21" y2="10"/>
  </svg>
  Agenda 30 minutos directo
  <span class="arrow">→</span>
</a>
<span class="calendly-microcopy">30 min · sin formulario · sin compromiso</span>
```

**Accesibilidad:**
- Divider con `role="separator" aria-label="o"`.
- Link Calendly con `target="_blank" rel="noopener"` + atributo `data-pilar` (analytics futuras).
- Icono SVG con `aria-hidden="true"` (decorativo; el texto "Agenda 30 minutos directo" comunica la acción).

**Versión v1.1 (2026-06-30):** El diseño inicial usaba `display:inline-flex` + ancho ajustado al contenido + color `--fg-2` (gris) + border `--border` (gris). Resultado: el botón quedaba diminuto al lado del primary CTA (full-width) y se perdía visualmente. Fix: `width:100%` + `min-height:48px` (match `.btn`) + texto en `--paper` + border `rgba(accent,.35)` + bg sutil `rgba(accent,.04)` + icono calendario en `--accent` + microcopy mono "30 min · sin formulario · sin compromiso". Mantiene jerarquía (sigue siendo segundario) pero ahora se PRESENTA con suficiente peso para no perderse.

**Por qué `var(--s5)` y no token estándar:** `--s5` es derivado de la escala 4-8-12-16-20-24-32... La pill Calendly usa 20px de padding horizontal (intermedio entre s4=16 y s6=24). Si tu hoja de tokens no tiene `--s5`, añadirlo: `--s5:20px;`.

---

## 13. Esqueleto HTML — plantilla de página web

> Copiar este archivo como punto de partida para cualquier página nueva. No inventa ningún estilo ni estructura — todo apunta a §12. El objetivo es que quien construya la página no tenga que leer nada más para saber QUÉ va dónde.

```html
<!DOCTYPE html>
<html lang="es-CO">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">

  <!-- TÍTULO: "SYNCON · [Tema de la página] · Ingeniería contextual" -->
  <title>SYNCON · [Tema] · Ingeniería contextual</title>
  <!-- DESCRIPCIÓN: 150-160 chars. Incluir "ingeniería contextual" y "LATAM". Sin exclamaciones. -->
  <meta name="description" content="[Descripción]">

  <!-- OG / Social — para LinkedIn y WhatsApp (ver §14 para LinkedIn) -->
  <meta property="og:title"       content="SYNCON · [Tema]">
  <meta property="og:description" content="[Descripción]">
  <meta property="og:image"       content="/assets/og-syncon.png">
  <meta property="og:type"        content="website">
  <meta property="og:locale"      content="es_CO">

  <!-- FONTS: Geist + Geist Mono — siempre Google Fonts CDN, mismo bloque -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Geist:wght@400;500;600;700;800&family=Geist+Mono:wght@400;500;700&display=swap" rel="stylesheet">

  <style>
  /* ─── TOKENS (§12 — no modificar nunca) ─────────────────────────────── */
  :root{
    --ink:#0A0A0A; --bg-2:#1A1A1A; --border:#444444; --muted:#888888;
    --fg-2:#CCCCCC; --surface-100:#F2F2F2; --paper:#FAFAFA;
    --accent:#FF6B00; --accent-hover:#FF8833; --accent-pressed:#CC5500;
    --agent-ceo:#00E5FF; --agent-coo:#FFB300; --agent-cto:#00E676;
    --sans:'Geist',-apple-system,BlinkMacSystemFont,'Inter',sans-serif;
    --mono:'Geist Mono','JetBrains Mono',ui-monospace,monospace;
    --s1:4px;--s2:8px;--s3:12px;--s4:16px;--s6:24px;--s8:32px;--s12:48px;--s16:64px;
    --r-sm:2px;--r-md:8px;--r-full:99px;
    --quick:150ms;--default:200ms;--ease:cubic-bezier(0.2,0,0,1);
    --maxw:1240px;
  }

  /* ─── BASE (§12.14) ──────────────────────────────────────────────────── */
  /* [copiar base styles de §12.14] */

  /* ─── COMPONENTES OBLIGATORIOS EN TODAS LAS PÁGINAS ─────────────────── */
  /* wrap / overflow        → §12.1  */
  /* section padding        → §12.2  */
  /* skip-link              → §12.12 */
  /* logo wordmark          → §12.15 */
  /* botones (.btn)         → §12.3  */
  /* header / nav sticky    → §12.9  */
  /* nav cursor + dropdown  → §12.16 */
  /* mobile menu            → §12.17 */
  /* reveal animation       → §12.29 */
  /* footer                 → §12.28 */
  /* responsive 3 tiers     → §12.11 */
  /* reduced-motion         → §12.12 */

  /* ─── COMPONENTES SEGÚN SECCIONES DE ESTA PÁGINA ────────────────────── */
  /* hero (si aplica)       → §12.13, §12.18, §12.19, §12.20 */
  /* kicker-pill            → §12.8  */
  /* grids de contenido     → §12.5  */
  /* cards / bento          → §12.7, §12.23 */
  /* steps                  → §12.24 */
  /* tiles / receipts       → §12.22 */
  /* pills de enemigos      → §12.25 */
  /* who grid               → §12.26 */
  /* faq accordion          → §12.27 */
  /* formulario             → §12.10 */
  /* big-quote              → §12.21 */
  /* console / terminal     → §12.19 */
  </style>
</head>
<body>

<!-- ═══ 1. SKIP LINK — §12.12 — SIEMPRE primero en el body ═══════════════ -->
<a href="#main-content" class="skip-link">Saltar al contenido</a>


<!-- ═══ 2. HEADER + NAV — §12.9, §12.15, §12.16 ══════════════════════════ -->
<header id="hdr">
  <nav class="wrap nav" aria-label="Navegación principal">

    <!-- Logo wordmark — §12.15 — idéntico en todas las páginas -->
    <a href="/" class="logo" aria-label="/syncon.solutions inicio">
      <span class="a">/</span>syncon<span class="a">.</span>solutions
    </a>

    <!-- Links — §12.16. El #nav-cursor es el pill flotante de hover (JS) -->
    <ul class="nav-links">
      <li id="nav-cursor" aria-hidden="true"></li>
      <li class="has-dropdown">
        <a href="/productos" aria-haspopup="true" aria-expanded="false">Productos</a>
        <ul class="dropdown" role="menu">
          <li id="dropdown-cursor" aria-hidden="true"></li>
          <li role="none"><a href="/productos/har"          role="menuitem">Company Brain + HAR</a></li>
          <li role="none"><a href="/productos/consultoria"  role="menuitem">Consultoría contextual</a></li>
          <li role="none"><a href="/productos/capacitacion" role="menuitem">Capacitación</a></li>
        </ul>
      </li>
      <li><a href="/#metodo">Cómo trabajamos</a></li>
      <li><a href="/articulos">Artículos</a></li>
      <li><a href="/about">La firma</a></li>
      <li><a href="/#faq">FAQ</a></li>
    </ul>

    <!-- CTA nav — §12.3 — pill via .nav-cta .btn-primary -->
    <div class="nav-cta">
      <a href="/#contacto" class="btn btn-primary">Diagnosticar mi operación</a>
    </div>

    <!-- Hamburger — visible solo ≤900px — §12.17 -->
    <button class="menu-btn" aria-label="Abrir menú" aria-expanded="false" aria-controls="mobile-menu">≡</button>
  </nav>
</header>


<!-- ═══ 3. MOBILE MENU — §12.17 — idéntico en todas las páginas ══════════ -->
<div id="mobile-menu" class="mobile-menu" aria-hidden="true">
  <div class="wrap mobile-menu-inner">
    <ul class="mobile-menu-links">
      <li>
        <a href="/productos">Productos</a>
        <ul class="mobile-menu-sub">
          <li><a href="/productos/har">Company Brain + HAR</a></li>
          <li><a href="/productos/consultoria">Consultoría contextual</a></li>
          <li><a href="/productos/capacitacion">Capacitación</a></li>
        </ul>
      </li>
      <li><a href="/#metodo">Cómo trabajamos</a></li>
      <li><a href="/articulos">Artículos</a></li>
      <li><a href="/about">La firma</a></li>
      <li><a href="/#faq">FAQ</a></li>
    </ul>
    <a href="/#contacto" class="btn btn-primary mobile-menu-cta">Diagnosticar mi operación</a>
  </div>
</div>


<!-- ═══ 4. MAIN CONTENT ════════════════════════════════════════════════════ -->
<main id="main-content">

  <!-- ── HERO (opcional — solo si la página lo necesita) ──────────────────
       - Usar en: home, /productos, /about
       - No usar en: artículos individuales, /receipts, páginas de error
       - SIEMPRE con style="border-bottom:none;padding:0" inline — §12.13  -->
  <section class="hero" style="border-bottom:none;padding:0">
    <div class="wrap hero-grid">
      <!-- Columna texto: kicker → h1 → lede → actions (stagger via data-delay) -->
      <div>
        <span class="kicker kicker-pill reveal" data-delay=".05s">
          <span class="kicker-dot"></span>[Kicker — contexto de la página]
        </span>
        <h1 class="reveal" data-delay=".1s">
          <span class="line1">[Línea naranja — propuesta de valor.]</span><br>
          <span class="line2">[Línea blanca — complemento.]</span>
        </h1>
        <p class="lede reveal" data-delay=".2s">[Descripción 2-3 líneas. max-width:62ch automático.]</p>
        <div class="hero-actions reveal" data-delay=".3s">
          <a href="/#contacto" class="btn btn-primary">Diagnosticar mi operación</a>
          <a href="#[anchor]" class="btn btn-ghost">[CTA secundario] <span aria-hidden="true">→</span></a>
        </div>
      </div>
      <!-- Columna visual: frame / imagen / ilustración (sube al top en móvil via order:-1) -->
      <div class="frame-col reveal" data-delay=".35s">
        <!-- Opción A: video Company Brain — §12.19 -->
        <!--
        <div class="frame-label"><span class="rec-dot"></span>LIVE COMPANY BRAIN</div>
        <div class="frame-wrapper" aria-hidden="true">
          <span class="corner tl"></span><span class="corner tr"></span>
          <span class="corner bl"></span><span class="corner br"></span>
          <video autoplay muted loop playsinline>
            <source src="/assets/HAR-SynconSolutions.mp4" type="video/mp4">
          </video>
        </div>
        -->
        <!-- Opción B: imagen estática -->
        <!-- <img src="/assets/[imagen].webp" alt="[descripción]" width="640" height="360"> -->
      </div>
    </div>
    <!-- Hero strip (opcional) — §12.20 -->
    <!--
    <div class="hero-strip">
      <div class="wrap hero-strip-wrap">
        <span><span class="slash">/</span>&nbsp;<strong>[stat]</strong></span>
        ...
      </div>
    </div>
    -->
  </section>


  <!-- ── SECCIÓN ESTÁNDAR ───────────────────────────────────────────────────
       - id único obligatorio (ancla de nav)
       - border-bottom:1px solid var(--bg-2) viene de section{} — NO agregar
       - Fondo por defecto: --ink. Fondo elevado: agregar class="cierre" (bg-2)
       - H2 bicolor con kicker fusionado — §11.3             -->
  <section id="[nombre]">
    <div class="wrap">
      <h2 style="font-size:clamp(28px,3.6vw,40px);font-weight:800;letter-spacing:-0.04em;line-height:1.06;margin-bottom:var(--s8)">
        <span style="display:block;font-family:var(--mono);font-size:11px;font-weight:400;color:var(--accent);letter-spacing:.14em;text-transform:uppercase;margin-bottom:var(--s3)">[KICKER MONO UPPERCASE]</span>
        <span style="display:block;color:var(--paper)">[Título principal blanco]</span>
        <span style="display:block;color:var(--accent)">[Remate naranja.]</span>
      </h2>

      <!-- Elegir el grid apropiado según el contenido — §12.5:
           Texto larg + cuerpo extenso  →  .split (.85fr 1.15fr)
           2 cards de igual peso        →  .bento (1fr 1fr)
           Texto + tiles de datos       →  .producto-grid (1fr 1fr)
           Pasos de metodología         →  .steps (repeat(3,1fr))
           Perfiles / quiénes somos     →  .who (auto-fit minmax 240px)
           Texto + formulario           →  .cierre-grid (1fr 1fr)   -->

    </div>
  </section>


  <!-- ── SECCIÓN DE CIERRE / CONTACTO ──────────────────────────────────────
       - SIEMPRE la última sección antes del footer
       - bg-2 via class="cierre"
       - style="border-bottom:none" para no separar del footer   -->
  <section id="contacto" class="cierre" style="border-bottom:none">
    <div class="wrap cierre-grid">
      <!-- Col izquierda: h2 + lede + trust list -->
      <div>
        <h2>...</h2>
      </div>
      <!-- Col derecha: formulario — §12.10 -->
      <div id="form-container">
        <form class="form" id="form-diagnostico" name="diagnostico" method="POST" action="#">
          <!-- fields: nombre / empresa / email / dolor (select) -->
          <!-- submit: class="btn btn-primary" style="width:100%" — r-sm (NO pill) -->
        </form>
      </div>
    </div>
  </section>

</main>


<!-- ═══ 5. FOOTER — §12.28 — idéntico en todas las páginas ══════════════ -->
<footer>
  <div class="wrap">
    <div class="foot-grid">
      <div>
        <a href="/" class="logo"><span class="a">/</span>syncon<span class="a">.</span>solutions</a>
        <p class="tagline">Nativos en IA. Veteranos en industria.</p>
      </div>
      <div class="foot-links">
        <div>
          <h5>Productos</h5>
          <a href="/productos/har">Company Brain + HAR</a>
          <a href="/productos/consultoria">Consultoría contextual</a>
          <a href="/productos/capacitacion">Capacitación</a>
        </div>
        <div>
          <h5>La empresa</h5>
          <a href="/#metodo">Cómo trabajamos</a>
          <a href="/about">La firma</a>
          <a href="/articulos">Artículos</a>
          <a href="/#faq">FAQ</a>
        </div>
        <div>
          <h5>Contacto</h5>
          <a href="/#contacto">Diagnóstico</a>
          <a href="mailto:lorena@syncon.solutions">lorena@syncon.solutions</a>
          <a href="https://www.linkedin.com/company/syncon-solutions" target="_blank" rel="noopener noreferrer">LinkedIn</a>
        </div>
      </div>
    </div>
    <div class="legal">SYNCON Solutions S.A.S. · Bogotá, Colombia · Firma latinoamericana de ingeniería contextual · © 2026</div>
  </div>
</footer>


<!-- ═══ 6. JS BLOCKS — siempre al final del body, en este orden ══════════

  OBLIGATORIOS en todas las páginas:
  1. Reveal / IntersectionObserver    → §12.29
  2. Header scroll (.scrolled)        → §12.9
  3. Nav cursor + dropdown aria       → §12.16
  4. Mobile menu                      → §12.17

  OPCIONALES — incluir solo si la sección existe:
  5. Video HAR + fallback al terminal → §12.19  (solo con .frame-wrapper video)
  6. Form submit handler              → §12.10  (solo con #form-diagnostico)
  7. Terminal animado                 → §12.19  (solo si el video falla)

═══════════════════════════════════════════════════════════════════════════ -->

<!-- JS 1: Reveal -->
<script>
(function(){
  var reduce=matchMedia('(prefers-reduced-motion:reduce)').matches;
  if(reduce){document.querySelectorAll('.reveal').forEach(function(el){el.classList.add('in-view');});return;}
  var obs=new IntersectionObserver(function(entries){
    entries.forEach(function(e){
      if(!e.isIntersecting)return;
      var el=e.target;
      el.style.transitionDelay=el.dataset.delay||'0s';
      el.classList.add('in-view');
      obs.unobserve(el);
    });
  },{threshold:0.08});
  document.querySelectorAll('.reveal').forEach(function(el){obs.observe(el);});
})();
</script>

<!-- JS 2: Header scroll -->
<script>
const hdr=document.getElementById('hdr');
const onScroll=()=>hdr.classList.toggle('scrolled',window.scrollY>24);
addEventListener('scroll',onScroll,{passive:true});onScroll();
</script>

<!-- JS 3: Nav cursor + dropdown aria -->
<script>
(function(){
  var nl=document.querySelector('.nav-links');
  var cursor=document.getElementById('nav-cursor');
  if(nl&&cursor){
    nl.querySelectorAll(':scope>li:not(#nav-cursor)').forEach(function(item){
      item.addEventListener('mouseenter',function(){
        cursor.style.left=item.offsetLeft+'px';
        cursor.style.width=item.offsetWidth+'px';
        cursor.style.opacity='1';
      });
    });
    nl.addEventListener('mouseleave',function(){cursor.style.opacity='0';});
  }
  var dropTrigger=document.querySelector('.has-dropdown>a');
  var dropContainer=document.querySelector('.has-dropdown');
  var dl=document.querySelector('.dropdown');
  var dc=document.getElementById('dropdown-cursor');
  if(dl&&dc){
    dl.querySelectorAll('li:not(#dropdown-cursor)').forEach(function(item){
      item.addEventListener('mouseenter',function(){
        dc.style.top=item.offsetTop+'px';
        dc.style.height=item.offsetHeight+'px';
        dc.style.opacity='1';
      });
    });
    dl.addEventListener('mouseleave',function(){dc.style.opacity='0';});
  }
  if(dropTrigger&&dropContainer){
    dropContainer.addEventListener('mouseenter',function(){dropTrigger.setAttribute('aria-expanded','true');});
    dropContainer.addEventListener('mouseleave',function(){dropTrigger.setAttribute('aria-expanded','false');});
    dropContainer.addEventListener('focusin',function(){dropTrigger.setAttribute('aria-expanded','true');});
    dropContainer.addEventListener('focusout',function(e){if(!dropContainer.contains(e.relatedTarget))dropTrigger.setAttribute('aria-expanded','false');});
  }
})();
</script>

<!-- JS 4: Mobile menu -->
<script>
(function(){
  var btn=document.querySelector('.menu-btn');
  var menu=document.getElementById('mobile-menu');
  if(!btn||!menu)return;
  function close(){
    menu.classList.remove('open');
    btn.setAttribute('aria-expanded','false');
    menu.setAttribute('aria-hidden','true');
    btn.textContent='≡';
    btn.setAttribute('aria-label','Abrir menú');
  }
  btn.addEventListener('click',function(){
    var isOpen=menu.classList.toggle('open');
    btn.setAttribute('aria-expanded',isOpen);
    menu.setAttribute('aria-hidden',!isOpen);
    btn.textContent=isOpen?'✕':'≡';
    btn.setAttribute('aria-label',isOpen?'Cerrar menú':'Abrir menú');
  });
  menu.querySelectorAll('a').forEach(function(link){link.addEventListener('click',close);});
  document.addEventListener('keydown',function(e){if(e.key==='Escape')close();});
})();
</script>

<!-- JS 5 (opcional): Form submit handler
<script>
(function(){
  var form=document.getElementById('form-diagnostico');
  var container=document.getElementById('form-container');
  if(!form||!container)return;
  form.addEventListener('submit',function(e){
    e.preventDefault();
    var btn=document.getElementById('btn-submit');
    btn.disabled=true;btn.textContent='Enviando…';
    setTimeout(function(){
      container.innerHTML='<div class="form-success"><span class="form-ok">/ Diagnóstico recibido</span><p>Revisaremos tu contexto y te respondemos en menos de 24h.</p></div>';
    },1200);
  });
})();
</script> -->

</body>
</html>
```

---

## 14. Canal: LinkedIn — implementación visual

> **Fuente de verdad de contenido: `brand-wiki-syncon-v1.2-interno-cerrado.md` §8, §9 y §11.**
> Qué publicar, cuándo, quién, en qué tono, el calendario de 20 posts del mes 1, los pilares editoriales y el Quality Gate → leer la Brand Wiki, no este documento.
>
> Esta sección cubre ÚNICAMENTE lo que la Brand Wiki no cubre: dimensiones de assets visuales, aplicación de tokens en herramientas de diseño (Canva/Figma), y checklist de assets a crear.

---

### 14.1 Fuentes de verdad por responsabilidad

| Decisión | Fuente | Sección |
|---|---|---|
| Qué publicar / pilares editoriales | Brand Wiki v1.2 | §8.1 |
| Cuándo publicar / cadencia | Brand Wiki v1.2 | §8.2 |
| Calendario mes 1 (20 posts) | Brand Wiki v1.2 | §8.3 |
| Voz, tono, vocabulario | Brand Wiki v1.2 | §9 |
| Quality Gate (≥4/5 para publicar) | Brand Wiki v1.2 | §11 |
| Claims permitidos y overclaims prohibidos | Brand Wiki v1.2 | §11 |
| Quién publica / gobernanza | Brand Wiki v1.2 | §12 |
| **Dimensiones y specs visuales** | **Design System §14** | **← aquí** |
| **Tokens en Canva/Figma** | **Design System §14** | **← aquí** |
| **Assets pendientes de crear** | **Design System §14** | **← aquí** |

---

### 14.2 Tokens en herramientas de diseño

LinkedIn no permite CSS. Estos son los valores a cargar en Canva, Figma o cualquier herramienta de diseño:

```
Fondo principal:  #0A0A0A   (--ink)
Fondo elevado:    #1A1A1A   (--bg-2)
Texto principal:  #FAFAFA   (--paper)
Texto secundario: #CCCCCC   (--fg-2)
Texto terciario:  #888888   (--muted)
Acento naranja:   #FF6B00   (--accent)
Borde sutil:      #444444   (--border)

Fuente títulos:   Geist (Google Fonts — descargar TTF)
Fuente kickers:   Geist Mono (Google Fonts — descargar TTF)
```

**Regla de fondo:** siempre `#0A0A0A`. Nunca blanco, nunca gris claro, nunca gradiente de fondo. El naranja es solo accent — nunca fondo dominante.

**Regla de texto naranja:** solo sobre fondo oscuro (ratio ≈6.9:1, pasa AA). Nunca texto naranja sobre blanco.

---

### 14.3 Dimensiones de assets

| Asset | Dimensiones | Uso |
|---|---|---|
| Banner empresa | 1128 × 191 px | Company page `/company/syncon-solutions` |
| Foto de perfil empresa | 300 × 300 px | Logo sobre fondo `#0A0A0A` |
| Imagen de post (horizontal) | 1200 × 627 px | Post con visual individual |
| Imagen cuadrada | 1080 × 1080 px | Post destacado / carrusel |
| Cover de artículo | 1920 × 1080 px | LinkedIn Articles (GEO/AEO) |
| Foto de perfil fundador | 400 × 400 px | Cris, Lorena, Pipe — foto real |

---

### 14.4 Estructura visual de posts con imagen

Todos los posts con imagen siguen esta estructura visual (no de contenido — el contenido lo define Brand Wiki §8):

```
[fondo #0A0A0A]
  ┌─────────────────────────────────────┐
  │  [KICKER MONO] — kicker en #FF6B00  │  ← Geist Mono, 13-16px, uppercase
  │                                     │
  │  Título en Geist Bold               │  ← #FAFAFA, grande, 2-3 líneas máx
  │  con remate en naranja.             │  ← última línea en #FF6B00
  │                                     │
  │  /syncon.solutions  [wordmark]       │  ← esquina inferior, Geist Mono
  └─────────────────────────────────────┘
```

- Sin stock photos. Sin ilustraciones decorativas.
- Los receipts/números van en Geist Mono, tamaño grande, en `#FAFAFA` o `#FF6B00`.
- No mezclar más de 2 tipografías.

---

### 14.6 Sistema de slides — carrusel (Document Post)

**Qué es técnicamente:** LinkedIn recibe un archivo PDF. Cada página del PDF se convierte en una card deslizable. "Carrusel", "cards" y "document post" son el mismo formato desde perspectivas distintas: carrusel = experiencia del usuario; PDF = formato de producción en Canva/Figma.

**Dimensión:** 1080 × 1080 px (cuadrado). Máximo 20 páginas; recomendado máximo 10.

**Fuente de verdad de estructura de contenido (qué va en cada slide):** Brand Wiki §8.4 y §8.5.

---

#### Slide 1 — Portada (obligatoria)

```
[fondo #0A0A0A]
┌─────────────────────────────────────────────┐
│  [KICKER MONO]                              │  ← Geist Mono 13px, #FF6B00, uppercase
│                                             │
│  Promesa o pregunta específica              │  ← Geist Bold, 32-40px, #FAFAFA
│  que el lector no puede ignorar.           │  ← última línea puede ir en #FF6B00
│                                             │
│  /syncon.solutions              [N slides] │  ← wordmark Geist Mono + conteo total
└─────────────────────────────────────────────┘
```

**Regla de portada:** debe funcionar sola como post de imagen estática. Si el lector no desliza, la portada ya entregó valor. El kicker naranja es obligatorio.

---

#### Slides 2–(N-1) — Contenido

```
[fondo #0A0A0A o #1A1A1A alternados]
┌─────────────────────────────────────────────┐
│                            [slide N / total]│  ← Geist Mono 11px, #888888, sup-derecha
│                                             │
│  Una sola idea por slide.                  │  ← Geist Bold 24-28px, #FAFAFA
│                                             │
│  Desarrollo en 2-3 líneas máximo.          │  ← Geist Sans 16-18px, #CCCCCC
│                                             │
│  [dato, ratio o receipt si aplica]         │  ← Geist Mono, #FF6B00 si es número clave
│                                             │
│  /syncon.solutions                          │  ← wordmark pequeño, esquina inferior
└─────────────────────────────────────────────┘
```

**Reglas de slides de contenido:**
- Una idea por slide. Si hay dos ideas, dividir en dos slides.
- Máximo 40 palabras de texto por slide.
- No usar bullets en cascada. Si hay lista, una línea por slide, o convertir a infografía.
- Los números clave van en Geist Mono tamaño grande (40-56px), en `#FF6B00`.
- Alternar fondo `#0A0A0A` / `#1A1A1A` para crear ritmo visual sin romper coherencia.

---

#### Slide final — CTA (obligatoria)

```
[fondo #0A0A0A]
┌─────────────────────────────────────────────┐
│  [KICKER MONO] "¿Qué sigue?"               │  ← Geist Mono 13px, #FF6B00
│                                             │
│  Acción específica en una línea.           │  ← Geist Bold 28-32px, #FAFAFA
│                                             │
│  ▸ Comenta [PALABRA CLAVE]                  │  ← Geist Sans 16px, #FF6B00
│    para recibir [activo concreto]           │
│                                             │
│  /syncon.solutions                          │
└─────────────────────────────────────────────┘
```

**Regla de CTA:** el CTA de la slide final debe ser idéntico al CTA del texto del post. Consistencia elimina fricción. Nunca usar "síguenos para más".

---

#### Anti-patrones prohibidos en carruseles SYNCON

| Anti-patrón | Por qué está prohibido |
|---|---|
| Más de 40 palabras por slide | Destruye el dwell time; el usuario deja de deslizar |
| Bullets en lista vertical | Usar slides separadas o infografía |
| Más de 2 colores de texto por slide | Solo `#FAFAFA` + `#FF6B00` |
| Fondo blanco o claro | Rompe coherencia del sistema visual |
| Ilustraciones decorativas / stock / redes neuronales | Sin excepciones |
| Slides sin wordmark `/syncon.solutions` | Toda pieza identifica a SYNCON |
| Portada sin kicker naranja | El kicker es el marcador de categoría |
| CTA genérico en slide final | El CTA debe nombrar una acción y un activo específicos |

---

#### Checklist de producción — antes de exportar el PDF

- [ ] La portada funciona sola como imagen de post estático
- [ ] Cada slide tiene una sola idea central
- [ ] Ningún slide supera 40 palabras de texto
- [ ] El CTA de la última slide coincide con el CTA del texto del post en LinkedIn
- [ ] El wordmark `/syncon.solutions` aparece en todas las slides
- [ ] El conteo de slides aparece en la portada
- [ ] El PDF exportado pesa menos de 8 MB (LinkedIn rechaza archivos más grandes)
- [ ] Vista revisada a 375px de ancho — legibilidad correcta en móvil

---

### 14.5 Assets a crear (checklist)

- [ ] **Banner empresa** (1128×191) — `/syncon.solutions` wordmark + tagline "Ingeniería contextual. Operaciones inteligentes." sobre fondo `#0A0A0A`
- [ ] **Foto de perfil empresa** (300×300) — logo `/syncon.solutions` centrado sobre `#0A0A0A`
- [ ] **Plantilla post horizontal** (1200×627) en Canva/Figma — kicker + título bicolor + wordmark
- [ ] **Plantilla post cuadrado** (1080×1080) — misma estructura que §14.4
- [ ] **Plantilla carrusel** (1080×1080, hasta 10 slides) — según sistema §14.6: portada + slides de contenido + slide CTA
- [ ] **Plantilla receipt** — número grande Geist Mono + label + fecha + `/syncon.solutions`
- [ ] Fotos de perfil de fundadores (Cris, Lorena, Pipe) — fondo `#0A0A0A` o foto corporativa real

---

*SYNCON Design System v1.6 · 2026-06-26 · es-CO*
*§1–10: brand canon (2026-06-24/25). §11–12: CSS home mockup. §13: esqueleto HTML página nueva. §14: LinkedIn — specs visuales; §14.6 sistema de slides carrusel (2026-06-26). Contenido/estrategia en `brand-wiki-syncon-v1.3-interno-cerrado.md`. Cambios estructurales: 3-de-3 (Cris, Lorena, Pipe). Claims públicos: 2-of-2 + receipt dateado.*
