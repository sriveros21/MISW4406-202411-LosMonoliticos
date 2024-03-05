from uuid import UUID

from PropiedadesdelosAlpes.config.db import db
from PropiedadesdelosAlpes.modulos.cliente.dominio.entidades import Cliente
from PropiedadesdelosAlpes.modulos.cliente.dominio.fabricas import FabricaCliente
from PropiedadesdelosAlpes.modulos.cliente.dominio.repositorios import RepositorioCliente

from .dto import Cliente as ClienteDTO
from .mapeadores import MapeadorCliente


class RepositorioClienteSQLite(RepositorioCliente):
    def __init__(self):
        self._fabrica_cliente: FabricaCliente = FabricaCliente()

    @property
    def fabrica_cliente(self):
        return self._fabrica_cliente

    def obtener_por_id(self, id_cliente: UUID) -> Cliente:
        cliente_dto = db.session.query(ClienteDTO).filter_by(id_cliente=str(id_cliente)).one()
        return self.fabrica_cliente.crear_objeto(cliente_dto, MapeadorCliente())

    def agregar(self, cliente: Cliente):
        cliente_dto = self.fabrica_cliente.crear_objeto(cliente, MapeadorCliente())
        db.session.add(cliente_dto)
        db.session.commit()
