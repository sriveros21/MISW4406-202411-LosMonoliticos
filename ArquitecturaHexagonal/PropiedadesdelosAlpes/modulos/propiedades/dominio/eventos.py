from __future__ import annotations
from dataclasses import dataclass, field
from ....seedwork.dominio.eventos import (EventoDominio)
from datetime import datetime
import uuid

@dataclass
class PropiedadCreada(EventoDominio):
    propiedad_id: uuid.UUID
    nombre: str
    ubicacion: str
    
@dataclass(frozen=True)
class EstadoPropiedadCambiado(EventoDominio):
    propiedad_id: uuid.UUID
    nuevo_estado: str