import uuid
from dataclasses import dataclass

from ....seedwork.dominio.eventos import (EventoDominio)


class EventoCliente(EventoDominio):
    ...


@dataclass
class ClienteCreado(EventoCliente):
    id: str = None
    id_cliente: uuid.UUID = None
    nombre: str = None
    apellido: str = None
    email: str = None


@dataclass
class FaseClienteCambiado(EventoCliente):
    nombre: str = None
    apellido: str = None
    email: str = None
