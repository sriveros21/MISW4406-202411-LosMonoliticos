from abc import ABC, abstractmethod

from .mixins import ValidarReglasMixin
from .repositorios import Mapeador


class Fabrica(ABC, ValidarReglasMixin):
    @abstractmethod
    def crear_objeto(self, obj: any, mapeador: Mapeador = None) -> any:
        pass
