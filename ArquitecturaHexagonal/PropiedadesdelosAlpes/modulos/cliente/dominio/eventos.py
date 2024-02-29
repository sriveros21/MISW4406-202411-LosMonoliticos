from dataclasses import dataclass

from PropiedadesdelosAlpes.seedwork.dominio.eventos import (EventoDominio)


@dataclass
class ClienteCreado(EventoDominio):
    id_cliente: str = None
    nombre: str = None
    apellido: str = None
    email: str = None


@dataclass
class ClienteConsultado(EventoDominio):
    id: str = None
