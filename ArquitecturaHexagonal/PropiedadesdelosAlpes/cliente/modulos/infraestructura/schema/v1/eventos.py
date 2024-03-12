import uuid

from PropiedadesdelosAlpes.cliente.seedwork.infraestructura.schema.v1.eventos import EventoIntegracion
from PropiedadesdelosAlpes.cliente.seedwork.infraestructura.utils import time_millis
from pulsar.schema import *


class ClienteCreadoPayLoad(Record):
    id_cliente = String()
    nombre = String()
    apellido = String()
    email = String()


class EventoClienteCreado(EventoIntegracion):
    id = String(default=str(uuid.uuid4()))
    time = Long()
    ingestion = Long(default=time_millis())
    specversion = String()
    type = String()
    datacontenttype = String()
    service_name = String()
    data = ClienteCreadoPayLoad()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
