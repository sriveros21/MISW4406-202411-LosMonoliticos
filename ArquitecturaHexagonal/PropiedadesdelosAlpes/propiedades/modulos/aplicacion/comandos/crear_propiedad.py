from typing import List
from PropiedadesdelosAlpes.propiedades.modulos.aplicacion.mapeadores import MapeadorPropiedad
from PropiedadesdelosAlpes.seedwork.aplicacion.comandos import Comando
from PropiedadesdelosAlpes.propiedades.modulos.aplicacion.dto import PropiedadDTO
from .base import CrearPropiedadBaseHandler
from dataclasses import dataclass, field
from PropiedadesdelosAlpes.seedwork.aplicacion.comandos import ejecutar_commando as comando

from PropiedadesdelosAlpes.propiedades.modulos.dominio.entidades import Propiedad
from PropiedadesdelosAlpes.seedwork.infraestructura.uow import UnidadTrabajoPuerto
from PropiedadesdelosAlpes.propiedades.modulos.infraestructura.repositorios import RepositorioPropiedades
from PropiedadesdelosAlpes.propiedades.modulos.aplicacion.dto import UbicacionDTO, DimensionDTO, TerrenoDTO, EdificacionDTO
@dataclass
class CrearPropiedad(Comando):
    id: str
    nombre: str
    ubicacion: UbicacionDTO
    dimension: DimensionDTO
    tipo: str
    estado: str
    terreno: TerrenoDTO
    edificaciones: List[EdificacionDTO]

class CrearPropiedadHandler(CrearPropiedadBaseHandler):
    
    def handle(self, comando: CrearPropiedad):
        propiedad_dto = PropiedadDTO(
                id=comando.id,
                nombre=comando.nombre,
                ubicacion=comando.ubicacion,
                dimension=comando.dimension,
                tipo=comando.tipo,
                estado=comando.estado,
                terreno=comando.terreno,
                edificaciones=comando.edificaciones)

        propiedad: Propiedad = self.fabrica_propiedades.crear_objeto(propiedad_dto, MapeadorPropiedad())
        propiedad.crear_propiedad(propiedad)

        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioPropiedades.__class__)

        UnidadTrabajoPuerto.registrar_batch(repositorio.agregar, propiedad, repositorio_eventos_func=repositorio_eventos.agregar)
        UnidadTrabajoPuerto.commit()

@comando.register(CrearPropiedad)
def ejecutar_comando_crear_propiedad(comando: CrearPropiedad):
    handler = CrearPropiedadHandler()
    handler.handle(comando)
