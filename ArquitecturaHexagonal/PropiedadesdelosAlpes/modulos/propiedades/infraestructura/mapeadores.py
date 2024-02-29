""" Mapeadores para la capa de infrastructura del dominio de propiedades

En este archivo usted encontrará los diferentes mapeadores
encargados de la transformación entre formatos de dominio y DTOs

"""

from PropiedadesdelosAlpes.modulos.propiedades.aplicacion.dto import EdificacionDTO
from PropiedadesdelosAlpes.modulos.propiedades.dominio.objetos_valor import EstadoPropiedad, IdentificadorPropiedad, Lote, Nombre, Piso, TipoPropiedad
from PropiedadesdelosAlpes.seedwork.dominio.objetos_valor import Dimension, Ubicacion
from PropiedadesdelosAlpes.seedwork.dominio.repositorios import Mapeador
from PropiedadesdelosAlpes.modulos.propiedades.dominio.entidades import Edificacion, Especializado, Industrial, Minorista, Oficina, Propiedad
from .dto import Propiedad as PropiedadDTO

class MapeadorPropiedades(Mapeador):
    
    def obtener_tipo(self) -> type:
        return Propiedad.__class__
  
    def entidad_a_dto(self, entidad: Propiedad) -> PropiedadDTO:

        propiedad_dto = PropiedadDTO()
        propiedad_dto.id_propiedad = entidad.id
        propiedad_dto.nombre = entidad.nombre
        propiedad_dto.dimensiones = entidad.dimensiones
        propiedad_dto.tipo = entidad.tipo
        propiedad_dto.longitude = entidad.ubicacion
        propiedad_dto.estado = entidad.estado

        return propiedad_dto

    
    def dto_a_entidad(self, dto: PropiedadDTO) -> Propiedad:
        id = IdentificadorPropiedad(identificador=dto.id_propiedad)
        nombre = Nombre(valor=dto.nombre)
        ubicacion = Ubicacion(latitud=dto.latitude, longitud=dto.longitude)
        dimensiones = Dimension(dto.dimensiones)
        tipo = TipoPropiedad(dto.tipo)  
        estado = EstadoPropiedad(dto.estado) 
        
        # Convert edificaciones DTO list to domain objects
        edificaciones = [self.map_edificacion_dto_to_domain(ed) for ed in dto.edificaciones]
        
        # Convert terreno DTO to domain object
        terreno = Lote(valor=dto.terreno.id)  # Simplified, implement proper mapping based on Terreno domain class
        
        return Propiedad(
            id=id,
            nombre=nombre,
            ubicacion = Ubicacion(latitud=dto.latitude, longitud=dto.longitude),
            dimensiones=dimensiones,
            tipo=tipo,
            estado=estado,
            edificaciones=edificaciones,  # Assuming proper mapping is applied
            terreno=terreno  # Assuming proper mapping is applied
        )
    
    def map_edificacion_dto_to_domain(self, edificacion_dto: EdificacionDTO) -> Edificacion:
        pisos = [Piso(descripcion=piso.descripcion, metros_cuadrados=piso.metros_cuadrados) for piso in edificacion_dto.pisos]
        
        if edificacion_dto.tipo == "Minorista":
            return Minorista(id=edificacion_dto.id, dimensiones=Dimension(edificacion_dto.dimensiones), tipo=edificacion_dto.tipo, pisos=pisos)
        elif edificacion_dto.tipo == "Oficina":
            return Oficina(id=edificacion_dto.id, dimensiones=Dimension(edificacion_dto.dimensiones), tipo=edificacion_dto.tipo, pisos=pisos)
        elif edificacion_dto.tipo == "Industrial":
            return Industrial(id=edificacion_dto.id, dimensiones=Dimension(edificacion_dto.dimensiones), tipo=edificacion_dto.tipo, pisos=pisos)
        elif edificacion_dto.tipo == "Especializado":
            return Especializado(id=edificacion_dto.id, dimensiones=Dimension(edificacion_dto.dimensiones), tipo=edificacion_dto.tipo, pisos=pisos)
        else:
            # Handle unexpected type or throw an error
            raise ValueError("Unknown Edificacion type")
