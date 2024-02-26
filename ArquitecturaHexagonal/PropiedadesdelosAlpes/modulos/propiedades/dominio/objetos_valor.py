from dataclasses import dataclass, field
from ....seedwork.dominio.objetos_valor import ObjetoValor
from datetime import datetime
from enum import Enum

@dataclass(frozen=True)
class InformacionGeoespacial:
    latitude: float
    longitude: float

@dataclass(frozen=True)
class IdentificadorPropiedad:
    identificador: str

@dataclass(frozen=True)
class EstadoPropiedad(Enum):
    DISPONIBLE = "Disponible"
    NO_DISPONIBLE = "No Disponible"
    EN_REPARACION = "En Reparación"

@dataclass(frozen=True)
class TipoPropiedad(Enum):
    RESIDENCIAL = "Residencial"
    COMERCIAL = "Comercial"
    INDUSTRIAL = "Industrial"

@dataclass(frozen=True)
class Precio(ObjetoValor):
    valor: float
    moneda: str

@dataclass(frozen=True)
class Piso(ObjetoValor):
    valor: float

@dataclass(frozen=True)
class Lote(ObjetoValor):
    valor: float

@dataclass(frozen=True)
class Nombre(ObjetoValor):
    valor: str
