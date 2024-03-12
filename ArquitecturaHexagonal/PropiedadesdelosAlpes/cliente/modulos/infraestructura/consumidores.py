import logging
import traceback

import pulsar
from PropiedadesdelosAlpes.cliente.modulos.infraestructura.proyecciones import ProyeccionClienteLista, ProyeccionClienteTotales
from PropiedadesdelosAlpes.cliente.modulos.infraestructura.schema.v1.comandos import ComandoCrearCliente
from PropiedadesdelosAlpes.cliente.modulos.infraestructura.schema.v1.eventos import EventoClienteCreado
from PropiedadesdelosAlpes.cliente.seedwork.infraestructura import utils
from PropiedadesdelosAlpes.cliente.seedwork.infraestructura.proyecciones import ejecutar_proyeccion
from pulsar.schema import *


def suscribirse_a_eventos(app=None):
    cliente = None
    try:
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        consumidor = cliente.subscribe('eventos-cliente', consumer_type=pulsar.ConsumerType.Shared, subscription_name='PropiedadesdelosAlpes-sub-eventos', schema=AvroSchema(EventoClienteCreado))

        while True:
            mensaje = consumidor.receive()
            datos = mensaje.value().data
            print(f'Evento recibido: {datos}')
            print(f'Evento recibido: {datos.fecha}')

            ejecutar_proyeccion(ProyeccionClienteTotales(datos.fecha, ProyeccionClienteTotales.ADD), app=app)
            ejecutar_proyeccion(ProyeccionClienteLista(
                datos.id,
                datos.id_cliente,
                datos.nombre,
                datos.apellido,
                datos.email,
            ), app=app)

            consumidor.acknowledge(mensaje)

        cliente.close()
    except Exception as e:
        logging.error('ERROR: Suscribiendose al tópico de eventos de cliente!')
        traceback.print_exc()
        if cliente:
            cliente.close()


def suscribirse_a_comandos(app=None):
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
