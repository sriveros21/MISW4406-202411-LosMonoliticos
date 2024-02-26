from __future__ import annotations
from abc import ABC, abstractmethod

from dataclasses import dataclass, field
from typing import List

from ....seedwork.dominio.entidades import Entidad, AgregacionRaiz
from ....seedwork.dominio.objetos_valor import Ubicacion, Dimension
import PropiedadesdelosAlpes.modulos.propiedades.dominio.objetos_valor as ov

@dataclass
class Edificacion(Entidad, ABC):
    id: ov.IdentificadorPropiedad = field(default_factory=ov.IdentificadorPropiedad)
    dimensiones: Dimension = field(default_factory=Dimension)
    tipo: str  # Minorista, Oficina, Industrial, Especializado
    pisos: List[ov.Piso] = field(default_factory=list)

    @abstractmethod
    def agregar_piso(self, piso: ov.Piso):
        self.pisos.append(piso)

@dataclass
class Minorista(Edificacion):
    def agregar_piso(self, piso: ov.Piso):
        self.pisos.append(piso)
        # Specific minorista logic here

@dataclass
class Oficina(Edificacion):
    def agregar_piso(self, piso: ov.Piso):
        self.pisos.append(piso)
        # Specific oficina logic here

@dataclass
class Industrial(Edificacion):
    def agregar_piso(self, piso: ov.Piso):
        self.pisos.append(piso)
        # Specific industrial logic here

@dataclass
class Especializado(Edificacion):
    def agregar_piso(self, piso: ov.Piso):
        self.pisos.append(piso)
        # Specific especializado logic here

@dataclass
class Terreno(Entidad):
    id: ov.IdentificadorPropiedad = field(default_factory=ov.IdentificadorPropiedad)
    dimensiones: Dimension = field(default_factory=Dimension)
    lote: ov.Lote = field(default_factory=ov.Lote)

@dataclass
class Propiedad(AgregacionRaiz):
    id: ov.IdentificadorPropiedad = field(default_factory=ov.IdentificadorPropiedad)
    nombre: ov.Nombre = field(default_factory=ov.Nombre)
    ubicacion: Ubicacion = field(default_factory=Ubicacion)
    dimensiones: Dimension = field(default_factory=Dimension)
    tipo: ov.TipoPropiedad = field(default_factory=ov.TipoPropiedad)
    estado: ov.EstadoPropiedad = field(default_factory=ov.EstadoPropiedad)
    edificaciones: List[Edificacion] = field(default_factory=list)
    terreno: Terreno = field(default_factory=Terreno)

    def agregar_edificacion(self, edificacion: Edificacion):
        self.edificaciones.append(edificacion)
