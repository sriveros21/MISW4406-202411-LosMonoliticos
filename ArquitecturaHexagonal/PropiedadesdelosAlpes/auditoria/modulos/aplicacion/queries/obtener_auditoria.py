from PropiedadesdelosAlpes.auditoria.seedwork.aplicacion.queries import Query, QueryHandler, QueryResultado
from PropiedadesdelosAlpes.auditoria.seedwork.aplicacion.queries import ejecutar_query as query
from PropiedadesdelosAlpes.auditoria.modulos.infraestructura.repositorios import RepositorioAuditorias
from PropiedadesdelosAlpes.auditoria.modulos.dominio.entidades import Auditoria
from dataclasses import dataclass
from .base import AuditoriaQueryBaseHandler
from PropiedadesdelosAlpes.auditoria.modulos.aplicacion.mapeadores import MapeadorAuditoria
import uuid

@dataclass
class ObtenerAuditoria(Query):
    id: str

class ObtenerAuditoriaHandler(AuditoriaQueryBaseHandler):

    def handle(self, query: ObtenerAuditoria) -> QueryResultado:
        vista = self.fabrica_vista.crear_objeto(Auditoria)
        auditoria =  self.fabrica_auditorias.crear_objeto(vista.obtener_por_id(id=query.id)[0], MapeadorAuditoria())
        return QueryResultado(resultado=auditoria)

@query.register(ObtenerAuditoria)
def ejecutar_query_obtener_auditoria(query: ObtenerAuditoria):
    handler = ObtenerAuditoriaHandler()
    return handler.handle(query)