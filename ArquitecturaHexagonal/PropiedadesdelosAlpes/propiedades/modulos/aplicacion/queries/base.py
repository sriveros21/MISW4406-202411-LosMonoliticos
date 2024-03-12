from PropiedadesdelosAlpes.seedwork.aplicacion.queries import QueryHandler
from PropiedadesdelosAlpes.propiedades.modulos.infraestructura.fabricas import FabricaVista
from PropiedadesdelosAlpes.propiedades.modulos.dominio.fabricas import FabricaPropiedades

class PropiedadQueryBaseHandler(QueryHandler):
    def __init__(self):
        self._fabrica_vista: FabricaVista = FabricaVista()
        self._fabrica_propiedades: FabricaPropiedades = FabricaPropiedades()

    @property
    def fabrica_vista(self):
        return self._fabrica_vista
    
    @property
    def fabrica_propiedades(self):
        return self._fabrica_propiedades
