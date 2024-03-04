from PropiedadesdelosAlpes.modulos.cliente.dominio.eventos import ClienteCreado
from pydispatch import dispatcher

from .handlers import HandlerClienteIntegracion

dispatcher.connect(HandlerClienteIntegracion.handle_cliente_creada, signal=f'{ClienteCreado.__name__}Integracion')
