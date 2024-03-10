from PropiedadesdelosAlpes.seedwork.infraestructura.schema.v1.eventos import EventoIntegracion
from pulsar.schema import *


class ClienteCreadoPayLoad(Record):
    id_cliente = String()
    nombre = String()
    apellido = String()
    email = String()


class ClienteCreado(EventoIntegracion):
    data = ClienteCreadoPayLoad()
