from PropiedadesdelosAlpes.cliente.modulos.dominio.fabricas import FabricaCliente
from PropiedadesdelosAlpes.cliente.modulos.infraestructura.fabricas import FabricaRepositorioCliente
from PropiedadesdelosAlpes.cliente.seedwork.aplicacion.comandos import ComandoHandler


class CrearClienteBaseHandler(ComandoHandler):
    def __init__(self):
        self._fabrica_repositorio: FabricaRepositorioCliente = FabricaRepositorioCliente()
        self._fabrica_cliente: FabricaCliente = FabricaCliente()

    @property
    def fabrica_repositorio(self):
        return self._fabrica_repositorio

    @property
    def fabrica_cliente(self):
        return self._fabrica_cliente
