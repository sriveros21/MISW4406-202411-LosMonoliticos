from __future__ import annotations
from abc import ABC, abstractmethod

from dataclasses import dataclass, field
from enum import Enum
from typing import List

from ....seedwork.dominio.entidades import Entidad, AgregacionRaiz
from ....seedwork.dominio.objetos_valor import Ubicacion, Dimension
import PropiedadesdelosAlpes.modulos.propiedades.dominio.objetos_valor as ov

@dataclass(frozen=True)
class TipoPropiedad(Enum):
    RESIDENCIAL = "Minorista"
    COMERCIAL = "Oficina"
    INDUSTRIAL = "Industrial"
    ESPECIALIZADO = "Especializado"
@dataclass
class Edificacion(Entidad, ABC):
    id: str = field(default_factory=str)
    dimension: Dimension = field(default_factory=Dimension)
    tipo: TipoPropiedad = field(default_factory=TipoPropiedad)
    pisos: List[ov.Piso] = field(default_factory=list)

@dataclass
class Terreno(Entidad):
    id: str = field(default_factory=str)
    dimension: Dimension = field(default_factory=Dimension)
    lote: ov.Lote = field(default_factory=ov.Lote)

@dataclass
class Propiedad(AgregacionRaiz):
    id: str = field(default_factory=str)
    nombre: ov.Nombre = field(default_factory=ov.Nombre)
    ubicacion: Ubicacion = field(default_factory=Ubicacion)
    dimension: Dimension = field(default_factory=Dimension)
    tipo: ov.TipoPropiedad = field(default_factory=ov.TipoPropiedad.COMERCIAL)
    estado: ov.EstadoPropiedad = field(default_factory=ov.EstadoPropiedad.DISPONIBLE)
    edificaciones: List[Edificacion] = field(default_factory=list)
    terreno: Terreno = field(default_factory=Terreno)

    def agregar_edificacion(self, edificacion: Edificacion):
        self.edificaciones.append(edificacion)
