import pulsar
from PropiedadesdelosAlpes.cliente.modulos.infraestructura.mapeadores import MapadeadorEventosCliente
from PropiedadesdelosAlpes.cliente.modulos.infraestructura.schema.v1.comandos import ComandoCrearCliente, ComandoCrearClientePayload
from PropiedadesdelosAlpes.cliente.modulos.infraestructura.schema.v1.eventos import EventoClienteCreado
from PropiedadesdelosAlpes.cliente.seedwork.infraestructura import utils
from pulsar.schema import *


class Despachador:

    def __init__(self):
        self.mapper = MapadeadorEventosCliente()

    def _publicar_mensaje(self, mensaje, topico, schema):
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        publicador = cliente.create_producer(topico, schema=AvroSchema(EventoClienteCreado))
        publicador.send(mensaje)
        cliente.close()

    def publicar_evento(self, evento, topico):
        evento = self.mapper.entidad_a_dto(evento)
        self._publicar_mensaje(evento, topico, AvroSchema(evento.__class__))

    def publicar_comando(self, comando, topico):
        payload = ComandoCrearClientePayload(
            id_auditoria=str(comando.id_auditoria)
        )
        comando_integracion = ComandoCrearCliente(data=payload)
        self._publicar_mensaje(comando_integracion, topico, AvroSchema(ComandoCrearCliente))
