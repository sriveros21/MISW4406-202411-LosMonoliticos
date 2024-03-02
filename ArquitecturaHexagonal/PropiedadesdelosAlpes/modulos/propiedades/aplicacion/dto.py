from dataclasses import dataclass, field
from PropiedadesdelosAlpes.seedwork.dominio.objetos_valor import Dimension
from PropiedadesdelosAlpes.seedwork.aplicacion.dto import DTO
from typing import List


@dataclass(frozen=True)
class UbicacionDTO(DTO):
    latitud: float
    longitud: float

@dataclass(frozen=True)
class DimensionDTO(DTO):
    width: float
    length: float
    unit: str

@dataclass(frozen=True)
class PisoDTO(DTO):
    numero: int

@dataclass(frozen=True)
class EdificacionDTO(DTO):
    id: str
    tipo: str  # Minorista, Oficina, Industrial, Especializado
    dimension: DimensionDTO
    pisos: List[PisoDTO] = field(default_factory=list)

@dataclass(frozen=True)
class TerrenoDTO(DTO):
    id: str
    dimension: DimensionDTO
    lote: str

@dataclass(frozen=True)
class PropiedadDTO(DTO):
    id: str = field(default_factory=str)
    nombre:str = field(default_factory=str)
    ubicacion: UbicacionDTO = field(default_factory=float)
    dimension: DimensionDTO = field(default_factory=float)
    tipo: str = field(default_factory=str)
    estado: str = field(default_factory=str)
    edificaciones: List[EdificacionDTO] = field(default_factory=list)
    terreno: TerrenoDTO = field(default_factory=TerrenoDTO)