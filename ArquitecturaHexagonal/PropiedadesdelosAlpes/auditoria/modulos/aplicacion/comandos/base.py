from PropiedadesdelosAlpes.auditoria.seedwork.aplicacion.comandos import ComandoHandler
from PropiedadesdelosAlpes.auditoria.modulos.infraestructura.fabricas import FabricaRepositorioAuditorias
from PropiedadesdelosAlpes.auditoria.modulos.dominio.fabricas import FabricaAuditorias

class CrearAuditoriaBaseHandler(ComandoHandler):
    def __init__(self):
        self._fabrica_repositorio: FabricaRepositorioAuditorias = FabricaRepositorioAuditorias()
        self._fabrica_auditorias: FabricaAuditorias = FabricaAuditorias()

    @property
    def fabrica_repositorio(self):
        return self._fabrica_repositorio
    
    @property
    def fabrica_auditorias(self):
        return self._fabrica_auditorias   
    