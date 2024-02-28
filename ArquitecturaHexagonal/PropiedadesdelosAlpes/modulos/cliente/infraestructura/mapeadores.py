from PropiedadesdelosAlpes.modulos.cliente.dominio.entidades import Cliente
from PropiedadesdelosAlpes.seedwork.dominio.repositorios import Mapeador

from .dto import Cliente as ClienteDTO


class MapeadorCliente(Mapeador):
    def obtener_tipo(self) -> type:
        return Cliente.__class__

    def entidad_a_dto(self, entidad: Cliente) -> ClienteDTO:
        cliente_dto = ClienteDTO()
        cliente_dto.id_cliente = entidad.id
        cliente_dto.nombre_cliente = entidad.nombre
        cliente_dto.apellido_cliente = entidad.apellido
        cliente_dto.email_cliente = entidad.email

        return cliente_dto

    def dto_a_entidad(self, dto: ClienteDTO) -> Cliente:
        cliente = Cliente(
            dto.id_cliente,
            dto.nombre_cliente,
            dto.email_cliente
        )

        return cliente
