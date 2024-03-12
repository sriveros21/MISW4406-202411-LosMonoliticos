from dataclasses import dataclass

from PropiedadesdelosAlpes.cliente.modulos.dominio.repositorios import RepositorioCliente, RepositorioEventosCliente
from PropiedadesdelosAlpes.cliente.modulos.infraestructura.vistas import VistaCliente
from PropiedadesdelosAlpes.cliente.seedwork.dominio.fabricas import Fabrica
from PropiedadesdelosAlpes.cliente.seedwork.dominio.repositorios import Repositorio
from PropiedadesdelosAlpes.cliente.seedwork.infraestructura.vistas import Vista

from .excepciones import ExcepcionFabrica
from .repositorios import RepositorioClienteSQLAlchemy, RepositorioEventosClienteSQLAlchemy


@dataclass
class FabricaRepositorioCliente(Fabrica):

    def crear_objeto(self, obj: type, mapeador: any = None) -> Repositorio:
        if obj == RepositorioCliente:
            return RepositorioClienteSQLAlchemy()
        elif obj == RepositorioEventosCliente:
            return RepositorioEventosClienteSQLAlchemy()
        else:
            raise ExcepcionFabrica(f'No existe fábrica para el objeto {obj}')

    @dataclass
    class FabricaVista(Fabrica):
        def crear_objeto(self, obj: type, mapeador: any = None) -> Vista:
            if obj == Cliente:
                return VistaCliente()
            else:
                raise ExcepcionFabrica(f'No existe fábrica para el objeto {obj}')
