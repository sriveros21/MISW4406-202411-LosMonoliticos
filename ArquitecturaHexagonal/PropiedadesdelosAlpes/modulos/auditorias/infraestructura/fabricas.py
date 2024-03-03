""" Fábricas para la creación de objetivos en la capa de Infraestructura del dominio de auditorias

En este archivo se encontrarán las diferentes fábricas para crear
objetos complejos en la capa de infraestructura del dominio de propiedades

"""

from dataclasses import dataclass, field
from typing import Any
from PropiedadesdelosAlpes.seedwork.dominio.fabricas import Fabrica
from PropiedadesdelosAlpes.seedwork.dominio.repositorios import Repositorio
from PropiedadesdelosAlpes.modulos.auditorias.dominio.repositorios import RepositorioAuditorias
from PropiedadesdelosAlpes.modulos.auditorias.infraestructura.mapeadores import MapeadorAuditorias
from PropiedadesdelosAlpes.modulos.auditorias.dominio.fabricas import FabricaAuditorias
from .repositorios import RepositorioAuditoriasSQLite
from.excepciones import ExcepcionFabrica
from sqlalchemy.orm import Session


@dataclass
class FabricaRepositorio:
    def __init__(self, db_session:Session):
        self.db_session =db_session

    def crear_repositorio_auditorias(self) -> RepositorioAuditoriasSQLite:
        mapeador_auditorias = MapeadorAuditorias(db_session=self.db_session)
        fabrica_auditorias = FabricaAuditorias()
        return RepositorioAuditoriasSQLite(db_session=self.db_session, mapeador=mapeador_auditorias, fabrica=fabrica_auditorias)   

    # def crear_objeto(self, obj: type, mapeador: any = None) -> Repositorio:
    #     if obj == RepositorioAuditorias.__class__:
    #         return RepositorioAuditoriasSQLite()
    #     raise ExcepcionFabrica()

    def obtener_repositorio_auditorias(self) -> RepositorioAuditorias:
        """
        Returns an instance of RepositorioAuditorias.
        This method simplifies accessing the auditories repository.
        """
        return RepositorioAuditoriasSQLite()