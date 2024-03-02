from PropiedadesdelosAlpes.modulos.cliente.dominio.entidades import Cliente as ClienteEntidad
from PropiedadesdelosAlpes.modulos.cliente.dominio.objetos_valor import Nombre, Apellido, Email
from PropiedadesdelosAlpes.modulos.cliente.infraestructura.dto import Cliente
from PropiedadesdelosAlpes.seedwork.dominio.repositorios import Mapeador

from .dto import Cliente as ClienteDTO
from ..dominio.objetos_valor import Apellido


class MapeadorCliente(Mapeador):

    def __init__(self, db_session):
        self.db_session = db_session

    def obtener_tipo(self) -> type:
        return ClienteEntidad.__class__

    def entidad_a_dto(self, cliente: ClienteEntidad) -> Cliente:
        cliente_dto = Cliente(
            id_cliente=cliente.id_cliente,
            nombre=cliente.nombre,
            apellido=cliente.apellido,
            email=cliente.email
        )
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
