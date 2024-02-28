from typing import List
from uuid import UUID

from PropiedadesdelosAlpes.modulos.cliente.dominio.entidades import Cliente
from PropiedadesdelosAlpes.modulos.cliente.dominio.fabricas import FabricaCliente
from PropiedadesdelosAlpes.modulos.cliente.dominio.repositorios import RepositorioCliente

from .dto import Cliente as ClienteDTO
from .mapeadores import MapeadorCliente
from ....config.db import db


class RepositorioClienteSQLite(RepositorioCliente):
    def __init__(self):
        self._fabrica_cliente: FabricaCliente = FabricaCliente()

    @property
    def fabrica_cliente(self):
        return self._fabrica_cliente

    def obtener_por_id(self, id: UUID) -> Cliente:
        cliente_dto = db.session.query(ClienteDTO).filter_by(id=str(id)).one()
        return self.fabrica_cliente.crear_objeto(cliente_dto, MapeadorCliente())

    def obtener_todos(self) -> List[Cliente]:
        id_cliente = 123
        nombre_cliente = "cliente.nombre"
        apellido_cliente = "cliente.apellido"
        email_cliente = "cliente.email"

        cliente = Cliente(
            id=id_cliente,
            nombre=nombre_cliente,
            apellido=apellido_cliente,
            email=email_cliente
        )

        return [cliente]

    def agregar(self, cliente: Cliente):
        cliente_dto = self.fabrica_cliente.crear_objeto(cliente, MapeadorCliente())
        db.session.add(cliente_dto)
        db.session.commit()
