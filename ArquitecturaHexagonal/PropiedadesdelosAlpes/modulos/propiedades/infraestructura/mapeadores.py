""" Mapeadores para la capa de infrastructura del dominio de propiedades

En este archivo usted encontrará los diferentes mapeadores
encargados de la transformación entre formatos de dominio y DTOs

"""

from PropiedadesdelosAlpes.seedwork.dominio.repositorios import Mapeador
from PropiedadesdelosAlpes.modulos.propiedades.dominio.objetos_valor import NombreAero, Odo, Leg, Segmento, Itinerario, CodigoIATA
from PropiedadesdelosAlpes.modulos.propiedades.dominio.objetos_valor import Propietario, P
from PropiedadesdelosAlpes.modulos.propiedades.dominio.entidades import Proveedor, Aeropuerto, Reserva
from PropiedadesdelosAlpes.modulos.propiedades.dominio.entidades import Propietario, Propiedad
from .dto import Propiedad as PropiedadDTO
from .dto import Propietario as PropietarioDTO
from typing import List

class MapeadorPropiedades(Mapeador):
    _FORMATO_FECHA = '%Y-%m-%dT%H:%M:%SZ'

    def _procesar_propiedades_dto(self, propiedades_dto: list) -> List[Propiedad]:
        prop_dict = dict()
        
        for prop in propiedades_dto:
            id_propiedad = prop.id
            nombre_propiedad = prop.nombre
            tamano_propiedad = prop.dimensiones
            tipo_construccion = prop.tipo
            ubicacion_propiedad = prop.ubicacion
            estado_propiedad = prop.estado


        return [Propiedad(propiedades_dto)]

    def entidad_a_dto(self, entidad: Propietario) -> PropietarioDTO:

        propietario_dto = PropiedadDTO()
        propietario_dto.id_propietario = propietario_dto.id_propietario
        propietario_dto.nombre_propietario = propietario_dto.nombre_propietario
        propietario_dto.email_propietario = propietario_dto.email_propietario
        propietario_dto.fecha_registro = propietario_dto.fecha_registro

        return propietario_dto

    
    def dto_a_entidad(self, dto: PropietarioDTO) -> Propietario:
        propietario = Propietario(dto.id, dto.fecha_registro)
        propietario.propiedades = list()

        propiedades_dto: list[PropiedadDTO] = dto.propiedades

        propietario.propiedades.extend(self._procesar_propiedades_dto(propiedades_dto))
        
        return propietario