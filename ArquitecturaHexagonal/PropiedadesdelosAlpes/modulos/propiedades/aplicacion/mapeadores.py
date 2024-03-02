from PropiedadesdelosAlpes.seedwork.aplicacion.dto import Mapeador as AppMap
from PropiedadesdelosAlpes.seedwork.dominio.repositorios import Mapeador as RepMap
from PropiedadesdelosAlpes.modulos.propiedades.dominio.entidades import Propiedad
from .dto import EdificacionDTO, PisoDTO, PropiedadDTO, TerrenoDTO, DimensionDTO, UbicacionDTO
from typing import List
from datetime import datetime

class MapeadorPropiedadDTOJson(AppMap):
    def externo_a_dto(self, propiedad: dict) -> PropiedadDTO:
        terreno_raw = propiedad.get('terreno')
        terreno_dto = TerrenoDTO(
            id=terreno_raw.get('id'),
            dimension=DimensionDTO(
                width=terreno_raw['dimensiones']['width'],
                length=terreno_raw['dimensiones']['length'],
                unit=terreno_raw['dimensiones']['unit']
            ),
            lote=terreno_raw.get('lote')
        )
        
 
        edificaciones_dto = [
            EdificacionDTO(
                id=str(edificacion.get('id')),
                tipo=edificacion.get('tipo'),
                dimension=DimensionDTO(
                    width=edificacion['dimensiones']['width'],
                    length=edificacion['dimensiones']['length'],
                    unit=edificacion['dimensiones']['unit']
                ),
                pisos=[PisoDTO(numero=piso['numero']) for piso in edificacion.get('pisos')],
            ) for edificacion in propiedad.get('edificaciones', [])
        ]

        ubicacion_raw = propiedad.get('ubicacion')
        ubicacion_dto = UbicacionDTO(
            latitud=ubicacion_raw['latitud'],
            longitud=ubicacion_raw['longitud']
        )


        propiedad_dto = PropiedadDTO(
            id=propiedad.get('id'),
            nombre=propiedad.get('nombre'),
            ubicacion=ubicacion_dto,
            dimension=DimensionDTO(
                width=propiedad['dimensiones']['width'],
                length=propiedad['dimensiones']['length'],
                unit=propiedad['dimensiones']['unit']
            ),
            tipo=propiedad.get('tipo'),
            estado=propiedad.get('estado'),
            edificaciones=edificaciones_dto,
            terreno=terreno_dto
        )

        return propiedad_dto
    
    def dto_a_externo(self, dto: PropiedadDTO) -> dict:
        return dto.__dict__  
    
class MapeadorPropiedad(RepMap):
    
    @staticmethod
    def entidad_a_dto(propiedad: Propiedad) -> PropiedadDTO:
        edificaciones_dto: List[EdificacionDTO] = [
            EdificacionDTO(
                id=str(edificacion.id.identificador),
                tipo=edificacion.tipo.value,
                dimension=DimensionDTO(
                    width=edificacion.dimension.width,
                    length=edificacion.dimension.length,
                    unit=edificacion.dimension.unit
                ),
                pisos=[PisoDTO(numero=piso.numero) for piso in edificacion.pisos]
            ) for edificacion in propiedad.edificaciones
        ]

        terreno_dto = TerrenoDTO(
            id=str(propiedad.terreno.id),
            dimension=DimensionDTO(
                width=propiedad.terreno.dimension.width,
                length=propiedad.terreno.dimension.length,
                unit=propiedad.terreno.dimension.unit
            ),
            lote=propiedad.terreno.lote.area
        )

        return PropiedadDTO(
            id=propiedad.id,
            nombre=propiedad.nombre.valor,
            ubicacion=UbicacionDTO(
                latitud=propiedad.ubicacion.latitud,
                longitud=propiedad.ubicacion.longitud
            ),
            dimension=DimensionDTO(
                width=propiedad.dimension.width,
                length=propiedad.dimension.length,
                unit=propiedad.dimension.unit
            ),
            tipo=propiedad.tipo.value,
            estado=propiedad.estado.value,
            edificaciones=edificaciones_dto,
            terreno=terreno_dto
        )

    def dto_a_entidad(self, dto: PropiedadDTO) -> Propiedad:
        propiedad: Propiedad = dto
        return propiedad
    
    def obtener_tipo(self) -> type:
        return Propiedad.__class__