import streamlit as st
from utils import load_data

st.set_page_config(
    page_title="Streaming - Análisis de Usuarios",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Análisis de Usuarios - Plataforma de Streaming")

st.markdown("""
### Objetivo de investigación
Identificar el perfil de los usuarios que generan mayor tiempo de visualización en la
plataforma de streaming, para comprender sus características y aportar información que
permita diseñar estrategias orientadas a incrementar los ingresos y la retención de clientes.

### Pregunta de investigación
¿Qué características tienen los usuarios que consumen más tiempo de contenido en la plataforma?
""")

st.divider()

st.markdown("""
### Cómo navegar esta aplicación

Usá el menú de la izquierda para recorrer el análisis:

- **📁 Dataset**: vista general de los datos utilizados.
- **📈 EDA**: análisis exploratorio univariado, bivariado y multivariado.
- **🧮 PCA**: análisis de componentes principales sobre las variables numéricas.
- **✅ Conclusiones**: síntesis de los hallazgos del proyecto.
""")

df = load_data()
st.caption(f"Dataset cargado: {df.shape[0]} usuarios, {df.shape[1]} variables.")
