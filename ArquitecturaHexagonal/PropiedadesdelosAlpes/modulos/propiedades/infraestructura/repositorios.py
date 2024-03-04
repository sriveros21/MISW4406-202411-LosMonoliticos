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

    def __init__(self, db_session, mapeador: MapeadorPropiedades, fabrica: FabricaPropiedades):
        self.db_session = db_session
        self.mapeador = mapeador
        self.fabrica = fabrica
        #self._fabrica_propiedades = FabricaPropiedades()
        #self.mapeador_propiedades = MapeadorPropiedades(db.session)

    @property
    def fabrica_propiedades(self):
        return self.fabrica

    def obtener_por_id(self, id: str) -> Propiedad:
        propiedad_dto = db.session.query(PropiedadDTO).filter_by(id=str(id)).one()
        print("OBJETO DB CONSULTA 2",propiedad_dto)
        return self.fabrica.crear_objeto(propiedad_dto, self.mapeador)

    def agregar(self, propiedad: Propiedad):
        print("Agregando propiedad")
        print(propiedad)
        #propiedad_dto = self.mapeador.entidad_a_dto(propiedad)
        propiedad_dto = self.fabrica.crear_objeto(propiedad, self.mapeador)
        print(propiedad_dto)
        print(self.mapeador)
        self.db_session.add(propiedad_dto)
        self.db_session.commit()