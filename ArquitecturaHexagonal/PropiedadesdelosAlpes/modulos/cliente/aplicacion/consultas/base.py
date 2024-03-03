from PropiedadesdelosAlpes.modulos.cliente.dominio.fabricas import FabricaCliente
from PropiedadesdelosAlpes.modulos.cliente.infraestructura.fabricas import FabricaRepositorio
from PropiedadesdelosAlpes.seedwork.aplicacion.queries import QueryHandler


class ClienteQueryBaseHandler(QueryHandler):
    def __init__(self):
        self._fabrica_repositorio: FabricaRepositorio = FabricaRepositorio()
        self._fabrica_cliente: FabricaCliente = FabricaCliente()

    @property
    def fabrica_repositorio(self):
        return self._fabrica_repositorio

    @property
    def fabrica_cliente(self):
        return self._fabrica_cliente
