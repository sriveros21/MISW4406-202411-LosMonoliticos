""" Reglas de Negocio dominio auditoria

Este archivo contiene las reglas de negocio del dominio auditoria

"""

from typing import Any
from ....seedwork.dominio.reglas import ReglaNegocio
from .objetos_valor import HallazgosAuditoria, CodigoAuditoria

#Revisar estas reglas

class DebeReportarHallazgos(ReglaNegocio):
    
    hallazgos_auditoria:HallazgosAuditoria

    def __init__(self, hallazgos_auditoria, mensaje='La auditoria debe contener hallazgos'):
        super().__init__(mensaje)
        self.hallazgos_auditoria =hallazgos_auditoria

    def es_valido(self) -> bool:
        if len(self.hallazgos_auditoria)>0:
            return True
        else:
            return False

class DebeIncluirCodigoAuditoria(ReglaNegocio):

    codigo_auditoria: CodigoAuditoria

    def __init__(self, codigo_auditoria, mensaje = 'La auditoria debe contener un código'):
        super().__init__(mensaje)
        self.codigo_auditoria=codigo_auditoria
    
    def es_valido(self) -> bool:
        if len(self.codigo_auditoria)>0:
            return True
        else:
            return False
 
