from PropiedadesdelosAlpes.auditoria.seedwork.aplicacion.queries import QueryHandler
from PropiedadesdelosAlpes.auditoria.modulos.infraestructura.fabricas import FabricaVista
from PropiedadesdelosAlpes.auditoria.modulos.dominio.fabricas import FabricaAuditorias

class AuditoriaQueryBaseHandler(QueryHandler):
    def __init__(self):
        self._fabrica_vista: FabricaVista = FabricaVista()
        self._fabrica_auditorias: FabricaAuditorias = FabricaAuditorias()

    @property
    def fabrica_vista(self):
        return self._fabrica_vista
    
    @property
    def fabrica_auditorias(self):
        return self._fabrica_auditorias