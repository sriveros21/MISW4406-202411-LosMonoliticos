from dataclasses import dataclass
from typing import Type
from .entidades import Auditoria, Entidad
from .reglas import DebeReportarHallazgos, DebeIncluirCodigoAuditoria
from .excepciones import TipoObjetoNoExisteEnDominioAuditoriasExcepcion
from ....modulos.auditorias.infraestructura.mapeadores import MapeadorAuditorias
from ....seedwork.dominio.fabricas import Fabrica
from ....seedwork.dominio.repositorios import Mapeador, Repositorio


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




