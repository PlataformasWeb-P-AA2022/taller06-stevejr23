from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_, or_ # se importa el operador and

# se importa la clase(s) del
# archivo genera_tablas
from crear_base import Pais

engine = create_engine('sqlite:///paises.db')

Session = sessionmaker(bind=engine)
session = Session()

# Presentar todos los países que tengan en su cadena de nombre de país "uador" o en su cadena de capital "ito".
paises = session.query(Pais).filter(or_(Pais.Nombre_pais.like("%uador"), Pais.Capital.like("%ito"))).all()
print(paises)