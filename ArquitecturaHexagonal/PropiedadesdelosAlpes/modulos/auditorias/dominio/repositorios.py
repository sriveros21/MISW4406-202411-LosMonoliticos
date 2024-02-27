"""Interfaces para los repositorios del dominio auditorias

En este archivo se encontrarán las diferentes interfaces para repositorios

"""

from abc import ABC
from ArquitecturaHexagonal.PropiedadesdelosAlpes.seedwork.dominio.repositorios import Repositorio

class RepositorioAuditorias(Repositorio, ABC):
    # Métodos específicos para manejar propiedades
    pass

