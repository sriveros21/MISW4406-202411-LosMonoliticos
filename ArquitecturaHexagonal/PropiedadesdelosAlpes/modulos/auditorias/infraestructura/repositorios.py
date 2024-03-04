""" Repositorios para el manejo de persistencia de objetos de dominio en la capa de infraestructura del dominio de auditorias

En este archivo usted encontrá las diferentes repositorios para
persistir objetos dominio (agregaciones) en la capa de infraestructura del dominio de auditorias

"""

from PropiedadesdelosAlpes.config.db import db
from PropiedadesdelosAlpes.modulos.auditorias.dominio.repositorios import RepositorioAuditorias
from PropiedadesdelosAlpes.modulos.auditorias.dominio.entidades import Auditoria
from PropiedadesdelosAlpes.modulos.auditorias.dominio.fabricas import FabricaAuditorias
from .dto import Auditoria as AuditoriaDTO
from .mapeadores import MapeadorAuditorias

from uuid import UUID
from typing import List

class RepositorioAuditoriasSQLite(RepositorioAuditorias):

    def __init__(self):
        self._fabrica_auditorias: FabricaAuditorias = FabricaAuditorias()

    @property
    def fabrica_auditorias(self):
        return self._fabrica_auditorias

    def obtener_por_id(self, id: UUID) -> Auditoria:
        auditoria_dto = db.session.query(AuditoriaDTO).filter_by(id=str(id)).one()
        return self.fabrica_auditorias.crear_objeto(auditoria_dto, MapeadorAuditorias())

    def agregar(self, auditoria: Auditoria):
        auditoria_dto = self.fabrica_auditorias.crear_objeto(auditoria, MapeadorAuditorias())
        db.session.add(auditoria_dto)
        db.session.commit()