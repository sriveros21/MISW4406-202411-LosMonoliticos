import strawberry
import typing

from strawberry.types import Info
from bff_web import utils
from bff_web.despachadores import Despachador

from .esquemas import *

@strawberry.type
class Mutation:

    @strawberry.mutation
    async def crear_auditoria(self, id_auditoria: str, id_correlacion: str, info: Info) -> AuditoriaRespuesta:
        print(f"ID Auditoria: {id_auditoria}, ID Correlación: {id_correlacion}")
        payload = dict(
            id_auditoria = id_auditoria,
            id_correlacion = id_correlacion,
            fecha_creacion = utils.time_millis()
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
        
        return ReservaRespuesta(mensaje="Procesando Mensaje", codigo=203)