import streamlit as st
import matplotlib.pyplot as plt
from utils import load_data

st.set_page_config(page_title="EDA", page_icon="📈", layout="wide")

st.title("📈 Análisis Exploratorio de Datos (EDA)")

df = load_data()

# ---------------------------------------------------------------
# Análisis univariado
# ---------------------------------------------------------------
st.header("Análisis univariado")

st.subheader("Distribución del tiempo de visualización mensual")
fig, ax = plt.subplots(figsize=(8, 5))
ax.hist(df["minutos_visualizacion_mensual"], bins=20, edgecolor="black")
ax.set_title("Distribución del tiempo de visualización mensual")
ax.set_xlabel("Minutos de visualización")
ax.set_ylabel("Cantidad de usuarios")
st.pyplot(fig)

st.markdown("""
Se visualiza la cantidad de usuarios según los minutos que visualizan, para saber qué
cantidad de usuarios consume más tiempo la plataforma.

Se observa lo siguiente:
- La distribución tiene forma asimétrica hacia la derecha. La masa de usuarios se concentra
entre 500 y 1200 minutos mensuales, con el pico más alto (1800 usuarios) alrededor de 700-800 minutos.
- Después de los 1500 minutos la frecuencia cae abruptamente, formando una cola larga y delgada
que se extiende hasta 4000+ minutos, con muy pocos usuarios en esos valores.
- Esto indica que la mayoría de los clientes tiene un consumo moderado, mientras que un grupo
pequeño y minoritario consume cantidades mucho mayores de contenido: son los "outliers" o
usuarios de alto consumo que aparecen dispersos en la cola derecha.

**En resumen:** el consumo "típico" ronda los 700-900 minutos al mes, pero existe un grupo chico
de usuarios muy intensivos que se aleja bastante de ese comportamiento normal.
""")

st.subheader("Cantidad de usuarios por plan")
planes = df["plan_suscripcion"].value_counts()
fig, ax = plt.subplots(figsize=(7, 5))
ax.bar(planes.index, planes.values)
ax.set_title("Cantidad de usuarios por plan")
ax.set_xlabel("Plan")
ax.set_ylabel("Cantidad de usuarios")
st.pyplot(fig)

st.markdown("""
Gráfico de barras que muestra la cantidad de usuarios según el tipo de plan al que están
suscriptos: Básico, Estándar y Premium, para determinar las preferencias de los clientes.

Se observa lo siguiente:
- El plan Básico concentra la mayor cantidad de usuarios, con cerca de 3600.
- El plan Estándar le sigue con aproximadamente 2800 usuarios.
- El plan Premium es el que menos usuarios tiene, alrededor de 1500.
- Se observa una relación decreciente: a medida que el plan es más caro, la base de usuarios se reduce.

**En resumen:** la base de usuarios está concentrada mayormente en el plan más barato, y se va
achicando a medida que subís de categoría hacia planes más premium.
""")

# ---------------------------------------------------------------
# Análisis bivariado
# ---------------------------------------------------------------
st.header("Análisis bivariado")

st.subheader("Promedio de minutos de visualización por plan")
promedio_plan = df.groupby("plan_suscripcion")["minutos_visualizacion_mensual"].mean()
fig, ax = plt.subplots(figsize=(7, 5))
ax.bar(promedio_plan.index, promedio_plan.values)
ax.set_title("Promedio de minutos de visualización por plan")
ax.set_xlabel("Plan")
ax.set_ylabel("Minutos promedio")
st.pyplot(fig)

st.markdown("""
Muestra el promedio de minutos de visualización mensual según el tipo de plan, buscando
alguna relación entre estas variables.

Se observa lo siguiente:
- El plan Básico tiene el promedio más bajo, alrededor de 600 minutos.
- El plan Estándar sube a cerca de 900 minutos.
- El plan Premium tiene el promedio más alto, cerca de 1050 minutos.
- Hay una relación creciente y clara: a mayor jerarquía del plan, mayor consumo promedio de contenido.

Cruzado con el gráfico anterior, se observa un patrón interesante: el plan Premium tiene la menor
cantidad de usuarios pero el mayor consumo promedio individual. Esto es un indicio fuerte de que
el tipo de plan es una característica relevante del perfil de "alto consumo".
""")

st.subheader("Relación entre edad y tiempo de visualización")
fig, ax = plt.subplots(figsize=(8, 5))
ax.scatter(df["edad"], df["minutos_visualizacion_mensual"], alpha=0.5)
ax.set_title("Relación entre edad y tiempo de visualización")
ax.set_xlabel("Edad")
ax.set_ylabel("Minutos de visualización")
st.pyplot(fig)

st.markdown("""
Cruza la edad de los usuarios con sus minutos de visualización mensual, para ver si existe
relación entre ambas variables.

Se ven dos grupos claramente separados (dos "nubes" de puntos):
- Un grupo grande y denso entre 0 y 1700 minutos, presente en todas las edades (de 10 a 80 años).
- Un segundo grupo, más disperso, ubicado entre 2500 y 4000 minutos, que se concentra sobre todo
entre los 15 y 60 años, y prácticamente desaparece después de los 60.

**En resumen:** ambos grupos muestran un comportamiento similar: los usuarios que más consumen
se encuentran entre los 15 y 60 años, un dato útil para la estrategia publicitaria de la empresa
y para especializar el contenido de la plataforma según ese rango etario.
""")

st.subheader("Promedio de minutos por género favorito")
promedio_genero = df.groupby("genero_favorito")["minutos_visualizacion_mensual"].mean()
fig, ax = plt.subplots(figsize=(8, 5))
ax.bar(promedio_genero.index, promedio_genero.values)
ax.set_title("Promedio de minutos por género favorito")
ax.set_xlabel("Género")
ax.set_ylabel("Minutos promedio")
st.pyplot(fig)

st.markdown("""
Se realiza este gráfico para observar si hay relación entre los minutos visualizados y el
género favorito, y determinar si este es determinante en los gustos de los usuarios.

**Se observa:** no existe una tendencia notoria; la mayoría de los géneros posee casi la misma
cantidad de minutos de visualización, lo que indica que el dataset está muy equilibrado y que
el género no tiene incidencia relevante para el propósito de esta investigación.
""")

# ---------------------------------------------------------------
# Análisis multivariado
# ---------------------------------------------------------------
st.header("Análisis multivariado")

st.subheader("Edad, plan y tiempo de visualización")

planes_unicos = df["plan_suscripcion"].unique()
planes_seleccionados = st.multiselect(
    "Filtrar por plan",
    options=list(planes_unicos),
    default=list(planes_unicos)
)

fig, ax = plt.subplots(figsize=(9, 6))
for plan in planes_unicos:
    if plan in planes_seleccionados:
        datos = df[df["plan_suscripcion"] == plan]
        ax.scatter(
            datos["edad"],
            datos["minutos_visualizacion_mensual"],
            alpha=0.6,
            label=plan
        )
ax.set_title("Edad, plan y tiempo de visualización")
ax.set_xlabel("Edad")
ax.set_ylabel("Minutos de visualización")
ax.legend(title="Plan")
st.pyplot(fig)

st.markdown("""
Es el mismo scatter de edad vs. minutos de visualización, pero coloreado según el plan del
usuario. Este análisis multivariado permite ver si la variable plan explica la separación en
dos grupos detectada antes.

Se observa lo siguiente:
- Los tres planes están mezclados tanto en la nube densa inferior (0-1700 min) como en la nube
superior (2500-4300 min). No es que "todo Premium" esté arriba y "todo Básico" abajo: hay
usuarios de los tres planes en ambos grupos.
- En la nube inferior predomina el plan Básico en la parte más baja, mientras que Premium tiende
a estar más presente en la franja superior de esa nube, coherente con que Premium consume más
en promedio.
- En la nube superior (alto consumo) hay una mezcla de los tres planes, sin un patrón dominante
muy marcado: hay usuarios Básico que consumen muchísimo, excelentes candidatos para ofrecerles
un plan mejor.
- El patrón de caída después de los 60 años se mantiene igual para los tres planes.

**En resumen:** el plan por sí solo no explica completamente quién es el usuario de alto consumo.
Conviene identificar a los "Básico intensivos" como el segmento más accionable para subirlos de
plan, ya que consumen como un Premium pero pagan como Básico.
""")
