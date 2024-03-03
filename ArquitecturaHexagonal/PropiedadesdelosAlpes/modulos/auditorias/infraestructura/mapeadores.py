""" Mapeadores para la capa de infraestructura del dominio de auditorias

En este archivo usted encontrará los diferentes mapeadores
encargados de la transformación entre formatos de dominio y DTOs

"""

from PropiedadesdelosAlpes.seedwork.dominio.repositorios import Mapeador
from PropiedadesdelosAlpes.modulos.auditorias.dominio.objetos_valor import FechaAuditoria, CodigoAuditoria, NombreAuditor, FaseAuditoria, HallazgosAuditoria, ObjetivoAuditoria
from PropiedadesdelosAlpes.modulos.auditorias.dominio.entidades import Auditoria
from .dto import Auditoria as AuditoriaDTO

class MapeadorAuditorias(Mapeador):

    def __init__(self, db_session):
        self.db_session = db_session
    
    
    def obtener_tipo(self) -> type:
        return Auditoria.__class__
  
    def entidad_a_dto(self, entidad: Auditoria) -> AuditoriaDTO:

        auditoria_dto = AuditoriaDTO()
        auditoria_dto.id = entidad.id
        auditoria_dto.codigo_auditoria = entidad.codigo
        auditoria_dto.fecha_auditoria = entidad.fecha
        auditoria_dto.nombre_auditor = entidad.auditor
        auditoria_dto.fase_auditoria = entidad.fase
        auditoria_dto.hallazgos_auditoria= entidad.hallazgos
        auditoria_dto.objetivo_auditoria= entidad.objetivo

        return auditoria_dto

    #cambiando esto
    def dto_a_entidad(self, dto: AuditoriaDTO) -> Auditoria:
        # nombreauditor=dto.nombre_auditor
        # nombre_auditor_class=NombreAuditor(nombre_auditor=nombreauditor)
        # #nombre_auditor.nombre_auditor=nombreauditor
        # print("*******")
        # print(nombre_auditor_class)
        # # auditor=NombreAuditor(nombre_auditor=str(dto.nombre_auditor))
        # fase=FaseAuditoria(dto.fase_auditoria)
        # print ('*******Fase****')
        # print (fase)
        # objetivo=ObjetivoAuditoria(dto.objetivo_auditoria)

        # auditoria = Auditoria(
        #     dto.codigo_auditoria,
        #     dto.fecha_auditoria,
        #     #NombreAuditor(nombre_auditor=nombreauditor),
        #     #nombre_auditor,
        #     #dto.nombre_auditor,
        #     nombre_auditor_class,
        #     fase,
        #     dto.hallazgos_auditoria,
        #     objetivo
        # )
        
        # return auditoria
        id =dto.id
        codigo=CodigoAuditoria(codigo=dto.codigo_auditoria)
        fecha=FechaAuditoria(fecha=dto.fecha_auditoria)
        auditor=NombreAuditor(nombre_auditor=dto.nombre_auditor)
        fase=FaseAuditoria(dto.fase_auditoria)
        hallazgos=HallazgosAuditoria(hallazgos_auditoria=dto.hallazgos_auditoria)
        objetivo=ObjetivoAuditoria(dto.objetivo_auditoria)

        return Auditoria(
            id=id,
            codigo=codigo,
            fecha=fecha,
            auditor=auditor,
            fase=fase,
            hallazgos=hallazgos,
            objetivo=objetivo
        )

