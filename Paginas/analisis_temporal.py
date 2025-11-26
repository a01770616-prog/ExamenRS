import streamlit as st
import pandas as pd
import plotly.express as px
from utils.data_loader import load_exam_data, get_unique_values
from utils.analysis_functions import filter_projects

# Título principal de la página
st.markdown("<h1 style='text-align: center;'>Visualizaciones y comparación</h1>", unsafe_allow_html=True)

# Cargar los datos de proyectos
df = load_exam_data()

# Barra lateral con controles de filtrado
with st.sidebar:
    st.header("Filtros")
    
    # Filtro múltiple para seleccionar managers
    st.write("Selecciona Manager")
    managers = get_unique_values(df, 'Manager')
    manager_filtro = st.multiselect("manager_select", managers, label_visibility="collapsed")
    
    # Filtro de selección única para categoría
    st.write("Filtra por categoría")
    categorias = ['Todos'] + get_unique_values(df, 'Category')
    categoria_filtro = st.selectbox("categoria_select", categorias, label_visibility="collapsed")

# Aplicar los filtros seleccionados
df_filtrado = filter_projects(
    df,
    managers=manager_filtro if manager_filtro else None,
    categorias=[categoria_filtro] if categoria_filtro != 'Todos' else None
)

# Crear gráfico de dispersión interactivo
# Muestra la relación entre presupuesto y avance del proyecto
fig = px.scatter(
    df_filtrado,
    x='BudgetThousands',      # Eje X: Presupuesto en miles
    y='PercentComplete',       # Eje Y: Porcentaje de avance
    color='State',             # Color según el estado del proyecto
    hover_data=['ProjectName', 'Manager', 'Category'],  # Info adicional al pasar el mouse
    title='Avance vs Presupuesto (K$)'
)

# Personalizar las etiquetas de los ejes
fig.update_layout(
    xaxis_title="BudgetThousands",
    yaxis_title="PercentComplete"
)

# Mostrar el gráfico usando todo el ancho disponible
st.plotly_chart(fig, use_container_width=True)
