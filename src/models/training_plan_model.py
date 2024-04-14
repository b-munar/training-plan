from sqlalchemy import Column, String, DateTime, Float, ForeignKey
from src.database.base import Base
from sqlalchemy.orm import relationship
from datetime import datetime, timezone
from uuid import uuid4
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.dialects.postgresql import ARRAY

class TrainingDayExerciseModel(Base):
    __tablename__ = 'training_day_exercise'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    traning_day_id = Column(UUID(as_uuid=True),ForeignKey("training_day.id"))
    exercise_id = Column(UUID(as_uuid=True),ForeignKey("exercise.id"))
    
class TrainingDayModel(Base):
    __tablename__ = 'training_day'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    training_plan_id = Column(UUID(as_uuid=True),ForeignKey("training_plan.id"))
    day= Column(String(), nullable=False)
    exercises = relationship("TrainingDayExerciseModel")
    
class TraningPlanModel(Base):
    __tablename__ = 'training_plan'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    trainer = Column(UUID(as_uuid=True), nullable=False)
    user=Column(UUID(as_uuid=True), nullable=False)
    days = relationship("TrainingDayModel")
    

