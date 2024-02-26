from pulsar.schema import *
from ArquitecturaHexagonal.PropiedadesdelosAlpes.seedwork.infraestructura.schema.v1.comandos import ComandoIntegracion

class ComandoCrearPropiedadPayload(ComandoIntegracion):
    nombre = String()
    ubicacion = String() 
    dimensiones = String() 
    tipo = String()
    estado = String()
    

class ComandoCrearPropiedad(ComandoIntegracion):
    data = ComandoCrearPropiedadPayload()
