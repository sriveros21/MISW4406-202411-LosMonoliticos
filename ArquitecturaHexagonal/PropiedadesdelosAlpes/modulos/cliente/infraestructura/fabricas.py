from dataclasses import dataclass

from PropiedadesdelosAlpes.modulos.cliente.dominio.repositorios import RepositorioCliente
from PropiedadesdelosAlpes.seedwork.dominio.fabricas import Fabrica
from PropiedadesdelosAlpes.seedwork.dominio.repositorios import Repositorio

from .excepciones import ExcepcionFabrica
from .repositorios import RepositorioClienteSQLite


@dataclass
class FabricaRepositorio(Fabrica):
    def crear_objeto(self, obj: type, mapeador: any = None) -> Repositorio:
        if obj == RepositorioCliente.__class__:
            return RepositorioClienteSQLite()
        else:
            raise ExcepcionFabrica()

    def obtener_repositorio_propiedades(self) -> RepositorioCliente:
        """
        Returns an instance of RepositorioPropiedades.
        This method simplifies accessing the properties repository.
        """
        return RepositorioClienteSQLite()
