import uuid
from pulsar.schema import *
from PropiedadesdelosAlpes.auditoria.seedwork.infraestructura.schema.v1.eventos import EventoIntegracion
from PropiedadesdelosAlpes.auditoria.seedwork.infraestructura.utils import time_millis

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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)