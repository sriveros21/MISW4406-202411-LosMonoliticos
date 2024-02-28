from dataclasses import dataclass

from PropiedadesdelosAlpes.modulos.cliente.aplicacion.mapeadores import MapeadorCliente
from PropiedadesdelosAlpes.modulos.cliente.infraestructura.repositorios import RepositorioCliente
from PropiedadesdelosAlpes.seedwork.aplicacion.queries import Query, QueryResultado
from PropiedadesdelosAlpes.seedwork.aplicacion.queries import ejecutar_query as query

from .base import ClienteQueryBaseHandler


@dataclass
class ObtenerCliente(Query):
    id: str


class ObtenerClienteHandler(ClienteQueryBaseHandler):

    def handle(self, query: ObtenerCliente) -> QueryResultado:
        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioCliente.__class__)
        cliente = self.fabrica_cliente.crear_objeto(repositorio.obtener_por_id(query.id), MapeadorCliente())
        return QueryResultado(resultado=cliente)


@query.register(ObtenerCliente)
def ejecutar_query_obtener_cliente(query: ObtenerCliente):
    handler = ObtenerClienteHandler()
    return handler.handle(query)
