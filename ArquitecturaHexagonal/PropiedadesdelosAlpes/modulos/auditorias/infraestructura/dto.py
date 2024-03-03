"""DTOs para la capa de infraestructura del dominio de auditorias

En este archivo se encontrarán los DTOs (modelos anémicos) 
de la infraestructura del dominio de auditorias

"""

from PropiedadesdelosAlpes.modulos.auditorias.dominio.objetos_valor import FaseAuditoria, ObjetivoAuditoria
from PropiedadesdelosAlpes.config.db import db
from sqlalchemy.orm import declarative_base, relationship, backref
from sqlalchemy import Column, ForeignKey, Integer, Table, String, Float, Enum as SQLEnum, DateTime
from sqlalchemy import Enum
from enum import Enum


class Auditoria(db.Model):
    __tablename__ = "auditorias"
    id = Column(String, primary_key=True)
    codigo_auditoria = Column(String, nullable=False)
    fecha_auditoria = Column(DateTime,nullable=False)
    nombre_auditor= Column(String, nullable=False)
    fase_auditoria = Column(SQLEnum(FaseAuditoria), nullable=False)
    hallazgos_auditoria=Column(String, nullable=False)
    objetivo_auditoria=Column(SQLEnum(ObjetivoAuditoria), nullable=False)

