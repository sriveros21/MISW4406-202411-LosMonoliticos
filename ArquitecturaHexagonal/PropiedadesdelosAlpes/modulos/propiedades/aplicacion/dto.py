from dataclasses import dataclass, field
from PropiedadesdelosAlpes.seedwork.dominio.objetos_valor import Dimension
from PropiedadesdelosAlpes.seedwork.aplicacion.dto import DTO
from typing import List

@dataclass(frozen=True)
class InformacionGeoespacialDTO(DTO):
    latitude: str
    longitude:str

@dataclass(frozen=True)
class IdentificadorPropiedadDTO(DTO):
    identificador:str

@dataclass(frozen=True)
class PrecioDTO(DTO):
    valor:str
    moneda:str

@dataclass(frozen=True)
class PisoDTO(DTO):
    descripcion: str
    metros_cuadrados: float

@dataclass(frozen=True)
class EdificacionDTO(DTO):
    id: str
    tipo: str  # Minorista, Oficina, Industrial, Especializado
    dimensiones: Dimension
    pisos: List[PisoDTO] = field(default_factory=list)

@dataclass(frozen=True)
class TerrenoDTO(DTO):
    id: str
    dimensiones: Dimension
    lote: str

@dataclass(frozen=True)
class PropiedadDTO(DTO):
    id_propiedad: str = field(default_factory=str)
    nombre:str = field(default_factory=str)
    ubicacion: str = field(default_factory=str)
    dimensiones: Dimension = field(default_factory=float)
    tipo: str = field(default_factory=str)
    estado: str = field(default_factory=str)
    edificaciones: List[EdificacionDTO] = field(default_factory=list)
    terreno: TerrenoDTO = field(default_factory=TerrenoDTO)