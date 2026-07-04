Proyecto Integrador - Minería de Datos
Descripción
Este proyecto corresponde al Proyecto Integrador de la Tecnicatura en Gestión de Datos e Inteligencia Artificial. Consiste en el análisis de un dataset de usuarios de una plataforma de streaming, con el objetivo de determinar las preferencias y características de los usuarios que generan mayor consumo (minutos de visualización) en la plataforma.
El trabajo incluye limpieza de datos, análisis exploratorio (EDA), reducción de dimensionalidad mediante PCA, y una aplicación interactiva desarrollada en Streamlit para visualizar los resultados.
Objetivo de investigación
Identificar el perfil de los usuarios que generan mayor consumo de contenido en la plataforma, en base a variables como edad, minutos de visualización mensual, tipo de plan de suscripción, tickets de soporte al cliente, entre otras.
Estructura del repositorio
├── notebooks/              # Notebooks del proceso de análisis
│   ├── 01_inspeccion_inicial.ipynb
│   ├── 02_calidad_y_limpieza.ipynb
│   ├── 03_eda.ipynb
│   ├── 04_pca.ipynb
│   └── 05_conclusiones.ipynb
│
├── pages/                  # Páginas de la app Streamlit
│   ├── 01_Dataset.py
│   ├── 02_EDA.py
│   ├── 03_PCA.py
│   └── 04_Conclusiones.py
│
├── Home.py                 # Página principal de la app Streamlit
├── utils.py                # Funciones auxiliares (carga de datos, etc.)
│
├── dataset_raw.json        # Dataset original sin procesar
├── dataset_processed.json  # Dataset limpio, listo para análisis
│
├── informe_final.docx      # Informe final del proyecto
├── requirements.txt        # Dependencias del proyecto
└── README.md
Metodología
Inspección inicial: revisión de la estructura y calidad general del dataset.
Limpieza de datos: tratamiento de valores nulos, negativos y outliers.
Análisis exploratorio (EDA): distribución de variables, correlaciones, visualizaciones.
PCA: reducción de dimensionalidad para identificar patrones de consumo.
Conclusiones: síntesis de hallazgos sobre el perfil de usuarios de alto consumo.
Cómo ejecutar la aplicación
Cloná el repositorio:
git clone https://github.com/Alanarias68/PI-Mineria_datos_1-.git
cd PI-Mineria_datos_1-
Instala las dependencias
pip install -r requirements.txt
Ejecuta la aplicación
streamlit run Home.py
Autor
Alan Arias, Carol Arias - Tecnicatura en Gestión de Datos e Inteligencia Artificial
