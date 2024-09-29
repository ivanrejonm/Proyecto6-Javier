import plotly.express as px
import pandas as pd
import streamlit as st

# Leer los datos
car_data = pd.read_csv('vehicles_us.csv')

# Título de la aplicación
st.title('Análisis de Datos de Vehículos')

# Encabezado
st.header('Bienvenido a la Aplicación de Análisis de Datos de Vehículos')

# Descripción
st.write('En esta aplicación, podrás explorar y visualizar datos relacionados con el flujo de los precios según el año para un conjunto de vehículos automóviles.')

# Descripción Datos
st.write('Este es el conjunto de vehículos automóviles que tienes a disposición para analizar:')
# Mostrar el conjunto de datos
st.write(car_data.head())

# Descripción Gráficos
st.write('A continuación, podrás visualizar los datos a través de diversos gráficos.')

# Casillas de verificación para los gráficos
show_price_hist = st.checkbox('Mostrar histograma de precios')
show_scatter = st.checkbox('Mostrar gráfico de dispersión: Precio vs. Año')
show_area = st.checkbox(
    'Mostrar gráfico de área de precios a lo largo del tiempo')

# Mostrar histograma de precios si la casilla está seleccionada
if show_price_hist:
    st.write('Creación de un histograma de precios de los vehículos')
    fig_price_hist = px.histogram(car_data, x="price")
    st.plotly_chart(fig_price_hist, use_container_width=True)

# Mostrar gráfico de dispersión si la casilla está seleccionada
if show_scatter:
    st.write(
        'Creación de un gráfico de dispersión del precio vs. año de los vehículos')
    fig_scatter = px.scatter(car_data, x="model_year",
                             y="price", color="model", title="Precio vs. Año")
    st.plotly_chart(fig_scatter, use_container_width=True)

# Mostrar gráfico de área si la casilla está seleccionada
if show_area:
    st.write(
        'Creación de un gráfico de área de precios de vehículos a lo largo del tiempo')
    fig_area = px.area(
        car_data,
        x="model_year",
        y="price",
        title="Precios a lo Largo del Tiempo",
        line_shape='linear',  # O 'spline' para líneas suaves
        # Cambiar el color del área si se desea
        color_discrete_sequence=['blue']
    )

    # Mejorar el diseño del gráfico
    fig_area.update_layout(
        xaxis_title='Año del Modelo',
        yaxis_title='Precio',
        xaxis=dict(tickmode='linear'),  # Mostrar todas las etiquetas del eje x
        title={'x': 0.5, 'xanchor': 'center'},  # Centrar el título
        template='plotly_white'  # Usar un tema blanco para mayor claridad
    )

    st.plotly_chart(fig_area, use_container_width=True)

# Descripción Fullscreen
st.write('Atención: Para una mejor visualización se recomienda hacer uso del "fullscreen"')