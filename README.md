# Proyecto Integrador - Minería de Datos

## Descripción

Este proyecto corresponde al Proyecto Integrador de la Tecnicatura en Gestión de Datos e Inteligencia Artificial. Consiste en el análisis de un dataset de usuarios de una plataforma de streaming, con el objetivo de determinar las preferencias y características de los usuarios que generan mayor consumo (minutos de visualización) en la plataforma.

## Objetivo de investigación

Identificar el perfil de los usuarios que generan mayor consumo de contenido en la plataforma, en base a variables como edad, minutos de visualización mensual, tipo de plan de suscripción, tickets de soporte al cliente, entre otras.

## Estructura del repositorio

- notebooks/ - Notebooks del proceso de análisis
- pages/ - Páginas de la app Streamlit
- Home.py - Página principal de la app Streamlit
- utils.py - Funciones auxiliares
- dataset_raw.json - Dataset original
- dataset_processed.json - Dataset limpio
- informe_final.docx - Informe final del proyecto
- requirements.txt - Dependencias del proyecto

## Metodología

1. Inspección inicial del dataset
2. Limpieza de datos
3. Análisis exploratorio (EDA)
4. PCA
5. Conclusiones

## Cómo ejecutar la aplicación

pip install -r requirements.txt

streamlit run Home.py

## Autor

Alan Arias, Carol Arias - Tecnicatura en Gestión de Datos e Inteligencia Artificial
