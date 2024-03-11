import pulsar,_pulsar  
from pulsar.schema import *
import uuid
import time
import logging
import traceback
from PropiedadesdelosAlpes.auditoria.modulos.infraestructura.proyecciones import ProyeccionAuditoriasLista, ProyeccionAuditoriasTotales
from PropiedadesdelosAlpes.auditoria.seedwork.infraestructura.proyecciones import ejecutar_proyeccion
from PropiedadesdelosAlpes.auditoria.modulos.infraestructura.schema.v1.eventos import EventoAuditoriaCreada
from PropiedadesdelosAlpes.auditoria.modulos.infraestructura.schema.v1.comandos import ComandoCrearAuditoria
from PropiedadesdelosAlpes.auditoria.seedwork.infraestructura import utils

def suscribirse_a_eventos(app=None):
    cliente = None
    try:
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        consumidor = cliente.subscribe('eventos-auditoria', consumer_type=_pulsar.ConsumerType.Shared,subscription_name='PropiedadesdelosAlpes-sub-eventos', schema=AvroSchema(EventoAuditoriaCreada))

        while True:
            mensaje = consumidor.receive()
            datos = mensaje.value().data
            print(f'Evento recibido: {datos}')
            print(f'Evento recibido: {datos.fecha}')
           # print(f'Evento recibido: {mensaje.value().data}')

            ejecutar_proyeccion(ProyeccionAuditoriasTotales(datos.fecha, ProyeccionAuditoriasTotales.ADD), app=app)
            ejecutar_proyeccion(ProyeccionAuditoriasLista(
                datos.id,
                datos.id_auditoria,
                datos.fecha,
                datos.codigo,
                datos.auditor,
                datos.fase,
                datos.hallazgos,
                datos.objetivo,
                ), app=app)
            
            consumidor.acknowledge(mensaje)          

        cliente.close()
    except:
        logging.error('ERROR: Suscribiendose al tópico de eventos!')
        traceback.print_exc()
        if cliente:
            cliente.close()

def suscribirse_a_comandos(app=None):
    cliente = None
    try:
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        consumidor = cliente.subscribe('comandos-auditoria', consumer_type=_pulsar.ConsumerType.Shared, subscription_name='PropiedadesdelosAlpes-sub-comandos', schema=AvroSchema(ComandoCrearAuditoria))

        while True:
            mensaje = consumidor.receive()
            print(f'Comando recibido: {mensaje.value().data}')

            consumidor.acknowledge(mensaje)     
            
        cliente.close()
    except:
        logging.error('ERROR: Suscribiendose al tópico de comandos!')
        traceback.print_exc()
        if cliente:
            cliente.close()