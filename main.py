import numpy as np
import streamlit as st
import pandas as pd
import altair as alt
import matplotlib.pyplot as plt


#grafica = alt.Chart(df).mark.circle().encode(x="TV", y="Sales")
#st.title("BIENVENIDOS A MI PAGINA")
#st.altair_chart(grafica)
#st.line_chart(df)

st.title("App de prediccion de anemia para el Perú :pencil:")
st.markdown("Esta aplicación predice si tenemos principios o si tenemos anemia")

st.markdown("Conoce mas sobre la anemia con el siguiente video:")
video_yt = "https://www.youtube.com/watch?v=q6Eh10Bvfzw"
st.video(video_yt)


st.title("Tabla de datos de algunos pacientes")
st.write("Visualiza los datos sobre algunos pacientes que ya han revisado sus resultados.")

# Cargar los datos desde un archivo CSV o DataFrame existente
data = pd.read_csv("ANEMIA_DATOS_PERU1.csv")  # Reemplaza "datos.csv" con la ruta a tu propio archivo de datos

# Mostrar el DataFrame en Streamlit
st.dataframe(data)


#mostrar imagen
logo = "logo.png"
st.sidebar.image(logo, width=300)

#cargar dataset del usuario
st.sidebar.header("Datos ingresados por el usuario")
uploaded_file = st.sidebar.file_uploader("cargue su archivo csv", type=["csv"])

#cuestionario
st.sidebar.markdown("Ingresa tus datos para predecir una posible anemia:")
age = st.sidebar.slider('Edad', 0, 100)


#cuadro de texto emoglobina
emoglobina = st.sidebar.number_input("Ingresa tu nivel de emoglobina")


#cuadro de texto talla
talla = st.sidebar.text_input("Ingresa tu talla (cm):")

#cuadro de texto peso
peso = st.sidebar.text_input("Ingresa tu peso (kg):")


#prediccion algoritmo
def calcular():
    if emoglobina<12.00:
        st.sidebar.markdown("Posible anemia")
    else:
        st.sidebar.markdown("Saludable")

#boton calcular
st.sidebar.button("Calcular", on_click=calcular)




#grafico de dispersion
st.title("Gráfico de Dispersión")


# Cargar los datos
data = pd.read_csv("ANEMIA_DATOS_PERU1.csv")  # Reemplaza "datos.csv" con tu propio archivo de datos

# Selección de columnas para el gráfico de dispersión
columna_x = st.selectbox("Selecciona la columna para el eje x", data.columns)
columna_y = st.selectbox("Selecciona la columna para el eje y", data.columns)
 # Crear el gráfico de dispersión
plt.figure(figsize=(10, 6))
plt.scatter(data[columna_x], data[columna_y])
plt.xlabel(columna_x)
plt.ylabel(columna_y)
plt.title("Gráfico de Dispersión")

# Mostrar el gráfico en Streamlit
st.pyplot(plt)


st.title("Gráfico de Líneas")

# Cargar los datos desde un archivo CSV o DataFrame existente
data = pd.read_csv("ANEMIA_DATOS_PERU1.csv")  # Reemplaza "datos.csv" con la ruta a tu propio archivo de datos

# Selección de columnas para el gráfico de líneas
columnas = st.multiselect("Selecciona las columnas para el gráfico de líneas", data.columns)

# Crear el gráfico de líneas
fig, ax = plt.subplots()
for columna in columnas:
    ax.plot(data[columna], label=columna)
ax.set_xlabel("Tiempo")
ax.set_ylabel("Valor")
ax.set_title("Gráfico de Líneas")
ax.legend()

# Mostrar el gráfico en Streamlit
st.pyplot(fig)


st.title("Histograma")

# Cargar los datos desde un archivo CSV o DataFrame existente
data = pd.read_csv("ANEMIA_DATOS_PERU1.csv")  # Reemplaza "datos.csv" con la ruta a tu propio archivo de datos

# Selección de columna para el histograma
columna = st.selectbox("Selecciona la columna para el histograma", data.columns)

# Crear el histograma
fig, ax = plt.subplots()
ax.hist(data[columna], bins=30)
ax.set_xlabel(columna)
ax.set_ylabel("Frecuencia")
ax.set_title("Histograma")

# Mostrar el histograma en Streamlit
st.pyplot(fig)


st.title("Gráfico de Barras")

# Cargar los datos desde un archivo CSV o DataFrame existente
data = pd.read_csv("ANEMIA_DATOS_PERU1.csv")  # Reemplaza "datos.csv" con la ruta a tu propio archivo de datos

# Selección de columnas para el gráfico de barras
columna_x = st.selectbox("Selecciona la columna para el eje x", options=data.columns, key="columna_x")
columna_y = st.selectbox("Selecciona la columna para el eje y", options=data.columns, key="columna_y")

# Crear el gráfico de barras
fig, ax = plt.subplots()
ax.bar(data[columna_x], data[columna_y])
ax.set_xlabel(columna_x)
ax.set_ylabel(columna_y)
ax.set_title("Gráfico de Barras")

# Mostrar el gráfico en Streamlit
st.pyplot(fig)