"""Excepciones del dominio de auditorias

En este archivo se encontrarán las excepciones del dominio de auditorias

"""


from ArquitecturaHexagonal.PropiedadesdelosAlpes.seedwork.dominio.excepciones import ExcepcionFabrica


class TipoObjetoNoExisteEnDominioAuditoriasExcepcion(ExcepcionFabrica):
    def __init__(self, mensaje='No existe una fábrica para el tipo solicitado en el módulo de auditorias'):
        self.__mensaje = mensaje

    def __str__(self):
        return str(self.__mensaje)