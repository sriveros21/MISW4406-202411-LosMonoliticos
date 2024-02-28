from pulsar.schema import *

from ArquitecturaHexagonal.PropiedadesdelosAlpes.seedwork.infraestructura.schema.v1.eventos import EventoIntegracion


class ClienteCreadoPayLoad(Record):
    id_cliente = String()
    nombre = String()
    apellido = String()


class ClienteCreado(EventoIntegracion):
    data = ClienteCreadoPayLoad()
