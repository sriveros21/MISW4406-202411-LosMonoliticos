from typing import List
from PropiedadesdelosAlpes.modulos.propiedades.aplicacion.mapeadores import MapeadorPropiedad
from PropiedadesdelosAlpes.seedwork.aplicacion.comandos import Comando
from PropiedadesdelosAlpes.modulos.propiedades.aplicacion.dto import PropiedadDTO
from .base import CrearPropiedadBaseHandler
from dataclasses import dataclass, field
from PropiedadesdelosAlpes.seedwork.aplicacion.comandos import ejecutar_commando as comando

from PropiedadesdelosAlpes.modulos.propiedades.dominio.entidades import Propiedad
from PropiedadesdelosAlpes.seedwork.infraestructura.uow import UnidadTrabajoPuerto
from PropiedadesdelosAlpes.modulos.propiedades.infraestructura.repositorios import RepositorioPropiedades
from PropiedadesdelosAlpes.modulos.propiedades.aplicacion.dto import UbicacionDTO, DimensionDTO, TerrenoDTO, EdificacionDTO
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

        UnidadTrabajoPuerto.registrar_batch(repositorio.agregar, propiedad)
        UnidadTrabajoPuerto.savepoint()
        UnidadTrabajoPuerto.commit()

@comando.register(CrearPropiedad)
def ejecutar_comando_crear_propiedad(comando: CrearPropiedad):
    handler = CrearPropiedadHandler()
    handler.handle(comando)
