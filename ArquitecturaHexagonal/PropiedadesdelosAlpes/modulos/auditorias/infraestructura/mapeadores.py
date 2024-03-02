""" Mapeadores para la capa de infraestructura del dominio de auditorias

En este archivo usted encontrará los diferentes mapeadores
encargados de la transformación entre formatos de dominio y DTOs

"""

from PropiedadesdelosAlpes.seedwork.dominio.repositorios import Mapeador
from PropiedadesdelosAlpes.modulos.auditorias.dominio.objetos_valor import FechaAuditoria, CodigoAuditoria, NombreAuditor, FaseAuditoria, HallazgosAuditoria, ObjetivoAuditoria
from PropiedadesdelosAlpes.modulos.auditorias.dominio.entidades import Auditoria
from .dto import Auditoria as AuditoriaDTO

class MapeadorAuditorias(Mapeador):
    
    def obtener_tipo(self) -> type:
        return Auditoria.__class__
  
    def entidad_a_dto(self, entidad: Auditoria) -> AuditoriaDTO:

        auditoria_dto = AuditoriaDTO()
        #auditoria_dto.id = entidad.id
        auditoria_dto.codigo_auditoria = entidad.codigo
        auditoria_dto.fecha_auditoria = entidad.fecha
        auditoria_dto.nombre_auditor = entidad.auditor
        auditoria_dto.fase_auditoria = entidad.fase
        auditoria_dto.hallazgos_auditoria= entidad.hallazgos
        auditoria_dto.objetivo_auditoria= entidad.objetivo

        return auditoria_dto

    #cambiando esto
    def dto_a_entidad(self, dto: AuditoriaDTO) -> Auditoria:
        nombreauditor=dto.nombre_auditor
        nombre_auditor_class=NombreAuditor(nombre_auditor=nombreauditor)
        #nombre_auditor.nombre_auditor=nombreauditor
        print("*******")
        print(nombre_auditor_class)
        # auditor=NombreAuditor(nombre_auditor=str(dto.nombre_auditor))
        auditoria = Auditoria(
            dto.codigo_auditoria,
            dto.fecha_auditoria,
            #NombreAuditor(nombre_auditor=nombreauditor),
            #nombre_auditor,
            #dto.nombre_auditor,
            nombre_auditor_class,
            dto.fase_auditoria,
            dto.hallazgos_auditoria,
            dto.objetivo_auditoria
        )
        
        return auditoria

