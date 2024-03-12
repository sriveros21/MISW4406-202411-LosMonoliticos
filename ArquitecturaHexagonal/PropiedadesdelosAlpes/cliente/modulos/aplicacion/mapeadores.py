from PropiedadesdelosAlpes.cliente.modulos.dominio.entidades import Cliente
from PropiedadesdelosAlpes.cliente.seedwork.aplicacion.dto import Mapeador as AppMap
from PropiedadesdelosAlpes.cliente.seedwork.dominio.repositorios import Mapeador as RepMap

from .dto import ClienteDTO


class MapeadorClienteDTOJson(AppMap):

    def externo_a_dto(self, externo: dict) -> ClienteDTO:
        cliente_dto = ClienteDTO(
            externo.get('id_cliente'),
            externo.get('nombre'),
            externo.get('apellido'),
            externo.get('email')
        )
        return cliente_dto

    def dto_a_externo(self, dto: ClienteDTO) -> dict:
        return dto.__dict__


class MapeadorCliente(RepMap):

    def obtener_tipo(self) -> type:
        return Cliente.__class__

    @staticmethod
    def entidad_a_dto(entidad: Cliente) -> ClienteDTO:
        return ClienteDTO(
            _id_cliente=str(entidad.id_cliente),
            nombre=entidad.nombre,
            apellido=entidad.apellido,
            email=entidad.email
        )

    def dto_a_entidad(self, dto: ClienteDTO) -> Cliente:
        return Cliente(
            id_cliente=dto.id_cliente,
            nombre=dto.nombre,
            apellido=dto.apellido,
            email=dto.email
        )
