from pulsar.schema import *
from PropiedadesdelosAlpes.seedwork.infraestructura.schema.v1.eventos import EventoIntegracion

class PropiedadCreadaPayload(Record):
    id = String()
    nombre = String()
    ubicacion = String()
    dimension = String()
    tipo = String()
    estado = String()

class PropiedadCreada(EventoIntegracion):
    id = String(default=str(uuid.uuid4()))
    time = Long()
    ingestion = Long(default=time_millis())
    specversion = String()
    type = String()
    datacontenttype = String()
    service_name = String()
    data = PropiedadCreadaPayload()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)