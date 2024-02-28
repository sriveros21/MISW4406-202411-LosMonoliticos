from dataclasses import dataclass
from typing import Type
from .entidades import Auditoria, Entidad
from .reglas import DebeReportarHallazgos, DebeIncluirCodigoAuditoria
from .excepciones import TipoObjetoNoExisteEnDominioAuditoriasExcepcion
from ....modulos.auditorias.infraestructura.mapeadores import MapeadorAuditorias
from ....seedwork.dominio.fabricas import Fabrica
from ....seedwork.dominio.repositorios import Mapeador, Repositorio

# @dataclass
# class FabricaAuditorias(Fabrica):
#     repositorio_auditorias: Repositorio
#     #Revisar el siguiente Mapeador en Infra
#     mapeador: Type[Mapeador] = MapeadorAuditorias

#     def crear_desde_dto(self, dto: any) -> Auditoria:
#         # Assuming dto is an instance of a data transfer object for Auditory
#         auditoria: Auditoria = self.mapeador.dto_a_entidad(dto)

#         # Validate specific rules for property creation
#         if not DebeReportarHallazgos(auditoria.hallazgos_auditoria).es_valido():
#             raise TipoObjetoNoExisteEnDominioAuditoriasExcepcion("No se reportan hallazgos")
        
#         if not DebeIncluirCodigoAuditoria(auditoria.codigo_auditoria).es_valido():
#             raise TipoObjetoNoExisteEnDominioAuditoriasExcepcion("No se reporta el código de auditoria")

#         # Additional logic for processing or storing the created Auditory entity
#         self.repositorio_auditorias.agregar(auditoria)
        
#         return auditoria
@dataclass
class _FabricaAuditorias(Fabrica):
    def crear_objeto(self, obj: any, mapeador: Mapeador) -> any:
        if isinstance(obj, Entidad):
            return mapeador.entidad_a_dto(obj)
        else:
            auditoria: Auditoria = mapeador.dto_a_entidad(obj)

            return auditoria

@dataclass
class FabricaAuditorias(Fabrica):
    def crear_objeto(self, obj: any, mapeador: Mapeador) -> any:
        if mapeador.obtener_tipo() == Auditoria.__class__:
            fabrica_auditorias = _FabricaAuditorias()
            return fabrica_auditorias.crear_objeto(obj, mapeador)
        else:
            raise TipoObjetoNoExisteEnDominioAuditoriasExcepcion()




