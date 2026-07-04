import streamlit as st
import pandas as pd


@st.cache_data
def load_data():
    """Carga el dataset procesado de la plataforma de streaming."""
    df = pd.read_json("data/dataset_processed.json")
    return df
