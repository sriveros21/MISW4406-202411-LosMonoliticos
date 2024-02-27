""" Mapeadores para la capa de infrastructura del dominio de propiedades

En este archivo usted encontrará los diferentes mapeadores
encargados de la transformación entre formatos de dominio y DTOs

"""

from .dto import Cliente as ClienteDTO
from ....modulos.cliente.dominio.entidades import Cliente
from ....seedwork.dominio.repositorios import Mapeador


class MapeadorClientes(Mapeador):
    _FORMATO_FECHA = '%Y-%m-%dT%H:%M:%SZ'

    def obtener_tipo(self) -> type:
        return Cliente.__class__

    def entidad_a_dto(self, entidad: Cliente) -> ClienteDTO:
        cliente_dto = ClienteDTO()
        cliente_dto.id_cliente = entidad.id
        cliente_dto.nombre_cliente = entidad.nombre
        cliente_dto.email_cliente = entidad.email

        return cliente_dto

    def dto_a_entidad(self, dto: ClienteDTO) -> Cliente:
        cliente = Cliente(
            dto.id_cliente,
            dto.nombre_cliente,
            dto.email_cliente
        )

        return cliente
