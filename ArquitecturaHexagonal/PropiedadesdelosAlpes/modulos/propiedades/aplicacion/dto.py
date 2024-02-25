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

#Ajustar este con entidad Propiedad en el Dominio
@dataclass(frozen=True)
class PropiedadDTO(DTO):
    fecha_creacion: str = field(default_factory=str)
    fecha_actualizacion: str = field(default_factory=str)
    id: str = field(default_factory=str)
    nombre:str = field(default_factory=str)
    ubicacion: str = field(default_factory=str)
    dimensiones: str = field(default_factory=str)
    tipo: str = field(default_factory=str)
    estado: str = field(default_factory=str)
    edificaciones: str = field(default_factory=str)
    terreno: str = field(default_factory=str)