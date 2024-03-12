from dataclasses import dataclass

from PropiedadesdelosAlpes.cliente.modulos.aplicacion.dto import ClienteDTO
from PropiedadesdelosAlpes.cliente.modulos.aplicacion.mapeadores import MapeadorCliente
from PropiedadesdelosAlpes.cliente.modulos.dominio.entidades import Cliente
from PropiedadesdelosAlpes.cliente.modulos.infraestructura.repositorios import RepositorioCliente, RepositorioEventosCliente
from PropiedadesdelosAlpes.cliente.seedwork.aplicacion.comandos import Comando
from PropiedadesdelosAlpes.cliente.seedwork.aplicacion.comandos import ejecutar_commando as comando
from PropiedadesdelosAlpes.cliente.seedwork.infraestructura.uow import UnidadTrabajoPuerto

from .base import CrearClienteBaseHandler


@dataclass
class CrearCliente(Comando):
    id_cliente: str
    nombre: str
    apellido: str
    email: str


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

        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioCliente)
        repositorio_eventos = self.fabrica_cliente.crear_objeto(RepositorioEventosCliente)

        UnidadTrabajoPuerto.registrar_batch(repositorio.agregar, cliente, repositorio_eventos_func=repositorio_eventos.agregar)
        UnidadTrabajoPuerto.commit()


@comando.register(CrearCliente)
def ejecutar_comando_crear_cliente(comando: CrearCliente):
    handler = CrearClienteHandler()
    handler.handle(comando)
