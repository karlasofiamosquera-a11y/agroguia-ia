import streamlit as st

st.set_page_config(page_title="AgroGuía IA | La Última Cosecha", page_icon="🌱", layout="wide")



CROPS = {
    "Anón": {
        "scientific": "Annona squamosa L.",
        "notes": "Familia: Annonaceae. Árbol pequeño de clima tropical. Prefiere suelos bien drenados. Tolera periodos secos, pero no el encharcamiento. Pendiente: validar condiciones específicas para el Valle del Cauca."
    },
    "Zapote": {
        "scientific": "Matisia cordata Humb. & Bonpl.",
        "notes": "Árbol frutal de la familia Bombacaceae según la fuente consultada. Prefiere exposición soleada y suelos ricos en materia orgánica. Hay diferencias entre las fuentes sobre el crecimiento y la profundidad de sus raíces. Pendiente: validar condiciones locales."
    },
    "Arazá": {
        "scientific": "Eugenia stipitata",
        "notes": "Familia: Myrtaceae. Especie amazónica de clima tropical y subtropical, sensible a las heladas. Se propaga por semillas. Su fruto es muy perecedero. Pendiente: completar requerimientos climáticos y de suelo para el Valle del Cauca."
    },
    "Brevo": {
        "scientific": "Ficus carica L.",
        "notes": "Familia: Moraceae. Especie de origen mediterráneo. Requiere buena exposición solar y suelos bien drenados. La disponibilidad de agua influye en su producción. Pendiente: evaluar su adaptación a las condiciones tropicales de Cali."
    },
    "Caimito": {
        "scientific": "Pouteria caimito",
        "notes": "Familia: Sapotaceae. Árbol frutal originario de la cuenca amazónica. Presenta raíces profundas y propagación por semillas. Pendiente: completar requerimientos de clima, suelo, agua y luz."
    },
    "Pomarrosa": {
        "scientific": "Syzygium jambos (L.) Alston",
        "notes": "Familia: Myrtaceae. Árbol tropical que tolera diferentes tipos de suelo y condiciones de luz. Puede soportar periodos secos cortos. Presenta potencial invasor en algunas regiones. Pendiente: evaluar su comportamiento ecológico local."
    },
    "Guama": {
        "scientific": "Inga edulis",
        "notes": "Familia: Leguminosae, según la clasificación de la fuente consultada. Árbol tropical americano de crecimiento rápido, raíces profundas y copa amplia. Pendiente: completar requerimientos climáticos, hídricos y de suelo."
    },
    "Carambola": {
        "scientific": "Averrhoa carambola L.",
        "notes": "Familia: Oxalidaceae. Árbol o arbusto frutal de origen asiático, cultivado en regiones tropicales. Se propaga por semillas. Pendiente: completar información de clima, suelo, agua, luz y producción."
    },
    "Madroño": {
        "scientific": "Garcinia madruno",
        "notes": "Árbol frutal nativo de Colombia y otras regiones tropicales de América. Se desarrolla en temperaturas medias de 22 a 28 °C y precipitaciones reportadas de 1.200 a 1.500 mm anuales. Pendiente: completar datos de suelo, luz, agua y espacio."
    },
    "Chirimoya": {
        "scientific": "Annona cherimola Mill.",
        "notes": "Familia: Annonaceae. Árbol frutal subtropical que requiere suelos bien drenados y humedad relativamente constante. La polinización manual puede ser necesaria para mejorar la fructificación. Pendiente: evaluar su adaptación al clima cálido de Cali."
    }
}


# Requerimientos documentados disponibles.
# Los valores ausentes se dejan como None: no se inventan.

REQUIREMENTS = {
    "Madroño": {
        "temperature": (22, 28),
        "rainfall": (1200, 1500),
        "altitude": (0, 1800),
        "drainage": "Drena bien"
    },
    "Anón": {
        "ph": (5.5, 7.5),
        "drainage": "Drena bien"
    },
    "Carambola": {
        "ph": (5.0, 6.8),
        "rainfall": (1800, 1800),
        "drainage": "Drena bien",
        "sunlight": ["Sol directo varias horas"]
    },
    "Arazá": {
        "ph": (4.0, 5.5),
        "rainfall": (2000, 3500),
        "drainage": "Drena bien"
    },
    "Pomarrosa": {
        "temperature": (20, 30),
        "rainfall": (1200, 1700),
        "altitude": (0, 2000),
        "ph": (5.5, 7.0)
    },
    "Brevo": {
        "ph": (5.5, 8.0),
        "sunlight": ["Sol directo varias horas"]
    },
    "Chirimoya": {
        "ph": (6.5, 7.6),
        "drainage": "Drena bien"
    },
    "Guama": {},
    "Zapote": {},
    "Caimito": {}
}


def evaluate_crop(name):
    requirements = REQUIREMENTS[name]
    alerts = []
    missing = []

    checks = {
        "temperature": (temperature, "temperatura"),
        "rainfall": (rainfall, "precipitación anual"),
        "ph": (soil_ph, "pH del suelo"),
        "altitude": (altitude, "altitud")
    }

    for key, (value, label) in checks.items():
        if key in requirements:
            if value == 0:
                missing.append(label)
            else:
                minimum, maximum = requirements[key]
                if not minimum <= value <= maximum:
                    alerts.append(
                        f"La {label} registrada ({value}) está fuera "
                        f"del rango documentado ({minimum}–{maximum})."
                    )

    if "drainage" in requirements:
        if drainage == "No sé":
            missing.append("drenaje")
        elif drainage != requirements["drainage"]:
            alerts.append(
                "El terreno presenta una condición de drenaje "
                "que requiere revisión frente a los requerimientos del cultivo."
            )

    if "sunlight" in requirements:
        if sunlight == "No sé":
            missing.append("exposición solar")
        elif sunlight not in requirements["sunlight"]:
            alerts.append(
                "La exposición solar registrada no coincide con "
                "la condición de luz documentada."
            )

    if not requirements:
        missing.append("requerimientos agronómicos documentados")

    if alerts:
        status = "Requiere atención"
    elif missing:
        status = "Información insuficiente"
    else:
        status = "Sin alertas en los criterios evaluados"

    return status, alerts, missing


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


with st.sidebar:
    st.header("Tu espacio de cultivo")
    location = st.text_input("Ubicación", "Cali, Valle del Cauca")
    climate = st.selectbox("Clima percibido", ["Cálido", "Templado", "Frío", "No estoy seguro"])
    temperature = st.number_input("Temperatura promedio (°C), si la conoces", min_value=0.0, max_value=50.0, value=0.0, step=0.5)
    rainfall = st.number_input("Precipitación anual (mm), si la conoces", min_value=0, max_value=10000, value=0, step=100)
    soil_ph = st.number_input("pH del suelo (0 si no lo conoces)", min_value=0.0, max_value=14.0, value=0.0, step=0.1)
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

    st.write(
        f"**Ubicación registrada:** {location or 'No indicada'}"
        f" · **Área:** {area:g} m²"
    )

    st.info(
        "Esta es una evaluación preliminar basada en los criterios "
        "documentados. No reemplaza una valoración agronómica."
    )

    if mode == "Tengo un fruto en mente":
        crops_to_evaluate = [selected]
    else:
        crops_to_evaluate = list(CROPS.keys())

    for name in crops_to_evaluate:
        status, alerts, missing = evaluate_crop(name)
        crop = CROPS[name]

        with st.container():
            st.markdown(f"### 🌿 {name}")
            st.caption(f"Nombre científico: {crop['scientific']}")

            if status == "Requiere atención":
                st.warning(status)
            elif status == "Información insuficiente":
                st.info(status)
            else:
                st.success(status)

            if alerts:
                st.markdown("**Condiciones que requieren atención:**")
                for alert in alerts:
                    st.write(f"- {alert}")

            if missing:
                st.markdown("**Datos o requisitos pendientes:**")
                for item in missing:
                    st.write(f"- {item.capitalize()}")

            if not alerts and not missing:
                st.write(
                    "No se encontraron alertas en los criterios "
                    "que esta versión puede evaluar."
                )

            st.caption(crop["notes"])
            st.divider()

    with st.expander("Fuentes y transparencia"):
        st.markdown("""
        - [AGROSAVIA — Sistema Experto MAPA](https://semapa.agrosavia.co/).
        - [Descripción institucional del Sistema Experto MAPA](https://www.agrosavia.co/productos-y-servicios/oferta-tecnol%C3%B3gica/l%C3%ADnea-agr%C3%ADcola/cultivos-transitorios-y-agroindustriales/sistemas-de-informaci%C3%B3n/723-sistema-experto-mapa).
        - Los rangos utilizados son referencias tomadas de las fuentes documentales del proyecto.
        - La ausencia de alertas no garantiza que el cultivo sea viable.
        - Los resultados no constituyen diagnósticos ni predicciones de rendimiento.
        """)

else:
    st.write(
        "Completa los datos del espacio en el panel lateral y "
        "selecciona una modalidad. Luego pulsa **Analizar condiciones**."
    )
