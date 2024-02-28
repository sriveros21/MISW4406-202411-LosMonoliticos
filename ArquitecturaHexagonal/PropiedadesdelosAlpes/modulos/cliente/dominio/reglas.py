from PropiedadesdelosAlpes.seedwork.dominio.objetos_valor import NombreCompleto
from PropiedadesdelosAlpes.seedwork.dominio.reglas import ReglaNegocio


class NombreValido(ReglaNegocio):
    nombreCompleto: NombreCompleto

    def __init__(self, nombreCompleto, mensaje='El nombre debe tener al menos dos caracteres'):
        super().__init__(mensaje)
        self.nombre = nombreCompleto

    def es_valido(self) -> bool:
        return True
