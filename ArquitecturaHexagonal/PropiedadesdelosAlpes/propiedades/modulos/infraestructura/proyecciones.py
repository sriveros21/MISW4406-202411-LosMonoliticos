from PropiedadesdelosAlpes.propiedades.seedwork.infraestructura.proyecciones import Proyeccion, ProyeccionHandler
from PropiedadesdelosAlpes.propiedades.seedwork.infraestructura.proyecciones import ejecutar_proyeccion as proyeccion
from PropiedadesdelosAlpes.propiedades.modulos.infraestructura.fabricas import FabricaRepositorio
from PropiedadesdelosAlpes.propiedades.modulos.infraestructura.repositorios import RepositorioPropiedades
from PropiedadesdelosAlpes.propiedades.modulos.dominio.entidades import Propiedad
from PropiedadesdelosAlpes.propiedades.modulos.infraestructura.dto import Propiedad as PropiedadDTO
from PropiedadesdelosAlpes.propiedades.modulos.infraestructura.dto import PropiedadAnalitica

from PropiedadesdelosAlpes.propiedades.seedwork.infraestructura.utils import millis_a_datetime
import datetime
import logging
import traceback
from abc import ABC, abstractmethod
from .dto import Propiedad as PropiedadDTO

class ProyeccionPropiedad(Proyeccion, ABC):
    @abstractmethod
    def ejecutar(self):
        ...

class ProyeccionPropiedadesTotales(ProyeccionPropiedad):
    ADD = 1
    DELETE = 2
    UPDATE = 3

    def __init__(self, fecha_propiedad, operacion):
        self.fecha_propiedad = (fecha_propiedad)
        self.operacion = operacion

    def ejecutar(self, db=None):
        if not db:
            logging.error('ERROR: DB del app no puede ser nula')
            return
        # NOTE esta no usa repositorios y de una vez aplica los cambios. Es decir, no todo siempre debe ser un repositorio
        record = db.session.query(PropiedadAnalitica).filter_by(fecha_creacion=self.fecha_propiedad).one_or_none()

        if record and self.operacion == self.ADD:
            record.total += 1
        elif record and self.operacion == self.DELETE:
            record.total -= 1 
            record.total = max(record.total, 0)
        else:
            db.session.add(PropiedadAnalitica(fecha_creacion=millis_a_datetime(self.fecha_propiedad), total=1))
        
        db.session.commit()

class ProyeccionPropiedadesLista(ProyeccionPropiedad):
    def __init__(self, id, fecha_creacion, codigo, auditor, fase, hallazgos, objetivo):
        self.id = id
        self.fecha = (fecha_creacion)
        self.codigo = codigo
        self.auditor = auditor
        self.fase = fase
        self.hallazgos = hallazgos
        self.objetivo = objetivo
    
    def ejecutar(self, db=None):
        if not db:
            logging.error('ERROR: DB del app no puede ser nula')
            return
        
        fabrica_repositorio = FabricaRepositorio()
        repositorio = fabrica_repositorio.crear_objeto(RepositorioPropiedades)
        
        # TODO Haga los cambios necesarios para que se consideren los itinerarios, demás entidades y asociaciones
        repositorio.agregar(
            Propiedad(
                id=str(self.id),
                codigo_auditoria=str(self.codigo),
                fecha_auditoria=self.fecha,
                nombre_auditor=str(self.auditor),
                fase_auditoria=str(self.fase),
                hallazgos_auditoria=str(self.hallazgos),
                objetivo_auditoria=str(self.objetivo)))
        
        db.session.commit()

class ProyeccionPropiedadHandler(ProyeccionHandler):
    
    def handle(self, proyeccion: ProyeccionPropiedad):

        # TODO El evento de creación no viene con todos los datos de itinerarios, esto tal vez pueda ser una extensión
        # Asi mismo estamos dejando la funcionalidad de persistencia en el mismo método de recepción. Piense que componente
        # podriamos diseñar para alojar esta funcionalidad
        from PropiedadesdelosAlpes.propiedades.config.db import db

        proyeccion.ejecutar(db=db)
        

@proyeccion.register(ProyeccionPropiedadesLista)
@proyeccion.register(ProyeccionPropiedadesTotales)
def ejecutar_proyeccion_propiedad(proyeccion, app=None):
    if not app:
        logging.error('ERROR: Contexto del app no puede ser nulo')
        return
    try:
        with app.app_context():
            handler = ProyeccionPropiedadHandler()
            handler.handle(proyeccion)
            
    except:
        traceback.print_exc()
        logging.error('ERROR: Persistiendo!')
    