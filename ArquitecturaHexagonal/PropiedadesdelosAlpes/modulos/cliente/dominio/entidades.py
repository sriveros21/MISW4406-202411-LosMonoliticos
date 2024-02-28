from dataclasses import dataclass, field

import PropiedadesdelosAlpes.modulos.cliente.dominio.objetos_valor as ov
from PropiedadesdelosAlpes.seedwork.dominio.entidades import AgregacionRaiz, Entidad


@dataclass
class Cliente(AgregacionRaiz):
    nombre: ov.Nombre = field(default_factory=ov.Nombre)
    apellido: ov.Apellido = field(default_factory=ov.Apellido)
    email: ov.Email = field(default_factory=ov.Email)
