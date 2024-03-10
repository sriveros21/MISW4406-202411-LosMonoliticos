from PropiedadesdelosAlpes.modulos.cliente.infraestructura.despachadores import Despachador
from PropiedadesdelosAlpes.seedwork.aplicacion.handlers import Handler


class HandlerClienteIntegracion(Handler):

    @staticmethod
    def handle_cliente_creada(evento):
        despachador = Despachador()
        despachador.publicar_evento(evento, 'eventos-cliente')

    @staticmethod
    def handle_cliente_consultada(evento):
        despachador = Despachador()
        despachador.publicar_evento(evento, 'eventos-cliente')

    @staticmethod
    def handle_cliente_actualizada(evento):
        despachador = Despachador()
        despachador.publicar_evento(evento, 'eventos-cliente')

    @staticmethod
    def handle_cliente_eliminada(evento):
        despachador = Despachador()
        despachador.publicar_evento(evento, 'eventos-cliente')
