from PropiedadesdelosAlpes.seedwork.aplicacion.comandos import ComandoHandler
from PropiedadesdelosAlpes.propiedades.modulos.infraestructura.fabricas import FabricaRepositorio
from PropiedadesdelosAlpes.propiedades.modulos.dominio.fabricas import FabricaPropiedades

class CrearPropiedadBaseHandler(ComandoHandler):
    def __init__(self):
        self._fabrica_repositorio: FabricaRepositorio = FabricaRepositorio()
        self._fabrica_propiedades: FabricaPropiedades = FabricaPropiedades()

    @property
    def fabrica_repositorio(self):
        return self._fabrica_repositorio
    
    @property
    def fabrica_propiedades(self):
        return self._fabrica_propiedades
