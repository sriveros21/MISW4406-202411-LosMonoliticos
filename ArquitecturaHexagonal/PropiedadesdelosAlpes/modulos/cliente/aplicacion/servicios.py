from PropiedadesdelosAlpes.modulos.cliente.dominio.entidades import Cliente
from PropiedadesdelosAlpes.modulos.cliente.dominio.fabricas import FabricaCliente
from PropiedadesdelosAlpes.modulos.cliente.infraestructura.fabricas import FabricaRepositorio
from PropiedadesdelosAlpes.modulos.cliente.infraestructura.repositorios import RepositorioCliente
from PropiedadesdelosAlpes.seedwork.aplicacion.servicios import Servicio

from .dto import ClienteDTO
from .mapeadores import MapeadorCliente


class ServicioCliente(Servicio):

    def __init__(self):
        self._fabrica_repositorio: FabricaRepositorio = FabricaRepositorio()
        self._fabrica_cliente: FabricaCliente = FabricaCliente()

    @property
    def fabrica_repositorio(self):
        return self._fabrica_repositorio

    @property
    def fabrica_cliente(self):
        return self._fabrica_cliente

    def crear_cliente(self, cliente_dto: ClienteDTO) -> ClienteDTO:
        cliente: Cliente = self.fabrica_cliente.crear_objeto(cliente_dto, MapeadorCliente())

        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioCliente.__class__)
        repositorio.agregar(cliente)

        return self.fabrica_cliente.crear_objeto(cliente, MapeadorCliente())

    def obtener_cliente_por_id(self, id) -> ClienteDTO:
        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioCliente.__class__)
        return repositorio.obtener_por_id(id).__dict__
