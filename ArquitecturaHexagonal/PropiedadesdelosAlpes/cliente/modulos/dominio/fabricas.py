from dataclasses import dataclass

from PropiedadesdelosAlpes.cliente.seedwork.dominio.eventos import EventoDominio
from PropiedadesdelosAlpes.cliente.seedwork.dominio.fabricas import Fabrica
from PropiedadesdelosAlpes.cliente.seedwork.dominio.repositorios import Mapeador

from .entidades import Cliente, Entidad
from .excepciones import TipoObjetoNoExisteEnDominioClienteExcepcion


@dataclass
class _FabricaCliente(Fabrica):

    def crear_objeto(self, obj: any, mapeador: Mapeador) -> any:
        if isinstance(obj, Entidad) or isinstance(obj, EventoDominio):
            return mapeador.entidad_a_dto(obj)
        else:
            cliente: Cliente = mapeador.dto_a_entidad(obj)
            return cliente


@dataclass
class FabricaCliente(Fabrica):

    def crear_objeto(self, obj: any, mapeador: Mapeador) -> any:
        if mapeador.obtener_tipo() == Cliente.__class__:
            fabrica_cliente = _FabricaCliente()
            return fabrica_cliente.crear_objeto(obj, mapeador)
        else:
            raise TipoObjetoNoExisteEnDominioClienteExcepcion()
