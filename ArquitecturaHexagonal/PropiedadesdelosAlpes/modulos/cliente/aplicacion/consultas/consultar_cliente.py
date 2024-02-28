import uuid
from dataclasses import dataclass

from .base import ClienteQueryBaseHandler
from .....modulos.cliente.aplicacion.mapeadores import MapeadorCliente
from .....modulos.cliente.infraestructura.repositorios import RepositorioCliente
from .....seedwork.aplicacion.queries import Query, QueryResultado
from .....seedwork.aplicacion.queries import ejecutar_query as query


@dataclass
class ObtenerCliente(Query):
    id: uuid.UUID


class ObtenerClienteHandler(ClienteQueryBaseHandler):

    def handle(self, query: ObtenerCliente) -> QueryResultado:
        repositorio: RepositorioCliente = self.fabrica_repositorio.obtener_repositorio_cliente()
        cliente = repositorio.obtener_por_id(query.id)
        cliente_dto = MapeadorCliente.entidad_a_dto(cliente)
        return QueryResultado(resultado=cliente_dto)


@query.register(ObtenerCliente)
def ejecutar_query_obtener_cliente(query: ObtenerCliente):
    handler = ObtenerClienteHandler()
    return handler.handle(query)
