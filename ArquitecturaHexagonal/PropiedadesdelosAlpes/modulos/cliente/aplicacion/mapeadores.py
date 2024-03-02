from PropiedadesdelosAlpes.modulos.cliente.dominio.entidades import Cliente
from PropiedadesdelosAlpes.seedwork.aplicacion.dto import Mapeador as AppMap
from PropiedadesdelosAlpes.seedwork.dominio.repositorios import Mapeador as RepMap

from .dto import ClienteDTO


class MapeadorClienteDTOJson(AppMap):

    def externo_a_dto(self, cliente: dict) -> ClienteDTO:
        cliente_dto = ClienteDTO(
            id_cliente=cliente.get('id_cliente'),
            nombre=cliente.get('nombre'),
            apellido=cliente.get('apellido'),
            email=cliente.get('email')
        )
        return cliente_dto

    def dto_a_externo(self, dto: ClienteDTO) -> dict:
        return dto.__dict__


class MapeadorCliente(RepMap):

    def obtener_tipo(self) -> type:
        return Cliente.__class__

    def entidad_a_dto(self, cliente: Cliente) -> ClienteDTO:
        return ClienteDTO(
            id_cliente=cliente.id_cliente,
            nombre=cliente.nombre,
            apellido=cliente.apellido,
            email=cliente.email
        )

    def dto_a_entidad(self, dto: ClienteDTO) -> Cliente:
        cliente: Cliente = dto
        return cliente