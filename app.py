import pandas as pd
import plotly.express as px
import streamlit as st
st.title('Graficos de dispersion e histograma para el conjunto de datos de anuncios de venta de coches')
car_data = pd.read_csv('dataset/vehicles_us.csv')  # leer los datos
hist_button = st.button('Construir histograma')    # crear un botón

if hist_button:
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True) 

import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('dataset/vehicles_us.csv')  # leer los datos
hist_button = st.button('Construir grafico de dispersion')    # crear un botón

if hist_button:
    st.write('Creación de un grafico de dispersion para el conjunto de datos de anuncios de venta de coches')
    fig = px.scatter(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True) 
    
