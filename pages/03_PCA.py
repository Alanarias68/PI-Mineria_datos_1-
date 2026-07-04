import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from utils import load_data

st.set_page_config(page_title="PCA", page_icon="🧮", layout="wide")

st.title("🧮 Análisis de Componentes Principales (PCA)")

st.markdown("""
En esta etapa se aplica el Análisis de Componentes Principales (PCA) para reducir la
dimensionalidad de las variables numéricas del conjunto de datos, conservando la mayor
cantidad posible de información. Esto permite identificar patrones entre las variables y
facilitar la interpretación del comportamiento de los usuarios con mayor tiempo de visualización.
""")

df = load_data()

variables = df[["edad", "minutos_visualizacion_mensual", "tickets_soporte_cliente"]]

st.subheader("Variables numéricas utilizadas")
st.dataframe(variables.head(), use_container_width=True)

st.markdown("""
Antes de aplicar el PCA es necesario escalar las variables, ya que presentan diferentes
unidades de medida. El método `StandardScaler` estandariza cada variable para que tenga
media 0 y desviación estándar 1, evitando que una variable con valores más grandes tenga
mayor influencia en el análisis.
""")

scaler = StandardScaler()
variables_escaladas = scaler.fit_transform(variables)

pca = PCA()
componentes = pca.fit_transform(variables_escaladas)

st.subheader("Varianza explicada por componente")

varianza = pd.DataFrame({
    "Componente": range(1, len(pca.explained_variance_ratio_) + 1),
    "Varianza explicada": pca.explained_variance_ratio_,
    "Varianza acumulada": pca.explained_variance_ratio_.cumsum()
})

st.dataframe(varianza, use_container_width=True)

fig, ax = plt.subplots(figsize=(8, 5))
ax.plot(varianza["Componente"], varianza["Varianza acumulada"], marker="o")
ax.set_title("Varianza acumulada explicada por el PCA")
ax.set_xlabel("Número de componentes")
ax.set_ylabel("Varianza acumulada")
ax.grid(True)
st.pyplot(fig)

st.markdown("""
Este gráfico muestra la varianza acumulada explicada por el PCA. En el eje X está el número
de componentes principales y en el eje Y el porcentaje acumulado de varianza que esos
componentes logran capturar.

Se observa lo siguiente:
- Con 1 componente se explica aproximadamente el 35% de la varianza total.
- Con 2 componentes se explica cerca del 68-70%.
- Con 3 componentes se explica aproximadamente el 100% (lógico, ya que el dataset tiene solo
3 variables numéricas).

La curva no muestra un "codo" muy marcado; sube de forma bastante lineal, lo que sugiere que
las 3 variables originales aportan información relativamente similar entre sí, sin mucha
redundancia. Para retener al menos 80-90% de la varianza se necesitan los 3 componentes: en
este caso el PCA no permite reducir mucho la dimensionalidad sin perder información relevante.

**En conclusión:** con solo 3 variables numéricas de entrada, probablemente no haga falta
aplicar PCA como técnica de reducción; esto tiene más sentido cuando se tienen muchas variables
correlacionadas entre sí.
""")

st.subheader("Cargas de los componentes principales")

componentes_df = pd.DataFrame(
    pca.components_,
    columns=variables.columns,
    index=[f"CP{i+1}" for i in range(len(variables.columns))]
)

st.dataframe(componentes_df, use_container_width=True)

st.markdown("""
El PCA se aplicó sobre las variables **edad**, **minutos de visualización mensual** y
**tickets de soporte al cliente**, con el fin de identificar combinaciones lineales que
resuman la variabilidad del dataset.

Los resultados muestran que:
- **CP1** está determinado principalmente por los minutos de visualización mensual (carga de
0.72) y, en sentido opuesto, por los tickets de soporte al cliente (carga de -0.68), con
escasa influencia de la edad. Puede interpretarse como un eje que contrapone el nivel de
consumo de contenido con el nivel de reclamos generados por el usuario.
- **CP2** está explicado casi en su totalidad por la variable edad (carga de 0.92),
constituyendo prácticamente un eje etario independiente de las demás variables.
- **CP3** combina las tres variables con pesos moderados, oponiendo la edad (carga de -0.38)
al consumo y los tickets de soporte, que presentan cargas similares y de igual signo (0.67 y
0.64 respectivamente).

Dado que las tres variables originales presentan una correlación relativamente baja entre sí,
el PCA no logró concentrar la varianza en uno o dos componentes: se requieren los tres
componentes principales para explicar aproximadamente el 100% de la varianza total. Esto
indica que, si bien la técnica permitió identificar patrones de asociación entre las
variables, no resultó eficaz como método de reducción de dimensionalidad para este conjunto
de datos particular.
""")
