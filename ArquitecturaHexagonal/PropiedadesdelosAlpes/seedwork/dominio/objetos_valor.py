from abc import ABC
from dataclasses import dataclass
from datetime import datetime


@dataclass(frozen=True)
class ObjetoValor:
    pass


@dataclass(frozen=True)
class IdentificadorUnico(ABC, ObjetoValor):
    id: str


@dataclass(frozen=True)
class Dimension:
    width: float
    length: float
    unit: str


@dataclass(frozen=True)
class Direccion(ObjetoValor):
    calle: str
    numero: str
    ciudad: str
    estado: str
    codigo_postal: str


@dataclass(frozen=True)
class Ubicacion(ObjetoValor):
    direccion: Direccion
    latitud: float
    longitud: float


@dataclass(frozen=True)
class Precio(ObjetoValor):
    valor: float
    moneda: str


@dataclass(frozen=True)
class Fecha(ObjetoValor):
    fecha: datetime


@dataclass(frozen=True)
class NombreCompleto(ObjetoValor):
    nombre: str
    apellido: str


@dataclass(frozen=True)
class EmailContacto(ObjetoValor):
    correo: str


@dataclass(frozen=True)
class Identificacion(ObjetoValor):
    tipo: str
    numero: str


@dataclass(frozen=True)
class FechaRegistro(ObjetoValor):
    fecha: datetime
