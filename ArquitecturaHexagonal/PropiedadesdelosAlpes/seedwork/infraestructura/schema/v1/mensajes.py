import uuid
from datetime import datetime
from pulsar.schema import *
from ....infraestructura.utils import time_millis

class Mensaje(Record):
    id = String(default=str(uuid.uuid4()))
    time = Long()
    ingestion = Long(default=time_millis())
    specversion = String(default="1.0")
    type = String()
    datacontenttype = String(default="application/json")
    service_name = String()
