""" Mapeadores para la capa de infrastructura del dominio de propiedades

En este archivo usted encontrará los diferentes mapeadores
encargados de la transformación entre formatos de dominio y DTOs

"""

#from PropiedadesdelosAlpes.modulos.propiedades.aplicacion.dto import DimensionDTO, EdificacionDTO, PisoDTO, PropiedadDTO, TerrenoDTO, UbicacionDTO
#from PropiedadesdelosAlpes.modulos.propiedades.infraestructura.dto import Ubicacion, Dimension, Terreno, Edificacion, Piso, Propiedad
from PropiedadesdelosAlpes.modulos.propiedades.dominio.objetos_valor import EstadoPropiedad, Lote, Nombre, Piso, TipoPropiedad 
from PropiedadesdelosAlpes.seedwork.dominio.objetos_valor import Dimension as DimensionVO, Ubicacion as UbicacionVO
from PropiedadesdelosAlpes.modulos.propiedades.infraestructura.dto import Dimension, Ubicacion
from PropiedadesdelosAlpes.seedwork.dominio.repositorios import Mapeador
from PropiedadesdelosAlpes.modulos.propiedades.dominio.entidades import Edificacion as EdificacionEntidad, Propiedad as PropiedadEntidad, Terreno as TerrenoEntidad
from .dto import Propiedad as PropiedadDTO, Edificacion as EdificacionDTO, Piso as PisoDTO, Terreno as TerrenoDTO, Ubicacion as UbicacionDTO, Dimension as DimensionDTO

class MapeadorPropiedades(Mapeador):
    
    def __init__(self, db_session):
        self.db_session = db_session
    
    def obtener_tipo(self) -> type:
        return PropiedadEntidad.__class__

    def entidad_a_dto(self, propiedad: PropiedadEntidad) -> PropiedadDTO:
        
        ubicacion_dto = UbicacionDTO(
            latitud=propiedad.ubicacion.latitud,
            longitud=propiedad.ubicacion.longitud,
        )

        dimension_dto = DimensionDTO(
            width=propiedad.dimension.width,
            length=propiedad.dimension.length,
            unit=propiedad.dimension.unit
        )
        terreno_dto = TerrenoDTO(
            id=propiedad.terreno.id,
            dimension=dimension_dto,
            lote=propiedad.terreno.lote.area
        )
        edificaciones_dto = [self.map_edificacion_entidad_to_dto(ed) for ed in propiedad.edificaciones]

        propiedad_dto = PropiedadDTO(
            id=propiedad.id,
            nombre=propiedad.nombre.valor,
            ubicacion=ubicacion_dto,
            dimension=dimension_dto,
            tipo=propiedad.tipo.value,
            estado=propiedad.estado.value,
            terreno=terreno_dto,
            edificaciones=edificaciones_dto
        )

        return propiedad_dto
    
    def dto_a_entidad(self, dto: PropiedadDTO) -> PropiedadEntidad:

        id = dto.id
        nombre = Nombre(valor=dto.nombre)
        #ubicacion = self.map_ubicacion_dto_to_domain(dto.ubicacion)
        #dimension = self.map_dimension_dto_to_domain(dto.dimension)
        ubicacion = UbicacionVO(latitud=dto.ubicacion.latitud, longitud=dto.ubicacion.longitud)
        dimension = DimensionVO(width=dto.dimension.width, length=dto.dimension.length, unit=dto.dimension.unit)

        tipo = TipoPropiedad(dto.tipo)
        estado = EstadoPropiedad(dto.estado)

        edificaciones = [self.map_edificacion_dto_to_domain(ed) for ed in dto.edificaciones]

        terreno = self.map_terreno_dto_to_domain(dto.terreno)

        return PropiedadEntidad(
            id=id,
            nombre=nombre,
            ubicacion=ubicacion,
            dimension=dimension,
            tipo=tipo,
            estado=estado,
            edificaciones=edificaciones,
            terreno=terreno
        )
    def map_edificacion_dto_to_domain(self, ed_dto: EdificacionDTO) -> EdificacionEntidad:
        dimension = Dimension(
        width=ed_dto.dimension.width,
        length=ed_dto.dimension.length,
        unit=ed_dto.dimension.unit
        )

        pisos = [Piso(numero=piso_dto.numero) for piso_dto in ed_dto.pisos]
        edificacion = EdificacionEntidad(
        id=ed_dto.id, 
        tipo=ed_dto.tipo,
        dimension=dimension,
        pisos=pisos
        )
        
        return edificacion

    def map_terreno_dto_to_domain(self, terreno_dto: TerrenoDTO) -> TerrenoEntidad:
        dimension = Dimension(
            width=terreno_dto.dimension.width,
            length=terreno_dto.dimension.length,
            unit=terreno_dto.dimension.unit
        )
        lote = Lote(area=terreno_dto.lote)
        return TerrenoEntidad(id=terreno_dto.id, dimension=dimension, lote=lote)

    def map_ubicacion_dto_to_domain(self, ubicacion_dto: UbicacionDTO) -> Ubicacion:
        return Ubicacion(
            latitud=ubicacion_dto.latitud,
            longitud=ubicacion_dto.longitud,
        )

    def map_dimension_dto_to_domain(self, dimension_dto: DimensionDTO) -> Dimension:
        return Dimension(
            width=dimension_dto.width,
            length=dimension_dto.length,
            unit=dimension_dto.unit
        )
    
    def map_edificacion_entidad_to_dto(self, ed: EdificacionEntidad) -> EdificacionDTO:
        dimension_dto = DimensionDTO(width=ed.dimension.width, length=ed.dimension.length, unit=ed.dimension.unit)

        pisos_dto = [PisoDTO(numero=piso.numero) for piso in ed.pisos]

        return EdificacionDTO(id=ed.id, tipo=ed.tipo, dimension=dimension_dto, pisos=pisos_dto)