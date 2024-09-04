import pandas as pd
import plotly.express as px
import streamlit as st

#Titulo de la aplicacióm
st.title("Graficos estadísticos")

#Descripcion del titulo
st.write("Esta aplicacion crea graficos que sirven como herramientas para el análisis de datos.")

#Encabezado
st.header('Diagramas disponibles')


car_data = pd.read_csv('vehicles_us.csv') # leer los datos

build_histogram = st.checkbox('Construir un histograma')

        
if build_histogram: # si la casilla de verificación está seleccionada
    
    st.write('Construir un histograma para la columna odómetro')
            
    # crear un histograma
    fig = px.histogram(car_data, x="odometer")
        
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)


build_dispersion = st.checkbox('Construir un diagrama de dispersion')

if build_dispersion:
    st.write("Construir un diagrama de dispersion para la colummna odómetro vs precio")

    # crear un diagrama de dispersion
    fig = px.scatter(car_data, x="odometer", y="price", title="Diagrama de Dispersión de Odometer vs. Price")

    # Mostrar el gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)