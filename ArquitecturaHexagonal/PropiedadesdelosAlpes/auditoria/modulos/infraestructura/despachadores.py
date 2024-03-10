import pulsar
from pulsar.schema import *

from PropiedadesdelosAlpes.auditoria.modulos.infraestructura.schema.v1.eventos import EventoAuditoriaCreada, AuditoriaCreadaPayload
from PropiedadesdelosAlpes.auditoria.modulos.infraestructura.schema.v1.comandos import ComandoCrearAuditoria, ComandoCrearAuditoriaPayload
from PropiedadesdelosAlpes.auditoria.seedwork.infraestructura import utils
from PropiedadesdelosAlpes.auditoria.modulos.infraestructura.mapeadores import MapadeadorEventosAuditoria
import datetime

class Despachador:
    def __init__(self):
        self.mapper = MapadeadorEventosAuditoria()

    def _publicar_mensaje(self, mensaje, topico, schema):
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        publicador = cliente.create_producer(topico, schema=AvroSchema(EventoAuditoriaCreada))
        publicador.send(mensaje)
        cliente.close()
    
    def publicar_evento(self, evento, topico):
        evento = self.mapper.entidad_a_dto(evento)
        self._publicar_mensaje(evento, topico, AvroSchema(evento.__class__))

    def publicar_comando(self, comando, topico):
        # TODO Debe existir un forma de crear el Payload en Avro con base al tipo del comando
        payload = ComandoCrearAuditoriaPayload(
            id_auditoria=str(comando.id_auditoria)
        )
        comando_integracion = ComandoCrearAuditoria(data=payload)
        self._publicar_mensaje(comando_integracion, topico, AvroSchema(ComandoCrearAuditoria))

