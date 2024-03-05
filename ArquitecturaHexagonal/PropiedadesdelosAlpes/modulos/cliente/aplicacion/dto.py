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
class ClienteDTO(DTO):
    id_cliente: str = field(default_factory=str)
    nombre: str = field(default_factory=str)
    apellido: ApellidoDTO = field(default_factory=ApellidoDTO)
    email: EmailDTO = field(default_factory=EmailDTO)
