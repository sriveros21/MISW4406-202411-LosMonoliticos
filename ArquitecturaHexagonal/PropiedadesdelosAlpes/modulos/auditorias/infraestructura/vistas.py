from PropiedadesdelosAlpes.seedwork.infraestructura.vistas import Vista
from PropiedadesdelosAlpes.modulos.auditorias.dominio.entidades import Auditoria
from PropiedadesdelosAlpes.config.db import db
from .dto import Auditoria as AuditoriaDTO

class VistaAuditoria(Vista):
    def obtener_todos(self):
        auditorias_dto = db.session.query(AuditoriaDTO).all()
        auditorias = list()

        for auditoria_dto in auditorias_dto:
            auditorias.append(Auditoria(id=auditoria_dto.id, 
                fecha=auditoria_dto.fecha, 
                objetivo=auditoria_dto.objetivo))
        
        return auditorias
    
    #Revisar sí aca se deben incluir todos los atributos

    def obtener_por(self, id=None, codigo=None, auditor=None, **kwargs) -> [Auditoria]:
        params = dict()

        if id:
            params['id'] = str(id)
        
        if codigo:
            params['codigo'] = str(codigo)
        
        if auditor:
            params['auditor'] = str(auditor)
            
        # TODO Convierta ReservaDTO a Reserva y valide que la consulta es correcta
        return db.session.query(AuditoriaDTO).filter_by(**params)