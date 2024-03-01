"""DTOs para la capa de infrastructura del dominio de propiedades

En este archivo usted encontrará los DTOs (modelos anémicos) de
la infraestructura del dominio de propiedades

"""

from PropiedadesdelosAlpes.config.db import db
from sqlalchemy.orm import declarative_base, relationship, backref
from sqlalchemy import Column, ForeignKey, Integer, Table

import uuid

Base = db.declarative_base()


class Propiedad(db.Model):
    __tablename__ = "propiedades"
    id_propiedad = db.Column(db.String, primary_key=True, nullable=False)
    nombre = db.Column(db.String, primary_key=False, nullable=False)
    ubicacion = db.Column(db.String, nullable=False)
    dimensiones = db.Column(db.Float, nullable=False)
    tipo = db.Column(db.String, nullable=False)
    estado = db.Column(db.String, nullable=False)
    edificaciones = relationship("Edificacion", backref="propiedad")
    #terreno_id = db.Column(db.String, db.ForeignKey('terrenos.id'))
    terreno = relationship("Terreno", back_populates="propiedad")
