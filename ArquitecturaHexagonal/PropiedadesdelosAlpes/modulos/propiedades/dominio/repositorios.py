from abc import ABC
from ArquitecturaHexagonal.PropiedadesdelosAlpes.seedwork.dominio.repositorios import Repositorio

class RepositorioPropiedades(Repositorio, ABC):
    # Métodos específicos para manejar propiedades
    pass

class RepositorioClientes(Repositorio, ABC):
    # Métodos específicos para manejar clientes
    pass
