from PropiedadesdelosAlpes.modulos.cliente.dominio.entidades import Cliente
from PropiedadesdelosAlpes.modulos.cliente.dominio.objetos_valor import Nombre, Apellido, Email
from PropiedadesdelosAlpes.seedwork.dominio.repositorios import Mapeador

from .dto import Cliente as ClienteDTO
from ..dominio.objetos_valor import Apellido


class MapeadorCliente(Mapeador):

    def obtener_tipo(self) -> type:
        return Cliente.__class__

    def entidad_a_dto(self, entidad: Cliente) -> ClienteDTO:
        cliente_dto = ClienteDTO()
        cliente_dto.id_cliente = ''.join(map(str, entidad.id_cliente))
        cliente_dto.nombre = ''.join(map(str, entidad.nombre))
        cliente_dto.apellido = ''.join(map(str, entidad.apellido))
        cliente_dto.email = entidad.email
        return cliente_dto

    def dto_a_entidad(self, dto: ClienteDTO) -> Cliente:
        id_cliente = dto.id_cliente
        nombre = Nombre(nombre=dto.nombre)
        apellido = Apellido(apellido=dto.apellido)
        email = Email(email=dto.email)

        return Cliente(
            id_cliente=id_cliente,
            nombre=nombre,
            apellido=apellido,
            email=email
        )
