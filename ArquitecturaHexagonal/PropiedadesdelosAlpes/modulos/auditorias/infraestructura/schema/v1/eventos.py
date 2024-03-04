from pulsar.schema import *
from PropiedadesdelosAlpes.seedwork.infraestructura.schema.v1.eventos import EventoIntegracion

class AuditoriaCreadaPayload(Record):
    id_auditoria = String()
    fecha_creacion = Long()

class EventoAuditoriaCreada(EventoIntegracion):
    data = AuditoriaCreadaPayload()