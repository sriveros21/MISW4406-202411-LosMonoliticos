from PropiedadesdelosAlpes.seedwork.aplicacion.dto import AppMap
from PropiedadesdelosAlpes.seedwork.dominio.repositorios import Mapeador as RepMap
#Aca falta incluir Propiedad en Entidades de Dominio
from PropiedadesdelosAlpes.modulos.propiedades.dominio.entidades import Locacion, Propiedad
from PropiedadesdelosAlpes.modulos.propiedades.dominio.objetos_valor import InformacionGeoespacial , IdentificadorPropiedad, EstadoPropiedad , TipoPropiedad , Precio
from .dto import InformacionGeoespacialDTO, IdentificadorPropiedadDTO, PrecioDTO, PropiedadDTO

from datetime import datetime

class MapeadorPropiedadDTOJson(AppMap):
    def externo_a_dto(self, externo: dict) -> PropiedadDTO:
        propiedad_dto = PropiedadDTO()  
        return propiedad_dto
    
    #Esto debe modificarse?
    def dto_a_externo(self, dto: PropiedadDTO) -> dict:
        return dto.__dict__  
    
class MapeadorPropiedad(RepMap):

    def obtener_tipo(self) -> type:
        return Propiedad.__class__
    
    #Revisar 
    #Falta 1 id?
    def entidad_a_dto(self, entidad: Propiedad) -> PropiedadDTO:

        fecha_creacion = entidad.fecha_creacion.strftime(self._FORMATO_FECHA)
        fecha_actualizacion = entidad.fecha_actualizacion.strftime(self._FORMATO_FECHA)
        _id = str(entidad.id)
        _nombre=str(entidad.nombre)
        _ubicacion=str(entidad.str)
        _dimensiones=str(entidad.dimensiones)
        _tipo=str(entidad.tipo)
        _estado=str(entidad.estado)
        _edificaciones=str(entidad.edificaciones)
        _terreno=str(entidad.terreno)


    #Validar consitencia Entidad Propiedad en Dominio y AplicacionDTO
        return PropiedadDTO(fecha_creacion, fecha_actualizacion, _id, _nombre,_ubicacion,_dimensiones,_tipo,_estado,_edificaciones,_terreno)
    
    #Requiere Propiedad como entidad de Dominio
    def dto_a_entidad(self, dto: PropiedadDTO) -> Propiedad:
        propiedad = Propiedad()
        return propiedad