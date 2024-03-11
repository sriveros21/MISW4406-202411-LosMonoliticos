""" Repositorios para el manejo de persistencia de objetos de dominio en la capa de infraestructura del dominio de auditorias

En este archivo usted encontrá las diferentes repositorios para
persistir objetos dominio (agregaciones) en la capa de infraestructura del dominio de auditorias

"""

from PropiedadesdelosAlpes.auditoria.modulos.infraestructura.dto import EventosAuditoria
from PropiedadesdelosAlpes.auditoria.config.db import db
from PropiedadesdelosAlpes.auditoria.modulos.dominio.repositorios import RepositorioAuditorias, RepositorioEventosAuditorias
from PropiedadesdelosAlpes.auditoria.modulos.dominio.entidades import Auditoria
from PropiedadesdelosAlpes.auditoria.modulos.dominio.fabricas import FabricaAuditorias
from .dto import Auditoria as AuditoriaDTO
from .mapeadores import MapadeadorEventosAuditoria, MapeadorAuditorias
from uuid import UUID
from typing import List
from pulsar.schema import *

class RepositorioAuditoriasSQLAlchemy(RepositorioAuditorias):

    def __init__(self):
        self._fabrica_auditorias: FabricaAuditorias = FabricaAuditorias()

    @property
    def fabrica_auditorias(self):
        return self._fabrica_auditorias

    def obtener_por_id(self, id: UUID) -> Auditoria:
        auditoria_dto = db.session.query(AuditoriaDTO).filter_by(id=str(id)).one()
        return self.fabrica_auditorias.crear_objeto(auditoria_dto, MapeadorAuditorias())

    def obtener_todos(self) -> list[Auditoria]:
        # TODO
        raise NotImplementedError

    def agregar(self, auditoria: Auditoria):
        auditoria_dto = self.fabrica_auditorias.crear_objeto(auditoria, MapeadorAuditorias())

        db.session.add(auditoria_dto)

    def actualizar(self, auditoria: Auditoria):
        # TODO
        raise NotImplementedError

    def eliminar(self, auditoria_id: UUID):
        # TODO
        raise NotImplementedError

class RepositorioEventosAuditoriaSQLAlchemy(RepositorioEventosAuditorias):

    def __init__(self):
        self._fabrica_auditorias: FabricaAuditorias = FabricaAuditorias()

    @property
    def fabrica_auditorias(self):
        return self._fabrica_auditorias

    def obtener_por_id(self, id: UUID) -> Auditoria:
        auditoria_dto = db.session.query(AuditoriaDTO).filter_by(id=str(id)).one()
        return self.fabrica_auditorias.crear_objeto(auditoria_dto, MapadeadorEventosAuditoria())

    def obtener_todos(self) -> 'list[Auditoria]':
        raise NotImplementedError

    def agregar(self, evento):
            auditoria_evento = self.fabrica_auditorias.crear_objeto(evento, MapadeadorEventosAuditoria())

            parser_payload = JsonSchema(auditoria_evento.data.__class__)
            json_str = parser_payload.encode(auditoria_evento.data)

            evento_dto = EventosAuditoria()
            evento_dto.id = str(evento.id)
            evento_dto.id_entidad = str(evento.id)
            evento_dto.fecha_evento = evento.fecha_creacion
            evento_dto.version = str(auditoria_evento.specversion)
            evento_dto.tipo_evento = evento.__class__.__name__
            evento_dto.formato_contenido = 'JSON'
            evento_dto.nombre_servicio = str(auditoria_evento.service_name)
            evento_dto.contenido = json_str

            db.session.add(evento_dto)

    def actualizar(self, auditoria: Auditoria):
        raise NotImplementedError

    def eliminar(self, auditoria_id: UUID):
        raise NotImplementedError