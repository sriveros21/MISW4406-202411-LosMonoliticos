from dataclasses import dataclass, field
from ....seedwork.dominio.objetos_valor import ObjetoValor
from datetime import datetime
from enum import Enum


class EstadoPropiedad(str,Enum):
    DISPONIBLE = "Disponible"
    NO_DISPONIBLE = "No Disponible"
    EN_REPARACION = "En Reparación"

class TipoPropiedad(str, Enum):
    RESIDENCIAL = "Residencial"
    COMERCIAL = "Comercial"
    INDUSTRIAL = "Industrial"
    ESPECIALIZADO = "Especializado"

@dataclass(frozen=True)
class Piso(ObjetoValor):
    numero: int

@dataclass(frozen=True)
class Nombre(ObjetoValor):
    valor: str
