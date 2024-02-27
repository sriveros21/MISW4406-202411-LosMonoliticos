"""DTOs para la capa de infraestructura del dominio de auditorias

En este archivo se encontrarán los DTOs (modelos anémicos) 
de la infraestructura del dominio de auditorias

"""

from PropiedadesdelosAlpes.config.db import db
from sqlalchemy.orm import declarative_base, relationship, backref
from sqlalchemy import Column, ForeignKey, Integer, Table

Base =db.declarative_base()

#Revisar esta tabla id string?

class Auditoria(db.Model):
    __tablename__ = "auditorias"
    #id= db.Column(db.String, primary_key=True, nullable=False)
    codigo_auditoria =  db.Column(db.String, primary_key=False, nullable=False)
    fecha_auditoria =  db.Column(db.DateTime, primary_key=False, nullable=False)
    nombre_auditor =  db.Column(db.String, primary_key=False, nullable=False)
    fase_auditoria =  db.Column(db.String, primary_key=False, nullable=False)
    hallazgos_auditoria =  db.Column(db.String, primary_key=False, nullable=False)
    objetivo_auditoria =  db.Column(db.String, primary_key=False, nullable=False)


