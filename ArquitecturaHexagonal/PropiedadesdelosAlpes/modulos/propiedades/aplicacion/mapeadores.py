from PropiedadesdelosAlpes.seedwork.aplicacion.dto import Mapeador as AppMap
from PropiedadesdelosAlpes.seedwork.dominio.repositorios import Mapeador as RepMap
from PropiedadesdelosAlpes.modulos.propiedades.dominio.entidades import Propiedad
from PropiedadesdelosAlpes.modulos.propiedades.dominio.objetos_valor import InformacionGeoespacial , IdentificadorPropiedad, EstadoPropiedad , TipoPropiedad , Precio
from .dto import EdificacionDTO, PisoDTO, PropiedadDTO, TerrenoDTO
from typing import List
from datetime import datetime

class MapeadorPropiedadDTOJson(AppMap):
    def externo_a_dto(self, propiedad: dict) -> PropiedadDTO:

        terreno_dto:TerrenoDTO=TerrenoDTO(
            id=str(propiedad.get('terreno').get('id')),
            dimensiones=propiedad.get('terreno').get('dimensiones'),
            lote=propiedad.get('terreno').get('lote')
        )
        
        edificaciones_dto: List[EdificacionDTO] = [
            EdificacionDTO(
                id=str(edificacion.get('id')),
                tipo=edificacion.get('tipo'),
                dimensiones=edificacion.get('dimensiones'),
                pisos=[PisoDTO(descripcion=piso.get('descripcion'), metros_cuadrados=piso.get('metros_cuadrados')) for piso in edificacion.get('pisos')]
            ) for edificacion in propiedad.get('edificaciones')
        ]

        propiedad_dto = PropiedadDTO(propiedad.get('nombre'),propiedad.get('ubicacion'),propiedad.get('dimensiones'),
                                     propiedad.get('tipo'), propiedad.get('estado'), edificaciones=edificaciones_dto,
                                    terreno=terreno_dto)  

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
        propiedad: Propiedad = dto
        return propiedad