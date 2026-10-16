# Al Pharma · estado de la sesión (16 oct 2026)

Documento para retomar el trabajo en una sesión nueva.

## Contexto

- **Cliente:** Al Pharma (Colombia, hemato-oncología). Sitio: alpharma.com.co.
- **Contacto de origen:** Juan Carlos Villalba Ordóñez. Pidió por LinkedIn "más información y brochure" a juan.villalba@alpharma.com.co, para llevarlo a la **Gerencia Comercial**.
- **Otros contactos en Apollo:** Carolina, Maritza, Pablo y Luis (enriquecidos).
  - Están en la lista **"Lista de llamadas"**.
  - Juan Carlos y Carolina: hoy. Pablo, Luis y Maritza: mañana.
- **Invitaciones de LinkedIn:** no se han enviado. Falta que Lorena decida la campaña en Waalaxy.

## Archivos en esta carpeta

| Archivo | Qué es |
|---|---|
| `syncon-brochure-alpharma-v2.html` | Brochure actual. Fuentes embebidas; se abre sin internet. |
| `syncon-brochure-alpharma-v2.pdf` | Exportación del mismo brochure, 13 páginas. |
| `brochure-texto-v0.2.md` | Texto aprobado v0.2, con el anexo del one-pager v0.3. |

**Para regenerar el PDF:**

```
/opt/pw-browsers/chromium-1194/chrome-linux/chrome --headless --no-pdf-header-footer --print-to-pdf=out.pdf file://.../syncon-brochure-alpharma-v2.html
```

## Reglas fijas que dio Lorena

- **Partners:** solo sector, expertise y país. Nunca nombres de empresas.
- **Advisors:** solo expertise y seniority. Nunca nombres.
- **Fundadores:** van solo con su nombre.
- **Se mantienen:** el brief en 48 horas y "sin costo hasta el MVP".
- **Company Brain:** debe quedar claro que vive dentro de un harness con las reglas corporativas y de negocio del cliente, y que las consultas responden dentro de esas reglas.
- **Formatos:** HTML y PDF, una vez aprobado.

## Dónde quedamos: replanteamiento de la sección de Al Pharma (no escrito aún)

**Crítica de Lorena:** la sección de hipótesis de valor sigue siendo inferencia. Quiere algo concreto, con datos y sin creatividad.

### Diagnóstico

Los datos de la sección v2 son del **sector**, no de Al Pharma:

- **Cartera:** Afidro reporta $4,42 billones, $1,6 billones vencidos y pagos de hasta 204 días.
  - No está verificado que Al Pharma sea afiliada a Afidro.
  - La propia empresa dice que tuvo su "mejor recaudo en 15 años", lo que contradice presentar la cartera como su dolor.
- **Precio:** la Circular 022/2026 cubre 33 mercados. Falta cruzarla con las moléculas de Al Pharma.
- **Abastecimiento:** se basa en una propuesta de Minsalud que todavía no está vigente. Respaldo débil.
- **Expansión LATAM:** es lo que la empresa aspira y no le corresponde a la Gerencia Comercial. Respaldo débil.

### Propuesta: tres niveles de evidencia

1. **Hechos de Al Pharma en fuentes oficiales:**
   - Supersociedades: ingresos, deudores comerciales, días de cartera y margen.
   - INVIMA (datos.gov.co): registros sanitarios y moléculas.
   - SECOP II: contratos públicos.
2. **El sector cruzado con su portafolio:**
   - Cuántas de sus moléculas quedaron bajo la Circular 022.
   - Cuáles aparecen en los listados de desabastecimiento del INVIMA.
   - Precios SISMED de sus moléculas frente a la competencia.
3. **Lo que solo existe adentro** (la agenda del diagnóstico): cartera por cliente, pipeline y cruce entre ventas e inventario.

- Reducir la sección a **1 o 2 frentes comerciales**: precio regulado y margen por molécula; cartera solo si Supersociedades lo confirma.
- **Nueva narrativa:** "Esto encontramos de Al Pharma en fuentes públicas… esto no lo vemos desde afuera y es lo que levantamos en 48 horas".

### Decisiones pendientes de Lorena

1. ¿Hacemos la extracción de los niveles 1 y 2?
2. ¿Reducimos a 1 o 2 frentes comerciales?
3. ¿Quitamos Afidro si no confirmamos la afiliación?

## Actualización: sección de Al Pharma reescrita (v2, 16 oct 2026)

- **Abre con sus números:** EMIS 2025 reporta ventas +6,78 % y utilidad neta +15,68 %. El crecimiento real calculado es ≈ +1,5 %, con inflación de 5,2 % según Bloomberg Línea.
- **Lo que dice la compañía** (Forbes) va separado y etiquetado.
- **Lectura:** gana por eficiencia, no por volumen. A 6,8 % anual, duplicar las ventas toma unos 10 años.
- **Un frente principal:** crecer en volumen con precios regulados (109+ moléculas y Circular 022).
- **Descartes explícitos:** cartera (no la priorizamos), abastecimiento y expansión (sin dato público), y 2024 junto con el detalle interno (se levanta en el brief).
- **Afidro y Cuenta de Alto Costo:** se retiraron.
- **Pendientes:**
  - Confirmar que el +6,78 % de EMIS es de 2025. Una búsqueda mostró el perfil de EMIS actualizado en abril de 2024, con +9,17 % para 2023.
  - Cuando Lorena traiga los datos de Supersociedades (NIT 830017238), reemplazar EMIS por las cifras exactas de 2023 a 2025.

## Otros pendientes

- **Borrador de Gmail** para Juan Carlos (asunto "SYNCON – información para la Gerencia Comercial de Al Pharma"):
  - Cambiar "30 minutos" por "15 minutos".
  - Adjuntar el PDF final.
  - No se tocó con update_draft porque puede borrar adjuntos.
- **PDF:** cuando esté aprobado, compactarlo a unas 6 páginas A4 para enviarlo como adjunto.
- **Inconsistencias que el equipo debe alinear:**
  - Duración de la primera llamada: "sin reloj" o 10 a 15 minutos. El brochure usa 15.
  - Si los advisors entran "cuando el caso lo pide" o en pasos fijos.
  - Un posible paso pagado de normalización de datos, que chocaría con "sin costo hasta el MVP".
