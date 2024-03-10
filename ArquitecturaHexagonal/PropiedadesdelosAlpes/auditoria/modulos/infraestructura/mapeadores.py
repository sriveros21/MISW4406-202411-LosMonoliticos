""" Mapeadores para la capa de infraestructura del dominio de auditorias

En este archivo usted encontrará los diferentes mapeadores
encargados de la transformación entre formatos de dominio y DTOs

"""

from PropiedadesdelosAlpes.auditoria.seedwork.dominio.repositorios import Mapeador
from PropiedadesdelosAlpes.auditoria.seedwork.infraestructura.utils import unix_time_millis
from PropiedadesdelosAlpes.auditoria.modulos.dominio.objetos_valor import FechaAuditoria, CodigoAuditoria, NombreAuditor, FaseAuditoria, HallazgosAuditoria, ObjetivoAuditoria
from PropiedadesdelosAlpes.auditoria.modulos.dominio.entidades import Auditoria
from PropiedadesdelosAlpes.auditoria.modulos.dominio.eventos.auditorias import AuditoriaCreada, FaseAuditoriaCambiada, EventoAuditoria
from .dto import Auditoria as AuditoriaDTO
from .excepciones import NoExisteImplementacionParaTipoFabricaExcepcion

class MapadeadorEventosAuditoria(Mapeador):

    # Versiones aceptadas
    versions = ('v1',)

    LATEST_VERSION = versions[0]

    def __init__(self):
        self.router = {
            AuditoriaCreada: self._entidad_a_auditoria_creada,
            FaseAuditoriaCambiada: self._entidad_a_auditoria_cambiada,
        }

    def obtener_tipo(self) -> type:
        return EventoAuditoria.__class__

    def es_version_valida(self, version):
        for v in self.versions:
            if v == version:
                return True
        return False

    def _entidad_a_auditoria_creada(self, entidad: AuditoriaCreada, version=LATEST_VERSION):
        def v1(evento):
            from .schema.v1.eventos import AuditoriaCreadaPayload, EventoAuditoriaCreada

            payload = AuditoriaCreadaPayload(
                id_auditoria = str(evento.codigo),
                fecha_creacion = int(unix_time_millis(evento.fecha_creacion))
            )
            evento_integracion = EventoAuditoriaCreada(id=str(evento.id))
            evento_integracion.id = str(evento.id)
            evento_integracion.time = int(unix_time_millis(evento.fecha_creacion))
            evento_integracion.specversion = str(version)
            evento_integracion.type = 'AuditoriaCreada'
            evento_integracion.datacontenttype = 'AVRO'
            evento_integracion.service_name = 'PropiedadesdelosAlpes'
            evento_integracion.data = payload

            return evento_integracion
                    
        if not self.es_version_valida(version):
            raise Exception(f'No se sabe procesar la version {version}')

        if version == 'v1':
            return v1(entidad)       
    
    def _entidad_a_auditoria_cambiada(self, entidad: FaseAuditoriaCambiada, version=LATEST_VERSION):
        # TODO
        raise NotImplementedError

    def entidad_a_dto(self, entidad: EventoAuditoria, version=LATEST_VERSION) -> AuditoriaDTO:
        if not entidad:
            raise NoExisteImplementacionParaTipoFabricaExcepcion
        func = self.router.get(entidad.__class__, None)

        if not func:
            raise NoExisteImplementacionParaTipoFabricaExcepcion

        return func(entidad, version=version)

    def dto_a_entidad(self, dto: AuditoriaDTO, version=LATEST_VERSION) -> Auditoria:
        raise NotImplementedError

class MapeadorAuditorias(Mapeador):

    def obtener_tipo(self) -> type:
        return Auditoria.__class__
  
    def entidad_a_dto(self, entidad: Auditoria) -> AuditoriaDTO:

        auditoria_dto = AuditoriaDTO()
        auditoria_dto.id = str(entidad.id)
        auditoria_dto.id_auditoria = ''.join(map(str, entidad.id_auditoria))
        auditoria_dto.codigo_auditoria = entidad.codigo
        auditoria_dto.fecha_auditoria = entidad.fecha
        auditoria_dto.nombre_auditor = entidad.auditor
        auditoria_dto.fase_auditoria = entidad.fase
        auditoria_dto.hallazgos_auditoria= entidad.hallazgos
        auditoria_dto.objetivo_auditoria= entidad.objetivo

        return auditoria_dto

    #cambiando esto
    def dto_a_entidad(self, dto: AuditoriaDTO) -> Auditoria:
        id = dto.id
        id_auditoria=dto.id_auditoria
        codigo=CodigoAuditoria(codigo=dto.codigo_auditoria)
        fecha=FechaAuditoria(fecha=dto.fecha_auditoria)
        auditor=NombreAuditor(nombre_auditor=dto.nombre_auditor)
        fase=FaseAuditoria(dto.fase_auditoria)
        hallazgos=HallazgosAuditoria(hallazgos_auditoria=dto.hallazgos_auditoria)
        objetivo=ObjetivoAuditoria(dto.objetivo_auditoria)

        return Auditoria(
            id=id,
            id_auditoria=id_auditoria,
            codigo=codigo,
            fecha=fecha,
            auditor=auditor,
            fase=fase,
            hallazgos=hallazgos,
            objetivo=objetivo
        )

