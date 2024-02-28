from .....modulos.cliente.dominio.fabricas import FabricaCliente
from .....modulos.cliente.infraestructura.fabricas import FabricaRepositorio
from .....seedwork.aplicacion.comandos import ComandoHandler


class CrearClienteBaseHandler(ComandoHandler):
    def __init__(self):
        self._fabrica_repositorio: FabricaRepositorio = FabricaRepositorio()
        self._fabrica_propiedades: FabricaCliente = FabricaCliente()

    @property
    def fabrica_repositorio(self):
        return self._fabrica_repositorio

    @property
    def fabrica_cliente(self):
        return self._fabrica_cliente
