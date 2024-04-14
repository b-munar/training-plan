from sqlalchemy import Column, String, DateTime, Float
from sqlalchemy.orm import relationship
from src.database.base import Base
from datetime import datetime, timezone
from uuid import uuid4
from sqlalchemy.dialects.postgresql import UUID
from src.models.training_plan_model import TrainingDayExerciseModel

class ExerciseModel(Base):
    __tablename__ = 'exercise'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    name = Column(String(), nullable=False)
    description = Column(String(), nullable=False)
    timing_minutes = Column(Float(),nullable=False)
    image_url = Column(String(), nullable=False)
    muscular_group = Column(String(), nullable=False)
    training_day_exercise = relationship("TrainingDayExerciseModel")
    