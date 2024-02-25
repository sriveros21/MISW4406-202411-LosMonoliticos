"""DTOs para la capa de infrastructura del dominio de propiedades

En este archivo usted encontrará los DTOs (modelos anémicos) de
la infraestructura del dominio de propiedades

"""

from PropiedadesdelosAlpes.config.db import db
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, ForeignKey, Integer, Table

import uuid

Base = db.declarative_base()


class Propiedad(db.Model):
    __tablename__ = "propiedades"
    id_propiedad = db.Column(db.Integer, primary_key=True, nullable=False)
    nombre_propiedad = db.Column(db.String, primary_key=False, nullable=False)
    tamano_propiedad = db.Column(db.Integer, primary_key=False, nullable=False)
    tipo_construccion = db.Column(db.String, primary_key=False, nullable=False)
    zonificacion = db.Column(db.String, primary_key=False, nullable=False)
    tamano_lote = db.Column(db.Integer, primary_key=False, nullable=False)
    numero_pisos = db.Column(db.Integer, primary_key=False, nullable=False)
    estacionamiento = db.Column(db.Boolean, primary_key=False, nullable=False)

