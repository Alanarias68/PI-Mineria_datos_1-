import streamlit as st
from utils import load_data

st.set_page_config(page_title="Dataset", page_icon="📁", layout="wide")

st.title("📁 Dataset")

df = load_data()

st.markdown("""
Se trabaja con un conjunto de datos de usuarios de una plataforma de streaming,
previamente limpio (sin nulos, negativos ni outliers no justificados), que incluye
variables demográficas y de comportamiento de consumo.
""")

st.subheader("Vista previa de los datos")
st.dataframe(df.head(10), use_container_width=True)

col1, col2 = st.columns(2)

with col1:
    st.subheader("Dimensiones")
    st.write(f"Filas: **{df.shape[0]}**")
    st.write(f"Columnas: **{df.shape[1]}**")

with col2:
    st.subheader("Tipos de datos")
    st.dataframe(df.dtypes.astype(str).rename("Tipo"), use_container_width=True)

st.subheader("Estadísticas descriptivas")
st.dataframe(df.describe(), use_container_width=True)
