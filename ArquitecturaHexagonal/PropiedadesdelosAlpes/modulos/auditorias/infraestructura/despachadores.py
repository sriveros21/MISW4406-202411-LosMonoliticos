import pulsar
from pulsar.schema import *

from PropiedadesdelosAlpes.modulos.auditorias.infraestructura.schema.v1.eventos import EventoAuditoriaCreada, AuditoriaCreadaPayload
from PropiedadesdelosAlpes.modulos.auditorias.infraestructura.schema.v1.comandos import ComandoCrearAuditoria, ComandoCrearAuditoriaPayload
from PropiedadesdelosAlpes.seedwork.infraestructura import utils

import datetime

epoch = datetime.datetime.utcfromtimestamp(0)

def unix_time_millis(dt):
    return (dt - epoch).total_seconds() * 1000.0

class Despachador:
    def _publicar_mensaje(self, mensaje, topico, schema):
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        publicador = cliente.create_producer(topico, schema=AvroSchema(EventoAuditoriaCreada))
        publicador.send(mensaje)
        cliente.close()

    def publicar_evento(self, evento, topico):
        # TODO Debe existir un forma de crear el Payload en Avro con base al tipo del evento
        payload = AuditoriaCreadaPayload(
            codigo=str(evento.codigo), 
            fecha_creacion=int(unix_time_millis(evento.fecha_creacion))
        )
        evento_integracion = EventoAuditoriaCreada(data=payload)
        self._publicar_mensaje(evento_integracion, topico, AvroSchema(EventoAuditoriaCreada))

    def publicar_comando(self, comando, topico):
        # TODO Debe existir un forma de crear el Payload en Avro con base al tipo del comando
        payload = ComandoCrearAuditoriaPayload(
            id_auditoria=str(comando.id_auditoria)
        )
        comando_integracion = ComandoCrearAuditoria(data=payload)
        self._publicar_mensaje(comando_integracion, topico, AvroSchema(ComandoCrearAuditoria))
