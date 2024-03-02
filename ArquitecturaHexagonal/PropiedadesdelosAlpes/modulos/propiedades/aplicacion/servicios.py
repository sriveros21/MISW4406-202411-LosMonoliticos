from uuid import UUID
from PropiedadesdelosAlpes.seedwork.aplicacion.servicios import Servicio
from PropiedadesdelosAlpes.modulos.propiedades.dominio.entidades import Propiedad
from PropiedadesdelosAlpes.modulos.propiedades.infraestructura.repositorios import RepositorioPropiedades
from .mapeadores import MapeadorPropiedad

from .dto import PropiedadDTO

class ServicioPropiedad(Servicio):

    def __init__(self, repositorio: RepositorioPropiedades, mapeador: MapeadorPropiedad):
        self.repositorio = repositorio
        self.mapeador = mapeador

    def crear_propiedad(self, propiedad_dto: PropiedadDTO) -> PropiedadDTO:

        propiedad: Propiedad = self.mapeador.dto_a_entidad(propiedad_dto)

        self.repositorio.agregar(propiedad)
        return self.mapeador.entidad_a_dto(propiedad)

    def obtener_propiedad_por_id(self, id: UUID) -> PropiedadDTO:
        propiedad = self.repositorio.obtener_por_id(id)
        if propiedad:
            print("MIRENME HE INGRESADO AQUI")
            return self.mapeador.entidad_a_dto(propiedad)
        return None

