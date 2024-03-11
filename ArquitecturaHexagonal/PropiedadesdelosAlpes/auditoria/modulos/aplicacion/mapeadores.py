from PropiedadesdelosAlpes.auditoria.seedwork.aplicacion.dto import Mapeador as AppMap
from PropiedadesdelosAlpes.auditoria.seedwork.dominio.repositorios import Mapeador as RepMap
from PropiedadesdelosAlpes.auditoria.modulos.dominio.entidades import Auditoria
from PropiedadesdelosAlpes.auditoria.modulos.dominio.objetos_valor import FechaAuditoria, CodigoAuditoria, NombreAuditor, FaseAuditoria, HallazgosAuditoria, ObjetivoAuditoria
from .dto import AuditoriaDTO, FechaAuditoriaDTO, CodigoAuditoriaDTO, NombreAuditorDTO, HallazgosAuditoriaDTO, FaseAuditoria, ObjetivoAuditoria

from datetime import datetime

class MapeadorAuditoriaDTOJson(AppMap):
    def externo_a_dto(self, externo: dict) -> AuditoriaDTO:
        auditoria_dto = AuditoriaDTO(
            externo.get('id'),
            externo.get('id_auditoria'),
            externo.get('codigo_auditoria'), 
            externo.get('fecha_auditoria'),
            externo.get('nombre_auditor'),
            externo.get('fase_auditoria'),
            externo.get('hallazgos_auditoria'), 
            externo.get('objetivo_auditoria'))

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
            _id=str(entidad.id),
            id_auditoria=entidad.id_auditoria,
            codigo_auditoria=entidad.codigo_auditoria,
            fecha_auditoria=entidad.fecha_auditoria,
            nombre_auditor=entidad.nombre_auditor,
            fase_auditoria=entidad.fase_auditoria,
            hallazgos_auditoria=entidad.hallazgos_auditoria,
            objetivo_auditoria=entidad.objetivo_auditoria

        )

    def dto_a_entidad(self, dto: AuditoriaDTO) -> Auditoria:
        return Auditoria(
            id=dto.id,
            id_auditoria=dto.id_auditoria,
            codigo_auditoria=dto.codigo_auditoria,
            fecha_auditoria=dto.fecha_auditoria,
            nombre_auditor=dto.nombre_auditor,
            fase_auditoria=dto.fase_auditoria,
            hallazgos_auditoria=dto.hallazgos_auditoria,
            objetivo_auditoria=dto.objetivo_auditoria)