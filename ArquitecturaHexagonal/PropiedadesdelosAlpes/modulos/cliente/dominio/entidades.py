from datetime import datetime
from ArquitecturaHexagonal.PropiedadesdelosAlpes.seedwork.dominio.entidades import Entidad
from dataclasses import dataclass, field
from .objetos_valor import NombreCompleto, EmailContacto, Identificacion, FechaRegistro

@dataclass
class Usuario(Entidad):
    nombre: NombreCompleto = field(default_factory=NombreCompleto)
    email: EmailContacto = field(default_factory=EmailContacto)

@dataclass
class Propietario(Usuario):
    identificacion: Identificacion = field(default_factory=Identificacion)
    fecha_registro: datetime = field(default_factory=datetime.now)

@dataclass
class Inquilino(Usuario):
    identificacion: Identificacion = field(default_factory=Identificacion)
    fecha_inicio_contrato: datetime = field(default_factory=datetime.now)
