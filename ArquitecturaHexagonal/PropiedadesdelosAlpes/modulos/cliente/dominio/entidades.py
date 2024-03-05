from __future__ import annotations

from dataclasses import dataclass, field

import PropiedadesdelosAlpes.modulos.cliente.dominio.objetos_valor as ov
from PropiedadesdelosAlpes.modulos.cliente.dominio.eventos import ClienteCreado
from PropiedadesdelosAlpes.seedwork.dominio.entidades import AgregacionRaiz, Entidad


@dataclass
class Cliente(AgregacionRaiz):
    id_cliente: str = field(default_factory=str)
    nombre: ov.Nombre = field(default_factory=ov.Nombre)
    apellido: ov.Apellido = field(default_factory=ov.Apellido)
    email: ov.Email = field(default_factory=ov.Email)

    def crear_cliente(self, cliente: Cliente):
        self.id_cliente = cliente.id_cliente,
        self.nombre = cliente.nombre,
        self.apellido = cliente.apellido,
        self.email = cliente.email

        self.agregar_evento(ClienteCreado(id_cliente=self.id_cliente, nombre=self.nombre, apellido=self.apellido, email=self.email))
