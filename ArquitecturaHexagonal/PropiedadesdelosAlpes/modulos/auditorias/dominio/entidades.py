"""Entidades del dominio auditorias

En este archivo se encontraran las entidades del dominio auditoria

"""

from __future__ import annotations
from dataclasses import dataclass, field

import PropiedadesdelosAlpes.modulos.auditorias.dominio.objetos_valor as ov
from PropiedadesdelosAlpes.seedwork.dominio.entidades import AgregacionRaiz, Entidad

#Revisar si esta lleva Id
@dataclass
class Auditoria(AgregacionRaiz):
    codigo:ov.CodigoAuditoria = field(default_factory=ov.CodigoAuditoria)
    fecha:ov.FechaAuditoria = field(default_factory=ov.FechaAuditoria)
    auditor:ov.NombreAuditor = field(default_factory=ov.NombreAuditor)
    fase:ov.FaseAuditoria = field(default_factory=ov.FaseAuditoria)
    hallazgos:ov.HallazgosAuditoria = field(default_factory=ov.HallazgosAuditoria)
    objetivo: ov.ObjetivoAuditoria = field(default_factory=ov.ObjetivoAuditoria)