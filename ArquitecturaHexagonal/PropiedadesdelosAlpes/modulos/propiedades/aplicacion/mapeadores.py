from PropiedadesdelosAlpes.seedwork.aplicacion.dto import AppMap
from PropiedadesdelosAlpes.seedwork.dominio.repositorios import Mapeador as RepMap
#Aca falta incluir Propiedad en Entidades de Dominio
from PropiedadesdelosAlpes.modulos.propiedades.dominio.entidades import Locacion, Propiedad
from PropiedadesdelosAlpes.modulos.propiedades.dominio.objetos_valor import InformacionGeoespacial , IdentificadorPropiedad, EstadoPropiedad , TipoPropiedad , Precio
from .dto import EdificacionDTO, InformacionGeoespacialDTO, IdentificadorPropiedadDTO, PisoDTO, PrecioDTO, PropiedadDTO

from datetime import datetime

class MapeadorPropiedadDTOJson(AppMap):
    def externo_a_dto(self, propiedad: dict) -> PropiedadDTO:
        propiedad_dto = PropiedadDTO()  
        propiedad_dto.nombre=propiedad.nombre
        propiedad_dto.ubicacion=propiedad.ubicacion
        propiedad_dto.dimensiones=propiedad.dimensiones
        propiedad_dto.tipo=propiedad.tipo
        propiedad_dto.estado=propiedad.estado
        propiedad_dto.terreno=propiedad.terreno
        
        edificaciones_dto:list[EdificacionDTO]=list()
        #Ajustar de acuerdo al JSON

        for edificacion in propiedad.get('edificaciones',list()):
            pisos_dto:list[PisoDTO]=list()
            for piso in edificacion.get('pisos',list()):
                piso_dto:PisoDTO=PisoDTO(piso.get('descripcion'),piso.get('metros_cuadrados'))
                pisos_dto.append(piso_dto)
            edificacion_dto:EdificacionDTO=EdificacionDTO(edificacion.get('id'), edificacion.get('tipo'), edificacion.get('dimensiones'), pisos_dto)
            edificaciones_dto.append(edificacion_dto)
        #si no funciona hacerlo con .append
        propiedad_dto.edificaciones=edificaciones_dto
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
        _ubicacion=str(entidad.ubicacion)
        _dimensiones=str(entidad.dimensiones)
        _tipo=str(entidad.tipo)
        _estado=str(entidad.estado)
        #Validar esta as

        _edificaciones_dto:EdificacionDTO=list()
        for edificacion in entidad.edificaciones:
            pisos_dto:list[PisoDTO]=list()
            for piso in edificacion.pisos:
                piso_dto:PisoDTO=PisoDTO(piso.descripcion,piso.metros_cuadrados)
                pisos_dto.append(piso_dto)
            edificacion_dto:EdificacionDTO=EdificacionDTO(edificacion.id, edificacion.tipo, edificacion.dimensiones, pisos_dto)
            _edificaciones_dto.append(edificacion_dto)
        #si no funciona hacerlo con .append
        
        _terreno=str(entidad.terreno)


    #Validar consitencia Entidad Propiedad en Dominio y AplicacionDTO
        return PropiedadDTO(fecha_creacion, fecha_actualizacion, _id, 
                            _nombre,_ubicacion,_dimensiones,_tipo,
                            _estado,_edificaciones_dto,_terreno)
    
    #Requiere Propiedad como entidad de Dominio
    def dto_a_entidad(self, dto: PropiedadDTO) -> Propiedad:
        propiedad = Propiedad()
        return propiedad