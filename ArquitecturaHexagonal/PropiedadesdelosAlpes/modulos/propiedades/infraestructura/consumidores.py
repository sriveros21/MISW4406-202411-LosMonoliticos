import pulsar
from pulsar.schema import *
import logging
import traceback

from ArquitecturaHexagonal.PropiedadesdelosAlpes.modulos.propiedades.infraestructura.schema.v1.eventos import PropiedadCreada
from ArquitecturaHexagonal.PropiedadesdelosAlpes.modulos.propiedades.infraestructura.schema.v1.comandos import ComandoCrearPropiedad
from ArquitecturaHexagonal.PropiedadesdelosAlpes.seedwork.infraestructura import utils

def suscribirse_a_eventos():
    cliente = None
    try:
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        consumidor = cliente.subscribe('eventos-propiedad', consumer_type=pulsar.ConsumerType.Shared,subscription_name='your_project-sub-eventos', schema=AvroSchema(PropiedadCreada))

        while True:
            mensaje = consumidor.receive()
            print(f'Evento recibido: {mensaje.value().data}')

            consumidor.acknowledge(mensaje)     

        cliente.close()
    except Exception as e:
        logging.error('ERROR: Suscribiendose al tópico de eventos de propiedad!')
        traceback.print_exc()
        if cliente:
            cliente.close()

def suscribirse_a_comandos():
    cliente = None
    try:
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        consumidor = cliente.subscribe('comandos-propiedad', consumer_type=pulsar.ConsumerType.Shared, subscription_name='your_project-sub-comandos', schema=AvroSchema(ComandoCrearPropiedad))

        while True:
            mensaje = consumidor.receive()
            print(f'Comando recibido: {mensaje.value().data}')

            consumidor.acknowledge(mensaje)     
            
        cliente.close()
    except Exception as e:
        logging.error('ERROR: Suscribiendose al tópico de comandos de propiedad!')
        traceback.print_exc()
        if cliente:
            cliente.close()
