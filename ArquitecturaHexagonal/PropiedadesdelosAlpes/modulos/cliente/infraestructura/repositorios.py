""" Repositorios para el manejo de persistencia de objetos de dominio en la capa de infrastructura del dominio de clientes

En este archivo usted encontrará las diferentes repositorios para
persistir objetos dominio (agregaciones) en la capa de infraestructura del dominio de clientes

"""

from PropiedadesdelosAlpes.config.db import db
from PropiedadesdelosAlpes.modulos.cliente.dominio.repositorios import RepositorioClientes
from PropiedadesdelosAlpes.modulos.cliente.dominio.entidades import Cliente
from PropiedadesdelosAlpes.modulos.cliente.dominio.fabricas import FabricaClientes
from .dto import Cliente as ClienteDTO
from .mapeadores import MapeadorClientes
from uuid import UUID
from typing import List


class RepositorioClientesSQLite(RepositorioClientes):

    def __init__(self):
        self._fabrica_clientes: FabricaClientes = FabricaClientes()

    @property
    def fabrica_clientes(self):
        return self._fabrica_clientes

    def obtener_por_id(self, id: UUID) -> Cliente:
        cliente_dto = db.session.query(ClienteDTO).filter_by(id=str(id)).one()
        return self.fabrica_clientes.crear_objeto(cliente_dto, MapeadorClientes())

    def obtener_todos(self) -> List[Cliente]:
        id_cliente = 123
        nombre_cliente = "cliente.nombre"
        email_cliente = "cliente.email"

        cliente = Cliente(
            id=id_cliente,
            nombre=nombre_cliente,
            email=email_cliente
        )

        return [cliente]

    def agregar(self, cliente: Cliente):
        cliente_dto = self.fabrica_clientes.crear_objeto(cliente, MapeadorClientes())
        db.session.add(cliente_dto)
        db.session.commit()

    def actualizar(self, cliente: Cliente):
        # TODO
        raise NotImplementedError

    def eliminar(self, cliente_id: UUID):
        # TODO
        raise NotImplementedError