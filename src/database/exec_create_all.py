from src.database.base import Base
from src.database.engine import engine

from src.models.exercise_model import ExerciseModel
from src.models.training_plan_model import TrainingDayExerciseModel, TrainingDayModel, TraningPlanModel

table_objects = [ExerciseModel.__table__,TrainingDayExerciseModel.__table__,TrainingDayModel.__table__,TraningPlanModel.__table__]

if __name__ == "__main__":
    Base.metadata.create_all(
        bind = engine(), 
        tables=table_objects,
        checkfirst=True
    )