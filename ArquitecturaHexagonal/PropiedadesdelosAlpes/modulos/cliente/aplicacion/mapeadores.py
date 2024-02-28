from .dto import ClienteDTO
from ....modulos.cliente.dominio.entidades import Cliente
from ....seedwork.aplicacion.dto import Mapeador as AppMap
from ....seedwork.dominio.repositorios import Mapeador as RepMap


class MapeadorClienteDTOJson(AppMap):
    def externo_a_dto(self, cliente: dict) -> ClienteDTO:
        cliente_dto = ClienteDTO()

        cliente_dto.nombre.nombre = cliente.nombre
        cliente_dto.nombre.apellido = cliente.apellido
        cliente_dto.email.correo = cliente.email

        cliente_dto.cliente.append()
        return cliente_dto

    def dto_a_externo(self, dto: ClienteDTO) -> dict:
        return dto.__dict__


class MapeadorCliente(RepMap):
    def obtener_tipo(self) -> type:
        return Cliente.__class__

    def entidad_a_dto(self, entidad: Cliente) -> ClienteDTO:
        return ClienteDTO(
            nombre=entidad.nombre.nombre,
            apellido=entidad.nombre.apellido,
            email=entidad.email.correo
        )

    def dto_a_entidad(self, dto: ClienteDTO) -> Cliente:
        cliente = Cliente()
        return cliente
