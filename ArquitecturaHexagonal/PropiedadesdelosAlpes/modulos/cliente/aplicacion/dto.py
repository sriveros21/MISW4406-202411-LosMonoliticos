from dataclasses import dataclass, field

from PropiedadesdelosAlpes.seedwork.aplicacion.dto import DTO


@dataclass(frozen=True)
class NombreDTO(DTO):
    nombre: str


@dataclass(frozen=True)
class ApellidoDTO(DTO):
    apellido: str


@dataclass(frozen=True)
class EmailDTO(DTO):
    email: str


@dataclass(frozen=True)
class IdentificacionDTO(DTO):
    tipo: str
    numero: str


@dataclass(frozen=True)
class ClienteDTO(DTO):
    nombre: str = field(default_factory=str)
    apellido: str = field(default_factory=str)
    email: str = field(default_factory=str)
