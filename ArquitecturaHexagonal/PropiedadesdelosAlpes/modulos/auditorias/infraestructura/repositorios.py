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

    def __init__(self):
        self._fabrica_auditorias: FabricaAuditorias = FabricaAuditorias()

    @property
    def fabrica_auditorias(self):
        return self._fabrica_auditorias
    
    #Revisar consistencia del tipo del id
    def obtener_por_id(self, id: str) -> Auditoria:
        auditoria_dto = db.session.query(AuditoriaDTO).filter_by(id=id).one()
        return self.fabrica_auditorias.crear_objeto(auditoria_dto, MapeadorAuditorias())

    #Verificar sí aca se incluye el Id
    #Revisar fecha
    def obtener_todos(self) -> List[Auditoria]:
        #id= 123
        codigo_auditoria = "auditoria.codigo"
        fecha_auditoria = "auditoria.fecha"
        nombre_auditor= "auditoria.auditor"
        fase_auditoria = "auditoria.fase"
        hallazgos_auditoria = "auditoria.hallazgos"
        objetivo_auditoria= "auditoria.objetivo"

        auditoria = Auditoria(
            id=id,
            codigo=codigo_auditoria,
            fecha=fecha_auditoria,
            auditor=nombre_auditor,
            fase=fase_auditoria,
            hallazgos=hallazgos_auditoria,
            objetivo=objetivo_auditoria
        )

        return [auditoria]

    def agregar(self, auditoria: Auditoria):
        auditoria_dto = self.fabrica_auditorias.crear_objeto(auditoria, MapeadorAuditorias())
        db.session.add(auditoria_dto)
        db.session.commit()