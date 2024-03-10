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
class FabricaRepositorio(Fabrica):
    def crear_objeto(self, obj: type, mapeador: any = None) -> Repositorio:
        if obj == RepositorioPropiedades.__class__:
            return RepositorioPropiedadesSQLite()
        else:
            raise ExcepcionFabrica()
