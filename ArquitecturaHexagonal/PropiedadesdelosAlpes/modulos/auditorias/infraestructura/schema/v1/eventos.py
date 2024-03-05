import uuid
from pulsar.schema import *
from PropiedadesdelosAlpes.seedwork.infraestructura.schema.v1.eventos import EventoIntegracion
from PropiedadesdelosAlpes.seedwork.infraestructura.utils import time_millis
class AuditoriaCreadaPayload(Record):
    id_auditoria = String()
    fecha_creacion = Long()

class EventoAuditoriaCreada(EventoIntegracion):
    id = String(default=str(uuid.uuid4()))
    time = Long()
    ingestion = Long(default=time_millis())
    specversion = String()
    type = String()
    datacontenttype = String()
    service_name = String()
    data = AuditoriaCreadaPayload()