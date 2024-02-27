from PropiedadesdelosAlpes.seedwork.aplicacion.comandos import Comando
from PropiedadesdelosAlpes.modulos.auditorias.aplicacion.dto import AuditoriaDTO,FechaAuditoriaDTO,CodigoAuditoriaDTO,NombreAuditorDTO,HallazgosAuditoriaDTO, FaseAuditoria, ObjetivoAuditoria
from .base import CrearAuditoriaBaseHandler
from dataclasses import dataclass, field
from PropiedadesdelosAlpes.seedwork.aplicacion.comandos import ejecutar_commando as comando

from PropiedadesdelosAlpes.modulos.auditorias.dominio.entidades import Auditoria
from PropiedadesdelosAlpes.seedwork.infraestructura.uow import UnidadTrabajoPuerto
from PropiedadesdelosAlpes.modulos.auditorias.aplicacion.mapeadores import MapeadorAuditoria
from PropiedadesdelosAlpes.modulos.auditorias.infraestructura.repositorios import RepositorioAuditorias

#Revisar el manejo de DTOs aca
@dataclass
class CrearAuditoria(Comando):
    codigo: CodigoAuditoriaDTO
    fecha: FechaAuditoriaDTO
    auditor: NombreAuditorDTO
    fase: FaseAuditoria
    hallazgos:HallazgosAuditoriaDTO
    objetivo: ObjetivoAuditoria

class CrearAuditoriaHandler(CrearAuditoriaBaseHandler):
    
    def handle(self, comando: CrearAuditoria):
        auditoria_dto = AuditoriaDTO(
                codigo=comando.codigo,
                fecha=comando.fecha,
                auditor=comando.auditor,
                fase=comando.fase,
                hallazgos=comando.hallazgos,
                objetivo=comando.objetivo
                )

        auditoria: Auditoria = self.fabrica_auditorias.crear_objeto(auditoria_dto, MapeadorAuditoria())
        auditoria.crear_auditoria(auditoria)

        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioAuditorias.__class__)

        UnidadTrabajoPuerto.registrar_batch(repositorio.agregar, auditoria)
        UnidadTrabajoPuerto.savepoint()
        UnidadTrabajoPuerto.commit()