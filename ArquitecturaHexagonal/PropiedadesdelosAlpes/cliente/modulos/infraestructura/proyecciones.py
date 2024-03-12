import logging
import traceback
from abc import ABC, abstractmethod

from PropiedadesdelosAlpes.cliente.modulos.dominio.entidades import Cliente
from PropiedadesdelosAlpes.cliente.modulos.infraestructura.dto import ClienteAnalitica
from PropiedadesdelosAlpes.cliente.modulos.infraestructura.fabricas import FabricaRepositorioCliente
from PropiedadesdelosAlpes.cliente.modulos.infraestructura.repositorios import RepositorioCliente
from PropiedadesdelosAlpes.cliente.seedwork.infraestructura.proyecciones import Proyeccion, ProyeccionHandler
from PropiedadesdelosAlpes.cliente.seedwork.infraestructura.proyecciones import ejecutar_proyeccion as proyeccion
from PropiedadesdelosAlpes.cliente.seedwork.infraestructura.utils import millis_a_datetime


class ProyeccionCliente(Proyeccion, ABC):
    @abstractmethod
    def ejecutar(self):
        ...

    class ProyeccionClienteTotales(ProyeccionCliente):
        ADD = 1
        DELETE = 2
        UPDATE = 3

    # def __init__(self, fecha_auditoria, operacion):
    #     self.fecha_auditoria = (fecha_auditoria)
    #     print(f'Fecha Auditoria recibido: {self.fecha_auditoria}')
    #     self.operacion = operacion
    #
    # def ejecutar(self, db=None):
    #     if not db:
    #         logging.error('ERROR: DB del app no puede ser nula')
    #         return
    #     # NOTE esta no usa repositorios y de una vez aplica los cambios. Es decir, no todo siempre debe ser un repositorio
    #     record = db.session.query(ClienteAnalitica).filter_by(fecha_creacion=self.fecha_auditoria).one_or_none()
    #     print("SOY RECORD", record)
    #
    #     if record and self.operacion == self.ADD:
    #         record.total += 1
    #     elif record and self.operacion == self.DELETE:
    #         record.total -= 1
    #         record.total = max(record.total, 0)
    #     else:
    #         db.session.add(ClienteAnalitica(fecha_creacion=millis_a_datetime(self.fecha_auditoria), total=1))
    #
    #     db.session.commit()


class ProyeccionClienteLista(ProyeccionCliente):
    def __init__(self, id, id_cliente, nombre, apellido, email):
        self.id = id
        self.id_cliente = id_cliente
        self.nombre = nombre
        self.apellido = apellido
        self.email = email

    def ejecutar(self, db=None):
        if not db:
            logging.error('ERROR: DB del app no puede ser nula')
            return

        fabrica_repositorio = FabricaRepositorioCliente()
        repositorio = fabrica_repositorio.crear_objeto(RepositorioCliente)

        # TODO Haga los cambios necesarios para que se consideren los itinerarios, demás entidades y asociaciones
        repositorio.agregar(
            Cliente(
                id=str(self.id),
                id_cliente=str(self.id_cliente),
                nombre=str(self.nombre),
                apellido=str(self.apellido),
                email=str(self.email)))

        db.session.commit()


class ProyeccionClienteHandler(ProyeccionHandler):

    def handle(self, proyeccion: ProyeccionCliente):
        # TODO El evento de creación no viene con todos los datos de itinerarios, esto tal vez pueda ser una extensión
        # Asi mismo estamos dejando la funcionalidad de persistencia en el mismo método de recepción. Piense que componente
        # podriamos diseñar para alojar esta funcionalidad
        from PropiedadesdelosAlpes.cliente.config.db import db

        proyeccion.ejecutar(db=db)


@proyeccion.register(ProyeccionClienteLista)
@proyeccion.register(ProyeccionClienteTotales)
def ejecutar_proyeccion_cliente(proyeccion, app=None):
    if not app:
        logging.error('ERROR: Contexto del app no puede ser nulo')
        return
    try:
        with app.app_context():
            handler = ProyeccionClienteHandler()
            handler.handle(proyeccion)

    except:
        traceback.print_exc()
        logging.error('ERROR: Persistiendo!')
