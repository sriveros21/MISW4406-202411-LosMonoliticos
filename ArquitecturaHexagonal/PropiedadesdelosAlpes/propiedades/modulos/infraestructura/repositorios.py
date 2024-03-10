""" Repositorios para el manejo de persistencia de objetos de dominio en la capa de infrastructura del dominio de clientes

En este archivo usted encontrará las diferentes repositorios para
persistir objetos dominio (agregaciones) en la capa de infraestructura del dominio de clientes

"""

from PropiedadesdelosAlpes.config.db import db
from PropiedadesdelosAlpes.modulos.propiedades.dominio.repositorios import RepositorioPropiedades
from PropiedadesdelosAlpes.modulos.propiedades.dominio.entidades import Propiedad

from PropiedadesdelosAlpes.modulos.propiedades.dominio.fabricas import FabricaPropiedades
from .dto import Propiedad as PropiedadDTO
from .mapeadores import MapeadorPropiedades
from uuid import UUID
from typing import List


class RepositorioPropiedadesSQLite(RepositorioPropiedades):

    def __init__(self):
        self._fabrica_propiedades: FabricaPropiedades = FabricaPropiedades()

    @property
    def fabrica_propiedades(self):
        return self._fabrica_propiedades

    def obtener_por_id(self, id: UUID) -> Propiedad:
        propiedad_dto = db.session.query(PropiedadDTO).filter_by(id=str(id)).one()
        return self.fabrica_propiedades.crear_objeto(propiedad_dto, MapeadorPropiedades())

    def agregar(self, propiedad: Propiedad):
        #mapeador = MapeadorPropiedades()
        #propiedad_dto = mapeador.entidad_a_dto(propiedad)
        propiedad_dto = self.fabrica_propiedades.crear_objeto(propiedad, MapeadorPropiedades())
        print(f"Propiedad DTO: {propiedad_dto}")
        #propiedad_dto = self.fabrica_propiedades.crear_objeto(propiedad, MapeadorPropiedades())
        db.session.add(propiedad_dto)
        db.session.commit()