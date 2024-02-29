from dataclasses import dataclass

from PropiedadesdelosAlpes.seedwork.dominio.objetos_valor import ObjetoValor


@dataclass(frozen=True)
class IdentificadorCliente:
    identificador: str


@dataclass(frozen=True)
class Nombre(ObjetoValor):
    nombre: str


@dataclass(frozen=True)
class Apellido(ObjetoValor):
    apellido: str


@dataclass(frozen=True)
class Email(ObjetoValor):
    email: str
