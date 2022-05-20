from sqlalchemy import create_engine

# se genera en enlace al gestor de base de
# datos
# para el ejemplo se usa la base de datos
# sqlite
engine = create_engine('sqlite:///paises.db')

from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


from sqlalchemy import Column, Integer, String

class Pais(Base):
    __tablename__ = 'paises'
    
    id = Column(Integer, primary_key=True)
    Nombre_pais = Column(String(200))
    Capital = Column(String(200))
    Continent = Column(String(200))
    Dial = Column(String(200))
    Geoname_ID = Column(Integer)
    ITU = Column(String(200))
    Languages = Column(String(200))
    Independiente = Column(String(200))

    def __repr__(self):
        return "Pais: Nombre_pais:%s Capital:%s Continent:%s Dial:%s Geoname_ID:%s ITU:%s Languages:%s Independiente:%s" % (
                        self.Nombre_pais,
                        self.Capital,
                        self.Continent,
                        self.Dial,
                        self.Geoname_ID,
                        self.ITU,
                        self.Languages,
                        self.Independiente)
    


Base.metadata.create_all(engine)