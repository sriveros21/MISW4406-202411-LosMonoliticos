from PropiedadesdelosAlpes.modulos.cliente.dominio.entidades import Cliente
from PropiedadesdelosAlpes.seedwork.aplicacion.dto import Mapeador as AppMap
from PropiedadesdelosAlpes.seedwork.dominio.repositorios import Mapeador as RepMap

from .dto import ClienteDTO


class MapeadorClienteDTOJson(AppMap):
    def externo_a_dto(self, cliente: dict) -> ClienteDTO:
        cliente_dto = ClienteDTO()
        cliente_dto.nombre = cliente.get('nombre')
        cliente_dto.apellido = cliente.get('apellido')
        cliente_dto.email = cliente.get('email')

        return cliente_dto

    def dto_a_externo(self, dto: ClienteDTO) -> dict:
        return dto.__dict__


class MapeadorCliente(RepMap):
    def obtener_tipo(self) -> type:
        return Cliente.__class__

    def entidad_a_dto(self, entidad: Cliente) -> ClienteDTO:
        return ClienteDTO(
            nombre=entidad.nombre.valor,
            apellido=entidad.apellido.valor,
            email=entidad.email.valor
        )

    def dto_a_entidad(self, dto: ClienteDTO) -> Cliente:
        cliente = Cliente()
        return cliente
