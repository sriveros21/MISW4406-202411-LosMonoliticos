from dataclasses import dataclass, field
from ArquitecturaHexagonal.PropiedadesdelosAlpes.seedwork.dominio.objetos_valor import ObjetoValor, Identificacion
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
