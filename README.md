# AgroGuía IA — La Última Cosecha

Demostración académica construida con Streamlit. Recoge ubicación, clima percibido, altitud aproximada, espacio, agua, luz, suelo, drenaje y objetivo del cultivo. Incluye los diez frutos definidos por el proyecto.

## Ejecutar localmente

1. Instala Python 3.10 o superior.
2. Abre una terminal en esta carpeta.
3. Ejecuta `pip install -r requirements.txt`.
4. Ejecuta `streamlit run app.py`.

## Compartir en línea

Puedes desplegar el proyecto en Streamlit Community Cloud después de subir `app.py` y `requirements.txt` a un repositorio de GitHub. Guía oficial: https://docs.streamlit.io/deploy/streamlit-community-cloud/deploy-your-app/deploy

## Limitaciones

Este prototipo es una demostración de interfaz y flujo. No integra aún un modelo generativo, datos climáticos en tiempo real ni fichas agronómicas validadas. Las identidades botánicas basadas en nombres comunes deben verificarse. No utilizar para decisiones reales de siembra hasta que especialistas validen las reglas y fuentes.

## Siguientes pasos

1. Confirmar nombres científicos de los diez cultivos.
2. Crear una tabla de requerimientos con fuente, fecha, región y nivel de confianza.
3. Implementar reglas de compatibilidad a partir de esa tabla.
4. Probar casos y revisar resultados con una persona experta en agronomía.
5. Incorporar IA generativa con recuperación de documentos y citas, evitando que invente información.
