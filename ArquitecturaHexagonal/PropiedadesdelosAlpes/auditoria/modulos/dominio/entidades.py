"""Entidades del dominio auditorias

En este archivo se encontraran las entidades del dominio auditoria

"""

from __future__ import annotations
from dataclasses import dataclass, field
from enum import Enum

import PropiedadesdelosAlpes.auditoria.modulos.dominio.objetos_valor as ov
from PropiedadesdelosAlpes.auditoria.modulos.dominio.eventos.auditorias import AuditoriaCreada
from ....auditoria.seedwork.dominio.entidades import AgregacionRaiz, Entidad
import uuid
from datetime import datetime


@dataclass(frozen=True)
class FaseAuditoria(Enum):
    INICIAL = "Inicial"
    INTERMEDIA = "Intermedia"
    FINAL = "Final"    


@dataclass(frozen=True)
class ObjetivoAuditoria(Enum):
    VALIDAR_COBERTURA = "Validar Cobertura"
    VALIDAR_CALIDAD = "Validar Calidad"
    VALIDAR_CONFIABILIDAD = "Validar Confiabilidad"

@dataclass
class Auditoria(AgregacionRaiz):
    id: uuid.UUID = field(hash=True, default=None)
    id_auditoria:str = field(default_factory=str)
    codigo:ov.CodigoAuditoria = field(default_factory=ov.CodigoAuditoria)
    fecha:ov.FechaAuditoria = field(default_factory=ov.FechaAuditoria)
    auditor:ov.NombreAuditor = field(default_factory=ov.NombreAuditor)
    fase:ov.FaseAuditoria = field(default_factory=ov.FaseAuditoria.INICIAL)
    hallazgos:ov.HallazgosAuditoria = field(default_factory=ov.HallazgosAuditoria)
    objetivo: ov.ObjetivoAuditoria = field(default_factory=ov.ObjetivoAuditoria.VALIDAR_CALIDAD)

    def crear_auditoria(self, auditoria: Auditoria):
        self.id = auditoria.id,
        self.id_auditoria = auditoria.id_auditoria,
        self.codigo = auditoria.codigo
        self.fecha = auditoria.fecha
        self.auditor = auditoria.auditor
        self.fase = auditoria.fase
        self.hallazgos = auditoria.hallazgos
        self.objetivo = auditoria.objetivo

        self.agregar_evento(AuditoriaCreada(codigo=self.id, fecha_creacion=datetime.now()))