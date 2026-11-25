
import streamlit as st

st.set_page_config(
    page_title="AgroGuía IA | La Última Cosecha",
    page_icon="🌱",
    layout="wide"
)

# =====================================================
# 1. INFORMACIÓN DOCUMENTADA DE LOS CULTIVOS
# =====================================================

CROPS = {
    "Madroño": {
        "scientific": "Garcinia madruno",
        "family": "Clusiaceae (familia por verificar)",
        "ranges": {
            "temperature": (22, 28),
            "rainfall": (1200, 1500),
            "altitude": (0, 1800)
        },
        "drainage": ["Drena bien"],
        "sunlight": ["Sol directo varias horas", "Sol parcial"],
        "water": "Requiere humedad regular, sin saturación del terreno.",
        "soil_info": "Se adapta a diferentes suelos. Se reportan suelos francos o franco-arenosos.",
        "space": "Distancia de siembra estimada: 6 x 6 m a 8 x 8 m.",
        "notes": "Árbol nativo de regiones tropicales de América. Alcanza aproximadamente 8 a 15 m de altura. Su mejor desarrollo se reporta entre 22 y 28 °C y con 1.200 a 1.500 mm de precipitación anual.",
        "gaps": "Validar requerimientos en el Valle del Cauca y verificar los datos de suelo, luz y espaciamiento."
    },

    "Anón": {
        "scientific": "Annona squamosa L.",
        "family": "Annonaceae",
        "ranges": {
            "ph": (5.5, 6.5)
        },
        "drainage": ["Drena bien"],
        "sunlight": ["Sol directo varias horas", "Sol parcial"],
        "water": "Tolera períodos secos, pero requiere riego durante la floración.",
        "soil_info": "Se adapta a diferentes suelos bien drenados, incluidos los arenosos y calcáreos.",
        "space": "Distancia de siembra reportada: 4,5 a 6 m.",
        "notes": "Árbol pequeño o arbusto de clima tropical. Puede alcanzar entre 3 y 8 m de altura. Tiene raíces superficiales y débiles. No tolera suelos inundados ni heladas.",
        "gaps": "Faltan datos sólidos de temperatura, precipitación y altitud. El pH de 5,5 a 6,5 procede de Growables; otra referencia secundaria presenta un intervalo diferente."
    },

    "Carambola": {
        "scientific": "Averrhoa carambola L.",
        "family": "Oxalidaceae",
        "ranges": {
            "ph": (5.0, 6.8)
        },
        "drainage": ["Drena bien"],
        "sunlight": ["Sol directo varias horas"],
        "water": "Necesita disponibilidad de agua alta y uniforme. Se reportan aproximadamente 1.800 mm anuales como referencia, no como rango límite.",
        "soil_info": "Se reportan suelos francos o franco-areno-arcillosos, ricos en materia orgánica.",
        "space": "Distancia de siembra reportada: 5 x 5 m a 6 x 6 m.",
        "notes": "Árbol o arbusto frutal de origen asiático tropical. Alcanza aproximadamente 3 a 5 m según SINCHI. Tiene sistema radicular profundo y se propaga por semillas.",
        "gaps": "Faltan rangos cuantitativos confiables de temperatura, precipitación y altitud, además de validación regional."
    },

    "Guama": {
        "scientific": "Inga edulis",
        "family": "Mimosaceae (Leguminosae, según SINCHI)",
        "ranges": {
            "ph": (4.5, 7.5)
        },
        "drainage": ["Drena bien", "Se encharca"],
        "sunlight": [],
        "water": "La fuente consultada reporta tolerancia a inundaciones estacionales breves.",
        "soil_info": "Se adapta a suelos arenosos, francos o arcillosos. Puede contribuir a mejorar suelos pobres mediante fijación de nitrógeno.",
        "space": "Árbol de copa amplia y redondeada. Se requiere definir el espacio de plantación según el desarrollo adulto.",
        "notes": "Árbol del trópico americano, de aproximadamente 3 a 10 m de altura. Presenta raíces profundas, crecimiento rápido y propagación por semillas.",
        "gaps": "Faltan datos comparables de temperatura, precipitación, altitud, luz, espaciamiento y rendimiento."
    },

    "Zapote": {
        "scientific": "Matisia cordata Humb. & Bonpl.",
        "family": "Bombacaceae (según SINCHI; verificar taxonomía)",
        "ranges": {},
        "drainage": ["Drena bien"],
        "sunlight": ["Sol directo varias horas"],
        "water": "Se reporta sensibilidad a la sequía.",
        "soil_info": "Se recomienda suelo rico en materia orgánica y ligeramente ácido.",
        "space": "Árbol de aproximadamente 10 m de altura. Falta establecer una distancia de siembra confiable.",
        "notes": "Árbol frutal de la región norte de Suramérica. Produce frutos de pulpa anaranjada, dulce y fibrosa. Las fuentes presentan diferencias sobre profundidad de raíces y velocidad de crecimiento.",
        "gaps": "Faltan rangos climáticos, pH cuantitativo, precipitación, altitud, rendimiento y validación local. Existen contradicciones sobre raíces y crecimiento."
    },

    "Caimito": {
        "scientific": "Pouteria caimito",
        "family": "Sapotaceae",
        "ranges": {},
        "drainage": [],
        "sunlight": [],
        "water": "No hay información hídrica suficiente para realizar una comparación.",
        "soil_info": "No hay datos suficientes sobre textura, pH o drenaje.",
        "space": "Árbol de aproximadamente 5 a 10 m de altura.",
        "notes": "Árbol originario de la cuenca amazónica. Presenta raíces profundas, propagación por semillas y crecimiento moderadamente rápido.",
        "gaps": "Faltan datos de clima, altitud, precipitación, suelo, agua, luz, espaciamiento y rendimiento."
    },

    "Arazá": {
        "scientific": "Eugenia stipitata",
        "family": "Myrtaceae",
        "ranges": {},
        "drainage": [],
        "sunlight": [],
        "water": "No hay un requerimiento hídrico cuantitativo suficientemente documentado en el material.",
        "soil_info": "Se menciona adaptación a suelos pobres y ácidos, sin un rango de pH confirmado.",
        "space": "Se describe como arbusto cercano a 3 m, aunque existen reportes de individuos silvestres de mayor altura.",
        "notes": "Especie amazónica de clima tropical y subtropical. Es sensible a las heladas. Se propaga por semillas y su fruto es altamente perecedero.",
        "gaps": "Faltan rangos confiables de temperatura, precipitación, altitud, pH, drenaje, luz y validación en el Valle del Cauca."
    },

    "Pomarrosa": {
        "scientific": "Syzygium jambos (L.) Alston",
        "family": "Myrtaceae",
        "ranges": {
            "ph": (5.5, 7.0)
        },
        "drainage": ["Drena bien", "Se encharca"],
        "sunlight": ["Sol directo varias horas", "Sol parcial", "Principalmente sombra"],
        "water": "Los árboles establecidos toleran períodos secos breves; las sequías prolongadas son perjudiciales.",
        "soil_info": "Tolera una variedad amplia de tipos de suelo, incluso condiciones de drenaje imperfecto.",
        "space": "Árbol de aproximadamente 6 a 12 m de altura, con copa densa.",
        "notes": "Árbol tropical originario del sudeste asiático. Se propaga por semillas, acodo aéreo e injerto. Se reporta una fase juvenil de aproximadamente 4 a 5 años.",
        "gaps": "Faltan datos completos de temperatura, precipitación, altitud, rendimiento y evaluación ecológica local. La posible invasividad debe verificarse en Colombia."
    },

    "Brevo": {
        "scientific": "Ficus carica L.",
        "family": "Moraceae",
        "ranges": {
            "ph": (5.5, 8.0)
        },
        "drainage": [],
        "sunlight": ["Sol directo varias horas"],
        "water": "El estrés hídrico puede reducir el rendimiento. El riego es importante durante el establecimiento y las sequías prolongadas.",
        "soil_info": "Tolera diversos tipos de suelo.",
        "space": "Desarrolla raíces extensas y profundas. Su extensión puede superar los 3,7 m.",
        "notes": "Especie de origen mediterráneo. Requiere pleno sol. Algunas variedades necesitan horas de frío, pero esta necesidad depende del cultivar.",
        "gaps": "Falta verificar su adaptación a las condiciones tropicales cálidas y húmedas de Cali, así como identificar variedades apropiadas."
    },

    "Chirimoya": {
        "scientific": "Annona cherimola Mill.",
        "family": "Annonaceae",
        "ranges": {
            "ph": (6.5, 7.6)
        },
        "drainage": ["Drena bien"],
        "sunlight": ["Sol directo varias horas"],
        "water": "Requiere humedad relativamente uniforme. No tolera encharcamientos.",
        "soil_info": "Se recomienda suelo rico, franco y bien drenado.",
        "space": "Árbol de aproximadamente 5 a 9 m de altura.",
        "notes": "Árbol subtropical de crecimiento lento. La polinización manual puede ser necesaria para mejorar el cuajado de frutos. Se reporta cultivo hasta aproximadamente 1.524 m en las referencias consultadas.",
        "gaps": "Falta validar su adaptación al clima cálido de Cali. Los requerimientos de frío y altitud dependen de las condiciones regionales y del cultivar."
    }
}


# =====================================================
# 2. FUNCIONES DE EVALUACIÓN
# =====================================================

def evaluate_crop(name, data):
    crop = CROPS[name]
    alerts = []
    missing = []
    evaluated = []

    numeric_inputs = {
        "temperature": (data["temperature"], "temperatura"),
        "rainfall": (data["rainfall"], "precipitación anual"),
        "ph": (data["soil_ph"], "pH del suelo"),
        "altitude": (data["altitude"], "altitud")
    }

    # Comparación de rangos numéricos documentados
    for key, (value, label) in numeric_inputs.items():
        if key in crop["ranges"]:
            if value == 0:
                missing.append(label)
            else:
                minimum, maximum = crop["ranges"][key]
                evaluated.append(label)

                if not minimum <= value <= maximum:
                    alerts.append(
                        f"La {label} registrada ({value}) está fuera "
                        f"del rango documentado ({minimum}–{maximum})."
                    )

    # Comparación del drenaje
    if crop["drainage"]:
        if data["drainage"] == "No sé":
            missing.append("drenaje")
        else:
            evaluated.append("drenaje")
            if data["drainage"] not in crop["drainage"]:
                alerts.append(
                    "El drenaje registrado requiere revisión frente "
                    "a las condiciones documentadas del cultivo."
                )

    # Comparación de exposición solar
    if crop["sunlight"]:
        if data["sunlight"] == "No sé":
            missing.append("exposición solar")
        else:
            evaluated.append("exposición solar")
            if data["sunlight"] not in crop["sunlight"]:
                alerts.append(
                    "La exposición solar registrada requiere revisión "
                    "frente a las condiciones documentadas del cultivo."
                )

    # Comparación del tipo de suelo cuando existe información
    if data["soil"] == "No sé":
        if crop["soil_info"]:
            missing.append("tipo de suelo")
    elif crop["soil_info"]:
        evaluated.append("tipo de suelo")

    # Estado de la evaluación
    if alerts:
        status = "Requiere atención"
    elif missing or not evaluated:
        status = "Información insuficiente"
    else:
        status = "Evaluación parcial: sin alertas en los criterios evaluados"

    return status, alerts, missing, evaluated


# =====================================================
# 3. DISEÑO DE LA APLICACIÓN
# =====================================================

st.markdown("""
<style>
.stApp {
    background: #f7f8f3;
}
.hero {
    padding: 1.5rem;
    border-radius: 18px;
    background: linear-gradient(120deg,#e5f0dc,#f4f5e9);
    border: 1px solid #d7e4cf;
}
.eyebrow {
    color:#456b42;
    font-weight:700;
    letter-spacing:.08em;
    font-size:.78rem;
    text-transform:uppercase;
}
.hero h1 {
    color:#183c28;
    margin:.25rem 0 .4rem 0;
}
.hero p {
    color:#395343;
    font-size:1.05rem;
    margin-bottom:0;
}
</style>

<div class="hero">
<div class="eyebrow">La Última Cosecha · demostración académica</div>
<h1>🌱 AgroGuía IA</h1>
<p>Explora qué frutos podrías cultivar según las condiciones de tu espacio.</p>
</div>
""", unsafe_allow_html=True)


# =====================================================
# 4. DATOS DEL ESPACIO DE CULTIVO
# =====================================================

with st.sidebar:
    st.header("Tu espacio de cultivo")

    location = st.text_input(
        "Ubicación",
        "Cali, Valle del Cauca"
    )

    climate = st.selectbox(
        "Clima percibido",
        ["Cálido", "Templado", "Frío", "No estoy seguro"]
    )

    temperature = st.number_input(
        "Temperatura promedio (°C), si la conoces",
        min_value=0.0,
        max_value=50.0,
        value=0.0,
        step=0.5
    )

    rainfall = st.number_input(
        "Precipitación anual (mm), si la conoces",
        min_value=0,
        max_value=10000,
        value=0,
        step=100
    )

    soil_ph = st.number_input(
        "pH del suelo (0 si no lo conoces)",
        min_value=0.0,
        max_value=14.0,
        value=0.0,
        step=0.1
    )

    altitude = st.number_input(
        "Altitud aproximada (m s. n. m.), si la conoces",
        min_value=0,
        max_value=5000,
        value=0,
        step=50
    )

    area = st.number_input(
        "Área disponible (m²)",
        min_value=0.1,
        max_value=100000.0,
        value=10.0,
        step=1.0
    )

    space = st.selectbox(
        "Tipo de espacio",
        ["Balcón o materas", "Patio o jardín", "Huerta", "Parcela o terreno amplio"]
    )

    water = st.selectbox(
        "Disponibilidad de agua",
        ["Abundante", "Regular", "Principalmente lluvia", "Muy limitada", "No sé"]
    )

    sunlight = st.selectbox(
        "Exposición solar",
        ["Sol directo varias horas", "Sol parcial", "Principalmente sombra", "No sé"]
    )

    soil = st.selectbox(
        "Tipo de suelo",
        ["No sé", "Arcilloso", "Arenoso", "Franco", "Otro / mezcla de sustrato"]
    )

    drainage = st.selectbox(
        "Drenaje del terreno",
        ["No sé", "Drena bien", "Se encharca"]
    )

    goal = st.selectbox(
        "Objetivo",
        ["Obtener frutos", "Aprender a cultivar", "Restauración / biodiversidad", "Sombra u ornamental"]
    )


# =====================================================
# 5. SELECCIÓN DEL CULTIVO
# =====================================================

mode = st.radio(
    "¿Cómo quieres empezar?",
    ["Tengo un fruto en mente", "Recomiéndame cuáles investigar"],
    horizontal=True
)

selected = (
    st.selectbox("Fruto de interés", list(CROPS.keys()))
    if mode == "Tengo un fruto en mente"
    else None
)


# =====================================================
# 6. RESULTADOS
# =====================================================

st.subheader("Tu orientación preliminar")

if st.button("Analizar condiciones", type="primary", use_container_width=True):

    data = {
        "temperature": temperature,
        "rainfall": rainfall,
        "soil_ph": soil_ph,
        "altitude": altitude,
        "soil": soil,
        "drainage": drainage,
        "sunlight": sunlight
    }

    st.write(
        f"**Ubicación:** {location or 'No indicada'}"
        f" · **Área:** {area:g} m²"
    )

    st.info(
        "La evaluación compara únicamente los criterios para los que "
        "existen datos documentados. No determina por sí sola la viabilidad "
        "del cultivo ni reemplaza una valoración agronómica."
    )

    if mode == "Tengo un fruto en mente":
        crops_to_evaluate = [selected]
    else:
        crops_to_evaluate = list(CROPS.keys())

    for name in crops_to_evaluate:
        crop = CROPS[name]

        status, alerts, missing, evaluated = evaluate_crop(name, data)

        with st.container():
            st.markdown(f"### 🌿 {name}")
            st.caption(f"Nombre científico: {crop['scientific']}")
            st.caption(f"Familia: {crop['family']}")

            if status == "Requiere atención":
                st.warning(status)
            elif status == "Información insuficiente":
                st.info(status)
            else:
                st.success(status)

            if evaluated:
                st.markdown("**Criterios evaluados:**")
                st.write(", ".join(evaluated))

            if alerts:
                st.markdown("**Condiciones que requieren atención:**")
                for alert in alerts:
                    st.write(f"- {alert}")

            if missing:
                st.markdown("**Datos pendientes de evaluación:**")
                for item in missing:
                    st.write(f"- {item.capitalize()}")

            st.markdown("**Información del cultivo:**")
            st.write(crop["notes"])

            st.markdown("**Suelo:**")
            st.write(crop["soil_info"])

            st.markdown("**Agua:**")
            st.write(crop["water"])

            st.markdown("**Espacio:**")
            st.write(crop["space"])

            st.markdown("**Información pendiente de completar:**")
            st.write(crop["gaps"])

            st.divider()

    with st.expander("Fuentes y transparencia"):
        st.markdown("""
        **Fuentes documentales del proyecto:**

        - Parques Nacionales Naturales de Colombia (2025).
        - SINCHI: Descripción de árboles y arbustos en la ciudad de Leticia.
        - Growables: fichas de especies frutales.
        - iNaturalist: Eugenia stipitata.
        - Otras referencias técnicas consignadas en el documento de investigación.

        Los datos se presentan como referencias documentales y no como
        garantías de adaptación al Valle del Cauca.

        La ausencia de alertas no garantiza que un cultivo sea viable.
        Los resultados no constituyen diagnósticos ni predicciones de rendimiento.
        """)

else:
    st.write(
        "Completa los datos del espacio en el panel lateral, "
        "selecciona una modalidad y pulsa **Analizar condiciones**."
    )
