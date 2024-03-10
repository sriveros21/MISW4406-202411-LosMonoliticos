from dataclasses import dataclass

from PropiedadesdelosAlpes.modulos.cliente.aplicacion.dto import NombreDTO, ApellidoDTO, EmailDTO, ClienteDTO
from PropiedadesdelosAlpes.modulos.cliente.aplicacion.mapeadores import MapeadorCliente
from PropiedadesdelosAlpes.modulos.cliente.dominio.entidades import Cliente
from PropiedadesdelosAlpes.modulos.cliente.infraestructura.repositorios import RepositorioCliente
from PropiedadesdelosAlpes.seedwork.aplicacion.comandos import Comando
from PropiedadesdelosAlpes.seedwork.aplicacion.comandos import ejecutar_commando as comando
from PropiedadesdelosAlpes.seedwork.infraestructura.uow import UnidadTrabajoPuerto

from .base import CrearClienteBaseHandler


@dataclass
class CrearCliente(Comando):
    id_cliente: str
    nombre: NombreDTO
    apellido: ApellidoDTO
    email: EmailDTO


class CrearClienteHandler(CrearClienteBaseHandler):
    def handle(self, comando: CrearCliente):
        cliente_dto = ClienteDTO(
            id_cliente=comando.id_cliente,
            nombre=comando.nombre,
            apellido=comando.apellido,
            email=comando.email
        )

        cliente: Cliente = self.fabrica_cliente.crear_objeto(cliente_dto, MapeadorCliente())
        cliente.crear_cliente(cliente)

        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioCliente.__class__)

        UnidadTrabajoPuerto.registrar_batch(repositorio.agregar, cliente)
        UnidadTrabajoPuerto.savepoint()
        UnidadTrabajoPuerto.commit()


@comando.register(CrearCliente)
def ejecutar_comando_crear_cliente(comando: CrearCliente):
    handler = CrearClienteHandler()
    handler.handle(comando)
