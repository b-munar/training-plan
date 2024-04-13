from src.database.base import Base
from src.database.engine import engine

from src.models.exercise_model import ExerciseModel

table_objects = [ExerciseModel.__table__]

if __name__ == "__main__":
    Base.metadata.create_all(
        bind = engine(), 
        tables=table_objects,
        checkfirst=True
    )