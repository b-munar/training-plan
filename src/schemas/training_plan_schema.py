from marshmallow import Schema, fields

class ExerciseDeserializedSchema(Schema):
    id = fields.UUID()

class TraningDayDeserializedSchema(Schema):
    day = fields.String()
    exercises = fields.List(fields.Nested(ExerciseDeserializedSchema))
    
class TrainingPlanDeserializedSchema(Schema):
    trainer = fields.UUID()
    user = fields.UUID()
    days= fields.List(fields.Nested(TraningDayDeserializedSchema))
    
class ExerciseSerializedSchema(Schema):
    id = fields.UUID()

class TraningDaySerializedSchema(Schema):
    day = fields.String()
    exercises = fields.List(fields.Nested(ExerciseDeserializedSchema))
    
class TrainingPlanSerializedSchema(Schema):
    trainer = fields.UUID()
    user = fields.UUID()
    days= fields.List(fields.Nested(TraningDayDeserializedSchema))