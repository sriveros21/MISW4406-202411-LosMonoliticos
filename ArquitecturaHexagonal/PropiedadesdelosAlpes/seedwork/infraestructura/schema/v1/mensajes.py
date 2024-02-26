import uuid
from datetime import datetime
from pulsar.schema import *

def time_millis():
    return int(datetime.now().timestamp() * 1000)

class Mensaje(Record):
    id = String(default=str(uuid.uuid4()))
    time = Long(default=time_millis())
    ingestion = Long(default=time_millis())
    specversion = String(default="1.0")
    type = String()
    datacontenttype = String(default="application/json")
    service_name = String()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.time = time_millis()
        self.ingestion = time_millis()
