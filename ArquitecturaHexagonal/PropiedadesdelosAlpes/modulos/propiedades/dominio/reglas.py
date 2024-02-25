from ArquitecturaHexagonal.PropiedadesdelosAlpes.seedwork.dominio.reglas import ReglaNegocio
from .objetos_valor import Ubicacion, Propiedad, Dimensiones
from datetime import datetime

class UbicacionValida(ReglaNegocio):
    ubicacion: Ubicacion

    def __init__(self, ubicacion, mensaje='La ubicación propuesta es incorrecta'):
        super().__init__(mensaje)
        self.ubicacion = ubicacion

    def es_valido(self) -> bool:
        # Lógica para validar la ubicación
        return True

class MinimoUnaPropiedad(ReglaNegocio):
    propiedades: 'list[Propiedad]'

    def __init__(self, propiedades, mensaje='Debe haber al menos una propiedad disponible'):
        super().__init__(mensaje)
        self.propiedades = propiedades

    def es_valido(self) -> bool:
        return len(self.propiedades) > 0
    
class ReglaDimensionesValidas(ReglaNegocio):
    def __init__(self, dimensiones: Dimensiones, mensaje='Las dimensiones propuestas son incorrectas'):
        super().__init__(mensaje)
        self.dimensiones = dimensiones

    def es_valido(self) -> bool:
        # Logica para validar dimensiones
        return True
