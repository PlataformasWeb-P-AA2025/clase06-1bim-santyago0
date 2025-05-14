from sqlalchemy.orm import sessionmaker

from crear_base import Saludo2
from configuracion import engine

import csv

Session = sessionmaker(bind=engine)
session = Session()

# Creamos un objeto de tipo Saludo2

miSaludo = Saludo2()

# Leer el csv
with open('data/saludos_mundo.csv', mode='r', encoding='utf-8') as data_csv:
	data = csv.DictReader(data_csv, delimiter='|')