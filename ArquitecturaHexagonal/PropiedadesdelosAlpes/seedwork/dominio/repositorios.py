from abc import ABC, abstractmethod
from uuid import UUID
from .entidades import Entidad

class Repositorio(ABC):
    @abstractmethod
    def obtener_por_id(self, id: UUID) -> Entidad:
        pass

    @abstractmethod
    def obtener_todos(self) -> 'list[Entidad]':
        pass

    @abstractmethod
    def agregar(self, entidad: Entidad):
        pass

    # @abstractmethod
    # def actualizar(self, entidad: Entidad):
    #     pass
    #
    # @abstractmethod
    # def eliminar(self, entidad_id: UUID):
    #     pass

class Mapeador(ABC):
    @abstractmethod
    def obtener_tipo(self) -> type:
        pass

    @abstractmethod
    def entidad_a_dto(self, entidad: Entidad) -> any:
        pass

    @abstractmethod
    def dto_a_entidad(self, dto: any) -> Entidad:
        pass
