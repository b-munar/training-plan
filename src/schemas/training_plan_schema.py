from marshmallow import Schema, fields


class TraningDaySerializedSchema(Schema):
    id= fields.UUID()
    day = fields.String()
    exercises = fields.List(fields.Nested())

class TraniningPlanSerializeSchema(Schema):
    id = fields.UUID()
    trainer = fields.String()
    days_plan= fields.List(fields.Nested(TraningDaySerializedSchema))
    
class TraningDayDeserializedSchema(Schema):
    day = fields.String()
    exercises = fields.List(fields.String())
    
class TrainingPlanDeserializeSchema(Schema):
    id = fields.UUID()
    name = fields.String()
    trainer = fields.String()
    days_plan= fields.List(fields.Nested(TraningDayDeserializedSchema))