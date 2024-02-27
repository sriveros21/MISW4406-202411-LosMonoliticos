from dataclasses import dataclass
from typing import Type
from .entidades import Auditoria
from .reglas import DebeReportarHallazgos, DebeIncluirCodigoAuditoria
from .excepciones import TipoObjetoNoExisteEnDominioAuditoriasExcepcion
from ArquitecturaHexagonal.PropiedadesdelosAlpes.modulos.auditorias.infraestructura.mapeadores import MapeadorAuditorias
from ArquitecturaHexagonal.PropiedadesdelosAlpes.seedwork.dominio.fabricas import Fabrica
from ArquitecturaHexagonal.PropiedadesdelosAlpes.seedwork.dominio.repositorios import Mapeador, Repositorio

@dataclass
class FabricaAuditorias(Fabrica):
    repositorio_auditorias: Repositorio
    #Revisar el siguiente Mapeador en Infra
    mapeador: Type[Mapeador] = MapeadorAuditorias

    def crear_desde_dto(self, dto: any) -> Auditoria:
        # Assuming dto is an instance of a data transfer object for Auditory
        auditoria: Auditoria = self.mapeador.dto_a_entidad(dto)

        # Validate specific rules for property creation
        if not DebeReportarHallazgos(auditoria.hallazgos_auditoria).es_valido():
            raise TipoObjetoNoExisteEnDominioAuditoriasExcepcion("No se reportan hallazgos")
        
        if not DebeIncluirCodigoAuditoria(auditoria.codigo_auditoria).es_valido():
            raise TipoObjetoNoExisteEnDominioAuditoriasExcepcion("No se reporta el código de auditoria")

        # Additional logic for processing or storing the created Auditory entity
        self.repositorio_auditorias.agregar(auditoria)
        
        return auditoria
