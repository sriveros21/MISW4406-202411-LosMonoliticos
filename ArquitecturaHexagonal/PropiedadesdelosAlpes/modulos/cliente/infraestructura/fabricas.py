from dataclasses import dataclass

from PropiedadesdelosAlpes.modulos.cliente.dominio.fabricas import FabricaCliente
from PropiedadesdelosAlpes.modulos.cliente.dominio.repositorios import RepositorioCliente
from PropiedadesdelosAlpes.modulos.cliente.infraestructura.mapeadores import MapeadorCliente
from sqlalchemy.orm import Session

from .repositorios import RepositorioClienteSQLite


@dataclass
class FabricaRepositorioCliente:

    def __init__(self, db_session: Session):
        self.db_session = db_session

    def crear_repositorio_cliente(self) -> RepositorioClienteSQLite:
        mapeador_cliente = MapeadorCliente(db_session=self.db_session)
        fabrica_cliente = FabricaCliente()
        return RepositorioClienteSQLite(db_session=self.db_session, mapeador=mapeador_cliente, fabrica=fabrica_cliente)

    def obtener_repositorio_propiedades(self) -> RepositorioCliente:
        """
        Returns an instance of RepositorioPropiedades.
        This method simplifies accessing the properties repository.
        """
        return RepositorioClienteSQLite()
