import pandas as pd
import streamlit as st

# Los parámetros con =None va a permitie llamar la función de manera flexible (tema de los parámeteos)
def filter_projects(df, estados=None, categorias=None, avance_min=0, managers=None):
    
    # Crear copia para no modificar el DataFrame original
    df_filtrado = df.copy()
    
    # Filtrar por estados si se proporcionaron
    if estados and len(estados) > 0:
        df_filtrado = df_filtrado[df_filtrado['State'].isin(estados)]
    
    # Filtrar por categorías si se proporcionaron
    if categorias and len(categorias) > 0:
        df_filtrado = df_filtrado[df_filtrado['Category'].isin(categorias)]
    
    # Filtrar por managers si se proporcionaron
    if managers and len(managers) > 0:
        df_filtrado = df_filtrado[df_filtrado['Manager'].isin(managers)]
    
    # Filtrar por avance mínimo (siempre se aplica)
    df_filtrado = df_filtrado[df_filtrado['PercentComplete'] >= avance_min]
    
    return df_filtrado


def calculate_kpis(df):
   
    # Contar total de proyectos
    total_proyectos = len(df)
    
    # Calcular promedio de avance (0 si no hay proyectos)
    promedio_avance = df['PercentComplete'].mean() if total_proyectos > 0 else 0
    
    # Contar managers únicos
    total_managers = df['Manager'].nunique()   
    
    # Contar países únicos
    total_paises = df['Country'].nunique()
    
    # Calcular presupuesto promedio (0 si no hay proyectos)
    presupuesto_promedio = df['BudgetThousands'].mean() if total_proyectos > 0 else 0
    
    # Retornar diccionario con todos los KPIs
    return {
        'total_projects': total_proyectos,
        'avg_progress': promedio_avance,
        'total_managers': total_managers,
        'total_countries': total_paises,
        'avg_budget': presupuesto_promedio
    }


def obtener_proyectos_por_estado(df):
    return df['State'].value_counts().reset_index()


def obtener_proyectos_por_categoria(df):
    return df['Category'].value_counts().reset_index()


def obtener_proyectos_por_pais(df):
    return df['Country'].value_counts().reset_index()


def obtener_proyectos_criticos(df):
    return df[df['CriticalFlag'] == True]


def obtener_presupuesto_por_categoria(df):
    return df.groupby('Category')['BudgetThousands'].sum().reset_index()


def obtener_promedio_avance_por_manager(df):
    return df.groupby('Manager')['PercentComplete'].mean().reset_index()
