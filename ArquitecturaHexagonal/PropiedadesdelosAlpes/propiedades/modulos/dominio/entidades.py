from __future__ import annotations
from abc import ABC, abstractmethod

from dataclasses import dataclass, field
from enum import Enum
from typing import List
import uuid

from PropiedadesdelosAlpes.modulos.propiedades.dominio.eventos import EstadoPropiedadCambiado, PropiedadCreada

from ....seedwork.dominio.entidades import Entidad, AgregacionRaiz
from ....seedwork.dominio.objetos_valor import Ubicacion, Dimension
import PropiedadesdelosAlpes.modulos.propiedades.dominio.objetos_valor as ov

@dataclass
class TipoPropiedad(Enum):
    RESIDENCIAL = "Minorista"
    COMERCIAL = "Oficina"
    INDUSTRIAL = "Industrial"
    ESPECIALIZADO = "Especializado"
@dataclass
class Edificacion(Entidad, ABC):
    id: uuid.UUID = field(hash=True, default=None)
    dimension: Dimension = field(default_factory=Dimension)
    tipo: TipoPropiedad = field(default_factory=TipoPropiedad)
    pisos: List[ov.Piso] = field(default_factory=list)

@dataclass
class Terreno(Entidad):
    id: uuid.UUID = field(hash=True, default=None)
    dimension: Dimension = field(default_factory=Dimension)
    lote: str = field(default_factory=str)

@dataclass
class Propiedad(AgregacionRaiz):
    id: uuid.UUID = field(hash=True, default=None)
    nombre: ov.Nombre = field(default_factory=ov.Nombre)
    ubicacion: Ubicacion = field(default_factory=Ubicacion)
    dimension: Dimension = field(default_factory=Dimension)
    tipo: ov.TipoPropiedad = field(default_factory=ov.TipoPropiedad.COMERCIAL)
    estado: ov.EstadoPropiedad = field(default_factory=ov.EstadoPropiedad.DISPONIBLE)
    edificaciones: List[Edificacion] = field(default_factory=list)
    terreno: Terreno = field(default_factory=Terreno)

    def crear_propiedad(self, propiedad: Propiedad):
        self.id = propiedad.id
        self.nombre = propiedad.nombre
        self.ubicacion = propiedad.ubicacion
        self.dimension = propiedad.dimension
        self.tipo = propiedad.tipo
        self.estado = propiedad.estado
        self.edificaciones = propiedad.edificaciones
        self.terreno = propiedad.terreno

        #self.agregar_evento(PropiedadCreada(propiedad_id=self.id))
        self.agregar_evento(PropiedadCreada(id=self.id, nombre=self.nombre.valor, ubicacion=str(self.ubicacion), dimension=str(self.dimension), tipo=self.tipo.name, estado=self.estado.name, edificaciones=self.edificaciones, terreno=self.terreno))

    def cambiar_estado(self, nuevo_estado: ov.EstadoPropiedad):
        self.estado = nuevo_estado
        self.agregar_evento(EstadoPropiedadCambiado(propiedad_id=self.id, nuevo_estado=self.estado.valor))
