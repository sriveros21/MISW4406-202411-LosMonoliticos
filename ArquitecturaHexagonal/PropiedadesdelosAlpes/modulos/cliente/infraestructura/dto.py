from PropiedadesdelosAlpes.config.db import db

Base = db.declarative_base()


class Cliente(db.Model):
    __tablename__ = "clientes"
    id_cliente = db.Column(db.String, primary_key=True, nullable=False)
    nombre_cliente = db.Column(db.String, primary_key=False, nullable=False)
    apellido_cliente = db.Column(db.String, primary_key=False, nullable=False)
    email_cliente = db.Column(db.String, primary_key=False, nullable=False)
