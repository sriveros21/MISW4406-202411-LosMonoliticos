from PropiedadesdelosAlpes.seedwork.aplicacion.dto import Mapeador as AppMap
from PropiedadesdelosAlpes.seedwork.dominio.repositorios import Mapeador as RepMap
from PropiedadesdelosAlpes.modulos.propiedades.dominio.entidades import Propiedad
from PropiedadesdelosAlpes.modulos.propiedades.dominio.objetos_valor import InformacionGeoespacial , IdentificadorPropiedad, EstadoPropiedad , TipoPropiedad , Precio
from .dto import EdificacionDTO, PisoDTO, PropiedadDTO, TerrenoDTO
from typing import List
from datetime import datetime

class MapeadorPropiedadDTOJson(AppMap):
    def externo_a_dto(self, propiedad: dict) -> PropiedadDTO:
        propiedad_dto = PropiedadDTO()  
        propiedad_dto.nombre=propiedad.get('nombre')
        propiedad_dto.ubicacion=propiedad.get('ubicacion')
        propiedad_dto.dimensiones=propiedad.get('dimensiones')
        propiedad_dto.tipo=propiedad.get('tipo')
        propiedad_dto.estado=propiedad.get('estado')
        propiedad_dto.terreno=propiedad.get('terreno')
        
        edificaciones_dto:list[EdificacionDTO]=list()

        for edificacion in propiedad.get('edificaciones',list()):
            pisos_dto:list[PisoDTO]=list()
            for piso in edificacion.get('pisos',list()):
                piso_dto:PisoDTO=PisoDTO(piso.get('descripcion'),piso.get('metros_cuadrados'))
                pisos_dto.append(piso_dto)
            edificacion_dto:EdificacionDTO=EdificacionDTO(edificacion.get('id'), edificacion.get('tipo'), edificacion.get('dimensiones'), pisos_dto)
            edificaciones_dto.append(edificacion_dto)
        propiedad_dto.edificaciones=edificaciones_dto
        return propiedad_dto
    
    def dto_a_externo(self, dto: PropiedadDTO) -> dict:
        return dto.__dict__  
    
class MapeadorPropiedad(RepMap):

    def obtener_tipo(self) -> type:
        return Propiedad.__class__
    
    @staticmethod
    def entidad_a_dto(entidad: Propiedad) -> PropiedadDTO:
        edificaciones_dto: List[EdificacionDTO] = [
            EdificacionDTO(
                id=str(edificacion.id),
                tipo=edificacion.tipo,
                dimensiones=edificacion.dimensiones.valor,
                pisos=[PisoDTO(descripcion=piso.descripcion, metros_cuadrados=piso.metros_cuadrados) for piso in edificacion.pisos]
            ) for edificacion in entidad.edificaciones
        ]

        terreno_dto = TerrenoDTO(
            id=str(entidad.terreno.id),
            dimensiones=entidad.terreno.dimensiones.valor,
            lote=entidad.terreno.lote.valor
        )

        return PropiedadDTO(
            fecha_creacion=entidad.fecha_creacion.strftime("%Y-%m-%d"),
            fecha_actualizacion=entidad.fecha_actualizacion.strftime("%Y-%m-%d"),
            id=str(entidad.id),
            nombre=entidad.nombre.valor,
            ubicacion=str(entidad.ubicacion),
            dimensiones=entidad.dimensiones.valor,
            tipo=entidad.tipo.valor,
            estado=entidad.estado.valor,
            edificaciones=edificaciones_dto,
            terreno=terreno_dto
        )

    def dto_a_entidad(self, dto: PropiedadDTO) -> Propiedad:
        propiedad = Propiedad()
        return propiedad