import strawberry
import typing

from strawberry.types import Info
from bff_web import utils
from bff_web.despachadores import Despachador

from .esquemas import *

@strawberry.type
class Mutation:

#Rev id correlacion
    # TODO Agregue objeto de itinerarios o reserva
    @strawberry.mutation
    async def crear_auditoria(self, id: str, id_correlacion: str, info: Info) -> AuditoriaRespuesta:
        print(f"ID : {id}, ID Correlación: {id_correlacion}")
        payload = dict(
            id = id,
            id_correlacion = id_correlacion,
        )
        comando = dict(
            id = str(uuid.uuid4()),
            time=utils.time_millis(),
            specversion = "v1",
            type = "ComandoAuditoria",
            ingestion=utils.time_millis(),
            datacontenttype="AVRO",
            service_name = "BFF Web",
            data = payload
        )
        despachador = Despachador()
        info.context["background_tasks"].add_task(despachador.publicar_mensaje, comando, "comando-crear-auditoria", "public/default/comando-crear-auditoria")
        
        return AuditoriaRespuesta(mensaje="Procesando Mensaje", codigo=203)