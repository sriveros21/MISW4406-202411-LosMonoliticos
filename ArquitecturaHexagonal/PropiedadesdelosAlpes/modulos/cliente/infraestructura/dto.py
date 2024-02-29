from PropiedadesdelosAlpes.config.db import db

Base = db.declarative_base()


class Cliente(db.Model):
    __tablename__ = "clientes"
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    nombre = db.Column(db.String, primary_key=False, nullable=False)
    apellido = db.Column(db.String, primary_key=False, nullable=False)
    email = db.Column(db.String, primary_key=False, nullable=False)
