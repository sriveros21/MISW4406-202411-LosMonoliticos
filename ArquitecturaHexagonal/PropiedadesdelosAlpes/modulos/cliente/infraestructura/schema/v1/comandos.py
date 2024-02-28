from pulsar.schema import *

from ArquitecturaHexagonal.PropiedadesdelosAlpes.seedwork.infraestructura.schema.v1.comandos import ComandoIntegracion


class ComandoCrearClientePayLoad(ComandoIntegracion):
    nombre = String()
    apellido = String()


class ComandoCrearCliente(ComandoIntegracion):
    data = ComandoCrearClientePayLoad()
