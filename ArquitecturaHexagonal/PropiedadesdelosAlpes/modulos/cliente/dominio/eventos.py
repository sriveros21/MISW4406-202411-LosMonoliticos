import uuid
from dataclasses import dataclass

from PropiedadesdelosAlpes.seedwork.dominio.eventos import (EventoDominio)


@dataclass
class ClienteCreado(EventoDominio):
    cliente_id: uuid.UUID = None
    nombre: str = None
    apellido: str = None
    email: str = None


@dataclass
class ClienteConsultado(EventoDominio):
    cliente_id: uuid.UUID = None
