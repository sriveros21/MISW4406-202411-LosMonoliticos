from .objetos_valor import Nombre
from ....cliente.seedwork.dominio.reglas import ReglaNegocio


class NombreValido(ReglaNegocio):
    nombre: Nombre

    def __init__(self, nombre, mensaje='El nombre debe tener al menos dos caracteres'):
        super().__init__(mensaje)
        self.nombre = nombre

    def es_valido(self) -> bool:
        return True
