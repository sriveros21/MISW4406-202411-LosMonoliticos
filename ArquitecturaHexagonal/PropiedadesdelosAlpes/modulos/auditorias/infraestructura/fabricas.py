""" Fábricas para la creación de objetivos en la capa de Infraestructura del dominio de auditorias

En este archivo se encontrarán las diferentes fábricas para crear
objetos complejos en la capa de infraestructura del dominio de propiedades

"""

from dataclasses import dataclass, field
from PropiedadesdelosAlpes.seedwork.dominio.fabricas import Fabrica
from PropiedadesdelosAlpes.seedwork.dominio.repositorios import Repositorio
from PropiedadesdelosAlpes.modulos.auditorias.dominio.repositorios import RepositorioAuditorias
from .repositorios import RepositorioAuditoriasSQLite
from.excepciones import ExcepcionFabrica


@dataclass
class FabricaRepositorio(Fabrica):
    def crear_objeto(self, obj: type, mapeador: any = None) -> Repositorio:
        if obj == RepositorioAuditorias.__class__:
            return RepositorioAuditoriasSQLite()
        else:
            raise ExcepcionFabrica()

    def obtener_repositorio_auditorias(self) -> RepositorioAuditorias:
        """
        Returns an instance of RepositorioAuditorias.
        This method simplifies accessing the auditories repository.
        """
        return RepositorioAuditoriasSQLite()