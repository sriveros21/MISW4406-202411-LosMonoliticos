from dataclasses import dataclass

from PropiedadesdelosAlpes.seedwork.dominio.fabricas import Fabrica
from PropiedadesdelosAlpes.seedwork.dominio.repositorios import Mapeador

from .entidades import Cliente, Entidad
from .excepciones import TipoObjetoNoExisteEnDominioClienteExcepcion


@dataclass
class _FabricaCliente(Fabrica):
    def crear_objeto(self, obj: any, mapeador: Mapeador) -> any:
        if isinstance(obj, Entidad):
            return mapeador.entidad_a_dto(obj)
        else:
            cliente: Cliente = mapeador.dto_a_entidad(obj)
            return cliente


@dataclass
class FabricaCliente(Fabrica):
    def crear_objeto(self, obj: any, mapeador: Mapeador) -> any:
        if mapeador.obtener_tipo() == Cliente.__class__:
            fabrica_cliente = _FabricaCliente()
            return fabrica_cliente.crear_objeto(obj, mapeador)
        else:
            raise TipoObjetoNoExisteEnDominioClienteExcepcion()

    # repositorio_cliente: Repositorio
    # mapeador: Type[Mapeador] = MapeadorCliente
    #
    # def crear_desde_dto(self, dto: any) -> Cliente:
    #     # Assuming dto is an instance of a data transfer object for Propiedad
    #     cliente: Cliente = self.mapeador.dto_a_entidad(dto)
    #
    #     # Validate specific rules for property creation
    #     if not NombreValido(cliente.nombre).es_valido():
    #         raise TipoObjetoNoExisteEnDominioClienteExcepcion("Nombre no válido.")
    #
    #     # Additional logic for processing or storing the created Propiedad entity
    #     self.repositorio_cliente.agregar(cliente)
    #
    #     return cliente
