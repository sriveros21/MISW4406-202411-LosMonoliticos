from dataclasses import dataclass, field
from datetime import datetime

from .objetos_valor import NombreCompleto, EmailContacto, Identificacion, FechaRegistro
from ....seedwork.dominio.entidades import Entidad


@dataclass
class Cliente(Entidad):
    nombre: NombreCompleto = field(default_factory=NombreCompleto)
    email: EmailContacto = field(default_factory=EmailContacto)


@dataclass
class Inquilino(Cliente):
    identificacion: Identificacion = field(default_factory=Identificacion)
    fecha_inicio_contrato: FechaRegistro = field(default_factory=datetime.now)
