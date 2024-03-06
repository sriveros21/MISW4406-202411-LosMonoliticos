from PropiedadesdelosAlpes.config.db import db

Base = db.declarative_base()


class Cliente(db.Model):
    __tablename__ = "clientes"
    id_cliente = db.Column(db.String(60), primary_key=True)
    nombre = db.Column(db.String(60), primary_key=False, nullable=False)
    apellido = db.Column(db.String(60), primary_key=False, nullable=False)
    email = db.Column(db.String(60), primary_key=False, nullable=False)
