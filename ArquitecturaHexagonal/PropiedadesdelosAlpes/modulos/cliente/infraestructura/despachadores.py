import pulsar
from PropiedadesdelosAlpes.modulos.cliente.infraestructura.schema.v1.comandos import ComandoCrearCliente, ComandoCrearClientePayLoad
from PropiedadesdelosAlpes.modulos.cliente.infraestructura.schema.v1.eventos import EventoClienteCreado, ClienteCreadoPayLoad
from PropiedadesdelosAlpes.seedwork.infraestructura import utils
from pulsar.schema import *


class Despachador:
    def _publicar_mensaje(self, mensaje, topico, schema):
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        publicador = cliente.create_producer(topico, schema=AvroSchema(EventoClienteCreado))
        publicador.send(mensaje)
        cliente.close()

    def publicar_evento(self, evento, topico):
        payload = ClienteCreadoPayLoad(
            id_cliente=str(evento.id_cliente),
            nombre=evento.nombre,
            apellido=evento.apellido,
            email=evento.email
        )
        evento_integracion = EventoClienteCreado(data=payload)
        self._publicar_mensaje(evento_integracion, topico, AvroSchema(EventoClienteCreado))

    def publicar_comando(self, comando, topico):
        payload = ComandoCrearClientePayLoad(
            id_usuario=str(comando.id_usuario)
        )
        comando_integracion = ComandoCrearCliente(data=payload)
        self._publicar_mensaje(comando_integracion, topico, AvroSchema(ComandoCrearCliente))
