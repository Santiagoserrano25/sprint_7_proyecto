# sprint_7_proyecto
Descripción del proyecto: En este proyecto se realizó un análisis exploratorio de datos (EDA) y una implementación interactiva para visualizar información del conjunto de datos vehicles_us.csv, que contiene anuncios de venta de coches en EE. UU
1. Análisis exploratorio (EDA.ipynb)
   a. Se utilizó pandas para la carga y manipulación de datos.
   b. Se generaron visualizaciones con plotly.express:
       1. Histograma para analizar la distribución del kilometraje (odometer).
       2. Gráfico de dispersión para observar la relación entre el kilometraje (odometer) y el precio (price).
2. Aplicación interactiva (app.py)
  a. Se implementó una interfaz con Streamlit.
  b. Funcionalidades:
      1. Botón para generar el histograma de odometer.
      2. Botón para generar el gráfico de dispersión.
  c. Los gráficos se renderizan de forma interactiva y adaptados al ancho de la pantalla.
