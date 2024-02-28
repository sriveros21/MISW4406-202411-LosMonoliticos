from PropiedadesdelosAlpes.seedwork.infraestructura.schema.v1.comandos import ComandoIntegracion
from pulsar.schema import *


class ComandoCrearClientePayLoad(ComandoIntegracion):
    nombre = String()
    apellido = String()


class ComandoCrearCliente(ComandoIntegracion):
    data = ComandoCrearClientePayLoad()
