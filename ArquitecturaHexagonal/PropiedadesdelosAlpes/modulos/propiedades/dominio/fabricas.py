from dataclasses import dataclass
from typing import Type
from .entidades import Propiedad, Edificacion, Terreno, Entidad
from .reglas import UbicacionValida, ReglaDimensionesValidas
from .excepciones import TipoObjetoNoExisteEnDominioPropiedadesExcepcion
from ....modulos.propiedades.infraestructura.mapeadores import MapeadorPropiedades
from ....seedwork.dominio.fabricas import Fabrica
from ....seedwork.dominio.repositorios import Mapeador, Repositorio

@dataclass
class _FabricaPropiedades(Fabrica):
    def crear_objeto(self, obj: any, mapeador: Mapeador) -> any:
        if isinstance(obj, Entidad):
            return mapeador.entidad_a_dto(obj)
        else:
            propiedad: Propiedad = mapeador.dto_a_entidad(obj)

            return propiedad

@dataclass
class FabricaPropiedades(Fabrica):
    def crear_objeto(self, obj: any, mapeador: Mapeador) -> any:
        if mapeador.obtener_tipo() == Propiedad.__class__:
            fabrica_propiedades = _FabricaPropiedades()
            return fabrica_propiedades.crear_objeto(obj, mapeador)
        else:
            raise TipoObjetoNoExisteEnDominioPropiedadesExcepcion()