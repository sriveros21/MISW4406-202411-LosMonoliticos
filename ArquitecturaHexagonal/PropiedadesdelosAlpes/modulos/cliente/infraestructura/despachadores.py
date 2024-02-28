import pulsar
from PropiedadesdelosAlpes.modulos.cliente.infraestructura.schema.v1.comandos import ComandoCrearCliente, ComandoCrearClientePayLoad
from PropiedadesdelosAlpes.modulos.cliente.infraestructura.schema.v1.eventos import ClienteCreado, ClienteCreadoPayLoad
from PropiedadesdelosAlpes.seedwork.infraestructura import utils
from pulsar.schema import *


class Despachador:
    def _publicar_mensaje(self, mensaje, topico, schema):
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        publicador = cliente.create_producer(topico, schema=AvroSchema(schema))
        publicador.send(mensaje)
        cliente.close()

    def publicar_evento(self, evento, topico):
        payload = ClienteCreadoPayLoad(
            id_cliente=str(evento.cliente_id),
            nombre=evento.nombre,
            apellido=evento.apellido
        )
        evento_integracion = ClienteCreado(data=payload)
        self._publicar_mensaje(evento_integracion, topico, ClienteCreado)

    def publicar_comando(self, comando, topico):
        payload = ComandoCrearClientePayLoad(
            id_usuario=str(comando.id_usuario)
        )
        comando_integracion = ComandoCrearCliente(data=payload)
        self._publicar_mensaje(comando_integracion, topico, ComandoCrearCliente)
