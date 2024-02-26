"""DTOs para la capa de infrastructura del dominio de clientes

En este archivo usted encontrará los DTOs (modelos anémicos) de
la infraestructura del dominio de clientes

"""

from PropiedadesdelosAlpes.config.db import db
from sqlalchemy.orm import declarative_base, relationship, backref
from sqlalchemy import Column, ForeignKey, Integer, Table

import uuid

Base = db.declarative_base()


class Cliente(db.Model):
    __tablename__ = "clientes"
    id_cliente = db.Column(db.Integer, primary_key=True, nullable=False)
    nombre_cliente = db.Column(db.String, primary_key=False, nullable=False)
    email_cliente = db.Column(db.String, primary_key=False, nullable=False)
