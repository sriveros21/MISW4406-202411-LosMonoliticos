from PropiedadesdelosAlpes.seedwork.dominio.reglas import ReglaNegocio

from .objetos_valor import Nombre


class NombreValido(ReglaNegocio):
    nombre: Nombre

    def __init__(self, nombre, mensaje='El nombre debe tener al menos dos caracteres'):
        super().__init__(mensaje)
        self.nombre = nombre

    def es_valido(self) -> bool:
        if len(self.nombre) >= 2:
            return True
        else:
            return False
