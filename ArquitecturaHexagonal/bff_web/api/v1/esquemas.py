import typing
import strawberry
import uuid
import requests
import os

from datetime import datetime


PROPIEDADESDELOSALPES_HOST = os.getenv("PROPIEDADESDELOSALPES_ADDRESS", default="localhost")
print(PROPIEDADESDELOSALPES_HOST)
FORMATO_FECHA = '%Y-%m-%dT%H:%M:%SZ'

def obtener_auditoria(root) -> typing.List["Auditoria"]:
    auditoria_json = requests.get(f'http://{PROPIEDADESDELOSALPES_HOST}:5000/auditorias/auditoria').json()
    print("SOY JSON AUDITORIA", auditoria_json)
    auditorias = [
        Auditoria(
            fecha_creacion=datetime.strptime(a['fecha_creacion'], FORMATO_FECHA), 
            fecha_actualizacion=datetime.strptime(a['fecha_actualizacion'], FORMATO_FECHA), 
            id=a['id'],
            id_auditoria=a['id_auditoria']
        ) for a in auditoria_json
    ]
    return auditorias

@strawberry.type
class Auditoria:
    id: str
    id_auditoria: str
    fecha_creacion: datetime
    fecha_actualizacion: datetime


@strawberry.type
class AuditoriaRespuesta:
    mensaje: str
    codigo: int