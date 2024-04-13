from sqlalchemy import Column, String, DateTime, Float
from src.database.base import Base
from datetime import datetime, timezone
from uuid import uuid4
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.dialects.postgresql import ARRAY

class TraningPlanModel(Base):
    __tablename__ = 'training_plan'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    trainer = Column(UUID(as_uuid=True), nullable=False)
    user=Column(UUID(as_uuid=True), nullable=False)
    days_plan = Column(String(),nullable=False)
    
