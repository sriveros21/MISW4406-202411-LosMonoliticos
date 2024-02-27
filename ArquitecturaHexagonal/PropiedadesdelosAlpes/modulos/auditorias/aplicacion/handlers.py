from PropiedadesdelosAlpes.modulos.auditorias.dominio.eventos import AuditoriaCreada
from PropiedadesdelosAlpes.seedwork.aplicacion.handlers import Handler

class HandlerAuditoriaDominio(Handler):

    @staticmethod
    def handle_auditoria_creada(evento):
        print('================ AUDITORIA CREADA ===========')
        
