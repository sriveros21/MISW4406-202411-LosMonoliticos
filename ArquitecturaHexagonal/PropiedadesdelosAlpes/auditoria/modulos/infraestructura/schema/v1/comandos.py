from pulsar.schema import *
from dataclasses import dataclass, field
from PropiedadesdelosAlpes.auditoria.seedwork.infraestructura.schema.v1.comandos import (ComandoIntegracion)

class ComandoCrearAuditoriaPayload(ComandoIntegracion):
    id_auditoria = String()
    # TODO Crear los records

class ComandoCrearAuditoria(ComandoIntegracion):
    data = ComandoCrearAuditoriaPayload()