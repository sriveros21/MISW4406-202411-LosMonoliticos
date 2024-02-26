from PropiedadesdelosAlpes.seedwork.aplicacion.queries import Query, QueryHandler, QueryResultado
from PropiedadesdelosAlpes.seedwork.aplicacion.queries import ejecutar_query as query
from PropiedadesdelosAlpes.modulos.propiedades.infraestructura.repositorios import RepositorioPropiedades
from dataclasses import dataclass
from .base import PropiedadQueryBaseHandler
from PropiedadesdelosAlpes.modulos.propiedades.aplicacion.mapeadores import MapeadorPropiedad
import uuid

@dataclass
class ObtenerPropiedad(Query):
    id: uuid.UUID

class ObtenerPropiedadHandler(PropiedadQueryBaseHandler):

    def handle(self, query: ObtenerPropiedad) -> QueryResultado:
        repositorio: RepositorioPropiedades = self.fabrica_repositorio.obtener_repositorio_propiedades()
        propiedad = repositorio.obtener_por_id(query.id)
        propiedad_dto = MapeadorPropiedad.entidad_a_dto(propiedad)
        return QueryResultado(resultado=propiedad_dto)

@query.register(ObtenerPropiedad)
def ejecutar_query_obtener_propiedad(query: ObtenerPropiedad):
    handler = ObtenerPropiedadHandler()
    return handler.handle(query)
