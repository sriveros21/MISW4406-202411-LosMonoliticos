from dataclasses import dataclass
from typing import Type
from .entidades import Propiedad, Edificacion, Terreno
from .reglas import UbicacionValida, ReglaDimensionesValidas
from .excepciones import TipoObjetoNoExisteEnDominioPropiedadesExcepcion
from ....modulos.propiedades.infraestructura.mapeadores import MapeadorPropiedades
from ....seedwork.dominio.fabricas import Fabrica
from ....seedwork.dominio.repositorios import Mapeador, Repositorio

@dataclass
class FabricaPropiedades(Fabrica):
    repositorio_propiedades: Repositorio
    mapeador: Type[Mapeador] = MapeadorPropiedades

    def crear_desde_dto(self, dto: any) -> Propiedad:
        # Assuming dto is an instance of a data transfer object for Propiedad
        propiedad: Propiedad = self.mapeador.dto_a_entidad(dto)

        # Validate specific rules for property creation
        if not UbicacionValida(propiedad.ubicacion).es_valido():
            raise TipoObjetoNoExisteEnDominioPropiedadesExcepcion("Ubicación no válida.")
        
        if not ReglaDimensionesValidas(propiedad.dimensiones).es_valido():
            raise TipoObjetoNoExisteEnDominioPropiedadesExcepcion("Dimensiones no válidas.")

        # Additional logic for processing or storing the created Propiedad entity
        self.repositorio_propiedades.agregar(propiedad)
        
        return propiedad
