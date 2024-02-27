import datetime
from dataclasses import dataclass

from ArquitecturaHexagonal.PropiedadesdelosAlpes.seedwork.dominio.objetos_valor import ObjetoValor


@dataclass(frozen=True)
class NombreCompleto(ObjetoValor):
    nombre: str
    apellido: str


@dataclass(frozen=True)
class EmailContacto(ObjetoValor):
    correo: str


@dataclass(frozen=True)
class FechaRegistro(ObjetoValor):
    fecha: datetime


@dataclass(frozen=True)
class Identificacion(ObjetoValor):
    tipo: str
    numero: str
