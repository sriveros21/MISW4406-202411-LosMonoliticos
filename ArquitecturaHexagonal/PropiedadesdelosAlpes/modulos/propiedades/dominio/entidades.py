from __future__ import annotations
from dataclasses import dataclass, field

import ArquitecturaHexagonal.PropiedadesdelosAlpes.modulos.propiedades.dominio.objetos_valor as ov
from ArquitecturaHexagonal.PropiedadesdelosAlpes.seedwork.dominio.entidades import Entidad, AgregacionRaiz


@dataclass
class Ubicacion:
    direccion: ov.Direccion = field(default_factory=ov.Direccion)
    ciudad: ov.Ciudad = field(default_factory=ov.Ciudad)
    codigoPostal: ov.CodigoPostal = field(default_factory=ov.CodigoPostal)

    def __str__(self) -> str:
        return f"{self.direccion}, {self.ciudad}, {self.codigoPostal}"

@dataclass
class Propiedad(AgregacionRaiz):
    id: ov.IdPropiedad = field(default_factory=ov.IdPropiedad)
    ubicacion: Ubicacion = field(default_factory=Ubicacion)
    dimensiones: ov.Dimensiones = field(default_factory=ov.Dimensiones)
    tipo: ov.TipoPropiedad = field(default_factory=ov.TipoPropiedad)
    estado: ov.EstadoPropiedad = field(default_factory=ov.EstadoPropiedad)

    def marcar_como_disponible(self):
        self.estado = ov.EstadoPropiedad(disponible=True)

    def marcar_como_no_disponible(self):
        self.estado = ov.EstadoPropiedad(disponible=False)
