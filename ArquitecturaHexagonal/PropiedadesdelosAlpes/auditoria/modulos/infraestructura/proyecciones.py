from PropiedadesdelosAlpes.auditoria.seedwork.infraestructura.proyecciones import Proyeccion, ProyeccionHandler
from PropiedadesdelosAlpes.auditoria.seedwork.infraestructura.proyecciones import ejecutar_proyeccion as proyeccion
from PropiedadesdelosAlpes.auditoria.modulos.infraestructura.fabricas import FabricaRepositorioAuditorias
from PropiedadesdelosAlpes.auditoria.modulos.infraestructura.repositorios import RepositorioAuditorias
from PropiedadesdelosAlpes.auditoria.modulos.dominio.entidades import Auditoria
from PropiedadesdelosAlpes.auditoria.modulos.infraestructura.dto import Auditoria as AuditoriaDTO

from PropiedadesdelosAlpes.auditoria.seedwork.infraestructura.utils import millis_a_datetime
import datetime
import logging
import traceback
from abc import ABC, abstractmethod
from .dto import Auditoria as AuditoriaDTO

class ProyeccionAuditoria(Proyeccion, ABC):
    @abstractmethod
    def ejecutar(self):
        ...

class ProyeccionAuditoriasTotales(ProyeccionAuditoria):
    ADD = 1
    DELETE = 2
    UPDATE = 3

    def __init__(self, fecha_auditoria, operacion):
        self.fecha_auditoria = millis_a_datetime(fecha_auditoria)
        print(f'Fecha Auditoria recibido: {self.fecha_auditoria}')
        self.operacion = operacion

    def ejecutar(self, db=None):
        if not db:
            logging.error('ERROR: DB del app no puede ser nula')
            return
        # NOTE esta no usa repositorios y de una vez aplica los cambios. Es decir, no todo siempre debe ser un repositorio
        record = db.session.query(AuditoriaDTO).filter_by(fecha_auditoria=self.fecha_auditoria.date()).one_or_none()
        print("SOY RECORD", record)

        if record and self.operacion == self.ADD:
            record.total += 1
        elif record and self.operacion == self.DELETE:
            record.total -= 1 
            record.total = max(record.total, 0)
        else:
            db.session.add(Auditoria(fecha=self.fecha_auditoria.date()))
        
        db.session.commit()

class ProyeccionAuditoriasLista(ProyeccionAuditoria):
    def __init__(self, id, id_auditoria, fecha_creacion, codigo, auditor, fase, hallazgos, objetivo):
        self.id = id
        self.id_auditoria = id_auditoria
        self.fecha = millis_a_datetime(fecha_creacion)
        self.codigo = codigo
        self.auditor = auditor
        self.fase = fase
        self.hallazgos = hallazgos
        self.objetivo = objetivo
    
    def ejecutar(self, db=None):
        if not db:
            logging.error('ERROR: DB del app no puede ser nula')
            return
        
        fabrica_repositorio = FabricaRepositorioAuditorias()
        repositorio = fabrica_repositorio.crear_objeto(RepositorioAuditorias)
        
        # TODO Haga los cambios necesarios para que se consideren los itinerarios, demás entidades y asociaciones
        repositorio.agregar(
            Auditoria(
                id=str(self.id_auditoria),
                id_auditoria=str(self.id_auditoria),
                codigo=str(self.codigo),
                fecha=self.fecha_creacion,
                auditor=str(self.auditor),
                fase=str(self.fase),
                hallazgos=str(self.hallazgos),
                objetivo=str(self.objetivo)))
        
        db.session.commit()

class ProyeccionAuditoriaHandler(ProyeccionHandler):
    
    def handle(self, proyeccion: ProyeccionAuditoria):

        # TODO El evento de creación no viene con todos los datos de itinerarios, esto tal vez pueda ser una extensión
        # Asi mismo estamos dejando la funcionalidad de persistencia en el mismo método de recepción. Piense que componente
        # podriamos diseñar para alojar esta funcionalidad
        from PropiedadesdelosAlpes.auditoria.config.db import db

        proyeccion.ejecutar(db=db)
        

@proyeccion.register(ProyeccionAuditoriasLista)
@proyeccion.register(ProyeccionAuditoriasTotales)
def ejecutar_proyeccion_auditoria(proyeccion, app=None):
    if not app:
        logging.error('ERROR: Contexto del app no puede ser nulo')
        return
    try:
        with app.app_context():
            handler = ProyeccionAuditoriaHandler()
            handler.handle(proyeccion)
            
    except:
        traceback.print_exc()
        logging.error('ERROR: Persistiendo!')
    