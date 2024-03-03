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

from typing import List

class RepositorioAuditoriasSQLite(RepositorioAuditorias):

    def __init__(self, db_session, mapeador: MapeadorAuditorias, fabrica: FabricaAuditorias):
        self.db_session=db_session
        self.mapeador =mapeador
        self.fabrica=fabrica
        #self._fabrica_auditorias: FabricaAuditorias = FabricaAuditorias()

    @property
    def fabrica_auditorias(self):
        return self.fabrica
    
    #Revisar consistencia del tipo del id
    def obtener_por_id(self, id: str) -> Auditoria:
        auditoria_dto = db.session.query(AuditoriaDTO).filter_by(id=id).one()
        return self.fabrica_auditorias.crear_objeto(auditoria_dto, self.mapeador)

    #Verificar sí aca se incluye el Id
    #Revisar fecha
    def obtener_todos(self) -> List[Auditoria]:
        auditorias_dto = db.session.query(AuditoriaDTO).all()
        return [self.mapeador.dto_a_entidad(dto) for dto in auditorias_dto]       

    def agregar(self, auditoria: Auditoria):
        auditoria_dto = self.fabrica_auditorias.crear_objeto(auditoria, self.mapeador)
        db.session.add(auditoria_dto)
        db.session.commit()