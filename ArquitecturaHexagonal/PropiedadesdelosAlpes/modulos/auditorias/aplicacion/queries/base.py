from PropiedadesdelosAlpes.seedwork.aplicacion.queries import QueryHandler
from PropiedadesdelosAlpes.modulos.auditorias.infraestructura.fabricas import FabricaRepositorio
from PropiedadesdelosAlpes.modulos.auditorias.dominio.fabricas import FabricaAuditorias

class AuditoriaQueryBaseHandler(QueryHandler):
    def __init__(self):
        self._fabrica_repositorio: FabricaRepositorio = FabricaRepositorio()
        self._fabrica_auditorias: FabricaAuditorias = FabricaAuditorias()

    @property
    def fabrica_repositorio(self):
        return self._fabrica_repositorio
    
    @property
    def fabrica_auditorias(self):
        return self._fabrica_auditorias