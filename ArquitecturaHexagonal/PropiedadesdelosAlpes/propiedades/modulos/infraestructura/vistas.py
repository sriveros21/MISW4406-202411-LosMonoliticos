from PropiedadesdelosAlpes.propiedades.seedwork.infraestructura.vistas import Vista
from PropiedadesdelosAlpes.propiedades.modulos.dominio.entidades import Propiedad
from PropiedadesdelosAlpes.propiedades.config.db import db
from .dto import Propiedad as PropiedadDTO

class VistaPropiedad(Vista):
    def obtener_por(id=None, estado=None, id_cliente=None, **kwargs) -> [Propiedad]: # type: ignore
        params = dict()

        if id:
            params['id'] = str(id)
            
        return db.session.query(PropiedadDTO).filter_by(**params)