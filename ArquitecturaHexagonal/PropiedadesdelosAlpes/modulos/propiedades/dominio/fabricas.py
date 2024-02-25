from .entidades import Propiedad
from .reglas import ReglaDimensionesValidas, UbicacionValida
from .excepciones import TipoObjetoNoExisteEnDominioPropiedadesExcepcion
from ArquitecturaHexagonal.PropiedadesdelosAlpes.seedwork.dominio.repositorios import Mapeador, Repositorio
from ArquitecturaHexagonal.PropiedadesdelosAlpes.seedwork.dominio.fabricas import Fabrica
from ArquitecturaHexagonal.PropiedadesdelosAlpes.seedwork.dominio.entidades import Entidad
from dataclasses import dataclass

@dataclass
class FabricaPropiedades(Fabrica):
    def crear_objeto(self, obj: any, mapeador: Mapeador) -> any:
        if isinstance(obj, Entidad):
            return mapeador.entidad_a_dto(obj)
        else:
            propiedad: Propiedad = mapeador.dto_a_entidad(obj)

            # Validar reglas específicas para la creación de una propiedad
            self.validar_regla(UbicacionValida(propiedad.ubicacion))
            self.validar_regla(ReglaDimensionesValidas(propiedad.dimensiones))
            
            return propiedad
