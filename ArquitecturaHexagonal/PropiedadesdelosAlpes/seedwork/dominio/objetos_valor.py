from dataclasses import dataclass
from abc import ABC, abstractmethod
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
