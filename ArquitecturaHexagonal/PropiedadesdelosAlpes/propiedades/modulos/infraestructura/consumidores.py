import pulsar,_pulsar
from pulsar.schema import *
import logging
import traceback
from PropiedadesdelosAlpes.propiedades.modulos.infraestructura.proyecciones import ProyeccionPropiedadesLista, ProyeccionPropiedadesTotales
from PropiedadesdelosAlpes.propiedades.seedwork.infraestructura.proyecciones import ejecutar_proyeccion
from PropiedadesdelosAlpes.modulos.propiedades.infraestructura.schema.v1.eventos import PropiedadCreada
from PropiedadesdelosAlpes.modulos.propiedades.infraestructura.schema.v1.comandos import ComandoCrearPropiedad
from PropiedadesdelosAlpes.seedwork.infraestructura import utils

def suscribirse_a_eventos():
    cliente = None
    try:
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        consumidor = cliente.subscribe('eventos-propiedad', consumer_type=_pulsar.ConsumerType.Shared,subscription_name='propiedadeslosalapes-sub-eventos', schema=AvroSchema(PropiedadCreada))

        while True:
            mensaje = consumidor.receive()
            print(f'Evento recibido: {mensaje.value().data}')

            ejecutar_proyeccion(ProyeccionPropiedadesTotales(datos.fecha, ProyeccionPropiedadesTotales.ADD), app=app)
            ejecutar_proyeccion(ProyeccionPropiedadesLista(
                datos.id,
                datos.fecha,
                datos.nombre,
                datos.ubicacion,
                datos.dimension,
                datos.tipo,
                datos.estado,
                ), app=app)
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
        consumidor = cliente.subscribe('comandos-propiedad', consumer_type=_pulsar.ConsumerType.Shared, subscription_name='propiedadeslosalpes-sub-comandos', schema=AvroSchema(ComandoCrearPropiedad))

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
