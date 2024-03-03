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
    data = PropiedadCreadaPayload()
