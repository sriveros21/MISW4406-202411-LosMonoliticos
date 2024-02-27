from dataclasses import dataclass
from typing import Type

from .entidades import Cliente
from .excepciones import TipoObjetoNoExisteEnDominioClienteExcepcion
from .reglas import NombreValido
from ....modulos.cliente.infraestructura.mapeadores import MapeadorClientes
from ....seedwork.dominio.fabricas import Fabrica
from ....seedwork.dominio.repositorios import Mapeador, Repositorio


@dataclass
class FabricaCliente(Fabrica):
    repositorio_cliente: Repositorio
    mapeador: Type[Mapeador] = MapeadorClientes

    def crear_desde_dto(self, dto: any) -> Cliente:
        # Assuming dto is an instance of a data transfer object for Propiedad
        cliente: Cliente = self.mapeador.dto_a_entidad(dto)

        # Validate specific rules for property creation
        if not NombreValido(cliente.nombre).es_valido():
            raise TipoObjetoNoExisteEnDominioClienteExcepcion("Nombre no válido.")

        # Additional logic for processing or storing the created Propiedad entity
        self.repositorio_cliente.agregar(cliente)

        return cliente
