from PropiedadesdelosAlpes.auditoria.modulos.dominio.eventos import AuditoriaCreada
from PropiedadesdelosAlpes.auditoria.seedwork.aplicacion.handlers import Handler
from PropiedadesdelosAlpes.auditoria.modulos.auditorias.infraestructura.despachadores import Despachador

class HandlerAuditoriaIntegracion(Handler):

    @staticmethod
    def handle_auditoria_creada(evento):
        despachador = Despachador()
        despachador.publicar_evento(evento, 'eventos-auditoria')
