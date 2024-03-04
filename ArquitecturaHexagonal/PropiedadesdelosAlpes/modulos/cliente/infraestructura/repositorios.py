from typing import List

from PropiedadesdelosAlpes.config.db import db
from PropiedadesdelosAlpes.modulos.cliente.dominio.entidades import Cliente
from PropiedadesdelosAlpes.modulos.cliente.dominio.fabricas import FabricaCliente
from PropiedadesdelosAlpes.modulos.cliente.dominio.repositorios import RepositorioCliente

from .dto import Cliente as ClienteDTO
from .mapeadores import MapeadorCliente


class RepositorioClienteSQLite(RepositorioCliente):
    def __init__(self, db_session, mapeador: MapeadorCliente, fabrica: FabricaCliente):
        self.db_session = db_session
        self.mapeador = mapeador
        self.fabrica = fabrica

    @property
    def fabrica_cliente(self):
        return self._fabrica

    def obtener_por_id(self, id_cliente: str) -> Cliente:
        cliente_dto = db.session.query(ClienteDTO).filter_by(id_cliente=str(id_cliente)).one()
        print("OBJETO DB CONSULTA 2", cliente_dto)
        return self.fabrica.crear_objeto(cliente_dto, self.mapeador)

    def agregar(self, cliente: Cliente):
        print("Agregando cliente")
        print(cliente)
        cliente_dto = self.fabrica.crear_objeto(cliente, self.mapeador)
        print(cliente_dto)
        print(self.mapeador)
        self.db_session.add(cliente_dto)
        self.db_session.commit()
