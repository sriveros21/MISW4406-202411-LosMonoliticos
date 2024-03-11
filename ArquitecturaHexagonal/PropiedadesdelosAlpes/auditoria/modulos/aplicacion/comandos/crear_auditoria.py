from PropiedadesdelosAlpes.auditoria.seedwork.aplicacion.comandos import Comando
from PropiedadesdelosAlpes.auditoria.modulos.aplicacion.dto import AuditoriaDTO,FechaAuditoriaDTO,CodigoAuditoriaDTO,NombreAuditorDTO,HallazgosAuditoriaDTO, FaseAuditoria, ObjetivoAuditoria
from .base import CrearAuditoriaBaseHandler
from dataclasses import dataclass, field
from PropiedadesdelosAlpes.auditoria.seedwork.aplicacion.comandos import ejecutar_commando as comando

from PropiedadesdelosAlpes.auditoria.modulos.dominio.entidades import Auditoria
from PropiedadesdelosAlpes.auditoria.seedwork.infraestructura.uow import UnidadTrabajoPuerto
from PropiedadesdelosAlpes.auditoria.modulos.aplicacion.mapeadores import MapeadorAuditoria
from PropiedadesdelosAlpes.auditoria.modulos.infraestructura.repositorios import RepositorioAuditorias, RepositorioEventosAuditorias

#Revisar el manejo de DTOs aca
@dataclass
class CrearAuditoria(Comando):
    id: str
    id_auditoria: str
    codigo_auditoria: str
    fecha_auditoria: str
    nombre_auditor: str
    fase_auditoria: str
    hallazgos_auditoria: str
    objetivo_auditoria: str

class CrearAuditoriaHandler(CrearAuditoriaBaseHandler):
    
    def handle(self, comando: CrearAuditoria):
        auditoria_dto = AuditoriaDTO(
            id=comando.id,
            id_auditoria=comando.id_auditoria,
            codigo_auditoria=comando.codigo_auditoria,
            fecha_auditoria=comando.fecha_auditoria,
            nombre_auditor=comando.nombre_auditor,
            fase_auditoria=comando.fase_auditoria,
            hallazgos_auditoria=comando.hallazgos_auditoria,
            objetivo_auditoria=comando.objetivo_auditoria
            )

            

        auditoria: Auditoria = self.fabrica_auditorias.crear_objeto(auditoria_dto, MapeadorAuditoria())
        auditoria.crear_auditoria(auditoria)
        
        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioAuditorias)
        repositorio_eventos = self.fabrica_repositorio.crear_objeto(RepositorioEventosAuditorias)

        UnidadTrabajoPuerto.registrar_batch(repositorio.agregar, auditoria, repositorio_eventos_func=repositorio_eventos.agregar)
        UnidadTrabajoPuerto.commit()

@comando.register(CrearAuditoria)
def ejecutar_comando_crear_auditoria(comando: CrearAuditoria):
    handler = CrearAuditoriaHandler()
    handler.handle(comando)