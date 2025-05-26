import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

st.set_page_config(page_title="Análisis de Vehículos Usados", layout="wide")

@st.cache_data
def load_data():
    df = pd.read_csv("vehicles_us.csv")
    df['CAR_AGE'] = 2019 - df['model_year']
    df['date_posted'] = pd.to_datetime(df['date_posted'])
    df['POST_YEAR'] = df['date_posted'].dt.year
    df['POST_MONTH'] = df['date_posted'].dt.month
    return df

df = load_data()


menu = st.sidebar.radio("Selecciona una sección:", [
    "📄 Vista previa del dataset",
    "📊 Análisis general",
    "💰 Precio vs Condición",
    "📈 Precio vs Kilometraje",
    "🚙 Distribución del Kilometraje",
    "🔧 Precio vs Tipo de Vehículo",
    "🗓️ Precio vs Año de Publicación",
    "📉 Precio vs Edad del Auto"
])


if menu == "📄 Vista previa del dataset":
    st.subheader("Vista previa del dataset")
    st.write(df.head())

elif menu == "📊 Análisis general":
    st.subheader("Estadísticas generales")
    st.write(df.describe())
    st.write("Distribución del precio")
    fig, ax = plt.subplots()
    sns.histplot(df['price'], bins=50, kde=True, ax=ax)
    st.pyplot(fig)

elif menu == "💰 Precio vs Condición":
    st.subheader("Relación entre el precio y la condición del vehículo")
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.boxplot(data=df, x='condition', y='price', ax=ax)
    ax.set_title("Precio por condición del vehículo")
    st.pyplot(fig)

elif menu == "📈 Precio vs Kilometraje":
    st.subheader("Relación entre el precio y el kilometraje")
    fig, ax = plt.subplots()
    sns.scatterplot(data=df, x='odometer', y='price', alpha=0.3, ax=ax)
    ax.set_title("Precio vs Kilometraje")
    st.pyplot(fig)

elif menu == "🚙 Distribución del Kilometraje":
    st.subheader("Distribución del kilometraje")
    fig, ax = plt.subplots()
    sns.histplot(df['odometer'], bins=40, kde=True, ax=ax)
    ax.set_title("Distribución del kilometraje")
    st.pyplot(fig)

elif menu == "🔧 Precio vs Tipo de Vehículo":
    st.subheader("Precio según el tipo de vehículo")
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.boxplot(data=df, x='type', y='price', ax=ax)
    ax.set_xticklabels(ax.get_xticklabels(), rotation=45)
    ax.set_title("Relación entre tipo de vehículo y precio")
    st.pyplot(fig)

elif menu == "🗓️ Precio vs Año de Publicación":
    st.subheader("Precio según año de publicación")
    fig, ax = plt.subplots()
    sns.boxplot(data=df, x='POST_YEAR', y='price', ax=ax)
    ax.set_title("Precio vs Año de Publicación")
    st.pyplot(fig)

elif menu == "📉 Precio vs Edad del Auto":
    st.subheader("Relación entre el precio y la edad del vehículo")
    fig, ax = plt.subplots()
    sns.boxplot(data=df, x='CAR_AGE', y='price', ax=ax)
    ax.set_title("Precio vs Edad del Auto")
    st.pyplot(fig)




st.title("Análisis de Vehículos Usados")

# Titulo de la aplicacion 
st.title(" Análisis de Vehículos Usados")

@st.cache_data
def cargar_datos():
    return pd.read_csv("vehicles_us.csv")

df = cargar_datos()

#muestra los daatos 
st.subheader("Vista previa del dataset")
st.dataframe(df.head())

st.markdown(f"🔢 Filas: {df.shape[0]} | Columnas: {df.shape[1]}")

st.subheader("Distribución de precios")
fig, ax = plt.subplots()
sns.histplot(df['price'], bins=30, kde=True, ax=ax)
st.pyplot(fig)


#filtrar por condicion del vehiculo 
st.subheader(" Filtrar por condición del vehículo")

#cargar el archivo 
@st.cache_data
def load_data():
    return pd.read_csv("vehicles_us.csv")
data = load_data()


#menu 
selected_condition = st.selectbox(
    "Selecciona la condición del vehículo:",
    data['condition'].unique()
)
filtered_data = data[data['condition'] == selected_condition]

st.write(f"Vehículos en condición: **{selected_condition}**")
st.write(filtered_data.head())


# Diagrama de dispersión de precio vs año
st.subheader(" Precio vs Año del Vehículo")
fig2, ax2 = plt.subplots()
sns.scatterplot(data=filtered_data, x='model_year', y='price', alpha=0.5, ax=ax2)
ax2.set_title(f"Precio vs Año - condición: {selected_condition}")
ax2.set_xlabel("Año del modelo")
ax2.set_ylabel("Precio")
st.pyplot(fig2)

streamlit
pandas
matplotlib
seaborn