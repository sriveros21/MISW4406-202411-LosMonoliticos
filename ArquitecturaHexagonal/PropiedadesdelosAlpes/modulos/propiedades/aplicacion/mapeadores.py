from PropiedadesdelosAlpes.seedwork.aplicacion.dto import Mapeador as AppMap
from PropiedadesdelosAlpes.seedwork.dominio.repositorios import Mapeador as RepMap
from PropiedadesdelosAlpes.modulos.propiedades.dominio.entidades import Propiedad
from .dto import EdificacionDTO, PisoDTO, PropiedadDTO, TerrenoDTO, DimensionDTO, UbicacionDTO
from typing import List
from datetime import datetime

class MapeadorPropiedadDTOJson(AppMap):
    def _procesar_terreno(self, terreno: dict) -> TerrenoDTO:
        dimension_dto = DimensionDTO(
            width=terreno['dimension']['width'],
            length=terreno['dimension']['length'],
            unit=terreno['dimension']['unit']
        )
        terreno_dto = TerrenoDTO(
            id=terreno.get('id'),
            dimension=dimension_dto,
            lote=terreno.get('lote')
        )
        return terreno_dto
    
    def _procesar_edificaciones(self, edificaciones: List[dict]) -> List[EdificacionDTO]:
        edificaciones_dto = []
        for edificacion in edificaciones:
            dimension_dto = DimensionDTO(
                width=edificacion['dimension']['width'],
                length=edificacion['dimension']['length'],
                unit=edificacion['dimension']['unit']
            )
            pisos_dto = [PisoDTO(numero=piso['numero']) for piso in edificacion.get('pisos', [])]
            edificacion_dto = EdificacionDTO(
                id=edificacion.get('id'),
                tipo=edificacion.get('tipo'),
                dimension=dimension_dto,
                pisos=pisos_dto
            )
            edificaciones_dto.append(edificacion_dto)
        return edificaciones_dto
    
    def externo_a_dto(self, externo: dict) -> PropiedadDTO:
        terreno_dto = self._procesar_terreno(externo.get('terreno', {}))
        edificaciones_dto = self._procesar_edificaciones(externo.get('edificaciones', []))
        ubicacion_dto = UbicacionDTO(
            latitud=externo['ubicacion']['latitud'],
            longitud=externo['ubicacion']['longitud']
        )
        propiedad_dto = PropiedadDTO(
            id=externo.get('id'),
            nombre = str(externo['nombre']),
            ubicacion=ubicacion_dto,
            dimension=DimensionDTO(
                width=externo['dimension']['width'],
                length=externo['dimension']['length'],
                unit=externo['dimension']['unit']
            ),
            tipo=externo.get('tipo'),
            estado=externo.get('estado'),
            edificaciones=edificaciones_dto,
            terreno=terreno_dto
        )
        return propiedad_dto
    
    def dto_a_externo(self, dto: PropiedadDTO) -> dict:
        return dto.__dict__  
    
class MapeadorPropiedad(RepMap):
    
    @staticmethod
    def entidad_a_dto(self, entidad: Propiedad) -> PropiedadDTO:
        terreno_dto = TerrenoDTO(
            id=str(entidad.terreno.id),
            dimension=DimensionDTO(
                width=entidad.terreno.dimension.width,
                length=entidad.terreno.dimension.length,
                unit=entidad.terreno.dimension.unit
            ),
            lote=entidad.terreno.lote
        )
        edificaciones_dto = [
            EdificacionDTO(
                id=str(edificacion.id),
                tipo=edificacion.tipo,
                dimension=DimensionDTO(
                    width=edificacion.dimension.width,
                    length=edificacion.dimension.length,
                    unit=edificacion.dimension.unit
                ),
                pisos=[PisoDTO(numero=piso.numero) for piso in edificacion.pisos]
            ) for edificacion in entidad.edificaciones
        ]
        ubicacion_dto = UbicacionDTO(
            latitud=entidad.ubicacion.latitud,
            longitud=entidad.ubicacion.longitud
        )
        propiedad_dto = PropiedadDTO(
            id=str(entidad.id),
            nombre=entidad.nombre,
            ubicacion=ubicacion_dto,
            dimension=DimensionDTO(
                width=entidad.dimension.width,
                length=entidad.dimension.length,
                unit=entidad.dimension.unit
            ),
            tipo=entidad.tipo,
            estado=entidad.estado,
            edificaciones=edificaciones_dto,
            terreno=terreno_dto
        )
        return propiedad_dto

    def dto_a_entidad(self, dto: PropiedadDTO) -> Propiedad:
        propiedad: Propiedad = dto
        return propiedad
    
    def obtener_tipo(self) -> type:
        return Propiedad.__class__