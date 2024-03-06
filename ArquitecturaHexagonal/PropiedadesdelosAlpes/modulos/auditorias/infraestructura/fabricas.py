""" Fábricas para la creación de objetivos en la capa de Infraestructura del dominio de auditorias

En este archivo se encontrarán las diferentes fábricas para crear
objetos complejos en la capa de infraestructura del dominio de propiedades

"""

from dataclasses import dataclass, field
from PropiedadesdelosAlpes.modulos.auditorias.dominio.repositorios import RepositorioAuditorias, RepositorioEventosAuditorias
from PropiedadesdelosAlpes.modulos.auditorias.infraestructura.mapeadores import MapeadorAuditorias
from PropiedadesdelosAlpes.modulos.auditorias.dominio.fabricas import FabricaAuditorias
from PropiedadesdelosAlpes.seedwork.dominio.fabricas import Fabrica
from PropiedadesdelosAlpes.seedwork.dominio.repositorios import Repositorio
from PropiedadesdelosAlpes.seedwork.infraestructura.vistas import Vista
from PropiedadesdelosAlpes.modulos.auditorias.infraestructura.vistas import VistaAuditoria
from .repositorios import RepositorioAuditoriasSQLite, RepositorioEventosAuditoriaSQLAlchemy
from.excepciones import ExcepcionFabrica
from sqlalchemy.orm import Session


@dataclass
class FabricaRepositorioAuditorias(Fabrica):
    def crear_objeto(self, obj: type, mapeador: any = None) -> Repositorio:
        if obj == RepositorioAuditorias:
            return RepositorioAuditoriasSQLite()
        elif obj == RepositorioEventosAuditorias:
            return RepositorioEventosAuditoriaSQLAlchemy()
        else:
            raise ExcepcionFabrica(f'No existe fábrica para el objeto {obj}')

@dataclass
class FabricaVista(Fabrica):
    def crear_objeto(self, obj: type, mapeador: any = None) -> Vista:
        if obj == Auditoria:
            return VistaAuditoria()
        else:
            raise ExcepcionFabrica(f'No existe fábrica para el objeto {obj}')