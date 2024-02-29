from PropiedadesdelosAlpes.modulos.cliente.dominio.entidades import Cliente
from PropiedadesdelosAlpes.seedwork.dominio.repositorios import Mapeador

from .dto import Cliente as ClienteDTO


class MapeadorCliente(Mapeador):

    def obtener_tipo(self) -> type:
        return Cliente.__class__

    def entidad_a_dto(self, entidad: Cliente) -> ClienteDTO:
        cliente_dto = ClienteDTO()
        cliente_dto.id = entidad.id
        cliente_dto.nombre = entidad.nombre
        cliente_dto.apellido = entidad.apellido
        cliente_dto.email = entidad.email

        return cliente_dto

    def dto_a_entidad(self, dto: ClienteDTO) -> Cliente:
        cliente = Cliente(
            dto.id,
            dto.nombre,
            dto.apellido,
            dto.email
        )

        return cliente
