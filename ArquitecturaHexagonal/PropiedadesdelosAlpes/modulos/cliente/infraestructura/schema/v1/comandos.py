from PropiedadesdelosAlpes.seedwork.infraestructura.schema.v1.comandos import ComandoIntegracion
from pulsar.schema import *


class ComandoCrearClientePayLoad(ComandoIntegracion):
    id_cliente = String()
    nombre = String()
    apellido = String()
    email = String()


class ComandoCrearCliente(ComandoIntegracion):
    data = ComandoCrearClientePayLoad()
