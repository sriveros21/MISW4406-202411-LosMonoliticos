import pulsar
from pulsar.schema import *

from ArquitecturaHexagonal.PropiedadesdelosAlpes.modulos.propiedades.infraestructura.schema.v1.eventos import PropiedadCreada, PropiedadCreadaPayload
from ArquitecturaHexagonal.PropiedadesdelosAlpes.modulos.propiedades.infraestructura.schema.v1.comandos import ComandoCrearPropiedad, ComandoCrearPropiedadPayload
from ArquitecturaHexagonal.PropiedadesdelosAlpes.seedwork.infraestructura import utils

import datetime

epoch = datetime.datetime.utcfromtimestamp(0)

def unix_time_millis(dt):
    return (dt - epoch).total_seconds() * 1000.0

class Despachador:
    def _publicar_mensaje(self, mensaje, topico, schema):
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        publicador = cliente.create_producer(topico, schema=AvroSchema(schema))
        publicador.send(mensaje)
        cliente.close()

    def publicar_evento(self, evento, topico):
        payload = PropiedadCreadaPayload(
            id_propiedad=str(evento.propiedad_id),
            nombre=evento.nombre,
            ubicacion=evento.ubicacion,
            fecha_creacion=int(unix_time_millis(evento.fecha_evento))
        )
        evento_integracion = PropiedadCreada(data=payload)
        self._publicar_mensaje(evento_integracion, topico, PropiedadCreada)

    def publicar_comando(self, comando, topico):
        payload = ComandoCrearPropiedadPayload(
            id_usuario=str(comando.id_usuario)
        )
        comando_integracion = ComandoCrearPropiedad(data=payload)
        self._publicar_mensaje(comando_integracion, topico, ComandoCrearPropiedad)