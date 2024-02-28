from dataclasses import dataclass, field

from ....seedwork.aplicacion.dto import DTO


@dataclass(frozen=True)
class NombreCompletoDTO(DTO):
    nombre: str
    apellido: str


@dataclass(frozen=True)
class EmailContactoDTO(DTO):
    correo: str


@dataclass(frozen=True)
class IdentificacionDTO(DTO):
    tipo: str
    numero: str


@dataclass(frozen=True)
class ClienteDTO(DTO):
    nombre: str = field(default_factory=str)
    apellido: str = field(default_factory=str)
