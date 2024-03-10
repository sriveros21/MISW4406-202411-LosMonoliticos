import logging
import traceback

import pulsar
from PropiedadesdelosAlpes.modulos.cliente.infraestructura.schema.v1.comandos import ComandoCrearCliente
from PropiedadesdelosAlpes.modulos.cliente.infraestructura.schema.v1.eventos import EventoClienteCreado
from PropiedadesdelosAlpes.seedwork.infraestructura import utils
from pulsar.schema import *


def suscribirse_a_eventos():
    cliente = None
    try:
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        consumidor = cliente.subscribe('eventos-cliente', consumer_type=pulsar.ConsumerType.Shared, subscription_name='PropiedadesdelosAlpes-sub-eventos', schema=AvroSchema(EventoClienteCreado))

        while True:
            mensaje = consumidor.receive()
            print(f'Evento recibido: {mensaje.value().data}')

            consumidor.acknowledge(mensaje)

        cliente.close()
    except Exception as e:
        logging.error('ERROR: Suscribiendose al tópico de eventos de cliente!')
        traceback.print_exc()
        if cliente:
            cliente.close()


def suscribirse_a_comandos():
    cliente = None
    try:
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        consumidor = cliente.subscribe('comandos-cliente', consumer_type=pulsar.ConsumerType.Shared, subscription_name='PropiedadesdelosAlpes-sub-comandos', schema=AvroSchema(ComandoCrearCliente))

        while True:
            mensaje = consumidor.receive()
            print(f'Comando recibido: {mensaje.value().data}')

            consumidor.acknowledge(mensaje)

        cliente.close()
    except Exception as e:
        logging.error('ERROR: Suscribiendose al tópico de comandos de cliente!')
        traceback.print_exc()
        if cliente:
            cliente.close()
