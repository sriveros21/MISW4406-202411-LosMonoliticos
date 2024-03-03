from PropiedadesdelosAlpes.seedwork.aplicacion.servicios import Servicio
from PropiedadesdelosAlpes.modulos.auditorias.dominio.entidades import Auditoria
from PropiedadesdelosAlpes.modulos.auditorias.infraestructura.repositorios import RepositorioAuditorias
from .mapeadores import MapeadorAuditoria
from uuid import UUID
from .dto import AuditoriaDTO

class ServicioAuditoria(Servicio):
    def __init__(self,repositorio: RepositorioAuditorias, mapeador: MapeadorAuditoria):
        self.repositorio= repositorio
        self.mapeador =mapeador
        
    def crear_auditoria(self, auditoria_dto: AuditoriaDTO) -> AuditoriaDTO:
        auditoria: Auditoria = self.mapeador.dto_a_entidad(auditoria_dto)
        self.repositorio.agregar(auditoria)
        return self.mapeador.entidad_a_dto(auditoria)
    
    def obtener_auditoria_por_id(self, id: UUID) -> AuditoriaDTO:
        auditoria = self.repositorio.obtener_por_id(id)
        if auditoria:
            return self.mapeador.entidad_a_dto(auditoria)
        return None
    
