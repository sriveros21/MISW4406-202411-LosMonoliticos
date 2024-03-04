from PropiedadesdelosAlpes.config.db import db
from sqlalchemy import Column, String

Base = db.declarative_base()


class Cliente(db.Model):
    __tablename__ = "clientes"
    id_cliente = Column(String, primary_key=True)
    nombre = Column(String, nullable=False)
    apellido = Column(String, nullable=False)
    email = Column(String, nullable=False)
