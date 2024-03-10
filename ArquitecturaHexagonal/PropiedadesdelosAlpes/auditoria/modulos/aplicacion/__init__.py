from pydispatch import dispatcher
from .handlers import HandlerAuditoriaIntegracion

from PropiedadesdelosAlpes.auditoria.modulos.dominio.eventos.auditorias import AuditoriaCreada, FaseAuditoriaCambiada

dispatcher.connect(HandlerAuditoriaIntegracion.handle_auditoria_creada, signal=f'{AuditoriaCreada.__name__}Integracion')