import streamlit as st
import pandas as pd
import re

# Función para realizar la búsqueda
def buscar(df, campo_busqueda, termino_busqueda):
    # Asegurarse de que los nombres de las columnas no contengan espacios en blanco adicionales
    df.columns = df.columns.str.strip()

    # Convertir la columna de búsqueda a minúsculas
    df[campo_busqueda] = df[campo_busqueda].astype(str).str.lower()

    # Definir el patrón de búsqueda según el campo seleccionado
    if campo_busqueda == 'Clave cliente':
        # Remover las comas del término de búsqueda
        termino_busqueda = termino_busqueda.replace(',', '')
        patron = r'\b{}\b'.format(termino_busqueda)
    elif campo_busqueda == 'Nombre':
        patron = r'(?i)\b{}\b'.format(termino_busqueda)
    elif campo_busqueda == 'Correo':
        patron = r'\b{}\b'.format(termino_busqueda)
    elif campo_busqueda == 'Contacto':
        # Remover las comas del término de búsqueda
        termino_busqueda = termino_busqueda.replace(',', '')
        patron = r'\b{}\b'.format(termino_busqueda)
    else:
        st.error("Campo de búsqueda inválido")
        return

    # Filtrar los registros que coincidan con el patrón de búsqueda
    registros_encontrados = df[df[campo_busqueda].str.contains(patron, regex=True, case=False, na=False)]

    # Mostrar los registros encontrados
    st.info("Resultados de búsqueda:")
    st.dataframe(registros_encontrados)

# Título de la aplicación
st.title("Programa de búsqueda")

# Leer el archivo Excel y asignarlo al DataFrame df
df = pd.read_excel('contactos.xlsx', engine='openpyxl')
#df = df.iloc[:, :-2]

# Asegurarse de que los nombres de las columnas no contengan espacios en blanco adicionales
df.columns = df.columns.str.strip()




# Campo de selección para el campo de búsqueda
campo_busqueda = st.selectbox("Campo de búsqueda:", df.columns)

# Campo de entrada para el término de búsqueda
termino_busqueda = st.text_input("Término de búsqueda:")

# Botón de búsqueda
if st.button("Buscar"):
    # Llamada a la función de búsqueda
    buscar(df, campo_busqueda, termino_busqueda)
