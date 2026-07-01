# Página "Cómo trabajamos" — Plan de Implementación

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Crear la página dedicada `/como-trabajamos` (loop de acompañamiento + método Eliminar→Medir + acompañamiento como "la clave" + contacto con agenda 30 min) y repuntar los 6 enlaces "Cómo trabajamos" del sitio hacia ella.

**Architecture:** Página HTML autocontenida construida duplicando `productos.html` (que ya trae el shell canon: nav, footer, sección `#contacto` con bloque agenda 30 min, y el JS de submit) y reemplazando el cuerpo `<main>` por las 4 secciones nuevas. Sin framework: la verificación es por preview local (`py -m http.server 5174`) con asserts de DOM vía `preview_eval` y revisión visual a 360/768/1280 px.

**Tech Stack:** HTML5 estático, CSS inline (design system Syncon v1.5, tokens en `:root`), SVG inline para el loop, vanilla JS (heredado de productos.html). Netlify (URLs limpias). Spec fuente: `syncon-design-system/specs/2026-06-30-como-trabajamos-page-design.md`.

---

## File Structure

| Archivo | Responsabilidad | Acción |
|---|---|---|
| `syncon-netlify-deploy/como-trabajamos.html` | La página nueva, autocontenida | Crear (duplicar productos.html + reemplazar cuerpo) |
| `syncon-netlify-deploy/index.html` | Repuntar 3 enlaces nav/mobile/footer + CTA teaser en `#metodo` | Modificar |
| `syncon-netlify-deploy/productos.html` | Repuntar 3 enlaces | Modificar |
| `syncon-netlify-deploy/about.html` | Repuntar 3 enlaces | Modificar |
| `syncon-netlify-deploy/productos/har.html` | Repuntar 3 enlaces | Modificar |
| `syncon-netlify-deploy/productos/consultoria.html` | Repuntar 3 enlaces | Modificar |
| `syncon-netlify-deploy/productos/capacitacion.html` | Repuntar 3 enlaces | Modificar |

Convención de rutas: archivos `.html` físicos, URL limpia servida por Netlify. Enlace destino canónico: `/como-trabajamos`.

---

## Task 1: Scaffold de la página desde productos.html

**Files:**
- Create: `syncon-netlify-deploy/como-trabajamos.html` (copia de `productos.html`)

- [ ] **Step 1: Duplicar productos.html**

Run (PowerShell):
```powershell
Copy-Item "C:\Users\lilia\syncon-netlify-deploy\productos.html" "C:\Users\lilia\syncon-netlify-deploy\como-trabajamos.html"
```

- [ ] **Step 2: Actualizar `<title>` y meta description**

En `como-trabajamos.html`, reemplazar el `<title>` y la `<meta name="description">` del head por:
```html
<title>Cómo trabajamos · SYNCON</title>
<meta name="description" content="Consultoría, implementación de IA, software a la medida, capacitación y cerebro corporativo en un ciclo continuo. El acompañamiento es la clave: va después de cualquier entrega.">
```
(Buscar las etiquetas `<title>` y `<meta name="description"` existentes heredadas de productos y sustituir su contenido.)

- [ ] **Step 3: Marcar "Cómo trabajamos" activo en el nav de esta página**

En el nav y el mobile-menu de `como-trabajamos.html`, el enlace "Cómo trabajamos" hereda `href="/#metodo"`. Cambiarlo a `href="/como-trabajamos"` y, en el `<a>` del nav principal, añadir `aria-current="page"`. Localizar:
```html
<li><a href="/#metodo">Cómo trabajamos</a></li>
```
y dejar (nav principal):
```html
<li><a href="/como-trabajamos" aria-current="page">Cómo trabajamos</a></li>
```
El del mobile-menu: `href="/como-trabajamos"` (sin aria-current).
El del footer (`<a href="/#metodo">Cómo trabajamos</a>`): `href="/como-trabajamos"`.

- [ ] **Step 4: Vaciar el cuerpo dejando solo el shell**

En `como-trabajamos.html`, eliminar todas las `<section>` del cuerpo de producto que van **entre** la apertura de `<main ...>` y la línea `<!-- ... #contacto ... -->` / `<section id="contacto"`. Conservar intactos: `<header>`/nav, mobile-menu, `<main ...>` (apertura), la sección `#contacto` completa (con su bloque agenda 30 min), `</main>`, `<footer>`, y todos los `<script>`. Dejar un comentario marcador donde irán las secciones nuevas:
```html
<main id="main-content">
  <!-- ░░ SECCIONES COMO-TRABAJAMOS — se insertan en Tasks 2–5 ░░ -->

  <!-- ═══ #contacto … (heredado, intacto) ═══ -->
```

- [ ] **Step 5: Cambiar `data-pilar` del bloque agenda**

En la sección `#contacto` heredada, en el `<a class="calendly-link" ... data-pilar="productos">`, cambiar a `data-pilar="como-trabajamos"`.

- [ ] **Step 6: Verificar que carga**

Run: arrancar preview (`preview_start` name `syncon-deploy`) y `preview_eval` con:
```js
fetch('http://localhost:5174/como-trabajamos.html').then(r=>r.text()).then(t=>'title='+/<title>Cómo trabajamos/.test(t)+' contacto='+t.includes('id="contacto"')+' calendly='+t.includes('data-pilar="como-trabajamos"')+' agenda='+t.includes('Agenda 30 minutos directo'))
```
Expected: `title=true contacto=true calendly=true agenda=true`

- [ ] **Step 7: Commit (si el directorio es repo; si no, omitir)**

Solo si `syncon-netlify-deploy` es un repo git. Si no, omitir todos los pasos de commit del plan.

---

## Task 2: Sección Hero

**Files:**
- Modify: `syncon-netlify-deploy/como-trabajamos.html` (insertar tras el marcador de `<main>`)

- [ ] **Step 1: Insertar el HTML del hero**

Insertar como primera sección dentro de `<main id="main-content">`, después del comentario marcador:
```html
<!-- 1 · HERO -->
<section class="hero-simple">
  <div class="wrap">
    <h1 style="font-size:clamp(34px,5vw,60px);font-weight:800;letter-spacing:-0.04em;line-height:1.04;max-width:18ch">
      <span style="display:block;font-family:var(--mono);font-size:11px;font-weight:400;color:var(--accent);letter-spacing:.14em;text-transform:uppercase;margin-bottom:var(--s4)">Cómo trabajamos</span>
      <span style="display:block;color:var(--paper)">No es un proyecto con fecha de cierre.</span>
      <span style="display:block;color:var(--accent)">Es un loop de acompañamiento.</span>
    </h1>
    <p class="lede" style="margin-top:var(--s6);max-width:760px">Consultoría, implementación de IA, software a la medida, capacitación y —cuando el caso lo pide— un cerebro corporativo completo. No los entregamos y cerramos: ocurren en un ciclo, y el acompañamiento va después de cualquiera de ellos. Ahí es donde la efectividad se compone, vuelta a vuelta.</p>
    <div style="margin-top:var(--s8)">
      <a href="#contacto" class="btn btn-primary" style="border-radius:var(--r-full);padding:0 22px;font-size:14px">Quiero diagnosticar mi operación <span aria-hidden="true">→</span></a>
    </div>
  </div>
</section>
```

- [ ] **Step 2: Añadir CSS de `.hero-simple` (si no existe)**

Antes de `</style>` del head, añadir:
```css
.hero-simple{padding-top:clamp(72px,10vw,128px);padding-bottom:clamp(40px,6vw,72px)}
```
(Si productos.html ya define un padding de hero equivalente reutilizable, usarlo en su lugar y omitir esta regla.)

- [ ] **Step 3: Verificar en preview**

`preview_eval`:
```js
(function(){var h=document.querySelector('.hero-simple h1');return h?h.textContent.replace(/\s+/g,' ').trim().slice(0,80):'NO HERO';})()
```
Expected: contiene "Cómo trabajamos No es un proyecto con fecha de cierre. Es un loop de acompañamiento."

---

## Task 3: Sección El loop (SVG desktop + lista móvil + copy de nodos)

**Files:**
- Modify: `syncon-netlify-deploy/como-trabajamos.html`

- [ ] **Step 1: Añadir CSS del loop antes de `</style>`**

```css
/* ── Loop de acompañamiento ── */
.loop-grid{display:grid;gap:clamp(28px,4vw,56px);align-items:center}
@media(min-width:901px){.loop-grid{grid-template-columns:minmax(0,430px) 1fr}}
.loop-fig{margin:0;width:100%}
.loop-svg{width:100%;height:auto;display:block}
.loop-nodes{display:grid;gap:var(--s4);list-style:none;margin:0;padding:0}
.loop-node{display:grid;grid-template-columns:auto 1fr;gap:var(--s4);padding:var(--s4) var(--s5);border:1px solid var(--border);border-radius:var(--r-md);background:#0E0E0E}
.loop-node .ln-n{font-family:var(--mono);font-size:13px;color:var(--accent);padding-top:2px}
.loop-node h4{font-size:clamp(17px,1.9vw,20px);font-weight:700;letter-spacing:-0.01em;margin:0 0 4px;color:var(--paper)}
.loop-node p{font-size:16px;color:var(--fg-2);margin:0}
.loop-node.is-accent{border-color:var(--accent)}
.loop-node.is-accent .ln-n,.loop-node.is-accent h4{color:var(--accent)}
.loop-intro{max-width:760px;margin-top:var(--s4)}
@media(max-width:640px){.loop-fig{display:none}}
```

- [ ] **Step 2: Insertar el HTML de la sección loop (después del hero)**

```html
<!-- 2 · EL LOOP -->
<section id="loop" class="reveal">
  <div class="wrap">
    <h2 style="font-size:clamp(28px,3.6vw,40px);font-weight:800;letter-spacing:-0.04em;line-height:1.06">
      <span style="display:block;font-family:var(--mono);font-size:11px;font-weight:400;color:var(--accent);letter-spacing:.14em;text-transform:uppercase;margin-bottom:var(--s3)">El ciclo</span>
      <span style="display:block;color:var(--paper)">Un ciclo,</span>
      <span style="display:block;color:var(--accent)">no una entrega.</span>
    </h2>
    <p class="lede loop-intro">No todos pasan por todas las etapas. Algunos hacen una consultoría y una implementación de IA; otros, software a la medida; otros, el cerebro completo. Lo constante es que diagnosticamos primero y acompañamos siempre.</p>

    <div class="loop-grid" style="margin-top:var(--s12)">
      <figure class="loop-fig" aria-hidden="true">
        <!-- SVG del loop — insertar el bloque del Step 3 aquí -->
      </figure>
      <ol class="loop-nodes">
        <li class="loop-node"><span class="ln-n">1</span><div><h4>Consultoría</h4><p>Mapeamos el proceso real y el dolor en pesos. Si no justifica el payback, te lo decimos antes de firmar.</p></div></li>
        <li class="loop-node"><span class="ln-n">2</span><div><h4>Cerebro corporativo</h4><p>Cuando el caso lo pide: el conocimiento atrapado en WhatsApp, Excel y la cabeza de tu gente se vuelve memoria viva con agentes por rol.</p></div></li>
        <li class="loop-node"><span class="ln-n">3</span><div><h4>Software e IA a la medida</h4><p>Implementación de IA, automatización de procesos o una plataforma a la medida. Construimos lo que el caso pida, en producción.</p></div></li>
        <li class="loop-node"><span class="ln-n">4</span><div><h4>Capacitación</h4><p>Tu equipo aprende a operar la solución y a usar IA en su día a día. No queda dependiendo de nosotros.</p></div></li>
        <li class="loop-node is-accent"><span class="ln-n">5</span><div><h4>Acompañamiento</h4><p>Nos quedamos con tu equipo después de cualquier entrega: ajustes, operación gobernada y ROI medido. Y reinicia el ciclo.</p></div></li>
      </ol>
    </div>
  </div>
</section>
```

- [ ] **Step 3: Pegar el SVG del loop dentro de `<figure class="loop-fig">`**

(Opción 2 aprobada, con nodo 3 = "Software e IA a la medida".)
```html
<svg class="loop-svg" viewBox="0 0 560 560" xmlns="http://www.w3.org/2000/svg" role="img" aria-labelledby="loopT loopD" font-family="var(--sans)">
<title id="loopT">El loop de acompañamiento de Syncon</title>
<desc id="loopD">Cinco actividades en ciclo: Consultoría, Cerebro corporativo, Software e IA a la medida, Capacitación y Acompañamiento. El acompañamiento, resaltado, reinicia el ciclo hacia la consultoría.</desc>
<defs>
<marker id="cag" viewBox="0 0 10 10" refX="8.5" refY="5" markerWidth="6.5" markerHeight="6.5" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="#7d7d7d"/></marker>
<marker id="cao" viewBox="0 0 10 10" refX="8.5" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="#FF6B00"/></marker>
</defs>
<circle cx="280" cy="290" r="150" fill="none" stroke="#2a2a2a" stroke-width="1"/>
<path d="M321,150 A150 150 0 0 1 404,212" fill="none" stroke="#555" stroke-width="1.4" marker-end="url(#cag)"/>
<path d="M430,302 A150 150 0 0 1 398,400" fill="none" stroke="#555" stroke-width="1.4" marker-end="url(#cag)"/>
<path d="M335,447 A150 150 0 0 1 225,447" fill="none" stroke="#555" stroke-width="1.4" marker-end="url(#cag)"/>
<path d="M162,400 A150 150 0 0 1 130,302" fill="none" stroke="#555" stroke-width="1.4" marker-end="url(#cag)"/>
<path d="M156,212 A150 150 0 0 1 239,150" fill="none" stroke="#FF6B00" stroke-width="2.6" marker-end="url(#cao)"/>
<text x="197" y="168" text-anchor="middle" fill="#FF6B00" font-family="var(--mono)" font-size="11" letter-spacing=".5">reinicia</text>
<g><rect x="208" y="120" width="144" height="40" rx="20" fill="#181818" stroke="rgba(255,255,255,.16)"/><text x="280" y="145" text-anchor="middle" fill="#FAFAFA" font-size="13">Consultoría</text></g>
<g><rect x="346" y="222" width="150" height="40" rx="20" fill="#181818" stroke="rgba(255,255,255,.16)"/><text x="421" y="247" text-anchor="middle" fill="#FAFAFA" font-size="11.5">Cerebro corporativo</text></g>
<g><rect x="318" y="382" width="168" height="40" rx="20" fill="#181818" stroke="rgba(255,255,255,.16)"/><text x="402" y="407" text-anchor="middle" fill="#FAFAFA" font-size="11">Software e IA a la medida</text></g>
<g><rect x="146" y="382" width="150" height="40" rx="20" fill="#181818" stroke="rgba(255,255,255,.16)"/><text x="221" y="407" text-anchor="middle" fill="#FAFAFA" font-size="13">Capacitación</text></g>
<g><rect x="64" y="222" width="150" height="40" rx="20" fill="#181818" stroke="#FF6B00"/><text x="139" y="247" text-anchor="middle" fill="#FF6B00" font-size="12.5">Acompañamiento</text></g>
</svg>
```
Nota: el `viewBox` 560×560 centra el ciclo en (280,290) r=150; los nodos están en pentágono (top, der-sup, der-inf, izq-inf, izq-sup). Validar que ningún pill se salga del viewBox en el Step 4.

- [ ] **Step 4: Verificar en preview (desktop)**

`preview_eval`:
```js
(function(){var n=document.querySelectorAll('#loop .loop-node').length;var acc=document.querySelector('#loop .loop-node.is-accent h4').textContent;var svg=!!document.querySelector('#loop .loop-svg');return 'nodos='+n+' accent='+acc+' svg='+svg+' n3='+document.querySelectorAll('#loop .loop-node')[2].querySelector('h4').textContent;})()
```
Expected: `nodos=5 accent=Acompañamiento svg=true n3=Software e IA a la medida`

- [ ] **Step 5: Verificar fallback móvil**

`preview_resize` a 375px y `preview_eval`:
```js
getComputedStyle(document.querySelector('.loop-fig')).display
```
Expected: `none` (el SVG se oculta; las 5 tarjetas numeradas quedan como lista vertical).

---

## Task 4: Sección El método (Eliminar → Medir)

**Files:**
- Modify: `syncon-netlify-deploy/como-trabajamos.html`

- [ ] **Step 1: Insertar el HTML de la sección método (después del loop)**

Usa el patrón `.steps`/`.step` heredado del design system. Numeración 1–5 justificada (el orden es el contenido).
```html
<!-- 3 · EL MÉTODO -->
<section id="metodo-detalle" class="reveal">
  <div class="wrap">
    <h2 style="font-size:clamp(28px,3.6vw,40px);font-weight:800;letter-spacing:-0.04em;line-height:1.06">
      <span style="display:block;font-family:var(--mono);font-size:11px;font-weight:400;color:var(--accent);letter-spacing:.14em;text-transform:uppercase;margin-bottom:var(--s3)">El método detrás del diagnóstico</span>
      <span style="display:block;color:var(--paper)">Primero el contexto.</span>
      <span style="display:block;color:var(--accent)">Después la herramienta.</span>
    </h2>
    <p class="lede" style="margin-top:var(--s4);max-width:820px">La arquitectura del proceso manda sobre la herramienta. Una herramienta excelente sobre un proceso mal diseñado entrega el mismo problema, más rápido. Por eso no automatizamos el desorden: primero lo rediseñamos.</p>
    <div class="steps" style="margin-top:var(--s12)">
      <div class="step"><div class="n">1</div><h4>Eliminar</h4><p>Quitamos los pasos que no deberían existir. La intervención de mayor impacto y menor costo.</p></div>
      <div class="step"><div class="n">2</div><h4>Simplificar</h4><p>Reducimos lo que queda hasta que se explique a alguien nuevo en menos de diez minutos.</p></div>
      <div class="step"><div class="n">3</div><h4>Optimizar</h4><p>Mejoramos la ejecución de los pasos que permanecen.</p></div>
      <div class="step"><div class="n">4</div><h4>Automatizar</h4><p>Recién aquí entra la IA, sobre un proceso ya limpio. Antes, solo acelera el desorden.</p></div>
      <div class="step"><div class="n">5</div><h4>Medir</h4><p>Cerramos el ciclo. Sobre un proceso simple, los números son señal, no ruido.</p></div>
    </div>
  </div>
</section>
```

- [ ] **Step 2: Verificar que `.steps` soporta 5 columnas**

El CSS canon define `.steps` con `grid-template-columns:repeat(3,1fr)`. Con 5 ítems se verá 3+2. Para 5 etapas secuenciales conviene fila única en desktop y wrap en móvil. Añadir antes de `</style>`:
```css
#metodo-detalle .steps{grid-template-columns:repeat(5,1fr);gap:var(--s6)}
@media(max-width:900px){#metodo-detalle .steps{grid-template-columns:repeat(2,1fr)}}
@media(max-width:560px){#metodo-detalle .steps{grid-template-columns:1fr}}
```

- [ ] **Step 3: Verificar en preview**

`preview_eval`:
```js
Array.from(document.querySelectorAll('#metodo-detalle .step h4')).map(e=>e.textContent).join(' › ')
```
Expected: `Eliminar › Simplificar › Optimizar › Automatizar › Medir`

---

## Task 5: Sección "El acompañamiento es la clave"

**Files:**
- Modify: `syncon-netlify-deploy/como-trabajamos.html`

- [ ] **Step 1: Insertar el HTML (después del método, antes de #contacto)**

```html
<!-- 4 · LA CLAVE -->
<section id="la-clave" class="reveal">
  <div class="wrap">
    <h2 style="font-size:clamp(28px,3.6vw,40px);font-weight:800;letter-spacing:-0.04em;line-height:1.06">
      <span style="display:block;font-family:var(--mono);font-size:11px;font-weight:400;color:var(--accent);letter-spacing:.14em;text-transform:uppercase;margin-bottom:var(--s3)">Por qué importa</span>
      <span style="display:block;color:var(--paper)">El acompañamiento no es un extra.</span>
      <span style="display:block;color:var(--accent)">Es la clave.</span>
    </h2>
    <p class="lede" style="margin-top:var(--s4);max-width:820px">Va después de cualquier entrega — una consultoría, una implementación de IA, un software a la medida, una capacitación o un cerebro corporativo completo. Es nuestra propuesta de valor central.</p>
    <div class="who" style="margin-top:var(--s12)">
      <div><h4>No desaparecemos después de la entrega</h4><p>Sea lo que sea que construimos o diagnosticamos: ajustes, operación gobernada y reporte de ROI continuo.</p></div>
      <div><h4>El conocimiento queda en tu equipo</h4><p>Después de la capacitación y durante el acompañamiento, tu gente queda capaz de operar sin depender de la firma.</p></div>
      <div><h4>Gobernanza humana</h4><p>Cuando hay agentes de por medio, ellos proponen y tu gente ratifica; la decisión la toma un humano, siempre.</p></div>
    </div>
    <p class="anti" style="margin-top:var(--s12)">Lo que no somos:</p>
    <div class="pills">
      <span class="pill">el piloto que nunca llega a producción</span>
      <span class="pill">consultoría de slides</span>
      <span class="pill">pricing por horas</span>
    </div>
  </div>
</section>
```

- [ ] **Step 2: Verificar en preview**

`preview_eval`:
```js
(function(){var h=document.querySelector('#la-clave h2').textContent.replace(/\s+/g,' ').trim();var cards=document.querySelectorAll('#la-clave .who > div').length;var pills=document.querySelectorAll('#la-clave .pill').length;return 'h2="'+h+'" cards='+cards+' pills='+pills;})()
```
Expected: `h2` contiene "El acompañamiento no es un extra. Es la clave." · `cards=3` · `pills=3`

- [ ] **Step 3: Verificar que no quedó copy product-céntrico ni "foso"**

`preview_eval`:
```js
fetch('http://localhost:5174/como-trabajamos.html').then(r=>r.text()).then(t=>'foso='+/foso/i.test(t)+' claveOK='+t.includes('Es la clave')+' iaNode='+t.includes('Software e IA a la medida'))
```
Expected: `foso=false claveOK=true iaNode=true`

---

## Task 6: Repuntar los 6 enlaces "Cómo trabajamos" + teaser en home

**Files:**
- Modify: `index.html`, `productos.html`, `about.html`, `productos/har.html`, `productos/consultoria.html`, `productos/capacitacion.html`

- [ ] **Step 1: Repuntar en index.html (enlaces relativos `#metodo`)**

`Edit` con `replace_all:true` en `index.html`:
- old: `href="#metodo">Cómo trabajamos`
- new: `href="/como-trabajamos">Cómo trabajamos`
(Afecta nav, mobile-menu y footer — 3 ocurrencias. NO afecta `<section id="metodo">`.)

- [ ] **Step 2: Añadir CTA teaser dentro de `#metodo` del home**

En `index.html`, dentro de `<section id="metodo">`, después del `</div>` que cierra `.steps` y antes del `</div>` que cierra `.wrap`, insertar:
```html
    <div style="margin-top:var(--s8)">
      <a href="/como-trabajamos" class="btn btn-ghost" style="border-radius:var(--r-full);font-size:14px;padding:0 22px">Ver cómo trabajamos en detalle <span aria-hidden="true">→</span></a>
    </div>
```
Anchor de inserción: la secuencia `    </div>\n  </div>\n</section>` que cierra la sección `#metodo` (la primera de esas tras los 3 `.step`). Insertar el bloque entre el cierre de `.steps` (`    </div>`) y el cierre de `.wrap` (`  </div>`).

- [ ] **Step 3: Repuntar en los otros 5 archivos (enlaces absolutos `/#metodo`)**

Para cada uno de `productos.html`, `about.html`, `productos/har.html`, `productos/consultoria.html`, `productos/capacitacion.html`, `Edit` con `replace_all:true`:
- old: `href="/#metodo">Cómo trabajamos`
- new: `href="/como-trabajamos">Cómo trabajamos`
(3 ocurrencias por archivo: nav, mobile-menu, footer.)

- [ ] **Step 4: Verificar repunteo en preview**

`preview_eval`:
```js
Promise.all(['/index.html','/productos.html','/about.html','/productos/har.html','/productos/consultoria.html','/productos/capacitacion.html'].map(u=>fetch('http://localhost:5174'+u).then(r=>r.text()).then(t=>u+': metodo='+(t.match(/#metodo">Cómo trabajamos/g)||[]).length+' nueva='+(t.match(/\/como-trabajamos">Cómo trabajamos/g)||[]).length))).then(a=>a.join(' | '))
```
Expected: cada archivo con `metodo=0` y `nueva=3` (index puede tener `nueva=4` por el CTA teaser; verificar que `metodo=0` salvo el `id="metodo"` que no matchea este patrón).

---

## Task 7: Verificación integral (responsive + a11y + agenda)

**Files:** ninguno (solo verificación)

- [ ] **Step 1: Revisión visual a 3 anchos**

`preview_resize` y `preview_screenshot` (o snapshot si el screenshot se cuelga por assets) a 1280, 768 y 360 px sobre `/como-trabajamos`. Confirmar: sin overflow horizontal, loop circular legible en desktop, lista vertical en 360, secciones espaciadas.

- [ ] **Step 2: Verificar el bloque agenda 30 min**

`preview_eval`:
```js
(function(){var l=document.querySelector('#contacto .calendly-link');return l?getComputedStyle(l).borderRadius+' / '+getComputedStyle(l).padding+' / pilar='+l.getAttribute('data-pilar'):'NO CALENDLY';})()
```
Expected: `99px / 16px 20px / pilar=como-trabajamos`

- [ ] **Step 3: Verificar landmarks y SVG a11y**

`preview_eval`:
```js
'main='+!!document.querySelector('main#main-content')+' skip='+!!document.querySelector('.skip-link')+' svgRole='+(document.querySelector('.loop-svg')?.getAttribute('role'))+' svgTitle='+!!document.querySelector('.loop-svg title')
```
Expected: `main=true skip=true svgRole=img svgTitle=true`

- [ ] **Step 4: Verificar submit del formulario**

`preview_fill` los campos del form, `preview_click` el submit, `preview_snapshot` para confirmar el estado `.form-success` (heredado de productos.html). Si el JS de submit usa el mismo `id="form-diagnostico"`/`id="btn-submit"`, debe funcionar sin cambios.

- [ ] **Step 5: Chequear hallazgos impeccable**

Confirmar que los hallazgos de impeccable en `como-trabajamos.html` son solo los preexistentes del canon (fuente Inter, nav-cursor layout-transition) y no defectos nuevos del loop/método. Documentar cualquiera nuevo.

- [ ] **Step 6: Actualizar memoria**

Tras cerrar, actualizar `syncon_design_system.md` (memoria): nueva página `/como-trabajamos` creada, enlaces `#metodo` repunteados, decisión "acompañamiento = la clave (horizontal)". Y mover `/articulos` como única página pendiente.

---

## Self-Review (cobertura del spec)

- §4.1 Hero → Task 2 ✓
- §4.2 Loop (intro amplitud, SVG Opción 2, nodo 3 "Software e IA", copy 5 nodos, fallback móvil) → Task 3 ✓
- §4.3 Método (principio + Eliminar→Medir) → Task 4 ✓
- §4.4 La clave (reframe horizontal, 3 puntos, pills) → Task 5 ✓
- §4.5 #contacto + agenda 30 min → Task 1 (heredado) + Task 7 Step 2 ✓
- §4.6 Nav/Footer + activo → Task 1 ✓
- §5 Repunteo de los 6 enlaces + teaser home → Task 6 ✓
- §6 Restricciones design system (tokens, anti-patrones, WCAG, reveal) → Tasks 3–5 (clases canon, `.reveal`, SVG a11y) + Task 7 Step 3 ✓
- §8 Verificación → Task 7 ✓

Sin placeholders TBD/TODO en código. Nombres consistentes: `loop-node`, `is-accent`, `loop-fig`, `#metodo-detalle`, `#la-clave`, `data-pilar="como-trabajamos"` usados igual en build y verificación.
