from uuid import UUID
from PropiedadesdelosAlpes.modulos.propiedades.infraestructura.mapeadores import MapeadorPropiedades
from PropiedadesdelosAlpes.seedwork.infraestructura.uow import UnidadTrabajoPuerto
from PropiedadesdelosAlpes.modulos.propiedades.dominio.fabricas import FabricaPropiedades
from PropiedadesdelosAlpes.modulos.propiedades.infraestructura.fabricas import FabricaRepositorio
from PropiedadesdelosAlpes.seedwork.aplicacion.servicios import Servicio
from PropiedadesdelosAlpes.modulos.propiedades.dominio.entidades import Propiedad
from PropiedadesdelosAlpes.modulos.propiedades.infraestructura.repositorios import RepositorioPropiedades
from .mapeadores import MapeadorPropiedad

from .dto import PropiedadDTO

class ServicioPropiedad(Servicio):

    def __init__(self):
        self._fabrica_repositorio: FabricaRepositorio = FabricaRepositorio()
        self._fabrica_propiedades: FabricaPropiedades = FabricaPropiedades()

    @property
    def fabrica_repositorio(self):
        return self._fabrica_repositorio

    @property
    def fabrica_propiedades(self):
        return self._fabrica_propiedades

    def crear_propiedad(self, propiedad_dto: PropiedadDTO) -> PropiedadDTO:

        propiedad: Propiedad = self.fabrica_propiedades.crear_objeto(propiedad_dto, MapeadorPropiedad())
        print(f"Converted Propiedad Entity: {propiedad}")
        #mapeador = MapeadorPropiedades()
        #propiedad_entidad = mapeador.dto_a_entidad(propiedad_dto)
        #print(f"Converted Propiedad Entity Directly: {propiedad_entidad}")
        propiedad.crear_propiedad(propiedad)

        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioPropiedades.__class__)

        UnidadTrabajoPuerto.registrar_batch(repositorio.agregar, propiedad)
        UnidadTrabajoPuerto.savepoint()
        UnidadTrabajoPuerto.commit()

        return self.fabrica_propiedades.crear_objeto(propiedad, MapeadorPropiedad())

    def obtener_propiedad_por_id(self, id) -> PropiedadDTO:
        repositorio= self.fabrica_repositorio.crear_objeto(RepositorioPropiedades.__class__)
        return self.fabrica_propiedades.crear_objeto(repositorio.obtener_por_id(id), MapeadorPropiedad())

