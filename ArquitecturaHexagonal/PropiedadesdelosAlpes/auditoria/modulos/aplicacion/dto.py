from dataclasses import dataclass, field
from PropiedadesdelosAlpes.auditoria.seedwork.aplicacion.dto import DTO
from enum import Enum


@dataclass(frozen=True)
class FechaAuditoriaDTO(DTO):
    ...

@dataclass(frozen=True)
class CodigoAuditoriaDTO(DTO):
    codigo:str

@dataclass(frozen=True)
class NombreAuditorDTO(DTO):
    nombre_auditor:str

@dataclass(frozen=True)
class HallazgosAuditoriaDTO(DTO):
    hallazgos_auditoria:str

#Revisar estos Enums como quedan
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

#Revisar Enums
@dataclass(frozen=True)
class AuditoriaDTO(DTO):
    id: str = field(default_factory=str)
    id_auditoria: str = field(default_factory=str)
    codigo_auditoria: str = field(default_factory=str)
    fecha_auditoria: str = field(default_factory=str)
    nombre_auditor: str = field(default_factory=str)
    fase_auditoria: FaseAuditoria =field(default_factory=FaseAuditoria)
    hallazgos_auditoria: HallazgosAuditoriaDTO = field(default_factory=HallazgosAuditoriaDTO)
    objetivo_auditoria: ObjetivoAuditoria =field(default_factory=ObjetivoAuditoria)