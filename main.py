import streamlit as st

# Configuración de la página principal
# layout='wide' hace que la app use todo el ancho de pantalla
st.set_page_config(
    page_title='Dashboard multi-pagina',
    layout='wide',
    initial_sidebar_state='expanded'
)

# Definir las páginas de la aplicación
# Cada página es un archivo .py separado en la carpeta Paginas/

# Página principal con dashboard general
home_page = st.Page(
    'Paginas/dashboard_general.py',
    title='Home',
    icon=':material/home:',
    default=True  # Esta será la página por defecto
)

# Página de análisis y visualizaciones
analisis_page = st.Page(
    'Paginas/analisis_temporal.py',
    title='Análisis de proyectos',
    icon=':material/analytics:'
)

# Crear el sistema de navegación
# Las páginas se organizan en secciones (diccionario)
pg = st.navigation({
    'Inicio': [home_page],
    'Visualización': [analisis_page]
})

# Ejecutar la página seleccionada por el usuario
pg.run()
