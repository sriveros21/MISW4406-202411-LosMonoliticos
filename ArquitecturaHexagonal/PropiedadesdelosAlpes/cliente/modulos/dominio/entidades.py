import uuid
from dataclasses import dataclass, field

from PropiedadesdelosAlpes.cliente.modulos.dominio.eventos.cliente import ClienteCreado
from PropiedadesdelosAlpes.cliente.seedwork.dominio.entidades import AgregacionRaiz, Entidad


@dataclass
class Cliente(AgregacionRaiz):
    id: uuid.UUID = field(hash=True, default=None)
    id_cliente: str = field(default_factory=str)
    nombre: str = field(default_factory=str)
    apellido: str = field(default_factory=str)
    email: str = field(default_factory=str)


def crear_cliente(self, cliente: Cliente):
    self.id = cliente.id,
    self.id_cliente = cliente.id_cliente,
    self.nombre = cliente.nombre,
    self.apellido = cliente.apellido,
    self.email = cliente.email

    self.agregar_evento(ClienteCreado(
        id=self.id,
        id_cliente=self.id_cliente,
        nombre=self.nombre,
        apellido=self.apellido,
        email=self.email
    ))
