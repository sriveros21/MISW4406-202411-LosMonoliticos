from __future__ import annotations
from dataclasses import dataclass, field
from typing import List
import uuid

#from PropiedadesdelosAlpes.modulos.propiedades.dominio.entidades import Edificacion, Terreno
from ....seedwork.dominio.eventos import (EventoDominio)
import PropiedadesdelosAlpes.modulos.propiedades.dominio.objetos_valor as ov
import PropiedadesdelosAlpes.seedwork.dominio.objetos_valor as ovSeedwork
@dataclass
class PropiedadCreada(EventoDominio):
    id: uuid.UUID = None
    nombre: str = None
    ubicacion: ovSeedwork.Ubicacion = None
    dimension: ovSeedwork.Dimension = None
    tipo: ov.TipoPropiedad = None
    estado: ov.EstadoPropiedad = None
    edificaciones: List[str] = None
    terreno: str = None
    
@dataclass
class EstadoPropiedadCambiado(EventoDominio):
    id: uuid.UUID = None
    nuevo_estado: ov.EstadoPropiedad = None