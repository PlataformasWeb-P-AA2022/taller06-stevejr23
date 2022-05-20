from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_, or_ # se importa el operador and

# se importa la clase(s) del
# archivo genera_tablas
from crear_base import Pais

engine = create_engine('sqlite:///paises.db')

Session = sessionmaker(bind=engine)
session = Session()

# Presentar los países de Asía, ordenados por el atributo Dial.

paises = session.query(Pais).filter(Pais.Continent=="AS").order_by(Pais.Dial).all()
print(paises)