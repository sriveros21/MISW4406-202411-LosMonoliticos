from dataclasses import dataclass

from ....seedwork.aplicacion.dto import DTO


@dataclass(frozen=True)
class NombreCompletoDTO(DTO):
    nombre: str
    apellido: str


@dataclass(frozen=True)
class EmailContactoDTO(DTO):
    correo: str


@dataclass(frozen=True)
class IdentificacionDTO(DTO):
    tipo: str
    numero: str

@dataclass(frozen=True)
class ClienteDTO(DTO):

    id_cliente = db.Column(db.Integer, primary_key=True, nullable=False)
    nombre_cliente = db.Column(db.String, primary_key=False, nullable=False)
    email_cliente = db.Column(db.String, primary_key=False, nullable=False)
