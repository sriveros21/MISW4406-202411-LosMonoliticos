from PropiedadesdelosAlpes.modulos.cliente.dominio.entidades import Cliente
from PropiedadesdelosAlpes.seedwork.aplicacion.dto import Mapeador as AppMap
from PropiedadesdelosAlpes.seedwork.dominio.repositorios import Mapeador as RepMap

from .dto import ClienteDTO


class MapeadorClienteDTOJson(AppMap):

    def externo_a_dto(self, externo: dict) -> ClienteDTO:
        cliente_dto = ClienteDTO(
            id_cliente=externo.get('id_cliente'),
            nombre=str(externo['nombre']),
            apellido=str(externo['apellido']),
            email=str(externo['email'])
        )
        return cliente_dto

    def dto_a_externo(self, dto: ClienteDTO) -> dict:
        return {
            "id_cliente": dto.id_cliente,
            "nombre": dto.nombre,
            "apellido": dto.apellido,
            "email": dto.email
        }


class MapeadorCliente(RepMap):

    def obtener_tipo(self) -> type:
        return Cliente.__class__

    def entidad_a_dto(self, entidad: Cliente) -> ClienteDTO:
        cliente_dto = ClienteDTO(
            id_cliente=str(entidad.id_cliente),
            nombre=entidad.nombre,
            apellido=entidad.apellido,
            email=entidad.email
        )

        return cliente_dto

    def dto_a_entidad(self, dto: ClienteDTO) -> Cliente:
        cliente: Cliente = dto
        return cliente
