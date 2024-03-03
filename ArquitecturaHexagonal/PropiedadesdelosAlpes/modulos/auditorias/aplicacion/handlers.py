from PropiedadesdelosAlpes.modulos.auditorias.dominio.eventos import AuditoriaCreada
from PropiedadesdelosAlpes.seedwork.aplicacion.handlers import Handler
from PropiedadesdelosAlpes.modulos.auditorias.infraestructura.despachadores import Despachador

class HandlerAuditoriaIntegracion(Handler):

    @staticmethod
    def handle_auditoria_creada(evento):
        despachador = Despachador()
        despachador.publicar_evento(evento, 'eventos-auditoria')
