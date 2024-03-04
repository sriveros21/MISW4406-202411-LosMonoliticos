from dataclasses import dataclass
from typing import Type
from .entidades import Propiedad
from .reglas import UbicacionValida, ReglaDimensionesValidas
from .excepciones import TipoObjetoNoExisteEnDominioPropiedadesExcepcion
from ....seedwork.dominio.fabricas import Fabrica
from ....seedwork.dominio.entidades import Entidad
from PropiedadesdelosAlpes.seedwork.dominio.repositorios import Mapeador
#from PropiedadesdelosAlpes.modulos.propiedades.aplicacion.mapeadores import MapeadorPropiedad

@dataclass
class _FabricaPropiedades(Fabrica):
    def crear_objeto(self, obj: any, mapeador: Mapeador) -> any:
        if isinstance(obj, Entidad):
            print(f"Converting Entity to DTO: {obj}")
            return mapeador.entidad_a_dto(obj)
        else:
            print(f"Converting DTO to Entity: {obj}")
            propiedad: Propiedad = mapeador.dto_a_entidad(obj)
            print(f"Converted Propiedad Entity: {propiedad}")
            return propiedad

@dataclass
class FabricaPropiedades(Fabrica):
    def crear_objeto(self, obj: any, mapeador: Mapeador) -> any:
        if mapeador.obtener_tipo() == Propiedad.__class__:
            fabrica_propiedades = _FabricaPropiedades()
            return fabrica_propiedades.crear_objeto(obj, mapeador)
        else:
            raise TipoObjetoNoExisteEnDominioPropiedadesExcepcion()