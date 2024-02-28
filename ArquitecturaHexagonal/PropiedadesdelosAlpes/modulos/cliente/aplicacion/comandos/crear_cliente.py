from dataclasses import dataclass

from .base import CrearClienteBaseHandler
from .....modulos.cliente.aplicacion.dto import ClienteDTO
from .....modulos.cliente.dominio.entidades import Cliente
from .....seedwork.aplicacion.comandos import Comando
from .....seedwork.aplicacion.comandos import ejecutar_commando as comando
from .....seedwork.infraestructura.uow import UnidadTrabajoPuerto


@dataclass
class CrearCliente(Comando):
    nombre: str
    apellido: str


class CrearClienteHandler(CrearClienteBaseHandler):
    def handle(self, comando: CrearCliente):
        cliente_dto = ClienteDTO(
            nombre=comando.nombre,
            apellido=comando.apellido
        )

        cliente: Cliente = self.fabrica_cliente.crear_desde_dto(cliente_dto)
        repositorio = self.fabrica_repositorio.obtener_repositorio_cliente()

        UnidadTrabajoPuerto.registrar_batch(repositorio.agregar(), cliente)
        UnidadTrabajoPuerto.commit()


@comando.register(CrearCliente)
def ejecutar_comando_crear_cliente(comando: CrearCliente):
    handler = CrearClienteHandler()
    handler.handle(comando)
