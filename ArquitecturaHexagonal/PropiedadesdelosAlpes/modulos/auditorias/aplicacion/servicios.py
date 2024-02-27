from PropiedadesdelosAlpes.seedwork.aplicacion.servicios import Servicio
from PropiedadesdelosAlpes.modulos.auditorias.dominio.entidades import Auditoria
from PropiedadesdelosAlpes.modulos.auditorias.dominio.fabricas import FabricaAuditorias
from PropiedadesdelosAlpes.modulos.auditorias.infraestructura.fabricas import FabricaRepositorio
from PropiedadesdelosAlpes.modulos.auditorias.infraestructura.repositorios import RepositorioAuditorias
from .mapeadores import MapeadorAuditoria

from .dto import AuditoriaDTO

class ServicioAuditoria(Servicio):

    def __init__(self):
        self._fabrica_repositorio: FabricaRepositorio = FabricaRepositorio()
        self._fabrica_auditorias: FabricaAuditorias = FabricaAuditorias()

    @property
    def fabrica_repositorio(self):
        return self._fabrica_repositorio
    
    @property
    def fabrica_auditorias(self):
        return self._fabrica_auditorias

    def crear_auditoria(self, auditoria_dto: AuditoriaDTO) -> AuditoriaDTO:
        auditoria: Auditoria = self.fabrica_auditorias.crear_objeto(auditoria_dto, MapeadorAuditoria())

        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioAuditorias.__class__)
        repositorio.agregar(auditoria)

        return self.fabrica_auditorias.crear_objeto(auditoria, MapeadorAuditoria())

    def obtener_auditoria_por_id(self, id) -> AuditoriaDTO:
        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioAuditorias.__class__)
        return repositorio.obtener_por_id(id).__dict__
