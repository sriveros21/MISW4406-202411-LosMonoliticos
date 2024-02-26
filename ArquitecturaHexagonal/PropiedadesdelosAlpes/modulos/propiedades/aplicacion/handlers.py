from PropiedadesdelosAlpes.modulos.propiedades.dominio.eventos import PropiedadCreada, PropiedadActualizada, PropiedadEliminada
from PropiedadesdelosAlpes.seedwork.aplicacion.handlers import Handler
from PropiedadesdelosAlpes.modulos.propiedades.infraestructura.despachadores import Despachador

class HandlerPropiedadIntegracion(Handler):

    @staticmethod
    def handle_propiedad_creada(evento):
        despachador = Despachador()
        despachador.publicar_evento(evento, 'eventos-propiedad')

    @staticmethod
    def handle_propiedad_actualizada(evento):
        despachador = Despachador()
        despachador.publicar_evento(evento, 'eventos-propiedad')

    @staticmethod
    def handle_propiedad_eliminada(evento):
        despachador = Despachador()
        despachador.publicar_evento(evento, 'eventos-propiedad')