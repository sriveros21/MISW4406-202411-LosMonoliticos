from pydispatch import dispatcher
from .handlers import HandlerAuditoriaIntegracion

from PropiedadesdelosAlpes.modulos.auditorias.dominio.eventos import AuditoriaCreada, FaseAuditoriaCambiada

dispatcher.connect(HandlerAuditoriaIntegracion.handle_auditoria_creada, signal=f'{AuditoriaCreada.__name__}Integracion')
dispatcher.connect(HandlerAuditoriaIntegracion.handle_auditoria_creada, signal=f'{AuditoriaCreada.__name__}Integracion')