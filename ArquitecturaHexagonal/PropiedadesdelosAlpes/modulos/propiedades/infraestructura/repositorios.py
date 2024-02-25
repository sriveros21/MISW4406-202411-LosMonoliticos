""" Repositorios para el manejo de persistencia de objetos de dominio en la capa de infrastructura del dominio de vuelos

En este archivo usted encontrará las diferentes repositorios para
persistir objetos dominio (agregaciones) en la capa de infraestructura del dominio de vuelos

"""

from PropiedadesdelosAlpes.config.db import db
from PropiedadesdelosAlpes.modulos.propiedades.dominio.repositorios import RepositorioPropiedades, RepositorioClientes
from PropiedadesdelosAlpes.modulos.propiedades.dominio.entidades import Propietario, Propiedad
from PropiedadesdelosAlpes.modulos.propiedades.dominio.fabricas import FabricaPropiedades
from .dto import Propiedad as PropiedadDTO
from .mapeadores import MapeadorPropiedades
from uuid import UUID
from typing import List

class RepositorioPropiedadesSQLite(RepositorioPropiedades):

    def obtener_por_id(self, id: UUID) -> Propietario:
        # TODO
        raise NotImplementedError

    def obtener_todos(self) -> List[Propietario]:

        id_propiedad = 123
        nombre_propiedad = "prop.nombre"
        tamano_propiedad = 200
        tipo_construccion = "prop.tipo"
        ubicacion_propiedad = "prop.ubicacion"
        estado_propiedad = "prop.estado"

        propiedad = Propiedad(
            id=id_propiedad,
            nombre=nombre_propiedad,
            dimensiones=tamano_propiedad,
            tipo=tipo_construccion,
            ubicacion=ubicacion_propiedad,
            estado=estado_propiedad
        )

        return [propiedad]

    def agregar(self, entity: Propiedad):
        # TODO
        raise NotImplementedError

    def actualizar(self, entity: Propiedad):
        # TODO
        raise NotImplementedError

    def eliminar(self, entity_id: UUID):
        # TODO
        raise NotImplementedError


class RepositorioClientesSQLite(RepositorioClientes):

    def __init__(self):
        self._fabrica_propiedades: FabricaPropiedades = FabricaPropiedades()

    @property
    def fabrica_propiedades(self):
        return self._fabrica_propiedades

    def obtener_por_id(self, id: UUID) -> Propiedad:
        propiedad_dto = db.session.query(PropiedadDTO).filter_by(id=str(id)).one()
        return self.fabrica_propiedades.crear_objeto(propiedad_dto, MapeadorPropiedades())

    def obtener_todos(self) -> List[Propiedad]:
        # TODO
        raise NotImplementedError

    def agregar(self, propiedad: Propiedad):
        propiedad_dto = self.fabrica_propiedades.crear_objeto(propiedad, MapeadorPropiedades())
        db.session.add(propiedad_dto)
        db.session.commit()

    def actualizar(self, reserva: Propiedad):
        # TODO
        raise NotImplementedError

    def eliminar(self, reserva_id: UUID):
        # TODO
        raise NotImplementedError