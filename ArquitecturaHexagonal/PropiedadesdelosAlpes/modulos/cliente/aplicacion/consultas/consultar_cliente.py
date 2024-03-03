from dataclasses import dataclass

from PropiedadesdelosAlpes.modulos.cliente.aplicacion.mapeadores import MapeadorCliente
from PropiedadesdelosAlpes.seedwork.aplicacion.queries import Query, QueryResultado
from PropiedadesdelosAlpes.seedwork.aplicacion.queries import ejecutar_query as query

from .base import ClienteQueryBaseHandler


@dataclass
class ObtenerCliente(Query):
    id_cliente: str


class ObtenerClienteHandler(ClienteQueryBaseHandler):

    def handle(self, query: ObtenerCliente) -> QueryResultado:
        repositorio = RepositorioCliente = self.fabrica_repositorio.obtener_repositorio_cliente()
        cliente = repositorio.obtener_por_id(query.id_cliente)
        cliente_dto = MapeadorCliente.entidad_a_dto(cliente)
        return QueryResultado(resultado=cliente_dto)


@query.register(ObtenerCliente)
def ejecutar_query_obtener_cliente(query: ObtenerCliente):
    handler = ObtenerClienteHandler()
    return handler.handle(query)
