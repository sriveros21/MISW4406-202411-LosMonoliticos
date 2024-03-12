from PropiedadesdelosAlpes.cliente.modulos.dominio.eventos.cliente import ClienteCreado
from pydispatch import dispatcher

from .handlers import HandlerClienteIntegracion

dispatcher.connect(HandlerClienteIntegracion.handle_cliente_creado, signal=f'{ClienteCreado.__name__}Integracion')
