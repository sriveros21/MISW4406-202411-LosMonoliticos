"""DTOs para la capa de infrastructura del dominio de propiedades

En este archivo usted encontrará los DTOs (modelos anémicos) de
la infraestructura del dominio de propiedades

"""

from PropiedadesdelosAlpes.modulos.propiedades.dominio.objetos_valor import TipoPropiedad, EstadoPropiedad
from PropiedadesdelosAlpes.config.db import db
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, Float, Integer, ForeignKey, Enum as SQLEnum

import uuid
from sqlalchemy import Enum
from enum import Enum


class Ubicacion(db.Model):
    __tablename__ = 'ubicaciones'
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    latitud = Column(Float, nullable=False)
    longitud = Column(Float, nullable=False)

class Dimension(db.Model):
    __tablename__ = 'dimensiones'
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    width = Column(Float, nullable=False)
    length = Column(Float, nullable=False)
    unit = Column(String, nullable=False)

class Terreno(db.Model):
    __tablename__ = 'terrenos'
    id = Column(String, primary_key=True)
    dimension_id = Column(String, ForeignKey('dimensiones.id'))
    dimension = relationship("Dimension")
    lote = Column(String, nullable=False)
    propiedad_id = Column(String, ForeignKey('propiedades.id'))
    propiedad = relationship("Propiedad", back_populates="terreno")

class Edificacion(db.Model):
    __tablename__ = 'edificaciones'
    id = Column(String, primary_key=True)
    propiedad_id = Column(String, ForeignKey('propiedades.id'))
    tipo = Column(String, nullable=False)
    dimension_id = Column(String, ForeignKey('dimensiones.id'))
    dimension = relationship("Dimension")
    pisos = relationship("Piso", backref="edificacion")

class Piso(db.Model):
    __tablename__ = 'pisos'
    id_piso = Column(String, primary_key=True)
    edificacion_id = Column(String, ForeignKey('edificaciones.id'))
    numero = Column(Integer, nullable=False)
# class TipoPropiedad(Enum):
#     RESIDENCIAL = "Residencial"
#     COMERCIAL = "Comercial"
#     INDUSTRIAL = "Industrial"
#     ESPECIALIZADO = "Especializado"

# class EstadoPropiedad(Enum):
#     DISPONIBLE = "Disponible"
#     NO_DISPONIBLE = "No Disponible"
#     EN_REPARACION = "En Reparación"

class Propiedad(db.Model):
    __tablename__ = "propiedades"
    id = Column(String, primary_key=True)
    nombre = Column(String, nullable=False)
    ubicacion_id = Column(String, ForeignKey('ubicaciones.id'))
    ubicacion = relationship("Ubicacion")
    dimension_id = Column(String, ForeignKey('dimensiones.id'))
    dimension = relationship("Dimension")
    tipo = Column(SQLEnum(TipoPropiedad), nullable=False)
    estado = Column(SQLEnum(EstadoPropiedad), nullable=False)
    edificaciones = relationship("Edificacion", backref="propiedad")
    terreno = relationship("Terreno", uselist=False, back_populates="propiedad")
