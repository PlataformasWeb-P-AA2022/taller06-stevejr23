from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from crear_base import Pais

import json
import requests

# se genera en enlace al gestor de base de
# datos
# para el ejemplo se usa la base de datos
# sqlite
engine = create_engine('sqlite:///paises.db')


Session = sessionmaker(bind=engine)
session = Session()

# se crean objetos de tipo Pesona

# leer el archivo de datos

#archivo = open("data/data-personas-001.json", "r")
archivo = requests.get("https://pkgstore.datahub.io/core/country-codes/country-codes_json/data/616b1fb83cbfd4eb6d9e7d52924bb00a/country-codes_json.json")

#datos_json =  json.load(archivo) # paso los datos del archivo a json
datos = archivo.json()
#documentos = datos_json["docs"]


for d in datos:
    print(d)
    #print(len(d.keys()))
    p = Pais(Nombre_pais = d['CLDR display name'], Capital = d['Capital'], Continent = d['Continent'], Dial = d['Dial'], Geoname_ID = d['Geoname ID'], ITU = d['ITU'], Languages = d['Languages'], Independiente = d['is_independent'])
    session.add(p)

# confirmar transacciones

session.commit()