from uuid import UUID

from PropiedadesdelosAlpes.cliente.modulos.dominio.entidades import Cliente
from PropiedadesdelosAlpes.cliente.modulos.dominio.fabricas import FabricaCliente
from PropiedadesdelosAlpes.cliente.modulos.dominio.repositorios import RepositorioCliente, RepositorioEventosCliente
from PropiedadesdelosAlpes.cliente.modulos.infraestructura.dto import EventosCliente
from PropiedadesdelosAlpes.config.db import db
from pulsar.schema import *

from .dto import Cliente as ClienteDTO
from .mapeadores import MapeadorCliente, MapadeadorEventosCliente


class RepositorioClienteSQLAlchemy(RepositorioCliente):
    def __init__(self):
        self._fabrica_cliente: FabricaCliente = FabricaCliente()

    @property
    def fabrica_cliente(self):
        return self._fabrica_cliente

    def obtener_por_id(self, id_cliente: UUID) -> Cliente:
        cliente_dto = db.session.query(ClienteDTO).filter_by(id_cliente=str(id_cliente)).one()
        return self.fabrica_cliente.crear_objeto(cliente_dto, MapeadorCliente())

    def obtener_todos(self) -> list[Cliente]:
        # TODO
        raise NotImplementedError

    def agregar(self, cliente: Cliente):
        cliente_dto = self.fabrica_cliente.crear_objeto(cliente, MapeadorCliente())
        db.session.add(cliente_dto)

    def actualizar(self, cliente: Cliente):
        # TODO
        raise NotImplementedError

    def eliminar(self, cliente_id: UUID):
        # TODO
        raise NotImplementedError


class RepositorioEventosClienteSQLAlchemy(RepositorioEventosCliente):

    def __init__(self):
        self._fabrica_cliente: FabricaCliente = FabricaCliente()

    @property
    def fabrica_cliente(self):
        return self._fabrica_cliente

    def obtener_por_id(self, id: UUID) -> Cliente:
        cliente_dto = db.session.query(ClienteDTO).filter_by(id=str(id)).one()
        return self.fabrica_cliente.crear_objeto(cliente_dto, MapadeadorEventosCliente())

    def obtener_todos(self) -> 'list[Cliente]':
        raise NotImplementedError

    def agregar(self, evento):
        cliente_evento = self.fabrica_cliente.crear_objeto(evento, MapadeadorEventosCliente())

        parser_payload = JsonSchema(cliente_evento.data.__class__)
        json_str = parser_payload.encode(cliente_evento.data)

        evento_dto = EventosCliente()
        evento_dto.id = str(evento.id)
        evento_dto.id_entidad = str(evento.id)
        evento_dto.fecha_evento = evento.fecha_creacion
        evento_dto.version = str(cliente_evento.specversion)
        evento_dto.tipo_evento = evento.__class__.__name__
        evento_dto.formato_contenido = 'JSON'
        evento_dto.nombre_servicio = str(cliente_evento.service_name)
        evento_dto.contenido = json_str

        db.session.add(evento_dto)

    def actualizar(self, cliente: Cliente):
        raise NotImplementedError

    def eliminar(self, cliente_id: UUID):
        raise NotImplementedError
