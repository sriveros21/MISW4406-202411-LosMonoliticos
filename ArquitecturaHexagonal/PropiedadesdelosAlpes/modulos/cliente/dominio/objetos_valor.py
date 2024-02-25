import datetime
from ArquitecturaHexagonal.PropiedadesdelosAlpes.seedwork.dominio.objetos_valor import ObjetoValor
from dataclasses import dataclass

@dataclass(frozen=True)
class NombreCompleto(ObjetoValor):
    primer_nombre: str
    apellidos: str

@dataclass(frozen=True)
class EmailContacto(ObjetoValor):
    correo: str


@dataclass(frozen=True)
class FechaRegistro(ObjetoValor):
    fecha: datetime
