import uuid
from dataclasses import dataclass

from ....seedwork.dominio.eventos import (EventoDominio)


@dataclass
class ClienteCreado(EventoDominio):
    cliente_id: uuid.UUID = None
    nombre: str = None
    apellido: str = None


@dataclass
class ClienteConsultado(EventoDominio):
    cliente_id: uuid.UUID = None
