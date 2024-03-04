from PropiedadesdelosAlpes.seedwork.aplicacion.queries import Query, QueryHandler, QueryResultado
from PropiedadesdelosAlpes.seedwork.aplicacion.queries import ejecutar_query as query
from PropiedadesdelosAlpes.modulos.auditorias.infraestructura.repositorios import RepositorioAuditorias
from dataclasses import dataclass
from .base import AuditoriaQueryBaseHandler
from PropiedadesdelosAlpes.modulos.auditorias.aplicacion.mapeadores import MapeadorAuditoria
import uuid

@dataclass
class ObtenerAuditoria(Query):
    id: str

class ObtenerAuditoriaHandler(AuditoriaQueryBaseHandler):

    def handle(self, query: ObtenerAuditoria) -> QueryResultado:
        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioAuditorias.__class__)
        auditoria =  self.fabrica_auditorias.crear_objeto(repositorio.obtener_por_id(query.id), MapeadorAuditoria())
        return QueryResultado(resultado=auditoria)

@query.register(ObtenerAuditoria)
def ejecutar_query_obtener_auditoria(query: ObtenerAuditoria):
    handler = ObtenerAuditoriaHandler()
    return handler.handle(query)