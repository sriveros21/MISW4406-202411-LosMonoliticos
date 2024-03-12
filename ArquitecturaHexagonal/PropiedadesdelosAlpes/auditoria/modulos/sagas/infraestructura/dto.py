from sqlalchemy import create_engine, Column, Integer, String, Text, DateTime, func
from sqlalchemy.orm import sessionmaker
import uuid
from PropiedadesdelosAlpes.auditoria.config.db import db

class SagaLog(db.Model):
    __tablename__ = 'saga_logs'
    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    saga_id = Column(String(36), nullable=False, index=True)
    paso_index = Column(Integer, nullable=False)
    estado = Column(Text, nullable=False)
    timestamp = Column(DateTime, default=func.now())