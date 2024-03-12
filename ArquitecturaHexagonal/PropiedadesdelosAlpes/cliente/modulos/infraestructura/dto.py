import uuid

from PropiedadesdelosAlpes.cliente.config.db import db
from sqlalchemy import Column, String

Base = db.declarative_base()


class Cliente(db.Model):
    __tablename__ = "clientes"
    id = Column(String(60), primary_key=True, default=lambda: str(uuid.uuid4()))
    id_cliente = Column(db.String(60), primary_key=True)
    nombre = Column(db.String(60), primary_key=False, nullable=False)
    apellido = Column(db.String(60), primary_key=False, nullable=False)
    email = Column(db.String(60), primary_key=False, nullable=False)
