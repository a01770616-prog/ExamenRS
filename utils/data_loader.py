import streamlit as st
import pandas as pd


@st.cache_data  # Guarda los datos en caché para no recargarlos cada vez
def load_exam_data():
    
    # Leer el archivo CSV
    df = pd.read_csv('data/exam_data.csv')
    
    # Convertir la columna de fecha de texto a formato fecha
    df['StartDate'] = pd.to_datetime(df['StartDate'])
    
    return df


@st.cache_data  # Guarda en caché para mejorar el rendimiento
def get_unique_values(df, column):
   
    # Eliminar valores nulos, obtener únicos, convertir a lista y ordenar
    return sorted(df[column].dropna().unique().tolist())
