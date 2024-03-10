"""Objetos Valor del dominio auditorias

En este archivo usted encontrará los objetos valor del dominio auditorias

"""

from __future__ import annotations

from dataclasses import dataclass, field
from ....seedwork.dominio.objetos_valor import ObjetoValor, Fecha
from abc import ABC, abstractmethod
from datetime import datetime
from enum import Enum

@dataclass(frozen=True)
class FechaAuditoria(Fecha):
    ...

@dataclass(frozen=True)
class CodigoAuditoria(ABC, ObjetoValor):
    codigo: str

@dataclass(frozen=True)
class NombreAuditor(ObjetoValor):
    nombre_auditor: str

#@dataclass(frozen=True)
class FaseAuditoria(str, Enum):
    INICIAL = "Inicial"
    INTERMEDIA = "Intermedia"
    FINAL = "Final"

@dataclass(frozen=True)
class HallazgosAuditoria(ObjetoValor):
    hallazgos_auditoria: str

#@dataclass(frozen=True)
class ObjetivoAuditoria(str, Enum):
    VALIDAR_COBERTURA = "Validar Cobertura"
    VALIDAR_CALIDAD = "Validar Calidad"
    VALIDAR_CONFIABILIDAD = "Validar Confiabilidad"