import streamlit as st
from sqlalchemy.orm import sessionmaker
from crear_base import Saludo2
from configuracion import engine

# Crear sesión
Session = sessionmaker(bind=engine)
session = Session()

# Consultar saludo_dos
saludos = session.query(Saludo2).all()

# Mostrar con Streamlit
st.title("Presentación de todos los Saludo_dos")

for saludo  in saludos:
    st.write(saludo)
    st.markdown("---")

st.markdown("---")
st.title("Presentación de todos los Saludo_dos en Tabla")
lista = []

for s in saludos:
    diccionario = {"id": s.id, "mensaje": s.mensaje, "tipo": s.tipo, "origen": s.origen}
    lista.append(diccionario)

st.dataframe(lista)
