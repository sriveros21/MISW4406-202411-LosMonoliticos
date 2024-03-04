from __future__ import annotations
from dataclasses import dataclass, field
from ....seedwork.dominio.eventos import (EventoDominio)
from datetime import datetime

@dataclass
class AuditoriaCreada(EventoDominio):
    codigo: str = None
    fecha_creacion: datetime = None

#Revisar sí aca la fase debe ponerse con Enum
@dataclass
class FaseAuditoriaCambiada(EventoDominio):
    codigo: str = None
    nueva_fase: str = None
    fecha_actualizacion: datetime = None

