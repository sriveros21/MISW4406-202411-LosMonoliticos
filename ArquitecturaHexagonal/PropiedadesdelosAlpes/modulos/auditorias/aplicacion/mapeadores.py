from PropiedadesdelosAlpes.seedwork.aplicacion.dto import Mapeador as AppMap
from PropiedadesdelosAlpes.seedwork.dominio.repositorios import Mapeador as RepMap
from PropiedadesdelosAlpes.modulos.auditorias.dominio.entidades import Auditoria
from PropiedadesdelosAlpes.modulos.auditorias.dominio.objetos_valor import FechaAuditoria, CodigoAuditoria, NombreAuditor, FaseAuditoria, HallazgosAuditoria, ObjetivoAuditoria
from .dto import AuditoriaDTO, FechaAuditoriaDTO, CodigoAuditoriaDTO, NombreAuditorDTO, HallazgosAuditoriaDTO, FaseAuditoria, ObjetivoAuditoria

from datetime import datetime

class MapeadorAuditoriaDTOJson(AppMap):
    def externo_a_dto(self, externo: dict) -> AuditoriaDTO:
        auditoria_dto = AuditoriaDTO()
        auditoria_dto.codigo=externo.get('codigo')
        auditoria_dto.fecha=externo.get('fecha')
        auditoria_dto.auditor=externo.get('auditor')
        auditoria_dto.fase =externo.get('fase')
        auditoria_dto.hallazgos=externo.get('hallazgos')
        auditoria_dto.objetivo=externo.get('objetivo')

        return auditoria_dto

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
            codigo=entidad.codigo.valor,
            fecha=entidad.fecha.valor,
            auditor=entidad.auditor.valor,
            fase=entidad.fase.valor,
            hallazgos=entidad.hallazgos.valor,
            objetivos=entidad.objetivo.valor

        )

    def dto_a_entidad(self, dto: AuditoriaDTO) -> Auditoria:
        auditoria = Auditoria()
        return auditoria