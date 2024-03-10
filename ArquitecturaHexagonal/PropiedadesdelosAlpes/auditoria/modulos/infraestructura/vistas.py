from PropiedadesdelosAlpes.auditoria.seedwork.infraestructura.vistas import Vista
from PropiedadesdelosAlpes.auditoria.modulos.dominio.entidades import Auditoria
from PropiedadesdelosAlpes.auditoria.config.db import db
from .dto import Auditoria as AuditoriaDTO

class VistaAuditoria(Vista):
    def obtener_por(id=None, estado=None, id_cliente=None, **kwargs) -> [Auditoria]: # type: ignore
        params = dict()

        if id:
            params['id'] = str(id)
            
        return db.session.query(AuditoriaDTO).filter_by(**params)