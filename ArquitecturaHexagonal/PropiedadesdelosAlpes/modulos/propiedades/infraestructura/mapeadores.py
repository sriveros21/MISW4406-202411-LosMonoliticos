""" Mapeadores para la capa de infrastructura del dominio de propiedades

En este archivo usted encontrará los diferentes mapeadores
encargados de la transformación entre formatos de dominio y DTOs

"""

from PropiedadesdelosAlpes.seedwork.dominio.repositorios import Mapeador
from PropiedadesdelosAlpes.modulos.propiedades.dominio.entidades import Propiedad
from .dto import Propiedad as PropiedadDTO

class MapeadorPropiedades(Mapeador):
    
    def obtener_tipo(self) -> type:
        return Propiedad.__class__
  
    def entidad_a_dto(self, entidad: Propiedad) -> PropiedadDTO:

        propiedad_dto = PropiedadDTO()
        propiedad_dto.id_propiedad = entidad.id
        propiedad_dto.nombre_propiedad = entidad.nombre
        propiedad_dto.tamano_propiedad = entidad.dimensiones
        propiedad_dto.tipo_construccion = entidad.tipo
        propiedad_dto.ubicacion_propiedad = entidad.ubicacion
        propiedad_dto.estado_propiedad = entidad.estado

        return propiedad_dto

    
    def dto_a_entidad(self, dto: PropiedadDTO) -> Propiedad:
        propiedad = Propiedad(
            dto.id_propiedad,
            dto.nombre_propiedad,
            dto.tamano_propiedad,
            dto.tipo_construccion,
            dto.ubicacion_propiedad,
            dto.estado_propiedad
        )
        
        return propiedad