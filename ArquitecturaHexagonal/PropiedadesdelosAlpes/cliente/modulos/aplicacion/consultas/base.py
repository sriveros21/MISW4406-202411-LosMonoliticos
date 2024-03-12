from PropiedadesdelosAlpes.cliente.modulos.dominio.fabricas import FabricaCliente
from PropiedadesdelosAlpes.cliente.modulos.infraestructura.fabricas import FabricaVista
from PropiedadesdelosAlpes.cliente.seedwork.aplicacion.queries import QueryHandler


class ClienteQueryBaseHandler(QueryHandler):
    def __init__(self):
        self._fabrica_vista: FabricaVista = FabricaVista()
        self._fabrica_cliente: FabricaCliente = FabricaCliente()

    @property
    def fabrica_vista(self):
        return self._fabrica_vista

    @property
    def fabrica_cliente(self):
        return self._fabrica_cliente
