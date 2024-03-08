import typing
import strawberry
import uuid
import requests
import os

from datetime import datetime

#Revisar esta configuracion
PROPIEDADESDELOSALPES_HOST = os.getenv("PROPIEDADESDELOSALPES_ADDRESS", default="localhost")
FORMATO_FECHA = '%Y-%m-%dT%H:%M:%SZ'


def obtener_auditorias(root) -> typing.List["Auditoria"]:
    auditorias_json = requests.get(f'http://{PROPIEDADESDELOSALPES_HOST}:5000/auditoria-query').json()
    auditorias = []

    for auditoria in auditorias_json:
        auditorias.append(
            Auditoria(
                id=auditoria.get('id'), 
                codigo=auditoria.get('dodigo'), 
                auditor=auditoria.get('auditor')
            )
        )

    return auditorias


@strawberry.type
class Auditoria:
    id: str
    codigo: str
    auditor:str

@strawberry.type
class AuditoriaRespuesta:
    mensaje: str
    codigo: int