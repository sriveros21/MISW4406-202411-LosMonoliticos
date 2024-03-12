from PropiedadesdelosAlpes.cliente.config.db import db
from PropiedadesdelosAlpes.cliente.modulos.dominio.entidades import Cliente
from PropiedadesdelosAlpes.cliente.seedwork.infraestructura.vistas import Vista

from .dto import Cliente as ClienteDTO


class VistaCliente(Vista):
    def obtener_por(id=None, estado=None, id_cliente=None, **kwargs) -> [Cliente]:  # type: ignore
        params = dict()

        if id:
            params['id'] = str(id)

        return db.session.query(ClienteDTO).filter_by(**params)
