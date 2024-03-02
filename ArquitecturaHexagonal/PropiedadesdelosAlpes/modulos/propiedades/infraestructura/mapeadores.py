""" Mapeadores para la capa de infrastructura del dominio de propiedades

En este archivo usted encontrará los diferentes mapeadores
encargados de la transformación entre formatos de dominio y DTOs

"""

from PropiedadesdelosAlpes.modulos.propiedades.infraestructura.dto import Ubicacion, Dimension, Terreno, Edificacion, Piso, Propiedad
from PropiedadesdelosAlpes.modulos.propiedades.dominio.objetos_valor import EstadoPropiedad, Lote, Nombre, TipoPropiedad
from PropiedadesdelosAlpes.modulos.propiedades.infraestructura.dto import Dimension, Ubicacion
from PropiedadesdelosAlpes.seedwork.dominio.repositorios import Mapeador
from PropiedadesdelosAlpes.modulos.propiedades.dominio.entidades import Edificacion as EdificacionEntidad, Propiedad as PropiedadEntidad, Terreno as TerrenoEntidad
#from .dto import Propiedad as PropiedadDTO

class MapeadorPropiedades(Mapeador):
    
    def __init__(self, db_session):
        self.db_session = db_session
    
    def obtener_tipo(self) -> type:
        return PropiedadEntidad.__class__

    def entidad_a_dto(self, propiedad: PropiedadEntidad) -> Propiedad:
        
        ubicacion_dto = Ubicacion(
            latitud=propiedad.ubicacion.latitud,
            longitud=propiedad.ubicacion.longitud,
        )

        dimension_dto = Dimension(
            width=propiedad.dimension.width,
            length=propiedad.dimension.length,
            unit=propiedad.dimension.unit
        )
        terreno_dto = Terreno(
            id=propiedad.terreno.id,
            dimension=dimension_dto,
            lote=propiedad.terreno.lote.area
        )

        propiedad_dto = Propiedad(
            id=propiedad.id,
            nombre=propiedad.nombre.valor,
            ubicacion=ubicacion_dto,
            dimension=dimension_dto,
            tipo=propiedad.tipo.value,
            estado=propiedad.estado.value,
            terreno=terreno_dto
        )

        return propiedad_dto
    
    def dto_a_entidad(self, dto: Propiedad) -> PropiedadEntidad:

        id = dto.id
        nombre = Nombre(valor=dto.nombre)
        ubicacion = self.map_ubicacion_dto_to_domain(dto.ubicacion)
        dimension = self.map_dimension_dto_to_domain(dto.dimension)

        tipo = TipoPropiedad(dto.tipo)
        estado = EstadoPropiedad(dto.estado)

        edificaciones = [self.map_edificacion_dto_to_domain(ed) for ed in dto.edificaciones]

        terreno = self.map_terreno_dto_to_domain(dto.terreno)

        return Propiedad(
            id=id,
            nombre=nombre,
            ubicacion=ubicacion,
            dimension=dimension,
            tipo=tipo,
            estado=estado,
            edificaciones=edificaciones,
            terreno=terreno
        )
    def map_edificacion_dto_to_domain(self, ed_dto: Edificacion) -> EdificacionEntidad:
        dimension = Dimension(
        width=ed_dto.dimension.width,
        length=ed_dto.dimension.length,
        unit=ed_dto.dimension.unit
        )

        pisos = [Piso(numero=piso_dto.numero) for piso_dto in ed_dto.pisos]
        edificacion = Edificacion(
        id=ed_dto.id, 
        tipo=ed_dto.tipo,
        dimension=dimension,
        pisos=pisos
        )
        
        return edificacion

    def map_terreno_dto_to_domain(self, terreno_dto: Terreno) -> TerrenoEntidad:
        dimension = Dimension(
            width=terreno_dto.dimension.width,
            length=terreno_dto.dimension.length,
            unit=terreno_dto.dimension.unit
        )
        lote = Lote(area=terreno_dto.lote)
        return Terreno(id=terreno_dto.id, dimension=dimension, lote=lote)

    def map_ubicacion_dto_to_domain(self, ubicacion_dto: Ubicacion) -> Ubicacion:
        return Ubicacion(
            latitud=ubicacion_dto.latitud,
            longitud=ubicacion_dto.longitud,
        )

    def map_dimension_dto_to_domain(self, dimension_dto: Dimension) -> Dimension:
        return Dimension(
            width=dimension_dto.width,
            length=dimension_dto.length,
            unit=dimension_dto.unit
        )