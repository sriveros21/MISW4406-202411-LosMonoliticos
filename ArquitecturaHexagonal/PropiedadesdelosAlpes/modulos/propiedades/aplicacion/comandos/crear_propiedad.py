from ArquitecturaHexagonal.PropiedadesdelosAlpes.modulos.propiedades.aplicacion.mapeadores import MapeadorPropiedad
from PropiedadesdelosAlpes.seedwork.aplicacion.comandos import Comando
from PropiedadesdelosAlpes.modulos.propiedades.aplicacion.dto import PropiedadDTO
from .base import CrearPropiedadBaseHandler
from dataclasses import dataclass
from PropiedadesdelosAlpes.seedwork.aplicacion.comandos import ejecutar_commando as comando

from PropiedadesdelosAlpes.modulos.propiedades.dominio.entidades import Propiedad
from PropiedadesdelosAlpes.seedwork.infraestructura.uow import UnidadTrabajoPuerto
from ArquitecturaHexagonal.PropiedadesdelosAlpes.modulos.propiedades.infraestructura.repositorios import RepositorioPropiedades

@dataclass
class CrearPropiedad(Comando):
    nombre: str
    ubicacion: str
    dimensiones: str
    tipo: str
    estado: str

class CrearPropiedadHandler(CrearPropiedadBaseHandler):
    
    def handle(self, comando: CrearPropiedad):
        propiedad_dto = PropiedadDTO(
                nombre=comando.nombre,
                ubicacion=comando.ubicacion,
                dimensiones=comando.dimensiones,
                tipo=comando.tipo,
                estado=comando.estado)

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
