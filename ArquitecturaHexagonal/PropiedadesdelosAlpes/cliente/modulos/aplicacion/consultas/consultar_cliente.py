from dataclasses import dataclass

from PropiedadesdelosAlpes.cliente.modulos.aplicacion.mapeadores import MapeadorCliente
from PropiedadesdelosAlpes.cliente.modulos.dominio.entidades import Cliente
from PropiedadesdelosAlpes.cliente.seedwork.aplicacion.queries import Query, QueryResultado
from PropiedadesdelosAlpes.cliente.seedwork.aplicacion.queries import ejecutar_query as query

from .base import ClienteQueryBaseHandler


@dataclass
class ObtenerCliente(Query):
    id_cliente: str


class ObtenerClienteHandler(ClienteQueryBaseHandler):

    def handle(self, query: ObtenerCliente) -> QueryResultado:
        vista = self.fabrica_vista.crear_objeto(Cliente)
        cliente = self.fabrica_cliente.crear_objeto(vista.obtener_por_id(id_cliente=query.id_cliente)[0], MapeadorCliente)
        return QueryResultado(resultado=cliente)


@query.register(ObtenerCliente)
def ejecutar_query_obtener_cliente(query: ObtenerCliente):
    handler = ObtenerClienteHandler()
    return handler.handle(query)
