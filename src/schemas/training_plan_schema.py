from marshmallow import Schema, fields

from src.schemas.exercise_schema import ExerciseDeserializeSchema , ExerciseSerializeSchema

class TraningDaySerializedSchema(Schema):
    id= fields.UUID()
    day = fields.String()
    exercises = fields.List(fields.Nested(ExerciseSerializeSchema))

class TraniningPlanSerializeSchema(Schema):
    id = fields.UUID()
    name = fields.String()
    trainer = fields.String()
    days_plan= fields.List(fields.Nested(TraningDaySerializedSchema))
    
class TraningDayDeserializedSchema(Schema):
    id= fields.UUID()
    day = fields.String()
    exercises = fields.List(fields.Nested(ExerciseDeserializeSchema))
    
class TrainingPlanDeserializeSchema(Schema):
    id = fields.UUID()
    name = fields.String()
    trainer = fields.String()
    days_plan= fields.List(fields.Nested(TraningDayDeserializedSchema))