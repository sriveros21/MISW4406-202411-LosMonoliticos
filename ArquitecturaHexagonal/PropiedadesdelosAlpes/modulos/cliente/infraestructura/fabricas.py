""" Fábricas para la creación de objetos en la capa de infrastructura del dominio de propiedades

En este archivo usted encontrará las diferentes fábricas para crear
objetos complejos en la capa de infraestructura del dominio de propiedades

"""

from dataclasses import dataclass

from .excepciones import ExcepcionFabrica
from .repositorios import RepositorioClienteSQLite
from ....modulos.cliente.dominio.repositorios import RepositorioCliente
from ....seedwork.dominio.fabricas import Fabrica
from ....seedwork.dominio.repositorios import Repositorio


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
