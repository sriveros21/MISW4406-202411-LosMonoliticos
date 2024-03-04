from PropiedadesdelosAlpes.modulos.cliente.dominio.entidades import Cliente as ClienteEntidad
from PropiedadesdelosAlpes.modulos.cliente.dominio.objetos_valor import Nombre, Apellido, Email
from PropiedadesdelosAlpes.seedwork.dominio.repositorios import Mapeador

from .dto import Cliente as ClienteDTO
from ..dominio.objetos_valor import Apellido


class MapeadorCliente(Mapeador):

    def obtener_tipo(self) -> type:
        return ClienteEntidad.__class__

    def entidad_a_dto(self, entidad: ClienteEntidad) -> ClienteDTO:
        cliente_dto = ClienteDTO()
        cliente_dto.id_cliente = ''.join(map(str, entidad.id_cliente))
        cliente_dto.nombre = entidad.nombre.nombre
        cliente_dto.apellido = entidad.apellido.apellido
        cliente_dto.email = entidad.email.email
        return cliente_dto

    def dto_a_entidad(self, dto: ClienteDTO) -> ClienteEntidad:
        id_cliente = dto.id_cliente
        nombre = Nombre(nombre=dto.nombre)
        apellido = Apellido(apellido=dto.apellido)
        email = Email(email=dto.email)

        return ClienteEntidad(
            id_cliente=id_cliente,
            nombre=nombre,
            apellido=apellido,
            email=email
        )
