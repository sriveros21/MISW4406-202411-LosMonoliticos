from dataclasses import dataclass
from typing import Type
from .entidades import Auditoria, Entidad
from PropiedadesdelosAlpes.auditoria.seedwork.dominio.eventos import EventoDominio
from .reglas import DebeReportarHallazgos, DebeIncluirCodigoAuditoria
from .excepciones import TipoObjetoNoExisteEnDominioAuditoriasExcepcion
from ....auditoria.modulos.infraestructura.mapeadores import MapeadorAuditorias
from ....auditoria.seedwork.dominio.fabricas import Fabrica
from ....auditoria.seedwork.dominio.repositorios import Mapeador, Repositorio


@dataclass
class _FabricaAuditorias(Fabrica):
    def crear_objeto(self, obj: any, mapeador: Mapeador) -> any:
        if isinstance(obj, Entidad) or isinstance(obj, EventoDominio):
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
