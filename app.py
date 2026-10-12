import streamlit as st

st.set_page_config(page_title="AgroGuía IA | La Última Cosecha", page_icon="🌱", layout="wide")

# Prototipo académico: las fichas son una estructura inicial y NO deben tratarse como
# recomendaciones agronómicas validadas hasta completar fuentes técnicas verificadas.
CROPS = {
    "Anón": {"scientific": "Annona squamosa (por confirmar según nombre local)", "notes": "Confirmar especie, adaptación a temperatura y requerimientos de suelo con una ficha técnica local."},
    "Zapote": {"scientific": "Nombre común ambiguo; identificar especie", "notes": "El nombre zapote puede referirse a especies distintas. Confirmar nombre científico antes de evaluar aptitud."},
    "Arazá": {"scientific": "Eugenia stipitata", "notes": "Verificar adaptación local, requerimientos de humedad, drenaje y condiciones de establecimiento."},
    "Brevo": {"scientific": "Ficus carica (si se refiere a higuera); confirmar nombre local", "notes": "Confirmar qué especie se denomina brevo en el proyecto y revisar sus necesidades de clima y espacio."},
    "Caimito": {"scientific": "Chrysophyllum cainito (por confirmar)", "notes": "Confirmar identidad botánica y tamaño adulto; evaluar espacio, suelo, clima y disponibilidad de agua."},
    "Pomarrosa": {"scientific": "Syzygium jambos (por confirmar)", "notes": "El nombre común puede variar. Revisar identidad, tamaño adulto y posible comportamiento invasor en el contexto local."},
    "Guama": {"scientific": "Inga spp. (especie por confirmar)", "notes": "Identificar la especie de Inga y considerar tamaño adulto, función del cultivo y espacio disponible."},
    "Carambola": {"scientific": "Averrhoa carambola", "notes": "Verificar condiciones de temperatura, drenaje, exposición, manejo y tamaño del árbol."},
    "Madroño": {"scientific": "Garcinia madruno (si es la especie deseada)", "notes": "Confirmar identidad. Evaluar el espacio para el árbol adulto, suelo, drenaje, clima y luz."},
    "Chirimoya": {"scientific": "Annona cherimola", "notes": "La adaptación depende de temperatura, altitud y variedad; no asumir que un clima cálido es apropiado sin datos."},
}

st.markdown("""
<style>
.stApp { background: #f7f8f3; }
.hero { padding: 1.5rem; border-radius: 18px; background: linear-gradient(120deg,#e5f0dc,#f4f5e9); border: 1px solid #d7e4cf; }
.eyebrow { color:#456b42; font-weight:700; letter-spacing:.08em; font-size:.78rem; text-transform:uppercase; }
.hero h1 { color:#183c28; margin:.25rem 0 .4rem 0; }
.hero p { color:#395343; font-size:1.05rem; margin-bottom:0; }
</style>
<div class="hero">
<div class="eyebrow">La Última Cosecha · demostración académica</div>
<h1>🌱 AgroGuía IA</h1>
<p>Explora qué fruto podrías cultivar según tu ubicación, espacio y recursos disponibles.</p>
</div>
""", unsafe_allow_html=True)

st.write("")
st.info("Prototipo demostrativo: aún no consulta clima en tiempo real ni contiene una base agronómica validada. Las salidas son orientativas y no sustituyen asesoría profesional.")

with st.sidebar:
    st.header("Tu espacio de cultivo")
    location = st.text_input("Ubicación", "Cali, Valle del Cauca")
    climate = st.selectbox("Clima percibido", ["Cálido", "Templado", "Frío", "No estoy seguro"])
    altitude = st.number_input("Altitud aproximada (m s. n. m.), si la conoces", min_value=0, max_value=5000, value=0, step=50)
    area = st.number_input("Área disponible (m²)", min_value=0.1, max_value=100000.0, value=10.0, step=1.0)
    space = st.selectbox("Tipo de espacio", ["Balcón o materas", "Patio o jardín", "Huerta", "Parcela o terreno amplio"])
    water = st.selectbox("Disponibilidad de agua", ["Abundante", "Regular", "Principalmente lluvia", "Muy limitada", "No sé"])
    sunlight = st.selectbox("Exposición solar", ["Sol directo varias horas", "Sol parcial", "Principalmente sombra", "No sé"])
    soil = st.selectbox("Tipo de suelo", ["No sé", "Arcilloso", "Arenoso", "Franco", "Otro / mezcla de sustrato"])
    drainage = st.selectbox("Drenaje del terreno", ["No sé", "Drena bien", "Se encharca"])
    goal = st.selectbox("Objetivo", ["Obtener frutos", "Aprender a cultivar", "Restauración / biodiversidad", "Sombra u ornamental"])

mode = st.radio("¿Cómo quieres empezar?", ["Tengo un fruto en mente", "Recomiéndame cuáles investigar"], horizontal=True)
selected = st.selectbox("Fruto de interés", list(CROPS.keys())) if mode == "Tengo un fruto en mente" else None

st.subheader("Tu orientación preliminar")
if st.button("Analizar condiciones", type="primary", use_container_width=True):
    st.write(f"**Ubicación registrada:** {location or 'No indicada'}  ·  **Área:** {area:g} m²")
    if mode == "Tengo un fruto en mente":
        crop = CROPS[selected]
        st.markdown(f"### {selected}")
        st.caption(f"Identidad botánica de referencia: {crop['scientific']}")
        st.warning("Viabilidad por confirmar: todavía no hay suficientes datos técnicos validados para emitir una recomendación agronómica.")
        st.write(crop["notes"])
        st.markdown("**Datos que ayudarían a afinar la evaluación**")
        missing = []
        if altitude == 0: missing.append("altitud aproximada")
        if soil == "No sé": missing.append("tipo de suelo o sustrato")
        if drainage == "No sé": missing.append("drenaje")
        if sunlight == "No sé": missing.append("horas de sol directo")
        if water == "No sé": missing.append("disponibilidad real de agua en épocas secas")
        missing += ["nombre científico confirmado del fruto", "ficha técnica aplicable a la zona", "espacio requerido por la planta adulta"]
        for item in missing:
            st.write(f"- {item.capitalize()}")
        st.markdown("**Siguiente paso**")
        st.write("Contrastar los datos del sitio con una ficha técnica confiable y documentar la fuente antes de recomendar la siembra.")
    else:
        st.write("La aplicación puede organizar una lista de cultivos para investigar, pero aún no debe ordenarlos por viabilidad: primero hay que cargar los requerimientos agronómicos validados de las diez especies.")
        for name, data in CROPS.items():
            with st.expander(f"🌿 {name} — ficha pendiente de validar"):
                st.caption(data["scientific"])
                st.write(data["notes"])
    with st.expander("Fuentes y transparencia"):
        st.markdown("""
        - [AGROSAVIA — Sistema Experto MAPA](https://semapa.agrosavia.co/), referente para apoyo a decisiones agrícolas.
        - [Descripción institucional del Sistema Experto MAPA](https://www.agrosavia.co/productos-y-servicios/oferta-tecnol%C3%B3gica/l%C3%ADnea-agr%C3%ADcola/cultivos-transitorios-y-agroindustriales/sistemas-de-informaci%C3%B3n/723-sistema-experto-mapa).
        - Las identidades botánicas señaladas como “por confirmar” deben verificarse con el equipo del proyecto y fuentes botánicas/agronómicas. No se generan diagnósticos ni predicciones de rendimiento.
        """)
else:
    st.write("Completa los datos del espacio en el panel lateral y selecciona una modalidad. Luego pulsa **Analizar condiciones**.")
    st.markdown("#### ¿Cómo se decidirá la compatibilidad?")
    st.write("La futura versión comparará cada cultivo con clima, altitud, suelo, drenaje, agua, luz y espacio adulto. Si falta información crítica, pedirá aclaraciones en vez de inventar una recomendación.")

st.divider()
st.caption("AgroGuía IA · La Última Cosecha · prototipo académico no validado para decisiones reales.")
