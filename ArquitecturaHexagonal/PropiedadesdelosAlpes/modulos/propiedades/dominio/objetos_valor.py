from dataclasses import dataclass, field
from ArquitecturaHexagonal.PropiedadesdelosAlpes.seedwork.dominio.objetos_valor import ObjetoValor
from datetime import datetime
from enum import Enum

@dataclass(frozen=True)
class Direccion(ObjetoValor):
    calle: str
    numero: str
    ciudad: str
    estado: str
    codigo_postal: str

@dataclass(frozen=True)
class Dimensiones(ObjetoValor):
    metros_cuadrados: float

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
class FechaConstruccion(ObjetoValor):
    fecha: datetime

@dataclass(frozen=True)
class Precio(ObjetoValor):
    valor: float
    moneda: str
