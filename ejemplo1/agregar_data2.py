from sqlalchemy.orm import sessionmaker

from crear_base import Saludo2
from configuracion import engine

import csv

Session = sessionmaker(bind=engine)
session = Session()

data = []

# Leer el csv
with open('data/saludos_mundo.csv', mode='r', encoding='utf-8') as data_csv:
	diccionario = csv.DictReader(data_csv, delimiter='|')

	# Agregar la data a la lista
	for d in diccionario:
		data.append(d)

# Bucle para agregar los registros a la base de datos
for d in data:
	# Creamos un objeto de tipo Saludo2
	miSaludo = Saludo2()
	miSaludo.mensaje = d["saludo"]
	miSaludo.tipo = d["tipo"]
	miSaludo.origen = d["origen"]

	# Agregar el objeto Saludo2
	session.add(miSaludo)

# Confirmar las transacciones
session.commit()