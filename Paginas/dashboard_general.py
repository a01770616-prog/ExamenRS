import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from utils.data_loader import load_exam_data, get_unique_values
from utils.analysis_functions import filter_projects, calculate_kpis

# Título principal de la página
st.markdown("<h1 style='text-align: center;'>Dashboard principal de proyectos</h1>", unsafe_allow_html=True)

# Cargar los datos de proyectos
df = load_exam_data()

# Barra lateral con controles de filtrado
with st.sidebar:
    st.header("Filtros")
    
    # Filtro múltiple por Estado del proyecto (Active, Done, Pending)
    estados = get_unique_values(df, 'State')
    estado_filtro = st.multiselect("Estado", estados)
    
    # Filtro múltiple por Categoría (Research, Deployment, Infra)
    categorias = get_unique_values(df, 'Category')
    categoria_filtro = st.multiselect("Categoría", categorias)
    
    # Control deslizante para filtrar por porcentaje mínimo de avance
    avance_min = st.slider("Avance mínimo (%)", 0, 100, 0)
    
    # Filtro múltiple por Manager responsable del proyecto
    managers = get_unique_values(df, 'Manager')
    manager_filtro = st.multiselect("Manager", managers)

# Aplicar los filtros seleccionados a los datos
# Si no hay filtros seleccionados, se pasa None para mostrar todos
df_filtrado = filter_projects(
    df, 
    estados=estado_filtro if estado_filtro else None,
    categorias=categoria_filtro if categoria_filtro else None,
    avance_min=avance_min,
    managers=manager_filtro if manager_filtro else None
)

# Calcular los KPIs con los datos filtrados
kpis = calculate_kpis(df_filtrado)

# Mostrar las métricas principales en 4 columnas
col1, col2, col3, col4 = st.columns(4)

# Columna 1: Total de proyectos
with col1:
    st.metric('Total Proyectos', kpis['total_projects'])

# Columna 2: Promedio de avance
with col2:
    st.metric('Promedio avance (%)', f"{kpis['avg_progress']:.1f}")

# Columna 3: Número de managers únicos
with col3:
    st.metric('Managers únicos', kpis['total_managers'])

# Columna 4: Presupuesto promedio
with col4:
    st.metric('Presupuesto medio', f"{kpis['avg_budget']:.1f}K")

# Línea divisoria visual
st.markdown("---")

# Tabla con los detalles de los proyectos filtrados
st.subheader('Proyectos')
st.dataframe(
    # Seleccionar las columnas más importantes para mostrar
    df_filtrado[['ProjectID', 'ProjectName', 'Manager', 'Category', 'Country', 
                 'State', 'PercentComplete', 'BudgetThousands', 'StartDate', 'CriticalFlag']].head(20),
    use_container_width=True,  # Usar todo el ancho disponible
    hide_index=True,           # Ocultar el índice de pandas
    height=300                 # Altura fija de 300 píxeles
)


