import streamlit as st

st.set_page_config(page_title="Conclusiones", page_icon="✅", layout="wide")

st.title("✅ Conclusiones generales")

st.markdown("""
### Pregunta de investigación
¿Qué características tienen los usuarios que consumen más tiempo de contenido en la plataforma?

### Hallazgos del análisis EDA

**1. El consumo de contenido no es homogéneo — hay dos poblaciones diferenciadas**

La mayoría de los usuarios consume entre 500 y 1200 minutos/mes, pero existe un segmento
minoritario y bien diferenciado que consume entre 2500 y 4300 minutos/mes. No es una cola
gradual, sino un salto, lo que sugiere un patrón de uso cualitativamente distinto (posiblemente
uso más intensivo, o cuentas con múltiples perfiles activos).

**2. La edad es un factor relevante, pero de forma moderada**

El consumo alto se concentra mayormente entre los 15 y 60 años, y decae notablemente después
de los 60. La edad por sí sola no separa limpiamente a los grupos, pero sí actúa como un filtro.

**3. El plan de suscripción está asociado al consumo, pero no lo determina por completo**

Premium tiene el mayor promedio de minutos (1050) y Básico el menor (600). Sin embargo, los
tres planes tienen usuarios en el grupo de alto consumo, lo que indica que el plan es un
indicador parcial, no una etiqueta perfecta del perfil buscado.

**4. Conclusión del EDA**

El usuario de alto consumo no se explica por una sola variable, sino por una combinación:
tiende a tener entre 15-60 años, y aunque es más probable encontrarlo en plan Premium, existe
un grupo significativo de usuarios Básico/Estándar "sobre-consumiendo" para su plan actual.
Este grupo es el hallazgo más importante del análisis.

### Aporte del PCA

El análisis de componentes principales sobre edad, minutos de visualización y tickets de
soporte mostró que estas variables son relativamente independientes entre sí (baja
correlación), por lo que se necesitan los 3 componentes para explicar cerca del 100% de la
varianza. Esto confirma, desde otro ángulo, lo observado en el EDA: no existe una única
variable dominante que explique el comportamiento del usuario de alto consumo, sino una
combinación de factores.

### Conclusión final

Los usuarios que consumen más tiempo de contenido se caracterizan principalmente por estar en
un rango etario de 15 a 60 años, y aunque muestran mayor probabilidad de pertenecer al plan
Premium, el consumo elevado también aparece de forma significativa en usuarios de planes
Básico y Estándar. Esto indica que el alto consumo responde a un patrón de comportamiento más
que exclusivamente a la categoría de suscripción contratada.

**Recomendación:** con estas variables (edad, plan, minutos) podría construirse un modelo
predictivo para clasificar a nuevos usuarios como de alto o bajo consumo, y así diseñar
estrategias comerciales dirigidas (por ejemplo, ofrecer upgrades de plan a los usuarios
"Básico intensivos").
""")
