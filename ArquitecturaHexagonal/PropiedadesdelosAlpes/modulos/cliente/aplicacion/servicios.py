from uuid import UUID

from PropiedadesdelosAlpes.modulos.cliente.dominio.entidades import Cliente
from PropiedadesdelosAlpes.modulos.cliente.infraestructura.repositorios import RepositorioCliente
from PropiedadesdelosAlpes.seedwork.aplicacion.servicios import Servicio

from .dto import ClienteDTO
from .mapeadores import MapeadorCliente


class ServicioCliente(Servicio):

    def __init__(self, repositorio: RepositorioCliente, mapeador: MapeadorCliente):
        self.repositorio = repositorio
        self.mapeador = mapeador

    def crear_cliente(self, cliente_dto: ClienteDTO) -> ClienteDTO:
        cliente: Cliente = self.mapeador.dto_a_entidad(cliente_dto)
        self.repositorio.agregar(cliente)
        return self.mapeador.entidad_a_dto(cliente)

    def obtener_cliente_por_id(self, id: UUID) -> ClienteDTO:
        cliente = self.repositorio.obtener_por_id(id)
        if cliente:
            return self.mapeador.entidad_a_dto(cliente)
        return None
