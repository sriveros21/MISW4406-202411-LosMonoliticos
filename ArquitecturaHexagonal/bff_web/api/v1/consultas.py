
import strawberry
from .esquemas import *

@strawberry.type
class Query:
    auditorias: typing.List[Auditoria] = strawberry.field(resolver=obtener_auditoria)