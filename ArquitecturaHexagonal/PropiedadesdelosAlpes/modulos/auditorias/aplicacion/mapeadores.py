from PropiedadesdelosAlpes.seedwork.aplicacion.dto import Mapeador as AppMap
from PropiedadesdelosAlpes.seedwork.dominio.repositorios import Mapeador as RepMap
from PropiedadesdelosAlpes.modulos.auditorias.dominio.entidades import Auditoria
from PropiedadesdelosAlpes.modulos.auditorias.dominio.objetos_valor import FechaAuditoria, CodigoAuditoria, NombreAuditor, FaseAuditoria, HallazgosAuditoria, ObjetivoAuditoria
from .dto import AuditoriaDTO, FechaAuditoriaDTO, CodigoAuditoriaDTO, NombreAuditorDTO, HallazgosAuditoriaDTO, FaseAuditoria, ObjetivoAuditoria

from datetime import datetime

class MapeadorAuditoriaDTOJson(AppMap):
    def externo_a_dto(self, externo: dict) -> AuditoriaDTO:
        auditoria_dto = AuditoriaDTO(externo.get('id'),
        externo.get('codigo'), externo.get('fecha'),
        externo.get('auditor'),externo.get('fase'),
        externo.get('hallazgos'), externo.get('objetivo'))

        return auditoria_dto

    #Revisar este metodo
    def dto_a_externo(self, dto: AuditoriaDTO) -> dict:
        return dto.__dict__
    

class MapeadorAuditoria(RepMap):

    def obtener_tipo(self) -> type:
        return Auditoria.__class__
    
    @staticmethod
    def entidad_a_dto(entidad: Auditoria) -> AuditoriaDTO:

        return AuditoriaDTO(
            #fecha_creacion=entidad.fecha_creacion.strftime("%Y-%m-%d"),
            #fecha_actualizacion=entidad.fecha_actualizacion.strftime("%Y-%m-%d"),
            #id=str(entidad.id),
            id=str(entidad.id),
            codigo_auditoria=entidad.codigo,
            fecha_auditoria=entidad.fecha,
            nombre_auditor=entidad.auditor,
            fase_auditoria=entidad.fase,
            hallazgos_auditoria=entidad.hallazgos,
            objetivo_auditoria=entidad.objetivo

        )

    def dto_a_entidad(self, dto: AuditoriaDTO) -> Auditoria:
        auditoria:Auditoria=dto
        return auditoria