from PropiedadesdelosAlpes.cliente.modulos.dominio.entidades import Cliente
from PropiedadesdelosAlpes.cliente.modulos.dominio.eventos.cliente import ClienteCreado, FaseClienteCambiado, EventoCliente
from PropiedadesdelosAlpes.cliente.modulos.dominio.objetos_valor import Nombre, Apellido, Email
from PropiedadesdelosAlpes.cliente.seedwork.dominio.repositorios import Mapeador

from .dto import Cliente as ClienteDTO
from .excepciones import NoExisteImplementacionParaTipoFabricaExcepcion


class MapadeadorEventosCliente(Mapeador):
    # Versiones aceptadas
    versions = ('v1',)
    LATEST_VERSION = versions[0]

    def __init__(self):
        self.router = {
            ClienteCreado: self._entidad_a_cliente_creado,
            FaseClienteCambiado: self._entidad_a_cliente_cambiado,
        }

    def obtener_tipo(self) -> type:
        return EventoCliente.__class__

    def es_version_valida(self, version):
        for v in self.versions:
            if v == version:
                return True
        return False

    def _entidad_a_cliente_creado(self, entidad: ClienteCreado, version=LATEST_VERSION):
        def v1(evento):
            from .schema.v1.eventos import ClienteCreadoPayload, EventoClienteCreado

            payload = ClienteCreadoPayload(
                id=str(evento.id),
                id_cliente=str(evento.id_cliente),
                nombre=str(evento.nombre),
                apellido=str(evento.apellido),
                email=str(evento.email)
            )
            evento_integracion = EventoClienteCreado(id=str(evento.id))
            evento_integracion.id = str(evento.id)
            evento_integracion.nombre = str(evento.nombre)
            evento_integracion.apellido = str(evento.apellido)
            evento_integracion.email = str(evento.email)
            evento_integracion.service_name = 'PropiedadesdelosAlpes'
            evento_integracion.data = payload

            return evento_integracion

        if not self.es_version_valida(version):
            raise Exception(f'No se sabe procesar la version {version}')

        if version == 'v1':
            return v1(entidad)

    def _entidad_a_cliente_cambiado(self, entidad: FaseClienteCambiado, version=LATEST_VERSION):
        # TODO
        raise NotImplementedError

    def entidad_a_dto(self, entidad: EventoCliente, version=LATEST_VERSION) -> ClienteDTO:
        if not entidad:
            raise NoExisteImplementacionParaTipoFabricaExcepcion
        func = self.router.get(entidad.__class__, None)

        if not func:
            raise NoExisteImplementacionParaTipoFabricaExcepcion

        return func(entidad, version=version)

    def dto_a_entidad(self, dto: ClienteDTO, version=LATEST_VERSION) -> Cliente:
        raise NotImplementedError


class MapeadorCliente(Mapeador):

    def obtener_tipo(self) -> type:
        return Cliente.__class__

    def entidad_a_dto(self, entidad: Cliente) -> ClienteDTO:
        cliente_dto = ClienteDTO()
        cliente_dto.id = ''.join(map(str, entidad.id))
        cliente_dto.id_cliente = ''.join(map(str, entidad.id_cliente))
        cliente_dto.nombre = entidad.nombre
        cliente_dto.apellido = entidad.apellido
        cliente_dto.email = entidad.email

        return cliente_dto

    def dto_a_entidad(self, dto: ClienteDTO) -> Cliente:
        id = dto.id
        id_cliente = dto.id_cliente
        nombre = Nombre(nombre=dto.nombre)
        apellido = Apellido(apellido=dto.apellido)
        email = Email(email=dto.email)

        return Cliente(
            id=id,
            id_cliente=id_cliente,
            nombre=nombre,
            apellido=apellido,
            email=email
        )
