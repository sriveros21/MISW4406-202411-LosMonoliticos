from pulsar.schema import *
from ArquitecturaHexagonal.PropiedadesdelosAlpes.seedwork.infraestructura.schema.v1.eventos import EventoIntegracion

class PropiedadCreadaPayload(Record):
    id_propiedad = String()
    nombre = String()
    ubicacion = String()
    dimensiones = String()
    tipo = String()
    estado = String()

class PropiedadCreada(EventoIntegracion):
    data = PropiedadCreadaPayload()
