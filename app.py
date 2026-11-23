import streamlit as st

st.set_page_config(page_title="AgroGuía IA | La Última Cosecha", page_icon="🌱", layout="wide")


CROPS = {
    "Anón": {"scientific": "Annona squamosa"},
    "Zapote": {"scientific": "Matisia cordata"},
    "Arazá": {"scientific": "Eugenia stipitata"},
    "Brevo": {"scientific": "Ficus carica"},
    "Caimito": {"scientific": "Pouteria caimito"},
    "Pomarrosa": {"scientific": "Syzygium jambos"},
    "Guama": {"scientific": "Inga edulis"},
    "Carambola": {"scientific": "Averrhoa carambola"},
    "Madroño": {"scientific": "Garcinia madruno"},
    "Chirimoya": {"scientific": "Annona cherimola"},}


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
        st.caption(f"Nombre científico: {crop['scientific']}")
        st.info("Esta ficha presenta información documentada sobre el cultivo. La compatibilidad con tu terreno requiere comparar sus condiciones con los requerimientos agronómicos disponibles.")
        st.write(crop["notes"])
        st.markdown("**Datos que ayudarían a afinar la evaluación**")
        missing = []
        if altitude == 0: missing.append("altitud aproximada")
        if soil == "No sé": missing.append("tipo de suelo o sustrato")
        if drainage == "No sé": missing.append("drenaje")
        if sunlight == "No sé": missing.append("horas de sol directo")
        if water == "No sé": missing.append("disponibilidad real de agua en épocas secas")
       missing += ["ficha técnica aplicable a las condiciones de la zona", "espacio requerido por la planta adulta"]
        for item in missing:
            st.write(f"- {item.capitalize()}")
        st.markdown("**Siguiente paso**")
        st.write("Contrastar los datos del sitio con una ficha técnica confiable y documentar la fuente antes de recomendar la siembra.")
    else:
      st.write("AgroGuía IA presenta los cultivos incluidos en su base documental. La comparación de compatibilidad se realizará a partir de los requerimientos agronómicos registrados y las condiciones del terreno del usuario.")
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
  st.write("La herramienta utiliza información agronómica documentada para contrastar las condiciones del terreno con los requerimientos de cada cultivo. Cuando no dispone de datos suficientes, señala las limitaciones de la evaluación y evita emitir conclusiones sin respaldo.")

st.divider()
st.caption("AgroGuía IA · La Última Cosecha · prototipo académico no validado para decisiones reales.")
