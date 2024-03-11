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
    codigo_auditoria:str = field(default_factory=str)
    fecha_auditoria:str = field(default_factory=str)
    nombre_auditor:str = field(default_factory=str)
    fase_auditoria:str = field(default_factory=str)
    hallazgos_auditoria:str = field(default_factory=str)
    objetivo_auditoria: str = field(default_factory=str)

    def crear_auditoria(self, auditoria: Auditoria):
        self.id = auditoria.id,
        self.id_auditoria = auditoria.id_auditoria,
        self.codigo = auditoria.codigo_auditoria
        self.fecha = datetime.strptime(auditoria.fecha_auditoria, '%d-%m-%Y %H:%M:%S')
        self.auditor = auditoria.nombre_auditor
        self.fase = auditoria.fase_auditoria
        self.hallazgos = auditoria.hallazgos_auditoria
        self.objetivo = auditoria.objetivo_auditoria

        self.agregar_evento(AuditoriaCreada(
            id=self.id, 
            id_auditoria = self.id_auditoria,
            codigo=self.codigo, 
            fecha_creacion=self.fecha,
            auditor = self.nombre_auditor,
            fase = self.fase_auditoria,
            hallazgos = self.hallazgos_auditoria,
            objetivo = self.objetivo_auditoria,
            ))