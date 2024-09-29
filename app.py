import pandas as pd
import streamlit as st
import plotly.express as px

datos = pd.read_csv('vehicles_us.csv')

print(datos.head(10))

hist_boton = st.button('Contruir histograma')

if hist_boton:
    st.write('Creacion de un histograma de los valores del odometro')
    
    fig = px.histogram(datos, x='odometer')
    
    st.plotly_chart(fig)