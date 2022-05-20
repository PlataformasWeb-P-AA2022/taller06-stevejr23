from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_, or_ # se importa el operador and

# se importa la clase(s) del
# archivo genera_tablas
from crear_base import Pais

engine = create_engine('sqlite:///paises.db')

Session = sessionmaker(bind=engine)
session = Session()

# Presentar todos los países del continente americano

paises = session.query(Pais).filter(Pais.Continent.in_(['NA','SA','CA'])).order_by(Pais.Nombre_pais).all()
print(paises)

# Presentar los países de Asía, ordenados por el atributo Dial.

paises = session.query(Pais).filter(Pais.Continent=="AS").order_by(Pais.Dial).all()
print(paises)

# Presentar los lenguajes de cada país.

paises = session.query(Pais.Languages).all()
print(paises)

# Presentar los países ordenados por la capital, siempre que el país pertenezca a Europa

paises = session.query(Pais.Continent=='EU').order_by(Pais.Capital).all()
print(paises)

# Presentar todos los países que tengan en su cadena de nombre de país "uador" o en su cadena de capital "ito".
paises = session.query(Pais).filter(or_(Pais.Nombre_pais.like("%uador"), Pais.Capital.like("%ito"))).all()
print(paises)