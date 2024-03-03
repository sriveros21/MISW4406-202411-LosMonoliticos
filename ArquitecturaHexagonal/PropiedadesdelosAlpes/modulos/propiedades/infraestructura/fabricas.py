""" Fábricas para la creación de objetos en la capa de infrastructura del dominio de propiedades

En este archivo usted encontrará las diferentes fábricas para crear
objetos complejos en la capa de infraestructura del dominio de propiedades

"""

from dataclasses import dataclass, field
from PropiedadesdelosAlpes.modulos.propiedades.dominio.fabricas import FabricaPropiedades
from PropiedadesdelosAlpes.modulos.propiedades.infraestructura.mapeadores import MapeadorPropiedades
from PropiedadesdelosAlpes.seedwork.dominio.fabricas import Fabrica
from PropiedadesdelosAlpes.seedwork.dominio.repositorios import Repositorio
from PropiedadesdelosAlpes.modulos.propiedades.dominio.repositorios import RepositorioPropiedades
from .repositorios import RepositorioPropiedadesSQLite
from .excepciones import ExcepcionFabrica
from sqlalchemy.orm import Session

@dataclass
class FabricaRepositorio:
    def __init__(self, db_session: Session):
        self.db_session = db_session
    
    def crear_repositorio_propiedades(self) -> RepositorioPropiedadesSQLite:
        mapeador_propiedades = MapeadorPropiedades(db_session=self.db_session)
        fabrica_propiedades = FabricaPropiedades()
        return RepositorioPropiedadesSQLite(db_session=self.db_session, mapeador=mapeador_propiedades, fabrica=fabrica_propiedades)


    def obtener_repositorio_propiedades(self) -> RepositorioPropiedades:
        """
        Returns an instance of RepositorioPropiedades.
        This method simplifies accessing the properties repository.
        """
        return RepositorioPropiedadesSQLite()
