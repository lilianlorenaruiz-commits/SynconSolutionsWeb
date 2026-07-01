# SYNCON · Sitio web

Sitio corporativo de **SYNCON Solutions S.A.S.** — firma latinoamericana de ingeniería contextual (Bogotá). Sitio estático, sin build: HTML + CSS + JS vanilla, tipografía Geist, tema oscuro con acento naranja `#FF6B00`.

> Nativos en IA. Veteranos en industria.

## Estructura del repositorio

```
syncon-web/
├── sitio/            → La web lista para desplegar (esto es lo que sube a Netlify)
│   ├── index.html            → Home  (/)
│   ├── productos.html        → Productos  (/productos)
│   ├── faqs.html             → Preguntas frecuentes  (/faqs)
│   ├── como-trabajamos.html  → Cómo trabajamos  (/como-trabajamos)
│   ├── about.html            → La firma  (/about)
│   ├── productos/
│   │   ├── har.html          → Company Brain + HAR  (/productos/har)
│   │   ├── consultoria.html  → Consultoría  (/productos/consultoria)
│   │   └── capacitacion.html → Capacitación  (/productos/capacitacion)
│   ├── assets/               → Videos (.mp4) y logos (.svg)
│   └── _redirects            → Reglas de routing de Netlify (URLs limpias + fallback)
│
├── reglas/           → Design system y reglas de contenido por página/subpágina
│   ├── SYNCON_DESIGN_SYSTEM.md      → Canon de diseño (fuente de verdad)
│   ├── DESIGN.md                    → Guía de diseño resumida
│   ├── SYNCON_LinkedIn_Design_Card.md
│   ├── specs/                       → Especificaciones de diseño por página
│   └── plans/                       → Planes de implementación por página
│
├── tools/
│   └── serve_clean.py    → Servidor local con URLs limpias (para revisar como en Netlify)
│
├── README.md
└── .gitignore
```

## Correr en local

Requiere Python 3.7+. Desde la raíz del repo:

```bash
py tools/serve_clean.py
```

Luego abre **http://localhost:5174/** y navega por todo el menú. El servidor resuelve las URLs limpias igual que Netlify (`/faqs`, `/productos/har`, etc.), así que los enlaces del nav funcionan sin `.html`.

> Si cambias un archivo y no ves el cambio, refresca con `Ctrl+Shift+R` (el servidor envía `Cache-Control: no-store`, pero el navegador a veces cachea).

## Desplegar

El sitio es estático. Dos formas:

1. **Arrastrar carpeta** (manual): sube el contenido de **`sitio/`** al drop zone de Netlify (Sites → arrastrar). El `_redirects` ya está incluido.
2. **Conectar GitHub → Netlify** (recomendado para auto-deploy): en Netlify, "Import from Git", elige este repo y configura:
   - **Base directory / Publish directory:** `sitio`
   - **Build command:** (vacío — no hay build)

## Convenciones clave (ver `reglas/` para el detalle)

- **Rutas absolutas** para assets (`/assets/...`) y navegación (`/faqs`, `/productos/har`), para que resuelvan bien con URLs limpias en cualquier nivel.
- **Tokens de diseño** (colores, espaciado, tipografía) definidos en `:root` de cada página; ver `reglas/SYNCON_DESIGN_SYSTEM.md`.
- **Flujo de contacto unificado:** reunión de 30 min → diagnóstico contextual → viabilidad en 48h. Sin costo, sin compromiso.
- **Guardas de honestidad:** firma pre-ingresos; "los agentes proponen, tu gente ratifica"; no prometer retorno garantizado.

## Páginas pendientes

- `/articulos` — Blog de ingeniería contextual (enlazado en el nav; aún por construir; hoy cae al home vía el fallback de `_redirects`).
