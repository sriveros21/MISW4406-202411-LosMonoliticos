from PropiedadesdelosAlpes.seedwork.infraestructura.vistas import Vista
from PropiedadesdelosAlpes.modulos.auditorias.dominio.entidades import Auditoria
from PropiedadesdelosAlpes.config.db import db
from .dto import Auditoria as AuditoriaDTO

class VistaAuditoria(Vista):
    def obtener_por(id=None, estado=None, id_cliente=None, **kwargs) -> [Auditoria]: # type: ignore
        params = dict()

        if id:
            params['id'] = str(id)
            
        return db.session.query(AuditoriaDTO).filter_by(**params)