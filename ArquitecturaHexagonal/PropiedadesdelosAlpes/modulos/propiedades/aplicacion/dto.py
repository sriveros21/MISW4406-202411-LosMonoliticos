from dataclasses import dataclass, field
from PropiedadesdelosAlpes.seedwork.aplicacion.dto import DTO

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
    dimensiones: float
    pisos: list[PisoDTO] = field(default_factory=list)

@dataclass(frozen=True)
class TerrenoDTO(DTO):
    id: str
    dimensiones: float
    lote: str

#Ajustar este con entidad Propiedad en el Dominio
@dataclass(frozen=True)
class PropiedadDTO(DTO):
    fecha_creacion: str = field(default_factory=str)
    fecha_actualizacion: str = field(default_factory=str)
    id: str = field(default_factory=str)
    nombre:str = field(default_factory=str)
    ubicacion: str = field(default_factory=str)
    dimensiones: float = field(default_factory=float)
    tipo: str = field(default_factory=str)
    estado: str = field(default_factory=str)
    edificaciones: list[EdificacionDTO] = field(default_factory=list)
    terreno: TerrenoDTO = field(default_factory=TerrenoDTO)